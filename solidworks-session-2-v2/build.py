"""Build the single-file lesson: inline every SVG figure and every photo (base64)."""
import base64, io, json, os, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "lesson.src.html")
OUT = os.path.join(HERE, "Session-2-Hole-Tolerances-and-Fits-v2.html")
FIG = os.path.join(HERE, "figures")
PHOTOS = json.load(open(os.path.join(HERE, "photos", "photos.json")))


def svg_inline(name):
    s = open(os.path.join(FIG, name + ".svg")).read()
    # the page sets the size, so drop the fixed width/height
    s = re.sub(r'(<svg[^>]*?) width="\d+" height="\d+"', r"\1", s, count=1)
    return s


def img_data(path, width=640, quality=70):
    im = Image.open(path).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def photo_block(key):
    p = PHOTOS[key]
    items = p["images"]
    if len(items) == 1:
        it = items[0]
        return f'<div class="pic"><img src="{img_data(os.path.join(HERE, "photos", it["file"]))}" alt="{it["alt"]}"></div>'
    imgs = "".join(
        f'<img src="{img_data(os.path.join(HERE, "photos", it["file"]), width=520)}" alt="{it["alt"]}">' for it in items)
    return f'<div class="pair">{imgs}</div>'


def credit(key):
    parts = [f'{it["credit"]}' for it in PHOTOS[key]["images"]]
    return '<span class="credit">Photo: ' + " | ".join(parts) + "</span>"


html = open(SRC).read()
html = re.sub(r"\{\{fig:([\w-]+)\}\}", lambda m: svg_inline(m.group(1)), html)
html = re.sub(r"\{\{photo:(\w+)\}\}", lambda m: photo_block(m.group(1)), html)
html = re.sub(r"\{\{credit:(\w+)\}\}", lambda m: credit(m.group(1)), html)
html = re.sub(r"\{\{caption:(\w+)\}\}", lambda m: PHOTOS[m.group(1)]["caption"], html)
left = re.findall(r"\{\{[^}]+\}\}", html)
assert not left, left
assert "—" not in html, "em dash found"
open(OUT, "w").write(html)
print(OUT, round(os.path.getsize(OUT) / 1e6, 2), "MB")
