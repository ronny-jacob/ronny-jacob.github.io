# AGENTS.md: instructions for coding agents (opencode and others)

Read this first, then `docs/BRIEF.md`, `docs/DESIGN.md`, `docs/BACKLOG.md` and `CLAIMS.md`.

## What this is
The public portfolio of **Ronny Jacob** (MBA candidate, NMIMS Hyderabad), aimed at recruiters hiring for Associate Product Manager and AI Product Manager roles. A recruiter gives it about 60 seconds. It is a static site on GitHub Pages at https://ronny-jacob.github.io/. Plain HTML, CSS and a little JavaScript. No framework, no runtime dependencies.

## Commands
```bash
python3 tools/build.py          # fragments in pages/  ->  index.html, 404.html, case-studies/*.html
python3 tools/check.py          # quality gate; must print "CHECK OK" before every commit
python3 -m http.server 8000     # preview at http://localhost:8000
```
CI (`.github/workflows/deploy.yml`) runs build then check on every push and pull request, and deploys `main` to GitHub Pages. The generated HTML is git-ignored; never edit it by hand.

## Layout
- `pages/*.html`: the source. Each starts with `<!--title: ...-->`, `<!--desc: ...-->` and optionally `<!--image: ...-->`. `{{root}}` becomes the relative path to the site root. `{{include:name}}` inlines `pages/_name.html`.
- `tools/build.py`: wraps fragments in the shared header and footer. `tools/check.py`: the quality gate.
- `assets/css/style.css`: all styles (tokens at the top). `assets/js/main.js`: the hero demo and the "Try it live" gating. `assets/img/`: portrait and placeholder images.
- `CLAIMS.md`: every number or factual claim on the site with its source and status.

## Rules you must not break
1. **No invented facts.** Every number, outcome, date or role on the site must be in `CLAIMS.md` with a source. If it is not there and the owner has not confirmed it, do not add it. Never invent usage, revenue, conversions, testimonials, user research, ownership or production metrics.
2. **Keep measured and observed separate.** Offline test results are never described as production results. Keep the `Measured` / `Observed` tags and the "what I did not measure" statements.
3. **Gemini 2.5 Flash Lite (97%) was not deployed.** Never imply it was. The deployed model was Gemma 2.
4. **Confidentiality.** Never publish prompts, internal scoring logic or statistics, colleague names, the student ID, or Lean 12 body targets. `tools/check.py` blocks a list of forbidden terms; extend it, never weaken it.
5. **Medical.** Invisalign Tracker is a tracking tool, not medical advice. Make no treatment-efficacy claims.
6. **Honesty about the owner.** He is an MBA candidate with internship experience and self-built products, not a senior leader.
7. **Do not add** testimonials, a skills word cloud, decorative charts without real data, animated backgrounds, or new pages without approval.

## Design rules (details in `docs/DESIGN.md`)
One accent colour, one corner radius, one type scale. Charts start at zero and use direct labels. Keep every group to three items or fewer. Contrast at least 4.5:1 for text and 3:1 for graphics; tap targets at least 44px for primary controls. Respect `prefers-reduced-motion`. No horizontal scroll at 390px.

## Definition of done
- `python3 tools/build.py && python3 tools/check.py` passes.
- Checked at 390px and 1280px: no overflow, no broken images, text readable.
- Any new or changed claim is reflected in `CLAIMS.md`.
- Commit message says what changed and why. Small commits.

## Git workflow
Branch from `main`, open a pull request, let CI pass, then merge. The first deploy needs Settings → Pages → Source set to "GitHub Actions".

## When unsure
Stop and ask the owner. Items needing his input are listed under "Blocked on the owner" in `docs/BACKLOG.md`.
