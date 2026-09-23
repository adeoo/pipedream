# HTML components (what goes in parts.html)

`assets/shell.html` already has: the page frame, CSS (light and dark mode, phone layout), part navigation (Back/Next, part chips, progress bar), and the comment system (a Comment button on every box, a counter, and a "Copy my comments" button that copies plain text with `[Part > Box]` in front of each comment, kept in page memory only, no localStorage). Do not change it unless Adel asks. You only write `parts.html`.

## A part

```html
<section class="part" data-title="3. Draw the shaft">
  <h2>3. Draw the shaft: views and diameters</h2>
  <p class="mins">Reading about 8 minutes. Doing about 15 minutes.</p>
  ... boxes ...
</section>
```
`data-title` is the short name on the chip at the top and in copied comments. Use "N. Short name".

## Boxes (each gets a Comment button by itself)

| Class | Use | Label |
|---|---|---|
| `mission` | the project brief, top of part 1, short reminder at the top of other parts | `<span class="lbl">Mission</span>` |
| `src` | where the real data comes from + table of copied numbers | `<span class="lbl">Data from the source</span>` |
| `do` | one step of actions in SolidWorks, numbered list | `<span class="lbl"><span class="stepno">3</span>Do: ...</span>` |
| `learn` | the new idea this step needs, plain words + Portuguese word | `<span class="lbl">Learn: ...</span>` |
| `check` | what he should see after the step | `<span class="lbl">Check</span>` |
| `key` | the idea to remember | `<span class="lbl">Key idea</span>` |
| `tip` | a good habit, a shortcut | `<span class="lbl">Tip</span>` |
| `warn` | a common mistake and what goes wrong at the shop | `<span class="lbl">Watch out</span>` |
| `ex` | worked-out reasoning with real numbers (a decision) | `<span class="lbl">Worked out: ...</span>` |
| `prac` | "Your turn" task, with minutes | `<span class="lbl">Your turn, 10 minutes</span>` |
| `card` | plain content card, with `<h3>` title | |
| `details` | "+" box that opens for extra depth: `<details data-box="Plus box, NAME"><summary>...</summary><div class="in">...</div></details>` | |

Box names in copied comments come from `data-box` if present, else the `<h3>`, else the label. Give every `figure` and `details` a unique `data-box`.

## Figures and photos

```html
<figure data-box="Figure 2.1, the three views">
  <div class="pic">{{fig:fig05-three-views}}</div>
  <figcaption>Figure 2.1. ...</figcaption>
</figure>

<figure data-box="Photo 1.2, a caliper">
  {{photo:caliper}}
  <figcaption>Photo 1.2. ... {{credit:caliper}}</figcaption>
</figure>
```
- `{{fig:NAME}}` inlines `figures/NAME.svg`. The build adds the phone "swipe sideways" hint.
- `{{photo:key}}` inlines the photo(s) from `photos/photos.json` as base64. Two images in one key show side by side.
- `{{caption:key}}` inserts the caption stored in photos.json. `{{credit:key}}` inserts the credit line.

photos.json:
```json
{"caliper": {"caption": "optional text",
  "images": [{"file": "caliper.jpg", "alt": "A dial caliper",
              "credit": "Author, CC BY-SA 4.0, Wikimedia Commons (File name.jpg)"}]}}
```

## Other bits
- `<span class="pt">(palavra)</span>` for the Portuguese word. `<span class="word">...</span>` for a highlighted term.
- `<span class="path">Insert &gt; Annotations &gt; Hole Callout</span>` for a menu path.
- `<span class="num">20.000 to 20.021 mm</span>` for a key number.
- Tables: wrap in `<div class="scroll">` so they scroll on phones.
- Minus sign in numbers: use `−` (U+2212), never an em dash.

## lesson.json
```json
{"title": "Session 3: Drawings the shop can read",
 "subtitle": "One project: the drawing of a real bearing block. 7 parts. Honest time: about 50 minutes of reading and 70 minutes of doing. Do Parts 1 to 4 one day and 5 to 7 the next.",
 "output": "Session-3-Drawings-the-shop-can-read.html"}
```
