#!/usr/bin/env python3
"""Quality gate. Run after tools/build.py. Exit code 1 on any failure. Standard library only.
Checks: one <h1>, <title>, meta description, image alt attributes, no unrendered {{placeholders}},
internal links/images/anchors resolve, forbidden (confidential or personal) terms absent."""
import pathlib, re, sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ["index.html", "404.html", "case-studies/tradeindia.html", "case-studies/nmims-class-companion.html",
         "case-studies/invisalign-tracker.html", "case-studies/lean-12.html", "case-studies/splitbill.html"]
# Terms that must never appear on the public site (confidential, personal or unsupported). Case-insensitive.
FORBIDDEN = ["SAP ID", "80012500885", "Smarth", "Mohan", "Sajjad", "Akash", "Divyansh", "Afzal", "Ajay K",
             "Painless", "DialB2B", "Infocom", "Shadman", "P07", "P08", "Annexure",
             "75 kg", "68 kg", "168 cm", "2,000 kcal", "140 g protein"]

class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.h1 = 0; self.title = ""; self.in_title = False; self.desc = False
        self.imgs = []; self.refs = []; self.ids = set()
    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "h1": self.h1 += 1
        if tag == "title": self.in_title = True
        if tag == "meta" and a.get("name") == "description" and a.get("content"): self.desc = True
        if tag == "img": self.imgs.append(a)
        if "id" in a: self.ids.add(a["id"])
        for k in ("href", "src"):
            if k in a and tag != "meta": self.refs.append(a[k])
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
    def handle_data(self, d):
        if self.in_title: self.title += d

def main():
    errors, parsed = [], {}
    for rel in PAGES:
        f = ROOT / rel
        if not f.exists(): errors.append(f"{rel}: missing (run python3 tools/build.py first)"); continue
        src = f.read_text(encoding="utf-8"); p = P(); p.feed(src); parsed[rel] = p
        if p.h1 != 1: errors.append(f"{rel}: expected 1 <h1>, found {p.h1}")
        if not p.title.strip(): errors.append(f"{rel}: empty <title>")
        if not p.desc: errors.append(f"{rel}: missing meta description")
        for i in p.imgs:
            if "alt" not in i: errors.append(f"{rel}: <img src={i.get('src')}> has no alt attribute")
        if "{{" in src or "}}" in src: errors.append(f"{rel}: unrendered template placeholder")
        for t in FORBIDDEN:
            if re.search(re.escape(t), re.sub(r"<[^>]+>", " ", src), re.I): errors.append(f"{rel}: forbidden term '{t}'")
    for rel, p in parsed.items():
        base = (ROOT / rel).parent
        for ref in p.refs:
            if re.match(r"(https?:|mailto:|tel:|//|data:)", ref) or ref.startswith("{{"): continue
            path, _, frag = ref.partition("#")
            target = (base / path) if path else (ROOT / rel)
            if path.startswith("/"): target = ROOT / path.lstrip("/")
            if path and not target.exists(): errors.append(f"{rel}: broken reference {ref}"); continue
            if frag and target.suffix == ".html":
                tr = str(target.resolve().relative_to(ROOT.resolve()))
                ids = parsed.get(tr).ids if tr in parsed else set()
                if frag not in ids: errors.append(f"{rel}: anchor #{frag} not found in {tr}")
    for fragfile in (ROOT / "pages").glob("*.html"):
        s = fragfile.read_text(encoding="utf-8")
        for t in FORBIDDEN:
            if re.search(re.escape(t), re.sub(r"<[^>]+>", " ", s), re.I): errors.append(f"pages/{fragfile.name}: forbidden term '{t}'")
    if errors:
        print("CHECK FAILED"); [print(" -", e) for e in errors]; sys.exit(1)
    print(f"CHECK OK ({len(PAGES)} pages)")

if __name__ == "__main__":
    main()
