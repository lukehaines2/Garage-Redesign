# V4 mapping feasibility

Checked 23 September 2026. Billeaford Hall, Sloe Lane, Knodishall, IP17 1UU. Private household garage. This is a research decision note; no application map has been issued.

## Recommendation

Use QGIS for the measured site master and fixed-scale PDF layouts. Update from Dad at 17:06: only the unmarked screenshot exists, so original Promap recovery is closed. Dad proposes obtaining new licensed mapping; confirm coverage, scale and reuse rights before adopting it, and combine it with verified site measurements. If it is unsuitable, compare an adequately detailed open-data/survey route with a small licensed mapping purchase. Do not buy anything until the required extent and rights are known. A free-only submission cannot yet be promised.

The existing screenshot can explain which buildings Dad means, but it has no usable scale, north reference or licence details. Changing its colours or tracing it does not establish accuracy or remove its source rights.

## 1. Authority and application route

East Suffolk is the district planning authority to use for this confirmed location. Suffolk County Council handles minerals, waste and its own developments; it may have a highways role but is not the ordinary domestic-garage application authority. [Suffolk County Council](https://www.suffolk.gov.uk/planning-waste-and-environment/planning-applications/submit-a-planning-application)

Working route: a householder application for a replacement domestic outbuilding and associated works, provided the garage/driveway are within the lawful residential curtilage. Confirm curtilage, planning history and designations before fixing that route. Enlarging domestic curtilage or a material change of use needs a different assessment. The five drawing groups in Ben's list remain appropriate. Tree/ecology/heritage and level information depend on actual site impacts. The current householder chapter is V2, January 2026. [East Suffolk householder guidance, pp. 1-2 and 11-13](https://www.eastsuffolk.gov.uk/sites/default/files/2025-12/Local%20Validation%20Guidance%20Chapter%201.pdf)

S17 update: Dad asks for a low building within the relevant permitted-development limit. Assess Class E eligibility before fixing the application route; the height answer and slope/boundary dependencies are in [HEIGHT_AND_CONSTRUCTION.md](HEIGHT_AND_CONSTRUCTION.md). A householder application remains a possible fallback. Neither the property's eligibility nor a final ridge height is confirmed.

The council's current validation webpage identifies the Local Validation List 2024, effective 1 May 2024. Older 2014 Suffolk Coastal checklists still appear in search results; they were not used as the controlling list. [Current validation page](https://www.eastsuffolk.gov.uk/planning-and-building-control/planning-applications/local-validation)

## 2. Must the maps be bought from an OS partner?

No blanket OS-only purchase rule was found. Section 2.11.1 expressly permits licensed OS mapping, equivalent mapping, or a topographical survey for site plans. Section 2.61.1 makes OS licence details conditional on using OS data. Site plans use 1:500 or 1:200; location plans use 1:1250 or 1:2500. Required presentation includes north, identifying titles, drawing/revision/date information; site plans need a scale bar. We will include one on every scaled sheet. Accurate electronic drawings or correctly scaled scans are acceptable; photographed plans are not.

The location-plan red line includes development and access to the highway; nearby additional ownership/control is blue. Section 2.11 does not separately impose a universal blue-line rule on every site sheet. Our site sheets will carry the same relevant boundaries, with the wider ownership extent on the location sheet. The site drawing must show relevant buildings, trees, surfaces, drainage, parking and boundaries. These findings do not certify any particular alternative dataset. [Local Validation List, sections 2.11 and 2.61, printed pp. 25-27 and 138-144](https://www.eastsuffolk.gov.uk/sites/default/files/2025-10/Local%20Validation%20List.pdf)

**Building names:** label the named buildings Dad requested to make identities unambiguous. The guidance establishes the need to explain site layout and building uses; it does not prescribe this exact list of names. A numbered key can prevent crowded labels. [Planning Portal drawing guidance](https://www.planningportal.co.uk/planning/planning-applications/supporting-document-types/plans-and-drawings/)

## 3. Mapping options: rights and fitness are separate checks

| Source | Reuse position | Fitness for this project |
|---|---|---|
| Existing Promap | Check original order, product, licence holder, permitted copying/export, duration and attribution. Possession of a screenshot does not answer those questions. | Original unavailable, confirmed by Dad at 17:06. Screenshot remains reference-only. |
| OpenStreetMap | Open data under ODbL with attribution and applicable database obligations; tile providers have separate service terms. | Candidate context source, not automatically an accurate boundary/building survey. Check actual local coverage; do not invent absent features. |
| OS OpenMap Local | Free open mapping, with its applicable attribution/licence. | OS describes a generalised 1:10,000 product. Enlarging to 1:2500 or 1:500 does not add missing detail. Use for context assessment, not as the sole unverified block-plan base. |
| HM Land Registry INSPIRE | The current dataset page permits reuse under OGL with HMLR and OS attribution. | Indicative registered-freehold polygons; not a building basemap or proof of exact ownership extent. Title evidence and Dad's confirmation remain necessary. |
| Council planning portals | Public inspection is not evidence of a right to republish someone else's drawings/maps. Check the actual document's copyright/licence and provenance. | Useful for planning history and finding original surveys; do not assume an old neighbouring plan is current or belongs to this project. |
| Measured survey | Establish the source/ownership of the measurements and any underlying mapping. | Suitable route if sufficiently complete and accurate. DIY measurements can fill clear, accessible gaps; complex levels, trees or uncertain boundaries may need specialist input. |

Sources for the table: [Promap OS terms](https://www.promap.co.uk/ordnance-survey-terms-and-conditions/), [Promap export guidance](https://www.promap.co.uk/support/how-do-i-create-a-pdf-or-image-in-promap/), [OpenStreetMap licence](https://www.openstreetmap.org/copyright), [OS OpenMap Local specification](https://www.ordnancesurvey.co.uk/products/os-open-map-local), [current INSPIRE conditions and limitations](https://use-land-property-data.service.gov.uk/datasets/inspire). Portal reuse remains unverified for any particular document; it is not selected as our production source.

## 4. Free software and accurate annotations

**QGIS is the selected mapping workflow.** Use a British National Grid (EPSG:27700) project in metres, retain each source's real CRS, and use correctly transformed/georeferenced data. Store application boundary, other ownership, buildings, proposed footprint, access, hardstanding, trees and labels as separate editable layers. Keep unverified features distinct from checked measurements. QGIS is not installed in the current project runtime; setup is deferred until the base arrives.

Create a print layout, set its paper size, add a map item, enter the exact scale and lock its extent/layers. Link the scale bar and north arrow to that map item. Add title, revision, date, status and source/licence notes. Export PDF. QGIS supports explicit map scale, rotation, CRS and locked layers. [QGIS current map-item documentation](https://docs.qgis.org/3.44/en/docs/user_manual/print_layout/layout_items/layout_map.html)

Use Inkscape for optional vector presentation only, preserving document dimensions. Keep the existing Python/Blender workflow for the building geometry and drawings. Canva is unnecessary here: adding another layout/resizing step creates work without resolving measurement or mapping accuracy.

Use monochrome/light grey context with coloured boundary overlays and distinct proposed/demolition line styles. Different source colours are a presentation issue, not evidence of invalidity. Do not erase source acknowledgements when restyling.

## 5. Paper size, scale and file format

Target 1:2500 for location and 1:500 for the paired site plans, with a 1:200 detail sheet if needed. Use A4 if the required extent fits clearly, otherwise A3. The full ownership extent is not yet known, so a final paper choice is premature. National guidance recognises A4/A3 and typical 1:1250/1:2500 location scales. [Government planning guidance](https://www.gov.uk/guidance/making-an-application)

The following are calculated examples of map-frame coverage, not measurements of this estate:

| Landscape page | Example usable map frame | At 1:2500 | At 1:500 |
|---|---|---|---|
| A4, 297 x 210 mm | 260 x 160 mm | 650 x 400 m | 130 x 80 m |
| A3, 420 x 297 mm | 380 x 240 mm | 950 x 600 m | 190 x 120 m |

Formula: ground metres = paper millimetres x scale denominator / 1000. Export a true-size vector PDF; PNG is a preview, not our submission drawing. Print at actual size/100%. A 100 m scale bar at 1:2500 must measure 40 mm; a 20 m bar at 1:500 must also measure 40 mm. A4/A3 alone does not guarantee correct scale.

## 6. Driveway, new building and AI

Dad can provide a rough marked sketch to establish intent. Accurate drafting then requires measured widths, corner offsets, ties to stable features and levels. Enter those measurements into the mapping/model system. AI can help generate consistent vector geometry from explicit data; it cannot recover survey accuracy or ownership from a description or screenshot.

Record the driveway's route, width, turning area, surface/colour, permeability, edges, drainage and whether the highway entrance changes. East Suffolk's hard-surfacing guidance requires dimensional/material information; an altered highway access introduces additional access/visibility information. [Householder guidance, pp. 43 and 46](https://www.eastsuffolk.gov.uk/sites/default/files/2025-12/Local%20Validation%20Guidance%20Chapter%201.pdf)

## 7. Paid fallback - no purchase authorised or made

If no reusable base works, obtain appropriately licensed map coverage after boundaries are known. Illustrative published BuyAPlan prices checked today: A4 1:500, 90 x 90 m, GBP 16.49; A4 1:2500, 16 hectares, GBP 86.99; A3 1:500, 128 x 128 m, GBP 30.99. Prices are excluding VAT; the headline GBP 7.89 product is a much smaller 1:200 extent. These are examples, not a quote or recommendation to buy those extents. Check current price, licence and permitted adaptation at selection. [Prices](https://www.buyaplan.co.uk/prices), [licence](https://www.buyaplan.co.uk/license)

## 8. Decision and next handoff

Research is complete enough to select the workflow, but the mapping source is conditional. Dad confirms only the screenshot is available and proposes obtaining a new licensed map. Next: inspect the new file/rights, confirm boundaries/access and measured proposal positioning, then build the master. Dad's approximately GBP 20-25 estimate is not a verified quote or purchase authorisation. No location/site plan is issued until those checks and the agreed site review are complete.

Remaining project checks: lawful domestic curtilage, site planning history/designations, source suitability/licence, north/positions/levels, tree and drainage impacts, building dimensions and roof decision. No contact with council, suppliers or consultants has been made.
