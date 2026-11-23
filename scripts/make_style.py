"""Bake the map style into index.html.

Run:  python3 -I scripts/make_style.py      (needs network access to tiles.openfreemap.org)

Takes OpenFreeMap's "positron" style, applies this site's colours, and drops what can never be seen at the
zoom levels the map allows (3 - 18, min zoom 9.3): the sprite sheet, boundary/shield/airport/poi layers,
fully transparent layers and layers that end below the minimum zoom. The result is written between the
<script id="style"> tags in index.html, so the page doesn't fetch and rewrite a style at runtime.
Re-run it only if you want to pick up an upstream style change or change the palette.
"""
import json, re, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_ZOOM = 9.3   # keep in sync with minZoom in index.html
PAL = dict(land="#F3F7DC", park="#EAF3CB", wood="#EAF3CB", water="#A8CADB", road="#FFFFFF", casing="#E4ECC1", minor="#FBFDF0",
           rail="#D8E2AF", bldg="#EEF4D2", label="#5B4663", hood="#8A7A90", water_label="#4F7F99")

def main():
    st = json.load(urllib.request.urlopen(urllib.request.Request("https://tiles.openfreemap.org/styles/positron", headers={"User-Agent": "louisville-eat-local-build"})))
    drop = re.compile(r"^(boundary|highway-shield|road_shield|airport|aeroway|poi|label_country|label_state)")
    layers = [l for l in st["layers"] if not drop.search(l["id"]) and l.get("source") != "ne2_shaded"]
    for l in layers:
        p = l.setdefault("paint", {}); i = l["id"]; sl = l.get("source-layer"); t = l["type"]
        if t == "background": p["background-color"] = PAL["land"]
        elif sl == "water" and t == "fill": p["fill-color"] = PAL["water"]; p["fill-opacity"] = 1
        elif sl == "waterway" and t == "line": p["line-color"] = PAL["water"]
        elif sl == "park" and t == "fill": p["fill-color"] = PAL["park"]; p["fill-opacity"] = .6
        elif sl == "landcover" and t == "fill": p["fill-color"] = PAL["wood"]; p["fill-opacity"] = .5
        elif sl == "landuse" and t == "fill": p["fill-opacity"] = 0
        elif sl == "building" and t == "fill": p["fill-color"] = PAL["bldg"]; p["fill-opacity"] = 0
        elif sl == "transportation" and t == "line":
            minor = re.search(r"minor|service|path|track", i)
            if minor: l["minzoom"] = max(l.get("minzoom", 0), 12)   # fewer side streets at overview zoom
            p["line-color"] = PAL["casing"] if "casing" in i else PAL["rail"] if re.search(r"rail|transit", i) else PAL["minor"] if minor else PAL["road"]
        elif t == "symbol":
            p["text-color"] = PAL["water_label"] if "water" in i else PAL["hood"] if re.search(r"other|neighbourhood|suburb", i) else PAL["label"]
            if not re.search(r"city|water", i): p["text-opacity"] = ["interpolate", ["linear"], ["zoom"], 11.2, 0, 12, 1]   # keep the overview clean
            p["text-halo-color"] = PAL["land"]; p["text-halo-width"] = 1.4; p["text-halo-blur"] = 0
            p.pop("icon-color", None)
    # nothing to draw: invisible fills, and layers that end before the lowest zoom the map allows
    layers = [l for l in layers if l.get("paint", {}).get("fill-opacity", 1) != 0 and l.get("maxzoom", 99) > MIN_ZOOM]
    for l in layers:
        if not l.get("paint"): l.pop("paint", None)
    style = {"version": 8, "glyphs": st["glyphs"], "sources": {"openmaptiles": st["sources"]["openmaptiles"]}, "layers": layers}
    blob = json.dumps(style, separators=(",", ":"))
    page = ROOT / "index.html"
    html = page.read_text()
    new, n = re.subn(r'(<script type="application/json" id="style">).*?(</script>)', lambda m: m.group(1) + blob + m.group(2), html, flags=re.S)
    assert n == 1, "index.html needs one <script type=\"application/json\" id=\"style\"> block"
    page.write_text(new)
    print(f"style: {len(st['layers'])} -> {len(layers)} layers, {len(blob)} bytes; glyphs {st['glyphs']}")

if __name__ == "__main__":
    sys.exit(main())
