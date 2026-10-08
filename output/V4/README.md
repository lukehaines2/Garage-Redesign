# V4 preparation-stage review pack

23 September 2026. Billeaford Hall, Sloe Lane, Knodishall, IP17 1UU. Private household garage.

The revised brief, mapping research, input checklist/workbook, drawing audit and image trial are complete for this stage. Dad's S17 answers are recorded, including the 9 x 6 m footprint, east-facing entrance, full partition, equal bays and clay pantiles. Height/construction-drawing research is now included. Promised mapping/annotations, sketches and photographs remain awaited. The illustration is accepted. This is not the final five-group planning drawing set; no measured GIS master or V4 planning sheets have been issued.

## Start here

- [Interactive garage viewer](viewer/garage-V4-viewer.html): offline browser inspection with roof/door/weatherboarding controls. [Editable Blender model](model/garage-V4-review.blend), [portable GLB](model/garage-V4-review.glb) and [model notes](model/README.txt). The V4 layout is updated; ridge/eaves/plinth dimensions remain explicitly provisional. Flat ground is studio presentation, not a site survey.
- For the full family review bundle, open `output/Share/Billeaford-Hall-full-review/START-HERE.html` or send `output/Share/Billeaford-Hall-full-review.zip`. It includes current V4 and clearly labelled historical P02/V3 outputs.
- [Mapping feasibility](MAPPING_FEASIBILITY.md): sourced council requirements, mapping rights versus accuracy, QGIS workflow, scale/paper guidance and priced fallback examples.
- [Height and construction drawings](HEIGHT_AND_CONSTRUCTION.md): 4 m / 2.5 m rules, slope/datum implications, unresolved site eligibility and the response to Dad's architect question.
- [Recorded answers](../../Original%20Ref%20docs/V4-dad-answers-2026-09-23.md): all thirteen responses, with commitments distinguished from evidence received.
- [Dad's input workbook](pdf/dad-input-workbook-V4.pdf): six A4 pages with reference-map mark-up sheets, building key, measurement fields and driveway questions. Print/read as a workbook; reference maps are NOT TO SCALE.
- [Barn illustration trial](image/barn-pantiles-edit-V4-01.png): closed end reboarded, watermark removed, red pantiles added. Accepted by Dad on 23 September at 17:06. [Image QA and provenance](image/QA.md).
- [Drawing register and audit](DRAWING_REGISTER.md): each requested group, existing evidence and the exact inputs preventing issue.
- [DIY editing/export workflow](DIY_WORKFLOW.md): how the measured base and future PDFs will be maintained.
- [Full input checklist](../../MEASUREMENTS_FOR_DAD.md), [current work status](../../WORK_STATUS.md), [project brief](../../PROJECT_BRIEF.md).

## Recommended next step

Inspect the new map Dad supplies, including scale, date, licence and coverage, and cross-reference his building/boundary/driveway mark-up. See [positioning the new garage](POSITIONING_THE_NEW_GARAGE.md) for the sketch, measured ties and levels needed. His approximately GBP 20-25 estimate is unverified; no product has been selected or purchased by us. The workbook now records his answers and asks for the remaining evidence.

The proposed 9 x 6 m footprint is confirmed design intent; exact siting and roof heights remain unresolved. Three brick courses is a conditional preference, not a verified millimetre value. Current decisions are in data/v4-design-intent.json; P02 and V3 outputs remain intact. No site boundary, north or building position has been invented from the screenshot.

## Archive

`garage-V4-preparation-pack.zip` contains this stage's outputs, current brief/status/checklist snapshots, source PDF and images, and the workbook builder. It does not relabel the older P02 drawings as V4 or include them as a verified submission set. Read the included stage status before using the pack.

Workbook regeneration: `python3 scripts/v4_input_workbook.py` from project root with the existing ReportLab dependency. The image was edited using the built-in imagegen tool; its exact prompt is preserved beside it. QA results are in `QA_NOTES.md` and `validation-report.json`.

Model regeneration: run Blender 4.5 with `-b --python scripts/v4_scene.py`, then independently verify with `scripts/verify_v4_model.py`. No P02 or V3 output is overwritten. The viewer uses the exported evaluated geometry with simplified materials; no online libraries or hosted model are required. The viewer's Back to full pack link is intended for the complete family review bundle.
