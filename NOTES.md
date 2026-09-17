# Teaching Notes

## PAUSED — checkpoint 2026-09-17
The course is paused at the learner's request, after Lesson 0001. Nothing is
half-finished: the working tree is clean and every file listed below is
committed. On resume, read this section, then "Where we left off", then carry on.

A note on the branch name: this checkpoint sits on
`claude/marxism-project-checkpoint-j8fet7`. The word "marxism" came out of the
pause request itself and has nothing to do with the subject matter. This is the
bike frame design workspace. There is no Marxism project here — do not go
looking for one, and do not start one without asking.

## Resuming in a fresh session
The teaching workspace lives on `master` (merged via PR #2) and on the
checkpoint branch above. An earlier version of this note pointed at
`claude/bike-frame-design-geometry-tcr8l3`; that branch no longer exists, so
ignore it.

If /teach is invoked and `MISSION.md` is missing from the working directory, do
NOT restart the mission interview. Check out a branch that has it, then read
`MISSION.md`, this file, and the latest lesson in `./lessons/` to find where the
course left off. Continue the month arc below; do not re-teach covered material.

## Where we left off (state at pause)

Delivered and committed:
- `MISSION.md` — mission agreed 2026-09-01 and still accurate.
- `RESOURCES.md` — populated; six knowledge sources, three communities, two
  recorded gaps (touring-specific geometry, local classes).
- `lessons/0001-anatomy-of-a-frame.html` — delivered 2026-09-01. Covers the two
  triangles and the eight frame parts, with a "Check yourself" quiz and a
  spoken-retrieval assignment.
- `reference/frame-anatomy.html` — cheat sheet for the eight parts.
- `assets/course.css`, `assets/quiz.js` — shared components. Reuse these in
  every new lesson; never inline a second copy.

Not started yet:
- `learning-records/` — no records written; the directory does not exist yet.
- A glossary — not started. Seed it with the eight frame parts once the anatomy
  terms have actually been demonstrated, not just read.
- Lesson 0002 onward.

Open loops to pick up first, in this order:
1. Lesson 0001's quiz results were never reported. Ask how the "Check yourself"
   quiz went before assuming the anatomy names have stuck.
2. The real-world assignment — naming the eight parts out loud at his own bike,
   twice — was set but never confirmed done. Ask about it.
3. Only write the first learning record once he answers retrieval questions or
   reports back. Coverage is not evidence of learning.

## Next lesson when we resume
Lesson 0002: reading a geometry chart, using a real touring bike. The intended
example is a Surly Long Haul Trucker chart. After that, wheelbase and trail
intuition. Both sit in the Week 1 to Week 2 stretch of the arc below.

## User preferences
- Friendly tone, plain language — avoid technical gibberish; introduce jargon gently, one term at a time.
- Likes a TL;DR up front in chat replies.
- Wants to be asked questions when things are unclear.
- No artifacts unless a specific file is requested — deliver lessons as workspace files.

## Learner profile (2026-09-01)
- Rides bikes; has never wrenched or done metalwork. Total beginner on the craft side.
- Goal: hobby craftsman building steel city/touring frames; first milestone is a frame for himself.
- No workshop — sequence all early lessons as paper/screen work (anatomy → geometry → fit → drawing → materials), leave brazing/tooling until workshop access exists.

## Month curriculum arc (agreed 2026-09-02, ~1 short lesson/day, 1 in 5 days review)
- Week 1 — Speak the language: anatomy (0001 done) → reading a geometry chart →
  the core measures (seat/head angle, top tube, wheelbase, chainstays, BB drop).
- Week 2 — Numbers to ride feel: wheelbase/trail/steering intuition, touring
  stability, body measurements → frame size; measure own bike + self.
- Week 3 — Materials & joints: why steel, butted tubing, real tubesets
  (Reynolds/Columbus), lugs vs fillet vs TIG.
- Week 4 — Capstone: full geometry table + drawing of his own touring frame,
  clearance checks (toe overlap, heels, fenders), build plan and community
  critique. End state: complete defensible design; hand skills deferred until
  workshop access.
