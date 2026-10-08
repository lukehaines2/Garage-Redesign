# Work status - V4 preparation in progress; site inputs awaited

Updated 23 September 2026. V4 is authorised for staged implementation. PROJECT_BRIEF.md governs current intent; data/parameters.json remains the unchanged P02 dimensional baseline. No V4 planning drawings have been issued. The V4 section below supersedes historical sequencing.

S20: User requested diagnosis of the missing interactive render, repair of broken navigation and publication to ChatGPT Sites. The working-tree back-link target was missing and is now supplied. Online geometry loads separately from the page; load/graphics failures retain a rendered picture with a useful error. Local controls, full-pack navigation, failure fallback and complete ZIP download passed browser checks. The site is published privately at https://billeaford-garage-review.lukehaines2.chatgpt.site; sharing audience is awaiting the user's choice. Details: output/Share/SITE-PUBLICATION.json. Model geometry and historical drawings are unchanged.

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
- [x] Address and private household use confirmed: Billeaford Hall, Sloe Lane, Knodishall, IP17 1UU. East Suffolk planning context researched.
- [ ] Planning history/designations, lawful residential curtilage/final route, ownership/access, north and boundaries.
- [ ] Marked existing garage and proposed footprint; measured right stop/left fence/tree and access offsets; proof that footprint plus overhang fits.
- [ ] Existing/proposed site plans and location plan from suitable current mapping; current local validation review and submission readiness.
- [ ] Resolve roof geometry to the low-height intent, surveyed levels and applicable planning route. Class E height rules researched; site eligibility remains unknown. Red clay pantiles confirmed; exact product/pitch compatibility outstanding.
- [ ] Final door/drainage details, actual plinth dimension, roof assembly and frame sizes. Full dividing wall confirmed. Structural engineering/construction documentation remains separate from the planning milestone.
- [x] Vehicle-specific decision closed by S17: ignore specific vehicles; provide equal bays. Historical Model Y checks are not current design criteria.
- [x] S18: V4 editable Blender model, portable GLB, three rendered views and an offline interactive browser viewer created. Orbit, view directions and roof/door/weatherboarding visibility support Dad's inspection. No animation or surveyed walkthrough is claimed.
- [x] S19: Shared pack includes AGENTS.md, an always-applied Cursor rule, a starter prompt, project context and macOS/Windows/Linux Blender setup instructions. Dad's local agent can install Blender if needed and open the supplied model after he invokes setup. No installation on Dad's computer has been tested or claimed.

## V3 — design alternatives (authorised and built 14 September 2026)

The user's “build v3” instruction supersedes the earlier deferral to tomorrow. Outputs are separate in `output/V3/`; V2/P02 remains preserved.

- [x] V3-A: natural timber barn, red profiled tiles, straight braces and diagonal timber door bracing. Two closed end bays and one open centre bay, following an explicit interpretation of S9. This is an alternative layout, not a replacement of the approved V2 brief.
- [x] V3-B: assistant-proposed weathered silver-brown timber and charcoal profiled roof, natural timber doors/frame; left closed and two open bays retained.
- [x] Editable Blender file for each option, generated from the frozen V2 model; same 9 x 6 m footprint, ridge/eaves, Model Y and lighting/cameras.
- [x] Three exterior renders per option and matched V2/A/B comparison boards: front three-quarter, entrance and rear three-quarter.
- [x] Independent saved-model geometry checks and visual review complete; comparison boards and ZIP packaged.
- [x] Preferred V4 direction selected 23 September: Radnor Oak reference; one left enclosed bay/two open bays, natural timber, red pantiles, three-course plinth and concealed end framing. V3 alternatives retained historically.
- [ ] Confirm material products, supplier geometry and door operation. V4 bay arrangement is agreed; V3 alternatives remain historical.
- [ ] Develop chosen design's technical drawings during V4 after dimensions and site inputs are verified. No V3 planning drawing issue created.

Reproduction: `scripts/v3_scene.py`, `scripts/finish_v3.py` and `data/v3-options.json`. V3 archive includes the frozen V2 model dependency. See output/V3/README.md and geometry verification for details.


## V4 - authorised staged implementation, 23 September 2026

The 23 September decisions in PROJECT_BRIEF.md control. Mapping research is complete and the barn image is accepted. S17 confirms 9 x 6 m, entrance east, full dividing wall, equal bays, red clay pantiles/natural finishes and a general-builder construction route. Three courses is conditional on the low-height intent. A 300-400 mm courtyard fall is an estimate only. Dad has promised mapping/annotations, two sketches and four-side photos; these and measured positioning/levels remain awaited.

| Step | Work package | Status / next dependency |
|---|---|---|
| 1 | Revised brief and source capture | Complete through S19; original sources and normalised answers preserved; separate V4 design-intent record |
| 2 | Mapping feasibility | Complete research note; QGIS selected; new mapping source to be selected/checked; no original Promap available |
| 3 | Consolidated Dad inputs | S17 answers recorded; checklist/workbook updated; promised files and survey evidence awaited |
| 4 | Barn image trial | Complete: V4-01 image accepted by Dad at 17:06 on 23 September |
| 5 | Measured mapping base | Awaiting suitable base, measurements, identities and boundary review; no measured GIS master claimed |
| 6 | Location plan | Awaiting Step 5 and red/blue/access extent |
| 7 | Existing site plan | Awaiting measured features/buildings/trees/surfaces |
| 8 | Proposed site plan | Awaiting verified siting, driveway/drainage and layout review |
| 9 | Existing building verification | Desk audit complete; survey/cropped-feature/roof evidence awaited; no corrected issue |
| 10 | Proposed building coordination | V4 visual model updated under S18; saved geometry checked. Footprint/layout/materials agreed; roof/plinth heights remain labelled placeholders. Technical drawing reissue awaits site/level/frame decisions |
| 11 | Complete-set QA/package | Family review ZIP combines current V4 and historical P02/V3 with a Start Here page, offline viewer and Cursor/LLM setup/context guides. Review material packaged; final five-group drawing set still depends on Steps 5-10 |

Stage outputs are under output/V4/. Input workbook is not to scale and must not be submitted as a plan. MAPPING_FEASIBILITY.md contains sourced map findings. HEIGHT_AND_CONSTRUCTION.md answers the S17 height/architect questions without claiming site-specific eligibility. DRAWING_REGISTER.md records all groups and gaps. DIY_WORKFLOW.md gives the editing/export method. data/v4-design-intent.json records current decisions separately from the frozen P02 parameters.

No external message, purchase, appointment or submission has been made. P01, P02 and V3 outputs and baseline dimensions are preserved. Structural engineering remains outside this planning-drawing milestone.
