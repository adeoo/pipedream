# Independent review (required before sending)

Send a review agent that did **not** see the writing. It must not edit files. Give it:

1. The paths: the built HTML, `parts.html`, `figures/*.svg`, `photos/photos.json`.
2. How to render: `python3 <skill>/scripts/render_svg.py OUT figures/*.svg` and `python3 <skill>/scripts/render_svg.py OUT --page LESSON.html` (phone and desktop screenshots of every part). It must look at every PNG.
3. The learner profile summary and the writing rules (from learner-profile.md and teaching-method.md).
4. The list of facts and numbers you relied on, with their sources, and a list of numbers you computed yourself so it can re-check them against the standard.

Ask it to check, and report as a numbered list, most severe first, with location, problem and exact fix:
- WRONG FACT: every number, standard name and edition, catalog dimension (against the source you named), all arithmetic.
- WRONG MENU PATH: every SolidWorks path and field name, against help.solidworks.com for the current version.
- PROJECT FLOW: can Adel really do each step with only his computer, in order, without a missing step? Does every Check match what SolidWorks will show?
- FIGURE PROBLEM: overlaps, labels on the drawing, leaders to nowhere, wrong geometry, wrong hatching or centre lines.
- PHOTO PROBLEM: wrong subject, missing credit, license not free.
- LEVEL / WRITING RULE: words not explained, no Portuguese word, sentences over 25 words, em dashes, passive voice, too much at once.
- UI BUG: Back/Next, chips, progress bar, Comment buttons, counter, Copy my comments, phone width, dark mode, no browser storage.

## After the review
- Fix every finding you agree with. For each one you do not fix, tell Adel which and why (for example: "you gave this as a checked fact").
- Verify disputed SolidWorks paths yourself on help.solidworks.com. Fetch pages with a browser User-Agent; the topic text is in the page's `"helpText"` JSON.
- Re-render the changed figures and look at them again. Rebuild. Re-run the page test.
