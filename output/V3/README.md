# V3 design alternatives

V3-A follows the blurry barn reference with two closed end bays and one open centre bay. Door arrangement is an explicit design interpretation awaiting review, not a change to the V2 brief. Warm timber, red profiled tiles, diagonal door bracing and simple straight knee braces.

V3-B retains one closed left bay and two open bays, with weathered silver-brown boarding, natural timber doors/frame and charcoal profiled tiles. This is a proposed second option, not a supplier product specification.

Both retain V2's 9000 x 6000 footprint, 2300 eaves/4163 ridge datum, 31.84-degree roof pitch, Model Y envelope and matched camera/lighting. Straight braces and end-bay doors alter the appearance and available open parking; final structural and access details are unverified. Doors are shown closed, with no swing/approach assessment. No site placement is modelled.

Open `models/garage-V3-A.blend` or `models/garage-V3-B.blend` in Blender. Each opens with a front three-quarter camera, and the existing building remains hidden. Individual PNGs are in `renders/`; comparison boards place V2, A and B side by side in that order.

Reproduce from project root:

```
blender -b --python scripts/v3_scene.py
blender -b --python scripts/verify_v3.py
python3 scripts/finish_v3.py
```

The script loads the frozen V2 Blender file. The archive includes that dependency, configuration, source scripts, working documents and reference image. Python finishing requires Pillow. The live V2 parameters and drawing files are unchanged. No new technical/planning drawing issue is implied by these visual alternatives: select a design before V4 coordination.
