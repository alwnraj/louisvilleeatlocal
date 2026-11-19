# Louisville Eat Local — verification review

**Latest review:** see [Round 5 findings](ROUND5_REPORT.md). It resolves 6 of the remaining 59 unsure records and retains 53 flagged places. [Round 4](ROUND4_REPORT.md), [Round 3](ROUND3_REPORT.md) and the counts below document earlier reviews and are historical.

Review date: **18 November 2026**. Findings were reported before site integration. Original first-pass records and independent rechecks are preserved below.

## Coverage

All **25 batches / 1,613 stable OSM IDs** have results, in input order, with no missing or duplicate IDs.
Every first-pass non-open verdict received a second pass. A targeted sample of 23 original open verdicts was checked again, including Panera and Burger King.
Earlier completed first-pass records date to 17 November; new research and second passes date to 18 November. This is a web-evidence review, not a phone or in-person census.

| Final status | Places |
|---|---:|
| open | 1254 |
| closed | 122 |
| renamed | 14 |
| duplicate_or_not_a_restaurant | 6 |
| unsure | 217 |

Proposed removals: **142**. Keep **217 unsure places visible and flag their operating status as not confirmed**, per the user’s instruction.

## Corrections and traps

- The initial 59-removal audit restored both Pizza Hut locations (8131 Bardstown / 9160 Taylorsville), White Castle in Clarksville, and El Monstruo; 15 initial closure claims became unsure. El Monstruo replaced Funmi’s, rather than the reverse.
- Akiko’s announced a March 2026 closure but later reached an agreement to remain open. It must not be removed solely on the earlier announcement. Vincenzo’s and Mile Wide have future closure dates; announcements alone do not make them closed on 18 November.
- Official location pages and delivery menus can remain after closure. Conversely, a missing/changed locator URL does not itself establish closure. Temporary closure and “closed now” do not mean permanent closure.
- Moved businesses are evaluated at the mapped point, not at the replacement location. Coordinate-only or conflicting-address entries stay unsure when a match within roughly 150 m cannot be established.
- The build canonicalized Haymarket café (w329525593, 3020 River Road) to Haymarket Whiskey Bar, and three Louisville Moby Dick Seafood locations (w337418676, w339255615, w369784998) to the unrelated Moby Dick House of Kabob chain. These are brand-matching errors, not evidence of closure or a business rename. Restrict those ambiguous matching rules before publishing.
- Source searches exposed same-name places in other cities and stale predecessor/successor listings. Sources were matched to Louisville / Southern Indiana and exact addresses where available; ambiguous matches remain flagged.

## Batch completeness (first pass)

| Batch | Total | Open | Closed | Renamed | Not restaurant / duplicate | Unsure |
|---|---:|---:|---:|---:|---:|---:|
| chain_00 | 61 | 60 | 0 | 0 | 0 | 1 |
| chain_01 | 42 | 39 | 3 | 0 | 0 | 0 |
| chain_02 | 67 | 65 | 2 | 0 | 0 | 0 |
| chain_03 | 52 | 42 | 5 | 0 | 0 | 5 |
| chain_04 | 70 | 42 | 4 | 0 | 0 | 24 |
| chain_05 | 60 | 55 | 4 | 0 | 0 | 1 |
| chain_06 | 71 | 65 | 6 | 0 | 0 | 0 |
| chain_07 | 75 | 68 | 3 | 0 | 1 | 3 |
| chain_08 | 75 | 58 | 8 | 0 | 0 | 9 |
| chain_09 | 72 | 64 | 2 | 0 | 0 | 6 |
| chain_10 | 72 | 59 | 3 | 0 | 0 | 10 |
| chain_11 | 73 | 58 | 3 | 0 | 0 | 12 |
| chain_12 | 75 | 27 | 6 | 0 | 0 | 42 |
| chain_13 | 75 | 43 | 13 | 0 | 0 | 19 |
| chain_14 | 33 | 22 | 3 | 0 | 0 | 8 |
| ind_00 | 65 | 11 | 0 | 1 | 0 | 53 |
| ind_01 | 65 | 12 | 5 | 0 | 0 | 48 |
| ind_02 | 65 | 42 | 5 | 1 | 1 | 16 |
| ind_03 | 65 | 26 | 2 | 1 | 0 | 36 |
| ind_04 | 65 | 17 | 2 | 1 | 0 | 45 |
| ind_05 | 65 | 24 | 2 | 0 | 0 | 39 |
| ind_06 | 65 | 39 | 1 | 0 | 2 | 23 |
| ind_07 | 65 | 38 | 11 | 0 | 0 | 16 |
| ind_08 | 65 | 34 | 7 | 1 | 1 | 22 |
| ind_09 | 55 | 23 | 8 | 0 | 0 | 24 |

## Every proposed removal

Renamed records remove the stale old name; this report does not automatically add or classify the successor. Duplicate removals keep the other matching record.

| OSM ID | Name | Mapped address / point | Verdict and reason | Evidence |
|---|---|---|---|---|
| w343475147 | Bob Evans | 9797 Blairwood Road | closed: Independent address-matched listing explicitly marks 9797 Blairwood permanently closed. Checked in web search on2026-11-18. | [source 1](https://wanderlog.com/place/details/3285960/bob-evans) |
| w337706686 | Captain D's | 2960 Breckenridge Lane | closed: Independent WLKY publication confirms permanent closure at 2960 Breckenridge Lane in May 2020. Checked in web search on2026-11-18. | [source 1](https://www.wlky.com/article/captain-ds-in-hikes-point-is-closing-for-good/32630949) |
| n3433086546 | Crumbl | 4110 Summit Plaza Drive | closed: Independent delivery listing explicitly labels4110SummitPlaza PERM CLOSED, matching recent news closure. Checked in web search on2026-11-18. | [source 1](https://www.ubereats.com/store/perm-closed-crumbl-paddock-ky/P6fkCUx6V9WJqs7ybB-ITQ) |
| n3383405336 | Gordon Biersch Brewery Restaurant | 400 South 4th Street | closed: Independent LEO report confirms FourthStreetLive brewpub permanently closed after13years. Checked in web search on2026-11-18. | [source 1](https://leoweekly.com/news/gordon-biersch-closes-after-13-years-at-fourth-street-live-18024064/) |
| w333996844 | Hardee's | 3459 Taylor Boulevard | closed: Address-matched listing says CLOSED at 3459 Taylor; official Louisville directory lists two other stores and omits Taylor. Checked in web search on2026-11-18. | [source 1](https://www.restaurantji.com/ky/louisville/hardees-/) |
| w824935574 | Hardee's | 301 West Court Avenue | closed: Independent commercial listing labels 301 W Court former Hardee’s and offers premises for lease. Checked in web search on2026-11-18. | [source 1](https://www.loopnet.com/Listing/301-W-Court-Ave-Jeffersonville-IN/39727551/) |
| n454373037 | McAlister's Deli | 10041 Forest Green Boulevard | closed: Lease brochure identifies suite 10041 Forest Green as available and formerly McAlisters Deli. | [source 1](https://images1.showcase.com/d2/HRZVLEBw2yYsMFtV4qVU2tn_YIrXR7KaRKwFPMgcUkA/document.pdf) |
| n3516264329 | Panera Bread | 38.25477, -85.75704 (Downtown) | closed: March 2021 report confirms permanent closure at 400 W Market, matching mapped corner. | [source 1](https://www.wlky.com/article/panera-bread-closes-downtown-louisville-location/35843236) |
| w329523557 | Panera Bread | 4024 Shelbyville Road | closed: Exact location explicitly titled PERM CLOSED; independently corroborated by WLKY Dec 2020 report. | [source 1](https://www.ubereats.com/store/perm-closed-panera-4024-shelbyville-rd/fft1TdXCR9ef19DnryedBw) |
| w300587052 | Qdoba | 4600 Shelbyville Road | closed: Current property listing describes former Qdoba space at exact address. | [source 1](https://www.loopnet.com/Listing/4600-Shelbyville-Rd-Louisville-KY/11998952/) |
| w337887153 | Sonic | 6460 Outer Loop | closed: Official Dunkin page lists current hours at exact former Sonic address. | [source 1](https://www.dunkindonuts.com/locations/us/ky/louisville/6460-outer-loop/store-364581/) |
| n6392727788 | Beef 'O' Brady's | 38.2417, -85.54542 (Middletown & Anchorage) | closed: Independent Toast page explicitly names location zzClosed Middletown at241Blankenbaker. Checked in web search on2026-11-18. | [source 1](https://www.toasttab.com/local/beef-o-bradys-middletown-ky/r-b6c2232b-c302-40e2-a761-550cdc622439) |
| w337698336 | Bravo Italian Kitchen | 206 Bullitt Lane | closed: Loaded local February9 2026 report confirms BullittLane restaurant permanently closed; same first-pass source reconfirmed, no better independent local detail found. Checked in web search on2026-11-18. | [source 1](https://www.wdrb.com/news/business/louisville-restaurant-near-oxmoor-center-closes-without-notice/article_07cb8e61-ffd6-4943-bb6b-f46098aaa352.html) |
| w337886842 | Burger King | 6450 Outer Loop | closed: Official October2025 city bulletin explicitly identifies 6450 Outer Loop as former Burger King. Independently searched and loaded search result; same primary evidence as first pass because strongest exact-address source. | [source 1](https://content.govdelivery.com/accounts/KYLOUISVILLE/bulletins/3f69c41) |
| n11980061535 | Chick-fil-A | 7405 New La Grange Road | duplicate_or_not_a_restaurant: July 2020 report describes exact 7405 New LaGrange facility as catering/delivery hub outside traditional restaurant model; 2025 health inspection record identifies food truck base. | [source 1](https://www.wlky.com/article/chick-fil-a-unveils-first-louisville-food-truck/33405512) |
| n13424045322 | Corelife Eatery | 38.32868, -85.76147 (Clarksville, IN) | closed: Loaded July6 2026 report confirms permanent July1 Clarksville closure; earlier2024 reopening article predates this and does not override. Checked in web search on2026-11-18. | [source 1](https://www.wdrb.com/news/business/corelife-eatery-closes-southern-indiana-location/article_cb371e2a-0b24-4694-8df9-15ffd89bb4b6.html) |
| n3442884750 | Del Frisco's | 4107 Oechsli Avenue | closed: Independent WLKY report says moved four miles from4107Oechsli to101Whittington in2020. Checked in web search on2026-11-18. | [source 1](https://www.wlky.com/article/del-friscos-finally-reopens-in-new-east-end-location/34563164) |
| n11980061493 | Domino's | 4111 North Dixie Highway | duplicate_or_not_a_restaurant: Independent job listing ties exact 4111 N Dixie address to Elizabethtown, supported by official Domino store. OSM city/address belongs far outside mapped West End point; classify misplaced entry rather than claiming real store closed. | [source 1](https://www.indeed.com/q-dominos-pizza-l-elizabethtown%2C-ky-jobs.html) |
| n3447808197 | Duck Donuts | 4600 Shelbyville Road | closed: Independent address-matched Restaurantji page marked CLOSED; first-pass permanent closure listing agrees. Checked in web search on2026-11-18. | [source 1](https://www.restaurantji.com/ky/louisville/duck-donuts-/) |
| n643389000 | Hard Rock Cafe | 424 South 4th Street | closed: Independent WYMT/WAVE report quotes company confirming permanent closure at424S4th. Checked in web search on2026-11-18. | [source 1](https://www.wymt.com/2020/12/23/hard-rock-cafe-in-louisville-to-permanently-close-after-16-years/) |
| n3447808162 | Jason's Deli | 4600 Shelbyville Road | closed: Independent current commercial leasing listing marks4600Shelbyville suite formerJason’sDeli; first-pass closure agrees. Checked in web search on2026-11-18. | [source 1](https://www.loopnet.com/Listing/4600-Shelbyville-Rd-Louisville-KY/11998952/) |
| n11980061488 | KFC | 2513 Preston Highway | closed: Exact 2513 Preston location explicitly marked CLOSED; Uber Eats title likewise says Closed. | [source 1](https://www.restaurantji.com/ky/louisville/kfc-2/) |
| w336611953 | KFC | 9487 Westport Road | closed: Exact 9487 Westport location named KFC - Closed; official delivery subpage persists, so old 404 alone was inadequate. | [source 1](https://www.superpages.com/louisville-ky/bpp/kfc-closed-471097291) |
| w337494272 | KFC | 3280 Taylor Boulevard | closed: Property updated Sept 28, 2026 offers former KFC at exact address; official /delivery page shows Closed all days. | [source 1](https://www.commercialcafe.com/commercial-property/us/ky/louisville/3280-taylor-blvd/) |
| w343716083 | Long John Silver's and Taco Bell | 1805 Blankenbaker Parkway | renamed → Taco Bell: Official Taco Bell page gives current dine-in and drive-thru weekly hours at 1805 Blankenbaker. Former combined Long John Silver’s/Taco Bell identity is obsolete; restaurant continues as Taco Bell. Checked 2026-11-18. | [source 1](https://locations.tacobell.com/ky/louisville/1805-blankenbaker-parkway.html) |
| n3516418238 | Maker's Mark Bourbon House & Lounge | 446 South 4th Street | closed: Independent local2024 food report confirms Maker’sMarkLounge replaced byBourbonRaw around2015, which later closed; old named venue no longer operates. Checked in web search on2026-11-18. | [source 1](https://foodanddine.com/scarpetta-modern-italian-coming-to-fourth-street-live-this-fall/) |
| w337694469 | Mimi's Cafe | 615 South Hurstbourne Parkway | closed: Independent January2021 local food report confirms closure at615S Hurstbourne. Checked in web search on2026-11-18. | [source 1](https://foodanddine.com/oui-monsieur-the-fast-casual-mimis-cafe-is-now-extinct-in-louisville/) |
| n738010898 | Mitchell's Fish Market | 4031 Summit Plaza Drive | closed: Independent WLKY confirms final serviceOctober26 2024 at4031SummitPlaza. Checked in web search on2026-11-18. | [source 1](https://www.wlky.com/article/louisville-mitchells-fish-market-closes-seafood-why-search-new-location/62727953) |
| w336676513 | Red Robin | 9870 Von Allmen Court | closed: Reloaded exact store listing explicitly PERM CLOSE at9870VonAllmen; same first-pass source reconfirmed, further independent source needed. Checked in web search on2026-11-18. | [source 1](https://www.ubereats.com/store/perm-close-red-robin-gourmet-burgers-9870-von-allmen-court/nKQxk8BQQ4-2JIJ-lc99wg) |
| w337607249 | Smokey Bones | 2525 Hurstbourne Gem Lane | closed: Exact 2525 Hurstbourne location unavailable since Feb 2026; independent Courier Journal April 2026 report confirms chainwide remaining Kentucky closure.; Courier Journal April 2026 report says final Kentucky store Bowling Green closed; Louisville store therefore already gone, closure date not inferred from platform timestamp. | [source 1](https://www.ubereats.com/store/smokey-bones-jeffersontown/KWlXICDWTmCMFaGvpLf6pg) · [source 2](https://finance.yahoo.com/markets/stocks/articles/smokey-bones-closes-lone-kentucky-180817616.html) |
| n3373719472 | Smoothie King | 1504 Bardstown Road | renamed → Jump Start Smoothies: Current official Jump Start Highlands page identifies exact 1504 Bardstown address; distinct from initial Toast evidence.; Independent current exact-address delivery listing for replacement brand. | [source 1](https://jumpstartsmoothies.com/highlands-louisville/) · [source 2](https://www.ubereats.com/store/jump-start-smoothies-highlands/38OqaiCGQ2eiZELvA6WcVw) |
| w544701060 | Taco Bell | 1487 East 10th Street | closed: Courier Journal Aug 24, 2026 identifies 1487 E 10th as former Taco Bell leased to Holy Burger; opening anticipated within six months. | [source 1](https://www.aol.com/articles/york-burger-chain-holy-burger-175138000.html) |
| w338228210 | Texas Roadhouse | 3322 Outer Loop | closed: Independent November10 local report sets move from old Outer Loop; current official locator moved to3201 Brooke Elizabeth. Checked in web search on2026-11-18. | [source 1](https://www.bizjournals.com/louisville/news/2026/11/10/texas-roadhouse-outer-loop-opening-date.html) |
| n3516418240 | TGI Fridays | 415 South 4th Street | closed: June 2024 local report confirms last Louisville TGIF at Fourth Street Live closed permanently. | [source 1](https://www.wlky.com/article/louisville-tgi-fridays-closes-fourth-street-live/61426739) |
| n6044760425 | Wendy's | 2100 South Floyd Street | closed: Exact 2100 S Floyd location explicitly marked CLOSED; third-party listings with daily closed-now labels are not equivalent. | [source 1](https://www.restaurantji.com/ky/louisville/wendys-4/) |
| w336481842 | Wendy's | 2800 Packerland Way | closed: December 2024 local report includes Packerland in five permanent Louisville closures; stale Yellow Pages open-now labels conflict with dated news. | [source 1](https://www.wlky.com/article/wendys-closing-five-louisville-locations/63186415) |
| w336611957 | Wendy's | 9489 Westport Road | closed: Courier Journal reports 7 Brew replacing former Wendys at exact 9489 Westport address; official 7 Brew location also seen. | [source 1](https://www.yahoo.com/news/whats-replacing-former-wendys-westport-090053863.html) |
| w337118108 | Wendy's | 5101 Preston Highway | closed: Report gives nearby 5105 Preston rather than OSM 5101; consistent site, but address discrepancy retained. | [source 1](https://www.wlky.com/article/wendys-closing-five-louisville-locations/63186415) |
| w338215081 | Wendy's | 4259 Outer Loop | closed: December 2024 closure report includes exact Outer Loop address. | [source 1](https://www.wlky.com/article/wendys-closing-five-louisville-locations/63186415) |
| w329524174 | White Castle | 4020 Shelbyville Road | closed: December 2023 report identifies exact address and permanent Christmas closure. | [source 1](https://www.wlky.com/article/st-matthews-white-castle-closing-christmas-day/46147224) |
| w330411882 | Against the Grain Brewery and Public House | 1576 Bardstown Road | closed: 2024 closure report quotes brewery decision; Sept2024 WLKY confirms Pints&Union moving into former1576 Bardstown space. First-pass Dec2025 date was inaccurate. | [source 1](https://foodanddine.com/against-the-grains-public-house-bids-farewell-to-the-highlands/) |
| n6065590289 | Anoosh Bistro | 38.27864, -85.63671 (St. Matthews) | closed: Current replacement restaurant's own site confirms4864BrownsboroRoad; independent news traces Anoosh→Ata→HenHouse→Wasabi. | [source 1](https://www.wasabilouisville.com/) |
| n3383404395 | Another Place Sandwich Shop | 119 South 7th Street | closed: Independent listing marks Another Place Sandwich Shop permanently closed at 119 S Seventh, corroborating local 2021 closure reporting. Checked 2026-11-18. | [source 1](https://wanderlog.com/list/geoCategory/1562442/best-sandwiches-in-louisville) |
| n12699968777 | Äta | 4864 Brownsboro Road | closed: Current replacement Wasabi operates exact4864BrownsboroRoad, corroborating old Ata no longer operates. | [source 1](https://www.wasabilouisville.com/) |
| n3383407651 | Atlantic No. 5 | 605 West Main Street | closed: Independent May 2021 local report confirms Atlantic No 5 closed in Downtown Louisville. Checked 2026-11-18. | [source 1](https://www.bizjournals.com/louisville/news/2021/05/24/atlantic-no-5-closes-in-downtown-louisville.html) |
| n9336873203 | Barry's Cheese Steaks & More | 38.2348, -85.75661 (Old Louisville) | closed: August 2022 local report confirms Barry moved from 1161 South 2nd to 5408 Valley Station Road, well over 150 metres.; Independent WDRB report confirms departure from Second and Oak in Old Louisville. | [source 1](https://www.wave3.com/2022/08/30/barrys-cheesesteaks-more-moving-valley-station/) · [source 2](https://www.wdrb.com/news/business/barrys-cheesesteaks-relocating-to-valley-station/article_f7aa32b4-27dd-11ed-8c57-0365866063e4.html) |
| n3383404464 | Bearno's Pizza | 131 West Main Street | closed: Independent local food report says moved 350 yards from 131 W Main to Market, beyond 150 m limit. Checked in web search on2026-11-18. | [source 1](https://foodanddine.com/downtown-bearnos-moving/) |
| w331283045 | Bistro 301 | 301 West Market Street | closed: Independent specific 301 W Market listing explicitly says permanently closed. Checked 2026-11-18. | [source 1](https://wanderlog.com/place/details/1272044/bistro-301) |
| w331282522 | Bluegrass Brewing Company | 300 West Main Street | closed: 2026 local news reports Bluegrass Brewing Company 300 W Main closed, despite stale own menu/contact pages. | [source 1](https://www.wdrb.com/news/business/longtime-louisville-brewpub-closes-downtown-location/article_bd91c998-919f-4b07-b4e0-b79ff7bf9d22.html) |
| w333988955 | Bluegrass Brewing Company | 3929 Shelbyville Road | closed: Exact-address Bluegrass Brewing Co East St Matthews is marked closed; TwoBeerDudes separately says permanently closed at 3929 Shelbyville. | [source 1](https://www.beeradvocate.com/beer/profile/395/?view=ratings) |
| n3363783637 | Breadworks | 2204 Dundee Road | closed: September2022 report confirms bakery shutdown at DouglassLoop; 2024 Food&Dining says Dad'sCoffee replaced Breadworks2204Dundee. | [source 1](https://6amcity.com/ky/louisville/city/breadworks-closing-louisville) |
| n3516264327 | Bristol Bar and Grill | 614 West Main Street | closed: May 23, 2026 local report confirms final service May 24 at exact 614 W Main. | [source 1](https://foodanddine.com/bristol-bar-grill-will-close-downtown-after-service-on-may-24/) |
| n3368832060 | Bristol Bar & Grill | 1321 Bardstown Road | closed: February 2026 local report sets March 15 as final service at 1321 Bardstown Road.; May 2026 Courier Journal report confirms the Highlands location closed March 15. | [source 1](https://www.wlky.com/article/bristol-bar-grille-closing-highlands-location-louisville/70503198) · [source 2](https://www.aol.com/articles/tragic-bristol-bar-grille-close-201729000.html) |
| n3373722593 | Cafe 360 | 1582 Bardstown Road | closed: October 2024 report confirms Cafe 360 closure; later Hurry for Curry opened at same address, then itself closed in Nov 2026. | [source 1](https://www.wdrb.com/news/business/caf-360-on-bardstown-road-closes-its-doors/article_52fb2022-812f-11ef-943f-c3071f944131.html) |
| n6066622788 | City Cafe | 38.24652, -85.76029 (Downtown) | closed: Independent local dining report confirms Downtown City Café closed after 25 years, corroborating West Broadway closure report. Checked 2026-11-18. | [source 1](https://foodanddine.com/downtown-louisville-lunchtime-favorite-city-cafe-has-closed-after-25-years-in-business/) |
| n5268994595 | Comfy Cow | 38.22084, -85.76252 (Old Louisville) | closed: Exact 339 W Cardinal location explicitly marked CLOSED. | [source 1](https://www.restaurantji.com/ky/louisville/the-comfy-cow-5/) |
| n3445798127 | Corner Cafe | 9307 New La Grange Road | renamed → Basilico Cafe: Corner Café closed in April 2026; local follow-up confirms Basilico Café now operates at 9307 New La Grange. Checked 2026-11-18.; Corner Café closed in April 2026; local follow-up confirms Basilico Café now operates at 9307 New La Grange. Checked 2026-11-18.; Current Basilico Cafe website confirms service at 9307 New La Grange, independently corroborating the replacement of Corner Cafe. Checked 2026-11-18. | [source 1](https://foodanddine.com/basilico-cafe-is-up-and-running-where-corner-cafe-used-to-be-in-lyndon/) · [source 2](https://foodanddine.com/corner-cafe-in-lyndon-announces-a-late-april-closing/) · [source 3](https://basilicolouisville.com/) |
| w332419974 | Cunninghams Creek Side | 6301 River Road | duplicate_or_not_a_restaurant: Official restaurant at6301RiverRd matches both near-identical OSM entries; computed separation~1m, retain n7629878785. | [source 1](https://www.cunninghamscreekside.com/) |
| n6065590593 | Decca | 38.25289, -85.73746 (NuLu & Butchertown) | closed: Former chef's own biography confirms Decca closed2022; WLKY reports replacement LouLou at812EMarket. | [source 1](https://decaderestaurant.com/about/) |
| n6065597387 | Dish on Market | 434 West Market Street | closed: Independent local coverage confirms Dish on Market permanently shut in July 2020 at this downtown site. Checked 2026-11-18. | [source 1](https://www.wlky.com/article/another-downtown-closure-dish-on-market-permanently-shuts-down-due-to-2020-challenges/33474117) |
| n3383405090 | Down One Bourbon Bar & Restaurant | 321 West Main Street | closed: Courier Journal October 2026 closure report specifically identifies 321 W Main, corroborating own site's permanent-closure notice. Checked 2026-11-18. | [source 1](https://www.aol.com/articles/down-one-bourbon-bar-shuts-204402000.html) |
| n3363783654 | Dundee Tavern | 2224 Dundee Road | renamed → Derby City Pizza (subsequently announced as Parlour Pizza + Pints): Dundee transitioned to Derby City Pizza in 2024. September 2026 report announces a further Parlour replacement; old Dundee identity definitively obsolete. | [source 1](https://foodanddine.com/a-concept-swap-dundee-tavern-to-close-then-reopen-as-derby-city-pizza/) |
| n6069723085 | El Nopal | 38.28904, -85.50981 (Middletown & Anchorage) | closed: Exact 12418 La Grange #120 location explicitly marked CLOSED; Uber Eats unavailable since Oct 2025. | [source 1](https://www.restaurantji.com/ky/louisville/el-nopal-/) |
| n8953247262 | Fix Coffeehouse and Bakery | 10616 Meeting Street | renamed → Barry Bagels: Official current location list has BarryBagels NortonCommons10616MeetingStreet; intervening CafeCommons and Drick's names are stale. | [source 1](https://barrybagels.com/locations/) |
| n6391859999 | Gasthaus German Restaurant | 38.27774, -85.6368 (St. Matthews) | closed: Independent May2022 retirement/closure news corroborates own permanent-closure announcement. | [source 1](https://www.wdrb.com/news/business/gasthaus-german-restaurant-owners-retire-after-more-than-28-years-in-louisville/article_052581ec-d06c-11ec-9c55-274f167b6f0f.html) |
| n6800764286 | Goodwood | 38.25465, -85.74002 (NuLu & Butchertown) | closed: Independent April2026 report confirms NuLu and WhiskeyRow locations closed March30; later bankruptcy reporting corroborates. | [source 1](https://amp.kentucky.com/news/business/article315247053.html) |
| n6800616486 | Griff's | 38.25282, -85.75364 (Downtown) | renamed → Parlour: Current official Parlour locator shows operation at 133 W Liberty. The old Griff's identity is obsolete; retain removal of old name but classify as renamed/replaced by Parlour. Checked 2026-11-18. | [source 1](https://eatparlour.com/contact/) |
| w337501563 | Guaca Mole | 9921 Ormsby Station Road | closed: Independent Eater venue page explicitly marks9921OrmsbyStation permanently closed, agreeing own-site move. Checked in web search on2026-11-18. | [source 1](https://louisville.eater.com/venue/1460/guaca-mole) |
| n6065590594 | Harvest | 624 East Market Street | closed: Independent Sept2020 report identifies624EMarket and announced final service that week. | [source 1](https://spectrumnews1.com/news/2020/09/10/harvest-restaurant-closing) |
| n4792216814 | HI-Five Doughnuts | 1011 East Main Street | closed: Local report documents HiFive leaving MainStreet for HarvardDrive; former mapped location is no longer operating even though old website remains. | [source 1](https://foodanddine.com/sweets-bricks-n-mortar-swap-from-doughnuts-to-cheesecake-scones-to-be-named-later/) |
| n6066549688 | Hill Street Fish Fry | 38.22547, -85.75571 (Old Louisville) | closed: 2023 retrospective explicitly identifies Hill Street Fish Fry among closed restaurants; stale delivery menu is not reopening evidence. | [source 1](https://www.yahoo.com/entertainment/long-farewell-look-back-10-100620590.html) |
| n3505153162 | Hometown Pizza | 12607 Taylorsville Road | renamed → Craft House Pizza: Own current Craft House locations and specific listing identify Craft House Pizza at former Hometown address 12607 Taylorsville Suite 102. Checked 2026-11-18.; Own current Craft House locations and specific listing identify Craft House Pizza at former Hometown address 12607 Taylorsville Suite 102. Checked 2026-11-18. | [source 1](https://crafthousepizza.com/) · [source 2](https://www.restaurantji.com/ky/louisville/hometown-pizza-/) |
| n4039209453 | Hometown Pizza | 38.19339, -85.7285 (Audubon & Airport) | renamed → Craft House Pizza: Current brand site lists Craft House Pizza at 4041 Preston with hours and phone; first-pass historical same-address Hometown identity supports rename. | [source 1](https://crafthousepizza.com/) |
| n6629335485 | Hooked on Frankfort | 3200 Frankfort Avenue | closed: Independent exact-location Tripadvisor listing explicitly labels Hooked on Frankfort CLOSED at 3200 Frankfort. Checked 2026-11-18. | [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d17470528-Reviews-Hooked_on_Frankfort-Louisville_Kentucky.html) |
| n3363770013 | I Love Pollo | 243 Blankenbaker Parkway | renamed → Tacos D'Amor: Own current Tacos D Amor site lists 243 Blankenbaker Parkway, the mapped former I Love Pollo address.; Independent delivery listing identifies Tacos D Amor at the exact same address. | [source 1](https://tacosdamorus.com/) · [source 2](https://guava.failover.uber.com/store/tacos-d-amor-blankenbaker/vO8is2eMXTaa6QTU2-jz4g) |
| n3373719479 | I ♥ Tacos | 1534 Bardstown Road | closed: Mapped I Love Tacos at 1534 Bardstown was succeeded by Tacos D'Amor; subsequent local reports confirm that restaurant closed. Checked 2026-11-18.; Mapped I Love Tacos at 1534 Bardstown was succeeded by Tacos D'Amor; subsequent local reports confirm that restaurant closed. Checked 2026-11-18. | [source 1](https://www.wdrb.com/news/business/tacos-d-amor-closes-location-in-louisvilles-highlands-neighborhood-amid-declining-traffic/article_6335527d-bb7a-4aca-9735-43efb14d4a87.html) · [source 2](https://foodanddine.com/tacos-d-amor-more-closes-its-deer-park-location/) |
| n4755754362 | Impellizzeri's Pizza | 110 West Main Street | closed: Independent local reporting confirms 110 W Main Impellizzeri's closed permanently rather than remaining temporarily shut. Checked 2026-11-18. | [source 1](https://www.wlky.com/article/impellizzeris-closes-restaurant-in-downtown-louisville/35085927) |
| n6800764287 | International Tap House | 38.25497, -85.74003 (NuLu & Butchertown) | closed: Independent directory explicitly marks International Tap House637EMain permanently closed. | [source 1](https://wanderlog.com/list/geoCategory/12561/best-louisville-breweries-and-craft-beer) |
| n3383404391 | Jimmy Can't Dance | 119 South 7th Street | closed: Independent exact old-address listing marks Jimmy Can't Dance at 119 S Seventh permanently closed; current business is at a different NuLu address. Checked 2026-11-18. | [source 1](https://www.tripadvisor.com/Attraction_Review-g39604-d12910173-Reviews-Jimmy_Can_t_Dance-Louisville_Kentucky.html) |
| n6069185522 | Joy Luck | 38.3125, -85.56896 (Prospect & Northeast) | closed: Independent local report confirms closure of9850VonAllmenCourt branch. | [source 1](https://foodanddine.com/joy-luck-closes-its-east-end-location/) |
| w339254271 | Kathy & Joe's Restaurant | 5408 Valley Station Road | closed: August 2022 local report identifies Barry Cheesesteaks moving into exact 5408 Valley Station Road, replacing the old Kathy and Joe identity. Closure date of Kathy and Joe itself is not established.; November 2025 local report confirms the later Barry restaurant closure in Valley Station. This supports obsolete map identity, with medium confidence. | [source 1](https://www.wave3.com/2022/08/30/barrys-cheesesteaks-more-moving-valley-station/) · [source 2](https://www.wlky.com/article/barrys-cheesesteaks-closing-restaurant-valley-station/69499456) |
| n13953100730 | koko+rAe | 38.23184, -85.70862 (Highlands) | renamed → Mom's Kitchen: October 18, 2024 local article identifies new owners and Moms Kitchen replacing Koko + Rae at exact 1511 Bardstown. | [source 1](https://foodanddine.com/moms-kitchen-indian-replaces-and-retains-koko-rae-caribbean/) |
| n6065590591 | La Chasse | 38.23403, -85.71269 (Highlands) | closed: Independent local reports confirm La Chasse's July 2025 closure at the mapped Highlands site. Checked 2026-11-18.; Independent local reports confirm La Chasse's July 2025 closure at the mapped Highlands site. Checked 2026-11-18. | [source 1](https://www.wdrb.com/news/business/la-chasse-restaurant-on-bardstown-road-in-the-highlands-closes-abruptly/article_f504e8a6-8465-46cd-a30e-b76697d8a6de.html) · [source 2](https://www.bizjournals.com/louisville/news/2025/07/28/la-chasse-closes-abruptly-in-the-highlands.html) |
| n6066622790 | La Peche Gourmet To Go and Cafe | 38.23758, -85.71913 (Highlands) | closed: La Peche Gourmet at 1147 Bardstown is explicitly permanently closed; 2020 report of Kathy Cary's retirement corroborates closure of this Lilly's/La Peche operation. Checked 2026-11-18.; La Peche Gourmet at 1147 Bardstown is explicitly permanently closed; 2020 report of Kathy Cary's retirement corroborates closure of this Lilly's/La Peche operation. Checked 2026-11-18. | [source 1](https://wanderlog.com/place/details/1272034/la-peche-gourmet) · [source 2](https://foodanddine.com/legendary-chef-and-restaurateur-kathy-cary-has-announced-her-retirement/) |
| n3368831496 | Lilly's | 1147 Bardstown Road | closed: 2020 local closure report and explicit permanent-closure listing match Lilly's at 1147 Bardstown. Checked 2026-11-18.; 2020 local closure report and explicit permanent-closure listing match Lilly's at 1147 Bardstown. Checked 2026-11-18. | [source 1](https://www.wdrb.com/news/business/lillys-bistro-owner-to-retire-close-iconic-highlands-restaurant/article_68bbf974-a6a3-11ea-aa70-9b2baa70f515.html) · [source 2](https://louisville.eater.com/venue/1155/lillys-bistro) |
| n3363783653 | Loop22 | 2222 Dundee Road | closed: Independent address-matched listing at2222Dundee gives permanently-closed status for every weekday; first-pass closure agrees. Checked in web search on2026-11-18. | [source 1](https://wanderlog.com/de/place/details/12014110/loop-22) |
| n4755776092 | Los Aztecas | 530 West Main Street | closed: Restaurant history explicitly says 530 W Main moved to 445 E Market in 2019, well over 150m. | [source 1](https://www.losaztecasnulu.com/louisville-los-aztecas-mexican-restaurant-about) |
| n4792241551 | Louis's The Ton | 1601 Story Avenue | closed: GoldBar successor at1601Story closed2022; later BackDeck planned for former space, so old Louis'sTheTon no longer operates. | [source 1](https://www.wdrb.com/news/business/gold-bar-on-story-avenue-in-butchertown-closing/article_b43a9c5e-1cf1-11ed-88c2-a3e4218f645b.html) |
| n3373722596 | LouVino | 1606 Bardstown Road | closed: Independent Courier Journal report confirms immediate closure of1606Bardstown inSeptember2024. Checked in web search on2026-11-18. | [source 1](https://www.yahoo.com/news/10-years-louvino-close-louisville-213934772.html) |
| n9915806511 | Lucky Cat Café and Lounge | 2230 Dundee Road | closed: Two local reports confirm Lucky Cat Café at 2230 Dundee closed at the end of April 2025. Checked 2026-11-18.; Two local reports confirm Lucky Cat Café at 2230 Dundee closed at the end of April 2025. Checked 2026-11-18. | [source 1](https://www.wlky.com/article/lucky-cat-cafe-louisville-closing/64578577) · [source 2](https://www.wdrb.com/news/business/nonprofit-cat-caf-in-louisvilles-belknap-neighborhood-to-close-at-the-end-of-april/article_6c22c283-0849-44a2-bb99-cd55c4fa00e0.html) |
| n6069217507 | Magnolia & Fig | 38.24506, -85.51973 (Middletown & Anchorage) | duplicate_or_not_a_restaurant: Own contact page identifies women's clothing boutique; current own site at2910Frankfort, not an eating/drinking venue. | [source 1](https://magnoliaandfigboutique.com/pages/contact-us) |
| w337711887 | Mango's | 6201 Dutchmans Lane | closed: Independent August2021 report identifies closure at6201DutchmansLane after lease issue. | [source 1](https://www.wlky.com/article/popular-mexican-restaurant-closes-st-matthews-location/37397830) |
| w330411872 | Mark's Feed Store | 1514 Bardstown Road | closed: July 18, 2025 report sets final service August 24 at exact 1514 Bardstown. Official Toast closure notice also seen. | [source 1](https://foodanddine.com/marks-feed-stores-location-in-deer-park-to-close-aug-24/) |
| w683231820 | Milkwood Restaurant | 316 West Main Street | closed: 2020 local report states Milkwood at 316 W Main closed as commercial restaurant and became McAtee Community Kitchen; stronger than expired domain evidence. | [source 1](https://foodanddine.com/welcome-to-comings-goings-a-weekly-snapshot-of-the-food-and-dining-scene/) |
| n3364017717 | Molly Malone's | 3900 Shelbyville Road | closed: Independent May2024 report traces MollyMalone's→Raven at3900Shelbyville and finaldayMay31; replacementLimonYSal news corroborates. | [source 1](https://foodanddine.com/quoth-the-raven-in-st-matthews-nevermore-and-its-last-day-is-may-31/) |
| n3187693661 | New Wave Burritos | 3311 Preston Highway | closed: Independent local food writer reports owners' closure announcement at 3311 Preston. Checked 2026-11-18. | [source 1](https://www.kevingibsonwriter.com/blog/new-wave-burritos-owners-announce-immenent-closure) |
| n13233668040 | Nook and Nowhere | 1149 South Shelby Street | closed: May18 2026 report quotes ending service May31 2026 at S Shelby; independently corroborated by Shelf Awareness. | [source 1](https://www.aol.com/articles/nook-nowhere-popular-bookstore-cafe-163551000.html) |
| n3375256894 | North End Cafe | 2116 Bardstown Road | closed: Exact 2116 Bardstown location closed on platform; 2019 WLKY closure roundup independently identifies address. | [source 1](https://www.ubereats.com/store/north-end-cafe/rUHsORlAQcuu3LZfEmBMDw) |
| n3375256895 | North End Slice | 2118 Bardstown Road | closed: Local reporting confirms North End Café and adjoining North End Slice closed in 2019; input 2118 is adjoining 2116 premises. Checked 2026-11-18.; Local reporting confirms North End Café and adjoining North End Slice closed in 2019; input 2118 is adjoining 2116 premises. Checked 2026-11-18. | [source 1](https://www.wlky.com/article/here-are-the-restaurants-that-closed-in-louisville-in-2019/30286240) · [source 2](https://firststargroup.net/why-this-prominent-highlands-cafe-is-closing/) |
| w337283901 | Old Louisville Coffee Co-op | 316 West Ormsby Avenue | closed: Independent retrospective explicitly dates permanent closure March22 2026; March Food&Dining finalday report agrees. | [source 1](https://queerkentucky.com/a-queer-kentucky-safe-space-old-louisville-coffee-co-op/) |
| n6066456090 | Ostra | 38.25661, -85.71709 (Crescent Hill & Clifton) | closed: Correction to chronology: Ostra reopened after its reported 2020 closure; January 2022 local follow-up reports its subsequent end. Current exact-address Restaurantji and Wanderlog also say closed. Do not cite May 2020 as final closure date. Checked 2026-11-18. | [source 1](https://foodanddine.com/poetically-lyrically-and-commercially-it-appears-to-be-ostras-end/) |
| n9915810825 | Panchito's Ice Cream & Taqueria | 2245 Bardstown Road | closed: Independent closure reports match Panchitos at 2245 Bardstown; other Panchitos locations are separate. Checked 2026-11-18.; Independent closure reports match Panchitos at 2245 Bardstown; other Panchitos locations are separate. Checked 2026-11-18. | [source 1](https://foodanddine.com/the-highlands-location-of-panchitos-ice-cream-taqueria-to-close-oct-29/) · [source 2](https://www.yahoo.com/entertainment/panchitos-ice-cream-taqueria-close-145148684.html) |
| n2496186549 | Pastry Plus | 38.14286, -85.62285 (Highview & Fern Creek) | closed: Local January 2021 closure report and explicit permanently-closed listing match Pastry Plus at 7407 Fegenbush near mapped point. Checked 2026-11-18.; Local January 2021 closure report and explicit permanently-closed listing match Pastry Plus at 7407 Fegenbush near mapped point. Checked 2026-11-18. | [source 1](https://foodanddine.com/closings-pastry-plus-and-flora-kitchenette-have-departed-the-scene/) · [source 2](https://wanderlog.com/place/details/1535997/pastry-plus) |
| n5795892554 | Please & Thank You on the Avenue | 2341 Frankfort Avenue | closed: October 20, 2026 local report says exact 2341 Frankfort shop closed Oct 19; avoids contradictory automated Hoodline story. | [source 1](https://www.bizjournals.com/louisville/news/2026/10/20/please-thank-you-closes-frankfort-avenue-store.html) |
| n6069217385 | Queue Cafe | 38.25611, -85.7545 (Downtown) | closed: Rechecked exact 220 W Main Suite 160 listing explicitly labeled CLOSED. No independent second closure source established; other surviving directories lack current operation evidence. Keep medium confidence and expose this limitation. Checked 2026-11-18. | [source 1](https://www.restaurantji.com/ky/louisville/queue-cafe-/) |
| n3375209377 | Rawnaissance Raw Organic Desserts | 1759 Bardstown Road | closed: Two independent specific listings explicitly mark Rawnaissance at 1759 Bardstown permanently closed. Checked 2026-11-18.; Two independent specific listings explicitly mark Rawnaissance at 1759 Bardstown permanently closed. Checked 2026-11-18. | [source 1](https://www.happycow.net/reviews/rawnaissance-louisville-114527) · [source 2](https://wanderlog.com/place/details/1488603/rawnaissance-desserts) |
| n490481592 | Rich O's Public House | 38.32791, -85.8171 (New Albany, IN) | renamed → New Albanian Brewing Company Pizzeria & Public House: Brand history explicitly combines Rich Os and Sportstime into NABC Pizzeria and Public House at 3312 Plaza Drive.; Current own site operates the combined business at 3312 Plaza Drive with weekly hours.; Independent county inspection records New Albanian Brewing at exact 3312 Plaza Drive, corroborating the consolidated current identity. | [source 1](https://newalbanian.com/history/) · [source 2](https://newalbanian.com/) · [source 3](https://www.in.gov/counties/floyd/health-department/files/food-inspections/retail-food-inspections/2024/The-New-Albanian-04-10-24.PDF) |
| n6065590288 | Rivue Restaurant & Lounge | 38.2577, -85.75586 (Downtown) | renamed → Swizzle Dinner & Drinks: Hotel operator explicitly states Swizzle replaces RIVUE, which closed June 2019; same Galt House restaurant. | [source 1](https://ajshotels.com/restaurant-concept-louisville/) |
| n3467847353 | Roux | 38.23505, -85.7143 (Highlands) | closed: Specific Roux listing says permanently closed; 2016 Louisville Public Media report also lists Roux among closed restaurants. Checked 2026-11-18.; Specific Roux listing says permanently closed; 2016 Louisville Public Media report also lists Roux among closed restaurants. Checked 2026-11-18. | [source 1](https://wanderlog.com/place/details/5218506/roux) · [source 2](https://www.lpm.org/news/2016-10-19/for-louisville-chefs-its-about-the-regulars-not-bursting-bubbles) |
| n3375499199 | Rye | 900 East Market Street | closed: Independent July2020 report confirms permanent shutdown of Rye on Market. | [source 1](https://www.wlky.com/article/nulu-restaurant-rye-on-market-shutting-down-for-good-thank-you-louisville-for-embracing-us/33396391) |
| n3363737045 | Scarlet's Bakery | 741 East Oak Street | closed: Current replacement Perso confirms 741 East Oak Street, exact former Scarlet's address. | [source 1](https://www.persorestaurant.com/contact) |
| n3363783640 | Sinclair Smoked Salmon | 2208 Dundee Road | closed: Courier Journal closure report matches Sinclair Smoked Salmon at 2208 Dundee; specific menu listing also says closed. Checked 2026-11-18.; Courier Journal closure report matches Sinclair Smoked Salmon at 2208 Dundee; specific menu listing also says closed. Checked 2026-11-18. | [source 1](https://www.yahoo.com/lifestyle/smoked-salmon-shop-douglass-loop-185332830.html) · [source 2](https://www.menupix.com/louisville/restaurants/31990377/Sinclair-Smoked-Salmon-Louisville-KY) |
| n3368830981 | Somewhere Louisville | 1135 Bardstown Road | closed: Independent local reports confirm Somewhere at 1135 Bardstown closed after eviction in 2024. Checked 2026-11-18.; Independent local reports confirm Somewhere at 1135 Bardstown closed after eviction in 2024. Checked 2026-11-18. | [source 1](https://www.wlky.com/article/nowhere-somewhere-bar-bardstown-road-evicted/61456113) · [source 2](https://www.yahoo.com/news/two-neighboring-bars-bardstown-road-210348225.html) |
| w337191422 | Spinelli's Pizzeria | 4001 Shelbyville Road | closed: February 2025 Courier Journal reports closure at 4001 Shelbyville Road; later current exact-address listing marks it CLOSED.; Independent Restaurantji listing marks exact 4001 Shelbyville CLOSED. A stale delivery listing mixes the Baxter name with the old address. | [source 1](https://www.yahoo.com/news/spinellis-pizza-location-st-matthews-173240360.html) · [source 2](https://www.restaurantji.com/ky/louisville/spinellis-pizzeria-/) |
| n490481591 | Sportstime Pizza | 38.32816, -85.81718 (New Albany, IN) | renamed → New Albanian Brewing Company Pizzeria & Public House: Brand history combines the former Sportstime and Rich Os identities into NABC Pizzeria and Public House.; Independent county inspection records New Albanian Brewing at 3312 Plaza Drive. | [source 1](https://newalbanian.com/history/) · [source 2](https://www.in.gov/counties/floyd/health-department/files/food-inspections/retail-food-inspections/2024/The-New-Albanian-04-10-24.PDF) |
| n6392757787 | Thai Cafe | 38.2829, -85.63138 (Lyndon & Westport) | closed: Two specific listings explicitly mark Thai Café at 2226 Holiday Manor Center permanently closed, corresponding to mapped point. Checked 2026-11-18.; Two specific listings explicitly mark Thai Café at 2226 Holiday Manor Center permanently closed, corresponding to mapped point. Checked 2026-11-18. | [source 1](https://restaurantguru.com/Thai-Cafe-Louisville) · [source 2](https://wanderlog.com/place/details/2646836/thai-cafe) |
| n3357102175 | The Bard's Town | 1801 Bardstown Road | closed: Independent reports confirm The Bard's Town left 1801 Bardstown at the end of 2022; subsequent activity elsewhere does not keep old point open. Checked 2026-11-18.; Independent reports confirm The Bard's Town left 1801 Bardstown at the end of 2022; subsequent activity elsewhere does not keep old point open. Checked 2026-11-18. | [source 1](https://www.wlky.com/article/the-bards-town-moving-highlands-shelby-park-louisville-bar/42561641) · [source 2](https://leoweekly.com/arts/after-the-bards-town-the-life-and-work-of-doug-schutte-15756882/) |
| n6800764196 | The Celtic Pig | 38.25596, -85.7488 (Downtown) | closed: March 2022 local report identifies 217 East Main as the former Celtic Pig, replaced by Dasha Barbours.; Independent LEO story identifies Dasha Barbours in the former Celtic Pig space. | [source 1](https://www.wlky.com/article/southern-style-restaurant-relocating-downtown-louisville/39494448) · [source 2](https://leoweekly.com/food-drink/see-inside-dasha-barbours-expanded-southern-restaurant-in-downtown-louisville-15744713/) |
| n3364201077 | The Champagnery at Architype Gallery | 1764 Frankfort Avenue | closed: 2025 closure report for exact 1764 Frankfort; 2024 reopening predates this later closure. | [source 1](https://www.wdrb.com/news/business/champagne-bar-on-frankfort-avenue-in-louisville-closing-its-doors/article_4b4e45d4-02b7-4920-9962-810890e5ae4e.html) |
| n3410660500 | The Cheddar Box | 3909 Chenoweth Square | closed: Independent March2024 report places replacement ElderberryProvisions at3909ChenowethSquare after CheddarBox closure; otherCheddarBox concepts separate. | [source 1](https://foodanddine.com/elderberry-provisions-in-st-matthews-picking-up-where-cheddar-box-left-off/) |
| n5692585423 | The HUB | 38.25364, -85.70467 (Crescent Hill & Clifton) | closed: Hub relocated from 2235 Frankfort to 1133 Bardstown December 2024, well over 150m; closed at old map point. | [source 1](https://www.bizjournals.com/louisville/news/2024/12/05/the-hub-moving-to-bardstown-road-space.html) |
| w329933368 | The Joy Luck | 1285 Bardstown Road | closed: Local reporting confirms Joy Luck at 1285 Bardstown closed and Derby Dogs subsequently occupied the address. Checked 2026-11-18.; Local reporting confirms Joy Luck at 1285 Bardstown closed and Derby Dogs subsequently occupied the address. Checked 2026-11-18. | [source 1](https://www.wdrb.com/news/business/derby-dogs-opens-replaces-joy-luck-in-louisvilles-highlands/article_df0a5849-60f6-422e-a3b9-60ba23f44752.html) · [source 2](https://www.yahoo.com/news/popular-asian-restaurant-highlands-closes-174233789.html) |
| n3363783649 | The Silly Axe Cafe | 2216 Dundee Road | closed: Silly Axe left 2216 Dundee for Logan Street Market in 2022, well beyond 150 m; later report confirms Logan operation also closed. Checked 2026-11-18.; Silly Axe left 2216 Dundee for Logan Street Market in 2022, well beyond 150 m; later report confirms Logan operation also closed. Checked 2026-11-18. | [source 1](https://foodanddine.com/silly-axe-cafe-is-on-the-move-to-logan-street-market/) · [source 2](https://www.yahoo.com/lifestyle/gluten-free-cafe-closes-inside-184947411.html) |
| n13248773204 | The Silver Dollar | 1761 Frankfort Avenue | closed: Report states The Silver Dollar 1761 Frankfort Ave last service November15 2025; Business First corroborates closure announcement. | [source 1](https://www.kentucky.com/lexgoeat/bourbon/article312872498.html) |
| n3383406999 | The Thirsty Pedaler | 411, Suite 170 South 4th Street | duplicate_or_not_a_restaurant: Tourism bureau describes original Thirsty Pedaler contact as pedal-bike tours visiting 2–3 bars, not fixed restaurant. | [source 1](https://www.gotolouisville.com/directory/pedal-pub-louisville/) |
| n6800735287 | Toast on Market | 38.25331, -85.74105 (NuLu & Butchertown) | closed: Independent April2022 report distinguishes closed Louisville location from reopened NewAlbany branch; later replacement at620EMarket corroborates. | [source 1](https://leoweekly.com/food-drink/toast-on-market-to-close-louisville-location-reopen-new-albany-location-15772466/) |
| n5716196283 | Topp't | 379 Professional Court | closed: Independent January 2023 local report confirms Topp't concludes its run at the New Albany location, corroborating the specific CLOSED listing. Checked 2026-11-18. | [source 1](https://foodanddine.com/today-toppt-handcrafted-pizzas-chopped-salads-concludes-its-run-in-new-albany/) |
| n3390029668 | Verbena Cafe | 10639 Meeting Street | closed: Independent search locates exact10639MeetingStreet permanent closure report; no reliable reopening evidence found. | [source 1](https://www.wlky.com/article/verbena-cafe-in-norton-commons-closes-permanently-due-to-coronavirus/32440641) |
| w333995688 | Vinaigrette Salad Kitchen | 3012 Bardstown Road | closed: September 2026 report confirms last Louisville store at 3012 Bardstown closed Sept 2; earlier 2025 open report superseded. | [source 1](https://www.wdrbwave.com/2026/09/11/vinaigrette-salad-kitchen-closes-last-louisville-location-it-exits-market/?outputType=amp) |
| n3368937219 | Ward 426 | 426 Baxter Avenue | closed: Independent exact-brand OpenTable reviews explicitly report CLOSED; Food&Dining permanent-closure article also independently located. | [source 1](https://www.opentable.com/r/ward-426) |
| n6066623489 | Waycool Cafe | 38.24546, -85.75447 (Downtown) | renamed → Cardinal Crossing Cafe: Hotel's own page describes Cardinal Crossing Cafe as WAYCOOL social enterprise at Hotel Louisville. | [source 1](https://www.hotellouisville.org/cafe) |
| n3410660534 | Waylon's Feed and Firewater | 3939 Shelbyville Road | closed: Independent2019 report identifies formerWaylon's space3939Shelbyville as incomingHavanaRumba. | [source 1](https://foodanddine.com/exclusive-havana-rumba-moving-into-former-waylons-feed-firewater-space/) |
| n3383407007 | Whiskey Dry | 412 South 4th Street | closed: Exact 412 S 4th location marked permanently closed; corroborates first-pass local report. | [source 1](https://wanderlog.com/place/details/1234157/whiskey-dry) |
| n2497238182 | Willow Lake Tavern | 38.27002, -85.55256 (Middletown & Anchorage) | duplicate_or_not_a_restaurant: Own contact page names Selena's at Willow Lake Tavern10609LaGrange. Worklist two names are13m apart; retain Selena's node, suppress duplicate. | [source 1](https://www.selenasrestaurant.com/contact) |
| n6066410786 | Wiltshire at the Speed | 38.21821, -85.76119 (Old Louisville) | closed: Museum's current visit page identifies successor Est1927byMarigold now closed May10 2026; confirms old Wiltshire operator no longer current. | [source 1](https://www.speedmuseum.org/visit/) |
| n3375496674 | Wiltshire on Market | 636 East Market Street | closed: Independent July2023 report confirms closure/succession at636EMarket. | [source 1](https://foodanddine.com/wiltshire-on-market-calls-it-a-day-but-the-baton-is-being-passed/) |
| w339279901 | W.W. Cousins | 4913 Dixie Highway | closed: Independent July7 2023 report confirms permanent closure of W.W.Cousins Dixie branch. | [source 1](https://www.wdrbwave.com/2023/07/07/w-w-cousins-closes-dixie-highway-location/) |
| n3383404332 | Yaching's East West Cuisine | 105 South 4th Street | closed: 2019 local closure roundup identifies Yachings at 105 South 4th Street.; Historical directory independently matches the old business to 105 South 4th. Its daily Closed label alone is not permanent-closure evidence. | [source 1](https://www.wlky.com/article/here-are-the-restaurants-that-closed-in-louisville-in-2019/30286240) · [source 2](https://www.yellowbot.com/yachings-louisville-ky.html) |
| n6069862345 | Yang-Kee Noodle | 38.24768, -85.6099 (Lyndon & Westport) | closed: 2019 local closure roundup identifies Yang Kee at 7900 Shelbyville (Oxmoor), matching point; distinct from initial WDRB evidence. | [source 1](https://www.wlky.com/article/here-are-the-restaurants-that-closed-in-louisville-in-2019/30286240) |
| n6069300185 | Zeggz | 38.31071, -85.56701 (Prospect & Northeast) | closed: Courier Journal reports original 4600 Chamberlain location closed in 2017; mapped coordinate matches Chamberlain and independent Wanderlog marks permanent closure.; Exact 4600 Chamberlain location permanently closed. | [source 1](https://www.aol.com/news/zeegz-middletown-closes-plans-smaller-172415065.html) · [source 2](https://wanderlog.com/place/details/3285927/zeggz-amazing-eggs-chamberlain) |
| n6066623490 | Zeggz Amazing Eggs | 38.28642, -85.62919 (Lyndon & Westport) | closed: Dated April 3, 2019 brand press release confirms Lime Kiln closed April 1, 2019 for Mi Tierra expansion; distinct document from initial contact page. | [source 1](https://zeggzeggz.com/wp-content/uploads/2019/04/ZEGGZ-Lime-Kiln-Closing.pdf) |
| n3443828792 | Z's Oyster Bar & Steakhouse | 101 Whittington Parkway | closed: Independent local reports confirm Z's closed at 101 Whittington; later Del Frisco's occupancy corroborates. Checked 2026-11-18.; Independent local reports confirm Z's closed at 101 Whittington; later Del Frisco's occupancy corroborates. Checked 2026-11-18. | [source 1](https://foodanddine.com/shucks-zs-oyster-bar-steakhouse-is-shuttered/) · [source 2](https://www.wlky.com/article/zs-oyster-bar-and-steakhouse-unexpectedly-closes-after-20-years-in-business/30878723) |

## Still unsure

These remain visible with an operating-status flag. Empty evidence means a search did not establish a reliable matching source; it is not closure evidence.

| OSM ID | Name | Mapped address / point | Limitation / evidence |
|---|---|---|---|
| w329550775 | Arby's | 12929 Shelbyville Road | Old 12933 Shelbyville listing persists; OSM says 12929. No independent explicit closure at exact spot found; sitemap absence alone insufficient. [source 1](https://www.yellowpages.com/louisville-ky/arbys) |
| w337128164 | Arby's | 9905 La Grange Road | Historic exact 9905 Lagrange listing found, without reliable current operation/closure evidence. [source 1](https://www.ibegin.com/directory/us/kentucky/louisville/category/restaurants-fast-food/) |
| n6069862356 | Auntie Anne's | 38.24688, -85.61066 (Lyndon & Westport) | Official locator lists Oxmoor7900Shelbyville but exact mall-kiosk point not independently matched. Checked in web search on2026-11-18. [source 1](https://locations.auntieannes.com/ky/louisville) |
| n3436530756 | Baskin-Robbins | 9413 Westport Road | Address-matched listing has hours but official locator omitsWestport; current status unresolved. Checked in web search on2026-11-18. [source 1](https://maps.roadtrippers.com/us/louisville-ky/food-drink/baskin-robbins-louisville-ky--2) |
| w1225723020 | Bob Evans | 1101 East Lewis and Clark Parkway | Independent review listing matches address, but no current hours/post date available; previous Waze hours alone not conclusive. Checked in web search on2026-11-18. [source 1](https://www.tripadvisor.ca/Restaurant_Review-g37012-d881862-Reviews-Bob_Evans-Clarksville_Indiana.html) |
| n3464533100 | Buffalo Wild Wings | 38.15099, -85.83617 (Valley Station & PRP) | Search returns permanently closed Louisville Buffalo Wild Wings listing but exact street not established; old Dixie address listings do not prove status at this coordinate. [source 1](https://restaurantguru.com/Buffalo-Wild-Wings-Louisville) |
| n6069862327 | California Pizza Kitchen | 38.24763, -85.61046 (Lyndon & Westport) | Only generic directory listings at7900Shelbyville, no current menu/hours established. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/lyndon-ky/bars) |
| w329550776 | Captain D's | 12933 Shelbyville Road | Listing title explicitly says Closed For Remodel at 12929 Shelbyville. Restaurantji says CLOSED but permanence is unresolved; OSM address is 12933. Earlier grouped Yellow Pages permanent-closure label belonged to a different store at 3801 Oaklawn and is rejected. Checked 2026-11-18. [source 1](https://www.waze.com/live-map/directions/%28closed-for-remodel%29captain-ds-shelbyville-rd-12929-middletown?to=place.w.179896702.1798901488.1133210) |
| n13384463445 | Dave's Hot Chicken | 38.32612, -85.74751 (Clarksville, IN) | Official locator has Jeffersonville branch but no precise address in excerpt to confirm mapped point; Clarksville label may be imprecise. Checked in web search on2026-11-18. [source 1](https://restaurants.daveshotchicken.com/in/) |
| w337273036 | Fazoli's | 337 Whittington Parkway | Official Kentucky directory does not establish 337 Whittington; absence alone insufficient for permanent closure. Checked in web search on2026-11-18. [source 1](https://fazolis.com/directory/kentucky/) |
| n14374060124 | Freddy's Frozen Custard | 37.9963, -85.70763 (Shepherdsville) | Official directory mentions Shepherdsville, but exact addressless point not confirmed. [source 1](https://www.freddys.com/location?state=az) |
| n6069862355 | Great American Cookies | 38.24699, -85.61064 (Lyndon & Westport) | General directories refer7900Shelbyville and5000Shelbyville; precise mapped Oxmoor unit operation unresolved. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/louisville-ky/otis-spunkmeyer-cookies) |
| n11980061482 | Hardee's | 2740 Allison Lane | Current directory describes temporary closure at 2740 Allison; commercial listing suggests vacant but independent permanence not established. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/utica-in/fast-food-restaurants) |
| n12381248844 | Jersey Mike's Subs | 38.21719, -85.58619 (Jeffersontown) | 1983 South Hurstbourne listed; could not match this addressless point confidently. [source 1](https://www.restaurantji.com/ky/louisville/jersey-mikes/) |
| n3444277564 | Krispy Krunchy Chicken | 1610 Dixie Highway | Exact-name/address search did not find reliable current evidence for 1610 Dixie Highway.  |
| n3830893872 | Moe | 38.3246, -85.76706 (Clarksville, IN) | Search mixes Noblesville and Clarksville Tennessee Moe’s; no current Clarksville Indiana location established. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/clarksville-in/moe-s-southwest-grill) |
| w1190671158 | Panera Bread | 276 Keystone Crossroads Drive | Original locator URL inaccessible; search found historical utility filing at address, which does not establish current operation. [source 1](https://locations.panerabread.com/ky/shepherdsville/276-keystone-crossroads-dr.html) |
| w329551172 | Pizza Hut | 12425 Shelbyville Road | Historic/OSM-derived listing still shows 12425 Shelbyville; official base URL inaccessible. No independent closure evidence sufficient. [source 1](https://eatoutmap.com/en/usa/douglass-hills) |
| w337501562 | Qdoba | 100 Daventry Lane | Search locates old 100 Daventry listing but no explicit permanent closure or exact current successor; missing city directory alone not independently corroborated. [source 1](https://www.yellowpages.com/louisville-ky/qdoba-restaurants) |
| w820708215 | Rally's | 38.30919, -85.84321 (New Albany, IN) | Official source says 2316 State while delivery/recruitment says 2350 State. Addressless mapped point needs coordinate resolution; retain uncertainty. [source 1](https://checkersandrallys.com/location/rally-s-4302-state-st-2795577) |
| w334007680 | Sonic | 3425 Bardstown Road | Exact historic 3425 Bardstown entry found; no independently reliable current closure evidence. [source 1](https://www.city-data.com/locations/SONICDriveIn/Louisville-Kentucky.html) |
| w335692193 | Sonic | 630 Winkler Avenue | Exact 630 Winkler listing has hours whereas low-quality closure aggregator says closed. Neither establishes current operation; initial sitemap absence uncorroborated. [source 1](https://www.allbiz.com/business/sonic-drive-in_506f) |
| w337528083 | Sonic | 13310 Shelbyville Road | 2026 deal aggregator still advertises Sonic at 13310 Shelbyville, but cannot establish reliability. Old locator absence alone insufficient. [source 1](https://noshgrid.com/deals/ky/middletown) |
| n4780015155 | Subway | 38.30916, -85.84496 (New Albany, IN) | Search found Subway-Closed references in New Albany but did not establish exact State Street address or match to coordinate; retain unsure rather than trust missing directory alone. [source 1](https://www.superpages.com/new-albany-in/restaurants?page=4) |
| n6069056992 | Subway | 38.25732, -85.74784 (NuLu & Butchertown) | Exact 222 E Witherspoon store no longer available since August 2026, corroborating first-pass official directory absence. Delivery-platform closure alone would not establish permanent closure.; Final independent QA: platform departure and absence from locator do not independently prove permanent closure at this exact mapped location. Keep visible flagged. [source 1](https://www.ubereats.com/store/subway-222-witherspoon-aves/JWuHFaftTWuWR_nxIh8ndg) · [source 2](https://www.ubereats.com/store/subway-222-witherspoon-aves/JWuHFaftTWuWR_nxIh8ndg) |
| w330564804 | Subway | 2500 Bardstown Road | Jet Pizza operates at 2500 Bardstown but sources show multiple suites; this does not prove Subway in suite 1 closed. Initial missing-locator verdict not independently corroborated. [source 1](https://www.jetspizza.com/stores/kentucky/louisville/2500-bardstown-rd/) |
| w1093670252 | Zaxby's | 38.3208, -85.71046 (Jeffersonville, IN) | Official Jeffersonville directory found but exact addressless OSM coordinate has not been matched. [source 1](https://www.zaxbys.com/locations/in/jeffersonville) |
| n14355306467 | Biggby Coffee | 38.02643, -85.61409 (Hillview & Mount Washington) | Search returns proposed Biggby locations elsewhere in Louisville, not mapped Hillview point; rejected wrong-location evidence. Checked in web search on2026-11-18. [source 1](https://louisville.legistar.com/View.ashx?GUID=5A6AAC8D-2CFB-4362-9DE8-C44D501BF880&ID=1417946&M=PA) |
| n6069217514 | Burger King | 38.24402, -85.51902 (Middletown & Anchorage) | Search for Middletown/Shelbyville Burger King did not establish an exact address for the coordinate-only point; other branches cannot confirm this one. [source 1](https://www.yellowpages.com/louisville-ky/burger-king) |
| w1190671162 | Burger King | 37.99354, -85.70868 (Shepherdsville) | Tourism directory lists 315 Keystone Crossroads Drive but no coordinate match established against addressless OSM point; cannot verify exact mapped location. [source 1](https://travelbullitt.org/listing/burger-king-shepherdsville/) |
| w339258579 | Chili's | 6641 Dixie Highway | Only general directory records at 6641 Dixie; no official/current service evidence established. Checked in web search on2026-11-18. [source 1](https://www.superpages.com/pleasure-ridge-park-ky/take-out-restaurants) |
| n12750423684 | Chuck E. Cheese | 38.18988, -85.56551 (Jeffersontown) | Official directory lists 2030 S Hurstbourne, a separate mapped location from this coordinate; cannot establish current restaurant here. [source 1](https://www.chuckecheese.com/louisville-ky/adventurezone/locations/) |
| n3829329431 | Chuy's | 38.33042, -85.75519 (Clarksville, IN) | Directory gives Clarksville address 1440 Veterans Pkwy Court Suite100 but exact addressless point not matched. [source 1](https://mystore411.com/store/listing/680/Chuys-store-locations) |
| n12391907057 | Cold Stone Creamery | 38.33372, -85.71168 (Clarksville, IN) | Official Jeffersonville store found, but OSM addressless point labeled Clarksville needs exact-coordinate match. [source 1](https://www.coldstonecreamery.com/stores/ice-cream-near-jeffersonville/23571) |
| n13846896473 | Dairy Queen | 38.32799, -85.74163 (Clarksville, IN) | Clarksville municipal restaurant directory mentions Dairy Queen; exact coordinate-only point and current operating status unresolved. [source 1](https://www.townofclarksville.com/restaurants/) |
| n14372059296 | Dairy Queen | 38.13841, -85.6639 (Okolona) | 5608 Outer Loop listing found but official/delivery result for similarly named 5608 redirects address to 5103 Outer Loop, a different OSM entry; do not treat this as confirmation. [source 1](https://fastfoodinusa.com/dairy-queen/address-5608-outer-loop/) |
| w821982256 | DQ Grill & Chill | 1055 Veterans Parkway | Listing explicitly says temporarily closed, while delivery listings remain. Temporary closure is not evidence of permanent closure; current operation unresolved. [source 1](https://www.yellowpages.com/clarksville-in/bpp/dairy-queen-grill-chill-474224435) |
| w1093670243 | DQ Grill & Chill | 2909 East 10th Street | Franchisee location page remains, but third-party listings conflict (closed/temporarily closed). Current operation not established. [source 1](https://fourteenfoods.net/ffstore/2909-e-10th-street-jeffersonville-indiana/) |
| n6069862357 | Extreme Pita | 38.2468, -85.61067 (Lyndon & Westport) | Review listings have no current operating evidence or precise mall-unit match. Checked in web search on2026-11-18. [source 1](https://www.tripadvisor.ca/Restaurant_Review-g39604-d10391792-Reviews-Extreme_Pita-Louisville_Kentucky.html) |
| w337706687 | Frisch's Big Boy | 2962 Breckenridge Lane | Official current list omits2962Breckenridge; general directory remains, no conclusive independent permanence. Checked in web search on2026-11-18. [source 1](https://www.frischs.com/participating-locations-3/) |
| w337853317 | Frisch's Big Boy | 7401 Dixie Highway | Uber Eats departure2023 not permanent-closure proof; northernKentucky Dixie closure is different city and rejected. Checked in web search on2026-11-18. [source 1](https://www.ubereats.com/store/frischs-big-boy-7401-dixie-hwy/aZdkpKLdQvCzIKHAyGNkhw) |
| n6077278389 | Golden Corral | 38.21927, -85.62301 (Hikes Point & Buechel) | Official locator confirms 4032 Taylorsville Rd, but addressless mapped point not independently coordinate-matched. [source 1](https://www.goldencorral.com/locations/location-detail/899/golden-corral-taylorsville-rd/) |
| w339260716 | Golden Corral | 5362 Dixie Highway | Only 4032 Taylorsville found in official list, but 5362 Dixie still appears in third-party directories. Absence alone insufficient for permanent closure. [source 1](https://www.goldencorral.com/locations/all-locations/) |
| n5949868534 | Great American Grill | 38.31055, -85.57633 (Prospect & Northeast) | Mapped Von Allmen hotel cafe found only in OSM-derived directories; similarly named restaurants elsewhere rejected. Checked in web search on2026-11-18. [source 1](https://kentucky-streets.openalfa.com/zipcodes/6040241/eating-drinking) |
| n11981658730 | Honey Baked Ham | 38.33296, -85.8166 (New Albany, IN) | Current directory lists 3602 Northgate Court; addressless mapped point not coordinate-matched. [source 1](https://www.doordash.com/city/new-albany-in/b/the-honeybaked-ham-company-40241/) |
| n12677619514 | Hunt Brothers Pizza | 37.99918, -85.94441 (Valley Station & PRP) | Search lists other HuntBrothers counters, not exact mapped WestPoint point; no current address verified. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/valley-station-ky/pizza?page=2) |
| n6069846474 | Krispy Kreme | 38.2055, -85.57931 (Jeffersontown) | Mapped point appears old 9569 Taylorsville; official current locator omits it, but independent permanent closure not confirmed. Checked in web search on2026-11-18. [source 1](https://www.groupon.com/biz/jeffersontown-ky/krispy-kreme-east-louisville) |
| n5654275221 | Long John Silver's | 38.29168, -85.50982 (Middletown & Anchorage) | General result says may be permanently closed; no exact mapped La Grange-area address/current evidence. Checked in web search on2026-11-18. [source 1](https://restaurantguru.com/Middletown-Kentucky/5) |
| n13446959109 | Marco's Pizza | 2011 Charlestown Road | Official2025inspection establishes identity but no current service independent of first-pass Waze; remains unresolved. Checked in web search on2026-11-18. [source 1](https://www.in.gov/counties/floyd/health-department/files/food-inspections/retail-food-inspections/2025/Marcos-Pizza-7-18-25.pdf) |
| n9726086554 | Matt Winn's Steakhouse | 38.20343, -85.77402 (South End) | RestaurantGuru says permanently closed but ChurchillDowns restaurant/seasonal-event identity unresolved; avoid removing solely from one directory. Checked in web search on2026-11-18. [source 1](https://restaurantguru.com/Matt-Winns-Steakhouse-Louisville) |
| w337418676 | Moby Dick House of Kabob | 12414 Dixie Highway | House of Kabob is WashingtonDC-region brand; mapped Louisville identity appears incorrect and requires local Seafood source. Checked in web search on2026-11-18. [source 1](https://www.mobyskabob.com/) |
| n6069763987 | MOD Pizza | 38.21575, -85.62669 (Hikes Point & Buechel) | Only generic directory hours at3085Breckenridge; no current official store operation confirmed. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/louisville-ky/mip/mod-pizza-532146980) |
| n6069846444 | Noodles & Company | 38.22743, -85.57687 (Jeffersontown) | General directory at1225S Hurstbourne plus delivery menu without matched address insufficient to confirm mapped location. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/jeffersontown-ky/asian-restaurants) |
| n3170512516 | Papa John's | 38.21763, -85.75609 (Old Louisville) | Search found Papa Johns at 2336 S Floyd and food service at 2100 S Floyd, but cannot locate this addressless campus point precisely. Possible campus concession. [source 1](https://lamppost.fyi/louisville/neighborhood/university/food_service) |
| n12391906922 | Parlor Doughnuts | 38.3501, -85.70413 (Clarksville, IN) | Official Jeffersonville location found, but exact coordinate-only OSM point not matched. [source 1](https://www.parlordoughnuts.com/shops/jeffersonville-in) |
| n3453099463 | Penn Station | 38.13842, -85.67589 (Okolona) | Official locator lists 4247 Outer Loop; addressless point not coordinate-matched, so no exact-location confirmation. [source 1](https://penn-station.com/locations/?store=424) |
| n14372059290 | Popeyes | 38.13477, -85.57922 (Highview & Fern Creek) | Search shows Popeyes 7723 Bardstown Rd; addressless point needs coordinate matching; insufficient exact-location evidence. [source 1](https://www.ubereats.com/delivery/dish/shepherdsville-ky/chicken-gyro) |
| w336482091 | Shoney's | 6511 Signature Drive | Official directory still lists 6511 Signature Drive but displayed Closed hours lack enough context; exact current operation not established. [source 1](https://www.shoneys.com/locations/ky) |
| w339258880 | Skyline Chili | 6801 Dixie Highway | Old6801Dixie directory remains; current official site could not confirm move/new address, so do not infer closure. Research lead7105Dixie proved FairfieldOhio, not Louisville; rejected wrong-city relocation inference. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/fort-knox-ky/chilis-restaurant) |
| n3773229987 | Smashburger | 316 South 4th Street | Mapped address 316 S4th appears on directory but official city list only Hurstbourne; Closed now is not permanent closure evidence. [source 1](https://www.waze.com/live-map/directions/smashburger-s-4th-st-316-louisville?to=place.w.179700095.1797263089.1125482) |
| n6066607788 | Smashburger | 38.24741, -85.57819 (Lyndon & Westport) | Official Hurstbourne store confirms 9409 Shelbyville Rd; no exact coordinate match to addressless point established. [source 1](https://smashburger.com/locations/us/ky/louisville/9409-shelbyville-rd) |
| n7647535431 | Smoothie King | 38.3506, -85.79479 (Clarksville, IN) | Official New Albany location found despite OSM city label Clarksville, but coordinate match not independently established. [source 1](https://locations.smoothieking.com/ll/us/in/new-albany/4214-charlestown-rd-1/) |
| n6069056995 | Starbucks | 38.25644, -85.75779 (Downtown) | Current downtown directory lists Heine PNC and several hotel Starbucks. No address on map point, so cannot confidently identify former store; missing locator alone insufficient. [source 1](https://louisvilledowntown.org/coffee-shops-in-downtown-louisville/) |
| w336682483 | Steak 'n Shake | 10721 Fischer Park Drive | Cylex marks temporarily closed while Restaurantji lists service; current status unresolved. Checked in web search on2026-11-18. [source 1](https://www.cylex.us.com/company/steak-%27n-shake-20614750.html) |
| n3321208766 | sweetFrog | 38.29312, -85.55805 (Lyndon & Westport) | Listings describe temporary closure; no exact-address/current evidence to resolve addressless Springhurst point. [source 1](https://www.yellowpages.com/louisville-ky/sweet-frog-frozen-yogurt) |
| n6069217495 | Taziki's Mediterranean Cafe | 38.24348, -85.50579 (Middletown & Anchorage) | Official locator confirms 13317 Shelbyville Suite105; addressless mapped point not coordinate-matched. [source 1](https://www.tazikis.com/location/middletown) |
| n3447718845 | The Wing Zone | 3038 Hunsinger Lane | Exact-address menu listings remain at 3038 Hunsinger, but freshness/current hours not sufficient to establish current operation. [source 1](https://www.sluurpy.us/louisville/restaurant/3783447/wing-zone) |
| w343526641 | 3rd Turn Brewing | 10408 Watterson Trail | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.corner.inc/place/poqTX7Hz6UFF) |
| n3434829824 | 5 O'Clock Charlie's | 14808 Taylorsville Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.openingtimes.co/kentucky/louisville_40299) |
| w1078002456 | A Taste of Thai | 6002 Pleasant Colony Court Suite 102, Pleasant Colony | Sources give6549WHighway22 versus OSM6002PleasantColony; move distance/old spot not independently established.  |
| n3467847352 | Akiko's Restaurant | 38.23804, -85.71992 (Highlands) | March20 2026 follow-up says bar is not closing yet after agreement. Earlier announced March17 closure was rescinded; cannot use it as closure evidence. [source 1](https://www.wlky.com/article/akikos-karaoke-bar-highlands-closing/70736360) |
| n6069056988 | Al J's at the Conservatory | 38.25776, -85.7572 (Downtown) | Search for Al J's Conservatory found Galt House restaurant replacement information but no reliable current evidence for this specific bar. [source 1](https://ajshotels.com/restaurant-concept-louisville/) |
| n3375494286 | Alex&nder | 1121 East Washington Street | CurrentCopperKings officialrooftop operates withCulturedfood; whetherAlexNder remains an alias not established. [source 1](https://copperandkings.com/the-rooftop-bar/) |
| n11270546816 | Alley Cat Cafe & Catering | 11804 Shelbyville Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d552817-Reviews-Alley_Cat_Cafe_Catering-Louisville_Kentucky.html) |
| n2497238184 | Anchorage Cafe | 38.26543, -85.54042 (Middletown & Anchorage) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://louisville.eater.com/venue/2118/anchorage-cafe) |
| n14068590042 | Angie's Cafe | 2781 Jefferson Centre Way | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g37216-d19255578-Reviews-Angie_s_Cafe-Jeffersonville_Indiana.html) |
| n6044760478 | Aqua Sushi | 38.21703, -85.75619 (Old Louisville) | University dining guide mentions Aqua Sushi; cannot establish whether this exact campus point still operates or public access. [source 1](https://louisville.edu/healthpromotion/files/ULDiningVeganVegetarianGuide.pdf/) |
| n677657177 | Asian Moon | 38.21917, -85.62615 (Hikes Point & Buechel) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.openingtimes.co/asian-moon-louisville-ky) |
| n3467853440 | Asiatique Restaurant | 1716 | Asiatique closure sources give 1767 Bardstown; the map record gives 1716. Exact location mismatch remains unresolved.  |
| n3380192607 | Aspire Cafe & Juice Bar | 332 West Broadway | Only OSM-derivedAspire332Broadway references found.  |
| n6069846420 | AunTEA Pearl's Tea Establishment | 38.2259, -85.57565 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.wlky.com/article/these-restaurants-closed-permanently-during-the-pandemic/32804252) |
| w337062636 | Austins | 4950 U S Highway 42 | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.openingtimes.co/austins-louisville-ky) |
| n6069217485 | Barbarella | 38.25561, -85.75068 (Downtown) | Barbarella point not matched to current exact business.  |
| n6391860110 | Barbour Lane Pizza & Deli | 38.29614, -85.60234 (Lyndon & Westport) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://kentucky-streets.openalfa.com/zipcodes/6040241/eating-drinking) |
| n6800719886 | Barrel Bar | 38.25323, -85.75322 (Downtown) | CurrentBarrelBar110WMain evidence is >150m from map point; cannot transfer open status.  |
| n6178597442 | Base Camp Coffee at Quest Outdoors | 4600 Shelbyville Road | Quest Outdoors retail service does not establish whether its Base Camp coffee counter still operates.  |
| n3363641807 | Baxter's 942 Bar & Grill | 942 Baxter Avenue | Current third-party listing found for Baxters 942, but recent operating evidence is insufficient.  |
| n7573377487 | Bearno's Little Sicily Pizza | 38.32324, -85.64432 (Prospect & Northeast) | Search does not establish mapped River Road-area restaurant; other Bearno’s locations rejected. Checked in web search on2026-11-18. [source 1](https://www.cityof.com/ky/louisville/restaurants/pizza?p=1) |
| n13384448659 | Blossom Bar | 38.35073, -85.79614 (Clarksville, IN) | Blossom Bar addressless point not matched to current exact restaurant.  |
| n3765637769 | BoomBozz Pizza & Taphouse | 1450 Veterans Parkway | Independent review listing agrees address1450Veterans but no current hours/posts in excerpt; Waze alone not enough to upgrade. Checked in web search on2026-11-18. [source 1](https://www.tripadvisor.com.sg/Restaurant_Review-g37216-d5946710-Reviews-Boombozz_Pizza_Watch_Bar-Jeffersonville_Indiana.html) |
| w338407460 | BoomBozz Pizza & Taphouse | 1890 South Hurstbourne Parkway | General directories only at1890S Hurstbourne; no independent current service evidence. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/hurstbourne-acres-louisville-ky/restaurants) |
| n11270546821 | Boudreaux's New Orleans Style Sno-Balls | 11816 Shelbyville Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.yellowpages.com/middletown-ky/mip/boudreauxs-new-orleans-style-sno-balls-523967552) |
| n5750135027 | Bourbon Barrel Burgers | 38.25827, -85.75356 (Downtown) | BourbonBarrelBurgers map point not matched; search returns distinct Bourbon&Burgers and BourbonBarrelFoods.  |
| n2496184629 | Brix Wine Bar | 38.29005, -85.50923 (Middletown & Anchorage) | June26 2026 health inspection indexed and active-license directory conflict with old closed listings; current primary operation unconfirmed, so do not remove. [source 1](https://nosynelly.com/ky/louisville/restaurants/brix-wine-bar-bistro-12418-la-grange-rd) |
| n2934216022 | Bunz | 971 Baxter Avenue | Listings for Bunz at 969/971 Baxter found, but current operation is insufficiently confirmed.  |
| n6066643689 | Cafe Magnolia | 38.2582, -85.7558 (Downtown) | LegacyWyndham listsCafeMagnolia; hotel new floorplans show different restaurants but distinct room identity cannot resolve.  |
| w1068091564 | Caribbean Cafe | 317 West Woodlawn Avenue | Current delivery listing at317WWoodlawn under CaribbeanRestaurantandBakery and August2026 inspection conflict with old permanentclosed label; do not suppress without resolving identity/current operation. [source 1](https://www.ubereats.com/store/caribbean-restaurant-and-bakery/AfWHXEUYWw-DbdyzrudF0g) |
| w840573242 | Cast Iron Steakhouse | East Market Street | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://castironsteak.com/) |
| n13424071604 | Cherry Pickin' | 38.25389, -85.73648 (NuLu & Butchertown) | Addressless Cherry Pickin point not independently matched.  |
| w337083171 | Chicago Steak & Lemonade | 2126 West Broadway | Chicago Steak and Lemonade at 2126 West Broadway found only in OSM-derived references.  |
| n6066545287 | Chicken King | 38.24522, -85.74183 (NuLu & Butchertown) | Chicken King search returned delivery results without enough exact mapped-location confirmation.  |
| n13322053995 | Classico Takeout & Empanadas | 400 East Main Street | Classico Takeout and current Classico Pizzeria branding may refer to different locations; unresolved.  |
| n6399762803 | Coffee Crossing | 4215 Charlestown Road | 2026 official inspection and own locator say 4212 Charlestown while OSM says 4215; precise mapped storefront match unresolved. Checked in web search on2026-11-18. [source 1](https://www.in.gov/counties/floyd/health-department/files/food-inspections/retail-food-inspections/2026/Coffee-Crossing-Charlestown-Rd-2-24-26.pdf) |
| n3464533107 | Cosmic Pizza | 38.15078, -85.83537 (Valley Station & PRP) | Cosmic Pizza listing at 6801 Dixie may share a centre with other restaurants; current identity remains unconfirmed.  |
| w329519048 | Cottage Cafe | 11609 Main Street | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39657-d862627-Reviews-Cottage_Cafe-Middletown_Kentucky.html) |
| n6391859990 | Diamond Pub & Billiards | 38.25273, -85.65647 (St. Matthews) | Diamond Frankfort listings persist; closure reports about another branch cannot establish this branch status.  |
| n6069846468 | Double Dragon | 38.20668, -85.58074 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://dk.yp.com/jeffersontown-ky/restaurants) |
| n6065590587 | El Barrio | 38.25637, -85.75289 (Downtown) | ElBarrio addressless downtown point not matched to current business.  |
| n7618129085 | El Frijol | 1999B Brownsboro Road | Only OSM-derived ElFrijol listings found, not independent evidence.  |
| n3445815407 | El Rio Grande Mexican Restaurant | 10001 Forest Green Boulevard | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d8809292-Reviews-El_Rio_Grande_Mexican_Restaurant-Louisville_Kentucky.html) |
| n3372435580 | Encore on 4th | 630 South 4th Street | Encore630S4th older city/OpenTable listings insufficient current evidence.  |
| n3442881685 | Equus | 122 Sears Avenue | Own Equus site retains 2018 content; generic newer listing hours are insufficient current confirmation.  |
| n6391860085 | FABD Smokehouse | 38.2541, -85.675 (Crescent Hill & Clifton) | FABDSmokehouse exact3204Frankfort historic menu/listing but no reliable current confirmation.  |
| n3364252317 | Firenza Pizza | 12406 La Grange Road | Only historic Firenza listings at 12406 La Grange found.  |
| n6066549687 | Fishery Station | 38.13848, -85.65628 (Okolona) | Fishery Station II listing found at 5610 Outer Loop; current operation at the mapped point remains unconfirmed.  |
| n5999579236 | Flippin' Pancakes | 38.35183, -85.794 (Clarksville, IN) | Only old FlippinPancakes listings at1220Veterans/4320Charlestown; mapped Charlestown point current operation not established.  |
| w883990499 | Forest Music Hall | 38.28266, -85.82402 (New Albany, IN) | Historic Forest Music Hall identity not confirmed as an operating public venue.  |
| n7872507456 | Frascellis Pizza | 38.38278, -85.44117 (Crestwood & Oldham Co.) | Tourism/old county directory listsFrascellis4310W146 but current service not established.  |
| n3380191829 | Freddie's Bar and Lounge | 220 West Broadway | Freddies permanent-closed result says220E instead of220W; do not apply closure to wrong side.  |
| n7571670486 | Garrett's Goodies | 38.33518, -85.65295 (Prospect & Northeast) | Garretts Goodies addressless point remains unresolved.  |
| w337693834 | Ginza's Asian Bistro | 9420 Shelbyville Road | No reliable exact-location, current evidence established after two passes.  |
| n2548889297 | Great Wall | 38.259, -85.70412 (Crescent Hill & Clifton) | GreatWall current1977Brownsboro location does not match addressless point roughly400m east; cannot apply other entry evidence.  |
| n6044760479 | Green to Go | 38.21697, -85.75627 (Old Louisville) | Green to Go campus point not matched; unrelated Tavern To Go results rejected.  |
| n10879657977 | Hanoi Cafe | 38.25223, -85.65131 (St. Matthews) | Hanoi at 104 Fairfax is distinct from Nam Nam at 318 Wallace; wrong-location results rejected.  |
| n6069809467 | Happy China | 38.21235, -85.5907 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.waze.com/live-map/directions/happy-china-taylorsville-rd-9106-jeffersontown?to=place.w.179831166.1798377197.1854862) |
| n6064659386 | Haymarket Whiskey Bar | 38.25436, -85.74691 (NuLu & Butchertown) | Generic bar-guide entries only; no reliable current operating hours or address-specific activity. Checked in web search on2026-11-18. [source 1](https://wanderlog.com/list/geoCategory/818294/os-melhores-bares-com-m%C3%BAsica-ao-vivo-em-louisville) |
| n13676306722 | Heavy plates | 605 Lyndon Lane | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://kentucky-streets.openalfa.com/lyndon-city/eating-drinking) |
| n4755772899 | Heine Brothers' Coffee | 516 West Main Street | Old exact 516 Main listing persists; current PNC store is nearby at 101 S5th. Without exact former entrance geolocation, move may be within 150m; missing old address alone insufficient. [source 1](https://www.ubereats.com/store/heine-brothers-coffee-main-street/ZjAulYH_VkasZ-vmRMQoUw) |
| n5900605922 | Hibachi Buffet | 38.15671, -85.8363 (Valley Station & PRP) | Recent Hibachi Buffet reviews at 5372 Dixie do not match the mapped point several kilometres away.  |
| n6069705490 | Hike's Point Lounge and Bar | 38.22056, -85.62724 (Hikes Point & Buechel) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://jockssportsbar.com/) |
| n3321208401 | Home Run Burger | 4600 Shelbyville Road | Official ordering page omits4600Shelbyville; closed12949Shelbyville result is different location and rejected. Checked in web search on2026-11-18. [source 1](https://order.homerunburger.com/contact-us-2) |
| w329565878 | Homemade Ice Cream and Pie Kitchen | 1041 Bardstown Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d819368-Reviews-Homemade_Ice_Cream_Pie_Kitchen-Louisville_Kentucky.html) |
| w24022075 | hometown pizza | 38.0527, -85.53441 (Hillview & Mount Washington) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://hometownpizza.com/our-locations/) |
| n5218281360 | Hoops | 38.30476, -85.52412 (Crestwood & Oldham Co.) | Hoops point overlaps Rooties but current brand/succession unconfirmed.  |
| n3364361417 | I Heart Juice Bar | 13317 Shelbyville Road | Exact juice bar left Uber Eats in 2021; platform departure alone cannot establish permanent closure.  |
| n6392755492 | Impelli | 38.28196, -85.632 (Lyndon & Westport) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://guava.failover.uber.com/dish/hurstbourne-ky/gyro) |
| n6065597389 | Jack's Lounge | 38.25396, -85.64675 (St. Matthews) | Old shared Equus and Jacks website does not sufficiently confirm current lounge operation.  |
| n3442807046 | Jade Palace | 38.26728, -85.61243 (Lyndon & Westport) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.westportvillage.com/store/jade-palace/) |
| n3397256042 | Jeff's Burger Shack | 14126 Dixie Highway | Jeffs listing has hours but also a truck shutdown notice; no sufficiently current operating evidence.  |
| w339269741 | Jessie's Restaurant | 9609 Dixie Highway | Jessies has old news and generic menus, without current operating confirmation.  |
| n3166614945 | Jumbo Buffet | 38.21107, -85.59589 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://restaurantguru.com/Jumbo-Buffet-Louisville) |
| n6392702989 | Kentucky State Donuts | 38.28841, -85.51227 (Middletown & Anchorage) | Mapped Kentucky State Donuts point is near La Grange Road; Yonutz on Shelbyville Road is a different location.  |
| w330564839 | Kern's Korner | 2600 Bardstown Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.waze.com/live-map/directions/us/ky/louisville/kerns-korner?to=place.ChIJcbXiuVgLaYgRftiCPh511Ks) |
| n5700155943 | Kiwa | 2235 Frankfort Avenue | November 3, 2026 local news calls KIWA closure temporary; permanence is not established. [source 1](https://www.wdrbwave.com/2026/11/03/louisville-korean-cafe-kiwa-temporarily-closes-frankfort-avenue/) |
| n3375222879 | Kiwami Ramen | 1700 Bardstown Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://louisvillebarsandrestaurants.com/places/kiwami-ramen/) |
| n6806472486 | La Cucina de Mama | 38.2863, -85.56996 (Lyndon & Westport) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://kentucky-streets.openalfa.com/zipcodes/6040241/eating-drinking) |
| n3368832068 | Le Petit Cafe | 1325 Bardstown Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://kentucky-streets.openalfa.com/louisville-city/eating-drinking) |
| n6065597390 | Levee at River House | 38.28151, -85.69859 (Crescent Hill & Clifton) | RiverHouse operates at3015River but Levee separate venue identity/current status not established.  |
| n6392757287 | Liegue | 38.283, -85.63179 (Lyndon & Westport) | No reliable exact-location, current evidence established after two passes.  |
| n9020029117 | Loaves and Fishes | 38.23863, -85.74645 (Old Louisville) | Loaves and Fishes nonprofit meal service found, but status as a public restaurant at this point is unconfirmed.  |
| w337108644 | Lolitas Tacos | 38.19821, -85.70817 (Audubon & Airport) | Only old exact4222Poplar listings found; current operation not established.  |
| n5269119084 | Lovafare (vegan) | 38.24048, -85.72414 (Highlands) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.manta.com/c/mks3213/lovafare) |
| n4848336123 | Maggie Mae's Cafe | 435 North Bardstown Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://bullittcountykyguide.com/) |
| n6093788938 | Maker/Cafe | 38.25767, -85.7621 (Downtown) | MakerCafe exact downtown point not independently identified.  |
| n3448918171 | Mango's Bar and Grill | 4632 Hendrik Drive | No reliable exact-location, current evidence established after two passes.  |
| n3363962794 | Masa Japanese Bistro & Sushi | 12336 Shelbyville Road | Toast shows closed all week, conflicting with generic third-party hours; permanent closure is unconfirmed.  |
| n6066549689 | Mike Linnig's | 38.11908, -85.89727 (Valley Station & PRP) | Tourism bureau lists restaurant at 9308 Cane Run Rd and 2026 reopening news exists, but coordinate-only point not independently matched. [source 1](https://www.gotolouisville.com/directory/mike-linnigs/) |
| w1068091566 | Nagaad Cafe | 349 West Woodlawn Avenue | Nagaad listing gives 349 West Kenwood; map gives 349 West Woodlawn. Move and current status are unresolved.  |
| n6633976785 | Naila’s Caribbean cuisine | 1360 Veterans Parkway | Old source gives1370Veterans whereas OSM1360; no current exact confirmation.  |
| n9336873202 | Neon Pizza | 38.23446, -85.75521 (Old Louisville) | Neon Pizza addressless point not matched; unrelated pizza results rejected.  |
| n2496184448 | New Directions | 38.28952, -85.51503 (Middletown & Anchorage) | Addressless New Directions point not matched to a current business.  |
| n6044760472 | O-Mori Ramen Bar | 38.2172, -85.75616 (Old Louisville) | O-Mori campus point is over 150 metres from Renshoku at Second and Oak; evidence cannot transfer.  |
| w336416400 | Ole Hickory Pit Bar-B-Que | 5906 Shepherdsville Road | Directory says may be permanently closed, but initial news address6006 vs mapped5906 remains unverified; cannot assert mapped-site removal. [source 1](https://restaurantguru.com/Ole-Hickory-Pit-Bar-B-Que-Louisville) |
| w337087475 | Overtime Sports Bar and Grill | 307 Central Avenue | Overtime at 307 Central found only in OSM-derived references.  |
| n9726086555 | Paddock Grill | 700 Central Avenue | Churchill Downs Paddock Grill listing does not establish current public access or service schedule.  |
| n6066456091 | Passtime Fish House | 38.20431, -85.55706 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39545-d1833684-Reviews-PassTime_Fish_House_Tavern-Jeffersontown_Kentucky.html) |
| n3375222881 | Pho Cafe on Bardstown | 1704 Bardstown Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d12508311-Reviews-Pho_Cafe_on_Bardstown-Louisville_Kentucky.html) |
| w334733226 | Pizzeria Villagio | 38.196, -85.7475 (Audubon & Airport) | Only generic937Phillips listings; searches also return unrelated Virginia/Philadelphia businesses, rejected.  |
| n5979203195 | P.O.D. Cafe | 38.21548, -85.75779 (Old Louisville) | POD Cafe campus point not matched to a current dining outlet.  |
| n13384448664 | Puerto Vallarta | 38.35074, -85.79468 (Clarksville, IN) | Search results chiefly SouthBend or Jeffersonville; rejected as not mapped NewAlbany-area point.  |
| n6069733386 | Queenie's Restaurant | 38.22085, -85.62645 (Hikes Point & Buechel) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://callejero-kentucky.openalfa.com/calles/hikes-lane-hikes-point-ky-hikes-lane) |
| n6069718187 | Red Sun Chinese Restaurant | 38.19859, -85.62288 (Hikes Point & Buechel) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.yellowpages.com/hikes-point-louisville-ky/asian-restaurants) |
| n6069056987 | Robyn's Nest Bourbon Bistro | 38.25719, -85.76031 (Downtown) | RobynsNest search results unrelated; current exact status not established.  |
| n10244209700 | Rooties Sports Bar & Grille | 12205 Westport Road | Rooties current thirdparty hours appear generic9-6; embedded2year-old review says closed. No primary current evidence.  |
| w1029208210 | Sam's Gyros | 3123 S 2nd Street | Exact3123S2nd deliverylisting appears,but currentavailabilityunclear; retainunsure. [source 1](https://www.ubereats.com/store/sams-gyros/FIC5kDqoV7-3qxT-W5xopQ) |
| n3373722656 | Sarang | 1908 Eastern Parkway | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.waze.com/live-map/directions/sarang-korean-restaurant-eastern-pkwy-1908-louisville?to=place.w.179765630.1797590767.5740375) |
| n6069076485 | SCENE at the Center | 38.25707, -85.7585 (Downtown) | SCENE501WMain event-night service appears on2023map, insufficient current operation confirmation.  |
| n9668218017 | Scholars Coffee | Seminary Road | Seminary directory confirms campus coffee service, but current access to the public is unconfirmed. [source 1](https://inside.sbts.edu/dining-services/) |
| n12750423687 | Scoops | 38.18984, -85.5652 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.scoopsnsuch.com/) |
| n13283031543 | Scooters | 38.28487, -85.57999 (Lyndon & Westport) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.restaurantji.com/ky/louisville/scooters-coffee-5/) |
| n5145584127 | Scott's | 38.23965, -85.48846 (Middletown & Anchorage) | Addressless Scotts point not matched; unrelated Scotts Station results rejected.  |
| n11979358377 | Señor Iguanas | 14000 Broadway Street | 2026 official license and own site use 1415 Broadway; mapped 14000 is invalid. Precise point match unconfirmed. Checked in web search on2026-11-18. [source 1](https://www.in.gov/atc/files/2026.2-LB.pdf) |
| w337694055 | Señor Iguanas | 9424 Shelbyville Road | Only general old directory evidence at 9424 Shelbyville found; current restaurant not established. Checked in web search on2026-11-18. [source 1](https://www.yellowpages.com/shelbyville-ky/latin-american-restaurants) |
| n6328331485 | Señora Arepa | 938 Baxter Avenue | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.yahoo.com/lifestyle/bourbon-burgers-restaurant-replace-se-141649882.html) |
| w330411891 | Shenanigans Bar & Grill | 1611 Norris Place | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d3802667-Reviews-Shenanigans_Irish_Grille-Louisville_Kentucky.html) |
| n6392755488 | Shiraz Mediterranean Grill | 38.28281, -85.63128 (Lyndon & Westport) | Live official ordering lists 2226 Holiday Manor Ctr Ste1; addressless mapped point needs exact-coordinate check. [source 1](https://shirazmg.order.tryperdiem.com/locations/louisville-shiraz-holiday-manor) |
| w336676225 | Sho Gun | 4110 Hampton Lake Way | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://shogunsoutheast.com/louisville-ky/) |
| n6069809469 | Shogun Japanese Steakhouse | 38.21468, -85.59097 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d4230666-Reviews-Shogun_Japanese_Steak_House-Louisville_Kentucky.html) |
| n6069785130 | Shreeji Fast Food | 38.21717, -85.58627 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d15533543-Reviews-Shreeji-Louisville_Kentucky.html) |
| n6069846423 | Sichuan Garden Chinese Restaurant | 38.2256, -85.57587 (Jeffersontown) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.superpages.com/jeffersontown-ky/restaurants) |
| w842731526 | Slammer's Tavern | 38.27687, -85.72991 (Jeffersonville, IN) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g37216-d4637073-Reviews-Slammers_Tavern-Jeffersonville_Indiana.html) |
| n3441763197 | Smiley's Pocket | 2124 South Preston Street | Exact2124SPreston listing has no hours; Feb2026 licensing notice establishes plan, not current operation. [source 1](https://louisvillebarsandrestaurants.com/places/smileys-pocket/) |
| w339058764 | Southside Seafood Resturant | 6810 Southside Drive | Southside Seafood found only in OSM-derived references.  |
| w330558017 | Sow Bistro | 1770 Bardstown Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.yellowpages.com/glenview-ky/take-out-restaurants) |
| n3453099464 | Spaghetti Shop | 38.13843, -85.676 (Okolona) | Generic Spaghetti Shop ordering listing does not sufficiently establish current operation.  |
| w1339619918 | Starlight Coffee | 38.38905, -85.68194 (Clarksville, IN) | Official Starlight location list seen but mapped addressless point not confidently matched; may duplicate another entry.  |
| n7872507457 | Steve O's Italian Kitchen | 38.38403, -85.4388 (Crestwood & Oldham Co.) | Only county directory reference4205W146; current service not established.  |
| w883636923 | Sweet B's | 137 East Market Street | Sweet Bs has a 2025 inspection at 137 East Market; True North has a 2026 inspection at the same address. Sharing versus replacement is unresolved.  |
| n6800735392 | Taj | 38.25332, -85.73769 (NuLu & Butchertown) | January2025 report says indefinitely closed at807E Market with planned move just steps away; no current reopening/address established. Checked in web search on2026-11-18. [source 1](https://www.wdrb.com/news/business/louisville-bar-closes-in-nulu-plans-new-location-just-steps-away/article_1a8acbe8-d03f-11ef-9d5f-c3524f77fc18.html) |
| w336611152 | Taj Palace Indian Restaurant | 2929 Goose Creek Road | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.bizjournals.com/louisville/news/2026/11/06/taj-palace-indian-restaurant-to-relocate.html) |
| n13272377212 | Taqueria Danny | 38.25392, -85.672 (Crescent Hill & Clifton) | TaqueriaDanny delivery listing found but exact mapped point/operating status not sufficiently established.  |
| n3864886581 | TexMex BBQ | 38.32227, -85.47344 (Crestwood & Oldham Co.) | TexMexBBQ exact business not found; similarly named Crestwood restaurants rejected.  |
| n11270589483 | The Comfy Cow | 13301 Shelbyville Road | Exact Middletown listing persists with daily closed-now label, not permanent closure. Official site inaccessible during second pass; cannot independently confirm first pass. [source 1](https://www.tripadvisor.co.uk/Restaurant_Review-g39604-d8731654-Reviews-The_Comfy_Cow-Louisville_Kentucky.html) |
| n6066456089 | The Fish House | 38.23582, -85.72699 (Highlands) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39604-d397554-Reviews-The_Fish_House_Cafe_Beignet-Louisville_Kentucky.html) |
| n7661678885 | The Marque Bar | South 4th Street | Marque Bar has an ambiguous name and addressless map point; current business identity remains unresolved.  |
| n3445787833 | The Starving Artist Cafe & Deli | 8034 New La Grange Road | No reliable exact-location, current evidence established after two passes.  |
| n3363962127 | The Sugar Mamas Bakeshop | 11750 Shelbyville Road | Exact-address independent listing loaded with weekday9AM–1PM and order link; conflicts with first-pass permanent-closure directory. No reliable current evidence settles conflict. [source 1](https://www.restaurantji.com/ky/louisville/the-sugar-mamas-bakeshop-/) |
| w330578742 | The Weekly Juicery | 632 East Market Street | Exact 632 East Market delivery listing is unavailable; this does not establish permanent closure.  |
| n5649559522 | The Yellow Cactus | 2350 Frankfort Avenue | Two exact2350Frankfort delivery listings conflict; one closed onUber. Needs own current confirmation.  |
| n13363819601 | TryMe Treats | 2014 Peabody Lane | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.yellowpages.com/louisville-ky/tasty-treats) |
| w336682486 | Tumbleweed Tex Mex Grill | 3550 Springhurst Commons Drive | Exact Springhurst location unavailable since August 2021; corroborates first-pass locator absence, not independent proof of permanent closure.; Final independent QA: platform departure and absence from locator do not independently prove permanent closure at this exact mapped location. Keep visible flagged. [source 1](https://www.ubereats.com/store/tumbleweed-tex-mex-grill/8DObyO21Tyi_ip-uzSPxoA) · [source 2](https://www.ubereats.com/store/tumbleweed-tex-mex-grill/8DObyO21Tyi_ip-uzSPxoA) |
| w337607804 | Tumbleweed Tex Mex Grill | 8609 Citadel Way | Exact 8609 Citadel historic listing found but no reliable independent current closure/successor evidence. [source 1](https://www.menuswithprice.com/tumbleweed-tex-mex-grill-and-margarita-bar-menu/louisville/8293031/) |
| n6066545286 | Veronica's Mexican Restaurant | 38.08526, -85.66837 (Hillview & Mount Washington) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://veronicasmexrest.com/) |
| n6077278199 | Ville Tacos | 38.21529, -85.62515 (Hikes Point & Buechel) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://www.ubereats.com/delivery/dish/louisville-ky/tacos) |
| n12677619376 | West Point Station Bar and Grill | 37.9985, -85.94615 (Valley Station & PRP) | Samevenue/city listing says CLOSED but exact mapped coordinates/address not independently matched; no confident mapped-site removal. [source 1](https://www.tripadvisor.com/Restaurant_Review-g39973-d33123550-Reviews-West_Point_Station_And_Bar_And_Grill-West_Point_Kentucky.html) |
| w337087095 | Whirlaway Tavern | 2532 South 4th Street | Only historic or OSM-derived Whirlaway references found.  |
| w1093670246 | Zesto's | 38.3185, -85.70852 (Jeffersonville, IN) | Name/location search reviewed, but current operation at the exact mapped point was not established. Missing address, conflicting/stale listings, temporary closure, or insufficient current evidence; retained as unsure. Checked 2026-11-18. [source 1](https://mapcarta.com/W1093670246) |

## Disagreements between passes

This includes successful resolutions of first-pass unsure records, as well as reversed closure claims. Original results and independent recheck files are preserved for audit.

| OSM ID | Name | First pass | Final |
|---|---|---|---|
| w337607798 | McDonald's | unsure | open |
| n4780015155 | Subway | closed | unsure |
| n6069056992 | Subway | closed | unsure |
| w330564804 | Subway | closed | unsure |
| n6069056995 | Starbucks | closed | unsure |
| w329523748 | Burger King | unsure | open |
| w337886842 | Burger King | unsure | closed |
| w339267014 | Burger King | unsure | open |
| n11980061493 | Domino's | closed | duplicate_or_not_a_restaurant |
| w885791119 | Dairy Queen | unsure | open |
| n259306342 | DQ Grill & Chill | unsure | open |
| n11270546820 | DQ Grill & Chill | unsure | open |
| n11980061511 | DQ Grill & Chill | unsure | open |
| n11980061519 | DQ Grill & Chill | unsure | open |
| w329569093 | DQ Grill & Chill | unsure | open |
| w332419078 | DQ Grill & Chill | unsure | open |
| w332453661 | DQ Grill & Chill | unsure | open |
| w334014666 | DQ Grill & Chill | unsure | open |
| w336675930 | DQ Grill & Chill | unsure | open |
| w337709150 | DQ Grill & Chill | unsure | open |
| w339049715 | DQ Grill & Chill | unsure | open |
| w339232540 | DQ Grill & Chill | unsure | open |
| w339255602 | DQ Grill & Chill | unsure | open |
| w339670442 | DQ Grill & Chill | unsure | open |
| w339815791 | DQ Grill & Chill | unsure | open |
| w448289235 | DQ Grill & Chill | unsure | open |
| w456427843 | DQ Grill & Chill | unsure | open |
| w683267172 | DQ Grill & Chill | unsure | open |
| w1291978184 | DQ Grill & Chill | unsure | open |
| w337501562 | Qdoba | closed | unsure |
| w329550775 | Arby's | closed | unsure |
| w337128164 | Arby's | closed | unsure |
| w823994736 | White Castle | closed | open |
| n738651118 | Pizza Hut | closed | open |
| n3446758862 | Pizza Hut | closed | open |
| w329551172 | Pizza Hut | closed | unsure |
| n11980061490 | Chick-fil-A | unsure | open |
| n4755772899 | Heine Brothers' Coffee | closed | unsure |
| w1229645542 | Rally's | unsure | open |
| n6923919232 | Zaxby's | unsure | open |
| w1229646152 | Zaxby's | unsure | open |
| w336682486 | Tumbleweed Tex Mex Grill | closed | unsure |
| w337607804 | Tumbleweed Tex Mex Grill | closed | unsure |
| n3464533100 | Buffalo Wild Wings | closed | unsure |
| w334007680 | Sonic | closed | unsure |
| w335692193 | Sonic | closed | unsure |
| w337528083 | Sonic | closed | unsure |
| n3368978747 | Jersey Mike's Subs | unsure | open |
| n14353775962 | Jersey Mike's Subs | unsure | open |
| n11980061482 | Hardee's | closed | unsure |
| w333996844 | Hardee's | unsure | closed |
| n1712804813 | Little Caesars | unsure | open |
| n11112249555 | Little Caesars | unsure | open |
| w343716083 | Long John Silver's and Taco Bell | unsure | renamed |
| w343474718 | Olive Garden | unsure | open |
| n14003219697 | Jaggers | unsure | open |
| n3446758830 | Potbelly | unsure | open |
| n3373719472 | Smoothie King | unsure | renamed |
| n11270589483 | The Comfy Cow | closed | unsure |
| w330429895 | Shiraz Mediterranean Grill | unsure | open |
| n12678183701 | Freddy's Frozen Custard & Steakburgers | unsure | open |
| n3442159243 | Krispy Krunchy Chicken | unsure | open |
| n14372059284 | Bubba's 33 | unsure | open |
| w1229645294 | Bubba's 33 | unsure | open |
| n6069801089 | Chuck E. Cheese | unsure | open |
| w337698322 | Chuy's | unsure | open |
| n5690588821 | CM Chicken | unsure | open |
| w338402812 | CM Chicken | unsure | open |
| n12381248849 | Cold Stone Creamery | unsure | open |
| w339266954 | Dutch Bros. Coffee | unsure | open |
| w1504055048 | Dutch Bros. Coffee | unsure | open |
| n3447596802 | Firehouse Subs | unsure | open |
| n3452841308 | Firehouse Subs | unsure | open |
| n6034930527 | Honey Baked Ham | unsure | open |
| w337713202 | Hooters | unsure | open |
| w338215070 | Hooters | unsure | open |
| w337696190 | IHOP | unsure | open |
| w821984912 | IHOP | unsure | open |
| w823043724 | Parlor Doughnuts | unsure | open |
| w338213239 | Storming Crab | unsure | open |
| w715684940 | Storming Crab | unsure | open |
| n11957248672 | Taziki's Mediterranean Cafe | unsure | open |
| n6065590288 | Rivue Restaurant & Lounge | unsure | renamed |
| w331282522 | Bluegrass Brewing Company | unsure | closed |
| w333988955 | Bluegrass Brewing Company | unsure | closed |
| w343715283 | Backyard Burger | unsure | open |
| n736821970 | Bonefish Grill | unsure | open |
| n3442884750 | Del Frisco's | unsure | closed |
| n2496184049 | Gigi's Cupcakes | unsure | open |
| n6066622789 | J. Graham's Café | unsure | open |
| n6320809706 | Rapid Fired Pizza | unsure | open |
| n11974171978 | The Peach Cobbler Factory | unsure | open |
| n6066549691 | Le Moo | unsure | open |
| n13248773204 | The Silver Dollar | unsure | closed |
| w337108136 | Marma Dukes | unsure | open |
| n3187693661 | New Wave Burritos | unsure | closed |
| n3395892510 | Oskar's Slider Bar | unsure | open |
| n11919125412 | Preston Boba | unsure | open |
| n13283080840 | Proof Me Wrong Bourbon Bar | unsure | open |
| n4039286231 | The Deuce | unsure | open |
| n13283080839 | The Mint Julep | unsure | open |
| n14018375036 | Asian Buffet | unsure | open |
| w1527363968 | Carali's Rotisserie Chicken | unsure | open |
| n13424045321 | ChillBurger | unsure | open |
| n13925338042 | China Food | unsure | open |
| n6297867439 | Starlight | unsure | open |
| n5716196283 | Topp't | unsure | closed |
| w1444321318 | William's Bakery | unsure | open |
| w1291635957 | Yummy Bowl | unsure | open |
| n5702447325 | Asian Wok | unsure | open |
| n5626565722 | Blue Dog Bakery & Cafe | unsure | open |
| n3364312615 | Bourbons Bistro | unsure | open |
| n7618111885 | Cafe Aroma | unsure | open |
| n5637325726 | Caffe Classico | unsure | open |
| n3364290692 | Caspian Grill | unsure | open |
| w330369907 | Clifton Donut Shop | unsure | open |
| n3364290689 | Crescent Hill Coffee | unsure | open |
| n5643088122 | Eatz Vietnamese Restaurant | unsure | open |
| n3364290686 | Eggs over Frankfort | unsure | open |
| n5702477122 | Gallant Fox Brewing Company | unsure | open |
| n7211744480 | Gelato Gilberto | unsure | open |
| n7619070186 | Great Wall | unsure | open |
| n6629335485 | Hooked on Frankfort | unsure | closed |
| n3364206300 | Miki's Karaoke Bar | unsure | open |
| n12356469168 | New York Pizza Company | unsure | open |
| w330369910 | Ntaba Coffee Haus | unsure | open |
| n5681795914 | Osaka Sushi Bar | unsure | open |
| n6066456090 | Ostra | unsure | closed |
| w330370030 | Pat's Steak House | unsure | open |
| n7461437484 | Porcini | unsure | open |
| n5624467444 | Red Hog | unsure | open |
| n6065590595 | River House Restaurant & Raw Bar | unsure | open |
| n5692588322 | TMP The Manhattan Project | unsure | open |
| n7243510117 | 3rd Turn Oldham Gardens | unsure | open |
| n5218251592 | China King | unsure | open |
| n6069723091 | Double Dragon II | unsure | open |
| n5218203350 | Gustavo's mexican grill | unsure | open |
| n13473479121 | Los Compadres Taqueria | unsure | open |
| n5218198892 | Red Pepper | unsure | open |
| n5218187134 | Rikishi | unsure | open |
| n13850142574 | Wilders Cafe | unsure | open |
| n3372435504 | Abyssinia | unsure | open |
| n3383404342 | Addis Grill | unsure | open |
| n3383404395 | Another Place Sandwich Shop | unsure | closed |
| n3383407651 | Atlantic No. 5 | unsure | closed |
| w331283045 | Bistro 301 | unsure | closed |
| n3383407383 | Brazeiros Churrascaria | unsure | open |
| n3380192627 | Brendon's Catch 23 | unsure | open |
| n6066622788 | City Cafe | unsure | closed |
| n6069056994 | Cravings a la Carte | unsure | open |
| n6065597387 | Dish on Market | unsure | closed |
| n3383405090 | Down One Bourbon Bar & Restaurant | unsure | closed |
| n6800764292 | Ehrler's Ice Cream | unsure | open |
| n6800616486 | Griff's | unsure | renamed |
| n4755754362 | Impellizzeri's Pizza | unsure | closed |
| n3383404391 | Jimmy Can't Dance | unsure | closed |
| n3581286414 | Masala Grill | unsure | open |
| r13931929 | Merlle's Whiskey Kitchen | unsure | open |
| n6069056993 | Mussel & Burger Bar | unsure | open |
| n6065590586 | O'Shea's Public House | unsure | open |
| n7661678685 | Pizza Bar | unsure | open |
| n6069217385 | Queue Cafe | unsure | closed |
| n6328328087 | Safier Mediterranean Deli | unsure | open |
| n6800764196 | The Celtic Pig | unsure | closed |
| n3581286413 | Wei Wei Chinese Express | unsure | open |
| n3383404332 | Yaching's East West Cuisine | unsure | closed |
| n12379116924 | Adrienne and Company | unsure | open |
| n11820469385 | Carr’s BBQ | unsure | open |
| n10543006516 | Sams Food and Spirits | unsure | open |
| n4450998589 | El Tarasco | unsure | open |
| n14201672402 | Hinterhof Rösterie Kaffee | unsure | open |
| n13324770594 | Phalcha | unsure | open |
| w330275519 | Seidenfaddens | unsure | open |
| n3467847352 | Akiko's Restaurant | closed | unsure |
| n3368832060 | Bristol Bar & Grill | unsure | closed |
| n13953138860 | Dragon King's Daughter | unsure | open |
| n3373719479 | I ♥ Tacos | unsure | closed |
| w329933335 | Kashmir Restaurant | unsure | open |
| n3360773527 | Kizito Cookies | unsure | open |
| n6065590591 | La Chasse | unsure | closed |
| n6066622790 | La Peche Gourmet To Go and Cafe | unsure | closed |
| n3368831496 | Lilly's | unsure | closed |
| n9915806511 | Lucky Cat Café and Lounge | unsure | closed |
| n3375256895 | North End Slice | unsure | closed |
| n9915810825 | Panchito's Ice Cream & Taqueria | unsure | closed |
| n3375209377 | Rawnaissance Raw Organic Desserts | unsure | closed |
| w330412601 | River City Drafthouse | unsure | open |
| n3467847353 | Roux | unsure | closed |
| w330555899 | Safai Coffee | unsure | open |
| n3375222882 | Sapporro Grill & Sushi | unsure | open |
| n3363783640 | Sinclair Smoked Salmon | unsure | closed |
| n3368830981 | Somewhere Louisville | unsure | closed |
| n6739141655 | Spinelli's Pizza | unsure | open |
| n6724092871 | Sunergos Coffee | unsure | open |
| n3357102175 | The Bard's Town | unsure | closed |
| n3375222880 | The Bep - Boba Teahouse | unsure | open |
| n3364553593 | The Fat Lamb | unsure | open |
| w329933368 | The Joy Luck | unsure | closed |
| n3363783649 | The Silly Axe Cafe | unsure | closed |
| n3357102192 | Top 1 Korean BBQ & Hotpot | unsure | open |
| w544898832 | Twig and Leaf | unsure | open |
| n6328088885 | Wick's Pizza | unsure | open |
| n6034620203 | Nu-View Bar and Grill | unsure | open |
| n2496186549 | Pastry Plus | unsure | closed |
| n1709000068 | Puerto Vallarta Mexican Restaurant | unsure | open |
| n3467853442 | Bistro Le Relais | unsure | open |
| n3410869493 | El Caporal | unsure | open |
| n12064805337 | El Monstruo Louisville | closed | open |
| n6069620383 | Jock's Bar & Grill | unsure | open |
| n13950417801 | Kathmandu | unsure | open |
| n5269153316 | King Buffet | unsure | open |
| n3447718891 | Shark's Seafood | unsure | open |
| n5269159253 | Sullivan Bakery | unsure | open |
| n14360894702 | El Maguey Mexican Restaurant | unsure | open |
| n12699941573 | Barcelona Bistro | unsure | open |
| w337696182 | Brownies the Shed Grill & Bar | unsure | open |
| n12750423686 | China King | unsure | open |
| n3505153162 | Hometown Pizza | unsure | renamed |
| w337607799 | Mussel and Burger Bar | unsure | open |
| n5239976391 | RecBar | unsure | open |
| n3446735316 | Yellow Cactus | unsure | open |
| n3744913324 | Adrienne Bakery and Cafe | unsure | open |
| w1291783702 | BobaBun Cafe | unsure | open |
| w554300511 | Clucker's | unsure | open |
| n14068590039 | El Sombrero | unsure | open |
| n14068590041 | Food Lab | unsure | open |
| n14068584365 | Golden Blossom Buffet | unsure | open |
| n6750919492 | H.M. Franks | unsure | open |
| w1452705992 | Pearl Street Game & Coffee House | unsure | open |
| n2916114001 | Red Yeti | unsure | open |
| n9878973844 | Bandido Taqueria Mexicana | unsure | open |
| n3445798127 | Corner Cafe | unsure | renamed |
| n3436530764 | Fresh Wok | unsure | open |
| n3447597111 | Heitzman Traditional Bakery and Deli | unsure | open |
| n14183369602 | K- Brunch by Taco N' Madres | unsure | open |
| n6391860105 | Mojito Tapas Restaurant | unsure | open |
| n12179504360 | Osteria Italian Seafood | unsure | open |
| n6392757787 | Thai Cafe | unsure | closed |
| n3443828792 | Z's Oyster Bar & Steakhouse | unsure | closed |
| n3364360694 | Bento Asian Restaurant | unsure | open |
| n2496184629 | Brix Wine Bar | closed | unsure |
| n6069217500 | Carali's Rotisserie Chicken | unsure | open |
| n3364360420 | Clay Oven Indian Restaurant | unsure | open |
| w329510693 | El Toro | unsure | open |
| n11270546819 | Hometown Pizza - Middletown | unsure | open |
| n3363770013 | I Love Pollo | unsure | renamed |
| n3363962171 | Las Margaritas Mexican Cuisine | unsure | open |
| n3364360452 | Samurai Sushi And Hibachi | unsure | open |
| n3363962127 | The Sugar Mamas Bakeshop | closed | unsure |
| w883620479 | Bella Roma | unsure | open |
| w938694179 | Booty's Diner | unsure | open |
| w1057027821 | Casa México Gourmet | unsure | open |
| n11971987458 | Cultivated Table and Sip House | unsure | open |
| n7996383856 | Homemade Ice Cream & Pie Kitchen | unsure | open |
| n7996525067 | Kolkin Coffee | unsure | open |
| w1442471775 | Lady Tron's | unsure | open |
| w1579457340 | Norma Jean's Bakery | unsure | open |
| w938694192 | Paper Dolls Deli | unsure | open |
| w1087711229 | Pastime Grill & Pub | unsure | open |
| w884043542 | Pride Bar + Lounge | unsure | open |
| n490481592 | Rich O's Public House | unsure | renamed |
| n490481591 | Sportstime Pizza | unsure | renamed |
| n11972070184 | True North Coffee House | unsure | open |
| n11981631844 | Yamato | unsure | open |
| n6028042686 | Big Al’s Beeritaville | unsure | open |
| n13424071605 | Tacos Amor | unsure | open |
| n5747716221 | Holy Smokes Bar-B-Que and Catering | unsure | open |
| w336416400 | Ole Hickory Pit Bar-B-Que | closed | unsure |
| w330139956 | Stooge's Bar and Grill | unsure | open |
| n9336873203 | Barry's Cheese Steaks & More | unsure | closed |
| n6066550688 | Dixie Chicken | unsure | open |
| n6066410788 | King's Fried Chicken | unsure | open |
| n9336873204 | Pizza Donisi | unsure | open |
| n2637406501 | Casa Festa | unsure | open |
| w679975629 | Commonwealth Tap | unsure | open |
| n10163894970 | Dragon Cafe | unsure | open |
| n14001203286 | Gustavo’s | unsure | open |
| n14001203287 | King Donuts | unsure | open |
| n4094978329 | 1st Wok Chinese Resturant | unsure | open |
| w1068091564 | Caribbean Cafe | closed | unsure |
| w1068084520 | PIzza King II | unsure | open |
| n6391859989 | Gerstle's | unsure | open |
| n3410741323 | Katrouz Cafe | unsure | open |
| n13671779386 | King Gyros - St. Matthew’s Mall | unsure | open |
| n3814039790 | Lonnie's Best Taste of Chicago | unsure | open |
| n5266510443 | Mama's | unsure | open |
| n14220253175 | Phalcha | unsure | open |
| n6391859998 | Shady Lane Cafe | unsure | open |
| w337191422 | Spinelli's Pizzeria | unsure | closed |
| w337713637 | W.W.Cousins | unsure | open |
| n5770248511 | Catfish Haven Lake Bar & Grill | unsure | open |
| w337423000 | Christy's Restaurant | unsure | open |
| w339268453 | Fuji Asian Restaurant | unsure | open |
| w339254271 | Kathy & Joe's Restaurant | unsure | closed |
| n12677619376 | West Point Station Bar and Grill | closed | unsure |
| w337083175 | Chopsticks House | unsure | open |

## Source access and limits

- JavaScript-only or bot-blocked official locators (notably Burger King, Panera, Dairy Queen and some chain pages) could not always be read directly. Search-indexed official text, exact-address ordering pages, local news, and municipal/university sources were used where available.
- Some local news pages were paywalled or blocked. A source may have been observed in search results rather than loaded in full; evidence notes identify this when relevant. No access blocks were bypassed.
- Cached pages can contradict newer search results or recent news. Conflicts without decisive evidence remain unsure; old directories and expired domains alone were not treated as proof of closure.
- A URL’s presence or syntactic validity is not proof it supports a verdict. The review used observed page/search content. It does not claim a fresh HTTP availability check of every URL in all 1,613 original records.
- Local-news closure inventory is in results/news_closures.json. It is a researched cross-check list, not an exhaustive history of every regional closure since 2018.

## Validation

- Exact ID and ordering comparison for each of 25 batches against inputs.
- Merged key set equals the 1,613-ID worklist; status/confidence/date/schema checks pass.
- Every non-unsure final record has an observed HTTP(S) evidence URL; every renamed record has a successor name.
- All first-pass closed/renamed/nonrestaurant/unsure records have second-pass records. Original evidence is retained in batch files; merged evidence favors the better-supported recheck.
- Build integration, browser checks and deployment are separate from this data review.

## Build and browser validation

- Build output: 1,471 places (1,254 open, 217 unsure), with 122 closed, 14 renamed and 6 duplicate/nonrestaurant entries removed after deduplication.
- Generated IDs exactly match retained verification IDs; no removed IDs survive and no retained IDs are missing.
- All 217 unsure entries are flagged in list/card UI; nearby suggestions also disclose unsure operating status.
- Corrected Haymarket and three Moby Dick Seafood brand matches; unconfirmed ownership is marked `u: true` and never counted as PE-backed.
- Desktop Chromium: map loaded, search, unsure list/card, operating-status link, about dialog, and responsive width checked; zero JavaScript/console errors. Tile requests cancelled during map movement are normal.
- Actual iPhone 17 simulator Safari: rendered map and initial sheet visually inspected; direct-linked Akiko’s unsure card, date, evidence link and mobile sheet layout visually verified. Safari’s console was not separately instrumented.
- Added an inline favicon to remove the pre-existing favicon.ico 404. No packages were downloaded.

The consolidated second-pass result is `results/recheck.json` (603 unique IDs); the separate reviewer files preserve intermediate opinions.

## Addendum — 18 November 2026 recheck

Applied after the review above. These supersede the table where they differ.

- Texas Roadhouse on Outer Loop (`w338228210`) stays **closed**: the restaurant closed 15 Nov and its replacement at 3201 Brooke Elizabeth Way opens 19 Nov. A mid-review attempt to restore it relied on a stale search summary and was reverted.
- The 14 `renamed` places are kept under their `new_name`, not removed. Cuisine for Tacos D'Amor, Mom's Kitchen and Basilico Cafe is set with a `kind` field because the old OSM tags were wrong. Derby City Pizza (Dundee Road) became `unsure` because a further Parlour swap was announced and current evidence is missing.
- Per the owner's decision, **unsure places are removed, not flagged**: all 217 Codex-unsure places, two weak closures (Wendy's S Floyd, Hardee's Taylor Blvd), Derby City Pizza, and 20 "open" verdicts that had only low-confidence evidence (undated delivery or listing pages). Their evidence stays in `verification.json`; set a place to `open` and rebuild to restore it.
- New or unreviewed OSM IDs are also dropped by the build.
