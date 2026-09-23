from _lib import *

# ---------- 19 parts of a ball bearing ----------
f = "bp"
b = [text(30, 30, "The parts of a deep groove ball bearing: front view and cut view", "g-h")]
cx, cy = 200, 250
b.append(f'<path d="{annulus(cx, cy, 128, 150)}" fill="#d9dde4" fill-rule="evenodd" stroke="{INK}" stroke-width="2"/>')
b.append(f'<path d="{annulus(cx, cy, 62, 86)}" fill="#d9dde4" fill-rule="evenodd" stroke="{INK}" stroke-width="2"/>')
b.append(f'<path d="{annulus(cx, cy, 98, 116)}" fill="none" fill-rule="evenodd" stroke="{AMBER}" stroke-width="2"/>')
for k in range(9):
    px, py = polar(cx, cy, 107, k * 40 + 20)
    b.append(f'<circle cx="{px}" cy="{py}" r="17" fill="#f4f5f7" stroke="{INK}" stroke-width="1.8"/>')
b.append(line(cx - 170, cy, cx + 170, cy, "g-cl") + line(cx, cy - 170, cx, cy + 170, "g-cl"))
b.append(text(cx, 440, "Front view (seal removed)", "g-b", "middle"))
# section view, upper half ring pair
sx, sy = 560, 250
def ring_sec(y0, y1, groove_y, up):
    # rectangle with a round groove on the ball side
    return f'<rect x="{sx-45}" y="{y0}" width="90" height="{y1-y0}" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>'
for sign in (-1, 1):
    oy0, oy1 = sy + sign * 150, sy + sign * 118
    iy0, iy1 = sy + sign * 86, sy + sign * 62
    b.append(f'<rect x="{sx-45}" y="{min(oy0,oy1)}" width="90" height="32" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<rect x="{sx-45}" y="{min(iy0,iy1)}" width="90" height="24" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
    by = sy + sign * 102
    b.append(f'<circle cx="{sx}" cy="{by}" r="22" fill="#f4f5f7" stroke="{INK}" stroke-width="2"/>')
    # seals
    b.append(f'<rect x="{sx-45}" y="{min(sy+sign*118, sy+sign*86)}" width="5" height="32" fill="{INK}"/>')
    b.append(f'<rect x="{sx+40}" y="{min(sy+sign*118, sy+sign*86)}" width="5" height="32" fill="{INK}"/>')
b.append(line(sx - 80, sy, sx + 80, sy, "g-cl"))
b.append(text(sx, 440, "Cut view (corte), with seals", "g-b", "middle"))
# labels between views
b.append(leader(f, [polar(cx, cy, 140, 60), (300, 70), (375, 70)]))
b.append(text(381, 66, [("g-b", "Outer ring"), ("g-s g-pt", "anel externo")], dy=18))
b.append(leader(f, [polar(cx, cy, 107, 20), (330, 141), (375, 141)]))
b.append(text(381, 146, [("g-b", "Ball"), ("g-s g-pt", "esfera")], dy=18))
b.append(leader(f, [polar(cx, cy, 98, -8), (330, 231), (375, 231)]))
b.append(text(381, 236, [("g-b", "Cage"), ("g-s g-pt", "gaiola")], dy=18))
b.append(leader(f, [polar(cx, cy, 74, -40), (330, 321), (375, 321)]))
b.append(text(381, 326, [("g-b", "Inner ring"), ("g-s g-pt", "anel interno")], dy=18))
b.append(leader(f, [(sx + 43, sy - 100), (660, 80), (672, 80)]))
b.append(text(678, 76, [("g-b", "Seal"), ("g-s g-pt", "vedação")], dy=18))
b.append(leader(f, [(sx, sy - 102), (660, 170), (672, 170)]))
b.append(text(678, 166, [("g-b", "Ball in"), "its groove"], dy=18))
b.append(leader(f, [(sx + 30, sy + 74), (660, 330), (672, 330)]))
b.append(text(678, 326, [("g-b", "Bore"), "on the shaft"], dy=18))
write("fig19-bearing-parts.svg", svg(f, 760, 460, "Parts of a deep groove ball bearing, front view and section", "\n".join(b)))

# ---------- 20 UCP pillow block unit ----------
f = "ucp"
b = [text(30, 30, "Pillow block unit, UCP type (mancal com rolamento)", "g-h")]
cx, cy = 260, 200
# base foot
b.append(f'<path d="M60,330 H460 V300 H380 L350,290 H170 L140,300 H60 Z" fill="#b9c0cb" stroke="{INK}" stroke-width="2"/>')
b.append(f'<path d="M150,300 C150,160 170,95 {cx},95 C350,95 370,160 370,300 Z" fill="#b9c0cb" stroke="{INK}" stroke-width="2"/>')
# bolt slots
for x in (100, 420):
    b.append(f'<rect x="{x-16}" y="304" width="32" height="18" rx="9" fill="#ffffff" stroke="{INK}" stroke-width="1.6"/>')
# bearing insert
b.append(f'<circle cx="{cx}" cy="{cy}" r="70" fill="#dfe3ea" stroke="{INK}" stroke-width="2"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="44" fill="#eef0f3" stroke="{INK}" stroke-width="1.6"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="28" fill="#ffffff" stroke="{GREEN}" stroke-width="2"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="url(#hS-{f})" stroke="{GREEN}" stroke-width="1.6"/>')
# grease nipple and set screw
b.append(f'<rect x="{cx-6}" y="72" width="12" height="24" fill="#8a93a3" stroke="{INK}"/><circle cx="{cx}" cy="68" r="7" fill="#8a93a3" stroke="{INK}"/>')
b.append(f'<rect x="{cx+30}" y="{cy-40}" width="12" height="14" transform="rotate(35 {cx+36} {cy-33})" fill="{INK}"/>')
b.append(line(cx - 110, cy, cx + 110, cy, "g-cl") + line(cx, cy - 150, cx, cy + 150, "g-cl"))
b.append(leader(f, [(cx, 66), (430, 60), (500, 60)]))
b.append(text(506, 56, [("g-b", "Grease nipple"), ("g-s g-pt", "graxeira")], dy=18))
b.append(leader(f, [(cx + 40, cy - 34), (440, 135), (500, 135)]))
b.append(text(506, 131, [("g-b", "Set screw"), "locks the insert to the shaft", ("g-s g-pt", "parafuso de fixação")], dy=18))
b.append(leader(f, [(cx + 58, cy + 40), (440, 225), (500, 225)]))
b.append(text(506, 221, [("g-b", "Bearing insert"), "a ball bearing with a", "round outside", ("g-s g-pt", "rolamento de inserção")], dy=18))
b.append(leader(f, [(cx - 12, cy + 10), (170, 400), (150, 400)]))
b.append(text(30, 396, [("g-b", "Shaft"), "tolerance from", "the maker"], dy=18))
b.append(leader(f, [(362, 280), (440, 311), (500, 311)]))
b.append(text(506, 316, [("g-b", "Cast iron housing"), "bolted to the frame", ("g-s g-pt", "caixa de ferro fundido")], dy=18))
write("fig20-pillow-block.svg", svg(f, 760, 460, "UCP pillow block unit with its parts named", "\n".join(b)))
print("figs_e done")
