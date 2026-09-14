# P01 review-pack checks

Completed 14 September 2026.

- Both PDFs contain six A3 landscape pages. Automated checks confirm physical page size, 1:50 footprint geometry, scale-bar rectangles and text inside page margins.
- All twelve PDF pages were rasterised with Poppler and visually inspected. Height-label spacing was corrected; the final plan and entrance elevation were rechecked after the door and brace annotations were added.
- Twelve SVG sheets preserve A3 physical dimensions and editable vector/text elements.
- The saved Blender geometry was opened separately and checked against the parameter file: proposed 9 x 6 m floor footprint, roof extents including assumed overhangs, 4.163 m roof ridge, four front posts, paired left-bay door leaves, two open bays and the existing 7.2 m roof length.
- Floating-point comparisons allow 0.001 in the reported units; this is numerical tolerance, not claimed surveying precision.
- Final front, entrance and rear renders were inspected. Brick/boarding backing prevents open joints; gable backing sits below the roof skin to avoid surface overlap. The scale car is generic and has no mirrors.
- Both massing images were reviewed together at identical image size and camera scale. Their centre alignment is illustrative, not actual site placement.
- The three-view board and massing comparison board were visually inspected for cropping, text fit and consistent labels.
- Packaging checks require renders newer than the saved model and a geometry-verification SHA-256 matching that model.

These checks establish internal consistency and presentation quality for a preliminary review pack. They do not establish survey accuracy, structural adequacy, site boundaries or planning validation. The source roof-pitch discrepancy, cropped existing details and all recorded assumptions remain open.
