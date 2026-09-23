from _lib import *

# ---------- 07 SolidWorks Tolerance/Precision panel mock-up ----------
f = "swp"
b = []
b.append(text(30, 30, "Mock-up of the Tolerance/Precision box (simplified drawing, not a screenshot)", "g-s"))
# window
b.append('<rect x="30" y="45" width="300" height="410" rx="4" fill="#f3f4f6" stroke="#8a93a3" stroke-width="1.5"/>')
b.append('<rect x="30" y="45" width="300" height="34" rx="4" fill="#dfe3ea" stroke="#8a93a3" stroke-width="1.5"/>')
b.append(text(44, 68, "Dimension", "g-b"))
b.append(f'<circle cx="276" cy="62" r="10" fill="{GREEN}"/><path d="M271,62 l4,4 l7,-8" stroke="#fff" stroke-width="2.4" fill="none"/>')
b.append(f'<circle cx="304" cy="62" r="10" fill="{RED}"/><path d="M299,57 l10,10 M309,57 l-10,10" stroke="#fff" stroke-width="2.4"/>')
b.append('<rect x="40" y="92" width="280" height="352" rx="3" fill="#ffffff" stroke="#b8bfcb"/>')
b.append(text(52, 114, "Tolerance/Precision", "g-b"))
b.append('<path d="M300,106 l6,6 l6,-6" stroke="#4a5566" stroke-width="2" fill="none"/>')

def dropdown(y, label, value):
    out = [text(52, y - 6, label, "g-s")]
    out.append(f'<rect x="52" y="{y}" width="256" height="28" rx="3" fill="#fff" stroke="#8a93a3"/>')
    out.append(text(62, y + 19, value, "g-t"))
    out.append(f'<path d="M290,{y + 11} l5,6 l5,-6" stroke="#4a5566" stroke-width="2" fill="none"/>')
    return "\n".join(out)

rows = [(146, "Tolerance Type", "Fit with tolerance"),
        (198, "Classification", "Clearance"),
        (250, "Hole Fit", "H7"),
        (302, "Shaft Fit", "")]
for y, lab, val in rows:
    b.append(dropdown(y, lab, val))
# show parenthesis
b.append('<rect x="52" y="344" width="16" height="16" rx="2" fill="#2f6fde" stroke="#2f6fde"/><path d="M55,352 l4,4 l7,-8" stroke="#fff" stroke-width="2" fill="none"/>')
b.append(text(76, 357, "Show parenthesis", "g-t"))
# fit tolerance display buttons
b.append(text(52, 382, "Fit Tolerance Display", "g-s"))
for i, x in enumerate((52, 96, 140)):
    b.append(f'<rect x="{x}" y="388" width="36" height="30" rx="3" fill="{"#dce8ff" if i == 0 else "#fff"}" stroke="#8a93a3"/>')
b.append('<text x="70" y="401" text-anchor="middle" style="font:9px Arial">H7</text><line x1="60" y1="404" x2="80" y2="404" stroke="#1f2733"/><text x="70" y="414" text-anchor="middle" style="font:9px Arial">g6</text>')
b.append('<text x="114" y="401" text-anchor="middle" style="font:9px Arial">H7</text><text x="114" y="414" text-anchor="middle" style="font:9px Arial">g6</text>')
b.append('<text x="158" y="407" text-anchor="middle" style="font:9px Arial">H7/g6</text>')
# precision
b.append(text(196, 382, "Tolerance precision", "g-s"))
b.append('<rect x="196" y="388" width="112" height="30" rx="3" fill="#fff" stroke="#8a93a3"/>')
b.append(text(206, 408, ".123", "g-t"))
b.append('<path d="M290,400 l5,6 l5,-6" stroke="#4a5566" stroke-width="2" fill="none"/>')

# numbered callouts on the right
calls = [(160, "1", "Tolerance Type", ["Pick Fit with tolerance."]),
         (212, "2", "Classification", ["Clearance, Transitional or Press.", "It shortens the two lists below."]),
         (264, "3", "Hole Fit", ["On a hole: pick H7 here."]),
         (316, "4", "Shaft Fit", ["On a shaft: pick g6, k6 and so on.", "On a hole, you can leave it empty."]),
         (352, "5", "Show parenthesis", ["Ticked here: puts ( ) around", "the two numbers."]),
         (403, "6", "Display / Tolerance precision", ["Stacked or in one line.", "Set 3 decimals so you see 0.015."])]
ly = 70
for yy, n, head, lines in calls:
    b.append(leader(f, [(200 if n == "5" else 308, yy), (372, ly + 4)], dot=True))
    b.append(f'<circle cx="388" cy="{ly}" r="12" fill="{BLUE}"/>')
    b.append(text(388, ly + 5, n, "g-b", "middle", extra='style="fill:#fff"'))
    b.append(text(408, ly + 5, [("g-b", head)] + lines, dy=18))
    ly += 22 + 18 * (len(lines) + 1)
# result preview
b.append(text(30, 488, "What the dimension then shows on the drawing:", "g-b"))
b.append(line(40, 530, 250, 530, "g-thin", f'marker-start="url(#arrs-{f})" marker-end="url(#arr-{f})"'))
b.append(line(40, 505, 40, 545, "g-thin") + line(250, 505, 250, 545, "g-thin"))
b.append('<text x="92" y="522" style="font:700 20px Arial;fill:#1f2733">Ø10 H7</text>')
b.append('<text x="178" y="513" style="font:14px Arial;fill:#1f2733">(+0.015)</text><text x="178" y="529" style="font:14px Arial;fill:#1f2733">(+0.000)</text>')
b.append(leader(f, [(246, 521), (300, 512), (310, 512)]))
b.append(text(318, 506, ["The code, then the two deviations (afastamentos).",
                         "Limits: 10 + 0.015 = 10.015 and 10 + 0.000 = 10.000."], "g-t", dy=20))
write("fig07-sw-tolerance-panel.svg", svg(f, 760, 560, "Mock-up of the SolidWorks Tolerance/Precision panel with each field named", "\n".join(b)))

# ---------- 08 rotating vs stationary load ----------
f = "load"
b = []
b.append(text(380, 30, "Which ring turns against the load? That ring gets the tight fit.", "g-h", "middle"))

def bearing_end(cx, cy, tight_outer):
    out = []
    oc = RED if tight_outer else BLUE
    ic = BLUE if tight_outer else RED
    out.append(f'<path d="{annulus(cx, cy, 92, 112)}" fill="{oc}" fill-opacity=".28" fill-rule="evenodd" stroke="{oc}" stroke-width="2.4"/>')
    out.append(f'<path d="{annulus(cx, cy, 48, 66)}" fill="{ic}" fill-opacity=".28" fill-rule="evenodd" stroke="{ic}" stroke-width="2.4"/>')
    for k in range(9):
        px, py = polar(cx, cy, 79, k * 40 + 10)
        out.append(f'<circle cx="{px}" cy="{py}" r="12" fill="#e7eaef" stroke="{INK}" stroke-width="1.6"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="48" fill="url(#hS-{f})" stroke="{GREEN}" stroke-width="2"/>')
    out.append(line(cx - 130, cy, cx + 130, cy, "g-cl") + line(cx, cy - 130, cx, cy + 130, "g-cl"))
    return "\n".join(out)

def turn_arrow(cx, cy, r, col):
    x1, y1 = polar(cx, cy, r, 150)
    x2, y2 = polar(cx, cy, r, 40)
    mk = "arrR" if col == RED else "arrB"
    return f'<path d="M{x1},{y1} A{r},{r} 0 0,1 {x2},{y2}" fill="none" stroke="{col}" stroke-width="3" marker-end="url(#{mk}-{f})"/>'

# left: shaft turns
cx, cy = 190, 205
b.append(bearing_end(cx, cy, False))
b.append(turn_arrow(cx, cy, 34, RED))
b.append(line(cx, cy + 150, cx, cy + 190, "g-ink", f'style="stroke-width:3" marker-start="url(#arrs-{f})"'))
b.append(text(cx + 10, cy + 186, "load, always this way", "g-b"))
b.append(text(cx, 440, [("g-b", "Case 1: the shaft turns"), "conveyor roller shaft, gearbox shaft", "inner ring turns, load stays still", ("g-b", "inner ring tight: shaft k5"), "outer ring normal: housing H7"], anchor="middle"))
# right: outer ring turns
cx, cy = 570, 205
b.append(bearing_end(cx, cy, True))
b.append(turn_arrow(cx, cy, 124, RED))
b.append(line(cx, cy + 150, cx, cy + 190, "g-ink", f'style="stroke-width:3" marker-start="url(#arrs-{f})"'))
b.append(text(cx + 10, cy + 186, "load, always this way", "g-b"))
b.append(text(cx, 440, [("g-b", "Case 2: the outer ring turns"), "idler pulley or wheel on a fixed pin", "outer ring turns, load stays still", ("g-b", "outer ring tight: bore K7"), "inner ring normal: pin h6 or g6"], anchor="middle"))
# legend
b.append(f'<rect x="300" y="530" width="18" height="12" fill="{RED}" fill-opacity=".4" stroke="{RED}"/>')
b.append(text(326, 541, "red = the ring that needs the tight fit", "g-s"))
b.append(f'<rect x="300" y="550" width="18" height="12" fill="{BLUE}" fill-opacity=".4" stroke="{BLUE}"/>')
b.append(text(326, 561, "blue = normal fit. Red arrow = what turns.", "g-s"))
write("fig08-rotating-load.svg", svg(f, 760, 575, "Rotating inner ring versus rotating outer ring, and which ring gets the tight fit", "\n".join(b)))

# ---------- 09 bearing 6205 in a housing, half section ----------
f = "brg"
S = 7
AX = 440                     # axis y
def R(mm):
    return AX - mm * S
x0 = 250                     # left face of bearing (against shaft shoulder)
W = 15 * S
b = []
b.append(text(30, 30, "Bearing 6205 on a conveyor drive shaft, half section (corte)", "g-h"))
# housing (upper part), with housing shoulder on the left
hx1, hx2 = x0 - 70, x0 + W + 90
hpath = (f"M{hx1},{R(40)} L{hx2},{R(40)} L{hx2},{R(26)} L{x0},{R(26)} L{x0},{R(23.5)} L{hx1},{R(23.5)} Z")
b.append(f'<path d="{hpath}" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
# shaft
sx1, sx2 = 60, 560
spath = (f"M{sx1},{AX} L{sx1},{R(15)} L{x0},{R(15)} L{x0},{R(12.5)} L{sx2},{R(12.5)} L{sx2},{AX} Z")
b.append(f'<path d="{spath}" fill="url(#hB-{f})" stroke="none"/>')
b.append(f'<polyline points="{sx1},{AX} {sx1},{R(15)} {x0},{R(15)} {x0},{R(12.5)} {sx2},{R(12.5)} {sx2},{AX}" fill="none" stroke="{INK}" stroke-width="2"/>')
# bearing rings
b.append(f'<rect x="{x0}" y="{R(26)}" width="{W}" height="{(26 - 22.2) * S}" fill="url(#hR-{f})" stroke="{INK}" stroke-width="2"/>')
b.append(f'<rect x="{x0}" y="{R(16.3)}" width="{W}" height="{(16.3 - 12.5) * S}" fill="url(#hR-{f})" stroke="{INK}" stroke-width="2"/>')
b.append(f'<circle cx="{x0 + W / 2}" cy="{R(19.25)}" r="{3.97 * S}" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
# axis
b.append(line(40, AX, 590, AX, "g-cl", 'style="stroke-width:1.4"'))
b.append(text(596, AX + 5, "axis (eixo de giro)", "g-s"))
# labels
b.append(leader(f, [(x0 + W + 50, R(26)), (590, 120), (600, 120)]))
b.append(text(606, 110, [("g-b", "Housing bore"), ("g-b", "Ø52 H7"), "52.000 to 52.030", ("g-s g-pt", "furo do mancal")]))
b.append(leader(f, [(x0 + W / 2 + 8, R(19.25) - 6), (590, 250), (600, 250)]))
b.append(text(606, 245, [("g-b", "Bearing 6205"), "25 x 52 x 15 mm", ("g-s g-pt", "rolamento")]))
b.append(leader(f, [(470, R(12.5) + 20), (520, 490), (600, 490)]))
b.append(text(606, 485, [("g-b", "Shaft seat Ø25 k5"), "25.002 to 25.011", ("g-s g-pt", "assento do eixo")]))
b.append(leader(f, [(150, R(15) + 20), (200, 490), (250, 490)]))
b.append(text(30, 485, [("g-b", "Shaft shoulder Ø30"), "at least da min = 30", ("g-s g-pt", "encosto do eixo")]))
b.append(leader(f, [(x0 - 35, R(23.5) - 10), (215, 120), (200, 120)]))
b.append(text(30, 115, [("g-b", "Housing shoulder"), "at most Da max = 47", ("g-s g-pt", "encosto do mancal")]))
b.append(text(30, 580, "Hatching = cut metal. The two shoulders touch only the bearing rings, never the seals.", "g-s"))
b.append(text(30, 600, "Only the upper half is drawn. The lower half is the mirror image. Leaders below the axis point up to the shaft.", "g-s"))
write("fig09-bearing-6205.svg", svg(f, 760, 615, "Bearing 6205 on a shaft and in a housing with the seat fits", "\n".join(b)))

# ---------- 10 shoulder corner detail ----------
f = "shd"
b = []
b.append(text(30, 30, "Close-up of the shoulder corner (canto do encosto), about 25 times real size", "g-h"))
def corner(ox, oy, kind):
    """ox,oy = corner point where shaft seat meets shoulder face"""
    out = []
    left, right, top, bot = ox - 90, ox + 130, oy - 120, oy + 70
    if kind == "fillet_ok":
        r = 16
        shaft = f"M{left},{bot} L{left},{top} L{ox},{top} L{ox},{oy - r} A{r},{r} 0 0,0 {ox + r},{oy} L{right},{oy} L{right},{bot} Z"
    elif kind == "undercut":
        shaft = (f"M{left},{bot} L{left},{top} L{ox},{top} L{ox},{oy - 22} "
                 f"L{ox - 9},{oy - 22} L{ox - 9},{oy + 2} A14,14 0 0,0 {ox + 5},{oy + 16} "
                 f"L{ox + 22},{oy + 16} L{ox + 34},{oy} L{right},{oy} L{right},{bot} Z")
    else:
        r = 42
        shaft = f"M{left},{bot} L{left},{top} L{ox},{top} L{ox},{oy - r} A{r},{r} 0 0,0 {ox + r},{oy} L{right},{oy} L{right},{bot} Z"
    out.append(f'<path d="{shaft}" fill="url(#hB-{f})" stroke="{INK}" stroke-width="2"/>')
    # bearing inner ring with a 25 px corner radius
    rr = 25
    shift = 22 if kind == "fillet_bad" else 0
    rx = ox + shift
    ring = f"M{rx + rr},{oy} L{right},{oy} L{right},{top - 10} L{rx},{top - 10} L{rx},{oy - rr} A{rr},{rr} 0 0,0 {rx + rr},{oy} Z"
    col = RED if kind == "fillet_bad" else INK
    out.append(f'<path d="{ring}" fill="url(#hG-{f})" stroke="{col}" stroke-width="2"/>')
    return "\n".join(out)

b.append(corner(140, 250, "fillet_ok"))
b.append(corner(400, 250, "undercut"))
b.append(corner(650, 250, "fillet_bad"))
for x in (70, 330, 580):
    pass
b.append(text(150, 360, [("g-b", "OK: small fillet"), "shaft radius 1.0 mm max,", "smaller than the ring corner", ("g-s g-pt", "raio de concordância")], anchor="middle"))
b.append(text(410, 360, [("g-b", "OK: undercut"), "a small groove in the corner.", "Best when the seat is ground.", ("g-s g-pt", "rebaixo / canal de alívio")], anchor="middle"))
b.append(text(645, 360, [("g-b", "WRONG: fillet too big"), "the ring sits on the radius,", "not against the shoulder", ("g-s g-pt", "rolamento fora do lugar")], anchor="middle"))
b.append(leader(f, [(175, 180), (230, 90), (250, 90)]))
b.append(text(170, 72, "bearing inner ring", "g-s"))
b.append(leader(f, [(95, 280), (40, 330)]))
b.append(text(30, 345, "shaft", "g-s"))
b.append(leader(f, [(652, 228), (700, 110)], dot=True))
b.append(text(646, 100, "gap here", "g-b", extra=f'style="fill:{RED}"'))
write("fig10-shoulder-detail.svg", svg(f, 760, 440, "Bearing shoulder corner: small fillet, undercut, and a fillet that is too big", "\n".join(b)))
print("figs_b done")
