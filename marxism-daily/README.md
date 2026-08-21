# Daily Marxism — system

Automated daily email course. See `PROGRAM.md` for syllabus, voice, and email format.

## How it works
- **Weekly writer** (Claude Routine, Thursdays 12:00 UTC): a fresh session that
  1. Checks out branch `claude/scheduled-tasks-status-xr0587` of `adeoo/pipedream`.
  2. Reads `PROGRAM.md`, `state.json`, and the previous week's lessons in `lessons/` for continuity.
  3. Writes the next 7 lessons as `lessons/weekNN/dayNN.md` (front matter: `subject`, `send_date`).
  4. Sends each via the Resend connector (`send-email`) with `scheduledAt` set to `<send_date>T06:00:00-03:00`, from `Daily Marxism <onboarding@resend.dev>` to `moussaadel97@gmail.com`, with both `html` and `text` bodies rendered per PROGRAM.md style. Use an `idempotencyKey` of `marxism-dayNN` per lesson.
  5. Verifies last week's emails actually delivered (`list-emails`); re-sends any that failed.
  6. Updates `state.json`, commits, pushes to the same branch.
- **Sending**: there is no daily task — Resend's scheduled sends deliver each email at 6am Brasília.

## State
`state.json` tracks the next day number, next week number, and the first send date of the next batch.

## Changing the course
Moussa can ask any session to change cadence, themes, or style: edit `PROGRAM.md` and/or the Routine (via `list_triggers`/`update_trigger`), commit, push.
