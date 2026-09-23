"""Render SVG files (or a lesson HTML page) to PNG so you can LOOK at them before sending.

Usage:
  python3 render_svg.py OUT_DIR fig01.svg fig02.svg ...
  python3 render_svg.py OUT_DIR --page lesson.html        # phone (390 px) and desktop screenshots of every part

Uses the pre-installed Chromium if it exists (claude.ai cloud containers), else Playwright's default.
"""
import os, sys
from playwright.sync_api import sync_playwright

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
args = sys.argv[2:]

with sync_playwright() as p:
    kw = {"executable_path": CHROME} if os.path.exists(CHROME) else {}
    b = p.chromium.launch(**kw)
    if args and args[0] == "--page":
        page_file = os.path.abspath(args[1])
        for name, w in (("phone", 390), ("desktop", 900)):
            pg = b.new_page(viewport={"width": w, "height": 900})
            errs = []
            pg.on("pageerror", lambda e: errs.append(str(e)))
            pg.goto("file://" + page_file)
            n = pg.locator(".part").count()
            for i in range(n):
                pg.screenshot(path=os.path.join(out, f"{name}-part{i + 1}.png"), full_page=True)
                if i < n - 1:
                    pg.click("#next")
            print(name, "parts:", n, "comment buttons:", pg.locator(".cbtn").count(),
                  "page width:", pg.evaluate("document.documentElement.scrollWidth"), "errors:", errs)
    else:
        pg = b.new_page(viewport={"width": 800, "height": 600})
        for f in args:
            pg.goto("file://" + os.path.abspath(f))
            pg.query_selector("svg").screenshot(path=os.path.join(out, os.path.basename(f) + ".png"))
        print("rendered", len(args))
    b.close()
