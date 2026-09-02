# Teaching Notes

## Resuming in a fresh session
This teaching workspace lives ONLY on the teaching branches (latest:
`claude/continue-bike-lessons-06egtk`, earlier:
`claude/bike-frame-design-geometry-tcr8l3`). If /teach is invoked and
MISSION.md is missing from the working directory, DO NOT restart the mission
interview — fetch and check out the latest teaching branch first, then read
MISSION.md, this file, and the latest lesson in ./lessons/ to find where the
course left off. Continue the month arc below; do not re-teach material
already covered.

## User preferences
- Friendly tone, plain language — avoid technical gibberish; introduce jargon gently, one term at a time.
- Likes a TL;DR up front in chat replies.
- Wants to be asked questions when things are unclear.
- No artifacts unless a specific file is requested — deliver lessons as workspace files.
- READS ON HIS PHONE (2026-09-02): lessons must be fully self-contained
  (inline style/script — no ../assets/ links, they break in Claude's viewer)
  and phone-first: short paragraphs, cards over dense bullets, <500 words of
  prose, big quiz buttons, big SVG labels. He hated the desktop-dense v1 of
  lesson 0002. Full rules recorded in .claude/skills/teach/SKILL.md
  ("Delivery" section). Send each lesson via SendUserFile (render).

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

## Working notes
- Lesson 0001 (frame anatomy) delivered 2026-09-01. Quiz results not yet observed —
  do not write a learning record until he reports back or answers retrieval
  questions in chat.
- 2026-09-02: he read lesson 0002 v1 on his phone — broken render (external
  asset links) and too wordy. Rewrote 0002 phone-first + self-contained,
  retrofitted 0001 and both reference sheets, added Delivery rules to the
  teach SKILL.md. All future documents must follow those rules.
- Lesson 0002 (reading a geometry chart) delivered 2026-09-02, using the Surly
  Disc Trucker 700c 56/58cm chart (verified against surlybikes.com: 560/575mm,
  73°/72°, 450mm stays, 1051mm wheelbase, BB drop 80mm, offset 45mm). Opens
  with 2 warm-up retrieval questions on anatomy (spacing). Core frame: every
  chart row serves either FIT (rider's body) or BEHAVIOR (ride feel) — reuse
  this fit-vs-behavior split in all later geometry lessons.
- Assignment pending: he was asked to bring his own bike's six chart numbers to
  the next chat. If he does, that's the retrieval evidence — write learning
  record 0001 then, covering anatomy + chart reading.
- Next lesson candidates (week 1→2 bridge): head tube angle & steering feel,
  then BB drop; then fork offset + trail (needs the still-open touring-geometry
  resource gap in RESOURCES.md); stack & reach when sizing week starts.
- Glossary not started yet — wait until anatomy terms are demonstrated, then seed
  it with the eight frame parts + the six chart rows from lesson 0002.
