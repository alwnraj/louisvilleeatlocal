You're picking up work on **Louisville Eat Local**, a static map of ~1,613 Louisville-area restaurants, cafés and bars that shows who owns each one: PE-backed, corporate, or independent. Live at https://louisvilleeatlocal.vercel.app. Repo: https://github.com/alwnraj/louisvilleeatlocal, branch `main`. Every push to `main` auto-deploys on Vercel.

## Where things are
- **Project folder:** `/Users/AlwinRajkumar/Desktop/resume/louisvillebuylocal/louisville-food-money-matrix/`. It's its own git repo, nested inside an unrelated pasta-site repo. Don't touch the parent repo, apart from its `.claude/launch.json`, which has a `louisville-matrix` preview config that serves this folder with Vite.
- **`index.html`:** the whole app. It uses MapLibre 4.7.1 (vendored in `vendor/`) with OpenFreeMap tiles. On phones it's a full-screen map with a draggable bottom sheet.
- **`scripts/build.py`:** run `python3 -I scripts/build.py`. It matches OpenStreetMap places (`data/osm-raw.json`) to the ownership research (`data/brands.json`) and to Louisville Independent Business Alliance members (`data/liba-members.txt`). It writes the hashed `places.<hash>.js` and updates `index.html` to point at it. Each place has a stable `osm` id.
- **`README.md`:** explains the data model and how places are classified.
- **`data/`:** not deployed (see `.vercelignore`).

## Current task: remove places that are closed or don't exist
The user doesn't want the map to list places that have closed: it reads like made-up data. Verification work is in `data/verification/`:
- **What's there:** `worklist.json`, `batches/`, `results/`, and the rules in `INSTRUCTIONS.md` (first pass) and `RECHECK.md` (second pass).
- **Status:** about 1,000 places were checked before work stopped (633 open, 55 closed, 314 unsure).
- **Codex:** the user is giving the rest to Codex using `CODEX_PROMPT.md`. Codex should produce `data/verification.json`, keyed by place `id`, and `data/verification/REPORT.md`.

Your job:
1. **Check Codex's output.** Confirm every batch has results. Then spot-check the evidence, especially every "closed", "renamed" and "not a restaurant" verdict and a sample of "open" ones. Look for invented URLs, same-name places in other cities, and moved businesses. Tell the user what you found before changing anything on the site.
2. **Wire it into the build.**
   - Make `scripts/build.py` read `data/verification.json` and drop places marked `closed`, `renamed` or `duplicate_or_not_a_restaurant`.
   - Decide with the user what to do with "unsure" places: hide them, or show them flagged.
   - Print the counts of what was dropped.
   - Mention in the page's "How this was made" dialog that places were checked as open on a given date.
3. **Rebuild and test.**
   - Check desktop in the browser preview (`preview_start` with `louisville-matrix`).
   - Check phones in Safari on the iOS Simulator (iPhone 17) at the dev server URL.
   - Confirm the console is clean.
4. **Commit and push to `main`, then confirm the live site updated.**

## Conventions
- **Commits:** the user asked that commits list only them as author. Don't add Claude co-author or attribution lines.
- **Sources:** every ownership claim on a card needs a source URL that was actually seen. If an owner is uncertain, mark it "not confirmed" (`u: true` in `brands.json`) and never count it as PE-backed.
- **Tokens:** the user is watching token use. Avoid large fan-outs of subagents; do the review yourself, efficiently.
