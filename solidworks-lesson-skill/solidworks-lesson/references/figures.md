# Drawing the figures (inline SVG)

Adel liked these drawings a lot. Keep the same look.

## Rules for every drawing
- Engineering style: section views with hatching, dash-dot centre lines, dimension lines with arrows, hidden lines dashed.
- **Labels go outside the drawing, never on top of it**, joined with leader lines (a dot on the part, a thin line to the text).
- Each label: bold name, then one or two plain lines, then the Portuguese word in small italic grey.
- White "paper" background, even in dark mode (the page keeps figures on white).
- Drawn big where it helps ("gap drawn hundreds of times bigger than real"), and say so in the figure.
- One idea per drawing. A title line at the top of the SVG.
- Also save every drawing as a separate plain `.svg` file (no HTML around it) and send them to Adel.

## How to make them
Use `scripts/_lib.py` (copy `_lib.py` and `_style.txt` into the lesson's `figures/` folder). Write one Python file per group of figures, for example `figures/figs_a.py`:

```python
from _lib import *
f = "shd"                       # short unique id per figure: hatch patterns and markers get this suffix
b = [text(30, 30, "Title of the drawing", "g-h")]
b.append(f'<rect x="60" y="80" width="200" height="100" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
b.append(line(40, 130, 280, 130, "g-cl"))                       # centre line
b.append(leader(f, [(200, 100), (330, 70), (345, 70)]))          # dot on the part, then to the label
b.append(text(351, 66, [("g-b", "Bearing seat"), "Ø25 k5", ("g-s g-pt", "assento")], dy=18))
write("fig05-seat.svg", svg(f, 760, 300, "Short description for screen readers", "\n".join(b)))
```
Helpers: `svg`, `text` (multi-line, per-line class), `leader`, `line`, `dimv`, `dimh`, `annulus`, `circle_path`, `polar`, `write`.
Patterns: `hA` (45°), `hB` (−45°), `hS` (green shaft), `hC` (bronze), `hG`, `hR` (dense, for bearing rings). Markers: `dot`, `arr`, `arrs`, `arrR`, `arrB`. Colors: `INK`, `BLUE` (hole), `GREEN` (shaft), `RED` (interference or wrong), `AMBER`, `BRONZE`.
Text classes: `g-h` title, `g-b` bold label, `g-t` normal, `g-s` small grey, `g-pt` italic.
Canvas: 760 px wide. Keep text at 13 to 18 px.

Mock-ups of SolidWorks panels: draw them as simplified SVG with every field named by numbered callouts. Say "simplified drawing, not a screenshot". Check the field names on help.solidworks.com first.

## Check every drawing by eye (required)
```
python3 scripts/render_svg.py /path/to/scratch/render figures/*.svg
```
Then open each PNG with the Read tool and look for:
- text on top of a line, a part, or other text,
- a leader that ends in empty space or on the wrong feature,
- a label cut off at the edge,
- wrong geometry (a ball that floats, a groove that does not show, parts that change size between "before" and "after", hatching in the same direction on two touching parts),
- a solid line where a centre line should be (an outline drawn along the axis hides it).
Fix and render again until clean.

## Figure library from Session 2
`assets/figure-library/` holds the 20 finished Session 2 drawings (fits, bearings, dowel pins, bushings, drawing note, SolidWorks Tolerance/Precision mock-up) and the Python files that made them (`figs_a.py` to `figs_e.py`). Reuse a drawing by copying its `.svg` into the lesson's `figures/` folder, or copy the code as a starting point for a new one.
