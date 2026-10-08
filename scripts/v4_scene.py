"""Make a shareable V4 review model from frozen P02. Run with Blender 4.5.

This is appearance/layout coordination, not a new technical drawing issue.
Unresolved vertical dimensions explicitly retain their old placeholders.
"""
from pathlib import Path
import bpy, math, json, hashlib, base64, array, sys
from mathutils import Vector, Matrix

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/V4'
BASE = ROOT / 'output/P02/model/garage-baseline-P02.blend'
base_hash = hashlib.sha256(BASE.read_bytes()).hexdigest()
for part in ['model', 'renders', 'viewer']:
    (OUT / part).mkdir(parents=True, exist_ok=True)
intent = json.loads((ROOT / 'data/v4-design-intent.json').read_text())
assert intent['ridge_height_mm'] is None
bpy.ops.wm.open_mainfile(filepath=str(BASE))
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 32
scene.cycles.use_denoising = True
scene.render.resolution_x = 1500
scene.render.resolution_y = 1050
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False
scene.render.threads_mode = 'FIXED'
scene.render.threads = 8
scene.render.use_file_extension = True
bpy.context.preferences.filepaths.save_version = 0
pro = bpy.data.collections['PROPOSED - reference dimensions, provisional details']
pro.name = 'V4 GARAGE - agreed layout; provisional vertical dimensions'
for col in list(bpy.data.collections):
    if col.name.startswith(('TESLA', 'EXISTING')):
        for obj in list(col.objects):
            bpy.data.objects.remove(obj, do_unlink=True)
        bpy.data.collections.remove(col)
for txt in list(bpy.data.texts):
    bpy.data.texts.remove(txt)
for key in list(scene.keys()):
    del scene[key]

frame = bpy.data.materials['Natural oak frame - Dad requested']
boarding = bpy.data.materials['Natural wood weatherboarding - Dad requested']
brick = bpy.data.materials['Red brick plinth - reference finish']
mortar = bpy.data.materials['Mortar']
for mat in bpy.data.materials:
    if mat.name.startswith('Red pantile') or mat.name.startswith('Red profiled roof'):
        mat['material_intent'] = 'Red clay pantile appearance; product and pitch suitability unresolved'

def cube(name, location, dimensions, mat, bevel=.003):
    bpy.ops.mesh.primitive_cube_add(size=1, location=location)
    obj = bpy.context.object
    obj.name = name
    for col in list(obj.users_collection): col.objects.unlink(obj)
    pro.objects.link(obj)
    obj.dimensions = dimensions
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    obj.data.materials.append(mat)
    if bevel:
        mod = obj.modifiers.new('Timber edge', 'BEVEL'); mod.width=bevel; mod.segments=2
    return obj

def beam(name, a, b, width=.10, mat=frame):
    a, b = Vector(a), Vector(b)
    obj = cube(name, (a+b)/2, (width,width,(b-a).length), mat)
    obj.rotation_euler = (b-a).to_track_quat('Z','Y').to_euler()
    return obj

# Equal clear openings with retained, explicitly unengineered 150 mm posts.
# Four posts occupy 600 mm of the 9000 mm frontage: three 2800 mm openings.
post_centres = [.075, 3.025, 5.975, 8.925]
posts = sorted([o for o in pro.objects if o.name.startswith('Front post')], key=lambda o:o.location.x)
assert len(posts)==4
for obj,x in zip(posts,post_centres): obj.location.x=x
for obj in list(pro.objects):
    if obj.name.startswith('Partition'): obj.location.x += .025
    if obj.name.startswith('Curved oak knee brace'):
        # Baseline meshes have world-coordinate vertices and zero object origin.
        centre = sum(v.co.x for v in obj.data.vertices)/len(obj.data.vertices)
        obj.location.x += .025 if centre<4.5 else (-.025 if centre<7.5 else 0)
    if obj.name.startswith(('Left bay double door','Door vertical board','Door strap hinge','Door handle')):
        stretch = Matrix.Translation((.15,0,0)) @ Matrix.Diagonal((2.8/2.775,1,1,1)) @ Matrix.Translation((-.15,0,0))
        obj.matrix_world = stretch @ obj.matrix_world

# Three visible courses inside the retained 300 mm placeholder plinth envelope.
# Course count is illustrative; 100 mm model modules are NOT a brick specification.
for obj in list(pro.objects):
    if ' brick ' in obj.name or 'mortar backing' in obj.name:
        bpy.data.objects.remove(obj,do_unlink=True)
for label,a,b in [('Rear',(.1,5.95,0),(8.9,5.95,0)),('Left',(.05,0,0),(.05,6,0)),
                  ('Right',(8.95,0,0),(8.95,6,0)),('Partition',(3.025,0,0),(3.025,5.9,0))]:
    a,b=Vector(a),Vector(b); length=(b-a).length; u=(b-a)/length; mid=(a+b)/2
    obj=cube(label+' plinth mortar - 300 mm placeholder',(mid.x,mid.y,.15),(length,.088,.3),mortar,0)
    obj.rotation_euler.z=math.atan2(u.y,u.x)
    for row in range(3):
        start=-.12 if row%2 else 0
        while start<length:
            lo,hi=max(0,start),min(length,start+.23)
            if hi>lo:
                mid=a+u*((lo+hi)/2)
                obj=cube(f'{label} brick course {row+1} - illustrative',(mid.x,mid.y,(row+.5)*.1),(hi-lo,.10,.092),brick)
                obj.rotation_euler.z=math.atan2(u.y,u.x)
                obj['visual_course']=row+1
            start+=.24

# Interior members sit behind the external weatherboarding. Sizes/joints illustrative.
for obj in pro.objects:
    if obj.name.startswith('Rear horizontal boarding'):obj.scale.x *= 8.8/9
for x in [.18,3.025,5.975,8.82]:
    cube('Interior rear post - illustrative',(x,5.80,1.255),(.15,.15,1.91),frame,.006)
cube('Interior rear beam - illustrative',(4.5,5.80,2.12),(9,.15,.18),frame,.006)
for bay in range(3):
    left,right=post_centres[bay],post_centres[bay+1]
    for ratio in [1/3,2/3]:
        x=left+(right-left)*ratio
        cube('Interior rear stud - illustrative',(x,5.835,1.23),(.07,.09,1.86),frame)
    beam('Interior rear diagonal - illustrative',(left+.13,5.76,.36),(right-.13,5.76,2.0),.09)
for x in [.18,8.82,3.145]:
    for y in [1.4,2.8,4.2,5.5]:
        cube('Interior side stud - concealed externally',(x,y,1.23),(.09,.075,1.86),frame)
    for ya,yb in [(.25,2.8),(2.95,5.65)]:
        beam('Interior side diagonal - illustrative',(x,ya,.38),(x,yb,2.0),.085)
# Roof underside frame for inspection with covering hidden in the browser viewer.
for x in [.3,1.5,2.7,3.9,5.1,6.3,7.5,8.7]:
    beam('Interior rafter - illustrative',(x,.12,2.08),(x,3,3.97),.10)
    beam('Interior rafter - illustrative',(x,3,3.97),(x,5.88,2.08),.10)
for x in post_centres[1:3]:
    beam('Interior tie beam - illustrative',(x,.15,2.1),(x,5.85,2.1),.14)

# Keep outer end posts behind a continuous face; the boarding already covers x=0/9.
# A thin matching board face closes coplanar post seams without adding external framing.
for x in [.009,8.991]:
    z=.3
    while z<2.21:
        h=min(.14,2.21-z)
        cube('Continuous outer end weatherboard',(x,3,z+h/2),(.020,6,h),boarding,.001)
        z+=.14
# Narrow corner cover boards close weatherboarding end grain, not exposed frame.
for x in [.075,8.925]:
    for y in [-.006,6.006]:
        cube('Weatherboard corner cover strip',(x,y,1.255),(.15,.024,1.91),boarding,.003)

# Local East/North axes for design orientation only, not geographical coordinates.
transform = Matrix.Rotation(math.pi/2,4,'Z') @ Matrix.Translation((-4.5,-3,0))
for obj in pro.objects: obj.matrix_world = transform @ obj.matrix_world
ground=bpy.data.objects.get('Neutral ground')
if ground: ground.location=(0,0,-.20)
for obj in scene.objects:
    if obj.type=='LIGHT': obj.matrix_world=transform @ obj.matrix_world
scene['iteration']='V4 review - 23 September 2026'
scene['status']='Agreed layout and appearance; roof/plinth/frame dimensions provisional; not for construction'
scene['entrance_faces']='East (+X); North is +Y. No georeferencing or measured site placement.'
scene['footprint_mm']='9000 frontage x 6000 depth (confirmed design intent)'
scene['equal_clear_front_openings_mm']=2800
scene['post_width_mm_visual_assumption']=150
scene['open_bays']=2
scene['full_partition']=True
scene['ridge_height_mm_PLACEHOLDER']=4163
scene['eaves_height_mm_PLACEHOLDER']=2300
scene['plinth_height_mm_PLACEHOLDER']=300
scene['plinth_courses_visual']=3
scene['height_compliance']='Not established; current ridge placeholder is not the agreed low-height solution.'
notes='''V4 REVIEW MODEL - read before measuring or building
Agreed: 9 x 6 m; entrance east; one enclosed LEFT bay / two open bays;
full partition; equal spans; natural timber/doors; red clay pantile appearance.
Left is viewed from outside facing the entrance. No vehicle included.

UNRESOLVED VERTICAL DIMENSIONS RETAINED AS PLACEHOLDERS:
Ridge 4163 mm; eaves 2300 mm; plinth 300 mm. These are NOT agreed V4 heights.
Three plinth courses are drawn within the old 300 mm envelope for appearance;
the resulting 100 mm model course is not a real brick/mortar specification.
Frame members, joinery, foundations, roof product and build-up need design.
Equal front clear widths are 2800 mm using assumed 150 mm posts; final frame
dimensions may change. The centreline grid is therefore not exactly 3 x 3 m.

East is +X, North +Y; local origin is the garage centre. This is intended
orientation only. Ground is a flat studio plane, not the reported courtyard slope.
PD eligibility, exact siting, boundary offsets and measured levels remain unknown.

Model objects and procedural materials are embedded. Open in Blender 4.5+.
Orbit in the 3D viewport; numeric keypad 0 toggles camera; Home frames all visible.
The supplied offline browser viewer has roof/door visibility controls.
'''
txt=bpy.data.texts.new('START HERE - V4 confirmed and provisional');txt.write(notes)
(OUT/'model/README.txt').write_text(notes)
camera=scene.camera
def aim(location, target=(0,0,1.8), scale=13.7):
    camera.location=location
    camera.rotation_euler=(Vector(target)-camera.location).to_track_quat('-Z','Y').to_euler()
    camera.data.type='ORTHO';camera.data.ortho_scale=scale

aim((15,-11,8))
note_mat=bpy.data.materials.new('Review note ink');note_mat.use_nodes=True
nodes=note_mat.node_tree.nodes;nodes.clear()
em=nodes.new('ShaderNodeEmission');em.inputs['Color'].default_value=(.025,.045,.045,1)
outnode=nodes.new('ShaderNodeOutputMaterial');note_mat.node_tree.links.new(em.outputs[0],outnode.inputs['Surface'])
note_col=bpy.data.collections.new('REVIEW LABELS - excluded from model export');scene.collection.children.link(note_col)
for idx,line in enumerate(['V4 REVIEW | 9 x 6 m | entrance east | one enclosed + two open bays',
                           'Roof 4.163 m / plinth 0.300 m are placeholders - not a construction or site model']):
    curve=bpy.data.curves.new('Review label','FONT');curve.body=line;curve.size=.155;curve.materials.append(note_mat)
    obj=bpy.data.objects.new('Review label',curve);note_col.objects.link(obj);obj.parent=camera
    obj.location=(-6.48,-4.28-idx*.25,-1)
    obj.visible_shadow=False

for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type=='VIEW_3D':
            area.spaces.active.region_3d.view_perspective='CAMERA'
            area.spaces.active.shading.type='MATERIAL'
            area.spaces.active.overlay.show_overlays=False

bpy.context.view_layer.update()
bpy.ops.file.pack_all()
scene.cycles.samples=32
scene.cycles.use_denoising=True
print('V4 SAVE SAMPLES',scene.cycles.samples,flush=True)
model=OUT/'model/garage-V4-review.blend'
bpy.ops.wm.save_as_mainfile(filepath=str(model))

# Export a portable GLB and an offline viewer buffer from the same evaluated model.
for obj in scene.objects: obj.select_set(False)
for obj in pro.objects: obj.select_set(True)
bpy.context.view_layer.objects.active=posts[0]
bpy.ops.export_scene.gltf(filepath=str(OUT/'model/garage-V4-review.glb'),export_format='GLB',
                         use_selection=True,export_apply=True,export_extras=True,export_materials='EXPORT')

def category(obj):
    n=obj.name.lower()
    if n.startswith(('proposed roof','red pantiles','red profiled ridge','roof edge','dark gutter','downpipe')):return 'roof'
    if n.startswith(('left bay double door','door vertical','door strap','door handle')):return 'doors'
    if 'boarding' in n or 'weatherboard' in n:return 'walls'
    return 'structure'
groups={key:array.array('f') for key in ['structure','walls','doors','roof']}
deps=bpy.context.evaluated_depsgraph_get()
for obj in pro.objects:
    if obj.type!='MESH':continue
    evaluated=obj.evaluated_get(deps);mesh=evaluated.to_mesh();mesh.calc_loop_triangles()
    mat_normal=obj.matrix_world.to_3x3().inverted().transposed()
    for tri in mesh.loop_triangles:
        mat=mesh.materials[tri.material_index] if len(mesh.materials)>tri.material_index else None
        colour=tuple(mat.diffuse_color[:3]) if mat else (.45,.4,.3)
        for vi in tri.vertices:
            pos=obj.matrix_world @ mesh.vertices[vi].co
            norm=mat_normal @ (mesh.vertices[vi].normal if mesh.polygons[tri.polygon_index].use_smooth else tri.normal)
            norm.normalize()
            groups[category(obj)].extend((*pos,*norm,*colour))
    evaluated.to_mesh_clear()
payload={'groups':{key:base64.b64encode(buf.tobytes()).decode('ascii') for key,buf in groups.items()},
         'vertices':{key:len(buf)//9 for key,buf in groups.items()},'source_model_sha256':hashlib.sha256(model.read_bytes()).hexdigest()}
(OUT/'viewer/model-data.json').write_text(json.dumps(payload,separators=(',',':')))
assert hashlib.sha256(BASE.read_bytes()).hexdigest()==base_hash
(OUT/'model/build-record.json').write_text(json.dumps({'model_sha256':payload['source_model_sha256'],'baseline_sha256':base_hash,
 'source_intent':'data/v4-design-intent.json','viewer_vertices':payload['vertices'],'coordinate_system':'local X east, Y north, Z up; not surveyed',
 'changes':['equal front clear spans under assumed post sizes','full partition retained','three visible plinth courses in retained 300 mm placeholder','continuous end boarding','interior framing added','vehicle removed','east-facing local orientation','packed resources and GLB export'],
 'provisional_dimensions_mm':{'ridge':4163,'eaves':2300,'plinth':300,'posts':150},'final_height_selected':False},indent=2)+'\n')
if '--no-render' not in sys.argv:
    for name,loc in [('front-left',(15,-11,8)),('entrance',(18,0,5.0)),('rear-right',(-14,11,8))]:
        aim(loc)
        bpy.context.scene.cycles.samples=32
        bpy.context.scene.cycles.use_denoising=True
        print('V4 RENDER SAMPLES',bpy.context.scene.cycles.samples,flush=True)
        scene.render.filepath=str(OUT/'renders'/f'V4-review-{name}.png')
        bpy.ops.render.render(write_still=True)
print('V4 model/export/renders complete',flush=True)
