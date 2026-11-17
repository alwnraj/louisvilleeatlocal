# Louisville Food Money Matrix

A map of about 1,600 Louisville-area restaurants, coffee shops and bars, showing who owns each one: private equity, a big corporation, or a local independent. Open a PE-backed or corporate spot and it suggests three independents nearby.

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
- `data/liba-members.txt`: the Louisville Independent Business Alliance's Food & Drink members, read from keeplouisvilleweird.com/directory in November 2026. Places that match a member are marked "Confirmed local". LIBA only admits businesses that are majority-owned by Louisville-area residents, headquartered locally, privately held and not franchises.
- `data/osm-raw.json`: the OpenStreetMap export (Overpass, November 2026, bounding box 37.99,-85.96 to 38.39,-85.40).
- `scripts/build.py`: matches OSM places to brands by name, drops stadium stalls and junk rows, merges duplicates, assigns neighborhoods, checks the data, writes `places.<hash>.js` and points `index.html` at it.

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

Map data © OpenStreetMap contributors (ODbL).
