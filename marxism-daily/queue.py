#!/usr/bin/env python3
"""The Daily Marxism delivery queue: what goes out next, and where we stopped.

Delivery is cursor-based, not calendar-based. `state.json` records the last item
that actually went out (`delivery.last_sent`). The queue is every lesson and quiz
written so far, in course order. The next item is simply the one after the cursor.
A pause of any length therefore never skips a lesson and never repeats one: the
course continues from the exact point where it stopped.

Dates still carry the weekly rhythm: lessons go Monday to Saturday, the quiz goes
on Sunday. Every item keeps its `send_date`, and the sender delivers an item only
once that date has arrived. `resume` re-dates everything still unsent, starting
from the day you resume, so the rhythm survives a pause of any length.

Usage, from the repository root:

  queue.py next               the item to send today, as JSON
  queue.py status             human summary: paused or running, what is next
  queue.py pause              stop delivery, keep the cursor where it is
  queue.py resume [--on DATE] restart delivery and re-date everything unsent
                              (add --dry-run to see the new calendar first)
  queue.py advance KEY        record that item KEY went out (KEY comes from `next`)

`next` prints one JSON object. The sender reads its "action" field:

  "send"    deliver this item now; "kind" is "lesson" or "quiz"
  "wait"    the next item is not due yet ("send_date" says when)
  "paused"  the course is paused; send nothing
  "empty"   the queue ran out; the weekly writer has to write the next batch
"""
import datetime as dt
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(ROOT, 'state.json')
LESSONS = os.path.join(ROOT, 'lessons')
QUIZZES = os.path.join(ROOT, 'quizzes')

SUNDAY = 6  # datetime.weekday() value


def read_state():
    with open(STATE, encoding='utf-8') as f:
        state = json.load(f)
    state.setdefault('delivery', {})
    state['delivery'].setdefault('paused', False)
    state['delivery'].setdefault('last_sent', None)
    return state


def write_state(state):
    with open(STATE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
        f.write('\n')


def front_matter(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    m = re.match(r'---\n(.*?)\n---\n', raw, re.S)
    if not m:
        sys.exit(f'{path}: missing front matter')
    return dict(re.findall(r'(\w+):\s*"?(.*?)"?\s*$', m.group(1), re.M))


def parse_date(s):
    return dt.date.fromisoformat(s)


def build_queue():
    """Every lesson and quiz in course order, each as a queue item.

    A quiz sits directly after the last lesson it covers, which is where it
    belongs in the course and where the Sunday slot puts it.
    """
    items = []
    for week in sorted(os.listdir(LESSONS)):
        week_dir = os.path.join(LESSONS, week)
        if not os.path.isdir(week_dir):
            continue
        for name in sorted(os.listdir(week_dir)):
            m = re.fullmatch(r'day(\d+)\.md', name)
            if not m:
                continue
            path = os.path.join(week_dir, name)
            day = int(m.group(1))
            meta = front_matter(path)
            items.append({
                'key': f'day{day:02d}',
                'kind': 'lesson',
                'day': day,
                'order': (day, 0),
                'path': os.path.relpath(path, os.path.dirname(ROOT)),
                'send_date': meta.get('send_date', ''),
                'subject': meta.get('subject', ''),
                'subject_pt': meta.get('subject_pt', ''),
            })

    for name in sorted(os.listdir(QUIZZES)):
        m = re.fullmatch(r'quiz(\d+)\.json', name)
        if not m:
            continue
        path = os.path.join(QUIZZES, name)
        with open(path, encoding='utf-8') as f:
            meta = json.load(f)
        last_day = int(str(meta['covers_days']).split('-')[-1])
        items.append({
            'key': f'quiz{int(m.group(1)):02d}',
            'kind': 'quiz',
            'quiz': meta['quiz'],
            'order': (last_day, 1),
            'path': os.path.relpath(path, os.path.dirname(ROOT)),
            'meta_file': os.path.relpath(path, os.path.dirname(ROOT)),
            'send_date': meta.get('send_date', ''),
            'subject': meta.get('subject', ''),
            'subject_pt': meta.get('subject_pt', ''),
            'covers_days': meta.get('covers_days', ''),
        })

    items.sort(key=lambda i: i['order'])
    for item in items:
        item.pop('order')
    return items


def split_at_cursor(items, last_sent):
    """Return (already sent, still to send) around the cursor."""
    if not last_sent:
        return [], items
    for index, item in enumerate(items):
        if item['key'] == last_sent:
            return items[:index + 1], items[index + 1:]
    sys.exit(f'state.json: delivery.last_sent "{last_sent}" is not in the queue')


def next_item(state, items, today):
    pending = split_at_cursor(items, state['delivery']['last_sent'])[1]
    if state['delivery']['paused']:
        out = {'action': 'paused',
               'paused_on': state['delivery'].get('paused_on', ''),
               'last_sent': state['delivery']['last_sent']}
        if pending:
            out['next_key'] = pending[0]['key']
        return out
    if not pending:
        return {'action': 'empty', 'last_sent': state['delivery']['last_sent']}
    item = dict(pending[0])
    item['action'] = 'send' if parse_date(item['send_date']) <= today else 'wait'
    return item


def set_lesson_date(path, date):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    new, count = re.subn(r'^send_date:.*$', f'send_date: {date.isoformat()}',
                         raw, count=1, flags=re.M)
    if not count:
        sys.exit(f'{path}: no send_date line to update')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new)


def set_quiz_dates(path, date, covered):
    """Write the quiz send_date, and the dates of the lessons it covers."""
    with open(path, encoding='utf-8') as f:
        meta = json.load(f)
    meta['send_date'] = date.isoformat()
    if covered:
        first, last = covered[0], covered[-1]
        meta['covers_dates'] = f'{first.isoformat()} to {last.isoformat()}'
        meta['covers_dates_pt'] = (f'{first.strftime("%d/%m")} a '
                                   f'{last.strftime("%d/%m/%Y")}')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)
        f.write('\n')


def replan(pending, start):
    """Give every unsent item a new date from `start` on.

    A lesson takes the next day that is not a Sunday. A quiz takes the next
    Sunday. That keeps the six-lessons-then-quiz shape whatever weekday the
    course resumes on.
    """
    plan = []
    date = start
    for item in pending:
        if item['kind'] == 'quiz':
            while date.weekday() != SUNDAY:
                date += dt.timedelta(days=1)
        else:
            while date.weekday() == SUNDAY:
                date += dt.timedelta(days=1)
        plan.append((item, date))
        date += dt.timedelta(days=1)
    return plan


def apply_plan(plan, items, repo_root):
    """Write the new dates into the lesson and quiz files.

    A quiz can cover lessons on both sides of the pause: some already sent in
    the old calendar, some re-dated to the new one. So the covered range is
    built from every lesson in the course, and only the re-dated ones move.
    """
    lesson_dates = {i['day']: parse_date(i['send_date'])
                    for i in items if i['kind'] == 'lesson'}
    for item, date in plan:
        if item['kind'] == 'lesson':
            lesson_dates[item['day']] = date
    for item, date in plan:
        path = os.path.join(repo_root, item['path'])
        if item['kind'] == 'lesson':
            set_lesson_date(path, date)
        else:
            bounds = [int(d) for d in str(item['covers_days']).split('-')]
            first, last = bounds[0], bounds[-1]
            covered = [lesson_dates[d] for d in range(first, last + 1)
                       if d in lesson_dates]
            set_quiz_dates(path, date, covered)


def cmd_next(state, items, today):
    print(json.dumps(next_item(state, items, today), ensure_ascii=False))


def cmd_status(state, items, today):
    sent, pending = split_at_cursor(items, state['delivery']['last_sent'])
    if state['delivery']['paused']:
        since = state['delivery'].get('paused_on', 'an unrecorded date')
        print(f'PAUSED since {since}. Nothing is being sent.')
    else:
        print('RUNNING.')
    print(f'Delivered: {len(sent)} items, last was '
          f'{state["delivery"]["last_sent"] or "none yet"}.')
    if not pending:
        print('Nothing left in the queue. The weekly writer has to write more.')
        return
    print(f'Still to send: {len(pending)} items, next is {pending[0]["key"]} '
          f'("{pending[0]["subject"]}", dated {pending[0]["send_date"]}).')
    if state['delivery']['paused']:
        print(f'On resume it goes out first. Run: '
              f'python3 marxism-daily/queue.py resume')
    else:
        due = parse_date(pending[0]['send_date'])
        print('Due today.' if due <= today else f'Not due until {due}.')


def cmd_pause(state, items, today):
    if state['delivery']['paused']:
        print('Already paused. Nothing changed.')
        return
    state['delivery']['paused'] = True
    state['delivery']['paused_on'] = today.isoformat()
    write_state(state)
    pending = split_at_cursor(items, state['delivery']['last_sent'])[1]
    nxt = pending[0]['key'] if pending else 'nothing left in the queue'
    print(f'Paused on {today}. Next on resume: {nxt}.')
    print('Also disable the two Daily Marxism Routines, or they wake up daily '
          'to do nothing.')


def cmd_resume(state, items, today, start, dry_run):
    pending = split_at_cursor(items, state['delivery']['last_sent'])[1]
    if not pending:
        print('Nothing left in the queue. Resuming would send nothing.')
        return
    plan = replan(pending, start)
    print(f'{"Would re-date" if dry_run else "Re-dated"} {len(plan)} items:')
    for item, date in plan:
        print(f'  {item["key"]:>8}  {date}  {date.strftime("%a")}  '
              f'{item["subject"]}')
    if dry_run:
        return
    apply_plan(plan, items, os.path.dirname(ROOT))
    state['delivery']['paused'] = False
    state['delivery']['resumed_on'] = today.isoformat()
    state['delivery'].pop('paused_on', None)
    # The writer's calendar has to follow the new dates: its next quiz goes out
    # on the Sunday after everything already written, and the batch of lessons
    # it writes starts on the Monday after that quiz.
    sunday = plan[-1][1] + dt.timedelta(days=1)
    while sunday.weekday() != SUNDAY:
        sunday += dt.timedelta(days=1)
    state['next_quiz_send_date'] = sunday.isoformat()
    state['next_batch_first_send_date'] = (sunday + dt.timedelta(days=1)).isoformat()
    write_state(state)
    print(f'\nResumed. {plan[0][0]["key"]} goes out on {plan[0][1]}.')
    print('Now re-enable the two Daily Marxism Routines.')


def cmd_advance(state, items, today, key):
    keys = [i['key'] for i in items]
    if key not in keys:
        sys.exit(f'"{key}" is not in the queue. Known keys: {", ".join(keys)}')
    state['delivery']['last_sent'] = key
    state['delivery']['last_sent_on'] = today.isoformat()
    write_state(state)
    print(f'Cursor moved to {key} (sent {today}).')


def main(argv):
    if not argv:
        sys.exit(__doc__)
    command = argv[0]
    today = dt.date.today()
    if '--today' in argv:  # for testing the calendar without waiting
        today = parse_date(argv[argv.index('--today') + 1])
    state = read_state()
    items = build_queue()

    if command == 'next':
        cmd_next(state, items, today)
    elif command == 'status':
        cmd_status(state, items, today)
    elif command == 'pause':
        cmd_pause(state, items, today)
    elif command == 'resume':
        start = today
        if '--on' in argv:
            start = parse_date(argv[argv.index('--on') + 1])
        cmd_resume(state, items, today, start, '--dry-run' in argv)
    elif command == 'advance':
        if len(argv) < 2:
            sys.exit('advance needs a key, for example: advance day18')
        cmd_advance(state, items, today, argv[1])
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
