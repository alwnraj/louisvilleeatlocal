# Performance work

Branch `perf`, measured against `main` (`d4f8f19`). Look, data and behaviour are unchanged; the page loads less, starts the map sooner and does less work at startup. Pan/zoom frame time did not change, and the reason is below.

## How it was measured

`scripts/perf/` (needs `npm i playwright`; any Chromium works):

```bash
node scripts/perf/server.js . 8080                     # Vercel-like: brotli/gzip, ETag, headers from vercel.json
node scripts/perf/measure.js http://localhost:8080/ label desktop 7   # or: mobile 5
node scripts/perf/verify.js  http://localhost:8080/ [mobile]          # functional check
```

- **desktop**: 1280x800, no throttling. **mobile**: 390x844 @3x touch, 4x CPU throttle, 1.6 Mbps / 150 ms. Medians of 7 and 5 cold-cache runs.
- Chromium's software GL (SwiftShader) renders the map, which is the same situation as the iPhone simulator.
- Bytes are encoded (over-the-wire) bytes from Playwright's request log, workers included, so map tiles and glyphs are counted. "Initial load" is everything finished when the map first goes idle; the rest of the run (pan/zoom test) fetches more tiles.
- Frame times are `requestAnimationFrame` deltas over 60 frames of a scripted `panBy` / zoom at the overview (zoom 10.9) and downtown (zoom 13 to 14). Vsync quantises them to 16.7 ms steps.
- Network to OpenFreeMap goes through this sandbox's proxy, so absolute map-idle times are noisy (about +/-15% between runs). Compare the two columns, not the absolute numbers.

## Results (main -> perf)

| Metric | Desktop main | Desktop perf | Mobile main | Mobile perf |
|---|---|---|---|---|
| First / largest contentful paint | 60 ms | 64 ms | 296 ms | 300 ms |
| DOMContentLoaded | 112 ms | 95 ms (-15%) | 1454 ms | 1082 ms (-26%) |
| Load event | 235 ms | 175 ms (-26%) | 2492 ms | 2088 ms (-16%) |
| Pins on the map (map interactive) | 348 ms | 175 ms (-50%) | 2488 ms | 2084 ms (-16%) |
| Map idle (first tiles drawn) | 1224 ms | 1033 ms (-16%) | 5429 ms | 4131 ms (-24%) |
| Bytes, initial load | 676 KB | 552 KB (-18%) | 805 KB | 602 KB (-25%) |
| Bytes, whole test run | 1465 KB | 1370 KB (-7%) | 1211 KB | 1037 KB (-14%) |
| Requests, initial load | 18 | 16 | 21 | 19 |
| Layout time | 89 ms | 31 ms (-65%) | 275 ms | 152 ms (-45%) |
| Total blocking time | 198 ms | 220 ms | 1124 ms | 1113 ms |
| Script time | 84 ms | 78 ms | 358 ms | 304 ms (-15%) |
| JS heap | 15 MB | 13 MB | 16 MB | 12 MB |
| Data file parse + unpack (4x CPU) | 18.0 ms | 3.6 ms (-80%) | | |
| Frame time pan, overview (p50/p95/max) | 33/50/67 | 33/50/67 | 83/100/100 | 83/100/117 |
| Frame time zoom, overview | 50/67/83 | 50/67/100 | 83/100/117 | 83/117/117 |
| Frame time pan, zoom 13.5 | 50/67/83 | 50/67/67 | 100/117/133 | 100/117/133 |
| Frame time zoom 13-14 | 50/83/83 | 50/83/83 | 100/117/133 | 100/117/133 |

FCP and total blocking time are flat (within run-to-run spread). TBT is dominated by evaluating `maplibre-gl.js`, which is needed either way.

### Per-resource bytes (desktop, encoded)

| Resource | main | perf |
|---|---|---|
| index.html | 15.4 KB | 16.4 KB (now carries the 16 KB map style) |
| places data | 66.5 KB | 26.7 KB |
| detail data (new, fetched after the map is idle) | - | 28.7 KB |
| Fonts (Google CSS + 2 woff2) | 97.1 KB, 3 requests, 2 extra origins | 70.8 KB, 2 requests, same origin |
| maplibre-gl.js / .css | 174.9 / 7.8 KB | unchanged |
| Style JSON + sprite json/png | 59.3 KB, 3 requests | gone |
| TileJSON | 2.8 KB | 2.8 KB (preloaded) |
| Glyph ranges | 92.2 KB | 92.2 KB (requested as the library arrives) |
| Vector tiles (22) | 949 KB | 949 KB |

Vector tiles are about 70% of all bytes. They come straight from OpenFreeMap and contain every layer, so hiding layers does not shrink them.

## What changed, and what it bought

1. **Fonts self-hosted and subset** (`fonts/`). Latin only, Fraunces limited to the weights (600-800) and optical sizes (14-48) the CSS uses, Public Sans to 400-700. Every character in the data and page was checked against the subsets. 94 KB -> 70 KB and the Google CSS -> gstatic chain is gone. Screenshots differ from main only by sub-pixel edge antialiasing of text.
2. **Data** (`scripts/build.py`). `places.<hash>.js` is a columnar, index-coded table without the unused OSM ids: 533 KB -> 123 KB raw, 66 KB -> 27 KB brotli. Ownership notes, sources and status links moved to `detail.<hash>.json`, fetched once the map is idle. Decoding reproduces the old data exactly (0 mismatches over 1,436 places and 196 brands). The 243 / 532 / 661 split is unchanged.
3. **Map style baked in** (`scripts/make_style.py`). The page no longer fetches positron, waits, and rewrites it on every load. The sprite sheet is gone (its one dot icon is drawn on a canvas, pixel-matched), as are transparent and never-visible layers (55 -> 35). Screenshots at zoom 9.5, 10.9, 13.5 and 16 match main to within about 10 map pixels.
4. **Startup work**: search text and link ids are built on first use rather than for all 1,436 places; the list paints 40 rows first and fills to 250 when idle (also makes each filter keystroke cheaper); pins skip the 1,436-id literal filter when nothing is filtered; `crossSourceCollisions: false`; dead header-art code removed.
5. **Request ordering**: TileJSON is preloaded; the two glyph ranges are requested when the library arrives instead of in `<head>`, where they slowed the library on a slow link (mobile pins -15%, idle -6% from this alone); card details wait for the map's first idle.

## Why frame times did not move

A CPU profile of 80 panned frames at zoom 13.5 (software GL) put 94% of main-thread time in native `(program)`, which is the GL rasteriser. JavaScript was about 4 ms per frame, and MapLibre's own placement work was negligible. Frame time tracks the number of canvas pixels:

| `pixelRatio` (390x844 phone) | pan, overview (mean) | pan, zoom 13.5 (mean) |
|---|---|---|
| 2 (current cap) | 46 ms | 63 ms |
| 1.5 | 32 ms | 43 ms |
| 1 | 21 ms | 30 ms |

Hiding layers confirmed road lines are the largest per-pixel cost, then labels. Neither can be removed without changing the map.

## Not done (changes the look or carries risk), for the owner to decide

- **Lower `pixelRatio` on phones, or only while a gesture is in progress.** The table above is the effect: roughly -30% (1.5) or -55% (1) frame time under software rendering. It makes the map softer, and switching the ratio mid-gesture resizes the canvas, which can flash. Real iPhone GPUs are not fill-rate bound the way the simulator is, so this mainly helps the simulator and low-end phones.
- **Shrink the canvas to the part the bottom sheet leaves visible.** The sheet is opaque but the map renders the pixels under it too (about 46% by default). Rendering only the visible part would cut phone fill work by a third or more, but needs a resize on every sheet snap and care with the existing `applyBounds` logic.
- **Self-host and subset the glyph ranges** (about 20 KB): other ranges would need to keep working, so it was left alone.
- Pre-existing, unchanged: on phones, opening a place by deep link logs MapLibre's "Map cannot fit within canvas with the given bounds, padding, and/or offset" warning (identical on main).

## Trade-offs

- `index.html` is 17 KB over the wire instead of 15 KB because it carries the map style; that is cheaper than the two requests it replaces.
- The map style no longer follows upstream OpenFreeMap style changes automatically. Re-run `python3 -I scripts/make_style.py` to refresh it. Tiles, TileJSON and glyphs still come live from OpenFreeMap.
- A place card opened before `detail.<hash>.json` arrives (rare, since it loads right after the map is idle) shows briefly without notes and sources, then fills in.
- The first 40 list rows now paint before the remaining 210 (which fill in on idle).

## Follow-up: phone `pixelRatio` capped at 1.5 (owner decision, 23 Nov 2026)

`index.html` now caps the map's `pixelRatio` at 1.5 on phone-width screens (desktop stays at 2). Checked on a local run of this branch with the same harness, mobile profile, median of 3 cold runs, on an Apple-silicon Mac (Chromium software GL, much faster than the cloud sandbox used for the table above, so frame times were already near 60 fps and only the slowest frames show a difference):

| Metric (mobile profile) | cap 2 | cap 1.5 |
|---|---|---|
| Frame time pan, overview (p50/p95/max) | 16.7 / 17.5 / 17.7 | 16.6 / 17.5 / 17.7 |
| Frame time pan, zoom 13.5 | 16.7 / 33.3 / 34.3 | 16.7 / 17.6 / 17.7 |
| Frame time zoom 13-14 | 16.7 / 33.4 / 34.2 | 16.7 / 17.6 / 17.6 |
| DCL / load / map idle | 973 / 1806 / 3454 ms | 935 / 1813 / 3440 ms |
| Bytes, initial load | 597.7 KB | 597.7 KB |

The cap removes the 33 ms frames at downtown zoom without touching load numbers. Functional check (`verify.js`, phone profile): 0 failures. Looked at in the iPhone 17 simulator: labels and pins still read crisp. The larger win measured earlier in the cloud sandbox (-30% frame time at 1.5) applies to slower or software-rendered devices.

Not done, still the owner's call: shrinking the canvas to the area above the bottom sheet.
