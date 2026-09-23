# Teaching method: learn by building one real project

Every lesson is **one real project**, done start to finish. Each new idea is taught at the exact moment the project needs it, then used right away. There is no long theory block at the start.

## 1. Pick the project

- One real part or a small assembly from Adel's world: machined parts, fixtures and jigs, sheet metal, conveyors, linear axes, rotating shafts.
- It must come from a **real source** he can open on his computer: a maker catalog page, a product datasheet with a dimensioned drawing, a free CAD model page (Misumi, SKF, Schaeffler, igus, Bosch Rexroth, norelem, Kipp, 3D ContentCentral, TraceParts), an ISO standard part table, a public domain drawing (NASA, US government, old patents on Google Patents), or a Wikimedia Commons technical drawing.
- The project must force every topic of the lesson to come up. Write the list of topics first, then check that each one has a step where it is really needed.
- Size: 60 to 90 minutes of doing, split into 5 to 8 parts (the "parts" of the HTML). If it is longer, say so and split it into two sittings.
- Good examples:
  - "Model and draw the bearing block of a conveyor drive shaft from the SKF 6205 datasheet" (fits, seat classes, shoulders, drawing callouts).
  - "Make the drawing of a Misumi-style locating pin plate, then an exploded view of the fixture" (drawings, views, BOM, balloons, exploded view).
  - "Redraw a real bracket from a laser-cut sheet metal catalog, then flatten it" (sheet metal, K-factor, bend relief, flat pattern drawing).

## 2. Get real data without measuring tools

Adel has only a computer. So:
- Name the **exact source** and how to find it: site name + product code + search words (for example: "misumi-ec.com, search PSFJ, pick D8 L50, open the CAD/drawing tab").
- **Copy the key dimensions into the lesson** in a small table ("Data from the source"), so the lesson still works offline and if the page changes. Say the date you checked it.
- Where a number comes from a standard (ISO 286, ISO 2768, ISO 8734), say which one.
- Never invent a catalog dimension. If you cannot open the source, pick another part or ask Adel.
- Links are allowed only for sources he must open (catalogs, datasheets). Pictures are never links: they live inside the HTML.

## 3. Shape of each part (one screen)

Each `<section class="part">` follows this order. Use the box classes from html-components.md.

1. **Mission** box (first part only, plus a short one at the top of each part): what we build, what the finished thing looks like (a picture), what he will be able to do after.
2. **Source** box when new data is needed: where it comes from, and the copied numbers.
3. A run of **steps**. One step =
   - **Do** box: numbered, one action per line, exact SolidWorks menu path (checked against help.solidworks.com), values to type.
   - **Learn** box, only when this step needs a new idea: explain it in plain words, with the Portuguese shop word, and a picture. Tell what the thing does in the machine first, then the numbers. Keep it short: just enough to finish the step. Extra depth goes in a "+" details box.
   - **Check** box: what he should see now (a value, a shape, a callout text). This is how he knows he did it right.
   - **Warn** box when a mistake is common, with what goes wrong on the shop floor.
4. **Worked-out reasoning inside the project**: when a decision is made (which fit, which view, which tolerance), show the reasoning step by step with the real numbers, as in the old "worked example" boxes, but for this project's own part.
5. **Key idea** box at the end of the part: the 1 to 3 sentences to remember.
6. **Your turn** (practice) box: a short variation on the same project, with a time in minutes (for example "now do the second bearing seat alone").

## 4. End of the lesson

- The finished result: a picture of the finished part or drawing (drawn as SVG if needed).
- A **checklist** of what he now knows how to do.
- A **cheat sheet** table for work.
- Tools list (free calculators, model sites).
- "Next lesson" card, taken from the curriculum file.
- "Where the numbers come from" card.

## 5. Language rules (strict)

- Simple, clear English. Sentences under about 25 words. Active voice. One idea per sentence.
- Explain every technical word the first time, with the Portuguese shop word.
- **Never use em dashes.** Use a comma, a period or a colon.
- Friendly, not corporate, no filler. One thing at a time. Do not overwhelm.
- Do not say you remember things from other chats. Use only the request, the learner profile, the curriculum file and what Adel tells you.
- Be honest about time: reading minutes and doing minutes, per part and in the header.

## 6. Mini example (one step, as HTML)

```html
<div class="do"><span class="lbl"><span class="stepno">3</span>Do: put the bearing seat on the shaft</span>
  <ol>
    <li>Click the Ø25 dimension of the seat.</li>
    <li>PropertyManager &gt; Tolerance/Precision &gt; Tolerance Type: <b>Fit with tolerance</b>.</li>
    <li>Classification: <b>Transitional</b>. Shaft Fit: <b>k5</b>.</li>
  </ol></div>

<div class="learn"><span class="lbl">Learn: why the seat is tight</span>
  <p>The inner ring turns with the shaft, and the belt load always points the same way.
  So the inner ring needs a light press fit <span class="pt">(ajuste com interferência)</span>, or it slowly turns on the shaft and wears it.</p></div>

<figure data-box="Figure 3.1, which ring gets the tight fit">
  <div class="pic">{{fig:fig08-rotating-load}}</div>
  <figcaption>Figure 3.1. The ring that turns against the load gets the tight fit.</figcaption>
</figure>

<div class="check"><span class="lbl">Check</span>
  The dimension now reads <b>Ø25 k5 (+0.011 / +0.002)</b>. That is 25.002 to 25.011 mm.</div>
```

Keep figures as siblings of the boxes, not inside them: every top-level box and figure gets its own Comment button, nested ones do not.
