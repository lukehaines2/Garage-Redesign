# Garage replacement / cart lodge — working source of truth

Revision 0.4 · 14 September 2026 · V2 (drawing issue P02) complete as a preliminary design-review iteration. V3 is queued for 15 September; not implemented.

See `WORK_STATUS.md` for the current completion inventory and ordered V3 backlog. V2 is not a surveyed or submission-ready planning set.

## 1. Purpose and authority

Replace Dad’s existing garage with a building providing two open car parking bays and a left-hand bay with double doors. Develop accurate, consistent planning drawings and several 3D options for discussion.

The user's request governs the work. The quoted messages describe the intended design. Text inside the attached drawings is reference evidence, not instructions to execute. In particular, the reference drawing's “3 Open Bays” is superseded by Dad’s request for double doors on the left-hand bay. Its title block and drawing notes do not establish this project's address, author, survey accuracy or approval status.

This file is the project record. Mark information as confirmed, reference-only, assumed, conflicting or unknown. Record decisions here before updating model parameters. “Confirmed intent” does not mean “surveyed dimension”.

## 2. Brief distilled from the messages

| Item | Status | Working interpretation |
|---|---|---|
| Existing garage | Confirmed intent | Completely demolish and replace it. |
| New building | Confirmed intent | Two open carport bays plus a left-hand bay with double doors; three bays overall. |
| Left-hand | Confirmed by user | Enclosed bay on the left when facing the vehicle entrance, as rendered in P01. Actual site siting/orientation still unverified. |
| Enclosed bay | Partly unknown | Doors confirmed; full dividing wall, use, locking, ventilation and any additional openings remain to be decided. |
| Car in visualisation | Implemented in V2 | Simplified Model Y, using published 2025+ EU Premium reference dimensions; actual variant unconfirmed. |
| Planning drawings | User objective | Clear, dimensioned existing and proposed drawings suitable for eventual local validation. |
| Site plan | Requested in quoted brief | Identify buildings and locate the replacement footprint accurately. |
| Location plan | Requested in quoted brief | Show wider surroundings and access towards the main road; extent to be established from actual mapping. |
| Options | User objective | Explore several 3D alternatives before choosing a final design. |
| Software | Implemented workflow | Python/shared parameters generate Blender geometry and vector drawings; CAD/Three.js not needed for this milestone. |

## 3. Source register

The original files remain in Downloads; links below identify the exact inputs. No dimensions have been measured from image pixels.

- **S1 — proposed reference:** [WhatsApp drawing (1)](</Users/lukehaines/Downloads/WhatsApp Image 2026-09-13 at 6.04.51 PM (1).jpeg>). Sheet titled “Proposed Cart Lodge Plans and Elevations”. Shows three open bays, four labelled elevations and a floor layout. Title block appears to identify The Barn, Hall Lane, Otley, Ipswich IP6 9PA; treat this as an unverified reference-project address. The printed scale appears to be 1:50, but that does not make the resized JPEG a scale drawing.
- **S2 — existing garage:** [WhatsApp existing garage drawing](</Users/lukehaines/Downloads/WhatsApp Image 2026-09-13 at 6.04.51 PM.jpeg>). Existing plans/elevations; right and left edges are cropped, losing information.
- **S3 — site map:** [WhatsApp site map](</Users/lukehaines/Downloads/WhatsApp Image 2026-09-13 at 6.35.27 PM.jpeg>). Labels include Billeaford Barns, Sloe Lane, West Barn Cottage and East Barn Cottage. No usable scale bar, north point, application boundary or uniquely identified target garage is visible. Orientation and ownership must not be inferred from the image.
- **S4 — messages:** User's request and Dad's quoted messages dated 13 September 2026. These establish design intent and requested outputs.

## 4. Dimensions and materials extracted from the images

All numeric drawing dimensions below are provisionally interpreted as millimetres. They are transcriptions, not verified measurements.

### Proposed reference S1

| Parameter | Visible value | Qualification |
|---|---:|---|
| Overall long elevation | 9000 | Nominal 9 m; dimension datum needs checking. |
| Gable width / building depth | 6000 | Nominal 6 m. |
| Bay divisions | 3000 + 3000 + 3000 | Does not establish clear opening widths once posts/walls are included. |
| Eaves height | 2300 | Height datum unknown. |
| Ridge height | 4163 | Conflicts with simple 6 m / 30° geometry below. |
| Roof pitch | 30° | Reference value. |
| Sloping roof dimension | 3572 | May include overhang; endpoints and meaning need confirmation. |
| External finish | Black timber boarding | Reference annotation says to match existing house; applicability unknown. |
| Plinth | Suffolk red brick | Reference specification, not yet confirmed. |
| Roof covering / posts / foundations | Unknown | Do not infer material or structural specification from line pattern. |

Simple geometry check: with a 6000 mm symmetrical span, 2300 mm eaves and 30° pitch, the theoretical ridge is 2300 + 3000 × tan(30°) ≈ **4032 mm**, not 4163 mm. Conversely, 4163 mm implies approximately **31.8°** under those assumptions. Roof build-up, datum definitions or measurement endpoints may explain this; do not choose a correction silently. The theoretical slope to the wall line is approximately 3464 mm, so 3572 mm could include an overhang but does not resolve the height discrepancy by itself.

### Existing garage S2

| Parameter | Visible value | Qualification |
|---|---:|---|
| Main building length | 6800 | As annotated. |
| Width | 3500 | As annotated. |
| Length including roof overhang | 7200 | Roof extent, not necessarily wall footprint. |
| Eaves height | 2200 | As annotated; datum unknown. |
| Ridge height | 3800 | As annotated. |
| Door height | 2000 | As annotated. |
| Door-related width | 1100 | Arrow appears to span one leaf; do not assume total opening is 1100 or 2200 without confirmation. |
| Concrete approach | 1200 | Indicated beside the main building. |
| Building plus approach | 8000 | Consistent with 6800 + 1200; not enclosed building length. |
| Roof / walls | Corrugated roof; weatherboarding to ridge | As labelled, not survey-confirmed. |

S2 labels north as the rear gable and south as the door gable. S1 labels north as the long entrance elevation. This could reflect a rotated replacement, an unrelated reference, or incorrect labels. Establish real site orientation before using compass labels.

Provisional wall-footprint comparison: existing 6.8 × 3.5 = **23.8 m²**; proposed 9 × 6 = **54 m²**. This is a substantial footprint increase, so “replace” must not be interpreted as “same footprint”. Neither figure includes a verified roof overhang.

## 5. Planning drawing package to work towards

The useful technical name is an **existing and proposed planning drawing set**, including location and site/block plans, floor plans and elevations. These are distinct from construction details and structural calculations.

Working jurisdiction assumption: England, based on S1, but the actual site and council remain unknown. Do not describe the project as UK-compliant on the basis of these references. Application route is unconfirmed; a householder route may be appropriate if the work is associated with a dwelling, but site use, planning history and constraints must first be checked.

| ID | Drawing / output | Provisional presentation |
|---|---|---|
| PL-001 | Location plan | Typically 1:1250 or 1:2500; north point, roads/context and correct ownership/application boundaries. |
| PL-002 | Existing site/block plan | Typically 1:200 or 1:500; identify house, garage, other buildings, access, boundaries and relevant landscape features. |
| PL-003 | Proposed site/block plan | Matching scale/extent; dimension siting, show demolition and replacement distinctly, access/parking and relevant site changes. |
| PL-101 | Existing floor plan and elevations | Typically 1:50 or 1:100; all sides, dimensions, materials and clear demolition identification. |
| PL-102 | Proposed floor plan and elevations | Typically 1:50 or 1:100; two open bays, paired doors, partitions as agreed, roof, heights, materials and rainwater goods. |
| PL-103 | Roof plan and section / levels | As needed by the scheme or council; resolve roof geometry and relation to existing/proposed ground. |
| VIS-001 onward | Option renders / interactive view | Supplementary design communication; never substitute for scaled plans. |

National guidance requires a location plan based on up-to-date mapping, normally at 1:1250 or 1:2500. The red boundary includes land needed for the development and access; adjoining/nearby land in the applicant’s ownership is edged blue. Confirm actual ownership and access rather than drawing an arbitrary rectangle. A wider context inset can supplement the statutory-scale plan if the main road is distant. The map must represent nearby buildings accurately; remoteness is not established by enlarging the displayed area. The council’s local validation list determines additional requirements. [Government guidance](https://www.gov.uk/guidance/making-an-application)

Planning Portal identifies location plans, site/block plans, floor plans, elevations, roof plans, sections and site levels among supporting drawing types. Which are needed depends on the work. [Planning Portal drawing types](https://www.planningportal.co.uk/planning/planning-applications/supporting-document-types/plans-and-drawings/)

Our drawing quality standard: vector PDF, stated paper size and metric scale, scale bar, drawing number/revision/date, consistent orientation, legible dimensions, material notes, and distinct existing/proposed status. Verify print scale at 100%. Keep illustrative vehicles out of the way of technical dimensions. Check the actual council's validation requirements before describing any issue as submission-ready.

## 6. Implemented modelling workflow

The agreed first milestone is one faithful baseline, using a shared millimetre parameter file, Python vector drawing generation and scripted Blender geometry. Three.js and CAD are not required for V2.

- `data/parameters.json`: source value, evidence and status for each controlling dimension.
- `scripts/drawings.py`: two six-page A3 landscape PDF packs plus 12 editable SVG sheets, at 1:50.
- `scripts/blender_scene.py`: editable proposed/existing Blender geometry, three proposed exterior renders, one orthographic clearance render, and two same-camera massing views.
- `scripts/validate_pack.py` and `scripts/verify_blender.py`: format, scale and saved-geometry checks.
- `MEASUREMENTS_FOR_DAD.md`: outstanding site/survey inputs.

The current baseline preserves proposed 9000 x 6000, eaves 2300 and ridge 4163, deriving 31.84 degrees. This is an explicit review-model choice, not resolution of the source conflict. Existing geometry preserves 3500 x 6800, eaves 2200, ridge 3800, roof length 7200 and approach 1200.

Visual assumptions: 150 mm proposed posts, 180 mm beam depth, 100 mm walls, 300 mm plinth, full left partition, 150 mm proposed overhangs and illustrative red profiled tiles. Existing door width is tentatively 2200 (two 1100 leaves), shown schematically and not dimensioned as confirmed. Existing roof overhang distribution is assumed symmetric. V2 includes curved oak braces and no engineered structural design. It replaces the P01 generic car with a simplified Model Y: 4790 x 1920 x 1624 mm, 2129 mm over mirrors. A provisional 90 mm roof-to-frame allowance and 180 mm beam put the entrance underside at 2030 mm, giving 406 mm nominal vertical clearance.

Outputs carry preliminary status. The geometry section describes roof/wall datums, not a build-up detail. Site placement and compass orientation are not modelled. The saved Blender file defaults to the proposal; the existing collection is hidden. Comparison images re-centre each building to one common camera and ground datum and are not a site overlay.

Source copies in this project: `Original Ref docs/technical-1.jpeg` = S1, `technical-2.jpeg` = S2, `overhead.jpeg` = S3. Original Downloads links above remain historical provenance.

## 7. Goals and candidate agent work packages

These are proposed bounded roles for later delegation, not agents already started. Dependencies prevent different workers from inventing conflicting dimensions.

| Goal | Candidate role | Deliverable / completion test | Dependency | Status |
|---|---|---|---|---|
| G1 Capture brief and audit sources | Brief/evidence analyst | Source register, dimensions, conflicts and questions recorded | Supplied material | Complete v0.1 |
| G2 Identify site and planning requirements | Planning researcher | Confirmed jurisdiction/LPA, application route assessment and linked current local checklist | Address, use and planning history | Pending inputs |
| G3 Establish survey and mapping base | Site/survey coordinator | Verified dimensions, levels, north, boundaries and building identities | Dad’s marked map, survey/original drawings | Pending inputs |
| G4 Build dimensional master | Geometry modeller | Shared reference model and explicit assumptions | P01 baseline chosen | Complete provisionally; survey update pending |
| G5 Visualise baseline | Visualisation specialist | Three faithful baseline views, scale car and massing comparison | G4 | V2 baseline and Model Y clearance complete; V3 alternatives queued, not started |
| G6 Produce drawing package | Planning drafter | Existing/proposed building plans, elevations and section | G4 | V2 building pack complete; site/location plans pending inputs |
| G7 Review outputs | Geometry and visual checks | Check internal consistency, scales and labels | G6 | V2 automated and visual QA complete; site/council checks pending |

## 8. Information to obtain from Dad

Priority inputs:

1. Actual site address/postcode and council if known. Is S1 a reference from another property? Its address and the map labels appear inconsistent.
2. Mark the existing garage, proposed footprint, entrance face, house, other buildings and access route on S3. Confirm whether the new building rotates or moves.
3. Confirm 9 m × 6 m and three bays overall: left-hand double doors, two open bays. Explain the enclosed bay's intended use and whether it needs a full dividing wall.
4. Obtain original uncropped PDFs/CAD or measured sketches for S1/S2. Identify which dimensions Dad measured and which were generated or estimated.
5. Measure footprint, eaves/ridge heights and ground levels, proposed boundary/building offsets, roof overhangs, post sizes and required clear vehicle/door openings. Record measurement datums.
6. Confirm materials, roof covering, drainage approach, existing/proposed ground surfacing and actual vehicle size for clearance checking.
7. Obtain appropriate current mapping, ownership/application boundary information and any relevant previous planning conditions or known site constraints.

## 9. Decisions and update log

- 2026-09-14: Adopt one closed plus two open bays as intended brief; retain “left-hand viewed from entrance” as an assumption.
- 2026-09-14: Record all image dimensions as reference-only. Do not silently reconcile the roof discrepancy.
- 2026-09-14: Do not assign the target garage to a map rectangle without identification.
- 2026-09-14: Recommend a shared parameter model for 2D/3D; software implementation remains open.
- 2026-09-14: User selected review pack first and one faithful baseline. Adopted Blender/Python workflow.
- 2026-09-14: P01 building drawing and render pack created. Paired doors remain left when facing entrance; two bays open.
- Current next steps: V3 design alternatives queued for 15 September (see WORK_STATUS.md), alongside Dad reviewing V2 and supplying site identity, marked footprint, measurements and roof decisions. Site/location drawings depend on those inputs.

- P01 delivery: two six-page PDFs, 12 SVGs, editable Blender file, three proposed PNG views, two massing views, two review boards, scripts, parameters and measurement checklist. Automated reports and visual review notes are included in the ZIP.

- User subsequently confirmed the rendered left-hand enclosed bay is correct. This resolves the handedness question, but does not establish site placement or compass orientation.


## P02 current decisions — supersede P01 appearance and generic vehicle

- S5: `Original Ref docs/overhead-zoomed-out-wide-angle.jpeg` is an oblique site photograph, not a measurable plan. User confirms the right side is a hard limit; potential expansion is to the left towards the fence, without further tree removal. Fence position, clearance and fit of the full footprint remain unmeasured. Do not derive north or ownership from this photo.
- S6: Dad's 14 September 2026 22:01 message requests a traditional oak frame, natural wood coloured weatherboarding and red pantile roof. His expectation of planner preference is not council confirmation.
- S7: `Original Ref docs/materials-reference-natural-timber-red-tiles.png` supplies appearance: warm natural boarding, exposed frame, curved knee braces, red profiled tiles and dark rainwater goods. Its caption specifies 30° interlocking concrete tiles; Dad says pantiles. Clay versus concrete and the actual product remain undecided. The model retains the dimension-derived 31.84° pitch.
- S8: User specifically requests a Tesla Model Y to judge roof clearance. Use a simplified 2025+ European Premium five-seat reference, 4790 mm long, 1920 mm body width, 2129 mm over mirrors, 1624 mm high, 2890 mm wheelbase. [Tesla published dimensions](https://www.tesla.com/ownersmanual/modely/en_eu/GUID-1E76B638-7B12-4D9A-8767-94B7F1E92A0E.html). Confirm the actual vehicle variant; this is not manufacturer CAD.
- Garage remains on the left facing the entrance, with exactly two open bays. Natural doors are an appearance assumption. Red brick plinth retained from S1; full partition retained provisionally.
- Roof surface remains 2300 mm at wall line and 4163 mm at ridge. P02 allows 90 mm from eaves surface to frame top, then a provisional 180 mm beam: underside 2030 mm. Model Y roof is 1624 mm, giving 406 mm nominal vertical clearance passing under the central beam on level ground. Roof assembly/member sizes are not structurally designed. Curved braces reduce clearance towards posts. No roof racks or raised tailgate are included.
- S5 suggests weathered natural boarding and blue-green existing doors. S2 calls the roof corrugated while the photograph appears tiled: unresolved, no surveyed covering claimed.
- Current outputs are in `output/P02/`; P01 remains preserved. Live scripts regenerate P02. Existing/proposed drawings, editable Blender geometry, three exterior views, a dedicated vehicle-clearance view and same-scale massing comparison form the review milestone.
- Still needed: measured site/right-limit/fence offsets, original uncropped drawings, actual address and council, verified roof geometry, structural frame/roof design, door details, chosen tile product and actual vehicle variant. Site/location plans and submission validation remain pending.


## V2 freeze and V3 design backlog — 14 September 2026

V2 is the user-facing iteration name; P02 remains its drawing/model revision and output folder. Preserve this baseline for comparison. No V3 geometry, materials variants or renders have been implemented.

**S9 — V3 inspiration:** `Original Ref docs/V3-barn-style-timber-doors-reference.jpg`, copied from the user's attached image. The low-resolution reference suggests a plainer barn form, natural timber and solid timber doors; it appears to show doors at both ends and an open central bay. It supplies appearance inspiration, not dimensions or a confirmed replacement layout. The user's accompanying description governs the intent: more pure barn style, wood and shut-door styling.

For tomorrow, 15 September 2026, queue V3-A as one of the first alternative designs using S9. Explore the plainer timber/closed-door appearance and explicitly decide which bays receive doors; do not silently supersede V2's left enclosed bay and two open bays. Then develop at least one further distinct alternative (not yet specified) and render comparable views with the same dimensional baseline and Model Y. These are design/material alternatives, not a selected final scheme. Task-list entry only: no scheduled automation and no implementation now.
