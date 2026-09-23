"""Small helpers to write the lesson figures as plain SVG files."""
import math, os

HERE = os.path.dirname(os.path.abspath(__file__))
STYLE = open(os.path.join(HERE, "_style.txt")).read()

BLUE = "#2f6fde"
GREEN = "#1f8a4c"
RED = "#c0392b"
AMBER = "#c8761a"
BRONZE = "#a86b2d"
INK = "#1f2733"


def defs(f):
    return f"""<defs>
<pattern id="hA-{f}" patternUnits="userSpaceOnUse" width="9" height="9" patternTransform="rotate(45)"><rect width="9" height="9" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="9" stroke="{INK}" stroke-width="1"/></pattern>
<pattern id="hB-{f}" patternUnits="userSpaceOnUse" width="9" height="9" patternTransform="rotate(-45)"><rect width="9" height="9" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="9" stroke="{INK}" stroke-width="1"/></pattern>
<pattern id="hS-{f}" patternUnits="userSpaceOnUse" width="7" height="7" patternTransform="rotate(-45)"><rect width="7" height="7" fill="#eaf5ee"/><line x1="0" y1="0" x2="0" y2="7" stroke="{GREEN}" stroke-width="1.1"/></pattern>
<pattern id="hC-{f}" patternUnits="userSpaceOnUse" width="7" height="7" patternTransform="rotate(45)"><rect width="7" height="7" fill="#f6e7d3"/><line x1="0" y1="0" x2="0" y2="7" stroke="{BRONZE}" stroke-width="1.2"/></pattern>
<pattern id="hG-{f}" patternUnits="userSpaceOnUse" width="10" height="10" patternTransform="rotate(45)"><rect width="10" height="10" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="10" stroke="{INK}" stroke-width="1"/><line x1="5" y1="0" x2="5" y2="10" stroke="{INK}" stroke-width="0.5"/></pattern>
<pattern id="hR-{f}" patternUnits="userSpaceOnUse" width="5" height="5" patternTransform="rotate(-60)"><rect width="5" height="5" fill="#f4f5f7"/><line x1="0" y1="0" x2="0" y2="5" stroke="{INK}" stroke-width="0.9"/></pattern>
<marker id="dot-{f}" markerWidth="8" markerHeight="8" refX="4" refY="4" markerUnits="userSpaceOnUse"><circle cx="4" cy="4" r="3" fill="{INK}"/></marker>
<marker id="arr-{f}" markerWidth="12" markerHeight="10" refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L12,5 L0,10 z" fill="{INK}"/></marker>
<marker id="arrs-{f}" markerWidth="12" markerHeight="10" refX="1" refY="5" orient="auto" markerUnits="userSpaceOnUse"><path d="M12,0 L0,5 L12,10 z" fill="{INK}"/></marker>
<marker id="arrR-{f}" markerWidth="14" markerHeight="12" refX="13" refY="6" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L14,6 L0,12 z" fill="{RED}"/></marker>
<marker id="arrB-{f}" markerWidth="14" markerHeight="12" refX="13" refY="6" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L14,6 L0,12 z" fill="{BLUE}"/></marker>
</defs>"""


def svg(f, w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" id="svg-{f}" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" role="img" aria-label="{title}">\n'
            f'<title>{title}</title>\n{STYLE}{defs(f)}\n'
            f'<rect x="0" y="0" width="{w}" height="{h}" fill="#ffffff"/>\n{body}\n</svg>\n')


def text(x, y, lines, cls="g-t", anchor="start", dy=19, extra=""):
    if isinstance(lines, str):
        lines = [lines]
    out = []
    for i, ln in enumerate(lines):
        c = cls
        if isinstance(ln, tuple):
            c, ln = ln
        out.append(f'<text class="{c}" x="{x}" y="{y + i * dy}" text-anchor="{anchor}" {extra}>{ln}</text>')
    return "\n".join(out)


def leader(f, pts, dot=True, arrow=False):
    p = " ".join(f"{a},{b}" for a, b in pts)
    m = ""
    if dot:
        m = f' marker-start="url(#dot-{f})"'
    if arrow:
        m = f' marker-start="url(#arrs-{f})"'
    return f'<polyline class="g-thin" points="{p}"{m}/>'


def line(x1, y1, x2, y2, cls="g-ink", extra=""):
    return f'<line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {extra}/>'


def dimv(f, x, y1, y2):
    """vertical dimension line with two arrows"""
    return (f'<line class="g-thin" x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" '
            f'marker-start="url(#arrs-{f})" marker-end="url(#arr-{f})"/>')


def dimh(f, y, x1, x2):
    return (f'<line class="g-thin" x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" '
            f'marker-start="url(#arrs-{f})" marker-end="url(#arr-{f})"/>')


def annulus(cx, cy, r1, r2):
    """path for a ring between radius r1 (inner) and r2 (outer), even-odd"""
    return (f"M{cx - r2},{cy} a{r2},{r2} 0 1,0 {2 * r2},0 a{r2},{r2} 0 1,0 {-2 * r2},0 Z "
            f"M{cx - r1},{cy} a{r1},{r1} 0 1,0 {2 * r1},0 a{r1},{r1} 0 1,0 {-2 * r1},0 Z")


def circle_path(cx, cy, r):
    return f"M{cx - r},{cy} a{r},{r} 0 1,0 {2 * r},0 a{r},{r} 0 1,0 {-2 * r},0 Z"


def polar(cx, cy, r, deg):
    a = math.radians(deg)
    return (round(cx + r * math.cos(a), 1), round(cy - r * math.sin(a), 1))


def write(name, content):
    with open(os.path.join(HERE, name), "w") as fh:
        fh.write(content)
