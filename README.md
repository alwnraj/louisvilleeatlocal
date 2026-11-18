# Louisville Eat Local

A map of 1,268 Louisville-area restaurants, coffee shops and bars, showing who owns each one: private equity, a big corporation, or a local independent. Open a PE-backed or corporate spot and it suggests three independents nearby. Operating status was reviewed on 17–18 November 2026; places whose status could not be confirmed (219) are removed.

The idea comes from the London Food Money Matrix (london-food-money-matrix.vercel.app). This version's code, artwork and data are new.

## Run it

It's a static site with no build step. Serve the folder with any static server, for example:

```bash
python3 -m http.server 8000
```

It's deployed on Vercel as a static site: every push to `main` redeploys it.

## Files

- `index.html`: the page (MapLibre GL 4.7.1 with OpenFreeMap tiles, restyled). The list renders first; the map library loads right after the first paint.
- `places.<hash>.js`: generated data, named by content hash so it can be cached forever. Don't edit it by hand.
- `vendor/maplibre-gl-4.7.1/`: MapLibre GL JS and CSS (BSD-3-Clause, see LICENSE.txt), served from the site's own domain.
- `vercel.json` / `.vercelignore`: long-lived caching for hashed and vendored files; `data/`, `scripts/` and this README aren't deployed.
- `data/brands.json`: the research, with one record per chain or restaurant group: owner, year, note and source URL. `u: true` marks an owner we couldn't confirm.
- `data/verification.json`: reviewed operating status keyed by stable OSM ID (`n…` / `w…`), with confidence, evidence, checked date and second-pass agreement. The build keeps only `open` places, plus `renamed` ones that have a `new_name` (shown under the new name). It removes `closed`, `duplicate_or_not_a_restaurant`, `unsure` and any new, unreviewed ID.
- `data/verification/REPORT.md`: coverage, corrections, every proposed removal, remaining unsure places, disagreements and source limitations. Original batch results and second-pass evidence are preserved in `data/verification/results/`.
- `data/liba-members.txt`: the Louisville Independent Business Alliance's Food & Drink members, read from keeplouisvilleweird.com/directory in November 2026. Places that match a member are marked "Confirmed local". LIBA only admits businesses that are majority-owned by Louisville-area residents, headquartered locally, privately held and not franchises.
- `data/osm-raw.json`: the OpenStreetMap export with edit metadata (Overpass, data as of 2026-11-17 14:49 UTC, bounding box 37.99,-85.96 to 38.39,-85.40). Each card shows the year its entry was last edited.
- `scripts/build.py`: matches OSM places to brands by name, drops stadium stalls and junk rows, merges duplicates, applies reviewed operating status, assigns neighborhoods, checks the data, writes `places.<hash>.js` and points `index.html` at it. Verification filtering runs after deduplication so a second OSM entry cannot resurrect a removed place. The build prints removal counts by status.

```bash
python3 -I scripts/build.py
```

## How places are classified

- **PE-backed**: a private equity, growth or investment firm owns the brand or a significant stake in it. This includes lender or bondholder groups that took a chain over.
- **Corporate**: owned by a public company, or by a large private company or family based outside the area.
- **Independent**: founder, family or locally owned, with no outside parent found. Unbranded single-location places default to independent and haven't each been researched.
- Franchised locations follow the brand's owner.
- A brand whose owner is unconfirmed is never counted as PE-backed.

To fix or add an owner, edit `data/brands.json`. `m` holds the name prefixes to match, written lowercase with no punctuation. Then rerun the build.

Use a leading `=` for exact name matches where a prefix would confuse unrelated businesses. Haymarket café and Haymarket Whiskey Bar are separate businesses, as are Louisville's Moby Dick Seafood and Moby Dick House of Kabob. The café and seafood chain have unconfirmed ownership records rather than inheriting the unrelated business's owner.

## Operating-status review

All 25 batches cover the original 1,613 places. Every first-pass closed, renamed, nonrestaurant or unsure verdict received a second pass, and 23 original open entries were sampled. The reviewed build removes 122 closed entries, 14 stale renamed entries and 6 duplicates/nonrestaurants. Renamed places are kept under their `new_name`. Texas Roadhouse on Outer Loop was restored to open after recheck (its move is announced but not complete).

“Open” means supporting web evidence was found on the checked date. It is not a real-time hours guarantee. Locator URL changes, “closed now,” temporary closures, future closure announcements and same-name businesses elsewhere are not sufficient evidence of permanent closure. Moved businesses are checked at their mapped location; moves beyond roughly 150 m count as closed at the old point. Cards link operating-status evidence separately from ownership sources.

Map data © OpenStreetMap contributors (ODbL).
