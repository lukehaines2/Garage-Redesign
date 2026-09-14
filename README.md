# Garage redesign - P01 review pack

**Preliminary - reference dimensions, subject to verification.**

Start with `output/pdf/existing-drawings-P01.pdf` and `output/pdf/proposed-drawings-P01.pdf`. The complete bundle is `output/garage-review-pack-P01.zip`. Each PDF contains six A3 landscape sheets at 1:50: floor plan, front/rear/left/right elevations and a geometric roof section. Print at **100% / actual size**, never “fit to page”. A 2 m scale bar must measure 40 mm on paper.

`output/renders/baseline-review-board-P01.png` collects the three proposed views; `output/renders/massing-comparison-P01.png` compares the old and new buildings at one camera scale. Individual PNGs are also provided. The generic car body is 4500 x 1800 x 1450 mm (mirrors omitted). It is a scale aid, not a vehicle clearance assessment. `output/model/garage-baseline-P01.blend` is the editable Blender scene; its existing-building collection is hidden by default. Turn that collection on and the proposal off to inspect the old garage. The comparison renders centre the two buildings on the same camera target, not on a surveyed site.

## Sources and limits

`PROJECT_BRIEF.md` is the project record. `data/parameters.json` holds dimension values, evidence and uncertainty. Nothing has yet been measured on site. The proposed roof uses 2300 eaves / 4163 ridge and derives 31.84 degrees; the source's 30-degree annotation is unresolved. Details labelled as assumptions are for review only. `MEASUREMENTS_FOR_DAD.md` lists the inputs needed next.

The 2D drawings and model use the same plan orientation: viewed from outside facing the entrance, left bay has double doors. Compass labels await site confirmation. Existing garage width/door position and cropped-side features remain unresolved. Roof overhangs are assumed where not explicitly dimensioned. The section is a datum geometry diagram, not a designed roof assembly.

## Regenerate

Use Python 3 with `reportlab`, `pdfplumber`, `pypdf` and `Pillow`, and Blender 4.5 LTS. Dependencies are listed in `requirements.txt`.

```sh
python3 scripts/drawings.py
blender -b --python scripts/blender_scene.py
python3 scripts/validate_pack.py
blender -b output/model/garage-baseline-P01.blend --python scripts/verify_blender.py
python3 scripts/finish_pack.py
```

Use `-- --quick` after the Blender script argument for a 24-sample preview. Standard output uses 64-sample Cycles renders at 1500 x 1050. Blender stores units in metres; the parameter file is millimetres. Outputs are deterministically rebuilt at stable paths. Changing a parameter requires regenerating both drawings and model.

Blender 4.5.10 for Apple Silicon was downloaded from the [official Blender release directory](https://download.blender.org/release/Blender4.5/) and run from a temporary mounted disk image. The Blender application is not bundled in the review pack. Install Blender or point the command to its executable to regenerate later.

## Review and next issue

Automated checks verify PDF paper size, vector scale, text margins, roof geometry, saved model extents and door/open-bay counts. Rendered sheets and PNGs also receive visual review. Reports are under `output/` and `output/model/`.

Next issue requires a confirmed address/site, measurements, boundary and access mapping, roof decision and council validation checklist. Location/site plans and structural construction details are not included in P01. No claim of planning approval or survey accuracy is made.
