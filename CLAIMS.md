# Claims ledger

Every number or factual claim on the site, with its source and status. "Confirm" means I could not fully verify it from the files, so please check it before publishing.

| # | Claim on the site | Source | Status |
| --- | --- | --- | --- |
| 1 | Accuracy 43% to 86% on a 10,000-product test set (existing SpaCy approach to the new Gemma 2 prompt) | Your message. The final report PDF says 100 products in most places and mentions 10,000 in two | **Confirm** the 43% is the SpaCy approach and how "correct" was judged on 10,000 items |
| 2 | Gemma 2 76% to 88% (original prompt to new prompt plus validation pipeline) | Your message | **Confirm** that 86% is the prompt alone and 88% adds the pipeline |
| 3 | Gemini 2.5 Flash Lite 97% in separate API experiments, not deployed | Report; your original brief | Verified in report |
| 4 | 14 prompt variants tested on Gemma 2 | Your brief; report | Verified (report text also says 15 once) |
| 5 | Six models compared (GPT-4o, Claude 3.5 Sonnet, Mistral Large, DeepSeek V3, Gemini 2.5 Flash Lite, Gemma 2) | Report | Verified. Per-model accuracy is not shown because the report gives conflicting ranges |
| 6 | Test cycle 1–2 hours to 5–10 minutes; 20–50 keywords to 500–1,000+ per variant | Report; your brief | Verified in report |
| 7 | Solution deployed to production during the internship | Report; your brief | Verified. Engineering deployed it |
| 8 | Input prices per million tokens; Gemini about $0.10 and $15–30 a month estimate | Report (published pricing, mid-2026; your estimate) | Verified in report |
| 9 | "Tens of thousands of inquiries a day" | Report (15,000–30,000 in different places) | Approximate on purpose |
| 10 | SpaCy approach and first Gemma 2 prompt built by the tech team; engineering deployed | Report; your message | Verified |
| 11 | Pipeline: skip model for 1–2 word inputs; retry up to 5 times on one-word output; fall back to original | Report | Verified in report |
| 12 | 56 different students in the first 99 sign-in entries, 13–14 July 2026 | Analytics sheet (first 100 rows visible to me) | **Confirm** the full log size; the true total is probably higher |
| 13 | Class Companion features | Ran your uploaded file | Verified |
| 14 | Data arrives as Excel sheets by email and WhatsApp placement messages | Your message | Verified by you |
| 15 | Invisalign Tracker: 75 of 75 tests pass | I ran `rules-tests.js` | Verified |
| 16 | Invisalign features, local-only storage, not-medical-advice notice | Your uploaded code and onboarding screen | Verified |
| 17 | Rule change in v1.6.0 (single 41–60 minute removal) | `RULESHEET.md` | Verified. `CHANGELOG.md` was not uploaded |
| 18 | Lean 12 features, local storage, RepDB credit; live at ronny-jacob.github.io/lean12 | Your uploaded file; the live page loads (I could only see its title, not its content) | **Confirm** the live copy's default targets (see below) |
| 19 | NMIMS MBA 2025–27; BBA LL.B., University of Kerala; advocate at Trivandrum District Court 2023–25 | Your CV | Verified from CV |
| 20 | Email address ronnyjacobmba@gmail.com | Your CV | **Confirm** you want it public |

## Deliberately left out
- From your CV but not in the report: automated seller matching up 2x, seller discovery up 5x, "~80% of buyer inquiries", 10+ LLMs, 50+ prompt iterations, planned A/B tests, written PRDs. Add them only if you can source them.
- The report's daily-impact estimate (6,500 or 1,500 fewer wrong mappings a day). It is an extrapolation.
- Prompts, internal scoring logic, internal statistics, colleague names and your student ID.
- Lean 12 weight, waist and calorie targets (they are in the app's Guide and Progress tabs).

## Lean 12 live copy
The uploaded file has these defaults built in: start weight 75 kg, height 168 cm, goal 68 kg, 2,000 kcal, 140 g protein, 9,000 steps. If the live page is the same file, every visitor sees them in the Progress, Guide and Data tabs. Replace them with neutral defaults if you do not want them public.
