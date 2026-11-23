# Louisville Eat Local

A map of 1,436 Louisville-area restaurants, coffee shops and bars, showing who owns each one: private equity, a big corporation, or a local independent. Open a PE-backed or corporate spot and it suggests three independents nearby. Operating status was reviewed on 17–19 November 2026; 46 places whose operating status remains uncertain stay visible and flagged.

The idea comes from the London Food Money Matrix (london-food-money-matrix.vercel.app). This version's code, artwork and data are new.

## Run it

It's a static site with no build step. Serve the folder with any static server, for example:

```bash
python3 -m http.server 8000
```

It's deployed on Vercel as a static site: every push to `main` redeploys it.

## Files

- `index.html`: the page (MapLibre GL 4.7.1 with OpenFreeMap tiles). The list renders first; the map library loads right after the first paint. The map style is baked into a `<script type="application/json" id="style">` block by `scripts/make_style.py`.
- `places.<hash>.js`: generated data the first view needs: place names, coordinates, areas, owners, as an index-coded columnar table (`window.D`). Named by content hash so it can be cached forever. Don't edit it by hand.
- `detail.<hash>.json`: generated data only a place card needs (operating-status links, ownership notes and sources). The page fetches it once the map is up. Same hashing rule.
- `fonts/`: Fraunces and Public Sans, latin only, as variable woff2 (Fraunces trimmed to weights 600-800 and optical sizes 14-48, the ones the page uses).
- `vendor/maplibre-gl-4.7.1/`: MapLibre GL JS and CSS (BSD-3-Clause, see LICENSE.txt), served from the site's own domain.
- `vercel.json` / `.vercelignore`: long-lived caching for hashed and vendored files; `data/`, `scripts/` and this README aren't deployed.
- `data/brands.json`: the research, with one record per chain or restaurant group: owner, year, note and source URL. `u: true` marks an owner we couldn't confirm.
- `data/verification.json`: reviewed operating status keyed by stable OSM ID (`n…` / `w…`), with confidence, evidence, checked date and second-pass agreement. Optional reviewed `address`, `area` and `kind` fields correct stale OSM labels while preserving coordinates. The build keeps `open` and visibly flagged `unsure` places, plus `renamed` ones that have a confirmed `new_name` (shown under the new name). It removes `closed`, `duplicate_or_not_a_restaurant` and any new, unreviewed ID.
- `data/verification/REPORT.md`: coverage, corrections, every proposed removal, remaining unsure places, disagreements and source limitations. Original batch results and second-pass evidence are preserved in `data/verification/results/`.
- `data/liba-members.txt`: the Louisville Independent Business Alliance's Food & Drink members, read from keeplouisvilleweird.com/directory in November 2026. Places that match a member are marked "Confirmed local". LIBA only admits businesses that are majority-owned by Louisville-area residents, headquartered locally, privately held and not franchises.
- `data/osm-raw.json`: the OpenStreetMap export with edit metadata (Overpass, data as of 2026-11-17 14:49 UTC, bounding box 37.99,-85.96 to 38.39,-85.40). Each card shows the year its entry was last edited.
- `scripts/build.py`: matches OSM places to brands by name, drops stadium stalls and junk rows, merges duplicates, applies reviewed operating status, assigns neighborhoods, checks the data, writes `places.<hash>.js` and points `index.html` at it. Verification filtering runs after deduplication so a second OSM entry cannot resurrect a removed place. The build prints removal counts by status and the number of unsure places kept and flagged.

```bash
python3 -I scripts/build.py
```

- `scripts/make_style.py`: fetches OpenFreeMap's positron style, applies this site's colours, drops layers that can't be seen at the map's zoom range (and the sprite sheet) and writes the result into `index.html`. Only needed to change the palette or pick up an upstream style change: `python3 -I scripts/make_style.py`.


## How places are classified

- **PE-backed**: a private equity, growth or investment firm owns the brand or a significant stake in it. This includes lender or bondholder groups that took a chain over.
- **Corporate**: owned by a public company, or by a large private company or family based outside the area.
- **Independent**: founder, family or locally owned, with no outside parent found. Unbranded single-location places default to independent and haven't each been researched.
- Franchised locations follow the brand's owner.
- A brand whose owner is unconfirmed is never counted as PE-backed.

To fix or add an owner, edit `data/brands.json`. `m` holds the name prefixes to match, written lowercase with no punctuation. Then rerun the build.

Use a leading `=` for exact name matches where a prefix would confuse unrelated businesses. Haymarket café and Haymarket Whiskey Bar are separate businesses, as are Louisville's Moby Dick Seafood and Moby Dick House of Kabob. The café and seafood chain have unconfirmed ownership records rather than inheriting the unrelated business's owner.

## Operating-status review

All 25 batches cover the original 1,613 places. Every first-pass closed, renamed, nonrestaurant or unsure verdict received a second pass, and 23 original open entries were sampled. The latest review rechecked the remaining 53 unsure records and resolved 7: 3 current successors and 4 closed at the mapped location. The remaining 46 stay visible with an “Operating status not confirmed” flag. The build retains confirmed successors, removes closed and duplicate/nonrestaurant records, and preserves the earlier successor merges. Result: 1,436 places. Evidence, confidence levels and limitations are in [`ROUND6_REPORT.md`](data/verification/ROUND6_REPORT.md); the 53-record review is `data/verification/results/round6_reviewed.json`. Earlier findings remain in [`ROUND5_REPORT.md`](data/verification/ROUND5_REPORT.md) and the reports linked there.

“Open” means supporting web evidence was found on the checked date. It is not a real-time hours guarantee. Locator URL changes, “closed now,” temporary closures, future closure announcements and same-name businesses elsewhere are not sufficient evidence of permanent closure. Moved businesses are checked at their mapped location; moves beyond roughly 150 m count as closed at the old point. Cards link operating-status evidence separately from ownership sources.

Map data © OpenStreetMap contributors (ODbL).
