from _lib import *

# ---------- 11 dowel pin in two plates, section ----------
f = "dws"
S = 9                   # px per mm
b = []
b.append(text(30, 30, "Dowel pin Ø8 in a fixture plate and a base, section (corte)", "g-h"))
top, mid, bot = 125, 125 + 12 * S, 125 + 12 * S + 20 * S      # 12 mm top plate, 20 mm base
L, Rr = 60, 470
pc = 265                # pin centre x
pr = 4 * S              # pin radius
# plates with the hole cut out
b.append(f'<path d="M{L},{top} H{pc - pr} V{mid} H{L} Z M{pc + pr},{top} H{Rr} V{mid} H{pc + pr} Z" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
b.append(f'<path d="M{L},{mid} H{pc - pr} V{bot} H{L} Z M{pc + pr},{mid} H{Rr} V{bot} H{pc + pr} Z" fill="url(#hB-{f})" stroke="{INK}" stroke-width="2"/>')
# pin: 20 mm long, 10 in each plate, not hatched (standard for pins cut along the axis)
p_top, p_bot = mid - 10 * S, mid + 10 * S
ch = 6
b.append(f'<path d="M{pc - pr + ch},{p_top} H{pc + pr - ch} L{pc + pr},{p_top + ch} V{p_bot - ch} L{pc + pr - ch},{p_bot} H{pc - pr + ch} L{pc - pr},{p_bot - ch} V{p_top + ch} Z" fill="#d9dde4" stroke="{INK}" stroke-width="2"/>')
b.append(line(pc, top - 20, pc, bot + 20, "g-cl"))
# engagement dimensions on the right of the plates
xd = Rr + 30
for y in (p_top, mid, p_bot):
    b.append(line(pc + pr + 4, y, xd + 8, y, "g-thin"))
b.append(dimv(f, xd, p_top, mid))
b.append(dimv(f, xd, mid, p_bot))
b.append(text(xd + 14, (p_top + mid) / 2 - 4, [("g-b", "10 mm in the top plate"), "1 to 1.5 x d = 8 to 12 mm"], dy=18))
b.append(text(xd + 14, (mid + p_bot) / 2 - 4, [("g-b", "10 mm in the base"), "1 to 1.5 x d = 8 to 12 mm"], dy=18))
# pin diameter
b.append(line(pc - pr, bot + 8, pc - pr, bot + 46, "g-thin") + line(pc + pr, bot + 8, pc + pr, bot + 46, "g-thin"))
b.append(dimh(f, bot + 38, pc - pr, pc + pr))
# labels
b.append(leader(f, [(120, top + 30), (40, top - 20)], dot=True))
b.append(text(30, top - 28, "Fixture plate, 12 mm", "g-b"))
b.append(leader(f, [(120, bot - 40), (40, bot + 40)], dot=True))
b.append(text(30, bot + 58, [("g-b", "Base, 20 mm"), ("g-s g-pt", "base / placa")]))
b.append(leader(f, [(pc, p_top + 40), (360, top - 64), (380, top - 64)]))
b.append(text(386, top - 68, [("g-b", "Pin Ø8 m6, ISO 8734"), "8.006 to 8.015 mm", ("g-s g-pt", "pino de guia, temperado e retificado")], dy=18))
b.append(leader(f, [(pc + pr, bot - 30), (400, bot + 70), (420, bot + 70)]))
b.append(text(426, bot + 66, [("g-b", "Holes Ø8 H7, reamed through"), "8.000 to 8.015 mm", ("g-s g-pt", "furo alargado, passante")], dy=18))
b.append(text(pc, bot + 70, "d = 8", "g-b", "middle"))
b.append(text(30, 590, "The pin is not hatched: by drawing rules, pins and shafts cut along their axis are drawn plain.", "g-s"))
write("fig11-dowel-section.svg", svg(f, 760, 605, "Dowel pin in two plates, section view, with engagement depth", "\n".join(b)))

# ---------- 12 dowel layout top view ----------
f = "dwl"
b = []
b.append(text(30, 30, "Fixture plate from above: one round hole, one slot", "g-h"))
b.append(f'<rect x="60" y="80" width="480" height="170" fill="#f7f8fa" stroke="{INK}" stroke-width="2"/>')
h1, h2, yc = 130, 480, 165
b.append(f'<circle cx="{h1}" cy="{yc}" r="18" fill="#ffffff" stroke="{BLUE}" stroke-width="2.4"/>')
b.append(f'<circle cx="{h1}" cy="{yc}" r="14" fill="#d9dde4" stroke="{INK}" stroke-width="1.6"/>')
b.append(f'<rect x="{h2 - 34}" y="{yc - 18}" width="68" height="36" rx="18" fill="#ffffff" stroke="{BLUE}" stroke-width="2.4"/>')
b.append(f'<circle cx="{h2}" cy="{yc}" r="14" fill="#d9dde4" stroke="{INK}" stroke-width="1.6"/>')
for x in (h1, h2):
    b.append(line(x - 34 if x == h1 else x - 50, yc, x + 34 if x == h1 else x + 50, yc, "g-cl"))
    b.append(line(x, yc - 34, x, yc + 34, "g-cl"))
# screws
for sx, sy in ((230, 115), (390, 115), (230, 215), (390, 215)):
    b.append(f'<circle cx="{sx}" cy="{sy}" r="11" fill="#ffffff" stroke="{INK}" stroke-width="1.6"/><circle cx="{sx}" cy="{sy}" r="5" fill="none" stroke="{INK}" stroke-width="1.2"/>')
# spacing dim
b.append(line(h1, yc + 34, h1, 300, "g-thin") + line(h2, yc + 34, h2, 300, "g-thin"))
b.append(dimh(f, 292, h1, h2))
b.append(text((h1 + h2) / 2, 285, "as far apart as you can", "g-b", "middle"))
# labels
b.append(leader(f, [(h1 + 12, yc - 14), (180, 60), (200, 60)]))
b.append(text(206, 56, [("g-b", "Round hole Ø8 H7: this pin locates (localiza)")]))
b.append(leader(f, [(h2 + 30, yc - 10), (575, 110), (585, 110)]))
b.append(text(591, 106, [("g-b", "Slot (rasgo)"), "8 H7 wide, long in", "the direction of", "the other pin"], dy=18))
b.append(leader(f, [(390, 226), (575, 235), (585, 235)]))
b.append(text(591, 231, [("g-b", "Screws"), "they clamp,", "they do not locate"], dy=18))
# diamond pin inset
b.append(text(30, 345, "Other way: two round holes, and a diamond pin (pino losango) in the second one.", "g-b"))
dx, dy = 150, 420
b.append(f'<circle cx="{dx}" cy="{dy}" r="40" fill="#ffffff" stroke="{BLUE}" stroke-width="2.4"/>')
b.append(f'<path d="M{dx - 12},{dy - 38} A38,38 0 0,1 {dx + 12},{dy - 38} L{dx + 12},{dy + 38} A38,38 0 0,1 {dx - 12},{dy + 38} Z" fill="#d9dde4" stroke="{INK}" stroke-width="1.8"/>')
b.append(line(dx - 55, dy, dx + 55, dy, "g-cl") + line(dx, dy - 55, dx, dy + 55, "g-cl"))
b.append(leader(f, [(dx + 12, dy - 20), (250, 390), (262, 390)]))
b.append(text(268, 386, [("g-b", "Diamond pin, seen from above"), "only two narrow bands touch the hole.", "It stops turning, but it lets the", "centre distance be a little off."], dy=18))
write("fig12-dowel-layout.svg", svg(f, 760, 480, "Top view of a plate with a round dowel hole, a slot and a diamond pin option", "\n".join(b)))

# ---------- 13 drill then ream ----------
f = "drm"
b = []
b.append(text(30, 30, "Drill, then ream: how the shop makes an Ø8 H7 hole", "g-h"))

def plate_with_hole(cx, hw, rough):
    top, bot = 250, 360
    out = []
    left, right = cx - 110, cx + 110
    if rough:
        # wavy hole wall
        lw = " ".join(f"L{cx - hw + (2 if k % 2 else -1)},{top + k * 10}" for k in range(12))
        rw = " ".join(f"L{cx + hw + (-2 if k % 2 else 1)},{bot - k * 10}" for k in range(12))
        out.append(f'<path d="M{left},{top} H{cx - hw} {lw} L{cx - hw},{bot} H{left} Z" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
        rw = " ".join(f"L{cx + hw + (-2 if k % 2 else 1)},{top + k * 10}" for k in range(12))
        out.append(f'<path d="M{right},{top} H{cx + hw} {rw} L{cx + hw},{bot} H{right} Z" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
    else:
        out.append(f'<path d="M{left},{top} H{cx - hw} V{bot} H{left} Z M{cx + hw},{top} H{right} V{bot} H{cx + hw} Z" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
    out.append(line(cx, 60, cx, bot + 15, "g-cl"))
    return "\n".join(out)

# step 1: twist drill
cx = 140
b.append(plate_with_hole(cx, 26, True))
b.append(f'<path d="M{cx - 24},70 V300 L{cx},322 L{cx + 24},300 V70 Z" fill="#c9ced8" stroke="{INK}" stroke-width="1.8"/>')
for k in range(7):
    y0 = 80 + k * 32
    b.append(f'<path d="M{cx - 24},{y0} L{cx + 24},{y0 + 24}" stroke="{INK}" stroke-width="1.4"/>')
b.append(text(cx, 395, [("g-b", "Step 1: drill Ø7.8"), "0.2 mm under size", "rough wall, size not exact", "(about IT11 to IT13)", ("g-s g-pt", "furar com broca")], anchor="middle"))
# step 2: reamer
cx = 390
b.append(plate_with_hole(cx, 28, False))
b.append(f'<path d="M{cx - 27},70 V304 L{cx - 20},318 H{cx + 20} L{cx + 27},304 V70 Z" fill="#c9ced8" stroke="{INK}" stroke-width="1.8"/>')
for dx in (-16, -6, 4, 14):
    b.append(line(cx + dx, 78, cx + dx, 300, "g-thin", 'style="stroke-width:1.4"'))
b.append(text(cx, 395, [("g-b", "Step 2: ream Ø8 H7"), "straight flutes", "take off the last 0.2 mm", "slow speed, with oil", ("g-s g-pt", "alargar com alargador")], anchor="middle"))
# step 3: result
cx = 630
b.append(plate_with_hole(cx, 28, False))
b.append(line(cx - 28, 225, cx - 28, 245, "g-thin") + line(cx + 28, 225, cx + 28, 245, "g-thin"))
b.append(dimh(f, 232, cx - 28, cx + 28))
b.append(text(cx, 215, "Ø8 H7", "g-b", "middle"))
b.append(text(cx, 395, [("g-b", "Result"), "8.000 to 8.015 mm", "smooth and round", "the pin fits every time", ("g-s g-pt", "furo pronto")], anchor="middle"))
b.append(text(140 + 32, 90, "twist drill (broca)", "g-s"))
b.append(text(390 + 34, 90, "machine reamer", "g-s"))
b.append(text(390 + 34, 106, "(alargador)", "g-s g-pt"))
write("fig13-drill-then-ream.svg", svg(f, 760, 500, "Drill undersize, then ream to H7", "\n".join(b)))

# ---------- 14 bronze bushing before and after pressing ----------
f = "bsh"
b = []
b.append(text(30, 30, "Bronze bushing (bucha de bronze): before and after pressing, section", "g-h"))
def housing(cx, bore_half, top=230, bot=380):
    return (f'<path d="M{cx - 150},{top} H{cx - bore_half} V{bot} H{cx - 150} Z M{cx + bore_half},{top} H{cx + 150} V{bot} H{cx + bore_half} Z" '
            f'fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
# before
cx = 190
b.append(housing(cx, 60))
b.append(f'<path d="M{cx - 66},70 H{cx - 42} V200 H{cx - 66} Z M{cx + 42},70 H{cx + 66} V200 H{cx + 42} Z" fill="url(#hC-{f})" stroke="{BRONZE}" stroke-width="2"/>')
b.append(line(cx, 55, cx, 395, "g-cl"))
b.append(line(cx, 206, cx, 226, "g-ink", f'style="stroke-width:3" marker-end="url(#arr-{f})"'))
b.append(text(cx + 10, 222, "press", "g-b"))
b.append(line(cx - 42, 60, cx - 42, 44, "g-thin") + line(cx + 42, 60, cx + 42, 44, "g-thin"))
b.append(dimh(f, 52, cx - 42, cx + 42))
b.append(text(cx + 50, 57, "bore as bought", "g-s"))
b.append(text(cx, 420, [("g-b", "Before"), "the outside of the bushing is a", "little bigger than the housing bore"], anchor="middle"))
# after
cx = 560
b.append(housing(cx, 60))
b.append(f'<path d="M{cx - 60},240 H{cx - 34} V370 H{cx - 60} Z M{cx + 34},240 H{cx + 60} V370 H{cx + 34} Z" fill="url(#hC-{f})" stroke="{BRONZE}" stroke-width="2"/>')
b.append(line(cx - 42, 225, cx - 42, 385, "g-hid") + line(cx + 42, 225, cx + 42, 385, "g-hid"))
b.append(line(cx, 55, cx, 395, "g-cl"))
for y in (275, 335):
    b.append(line(cx - 10, y, cx - 30, y, "g-ink", f'style="stroke:{RED};stroke-width:2.6" marker-end="url(#arrR-{f})"'))
    b.append(line(cx + 10, y, cx + 30, y, "g-ink", f'style="stroke:{RED};stroke-width:2.6" marker-end="url(#arrR-{f})"'))
b.append(leader(f, [(cx + 42, 232), (cx + 42, 200), (608, 110), (616, 110)]))
b.append(text(622, 100, [("g-b", "dashed line ="), "bore before", "pressing"], dy=18))
b.append(leader(f, [(cx + 34, 300), (cx + 20, 215), (608, 190), (616, 190)]))
b.append(text(622, 186, [("g-b", "bore now"), "smaller"], dy=18, extra=f'style="fill:{RED}"'))
b.append(leader(f, [(cx - 110, 260), (470, 120), (460, 120)]))
b.append(text(370, 100, [("g-b", "Housing"), "bore H7", ("g-s g-pt", "mancal")], dy=18))
b.append(text(cx, 420, [("g-b", "After"), "the housing squeezes the bushing,", "so the bore closes in (fecha)"], anchor="middle"))
b.append(text(30, 490, "Sizes drawn much bigger than real. Fix: use the maker's after-press bore size, or ream the bore after pressing.", "g-s"))
write("fig14-bushing-press.svg", svg(f, 760, 505, "Bronze bushing before and after pressing, the bore gets smaller", "\n".join(b)))

# ---------- 15 drawing corner with the general note ----------
f = "drw"
b = []
b.append(text(30, 30, "Bottom right corner of a drawing sheet (folha de desenho)", "g-h"))
X0, Y0, X1, Y1 = 250, 50, 745, 470
b.append(f'<rect x="{X0}" y="{Y0}" width="{X1 - X0}" height="{Y1 - Y0}" fill="#ffffff" stroke="{INK}" stroke-width="2.2"/>')
# a small part view: plate with hole
b.append(f'<rect x="290" y="90" width="200" height="110" fill="none" stroke="{INK}" stroke-width="2"/>')
b.append(f'<circle cx="390" cy="145" r="18" fill="none" stroke="{INK}" stroke-width="2"/>')
b.append(line(362, 145, 418, 145, "g-cl") + line(390, 117, 390, 173, "g-cl"))
b.append(line(290, 205, 290, 235, "g-thin") + line(490, 205, 490, 235, "g-thin"))
b.append(dimh(f, 228, 290, 490))
b.append(text(390, 222, "100", "g-t", "middle"))
b.append(f'<polyline class="g-thin" points="403,132 440,97 510,97" marker-start="url(#arrs-{f})"/>')
b.append(text(446, 90, "Ø10 H7", "g-t"))
# notes
b.append(text(280, 300, "NOTES:", "g-b"))
b.append('<text x="280" y="322" style="font:13px Arial;fill:#1f2733">1. UNLESS OTHERWISE STATED:</text>')
b.append('<text x="296" y="340" style="font:13px Arial;fill:#1f2733">GENERAL TOLERANCES ISO 2768-m</text>')
b.append('<text x="280" y="360" style="font:13px Arial;fill:#1f2733">2. BREAK ALL SHARP EDGES 0.3 MAX</text>')
b.append('<text x="296" y="378" style="font:13px Arial;fill:#1f2733">(QUEBRAR CANTOS VIVOS)</text>')
# title block
tx, ty = 540, 385
b.append(f'<rect x="{tx}" y="{ty}" width="{X1 - tx}" height="{Y1 - ty}" fill="#f7f8fa" stroke="{INK}" stroke-width="2"/>')
for yy in (ty + 28, ty + 65):
    b.append(line(tx, yy, X1, yy, "g-thin"))
b.append(line(tx + 100, ty + 28, tx + 100, Y1, "g-thin"))
b.append('<text x="548" y="405" style="font:700 13px Arial;fill:#1f2733">FIXTURE PLATE  FP-01</text>')
b.append('<text x="548" y="428" style="font:11px Arial;fill:#4a5566">MATERIAL</text><text x="548" y="444" style="font:12px Arial;fill:#1f2733">SAE 1045</text>')
b.append('<text x="648" y="428" style="font:11px Arial;fill:#4a5566">SCALE</text><text x="648" y="444" style="font:12px Arial;fill:#1f2733">1:1</text>')
b.append('<text x="548" y="465" style="font:11px Arial;fill:#4a5566">DRAWN: ADEL</text><text x="648" y="465" style="font:11px Arial;fill:#4a5566">SHEET 1/1  A4</text>')
# explanations outside the sheet
b.append(leader(f, [(452, 73), (440, 62), (230, 62)], dot=True))
b.append(text(30, 66, [("g-b", "Fit written on the size"), "the note does not apply here"], dy=18))
b.append(leader(f, [(340, 228), (230, 170)], dot=True))
b.append(text(30, 166, [("g-b", "No tolerance written"), "the note gives it: ±0.3", "(30 to 120 mm, class m)"], dy=18))
b.append(leader(f, [(282, 330), (230, 300)], dot=True))
b.append(text(30, 296, [("g-b", "General tolerance note"), "covers every size with", "no tolerance of its own", ("g-s g-pt", "nota de tolerância geral")], dy=18))
b.append(leader(f, [(540, 450), (500, 500), (230, 500)], dot=True))
b.append(text(30, 496, [("g-b", "Title block (legenda)"), "put the notes near it"], dy=18))
write("fig15-drawing-note.svg", svg(f, 760, 545, "Corner of a drawing with the ISO 2768-m general tolerance note and the title block", "\n".join(b)))
print("figs_c done")

# ---------- 16 which fit, decision path ----------
f = "dec"
b = []
b.append(text(30, 30, "Which fit? Ask these questions in this order.", "g-h"))
def box(x, y, w, h, lines, fill="#f3f6fb", stroke=INK):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>']
    out.append(text(x + 12, y + 22, lines, dy=18))
    return "\n".join(out)
qs = [(60, ["1. Does it touch a bought part?", "bearing, pin, bushing"], ["Use the maker's number,", "or the cheat sheet row."]),
      (150, ["2. Must it move?", "turn or slide"], ["Clearance: H7/g6 slides,", "H8/f7 turns."]),
      (240, ["3. Must it sit exactly and", "still come apart for service?"], ["H7/h6 by hand,", "H7/k6 with a light tap."]),
      (330, ["4. Must it never move and", "never come apart?"], ["Interference:", "H7/p6, or H7/s6."])]
for y, q, a in qs:
    b.append(box(40, y, 290, 66, [("g-b", q[0]), q[1]]))
    b.append(line(330, y + 33, 420, y + 33, "g-ink", f'marker-end="url(#arr-{f})"'))
    b.append(text(360, y + 26, "yes", "g-b", "middle"))
    b.append(box(424, y, 300, 66, [("g-b", a[0]), a[1]], fill="#eaf5ee", stroke=GREEN))
    if y < 330:
        b.append(line(185, y + 66, 185, y + 88, "g-ink", f'marker-end="url(#arr-{f})"'))
        b.append(text(195, y + 83, "no", "g-s"))
b.append(line(185, 396, 185, 420, "g-ink", f'marker-end="url(#arr-{f})"'))
b.append(text(195, 415, "no", "g-s"))
b.append(box(40, 422, 684, 50, [("g-b", "None of these? No fit class. The general note ISO 2768-m covers it."), "Most sizes on a drawing end up here, and that keeps the part cheap."], fill="#fdf1e0", stroke=AMBER))
write("fig16-which-fit.svg", svg(f, 760, 490, "Decision path: which fit to use", "\n".join(b)))
print("fig16 done")
