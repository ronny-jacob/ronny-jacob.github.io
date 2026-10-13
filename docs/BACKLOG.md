# Backlog

## Blocked on the owner (do not guess; ask)
1. Confirm the 43% → 86% claim: that 43% is the SpaCy approach, that it was measured on 10,000 products, and how "correct" was judged. (The source report says 100 products in most places.)
2. Confirm the chain 76% → 88% for Gemma 2 and that 86% is the prompt alone while 88% adds the validation pipeline.
3. ~~Full NMIMS sign-in count~~ Resolved 13 Oct 2026: 147 students, see CLAIMS.md #12.
4. Whether the email ronnyjacobmba@gmail.com is public.
5. Lean 12 live copy: it may expose default body targets (75 kg, 168 cm, 68 kg, 2,000 kcal, 140 g, 9,000 steps). Offer a neutral-defaults copy for the `lean12` repository.
6. CV claims not in the report and therefore not on the site: 2x seller matching, 5x seller discovery, "~80% of buyer inquiries", 10+ LLMs, 50+ prompt iterations, planned A/B tests, PRDs. Add only if sourced.
7. Availability line (graduation date, role types, location) and a résumé PDF button. Not provided.
8. A one-sentence recommendation from his TradeIndia manager, with permission.

## Ready to do
1. **Verify the live site after the first deploy.** Check the three iframes load (the sandbox used to build this had no network), the "Try it live" gating works on a phone, and the Google Fonts render.
2. **Dark-mode visual QA** of all five pages (contrast was computed but not viewed).
3. **Accessibility audit** with Lighthouse and one screen reader pass. Target Lighthouse accessibility 95 or higher.
4. **Optional:** a jump list on the TradeIndia page. Only if it does not add clutter.
5. **Optional:** a Playwright smoke test in CI (loads each page at 390px and 1280px, fails on horizontal overflow or console errors).
6. **Optional:** open-graph image for the home page (a 1200×630 card with the headline and before/after bars).

## Done
Minimal one-path home page, five-page structure, diagrams, live embeds, accessibility pass, CI/CD, quality gate.
