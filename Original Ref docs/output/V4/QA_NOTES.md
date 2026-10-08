# V4 preparation-stage checks

23 September 2026. This stage includes research, a static input workbook, a drawing desk audit and an image edit. It does not contain a verified measured base or newly issued location/site/building drawings.

- All six workbook pages rendered and visually inspected. Page sizes are A4 portrait; text stays within the page; tables/fields and the two unchanged reference-map images are legible. The map sheets explicitly state NOT TO SCALE. This workbook is for information collection only.
- S17 update: workbook regenerated and all six pages re-inspected after recording the answers. Old footprint/partition/vehicle questions removed; promised files, boundary distances and measured levels remain blank. The source transcript is retained; V4 design intent is separate from the frozen P02 parameters.
- Workbook embeds its fonts. An initial local Poppler font-configuration failure was resolved by font embedding, then the complete PDF was regenerated and rendered successfully without rendering errors.
- Exact copies of the supplied PDF and Radnor image match their source SHA-256 hashes.
- Generated barn PNG opens correctly. Visual review and provenance are recorded in image/QA.md; Dad accepted V4-01 on 23 September at 17:06. The exact built-in imagegen prompt is preserved.
- Current East Suffolk 2024 validation list and January 2026 householder guidance were checked, including the detailed map criteria. Applicable source URLs and section/page locators are in MAPPING_FEASIBILITY.md. The legacy 2014 checklist was not adopted.
- National Class E height/datum guidance, Planning Portal planning/building-regulations guidance and ARB title/services guidance checked on 23 September. Sources and project implications are in HEIGHT_AND_CONSTRUCTION.md. Site-specific PD eligibility remains unresolved; the 4000/2500 mm rules are not stored as selected project heights.
- No geometry change, boundary, building identity or north direction has been inferred from the map screenshot. No submitted plan has been declared council-ready.
- Git comparison confirms no changes to P02/V3 outputs, original drawing/model outputs, or their parameter files. Only current records and new V4 preparation outputs changed.
- README local links checked. Machine-readable results, source/image/PDF hashes and page checks are in validation-report.json. The ZIP is tested separately for corruption and inclusion of required stage outputs.

Remaining acceptance gates: mapping/rights and site evidence from Dad; boundary/building identity review; siting/driveway review; verified building details; final drawing QA against the actual applicable requirements.

## S18 model and sharing update

- A separate V4 .blend and GLB now accompany three renders and an offline WebGL viewer. P02/V3 models remain unchanged.
- The saved V4 model is independently reopened by verify_v4_model.py: 9 x 6 m floor, three equal 2.8 m clear openings under assumed post sizes, paired left doors, two open bays, full partition, east-facing local orientation and three illustrated plinth courses. No linked library or unpacked image dependency remains. See model/verification.json.
- The 4163/2300/300 mm ridge/eaves/plinth values remain explicitly labelled placeholders. No surveyed slope or final height is modelled. The three-course depiction inside a 300 mm envelope is not a brick specification.
- End boarding, interior framing and corner seams visually inspected; rendered captions identify the provisional dimensions. Browser materials simplify the procedural Blender materials.
- The full sharing pack includes a readable HTML index, converted project notes, current model/viewer and historical P02/V3 outputs. Local link, GLB embedding, model-hash and ZIP checks are recorded in its SHARE-CHECKS.json.
