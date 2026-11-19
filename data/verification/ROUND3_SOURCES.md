# Round 3: official civic sources

Checked directly on **2026-11-18**. These are research inputs; no app data or site changes were made while collecting them.

## Use these local snapshots first

Every file is a JSON object with `source`, `checked`, `row_count`, `fields`, and `records`. Rows in `records` are plain attribute objects. All pages were fetched, ordered by `ObjectId`; permit IDs were unique within each snapshot.

| Snapshot | Rows | Purpose |
| --- | ---: | --- |
| `/tmp/louisville-r3-civic-establishments.json` | 8,520 | Names, split addresses, coordinates, permit state and operation fields |
| `/tmp/louisville-r3-civic-latest-inspections.json` | 7,214 | Last three inspection dates/scores, names and addresses |
| `/tmp/louisville-r3-civic-permitted.json` | 3,441 | Published permitted-establishment list; incomplete compared with other current health tables |
| `/tmp/louisville-r3-civic-abc-state.json` | 5,360 | State alcohol licenses, trade names, addresses, coordinates and expiry dates |

The `/tmp` snapshots are temporary and are not deployed or committed. Downloaded data totaled about 12 MB. An untracked image already present in the repository was left untouched.

## 1. Establishments with coordinates

[Observed live schema](https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Environmental_Health_Bulk_Data_Establishments/FeatureServer/0?f=pjson)

```text
https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Environmental_Health_Bulk_Data_Establishments/FeatureServer/0
```

This is a **table**, not a geometry layer. Coordinates are attributes: lowercase `latitude` and `longitude`.

Useful live fields:

- Identity: `EstablishmentID`, `PremiseName`.
- Address: **`PermiseStreetNo`** (the API really uses this misspelling), `PremiseStreet`, `PremiseExtraAddrLine`, `PremiseCity`, `PremiseState`, `PremiseZip`.
- Permit: `Status`, `RenewalStatus`, `permit_expiration_date`, `opening_date`.
- Operation: `IsCaterer`, `IsTrucksOnly`, `HoursOfOperation`, `DaysOfOperation`, `MonthsOfOperation`.

The service data timestamp was **2026-11-18 13:44 UTC**. Every returned establishment had `Status=ACTIVE`; renewal states included `RCVD`, `SENT`, `N/A`, and null. Do not interpret renewal-mail state as restaurant operating status. Hours fields were null for the sampled Panera records.

Only **4,938 of 8,520** rows had coordinates inside the app's bounding box. For example, Panera at 3131 Poplar Level had longitude **0**. Reject zero, null and out-of-area coordinates; even plausible coordinates can be inaccurate.

### Tested name lookup

Append `/query` to the base endpoint and URL-encode these parameters:

```text
where=UPPER(PremiseName) LIKE '%PANERA%'
outFields=EstablishmentID,PremiseName,PermiseStreetNo,PremiseStreet,PremiseCity,Status,RenewalStatus,permit_expiration_date,latitude,longitude,HoursOfOperation,DaysOfOperation,IsTrucksOnly
returnGeometry=false
resultRecordCount=4
f=json
```

The query returned, among others, permit **64736**, `PANERA BREAD #826`, **6221 DUTCHMANS LN**, coordinates **38.2306, -85.6396**, active permit. This is a source example, not a new verification verdict.

### Tested coordinate-window lookup

Because this is a table, use numeric fields rather than a spatial `geometry` query:

```text
where=latitude BETWEEN 38.24 AND 38.26 AND longitude BETWEEN -85.76 AND -85.73
outFields=EstablishmentID,PremiseName,PermiseStreetNo,PremiseStreet,Status,latitude,longitude
returnGeometry=false
resultRecordCount=3
f=json
```

This returned establishments including Galt House, Dryden Provision and Econo Lodge. For a blank-address OSM point, select nearby candidates, compute actual distance locally, then require compatible names and premises. A broad window is only candidate generation. Use the task's approximately 150 m threshold when evaluating a move, accounting for bad geocodes.

## 2. Latest three inspections and current permits

[Latest-three schema](https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Inspection_Results_Food_Service_Establishments/FeatureServer/0?f=pjson)

```text
https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Inspection_Results_Food_Service_Establishments/FeatureServer/0
```

Fields include `permit_number`, `premise_name`, `premise_address`, `premise_city`, `premise_state`, `premise_zip`, `DateRecent`, `ScoreRecent`, `GradeRecent`, `Date2`, `Date3`, `opening_date`, `facility_type_description`, and `subtype_description`.

Join **`permit_number = EstablishmentID`** to the coordinate table. Dates here are Unix milliseconds; convert to the Louisville timezone before displaying a calendar date. The most recent `DateRecent` anywhere in this snapshot was **2026-11-13**. The service data timestamp was November 18, but that is a publication timestamp, not an inspection of every business that day.

This snapshot contains 3,613 food-service establishments, 2,517 temporary food-service establishments, 490 retail food stores, 479 retail/food establishments and 115 restricted concessions. Do not assume every permit is a public restaurant.

[Current-permit schema](https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Permitted_Food_Service_Establishments/FeatureServer/0?f=pjson)

```text
https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Permitted_Food_Service_Establishments/FeatureServer/0
```

This has the same permit/name/address identifiers, facility/subtype descriptions, `EHS`, and `opening_date`, but no inspection dates or coordinates.

**Coverage check:** its live `returnIdsOnly=true` response contained exactly 3,441 object IDs, all present in the snapshot; pagination is complete. Nevertheless, this source contains only 2,672 records classified as food-service establishments and omits **941** food-service permits present in the latest-inspection table. For example, Mike Linnig's Restaurant (permit 35213), its ice cream shop (127145), and Tiger Sugar (117745) are missing here despite active records and 2026 inspections elsewhere. No exposed service filter explained the difference. The data timestamp was November 18 at 13:50 UTC. Treat membership as positive corroboration, but absence as inconclusive; prefer the bulk active establishment table joined to latest inspections.

### Full inspection history for one permit

[Observed history schema](https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Environmental_Health_Bulk_Data_Inspections/FeatureServer/0?f=pjson)

```text
https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/Louisville_Metro_KY_Environmental_Health_Bulk_Data_Inspections/FeatureServer/0/query
where=EstablishmentID=64736
outFields=EstablishmentID,InspectionDate,InspectionType,GradeID,score,ACTION_CODE_DESC
orderByFields=InspectionDate DESC
resultRecordCount=2
returnGeometry=false
f=json
```

Tested successfully: permit 64736 had regular inspections on **2026-08-17** and **2026-03-09**. The history table was not downloaded in full; query only the required permit IDs.

## 3. Current state alcohol licenses

[Observed live schema](https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/ABC_State_ActiveLicenses/FeatureServer/0?f=pjson)

```text
https://services1.arcgis.com/79kfd2K6fskCAkyg/arcgis/rest/services/ABC_State_ActiveLicenses/FeatureServer/0
```

This **is** a point layer. Useful fields: `SiteID`, `DBA`, `Licensee`, `PremisesStreet`, `PremisesCityState`, `Status`, `LicenseNumber`, `LicenseType`, `IssueDate`, `EffectiveDate`, `ExpiryDate`, `Latitude`, `Longitude`. Multiple license/endorsement records can represent one physical restaurant. `Licensee` identifies the licensed entity, not necessarily the beneficial owner or parent company.

Data timestamp: **2026-11-18 13:16 UTC**. Tested query:

```text
where=UPPER(DBA) LIKE '%BRIX%'
outFields=DBA,Licensee,PremisesStreet,Status,IssueDate,ExpiryDate,Latitude,Longitude
returnGeometry=true
outSR=4326
f=json
```

It returned two active BRIX Wine Bar licenses at **12418 La Grange Rd Ste 110**, coordinates **38.289789, -85.5093375**. This can resolve identity/location conflicts but an unexpired alcohol license alone does not establish that a restaurant is serving customers today.

Avoid the similarly named **`ABCActiveLicenses`** service for current-status evidence: its metadata showed data last edited in **2022**, despite schema edits in 2023. `ABC_State_ActiveLicenses` is the current service inspected above.

## Query and interpretation notes

1. These service tables generally cap results at **1,000**. Full downloads used `where=1=1`, `orderByFields=ObjectId ASC`, `resultOffset`, `resultRecordCount=1000`; check `exceededTransferLimit` and count results. Do not mistake a truncated page for absence.
2. Name searches use `UPPER(PremiseName)` in establishments, `UPPER(premise_name)` in latest/current permits, `UPPER(EstablishmentName)` in `FoodServiceData`, and `UPPER(DBA)` in licenses. Escape an apostrophe as two apostrophes inside SQL strings, then URL-encode parameters with `urllib.parse.urlencode`.
3. The old [Restaurant Inspection Scores catalog](https://catalog.data.gov/dataset/louisville-metro-ky-restaurant-inspection-scores) describes latitude/longitude, but live `FoodServiceData/FeatureServer/0` has **neither coordinate fields nor geometry**. Its `InspectionDate` is a string, unlike the date fields in the bulk history and latest-three tables. Prefer the coordinate establishment table joined to latest inspections.
4. These health datasets cover Louisville/Jefferson County. They do not establish absence or closure in Southern Indiana, Bullitt or Oldham counties. A missing name, missing coordinate, stale permit, old inspection or new permit holder needs another source before a removal verdict.
5. A recent inspection plus active permit, exact business/address match and current official hours or ordering is much stronger than any one signal. A different DBA at the same address is a lead for a replacement/rename, not automatic proof that the older business closed; shared kitchens, hotel outlets and concessions can coexist.

## Access observations

The web-search connector located the official catalogs but could not render direct ArcGIS JSON endpoints. Ordinary sandbox Python also lacked DNS access. Read-only HTTPS requests using Python's standard-library `urllib.request` succeeded with the approved network execution path. No packages were installed and no service data was modified.
