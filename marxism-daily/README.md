# Daily Marxism — system

Automated daily email course. See `PROGRAM.md` for syllabus, voice, and email format.

## How it works
- **Weekly writer** (Claude Routine `trig_01MjchH1dTpTJgZJSttVwct9`, Thursdays 12:00 UTC): fires into the founding Claude session (self-bind, so it keeps the Resend connector), which then
  1. Checks out branch `claude/scheduled-tasks-status-xr0587` of `adeoo/pipedream`.
  2. Reads `PROGRAM.md`, `state.json`, and the previous week's lessons in `lessons/` for continuity.
  3. Writes the next 7 lessons as `lessons/weekNN/dayNN.md` (front matter: `subject`, `send_date`).
  4. Sends each via the Resend connector (`send-email`) with `scheduledAt` set to `<send_date>T06:00:00-03:00`, from `Daily Marxism <onboarding@resend.dev>` to `moussaadel97@gmail.com`, with both `html` and `text` bodies rendered per PROGRAM.md style. Use an `idempotencyKey` of `marxism-dayNN` per lesson.
  5. Verifies last week's emails actually delivered (`list-emails`); re-sends any that failed.
  6. Updates `state.json`, commits, pushes to the same branch.
- **Sending**: Resend's scheduled sends (`scheduledAt`) deliver each email at 6am Brasília.
- **Delivery check** (Claude Routine `trig_016cewnP9Tnrd14sQNZa2W9x`, daily 09:10 UTC, self-bind into the founding session): verifies today's lesson delivered and immediately re-sends it if the scheduled send failed. Added after the Day 1 incident (2026-08-22): the scheduled email flipped to `failed` at fire time while immediate sends work fine, so every scheduled send is treated as unreliable until proven otherwise. Scheduled sends turn out to be **intermittent**, not uniformly broken — observed so far: Day 1 (08-22) failed, Day 2 (08-23) failed, Day 3 (08-24) delivered on its own. So keep using `scheduledAt` and keep this check as the safety net; only if failures become near-total should the architecture switch to sending directly from this routine.

### Delivery log
| Day | Date | Scheduled send | Outcome |
|---|---|---|---|
| 1 | 2026-08-22 | failed | re-sent by hand, delivered |
| 2 | 2026-08-23 | failed | re-sent by check routine, delivered |
| 3 | 2026-08-24 | delivered | no action needed |
| 4 | 2026-08-25 | failed | re-sent by check routine, delivered |

Running tally: 3 of 4 scheduled sends failed at fire time (75%). The check routine has rescued every one of them within ~13 minutes, so lessons still arrive each morning — just at ~06:13 instead of 06:00 on a failed day. Keep both mechanisms: the scheduled send costs nothing when it fails, and dropping it would leave the routine as a single point of failure.

## State
`state.json` tracks the next day number, next week number, and the first send date of the next batch.

## Changing the course
Moussa can ask any session to change cadence, themes, or style: edit `PROGRAM.md` and/or the Routine (via `list_triggers`/`update_trigger`), commit, push.
