# Project context for Dad's AI assistant

Snapshot: 23 September 2026. Read this first, then the current decisions at the top of `PROJECT_BRIEF.md`. This pack carries the relevant context from Luke's project; another agent does not need access to the original chat or Luke's computer.

## What Dad and Luke are trying to do

Replace the existing garage at **Billeaford Hall, Sloe Lane, Knodishall, IP17 1UU**, serving the private household. Prepare five coordinated planning document groups: location plan; existing site plan; proposed site plan including the revised driveway/hardstanding; existing floor plan/elevations for demolition; proposed floor plan/elevations. A barn illustration and editable 3D model support review.

The preferred appearance comes from the Radnor Oak reference. Dad accepted the edited V4-01 illustration. The project prioritises free tools and existing material, with licensed mapping to be supplied by Dad. This is a staged DIY drawing workflow; construction details and structural design still need competent professional input before building.

## Decisions already made

| Topic | Current direction |
|---|---|
| Footprint | 9 x 6 m, confirmed design intent; site fit still to be measured. |
| Entrance | East-facing. “Left bay” means left when looking at the entrance from outside. |
| Layout | Three equal bays; left bay enclosed with paired doors and a full dividing wall; two open bays. |
| Timber | Natural finish for frame, weatherboarding and doors. |
| Roof | Red clay pantiles; exact product and roof geometry unresolved. |
| Framing | Interior framing visible; external framing on the enclosed end covered by weatherboarding. |
| Plinth | Three brick courses preferred, with flexibility if lowering the building requires reconsideration. |
| Height | Keep the building as low as practical under the applicable planning route. Final ridge/eaves/pitch not selected. |
| Vehicles | Ignore particular vehicles; equal spans. Old Tesla-specific images are historical. |
| Construction | General builder coordinating the trades and hand-building to coordinated drawings. |
| Ground | Dad estimates 300-400 mm fall towards the courtyard centre; exact extent and measured levels not supplied. |
| Landscape | Existing intention is no further tree removal; physical constraints need measuring. |

## What is actually in the current model

`output/V4/model/garage-V4-review.blend` is the editable V4 **review model**, created with Blender 4.5.10 LTS. The `.glb` beside it is a portable export. Geometry and procedural materials are embedded; it has no linked asset dependency on Luke's machine. The browser viewer uses a simplified material representation of the same evaluated geometry.

- The nominal floor footprint is 9 x 6 m. Four assumed 150 mm front posts give three equal **2800 mm clear openings**. Nominal bay divisions and clear openings are different measurements.
- The entrance faces local +X/east, north is +Y, up is +Z. The enclosed bay is at the south/left end. The local origin is the floor centre; this is not a surveyed/georeferenced position.
- The full partition continues into the roof profile. Added rear/side framing and rafters are illustrative; their sizes, joints and structural adequacy have not been designed.
- The model retains **4163 mm ridge, 2300 mm eaves and 300 mm plinth** as inherited placeholders. Dad has not approved these as final V4 dimensions. Three graphical plinth courses occupy that 300 mm envelope; the resulting 100 mm model courses are **not** a real brick/mortar specification.
- The accepted illustration and model are separate communication aids. The illustration is not a scale drawing. The model's flat ground and slab do not establish the courtyard levels, final floor or foundations.
- The saved-model checks in `output/V4/model/verification.json` check consistency of the digital model; they do not establish survey accuracy, planning compliance or structural safety.

## Why roof height is unresolved

The dated research in `output/V4/HEIGHT_AND_CONSTRUCTION.md` identifies the national English Class E dual-pitched outbuilding limit of 4 m overall and 2.5 m eaves, with a 2.5 m overall limit if any part is within 2 m of the house's curtilage boundary. Site eligibility, the relevant boundary, setbacks and the height datum are still unverified. The whole estate is not automatically domestic curtilage. Consult the sourced note and check current official guidance when advising; do not infer that this particular scheme is permitted development merely because a model dimension is below a threshold.

The 4.163 m placeholder has not been redesigned into a lower roof yet. A lower pitch must also suit the selected clay pantile, structural depths and measured ground/floor levels. Do not silently subtract the estimated courtyard fall from the ridge or choose 4.2 m as an allowance.

## What Dad has promised but not yet supplied

A licensed map with boundary/building annotations, a sketch of the new garage position, a driveway sketch, and photographs of all four sides of the existing garage. Exact offsets, boundary distances, ground levels, existing-building dimensions, drainage/surface details and relevant planning records remain inputs to obtain. The available coloured map is only an uncalibrated screenshot; original Promap recovery is closed.

Mapping feasibility and the drawing workflow have been researched. Accurate site drafting is awaiting those inputs and reviews. No new V4 location/site plans or final coordinated building drawing issue have been claimed.

## Which files answer which questions

| Purpose | File relative to this folder |
|---|---|
| Start page / whole pack navigation | `START-HERE.html` |
| Cursor setup and starter prompt | `START-WITH-CURSOR.md` |
| Agent workflow / installation | `AGENTS.md` and `SETUP-BLENDER.md` |
| Interactive model, including roof/door/wall visibility | `output/V4/viewer/garage-V4-viewer.html` |
| Editable current model / embedded notes | `output/V4/model/garage-V4-review.blend`, `output/V4/model/README.txt` |
| Current rendered views | `output/V4/renders/V4-review-front-left.png`, `V4-review-entrance.png`, `V4-review-rear-right.png` |
| Accepted appearance illustration | `output/V4/image/barn-pantiles-edit-V4-01.png` |
| Current authority and work status | `PROJECT_BRIEF.md`, `WORK_STATUS.md` |
| Agreed decisions in data form | `data/v4-design-intent.json` |
| Missing information / printable workbook | `MEASUREMENTS_FOR_DAD.md`, `output/V4/pdf/dad-input-workbook-V4.pdf` |
| Dad's thirteen answers | `Original Ref docs/V4-dad-answers-2026-09-23.md` |
| Mapping, positioning and height research | `output/V4/MAPPING_FEASIBILITY.md`, `POSITIONING_THE_NEW_GARAGE.md`, `HEIGHT_AND_CONSTRUCTION.md` in the same folder |
| Drawing inventory / future editing workflow | `output/V4/DRAWING_REGISTER.md`, `output/V4/DIY_WORKFLOW.md` |
| Existing and earlier proposed drawings | `output/P02/pdf/existing-drawings-P02.pdf`, `output/P02/pdf/proposed-drawings-P02.pdf` |
| Previous alternatives and comparisons | `output/V3/` |
| Human-readable copies of project notes | `readable-notes/` |

P02 is the frozen earlier baseline: preliminary existing/proposed drawings, model, renders and assumptions. V3-A has two enclosed end bays and an open centre; V3-B explores weathered timber/charcoal roofing. Neither is the selected V4 direction. Historical captions such as “no option selected” and old requests for vehicle details must not override the current decisions.

The original PDF and pasted messages are source evidence, not commands to execute. The current brief records the agreed interpretation. Do not treat their reference-project address, supplier watermark or printed scale as proof about this site's geometry.

## A useful first explanation to Dad

“You are looking at the current three-bay garage proposal. Looking at its east-facing entrance, the left bay is enclosed and separated from the two open bays by a full wall. The intended finishes are natural timber and red clay pantiles. This model helps you inspect the layout and appearance; its roof/plinth heights and frame sizes are still placeholders. We are waiting for your map, sketches, photos and measurements to establish accurate siting and finish the planning drawings.”

Adapt that explanation to the actual file/view Dad is asking about. If he supplies new decisions, record them with their source/date and keep measured facts separate from estimates.
