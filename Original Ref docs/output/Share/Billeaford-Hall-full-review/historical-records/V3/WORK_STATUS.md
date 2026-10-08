# Work status — V2 preserved; V3 design options built; V4 queued

Updated 14 September 2026. V2 = P02 drawing/model issue. The current pack is a preliminary design review, not a verified planning submission. PROJECT_BRIEF.md governs intent and evidence; data/parameters.json governs the current model values.

## Completed in V2

- [x] Shared parameters with reference sources and uncertainty; reproducible Python drawing and Blender scripts.
- [x] Existing and proposed drawing packs: two six-page A3 PDFs, twelve editable SVGs, 1:50 plans, four elevations and geometric roof sections, title blocks, dimensions, scale bars and preliminary notes.
- [x] Editable Blender baseline: 9 x 6 m proposal, left paired doors, two open bays, provisional partition, natural oak frame/boarding, curved braces, red profiled tiles and red brick plinth.
- [x] Simplified Model Y: 4790 mm long, 1920 mm body width, 2129 mm over mirrors, 1624 mm height. Nominal 406 mm clearance under the assumed 2030 mm entrance beam.
- [x] Six PNG renders: three proposed exterior views, orthographic clearance view and two massing views. Three composed boards: design review, annotated clearance and same-scale massing comparison.
- [x] PDF paper/scale/text checks, saved Blender geometry checks, visual inspection of all sheets/renders/boards and ZIP integrity check. Reports are in output/P02/.
- [x] Recorded oblique site photograph, right-hand hard stop, provisional space to left/fence and intention to avoid further tree removal.
- [x] Updated source record, measurement checklist and packaged deliverables in output/P02/garage-review-pack-P02.zip. P01 retained in original output locations.

## Not done / unresolved

- [ ] Measured survey, levels, original uncropped drawings, confirmed existing door dimensions/openings and roof covering (drawing says corrugated; photo appears tiled).
- [ ] Actual address/council, planning history, application route, ownership, north and boundaries.
- [ ] Marked existing garage and proposed footprint; measured right stop/left fence/tree and access offsets; proof that footprint plus overhang fits.
- [ ] Existing/proposed site plans and location plan from suitable current mapping; current local validation review and submission readiness.
- [ ] Resolve 30° versus 4163 mm ridge / 2300 mm eaves; current model derives 31.84°. Choose actual clay/concrete tile product.
- [ ] Final door/partition/drainage details, roof assembly and frame sizes. Structural engineering/construction documentation remains outside this review milestone.
- [ ] Confirm actual Model Y year/variant; roof racks, raised tailgate, approach gradients and swept vehicle clearance are not modelled.
- [ ] Interactive web viewer, animation or walkthrough deliverable. V3 alternative designs are now built. The editable Blender scene can be explored, but no dedicated walkthrough has been produced.

## V3 — design alternatives (authorised and built 14 September 2026)

The user's “build v3” instruction supersedes the earlier deferral to tomorrow. Outputs are separate in `output/V3/`; V2/P02 remains preserved.

- [x] V3-A: natural timber barn, red profiled tiles, straight braces and diagonal timber door bracing. Two closed end bays and one open centre bay, following an explicit interpretation of S9. This is an alternative layout, not a replacement of the approved V2 brief.
- [x] V3-B: assistant-proposed weathered silver-brown timber and charcoal profiled roof, natural timber doors/frame; left closed and two open bays retained.
- [x] Editable Blender file for each option, generated from the frozen V2 model; same 9 x 6 m footprint, ridge/eaves, Model Y and lighting/cameras.
- [x] Three exterior renders per option and matched V2/A/B comparison boards: front three-quarter, entrance and rear three-quarter.
- [x] Independent saved-model geometry checks and visual review complete; comparison boards and ZIP packaged.
- [ ] Dad/user to choose an option or request changes; no final scheme selected.
- [ ] Confirm doors/open-bay arrangement, materials/product and supplier feasibility. Closed-door options have no swing or approach assessment.
- [ ] Develop chosen design's technical drawings during V4 after dimensions and site inputs are verified. No V3 planning drawing issue created.

Reproduction: `scripts/v3_scene.py`, `scripts/finish_v3.py` and `data/v3-options.json`. V3 archive includes the frozen V2 model dependency. See output/V3/README.md and geometry verification for details.


## V4 — planning drawing package (queued; not started)

Source: Ben's email of 25 August 2026, supplied by the user (S10), recorded in `Original Ref docs/V4-planning-notes.md`. This is the project-specific working deliverable list; council validation remains to be confirmed. V3 selects/designs alternatives; V4 develops the chosen scheme towards application drawings.

| Ben's requested document | What we have | V4 work remaining |
|---|---|---|
| Site Location Plan | Context map image only | Obtain suitable current mapping; confirm site, access, north and application/ownership boundaries; prepare scaled plan. |
| Existing Site Plan | Map and oblique photograph, no surveyed siting | Identify buildings and measure/verify boundaries, garage position, levels, access, trees and hardstanding. |
| Proposed Site Plan | 9 x 6 m model; right-stop/left-fence intent | Position selected design on verified base; dimension offsets, roof extent and access; show demolition/replacement and relevant site changes. |
| Existing Building Elevations and Floor Plan — demolition | V2 preliminary floor plan, four elevations and extra geometric section | Verify measurements, cropped/missing features and materials; confirm orientation and demolition annotation; correct and issue planning drawings. |
| Proposed Building Elevations and Floor Plan | V2 preliminary floor plan/four elevations and geometric section | Adopt V3 selection; coordinate supplier geometry, openings, roof/material decisions and verified levels; regenerate consistent drawings. |

Ordered tasks:

1. [ ] Confirm which kit provider(s) are under consideration and obtain an inventory/sample of drawings they can provide: floor plan, all elevations, dimensions, materials, file formats, scales, revision/customisation scope and whether drawings match the selected kit/site requirements. Dad/user to obtain correspondence; no messages sent by us.
2. [ ] Record a responsibility matrix: supplier deliverables, drawings we prepare from verified inputs, and any remaining measured survey/drafting/review needed from Ben, an architect or surveyor. No external engagement or fee agreed.
3. [ ] Obtain the outstanding site/measurement evidence and selected V3 scheme; resolve shared dimensions before producing coordinated site and building drawings.
4. [ ] Confirm actual council, application route and current validation requirements with primary sources/Ben. Assess supplementary roof plan, level sections, materials schedule and any design and access statement on their applicability; the pasted Perplexity answer does not make them mandatory.
5. [ ] Prepare the five requested document groups, coordinating supplier drawings where supplied; avoid duplicating or contradicting their final proposal.
6. [ ] Check sheet scales, dimensions, levels, orientation, material notes, boundaries, demolition/proposed status and revision consistency; visually inspect final sheets and arrange appropriate project review before calling the set submission-ready.

Ben's approximately £800 example relates to another project's architect preparing missing documents. It is not our quote or confirmed budget. The V2 geometric section is not a structural roof detail. Construction engineering remains outside the current scope.

V4 is planning/task recording only at this stage. No new site plans, mapping purchase, professional appointment or application submission has been undertaken. The committed V2 pack remains unchanged.
