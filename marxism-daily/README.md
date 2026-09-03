# Daily Marxism — system

Automated daily email course. See `PROGRAM.md` for syllabus, voice, and email format.

## Branch

Since 2026-09-02 the program lives on branch `claude/daily-programs` (before: `claude/daily-programs`). Both Routines read from and push to the new branch.

## How it works (v2 transport, since 2026-08-28; Sunday quiz since 2026-09-02)

Sending migrated from Resend to Inkbox on 2026-08-28. Resend is retired: nothing is scheduled there and no Routine touches it anymore.

- **Weekly writer** (Claude Routine `trig_01FwcGbF9PbBj7cSdHn5BpCq`, Thursdays 12:00 UTC, self-bind into the v2 operations session):
  1. Checks out branch `claude/daily-programs` of `adeoo/pipedream`.
  2. Reads `PROGRAM.md` (v2), `state.json`, and the previous week's lessons for continuity.
  3. Writes one batch: the quiz for the coming Sunday (`quizzes/quizNN.html`, `quizNN.pt.html`, `quizNN.json`, built with the `test-workbook` skill) plus the next week's 6 bilingual lessons, Monday to Saturday, as `lessons/weekNN/dayNN.md` (front matter: `subject`, `subject_pt`, `send_date`; English lesson, then `=== PT-BR ===`, then the Portuguese version). A `transition` field in `state.json` overrides this for one batch.
  4. Verifies each lesson renders with `render.py`, updates `state.json`, commits, pushes. It does NOT send or schedule email.
- **Daily send** (Claude Routine `trig_018T2b8WrCRB2nZJxudgZoE8`, daily 09:00 UTC = 06:00 América/São Paulo, self-bind into the same session, which holds the Inkbox connector):
  1. Monday to Saturday: finds the lesson whose `send_date` is today (São Paulo time). Sunday: finds the quiz whose `quizzes/quizNN.json` `send_date` is today.
  2. Lessons: renders with `render.py` and sends via Inkbox from `adeosagent@inkboxmail.com` ("Daily Marxism"): the English version to `moussaadel97@gmail.com`, the PT-BR version to `ana.ruberrime@gmail.com`. Quiz: sends a short STE body with the HTML file as an attachment (English file to Moussa, PT-BR file to Carol). The quiz is never pasted into the body: mail clients remove scripts.
  3. Idempotent: checks Inkbox sent mail first and only sends whichever language version has not gone out today.
  4. Verifies both sends; on failure retries once, then reports the error in the session.

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

## State
`state.json` tracks the next day number, next week number, the first send date of the next batch, the next quiz number, its send date and the days it covers. An optional `transition` field describes a one-time batch that differs from the normal rhythm.

## Changing the course
Moussa can ask any session to change cadence, themes, or style: edit `PROGRAM.md` and/or the Routines (via `list_triggers`/`update_trigger`), commit, push.
