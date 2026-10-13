#!/usr/bin/env python3
"""Wraps the HTML fragments in pages/ with the shared header/footer and writes the site.
Usage: python3 tools/build.py   (run from the site root). Output goes next to pages/."""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://ronny-jacob.github.io/"
PAGES = {  # fragment -> output path
    "home.html": "index.html",
    "tradeindia.html": "case-studies/tradeindia.html",
    "nmims-class-companion.html": "case-studies/nmims-class-companion.html",
    "invisalign-tracker.html": "case-studies/invisalign-tracker.html",
    "lean-12.html": "case-studies/lean-12.html",
    "404.html": "404.html",
}
NAV = [("Work", "#work", "work"), ("Skills", "#skills", "skills"), ("About", "#about", "about"), ("Contact", "#contact", "contact")]

def meta(src, key):
    m = re.search(r"<!--\s*%s:\s*(.*?)\s*-->" % key, src, re.S)
    return m.group(1) if m else ""

def build():
    for frag, out in PAGES.items():
        src = (ROOT / "pages" / frag).read_text(encoding="utf-8")
        title, desc, image = meta(src, "title"), meta(src, "desc"), meta(src, "image")
        depth = out.count("/")
        root = "../" * depth if out != "404.html" else "/"
        body = re.sub(r"<!--\s*(title|desc|image):.*?-->\s*", "", src, flags=re.S)
        body = re.sub(r"\{\{include:(\w+)\}\}", lambda m: (ROOT / "pages" / ("_%s.html" % m.group(1))).read_text(encoding="utf-8"), body)
        body = body.replace("{{root}}", root)
        nav = '<a href="%scase-studies/tradeindia.html">Case study</a><a class="btn btn-primary btn-sm" href="mailto:ronnyjacobmba@gmail.com">Email me</a>' % root
        canon = BASE + ("" if out == "index.html" else out)
        og_img = BASE + (image or "assets/img/ronny-portrait.jpg")
        noindex = '<meta name="robots" content="noindex">' if out == "404.html" else ""
        page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
{noindex}
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#16505f">
<link rel="icon" type="image/svg+xml" href="{root}assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Schibsted+Grotesk:wght@500;600;700&display=swap">
<link rel="stylesheet" href="{root}assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{root}index.html">Ronny Jacob</a>
<nav class="hnav" aria-label="Primary">{nav}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<span>Ronny Jacob</span>
</div></footer>
<script src="{root}assets/js/main.js" defer></script>
</body>
</html>
"""
        dest = ROOT / out
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(page, encoding="utf-8")
        print("wrote", out)

if __name__ == "__main__":
    build()
