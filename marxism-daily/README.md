# Daily Marxism — system

Automated daily email course. See `PROGRAM.md` for syllabus, voice, and email format.

## Branch

Since 2026-09-02 the program lives on branch `claude/daily-programs` (before: `claude/daily-programs`). Both Routines read from and push to the new branch.

## How it works (v2 transport, since 2026-08-28; Sunday quiz since 2026-09-02; send protocol since 2026-09-10)

Sending migrated from Resend to Inkbox on 2026-08-28. Resend is retired: nothing is scheduled there and no Routine touches it anymore.

Both Routines start a fresh cloud session on every run (no memory between runs). Their prompts are stored in the Routines and copied in `routines/` (see `routines/README.md` for the trigger ids and how to update them).

- **Weekly writer** (Thursdays 12:00 UTC):
  1. Checks out branch `claude/daily-programs` of `adeoo/pipedream` and attaches the repo with push access (`add_repo`).
  2. Reads `PROGRAM.md` (v2), `state.json`, and the previous week's lessons for continuity.
  3. Writes one batch: the quiz for the coming Sunday (`quizzes/quizNN.html`, `quizNN.pt.html`, `quizNN.json`, built with the `test-workbook` skill) plus the next week's 6 bilingual lessons, Monday to Saturday, as `lessons/weekNN/dayNN.md` (front matter: `subject`, `subject_pt`, `send_date`; English lesson, then `=== PT-BR ===`, then the Portuguese version). A `transition` field in `state.json` overrides this for one batch.
  4. Verifies each lesson renders with `render.py`, updates `state.json`, commits, pushes. It does NOT send or schedule email.
- **Daily send** (daily 09:00 UTC = 06:00 América/São Paulo; the Routine holds the Inkbox connector):
  1. Asks `python3 marxism-daily/queue.py next` what to send. The queue answers with the item after the delivery cursor: a lesson, a quiz, or `paused` / `wait` / `empty`, in which case the run sends nothing. The sender never picks an item from the weekday itself. See "Pausing and resuming" below.
  2. Lessons: `python3 marxism-daily/render.py <file> --write /tmp/send` writes six ready-to-send files (`en.subject.txt`, `en.html`, `en.txt`, `pt.*`). The Routine copies each file verbatim into the matching `inkbox_email_send` parameter and sends from `adeosagent@inkboxmail.com`: English to `moussaadel97@gmail.com`, PT-BR to `ana.ruberrime@gmail.com`. Quiz: a short STE body with the HTML file as an attachment (English file to Moussa, PT-BR file to Carol). The quiz is never pasted into the body: mail clients remove scripts.
  3. Idempotent twice over: the cursor in `state.json` only moves once an item has gone out (`queue.py advance`, committed and pushed), and before sending it also checks Inkbox sent mail and only sends whichever language version is missing.
  4. **Send protocol.** After every send it reads the sent message back with `inkbox_email_get` and checks that `body_html` starts with `<div style=` and `body_text` starts with the subject. If the check fails it sends at most one "Corrected copy: ..." and reports the failure in its status line. No test or placeholder emails, ever.

Why the protocol exists: between 2026-09-04 and 2026-09-09 the fresh-session runs retyped the email body by hand into the Inkbox tool call and sometimes escaped the HTML (`<` became `&lt;`), sent placeholder bodies, or put a shell command in the body. Readers got two or three copies per day, some unreadable. The `--write` files plus the read-back check remove the retyping and catch what slips through. `render.py` also produces much smaller HTML now (one styled wrapper, bare `<p>` tags), so there is less to copy.

There is no pre-scheduled queue anymore: each morning's Routine run is the send. This replaced Resend's `scheduledAt` queue, whose scheduled sends failed at fire time 6 times out of 7 in week 1 of v1 and were rescued by a separate check routine (see log below, kept as history).

- **Retired** (disabled, kept for history): v1 writer Routine `trig_01MjchH1dTpTJgZJSttVwct9` and v1 delivery-check Routine `trig_016cewnP9Tnrd14sQNZa2W9x`, both bound to the founding session and Resend-based.

### v1 delivery log (course later reset; kept as transport history)
| Day | Date | Scheduled send | Outcome |
|---|---|---|---|
| 1 | 2026-08-22 | failed | re-sent by hand, delivered |
| 2 | 2026-08-23 | failed | re-sent by check routine, delivered |
| 3 | 2026-08-24 | delivered | no action needed |
| 4 | 2026-08-25 | failed | re-sent by check routine, delivered |
| 5 | 2026-08-26 | failed | re-sent by check routine, delivered |
| 6 | 2026-08-27 | failed | re-sent by check routine, delivered |
| 7 | 2026-08-28 | failed | re-sent by check routine, delivered |

## Pausing and resuming

**The course is paused.** It stopped on 2026-09-17, before that morning's send. Day 17
(2026-09-16) was the last email delivered. Day 18 is the first one on resume.

Delivery is **cursor-based**, not calendar-based. `state.json` → `delivery.last_sent`
records the last item that actually went out, and `queue.py` hands the sender the item
after it. A pause therefore never skips a lesson and never repeats one, whatever its
length: the course continues from the exact point where it stopped.

Dates still carry the weekly rhythm (lessons Monday to Saturday, quiz on Sunday), so
`resume` re-dates every unsent lesson and quiz from the day you resume. If that day is
mid-week, the first stretch is short and the rhythm snaps back to Monday-to-Sunday by
itself.

### To resume

```
git fetch origin claude/daily-programs && git checkout claude/daily-programs
python3 marxism-daily/queue.py resume --dry-run   # see the new calendar first
python3 marxism-daily/queue.py resume             # write it
git commit -am "Daily Marxism: resume" && git push -u origin claude/daily-programs
```

Then re-enable both Routines (`update_trigger` with `enabled=true`, ids in
`routines/README.md`). The first email goes out the next morning at 06:00 São Paulo.

Note: only three lessons are written (days 18, 19, 20). The weekly writer fires on the
first Thursday after you re-enable it and writes the next batch.

### To pause again

```
python3 marxism-daily/queue.py pause
git commit -am "Daily Marxism: pause" && git push -u origin claude/daily-programs
```

Then disable both Routines. Disabling them alone is enough to stop the email; the
`paused` flag is the belt to that pair of braces, and it is what makes a later `resume`
re-date the remaining lessons instead of leaving them stranded in the past.

### Commands

| Command | What it does |
|---|---|
| `queue.py status` | paused or running, what went out, what is next |
| `queue.py next` | the item due today, as JSON; what the sender reads |
| `queue.py pause` | stop delivery, keep the cursor |
| `queue.py resume` | restart and re-date everything unsent (`--dry-run`, `--on DATE`) |
| `queue.py advance KEY` | record that an item went out; the sender calls this |

Carol Daily (`carol-daily/`) is a separate program with its own Routine. It was left
running when Daily Marxism was paused.

## State
`state.json` tracks the next day number, next week number, the first send date of the next batch, the next quiz number, its send date and the days it covers. An optional `transition` field describes a one-time batch that differs from the normal rhythm. The `delivery` block is the delivery cursor: `paused`, `last_sent` (the key of the last item delivered, for example `day17`) and the dates around it. Only `queue.py` should write the `delivery` block.

## Changing the course
Moussa can ask any session to change cadence, themes, or style: edit `PROGRAM.md` and/or the Routines (via `list_triggers`/`update_trigger`), commit, push.
