"""Build places.js from OpenStreetMap places + the researched brand table.

Run:  python3 -I scripts/build.py   (from the louisville-food-money-matrix folder)
Input:  data/osm-raw.json  (Overpass export with edit metadata, Louisville area bounding box)
        data/brands.json   (researched owners, one record per brand)
        data/verification.json (reviewed operating status, keyed by stable OSM id)
Output: places.<hash>.js   (window.BRANDS + window.PLACES), and index.html is updated to load it
"""
import hashlib, json, math, re, sys, unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BBOX = (37.99, -85.96, 38.39, -85.40)  # south, west, north, east

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    s = s.lower().replace("&", " ")
    s = re.sub(r"[’'`.]", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

# Rows that are not really places to eat out (stadium stands, generic labels, shops)
DROP_EXACT = {norm(x) for x in """
Concession|Concessions|Concession Counter|Dining Area|Vending Area|Game|Lounge|Bar Area|Grill|Cafe|The Cafe|Corner|
Lunch Counter|Marketplace/Restaurants|Marketplace Restaurant|Premium Box Concessions|Premium Club Lounge|Home Plate Snacks|
Painting with a Twist|PT's Showclub|Beer Store|Waterfront Wine & Spirits|Morris' Liquors and Deli|Spirit Depot|Taste|Crave|
Diamond Drinks Counter|Kentucky Cattleman's Association Concession|Kentucky Pork Producers Concession|BCHS Concession Stand|
Miller Light Terrace Club Lounge|Budweiser Bowtie Bar|Goose Island Beer Bridge|Woodford Reserve Club Entrance|Heaven Hill Club Bar|
Old Foresters Bar East|Old Foresters Bar North|Old Foresters Bar West|Fielder's Fare|Fielder's Fare Counter|Grand Slam Grill|
Grand Slam Grill Counter|First Base Grill|First Base Grill Counter|Metro Grill Counter|Overlook Grill|Overlook Grill Counter|
Gateway Grill|Lynn's Cafe Counter|SBTS Cafeteria|SRC Cafe|Atrium Cafe|Founders Café|Speed Cafe|Neighborhood Services|
Divinity Fine Catering|Red Clover Catering|Forest Springs Nutrition|Bourdon Academy Tasting Room|Lexington / Bauer;Asahi|
Papa John's Food and Dining Area|4th Street Live! Food Court|Taco Bell Counter|KFC Counter|Haute Dog Counter|
Farmstead Chicken and Burgers Counter|Bourbon Barrel BBQ Counter|KemtuckyAle Taproom Counter|Coffee on the Go|Big Boy|
Angel's Envy Distillery|Evan Williams|Prohibition Craft Spirits|Prova Spirits|Cafe at Main Street|Lobby Bar & Grill|
Family Ties|Kentcuky Fried Chicken and Beer|Wagner's Pharmacy Counter|American Smokehouse Stadium|Fuzzy’s The 15th Club, Food & Spirits|Burnett's V lounge|
AC Lounge|Premium Club|Spirit Room|Spirit Room Bar|J-town Beach|Furlongs|Jockey Silks Bourbon Bar
""".replace("\n", "").split("|") if x.strip()}
DROP_RE = re.compile(r"\b(concession|concessions|vending|club lounge)\b")
# "counter"/"stand" mark stadium stalls only when the row has no street address (real businesses like "The Counter" do)
STALL_RE = re.compile(r"\b(counter|stand)\b")

# OSM tag → food type shown in the filter. Patterns are whole words (optionally plural), so "tea" can't match "steak".
CUISINE = [
    (r"coffee|tea|juice|bubble|smoothie", "Coffee & café"),
    (r"ice_cream|frozen_yogurt|custard", "Ice cream & frozen"),
    (r"donut|bakery|pastry|cake|cookie|dessert|bagel|pie", "Bakery & sweets"),
    (r"breakfast|brunch|pancake", "Breakfast & brunch"),
    (r"pizza", "Pizza"),
    (r"burger|hot_dog", "Burgers"),
    (r"chicken|wings", "Chicken"),
    (r"sandwich|deli|sub|salad|soup", "Sandwiches & deli"),
    (r"mexican|tex-mex|taco|burrito|latin|salvadoran|cuban|peruvian|colombian|venezuelan", "Mexican & Tex-Mex"),
    (r"chinese|japanese|sushi|thai|vietnamese|korean|asian|indian|nepal|ramen|noodle|filipino|pho|hibachi", "Asian"),
    (r"barbecue|bbq|southern|cajun|soul|creole|regional", "BBQ & Southern"),
    (r"steak|seafood|fish", "Steak & seafood"),
    (r"italian", "Italian"),
    (r"mediterranean|greek|lebanese|middle_eastern|turkish|kebab|persian|falafel|arab|yemeni|ethiopian|african|somali", "Mediterranean & Middle Eastern"),
    (r"american|diner|bar_and_grill|buffet|chili|caribbean|french|german|irish", "American"),
]
NAME_HINT = [
    (r"\b(coffee|espresso|cafe|caffe|tea|boba|juice|roast|roasters|roastery)", "Coffee & café"),
    (r"\b(ice cream|creamery|freeze|custard|gelato|yogurt|sno)", "Ice cream & frozen"),
    (r"\b(bakery|bakehouse|donut|doughnut|cake|cookie|pie|sweet|patisserie|bagel)", "Bakery & sweets"),
    (r"\b(pizza|pizzeria|slice)", "Pizza"),
    (r"\b(burger|dog)", "Burgers"),
    (r"\b(chicken|wing)", "Chicken"),
    (r"\b(taco|taqueria|mexican|cantina|mexico|tex mex|burrito|el |la |los |las )", "Mexican & Tex-Mex"),
    (r"\b(sushi|thai|pho|china|chinese|wok|asian|ramen|hibachi|korean|india|indian|kathmandu|bento|noodle|buffet)", "Asian"),
    (r"\b(bbq|barbecue|bar b|smokehouse|smoke)", "BBQ & Southern"),
    (r"\b(steak|steakhouse|seafood|fish|crab|oyster|catch)", "Steak & seafood"),
    (r"\b(italian|ristorante|trattoria|osteria|pasta)", "Italian"),
    (r"\b(gyro|greek|pita|mediterranean|kabob|kebab|falafel|persian|caspian|ethiopian|addis|lebanese)", "Mediterranean & Middle Eastern"),
    (r"\b(pub|tavern|bar|brew|brewing|brewery|taproom|taphouse|tap|saloon|lounge|beer|bourbon|whiskey|wine)", "Bar & pub"),
    (r"\b(deli|sandwich)", "Sandwiches & deli"),
]
def kind_for(tags, name):
    a = tags.get("amenity") or tags.get("shop") or ""
    cu = (tags.get("cuisine") or "").lower()
    if cu:
        for pat, k in CUISINE:
            if re.search(r"(?<![a-z])(?:" + pat + r")s?(?![a-z])", cu.split(";")[0]):
                return k
    n = norm(name) + " "
    for pat, k in NAME_HINT:
        if re.search(pat + r"s?\b", n):
            return k
    if a in ("bar", "pub", "biergarten"): return "Bar & pub"
    if a in ("cafe", "coffee"): return "Coffee & café"
    if a == "ice_cream": return "Ice cream & frozen"
    if a in ("bakery", "pastry"): return "Bakery & sweets"
    if a == "deli": return "Sandwiches & deli"
    return "Other" if a != "restaurant" else "American"

AREAS = [
    ("Downtown", 38.2540, -85.7590), ("NuLu & Butchertown", 38.2560, -85.7370),
    ("Old Louisville", 38.2340, -85.7600), ("Highlands", 38.2380, -85.7180),
    ("Germantown & Schnitzelburg", 38.2290, -85.7370), ("Crescent Hill & Clifton", 38.2560, -85.6990),
    ("St. Matthews", 38.2500, -85.6430), ("West End & Portland", 38.2520, -85.8080),
    ("South End", 38.1900, -85.7750), ("Audubon & Airport", 38.2050, -85.7300),
    ("Shively", 38.2000, -85.8230), ("Valley Station & PRP", 38.1250, -85.8550),
    ("Okolona", 38.1420, -85.6900), ("Highview & Fern Creek", 38.1550, -85.6050),
    ("Jeffersontown", 38.1940, -85.5640), ("Hikes Point & Buechel", 38.2120, -85.6600),
    ("Lyndon & Westport", 38.2700, -85.6000), ("Middletown & Anchorage", 38.2450, -85.5300),
    ("Prospect & Northeast", 38.3300, -85.6100), ("Fairdale", 38.1050, -85.7600),
    ("Hillview & Mount Washington", 38.0600, -85.6300), ("Shepherdsville", 38.0000, -85.7000),
    ("Crestwood & Oldham Co.", 38.3300, -85.4700),
    ("Jeffersonville, IN", 38.2800, -85.7350), ("Clarksville, IN", 38.3050, -85.7700),
    ("New Albany, IN", 38.2950, -85.8300), ("Floyds Knobs, IN", 38.3300, -85.8800),
]
IN_CITIES = {"jeffersonville": "Jeffersonville, IN", "clarksville": "Clarksville, IN", "new albany": "New Albany, IN",
             "floyds knobs": "Floyds Knobs, IN", "sellersburg": "Clarksville, IN", "georgetown": "Floyds Knobs, IN"}

# Louisville Independent Business Alliance members (data/liba-members.txt). LIBA only admits businesses that are
# majority-owned by Louisville-area residents, headquartered locally, not publicly traded and not franchises.
LIBA_STOP = {"the", "and", "restaurant", "restaurants", "cafe", "bar", "grille", "grill", "co", "company", "pub", "pubs",
             "inc", "llc", "traditional", "coffee", "house", "kitchen", "catering", "s"}
LIBA_NOT = {"dragon cafe", "pizza bar"}            # loose matches that are different businesses
LIBA_ALIAS = {"bandido taqueria mexicana": "bandidos taqueria mexicana", "flannigans ale house": "flanagans ale house",
              "wiltshire at the speed": "wiltshire pantry bakery cafe", "wiltshire on market": "wiltshire pantry bakery cafe"}

def liba_core(s):
    return " ".join(w for w in norm(s).split() if w not in LIBA_STOP)

def load_liba():
    members = [m for line in (ROOT / "data/liba-members.txt").read_text().splitlines()
               if not line.startswith("#") for m in line.split("|") if m.strip()]
    return {liba_core(m) for m in members if liba_core(m)}

def is_liba(name, cores):
    n = norm(name)
    if n in LIBA_NOT: return False
    pc = liba_core(LIBA_ALIAS.get(n, n))
    if not pc: return False
    for c in cores:
        if pc == c: return True
        if len(c) >= 5 and pc.startswith(c + " "): return True
        if len(pc) >= 5 and c.startswith(pc + " "): return True
    return False

def miles(a, b):
    R, r = 3958.8, math.pi / 180
    dl, dg = (b[0] - a[0]) * r, (b[1] - a[1]) * r
    h = math.sin(dl / 2) ** 2 + math.cos(a[0] * r) * math.cos(b[0] * r) * math.sin(dg / 2) ** 2
    return 2 * R * math.asin(math.sqrt(h))

# Rough Ohio River line (lng, lat), east to west; Indiana is the north/west side.
RIVER = [(-85.40, 38.45), (-85.50, 38.42), (-85.55, 38.395), (-85.60, 38.378), (-85.63, 38.362), (-85.66, 38.335),
         (-85.69, 38.302), (-85.71, 38.285), (-85.735, 38.268), (-85.76, 38.262), (-85.79, 38.277), (-85.81, 38.277),
         (-85.83, 38.275), (-85.86, 38.263), (-85.885, 38.24), (-85.90, 38.20), (-85.92, 38.15), (-85.94, 38.08), (-85.95, 37.95)]
INDIANA = RIVER + [(-86.2, 37.95), (-86.2, 38.6), (-85.40, 38.6)]

def in_indiana(lat, lng):
    inside, j = False, len(INDIANA) - 1
    for i in range(len(INDIANA)):
        xi, yi = INDIANA[i]; xj, yj = INDIANA[j]
        if (yi > lat) != (yj > lat) and lng < (xj - xi) * (lat - yi) / (yj - yi) + xi:
            inside = not inside
        j = i
    return inside

def area_for(lat, lng, tags):
    city = norm(tags.get("addr:city", ""))
    if city in IN_CITIES: return IN_CITIES[city]
    st = tags.get("addr:state", "").upper()
    indiana = st == "IN" if st in ("IN", "KY") else in_indiana(lat, lng)
    cands = [a for a in AREAS if a[0].endswith(", IN") == indiana]
    return min(cands, key=lambda a: (a[1] - lat) ** 2 + ((a[2] - lng) * 0.785) ** 2)[0]

def main():
    brands = json.loads((ROOT / "data/brands.json").read_text())
    verification = json.loads((ROOT / "data/verification.json").read_text())
    statuses = {"open", "unsure", "closed", "renamed", "duplicate_or_not_a_restaurant"}
    for osm, result in verification.items():
        if result.get("status") not in statuses:
            raise ValueError(f"Invalid verification status for {osm}: {result.get('status')!r}")
    # A pattern starting with "=" must equal the whole name (for generic words like "Mesh" or "Bravo");
    # any other pattern matches as a whole-word prefix ("subway" matches "Subway - Bardstown Rd").
    pats = []
    for i, b in enumerate(brands):
        for m in b["m"]:
            pats.append((norm(m.lstrip("=")), m.startswith("="), i))
    pats.sort(key=lambda x: -len(x[0]))  # longest prefix wins

    def brand_of(tags):
        # Match on the name only: OSM brand tags go stale when a new business moves into an old chain building.
        for key in ("name",):
            n = norm(tags.get(key, ""))
            if not n: continue
            for p, exact, i in pats:
                if n == p or (not exact and n.startswith(p + " ")):
                    return i
        return None

    els = json.loads((ROOT / "data/osm-raw.json").read_text())["elements"]
    rows, dropped = [], Counter()
    for e in els:
        t = e.get("tags", {})
        name = (t.get("name") or t.get("brand") or "").strip()
        lat = e.get("lat") or e.get("center", {}).get("lat")
        lng = e.get("lon") or e.get("center", {}).get("lon")
        if not name or lat is None: dropped["no name"] += 1; continue
        # A reviewed rename keeps the place on the map under its current name (matched to brands by that name).
        vr = verification.get(e["type"][0] + str(e["id"]))
        if vr and vr["status"] == "renamed" and vr.get("new_name"):
            name = vr["new_name"]; t = {**t, "name": name}
        if t.get("indoor") == "room": dropped["stall inside an arena or mall"] += 1; continue
        if norm(name).startswith(("ocharleys", "zoes kitchen")): dropped["closed"] += 1; continue  # O'Charley's corporate stores closed Sept 2026; Zoës Kitchen was folded into Cava
        if t.get("disused:amenity") or t.get("was:amenity") or t.get("opening_hours") == "closed": dropped["closed"] += 1; continue
        n = norm(name)
        if n in DROP_EXACT or DROP_RE.search(n) or (STALL_RE.search(n) and not t.get("addr:street")):
            dropped["not a place to eat out"] += 1; continue
        if not (BBOX[0] <= lat <= BBOX[2] and BBOX[1] <= lng <= BBOX[3]): dropped["outside"] += 1; continue
        bi = brand_of(t)
        street = " ".join(x for x in [t.get("addr:housenumber", ""), t.get("addr:street", "")] if x).strip()
        street = (vr or {}).get("address") or street  # reviewed current address; retain the original OSM point
        b = brands[bi] if bi is not None else None
        rows.append({
            "n": b["n"] if b and norm(b["n"]).split()[0] == n.split()[0] and len(n) <= len(norm(b["n"])) + 12 else re.sub(r"\s+", " ", name),
            "osm": e["type"][0] + str(e["id"]),   # stable id, used by data/verification.json
            "ll": [round(lat, 5), round(lng, 5)],
            "a": street, "area": area_for(lat, lng, t),
            "k": b["k"] if b else (vr or {}).get("kind") or kind_for(t, name),   # "kind" in verification.json fixes a cuisine the old OSM tags got wrong
            "c": b["c"] if b else "ind",
            "b": bi if bi is not None else -1,
            "_key": f"b{bi}" if bi is not None else n,
            "_addr": norm(street),
            "_name": n,
            "e": int(e["timestamp"][:4]) if e.get("timestamp") else None,   # year the OSM entry was last edited
        })

    # Merge duplicates: OSM often maps one place twice (a point and a building). Same brand/name within 120 m counts
    # as one place unless both rows carry different street addresses (two real branches close together).
    def same_place(o, r):
        if o["_key"] != r["_key"] or miles(o["ll"], r["ll"]) >= 0.075: return False
        # a restaurant group can have several different places in one building (e.g. the Galt House)
        if not (o["_name"].startswith(r["_name"]) or r["_name"].startswith(o["_name"])): return False
        return not (o["_addr"] and r["_addr"] and o["_addr"] != r["_addr"])
    out = []
    for r in rows:
        twin = next((o for o in out if same_place(o, r)), None)
        if twin:
            twin["e"] = max(filter(None, [twin["e"], r["e"]]), default=None)
            dropped["duplicate"] += 1; continue
        out.append(r)
    # Merge spelling variants of the same unbranded place (e.g. "Zeggz" / "ZEGGZ Amazing Eggs")
    final = []
    for r in out:
        if r["b"] == -1:
            k = r["_key"]
            if any(o["b"] == -1 and miles(o["ll"], r["ll"]) < 0.1 and (o["_key"].startswith(k) or k.startswith(o["_key"])) for o in final):
                dropped["duplicate"] += 1; continue
        final.append(r)
    # Filter after deduplication so a duplicate OSM node cannot resurrect a removed place.
    reviewed, verification_dropped = [], Counter()
    for r in final:
        result = verification.get(r["osm"])
        status = result["status"] if result else "unreviewed"
        if status == "renamed" and result.get("new_name"): status = "open"   # relabelled above, still operating
        if status not in {"open", "unsure"}:
            verification_dropped[status] += 1   # closed, renamed (no successor), duplicate or unreviewed
            continue
        r["status"] = status
        r["checked"] = result["checked"]
        if result["evidence"]:
            r["status_url"] = result["evidence"][0]["url"]
        reviewed.append(r)
    final = reviewed
    print("Verification dropped:", dict(verification_dropped))
    print("Operating status unsure (kept and flagged):", sum(r["status"] == "unsure" for r in final))

    # "Confirmed independent": a LIBA / Louisville Originals member, or a researched local owner with a source
    cores = load_liba()
    for r in final:
        if r["c"] != "ind": continue
        b = brands[r["b"]] if r["b"] >= 0 else None
        if is_liba(r["n"], cores) or (b and b.get("src") and not b.get("u")):
            r["v"] = 1
    final.sort(key=lambda r: ({"pe": 0, "corp": 1, "ind": 2}[r["c"]], norm(r["n"])))
    for r in final: r.pop("_key"); r.pop("_addr"); r.pop("_name")

    used = sorted({r["b"] for r in final if r["b"] >= 0})
    remap = {old: new for new, old in enumerate(used)}
    B = []
    for old in used:
        b = dict(brands[old]); b.pop("m")
        B.append(b)
    for r in final:
        if r["b"] >= 0: r["b"] = remap[r["b"]]

    # Sanity checks
    cnt = Counter(r["c"] for r in final)
    assert sum(cnt.values()) == len(final)
    for r in final:
        assert BBOX[0] <= r["ll"][0] <= BBOX[2] and BBOX[1] <= r["ll"][1] <= BBOX[3], r
        if r["c"] != "ind":
            b = B[r["b"]]
            assert b["o"], b
            assert b["src"] or b.get("u"), b["n"]
    for b in B:
        if not b.get("u"): assert b["src"].startswith("https://"), b["n"]

    # JSON.parse on a string literal parses much faster than an equivalent object literal for data this size.
    # The file name carries a content hash so it can be cached forever; index.html is pointed at the new name.
    lit = lambda v: "JSON.parse(" + json.dumps(json.dumps(v, ensure_ascii=False, separators=(",", ":")), ensure_ascii=False) + ")"
    js = ("/* Generated by scripts/build.py — do not edit by hand.\n"
          "   Places © OpenStreetMap contributors (ODbL). Ownership research: see data/brands.json. */\n"
          "window.BRANDS=" + lit(B) + ";\n"
          "window.PLACES=" + lit(final) + ";\n")
    digest = hashlib.sha256(js.encode()).hexdigest()[:10]
    for old in ROOT.glob("places*.js"):
        old.unlink()
    out_name = f"places.{digest}.js"
    (ROOT / out_name).write_text(js)
    page = ROOT / "index.html"
    html = page.read_text()
    html2 = re.sub(r'<script src="places[^"]*\.js"></script>', f'<script src="{out_name}"></script>', html)
    assert html2.count(out_name) == 1, "index.html has no places script tag to update"
    page.write_text(html2)
    print("wrote", out_name)
    print(f"{len(final)} places ({dict(cnt)}), {len(B)} brands used; dropped {dict(dropped)}")
    print("Confirmed independents:", sum(1 for r in final if r.get("v")), "of", cnt["ind"])
    print("areas:", Counter(r["area"] for r in final).most_common())
    print("kinds:", Counter(r["k"] for r in final).most_common())

if __name__ == "__main__":
    sys.exit(main())
