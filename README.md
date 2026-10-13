# Ronny Jacob: product portfolio

A static site: plain HTML, CSS and a few lines of JavaScript. No framework, no build step needed to run it.

## Run it locally
```bash
cd ronny-portfolio
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy (CI/CD)
1. Create a **public** GitHub repository named exactly `ronny-jacob.github.io` and push this folder (`git init`, `git add .`, `git commit`, `git branch -M main`, `git remote add origin ...`, `git push -u origin main`).
2. In the repository open Settings → Pages and set Source to **GitHub Actions**.
3. Every push to `main` runs `.github/workflows/deploy.yml`: build, check, deploy. Pull requests run build and check only. The site is live at https://ronny-jacob.github.io/ about a minute later.

Your apps keep working: they live in their own repositories at `/invisalign-tracker/`, `/nmims-class-schedule/` and `/lean12/`.

## Editing
- Edit the fragments in `pages/`, then run `python3 tools/build.py && python3 tools/check.py`. The generated HTML is git-ignored and rebuilt by CI. Never edit it by hand.
- Numbers shown on the site are listed in `CLAIMS.md` with their source. Update that file when you change a number.

## Files
| Path | Purpose |
| --- | --- |
| `index.html` | Home: hero, selected work, skills, about, contact |
| `case-studies/*.html` | The four case studies |
| `assets/css/style.css` | All styles, with light and dark themes |
| `assets/js/main.js` | The hero animation (respects reduced-motion settings) |
| `assets/img/` | Portrait and screenshots (Invisalign screenshots use sample data) |
| `pages/`, `tools/build.py`, `tools/check.py` | Page fragments, the build script and the quality gate |
| `AGENTS.md`, `docs/` | Instructions, brief, design system and backlog for coding agents |
| `.github/workflows/deploy.yml` | Build, check and deploy to GitHub Pages |
| `CLAIMS.md` | Every claim on the site and where it comes from |

## Notes
- The three app previews are live iframes of your GitHub Pages apps (`/nmims-class-schedule/`, `/invisalign-tracker/`, `/lean12/`). They only load once the portfolio is online (or when you are online locally). The screenshots in `assets/img/` show only while an app loads. If a preview ever stays blank, the "Open full app" link still works.
- On phones a "Try it live" tap enables each preview, so it does not trap page scrolling.
- Fonts (Newsreader and Schibsted Grotesk) load from Google Fonts. If they fail, the site falls back to Georgia and system sans-serif.
- Before sharing the link, replace `ronnyjacobmba@gmail.com` if you prefer a different public address (search for it in `pages/` and `tools/build.py`, then rebuild).
