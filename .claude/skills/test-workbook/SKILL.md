---
name: test-workbook
description: Build an evaluation activity (a "workbook") as one interactive HTML file, in the three-part format that Adel approved. Use when Adel asks for a test, a quiz, a test activity, or an evaluation activity on lessons or on study material. The workbook tests transfer of the concepts to new cases, not memory of the source text.
---

# test-workbook

Build one self-contained HTML file. The reference example is
`lessons/marxism-lesson-1-quiz.html` on branch `claude/marxism-lessons-quiz-5na9nh`
of `adeoo/pipedream`. If that file is not in the working tree, read it with
`git show origin/claude/marxism-lessons-quiz-5na9nh:lessons/marxism-lesson-1-quiz.html`.
Copy its page structure, its CSS, and its JavaScript. Replace only the content.

## Step 1: read the source material

1. Find the lessons or the material that the test must cover. Ask Adel if the source is not clear.
2. Test only the content that Adel studied. Do not test future lessons.
3. List the core concepts of the material. Each part of the workbook uses these concepts.

## Step 2: obey the content rules

These rules came from Adel's feedback. They are not optional.

- **Transfer, not recall.** Use new examples. Do not quote the source lessons. Do not reuse their examples. A question must make Adel apply a concept to a case he did not see.
- **No length cues.** The length of an option must not show the correct answer. For classification items, use options of one or two words. For sentence items, make all options sentences of equal weight.
- **Distractors are plausible misreadings.** Each wrong option is an error that a real student makes: the half-right option, the character explanation for a structural fact, the spark mistaken for a cause, the conspiracy version of a structural account. The feedback names the exact flaw.
- **Honest grey zones.** When a case is a true border case, the correct option is the border label. When two answers are defensible, say so in the feedback and give credit to both.
- **Feedback teaches.** Feedback for a correct answer extends the idea. Feedback for a wrong answer explains why that option tempts people, and where it fails.

## Step 3: build the three parts

**Part 1: classification drill.** Six to ten short cases. Each case is one to three
sentences. Each case has the same three to five one-word or two-word labels. Include
at least one grey-zone case and at least one case with two defensible answers.

**Part 2: find the error.** Two to four passages. Each passage has four sentences of
analysis that use the material's method. Exactly one sentence breaks the method.
Adel clicks the sentence that breaks it. The feedback for a wrong click explains why
that sentence is correct. The three sound sentences must be genuinely sound.

**Part 3: written analysis.** Two to four exercises with a text area, a reveal button,
and a model answer. Include, when the material permits:

1. A "two accounts" exercise: write two rival explanations of one fact.
2. A "predict, then check" exercise: give a real historical or current case, ask for a
   prediction from the material's method, then reveal what happened. Add an honest
   note: a prediction that beats the template is analysis, not failure.
3. A "concepts on each other" exercise: use one concept of the material to explain
   the result of another.

Each model answer ends with a self-test question, so Adel can check his own version.

## Step 4: obey the style rules

- **Writing style:** load the `asd-ste100` skill and write all prose with it.
  Short sentences, one idea per sentence, active voice, plain words, no idioms,
  no em dashes. Technical terms of the subject are permitted.
- **Visual style:** link `../assets/course.css` (the shared course stylesheet) and
  keep an inline mirror of it in the file, so the file also renders alone. Copy this
  arrangement from the reference example, including the high-specificity overrides
  for the row buttons.
- **Tone:** no grades, no timers, no penalties. Every drill has a "try again" button.
  The summary treats a miss as information, not as a verdict. Warm words are
  permitted. Praise is specific, not generic.

## Step 5: verify and deliver

1. Make sure each part works: click handlers, retry buttons, reveal buttons, and the summary count.
2. Make sure no correct answer is the longest option of its item.
3. Save the file in `lessons/` when you work in the repo. Commit and push on the designated branch.
4. Send the file to Adel.
5. For delivery by email: attach the HTML file to the email. Do not paste the HTML
   into the email body. Mail clients remove scripts, and the interactive parts die.
   Write a short STE body that tells Adel to open the attachment in a browser.
