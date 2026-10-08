"""Read the saved V4 model independently; do not change it."""
import bpy, json, hashlib
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'output/V4/model/garage-V4-review.blend'
bpy.ops.wm.open_mainfile(filepath=str(path))
scene=bpy.context.scene
pro=next(c for c in bpy.data.collections if c.name.startswith('V4 GARAGE'))
def bounds(o):
    pts=[o.matrix_world@Vector(v) for v in o.bound_box]
    return [[min(p[i] for p in pts),max(p[i] for p in pts)] for i in range(3)]
floor=bounds(bpy.data.objects['Floor visual only'])
assert abs(floor[0][1]-floor[0][0]-6)<.001
assert abs(floor[1][1]-floor[1][0]-9)<.001
posts=sorted((bounds(o) for o in pro.objects if o.name.startswith('Front post')),key=lambda b:b[1][0])
gaps=[posts[i+1][1][0]-posts[i][1][1] for i in range(3)]
assert all(abs(v-2.8)<.001 for v in gaps)
doors=[o for o in pro.objects if o.name.startswith('Left bay double door')]
assert len(doors)==2 and all(bounds(o)[0][0]>2.8 for o in doors)
assert max(bounds(o)[1][1] for o in doors)<0 # Left bay is south when looking west at entrance.
assert any(o.name.startswith('Partition upper boarding') for o in pro.objects)
assert not any('TESLA' in c.name or 'EXISTING' in c.name for c in bpy.data.collections)
courses=sorted({o['visual_course'] for o in pro.objects if 'visual_course' in o})
assert courses==[1,2,3]
ridge=bounds(bpy.data.objects['Red profiled ridge caps'])[2][1]
assert abs(ridge-4.163)<.001
assert scene['ridge_height_mm_PLACEHOLDER']==4163
assert len(bpy.data.libraries)==0
external_images=[im.name for im in bpy.data.images if im.source=='FILE' and not im.packed_file]
assert not external_images
record={'result':'PASS','checked':'Saved Blender geometry, orientation, clear spans, door count, partition and embedded resources',
        'model_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'floor_extents_m':floor,'clear_front_openings_m':gaps,
        'entrance_direction':'+X/east; no site georeferencing','closed_bay':'left/south','door_leaves':len(doors),'open_bays':2,
        'plinth_visible_courses':courses,'ridge_placeholder_m':ridge,'render_samples':scene.cycles.samples,
        'unpacked_image_dependencies':external_images,'linked_libraries':len(bpy.data.libraries),'construction_verified':False}
(ROOT/'output/V4/model/verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record),flush=True)
