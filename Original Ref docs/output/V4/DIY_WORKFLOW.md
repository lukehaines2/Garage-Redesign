# Editing and exporting the eventual V4 drawings

This is the selected workflow, ready for use when the verified base arrives. It is not evidence that a measured GIS project already exists.

1. Inspect the original map/survey: date, licence, CRS or scale, coverage, grid/control and source acknowledgement. Keep an untouched copy and record the evidence.
2. In QGIS create a project in British National Grid / EPSG:27700 (metres). Import data using its real source CRS. A screenshot without control points is reference-only. If a permitted raster must be georeferenced, use reliable control and verify residuals and independent dimensions; never set scale just by eyeballing buildings.
3. Maintain separate layers for the base, existing buildings, demolition, proposed building, current/proposed hardstanding, access, trees, application boundary, other ownership and labels. Record the source and confirmation state of each user-added feature.
4. Enter building geometry from measured dimensions. Locate the garage from measured ties to stable features; check footprint, roof overhang, right-hand limit, fence and trees. Obtain Dad's review of the site and boundaries before issue.
5. Save existing and proposed map themes from the same base. Use matching site extents/orientation and a fixed 1:500 scale. Add a separate 1:200 detail if necessary. Use 1:2500 for the location layout unless the verified extent requires a reviewed alternative.
6. Use monochrome/light grey context, red application outline, blue other ownership, a labelled dashed demolition outline and clear proposed linework. Do not rely on colour alone for demolition/proposal. Preserve mapping attribution; do not invent an OS licence number for non-OS mapping.
7. Set the layout page and map-frame size before fixing scale. Add a linked scale bar and north arrow, drawing title/ID, revision, date, site address and preliminary/issue status. Lock map layers/extent after checking.
8. Export a vector PDF and retain the QGIS project plus its permitted data. Open the PDF at its actual page size; check text, linework and margins. Print at 100% and measure the scale bar. Recheck the scale after any subsequent PDF editing.
9. For building drawings use the shared dimension file and existing Python/Blender workflow, but only in a separate V4 output configuration. Do not run the P02 generator to overwrite the frozen reference pack. Keep door/bay layout, plinth, roof and heights coordinated between drawings and model.
10. Update the drawing register and revision note for every issue. Re-run relevant scale/geometry checks and inspect the affected pages. Package the final verified PDF sheets, editable sources, source register and print instructions.

QGIS map scale, extent, CRS and layer-locking controls: [official current documentation](https://docs.qgis.org/3.44/en/docs/user_manual/print_layout/layout_items/layout_map.html).
