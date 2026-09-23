"""Build ONE self-contained lesson HTML file.

Lesson folder layout:
  lesson.json        {"title": "...", "subtitle": "...", "output": "Session-3-....html"}
  parts.html         the <section class="part" data-title="..."> blocks (no <html>, no <head>)
  figures/NAME.svg   drawings, referenced in parts.html as {{fig:NAME}}
  photos/photos.json photo list, referenced as {{photo:key}}, {{credit:key}}, {{caption:key}}
  photos/*.jpg

Usage:  python3 build_lesson.py LESSON_DIR
The shell (CSS, navigation, progress bar, comment buttons, copy button, dark mode) comes from
../assets/shell.html. Every photo is resized to <= 640 px, JPEG q70, and embedded as base64.
The build fails on: a {{placeholder}} left over, an em dash, a missing figure or photo.
"""
import base64, io, json, os, re, sys
from PIL import Image

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON = os.path.abspath(sys.argv[1])
meta = json.load(open(os.path.join(LESSON, "lesson.json")))
shell = open(os.path.join(SKILL, "assets", "shell.html")).read()
parts = open(os.path.join(LESSON, "parts.html")).read()
pj = os.path.join(LESSON, "photos", "photos.json")
PHOTOS = json.load(open(pj)) if os.path.exists(pj) else {}


def svg_inline(name):
    s = open(os.path.join(LESSON, "figures", name + ".svg")).read()
    return re.sub(r'(<svg[^>]*?) width="\d+" height="\d+"', r"\1", s, count=1)


def img_data(path, width=640, quality=70):
    im = Image.open(path).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def photo_block(key):
    items = PHOTOS[key]["images"]
    if len(items) == 1:
        it = items[0]
        return f'<div class="pic"><img src="{img_data(os.path.join(LESSON, "photos", it["file"]))}" alt="{it["alt"]}"></div>'
    imgs = "".join(f'<img src="{img_data(os.path.join(LESSON, "photos", it["file"]), 520)}" alt="{it["alt"]}">' for it in items)
    return f'<div class="pair">{imgs}</div>'


def credit(key):
    return '<span class="credit">Photo: ' + " | ".join(it["credit"] for it in PHOTOS[key]["images"]) + "</span>"


# figures get the "sv" class and a swipe hint for phones
parts = parts.replace('<div class="pic">{{fig:', '<div class="pic sv">{{fig:')
parts = re.sub(r'(<div class="pic sv">\{\{fig:[\w-]+\}\}</div>)(\s*)(?!<div class="swipe">)',
               r'\1\2<div class="swipe">Swipe sideways to see the whole drawing.</div>\2', parts)
html = shell.replace("{{PARTS}}", parts).replace("{{TITLE}}", meta["title"]).replace("{{SUBTITLE}}", meta["subtitle"])
html = re.sub(r"\{\{fig:([\w-]+)\}\}", lambda m: svg_inline(m.group(1)), html)
html = re.sub(r"\{\{photo:(\w+)\}\}", lambda m: photo_block(m.group(1)), html)
html = re.sub(r"\{\{credit:(\w+)\}\}", lambda m: credit(m.group(1)), html)
html = re.sub(r"\{\{caption:(\w+)\}\}", lambda m: PHOTOS[m.group(1)]["caption"], html)
left = re.findall(r"\{\{[^}]+\}\}", html)
assert not left, f"placeholders left: {left}"
assert "\u2014" not in html, "em dash found: replace it with a comma, period or colon"
assert "localStorage" not in html and "sessionStorage" not in html, "no browser storage allowed"
out = os.path.join(LESSON, meta["output"])
open(out, "w").write(html)
mb = os.path.getsize(out) / 1e6
print(out, round(mb, 2), "MB")
assert mb < 8, "file too big: shrink photos"
