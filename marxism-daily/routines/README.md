# Routine prompts

**Both Daily Marxism Routines are currently disabled**: the course is paused (see `../README.md`, section "Pausing and resuming"). Carol Daily is still enabled. Re-enable the two Marxism Routines with `update_trigger` (`enabled=true`) after running `queue.py resume`.

Both Daily Marxism Routines (and Carol Daily's, in `carol-daily/routines/`) start a
fresh cloud session on every run. They read from and push to branch `claude/daily-programs`.
The files here are copies of the prompts stored in the Routines, kept for reference.

To apply a change: edit the file, then update the Routine with `update_trigger`
(trigger id below) using the file content as `prompt`, from any Claude Code session.

| Routine | Trigger id | Prompt file |
|---|---|---|
| Weekly writer (Thursdays 12:00 UTC) | `trig_012MfVR5ARzo3EcThuMqofkR` | `weekly-writer.prompt.txt` |
| Daily sender (daily 09:00 UTC, 06:00 São Paulo) | `trig_013J1Y22YKk49GeqW1XJ9YRj` | `daily-sender.prompt.txt` |
| Carol Daily (daily 09:00 UTC, 06:00 São Paulo) | `trig_01S1c9MS23QnRVreYxj2WwJp` | `../../carol-daily/routines/carol-daily.prompt.txt` |

## What the sender reads

The daily sender no longer picks an item from the weekday. It runs `python3 marxism-daily/queue.py next` and delivers whatever the queue names, then records the delivery with `queue.py advance <key>` and pushes `state.json`. That push is what stops the next morning from repeating the item, so a run that sends but cannot push has to be reported.

## Send protocol

The daily sender and Carol Daily prompts contain a SEND PROTOCOL: render with `--write`, copy the files verbatim into `inkbox_email_send`, read the sent message back with `inkbox_email_get`, at most one corrected copy. If you edit a prompt, keep that block intact. Both daily Routines and the writer also call `add_repo` (owner `adeoo`, repo `pipedream`, access `push`) before pushing; if a run still reports a refused push, attach the repo to the Routine at claude.ai/code/routines.
