from _lib import *

# ---------- 01 code anatomy ----------
f = "code"
b = []
b.append(text(380, 44, "A fit code on a drawing has three pieces", "g-h", "middle"))
b.append('<text x="232" y="150" style="font-family:Arial,Helvetica,sans-serif;font-size:72px;font-weight:700;fill:#1f2733">Ø10</text>')
b.append(f'<text x="400" y="150" style="font-family:Arial,Helvetica,sans-serif;font-size:72px;font-weight:700;fill:{BLUE}">H</text>')
b.append(f'<text x="458" y="150" style="font-family:Arial,Helvetica,sans-serif;font-size:72px;font-weight:700;fill:{AMBER}">7</text>')
# brackets
for x1, x2 in [(232, 372), (400, 450), (458, 498)]:
    b.append(f'<polyline class="g-thin" points="{x1},170 {x1},178 {x2},178 {x2},170"/>')
b.append(leader(f, [(302, 178), (302, 200), (130, 222)], dot=False))
b.append(leader(f, [(425, 178), (425, 200), (390, 222)], dot=False))
b.append(leader(f, [(478, 178), (478, 200), (640, 222)], dot=False))
b.append(text(130, 242, [("g-b", "Ø10 = nominal size"), "the round number", "you draw in the model", ("g-s g-pt", "medida nominal")], anchor="middle"))
b.append(text(390, 242, [("g-b", "H = where the band sits"), "capital letter = hole", "small letter = shaft", ("g-s g-pt", "posição / afastamento")], anchor="middle"))
b.append(text(640, 242, [("g-b", "7 = how wide the band is"), "the IT grade", "small number = tight", ("g-s g-pt", "qualidade IT")], anchor="middle"))
write("fig01-code-anatomy.svg", svg(f, 760, 330, "Anatomy of the fit code Ø10 H7", "\n".join(b)))

# ---------- 02 micron scale ----------
f = "um"
S = 3  # px per µm
base = 380
b = []
b.append(text(380, 38, "How big is a tolerance? All four drawn at the same scale.", "g-h", "middle"))
# paper
b.append(f'<rect x="70" y="{base - 100 * S}" width="100" height="{100 * S}" fill="#eef0f3" stroke="{INK}" stroke-width="1.6"/>')
# hair
b.append(f'<circle cx="365" cy="{base - 35 * S}" r="{35 * S}" fill="#b08a62" stroke="#5a4028" stroke-width="1.6"/>')
# H7 band
b.append(f'<rect x="535" y="{base - 15 * S}" width="80" height="{15 * S}" fill="{BLUE}" fill-opacity=".35" stroke="{BLUE}" stroke-width="1.6"/>')
# min gap
b.append(f'<rect x="675" y="{base - 5 * S}" width="50" height="{5 * S}" fill="{GREEN}" fill-opacity=".45" stroke="{GREEN}" stroke-width="1.6"/>')
b.append(line(40, base, 730, base, "g-thin"))
# height dims
b.append(dimv(f, 190, base - 100 * S, base))
b.append(text(198, base - 50 * S, "100 µm", "g-b"))
b.append(dimv(f, 485, base - 70 * S, base))
b.append(text(493, base - 35 * S, "70 µm", "g-b"))
b.append(dimv(f, 632, base - 15 * S, base))
b.append(text(638, base - 10, "15", "g-b"))
b.append(text(120, base + 28, [("g-b", "Sheet of paper"), "seen from its edge", ("g-s g-pt", "folha de papel")], anchor="middle"))
b.append(text(365, base + 28, [("g-b", "Human hair"), "cut across", ("g-s g-pt", "fio de cabelo")], anchor="middle"))
b.append(text(575, base + 28, [("g-b", "Whole H7 band"), "at Ø10: 15 µm", ("g-s g-pt", "campo de tolerância")], anchor="middle"))
b.append(text(702, base + 28, [("g-b", "Smallest gap"), "H7/g6: 5 µm", ("g-s g-pt", "folga mínima")], anchor="middle"))
b.append(text(40, 470, "1 µm (one micrometre, mícron) = 0.001 mm. The H7 band is about 1/5 of a hair.", "g-s"))
write("fig02-micron-scale.svg", svg(f, 760, 485, "15 micrometres next to a hair and a sheet of paper", "\n".join(b)))

# ---------- 03 tolerance zones at Ø10 ----------
f = "zones"
S = 7
Z = 235
def y(um):
    return Z - um * S
b = []
b.append(text(380, 32, "Ø10: one hole band and four shaft bands (1 µm = 0.001 mm)", "g-h", "middle"))
b.append(line(80, y(26), 80, y(-16), "g-ink"))
for v in (20, 10, 0, -10):
    b.append(line(73, y(v), 80, y(v), "g-thin"))
    b.append(text(68, y(v) + 5, f"{v:+d}" if v else "0", "g-s", "end"))
b.append(text(68, y(26) - 4, "µm", "g-s", "end"))
b.append(line(80, Z, 612, Z, "g-cl", 'style="stroke-width:1.6"'))
zones = [("H7 hole", 120, 0, 15, BLUE, "10.015", "10.000"),
         ("g6 shaft", 225, -14, -5, GREEN, "9.995", "9.986"),
         ("h6 shaft", 325, -9, 0, GREEN, "10.000", "9.991"),
         ("k6 shaft", 425, 1, 10, AMBER, "10.010", "10.001"),
         ("p6 shaft", 525, 15, 24, RED, "10.024", "10.015")]
for name, x, lo, hi, col, mx, mn in zones:
    b.append(f'<rect x="{x}" y="{y(hi)}" width="66" height="{(hi - lo) * S}" fill="{col}" fill-opacity=".30" stroke="{col}" stroke-width="1.8"/>')
    b.append(text(x + 33, 372, [("g-b", name), ("g-s", "max " + mx), ("g-s", "min " + mn)], anchor="middle", dy=18))
# legend
b.append(line(632, 120, 632, 80, "g-thin", f'marker-end="url(#arr-{f})"'))
b.append(text(642, 100, ["up =", "bigger size"], "g-s"))
b.append(line(632, 300, 632, 340, "g-thin", f'marker-end="url(#arr-{f})"'))
b.append(text(642, 318, ["down =", "smaller size"], "g-s"))
b.append(leader(f, [(600, Z), (640, 200)], dot=True))
b.append(text(646, 196, ["dash-dot line =", "10.000 exactly"], "g-s"))
write("fig03-tolerance-zones.svg", svg(f, 760, 430, "Tolerance bands of H7, g6, h6, k6 and p6 at 10 mm", "\n".join(b)))

# ---------- 04-06 fit sections (end view, cut across) ----------
def hub(f, cx, cy, half, r):
    return (f'<path d="M{cx - half},{cy - half} h{2 * half} v{2 * half} h{-2 * half} Z {circle_path(cx, cy, r)}" '
            f'fill="url(#hA-{f})" fill-rule="evenodd" stroke="{INK}" stroke-width="2"/>')

def axes(cx, cy, L):
    return line(cx - L, cy, cx + L, cy, "g-cl") + line(cx, cy - L, cx, cy + L, "g-cl")

# clearance
f = "fclr"
cx, cy = 200, 205
b = [text(40, 36, "Clearance fit, H7/g6 at Ø10", "g-h"), text(40, 58, "ajuste com folga: the shaft is always smaller than the hole", "g-s g-pt")]
b.append(hub(f, cx, cy, 125, 100))
b.append(f'<circle cx="{cx}" cy="{cy}" r="100" fill="#fff1b8" stroke="{BLUE}" stroke-width="2.4"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="82" fill="url(#hS-{f})" stroke="{GREEN}" stroke-width="2.4"/>')
b.append(axes(cx, cy, 140))
b.append(leader(f, [(300, 105), (400, 105), (410, 105)]))
b.append(text(418, 100, [("g-b", "Plate or hub, cut"), ("g-s g-pt", "peça em corte")]))
b.append(leader(f, polar_pts := [polar(cx, cy, 100, 40), (400, 150), (410, 150)]))
b.append(text(418, 155, [("g-b", "Hole Ø10 H7"), "10.000 to 10.015 mm", ("g-s g-pt", "furo")]))
b.append(leader(f, [(cx + 40, cy + 30), (400, 245), (410, 245)]))
b.append(text(418, 240, [("g-b", "Shaft Ø10 g6"), "9.986 to 9.995 mm", ("g-s g-pt", "eixo")]))
b.append(leader(f, [polar(cx, cy, 91, -35), (400, 320), (410, 320)]))
b.append(text(418, 318, [("g-b", "Gap, always there"), "5 to 29 µm", ("g-s g-pt", "folga")]))
b.append(text(40, 372, "The gap is drawn hundreds of times bigger than real, so you can see it.", "g-s"))
write("fig04-fit-clearance.svg", svg(f, 760, 390, "Clearance fit: shaft inside hole with a gap", "\n".join(b)))

# transition
f = "ftr"
b = [text(40, 36, "Transition fit, H7/k6 at Ø10", "g-h"), text(40, 58, "ajuste incerto: sometimes a tiny gap, sometimes a tiny press", "g-s g-pt")]
for cx, rs, lab in [(150, 64, "A"), (440, 84, "B")]:
    cy = 200
    b.append(hub(f, cx, cy, 100, 76))
    if rs < 76:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="76" fill="#fff1b8" stroke="{BLUE}" stroke-width="2.4"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{rs}" fill="url(#hS-{f})" stroke="{GREEN}" stroke-width="2.4"/>')
    else:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{rs}" fill="url(#hS-{f})" stroke="{GREEN}" stroke-width="2.4"/>')
        b.append(f'<path d="{annulus(cx, cy, 76, rs)}" fill="{RED}" fill-opacity=".55" fill-rule="evenodd"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="76" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="6 4"/>')
    b.append(axes(cx, cy, 115))
b.append(text(150, 335, [("g-b", "Case A"), "biggest hole, smallest shaft", "gap up to 14 µm"], anchor="middle"))
b.append(text(440, 335, [("g-b", "Case B"), "smallest hole, biggest shaft", "press up to 10 µm"], anchor="middle"))
b.append(leader(f, [polar(150, 200, 70, 45), (268, 90), (290, 90)]))
b.append(text(296, 95, "gap", "g-b"))
b.append(leader(f, [polar(440, 200, 80, 40), (566, 110), (580, 110)]))
b.append(text(586, 106, [("g-b", "red ring ="), "overlap, the", "parts squeeze"]))
b.append(text(586, 190, [("g-b", "Hole H7"), "10.000 to 10.015", ("g-b", "Shaft k6"), "10.001 to 10.010"]))
b.append(text(586, 290, ["You only know", "which case you", "get when you", "measure the parts."], "g-s"))
b.append(text(40, 410, "Sizes drawn hundreds of times bigger than real. Dashed blue circle = where the hole wall is.", "g-s"))
write("fig05-fit-transition.svg", svg(f, 760, 425, "Transition fit: small gap in one case, small press in the other", "\n".join(b)))

# interference
f = "fint"
cx, cy = 200, 205
b = [text(40, 36, "Interference fit, H7/p6 at Ø10", "g-h"), text(40, 58, "ajuste com interferência: the shaft is always bigger than the hole", "g-s g-pt")]
b.append(hub(f, cx, cy, 125, 90))
b.append(f'<circle cx="{cx}" cy="{cy}" r="104" fill="url(#hS-{f})" stroke="{GREEN}" stroke-width="2.4" stroke-dasharray="9 5"/>')
b.append(f'<path d="{annulus(cx, cy, 90, 104)}" fill="{RED}" fill-opacity=".55" fill-rule="evenodd"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="90" fill="none" stroke="{BLUE}" stroke-width="2.4"/>')
b.append(axes(cx, cy, 140))
b.append(leader(f, [(300, 100), (400, 100), (410, 100)]))
b.append(text(418, 95, [("g-b", "Plate or hub, cut"), ("g-s g-pt", "peça em corte")]))
b.append(leader(f, [polar(cx, cy, 90, 30), (400, 160), (410, 160)]))
b.append(text(418, 155, [("g-b", "Hole Ø10 H7"), "10.000 to 10.015 mm", ("g-s g-pt", "furo")]))
b.append(leader(f, [(cx + 30, cy + 40), (400, 250), (410, 250)]))
b.append(text(418, 245, [("g-b", "Shaft Ø10 p6, before press"), "10.015 to 10.024 mm", ("g-s g-pt", "eixo, antes de prensar")]))
b.append(leader(f, [polar(cx, cy, 97, -40), (400, 330), (410, 330)]))
b.append(text(418, 325, [("g-b", "Red ring = interference"), "0 to 24 µm of metal that", "must squeeze. This grip", "holds the shaft."]))
b.append(text(40, 405, "Dashed green = the shaft before you press it. Blue = the hole wall. Not to scale.", "g-s"))
write("fig06-fit-interference.svg", svg(f, 760, 420, "Interference fit: shaft bigger than hole, overlap shown in red", "\n".join(b)))
print("figs_a done")
