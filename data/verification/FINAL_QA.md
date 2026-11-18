# Final independent QA

Reviewed November 18, 2026, before application changes. All 25 batch-result files cover exactly 1,613 unique worklist IDs in input order. No missing or extra IDs, invalid status values, non-unsure verdicts without evidence, or renamed verdicts without a successor name were found. All reviewed recheck IDs belong to the worklist. The merged verification.json was subsequently checked: exactly 1,613 keys, no missing/extra worklist IDs, valid statuses/confidences/dates/pass fields, successor names for renamed entries, and syntactically usable HTTP(S) evidence URLs. The initial merged snapshot had 1,255 open, 215 unsure, 124 closed, 13 renamed and 6 duplicate/nonrestaurant. It still needed the two late Captain D’s/Taco Bell corrections below; parent was notified. Of the checked dates, 610 correctly remain November 17 and 1,003 are November 18. There are 603 second-pass records and 298 first/second disagreements at this checkpoint; counts may change when late QA corrections are applied.

## Corrections caught during QA

1. **Captain D’s, w329550776, mapped 12933 Shelbyville Road: keep unsure.** An expanded Yellow Pages result revealed its permanent-closure label applied to the separate 3801 Oaklawn store, not the 12929 Shelbyville listing. The address-matched Waze title explicitly says **Closed For Remodel**. Restaurantji says CLOSED, but permanence and the 12933/12929 numbering discrepancy remain unresolved. Corrected in recheck_missing_chains.json. [Observed Waze listing](https://www.waze.com/live-map/directions/%28closed-for-remodel%29captain-ds-shelbyville-rd-12929-middletown?to=place.w.179896702.1798901488.1133210).
2. **Long John Silver’s and Taco Bell, w343716083, 1805 Blankenbaker Parkway: renamed to Taco Bell.** Its official Taco Bell location page gives current dine-in and drive-thru hours. The old combined-brand identity is obsolete, but the premises still serve food. Corrected in recheck_missing_chains.json. [Official current location](https://locations.tacobell.com/ky/louisville/1805-blankenbaker-parkway.html).
3. **Skyline Chili, 6801 Dixie Highway: keep unsure.** A research lead for 7105 Dixie Highway was a different Skyline in Fairfield, Ohio. No Louisville relocation can be inferred from it. The wrong-city result was rejected.
4. **Akiko’s initial closure was rescinded.** The parent’s independent recheck found subsequent reporting that the March 2026 shutdown was avoided. The first-pass ind_02 record must be overridden at merge. Vincenzo’s and Mile Wide announced future December 31, 2026 closures and correctly remain open on this review date.

## Residual removal risks

Recommend **unsure** unless stronger exact-location evidence is added:

- **Subway n6069056992, 222 E Witherspoon:** second pass establishes only Uber Eats departure in August 2026 plus official-directory absence. Further searches returned historical maps and general listings, not an independent permanent closure/replacement. [Observed delivery record](https://www.ubereats.com/store/subway-222-witherspoon-aves/JWuHFaftTWuWR_nxIh8ndg).
- **Tumbleweed w336682486, 3550 Springhurst Commons Drive:** only platform departure in 2021 plus locator absence was independently found. A platform’s Closed Since field is not a storefront closure date. [Observed delivery record](https://www.ubereats.com/store/tumbleweed-tex-mex-grill/8DObyO21Tyi_ip-uzSPxoA).
- **Hardee’s n11980061482, 2740 Allison Lane:** first pass found premises available for lease; independent directory describes temporary closure. Conservative final unsure is appropriate without a dated permanent-closure/replacement report.
- **Matt Winn’s Steakhouse n9726086554:** one exact venue directory says permanently closed, but seasonal/race-event access and current Churchill Downs identity were not resolved. Keep unsure; do not generalize the closure of another dining room.

No proposed closure should be approved solely because a URL returns 404. Several old chain verdicts have since gained exact-address closure reports, explicit permanent-closure listings, or replacement-tenant evidence. Bare 404s, expired domains, general directory snippets, and discontinued platform delivery are insufficient by themselves. Current official sites can also be stale: the parent’s Anoosh/Äta review and the rescinded Akiko closure show why later dated evidence matters.

## Merge requirements

- Apply later explicit QA corrections after earlier second-pass records. Preserve the original verdict and disagreement history rather than overwriting provenance.
- Validate exactly 1,613 merged keys, allowed statuses/confidences, usable evidence URLs for non-unsure, dates, successor names for renamed cases, and consistent passes/agree fields.
- The original checked work happened November 17; new searches/rechecks happened November 18. Do not imply that every retained open location received a new independent check on November 18.
- Keep all unresolved entries visible with the user-requested unsure flag. Claims of operating businesses apply at the mapped point, not merely somewhere in the metro area.

No site, build, Git, or deployment changes were made by this reviewer.

## Parent merge refresh

All late corrections were applied before publishing. Final merged counts: 1,254 open, 217 unsure, 122 closed, 14 renamed and 6 duplicate/nonrestaurant (1,613 total). The reviewed build retains 1,471 places. Scholars Coffee remains unsure because public access was not confirmed.
