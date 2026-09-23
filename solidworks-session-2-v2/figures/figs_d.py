from _lib import *

# ---------- 17 diamond pin, two views ----------
f = "dia"
b = [text(30, 30, "Diamond pin (pino losango): side view and top view", "g-h")]
# side view: head (collar) + pin body with a flat band
cx = 190
b.append(f'<rect x="{cx-60}" y="250" width="120" height="30" fill="#d9dde4" stroke="{INK}" stroke-width="2"/>')   # collar
b.append(f'<rect x="{cx-40}" y="280" width="80" height="110" fill="#d9dde4" stroke="{INK}" stroke-width="2"/>')   # shank below
b.append(f'<path d="M{cx-40},250 V110 L{cx-32},96 H{cx+32} L{cx+40},110 V250" fill="#d9dde4" stroke="{INK}" stroke-width="2"/>')  # locating part
b.append(f'<rect x="{cx-34}" y="120" width="68" height="100" fill="#eef0f3" stroke="{INK}" stroke-width="1.4"/>')  # flat face
b.append(line(cx, 80, cx, 405, "g-cl"))
b.append(leader(f, [(cx+37, 170), (300, 120), (318, 120)]))
b.append(text(324, 116, [("g-b", "Narrow round band"), "(left and right edges): the", "only part that touches the hole"], dy=18))
b.append(leader(f, [(cx-10, 160), (80, 80), (60, 80)]))
b.append(text(30, 66, [("g-b", "Flat face, ground away")], dy=18))
b.append(leader(f, [(cx+55, 265), (300, 290), (318, 290)]))
b.append(text(324, 286, [("g-b", "Collar"), "stops at the plate"], dy=18))
b.append(leader(f, [(cx+30, 350), (300, 370), (318, 370)]))
b.append(text(324, 366, [("g-b", "Press-fit shank"), "goes into the base"], dy=18))
b.append(text(cx, 440, "Side view, looking at a flat", "g-b", "middle"))
# top view
tx, ty = 610, 240
b.append(f'<circle cx="{tx}" cy="{ty}" r="70" fill="#ffffff" stroke="{BLUE}" stroke-width="2.4"/>')
b.append(f'<path d="M{tx-26},{ty-65} A70,70 0 0,1 {tx+26},{ty-65} L{tx+26},{ty+65} A70,70 0 0,1 {tx-26},{ty+65} Z" fill="#d9dde4" stroke="{INK}" stroke-width="2"/>')
b.append(line(tx-90, ty, tx+90, ty, "g-cl") + line(tx, ty-90, tx, ty+90, "g-cl"))
b.append(line(tx-110, ty+110, tx+110, ty+110, "g-thin", f'marker-start="url(#arrs-{f})" marker-end="url(#arr-{f})"'))
b.append(text(tx, ty+132, "free: this way", "g-s", "middle"))
b.append(text(tx, 440, "Top view, pin in its hole", "g-b", "middle"))
b.append(text(30, 470, "The band touches the hole only at top and bottom, so the pin stops turning, but allows small errors in the other direction.", "g-s"))
write("fig17-diamond-pin.svg", svg(f, 760, 485, "Diamond pin in side view and top view", "\n".join(b)))

# ---------- 18 linear ball bushing on a shaft, section ----------
f = "lin"
b = [text(30, 30, "Linear ball bushing (bucha linear) on a hardened shaft, cut in half", "g-h")]
L, R_ = 150, 510
top, bot = 130, 330
# shaft
b.append(f'<rect x="40" y="200" width="550" height="60" fill="#dfe3ea" stroke="{INK}" stroke-width="2"/>')
b.append(line(20, 230, 605, 230, "g-cl"))
# outer sleeve, upper and lower, hatched
for y0, y1 in ((143, 177), (283, 317)):
    b.append(f'<rect x="{L}" y="{y0}" width="{R_-L}" height="{y1-y0}" fill="url(#hA-{f})" stroke="{INK}" stroke-width="2"/>')
# ball rows: loaded row touching shaft, return row higher
for yl, yr in ((188, 160), (272, 300)):
    for k in range(13):
        x = L + 22 + k * 26
        b.append(f'<circle cx="{x}" cy="{yl}" r="11" fill="#ffffff" stroke="{INK}" stroke-width="1.6"/>')
    for k in range(11):
        x = L + 48 + k * 26
        b.append(f'<circle cx="{x}" cy="{yr}" r="8" fill="#eef0f3" stroke="{INK}" stroke-width="1.2"/>')
# recirculation arrows
b.append(f'<path d="M{R_-10},{188} C{R_+30},188 {R_+30},160 {R_-20},160" fill="none" stroke="{RED}" stroke-width="2.2" marker-end="url(#arrR-{f})"/>')
b.append(f'<path d="M{L+30},160 C{L-20},160 {L-20},188 {L+10},188" fill="none" stroke="{RED}" stroke-width="2.2" marker-end="url(#arrR-{f})"/>')
# carriage motion arrow
b.append(line(300, 95, 420, 95, "g-ink", f'style="stroke-width:3" marker-end="url(#arr-{f})"'))
b.append(text(360, 82, "the bushing slides", "g-b", "middle"))
# labels
b.append(leader(f, [(480, 150), (600, 110), (612, 110)]))
b.append(text(618, 106, [("g-b", "Outer sleeve"), "sits in an H7 bore"], dy=18))
b.append(leader(f, [(410, 188), (600, 170), (612, 170)]))
b.append(text(618, 166, [("g-b", "Loaded balls"), "roll on the shaft"], dy=18))
b.append(leader(f, [(560, 245), (600, 290), (612, 290)]))
b.append(text(618, 286, [("g-b", "Shaft g6"), "hardened, ground"], dy=18))
b.append(leader(f, [(200, 304), (120, 380), (100, 380)]))
b.append(text(30, 400, [("g-b", "Return balls"), "go back in a loop"], dy=18))
b.append(text(30, 460, "Red arrows: at each end the balls turn and roll back in the return row. Not to scale.", "g-s"))
write("fig18-linear-bushing.svg", svg(f, 760, 475, "Linear ball bushing on a shaft, section, with ball recirculation", "\n".join(b)))
print("figs_d done")
