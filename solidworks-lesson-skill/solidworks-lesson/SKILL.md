---
name: solidworks-lesson
description: Makes a SolidWorks / mechanical design lesson for Adel as one self-contained, offline HTML file with photos and engineering SVG drawings, a Comment button on every box and a "Copy my comments" button. The lesson teaches by building one real project from a real drawing or catalog page, learning each idea at the moment it is needed. Use when Adel asks for a new lesson, a session, "teach me X", "I want to learn X", or names a topic from his curriculum file (SolidWorks features, drawings, ISO drawing norms, tolerances, GD&T, threads, sheet metal, design for machining).
---

# SolidWorks lesson maker

You make one lesson per request. The lesson is a single HTML file that works offline, plus every drawing as a separate `.svg` file.

## Before anything
1. Read `references/learner-profile.md`. Write for Adel.
2. Read `references/teaching-method.md`. The method is **learn by building one real project**. This is the most important file.
3. Find the topic:
   - If Adel names a topic, look for his curriculum file `solidworks-curriculum.md` (attached in the chat, or in the working directory). Use the matching chapter: its topics, suggested project, real sources and "leave out" notes. The curriculum file is kept outside this skill on purpose.
   - If there is no curriculum file, or the topic is not in it, work from his words.
4. If the request is not clear (topic too big for one lesson, no project idea, unknown time budget), ask **one short question**, unless Adel said not to ask. Also ask if you cannot find a real source for the project.
5. Read `references/checked-facts.md`. Reuse those facts. Do not research them again.

## Build the lesson
Work in a folder named for the lesson (for example `session-3-drawings/`). Layout: see `references/html-components.md`.

1. **Plan the project.** Pick one real part or small assembly with a real source Adel can open on his computer. List the lesson topics, and map each topic to the step that needs it. Split into 5 to 8 parts. Estimate reading and doing time honestly.
2. **Get the real data.** Open the source. Copy the key dimensions into a "Data from the source" table, with the date. Never invent catalog numbers. Check every SolidWorks menu path on help.solidworks.com (see review.md for how to fetch it).
3. **Photos, in parallel.** Send research agents (one per picture group, with a 20 minute limit) to find free photos. Rules and known-good files: `references/photos.md`. Download and look at each one yourself. No photo found: draw it.
4. **Drawings.** Copy `scripts/_lib.py` and `scripts/_style.txt` into `figures/`. Draw the SVGs in engineering style with labels outside. Render every one with `scripts/render_svg.py` and **look at it**. Fix until clean. Rules: `references/figures.md`.
5. **Write `parts.html`** with the box classes (mission, src, do, learn, check, key, tip, warn, ex, prac, details, figure). One project, each idea taught when needed. Language rules in teaching-method.md: short sentences, Portuguese shop words, no em dashes.
6. **Build**: `python3 scripts/build_lesson.py LESSON_DIR` (needs Pillow and Playwright: `pip install pillow playwright` if missing; do not download browsers when Chromium is already installed). It inlines figures and base64 photos into `assets/shell.html`, and fails on leftover placeholders, em dashes, browser storage, or more than 8 MB.
7. **Test the page**: `python3 scripts/render_svg.py OUT --page LESSON.html`. Look at the phone and desktop screenshots. Check no errors, the Comment buttons and the page width.
8. **Independent review**: send a review agent that did not see the writing (`references/review.md`). Fix what it finds, re-render, rebuild, re-test.
9. Add any new checked facts to `references/checked-facts.md` if you can edit the skill; otherwise list them for Adel.

## Deliver
- Send the HTML with the file-sending tool (not a published artifact, unless Adel asks). Send every `.svg` too.
- If you are in a git repo with a working branch, commit and push.
- Reply with a short TL;DR first. Then: what the project is, honest times, which pictures are drawn instead of photos and why, what the reviewer found and fixed, and anything you did not fix and why. Friendly, plain words.

## Keep these features (Adel asked for them)
One part on screen at a time with Back/Next, part chips and a progress bar. Short cards. Mission, Source, Do, Learn, Check, Key idea, Tip, Watch out, Worked out and Your turn boxes. "+" boxes for extra depth. Dark mode. Works on a phone. A Comment button on every box, a comment counter, and "Copy my comments" that copies `[Part > Box]` + comment as plain text. No localStorage. Every picture inside the file. Photo credits. Cheat sheet and tools list at the end.
