# Garage redesign — V2 / P02 review pack

**V2 complete for design review — preliminary, reference dimensions subject to verification.**

`WORK_STATUS.md` records what is complete, what remains outstanding and the V3 backlog for 15 September 2026. V3 is planned only; the first alternative will explore the newly supplied plainer timber barn and shut-door styling.

Start with `output/P02/pdf/existing-drawings-P02.pdf` and `output/P02/pdf/proposed-drawings-P02.pdf`. The complete bundle is `output/P02/garage-review-pack-P02.zip`. Each PDF contains six A3 landscape sheets at 1:50: floor plan, front/rear/left/right elevations and a geometric roof section. Print at **100% / actual size**, never “fit to page”. A 2 m scale bar must measure 40 mm on paper.

`output/P02/renders/baseline-review-board-P02.png` collects the three proposed views; `output/P02/renders/massing-comparison-P02.png` compares the old and new buildings at one camera scale. Individual PNGs are also provided. The simplified Tesla Model Y uses a 2025+ EU Premium reference: 4790 x 1920 x 1624 mm, 2129 mm over mirrors. `output/P02/renders/model-y-clearance-P02.png` shows 406 mm nominal clearance beneath the assumed 2030 mm entrance beam. Confirm actual car and structural dimensions; roof racks and raised tailgate are excluded. `output/P02/model/garage-baseline-P02.blend` is the editable Blender scene; its existing-building collection is hidden by default. Turn that collection on and the proposal off to inspect the old garage. The comparison renders centre the two buildings on the same camera target, not on a surveyed site.

## Sources and limits

`PROJECT_BRIEF.md` is the project record. `data/parameters.json` holds dimension values, evidence and uncertainty. Nothing has yet been measured on site. The proposed roof uses 2300 eaves / 4163 ridge and derives 31.84 degrees; the source's 30-degree annotation is unresolved. Details labelled as assumptions are for review only. `MEASUREMENTS_FOR_DAD.md` lists the inputs needed next.

The 2D drawings and model use the same plan orientation: viewed from outside facing the entrance, left bay has double doors. Compass labels await site confirmation. Existing garage width/door position and cropped-side features remain unresolved. Roof overhangs are assumed where not explicitly dimensioned. The section is a datum geometry diagram, not a designed roof assembly.

## Regenerate

Use Python 3 with `reportlab`, `pdfplumber`, `pypdf` and `Pillow`, and Blender 4.5 LTS. Dependencies are listed in `requirements.txt`.

```sh
python3 scripts/drawings.py
blender -b --python scripts/blender_scene.py
python3 scripts/validate_pack.py
blender -b output/P02/model/garage-baseline-P02.blend --python scripts/verify_blender.py
python3 scripts/finish_pack.py
```

Use `-- --quick` after the Blender script argument for a 24-sample preview. Standard output uses 64-sample Cycles renders at 1500 x 1050. Blender stores units in metres; the parameter file is millimetres. Outputs are deterministically rebuilt at stable paths. Changing a parameter requires regenerating both drawings and model.

Blender 4.5.10 for Apple Silicon was downloaded from the [official Blender release directory](https://download.blender.org/release/Blender4.5/) and run from a temporary mounted disk image. The Blender application is not bundled in the review pack. Install Blender or point the command to its executable to regenerate later.

## Review and next issue

Automated checks verify PDF paper size, vector scale, text margins, roof geometry, saved model extents and door/open-bay counts. Rendered sheets and PNGs also receive visual review. Reports are under `output/P02/` and `output/P02/model/`.

V3 design/material alternatives can proceed provisionally from this baseline. Progress towards a planning submission requires a confirmed address/site, measurements, boundary and access mapping, roof decision and council validation checklist. Location/site plans and structural construction details are not included in P02. No claim of planning approval or survey accuracy is made.

P02 uses natural oak framing, natural timber boarding, curved braces and red profiled tiles from the new appearance reference. Tile product and frame construction remain provisional. P01 is preserved in the original output paths.
