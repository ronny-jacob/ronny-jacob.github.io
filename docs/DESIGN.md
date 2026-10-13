# Design system

## Principles
Match each kind of information to the form that shows it fastest. Proof over claims. Three layers: glance (first screen), scan (case-study summary plus one picture), read (short sections). One memorable element per page; everything else stays quiet.

## Tokens (`assets/css/style.css`, `:root`)
- Colour: `--paper #f5f5f1`, `--surface #fff`, `--ink #14181b`, `--muted #586168`, `--line #d8d9d3`, accent `--teal #16505f`, `--amber #8f4a0c` (removed items and "Observed" tags). A dark theme is defined through `prefers-color-scheme`.
- Type: headings and UI in Schibsted Grotesk, body in Newsreader (Google Fonts, with Georgia and system fallbacks). Body 18px / 1.65, line length about 40rem.
- Radius: one value, `--r: 14px` (screenshots and the live phone frame are the only exceptions). Spacing steps `--s1` to `--s5`.

## Components
- **Hero:** outcome headline, one line about him, one primary button.
- **Cards (`.pcard`):** the big TradeIndia card plus three small cards with live previews (`.live`).
- **Brief (`.brief`):** four-row summary at the top of each case study.
- **Charts (`.bars`):** HTML bars, zero baseline, direct labels, the "after" series in the accent colour, dashed outline for non-deployed references.
- **Diagrams:** `.lanes` (who did what), `.decision`, `.steps` (pipeline), `.zones` (Invisalign minutes scale), `.merge` (NMIMS before/after), `.path` (career timeline).
- **Tags:** `.tag-m` Measured, `.tag-o` Observed.
- **Live previews (`.live`):** an iframe of the real app. On first load a "Try it live" button gates interaction so the iframe never traps touch scrolling. The screenshots in `assets/img/` are only a placeholder behind the iframe.

## Accessibility floor
Skip link, visible focus ring, reduced-motion support, alt text (empty alt only for decorative images), text contrast 4.5:1, graphic contrast 3:1, tap targets 44px for primary controls, no information carried by colour alone.

## Charts and data honesty
Never plot data that is not in `CLAIMS.md`. Do not chart per-model accuracy for the other four models (the source report gives conflicting ranges).

## Motion
Scroll reveal (fade up), bars growing from a zero baseline and count-ups that end on the real figure. Easing `--ease: cubic-bezier(.32,.72,0,1)`. Hero has one static soft gradient, no animated background. Everything is off under `prefers-reduced-motion`.
