"""Create V3 alternatives from the frozen, editable V2 baseline. Run in Blender."""
import bpy,sys,json,math,hashlib
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[1]
config=json.loads((ROOT/'data/v3-options.json').read_text())
base=ROOT/config['baseline'];out=ROOT/'output/V3'
for folder in ['models','renders']:(out/folder).mkdir(parents=True,exist_ok=True)
basehash=hashlib.sha256(base.read_bytes()).hexdigest()
def bounds(o):
 pts=[o.matrix_world@Vector(v) for v in o.bound_box]
 return [[min(v[i] for v in pts),max(v[i] for v in pts)] for i in range(3)]
def recolour(m,col):
 m.diffuse_color=(*col,1)
 for n in m.node_tree.nodes:
  if n.type=='BSDF_PRINCIPLED':n.inputs['Base Color'].default_value=(*col,1)
  elif n.type=='VALTORGB':
   n.color_ramp.elements[0].color=(*(v*.78 for v in col),1)
   n.color_ramp.elements[1].color=(*(v*1.10 for v in col),1)
def duplicate(o,dx):
 n=o.copy();n.data=o.data.copy();o.users_collection[0].objects.link(n);n.location.x+=dx;return n
def beam(name,a,b,width,depth,mat,col):
 a,b=Vector(a),Vector(b)
 bpy.ops.mesh.primitive_cube_add(size=1,location=(a+b)/2);o=bpy.context.object;o.name=name
 for c in list(o.users_collection):c.objects.unlink(o)
 col.objects.link(o);o.dimensions=(width,depth,(b-a).length);o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler();bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.append(mat)
 bevel=o.modifiers.new('Timber edges','BEVEL');bevel.width=.005;bevel.segments=2
 return o
def cam(loc,target,scale):
 o=bpy.context.scene.camera;o.location=loc;o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler();o.data.type='ORTHO';o.data.ortho_scale=scale
reports=[]
options=[sys.argv[sys.argv.index('--option')+1]] if '--option' in sys.argv else ['A','B']
for opt in options:
 bpy.ops.wm.open_mainfile(filepath=str(base));scene=bpy.context.scene
 pro=bpy.data.collections['PROPOSED - reference dimensions, provisional details']
 frame=bpy.data.materials['Natural oak frame - Dad requested']
 for o in list(pro.objects):
  if o.name.startswith('Curved oak knee brace'):bpy.data.objects.remove(o,do_unlink=True)
 for x,sgn in [(3,1),(6,-1),(6,1),(8.925,-1)]:beam('V3 straight knee brace',(x,.075,1.52),(x+sgn*.53,.075,2.03),.115,.10,frame,pro)
 # Surface-mounted diagonal door braces; door leaves remain closed.
 for lo,hi in [(.15,1.5375),(1.5375,2.925)]:beam('V3 door diagonal',(lo+.13,-.005,.20),(hi-.13,-.005,1.85),.085,.045,frame,pro)
 if opt=='A':
  prefixes=('Left bay double door','Door vertical board','Door strap hinge','Door handle','V3 door diagonal')
  for o in list(pro.objects):
   if o.name.startswith(prefixes):
    n=duplicate(o,5.925);n.name='V3 right '+o.name
  for o in list(pro.objects):
   if o.name.startswith('Partition'):
    n=duplicate(o,3);n.name='V3 right partition '+o.name
 else:
  recolour(bpy.data.materials['Natural wood weatherboarding - Dad requested'],(.31,.285,.24))
  for m in bpy.data.materials:
   if 'tile' in m.name.lower() or m.name.startswith('Red profiled roof'):
    recolour(m,(.10,.12,.13))
 # Close corner gaps with consistent timber cover strips.
 cladding=bpy.data.materials['Natural wood weatherboarding - Dad requested']
 for x in [.05,8.95]:
  for y in [.05,5.95]:beam('V3 corner trim',(x,y,.3),(x,y,2.21),.13,.13,cladding,pro)
 scene['iteration']='V3-'+opt;scene['option_notes']=json.dumps(config[opt]);scene['open_bays']=1 if opt=='A' else 2
 text=bpy.data.texts.new('V3 OPTION - READ ME');text.write(json.dumps(config[opt],indent=2)+'\n'+config['limitations'])
 cam((13,-13,8),(4.5,2.7,1.8),13.7)
 model=out/'models'/f'garage-V3-{opt}.blend';bpy.ops.wm.save_as_mainfile(filepath=str(model))
 # Inspect generated option geometry, not only configuration values.
 ridge=bounds(bpy.data.objects['Red profiled ridge caps'])[2][1]
 assert abs(ridge-4.163)<.001
 leaves=[o for o in pro.objects if 'bay double door' in o.name]
 assert len(leaves)==(4 if opt=='A' else 2)
 for o in leaves:
  bb=bounds(o)
  if bb[0][0]>6:assert bb[0][0]>=6.075-.001 and bb[0][1]<=8.85+.001
  else:assert bb[0][0]>=.15-.001 and bb[0][1]<=2.925+.001
 car=bpy.data.collections['TESLA MODEL Y - 2025+ Premium reference, simplified']
 carheight=max(bounds(o)[2][1] for o in car.objects if o.type=='MESH');assert abs(carheight-1.624)<.001
 floor=bounds(bpy.data.objects['Floor visual only']);assert abs(floor[0][1]-floor[0][0]-9)<.001 and abs(floor[1][1]-floor[1][0]-6)<.001
 reports.append({'option':opt,'result':'PASS','model_sha256':hashlib.sha256(model.read_bytes()).hexdigest(),'doors':len(leaves),'open_bays':scene['open_bays'],'ridge_m':ridge,'car_height_m':carheight,'baseline_sha256':basehash})
 for name,loc,target,scale in [('front-three-quarter',(13,-13,8),(4.5,2.7,1.8),13.7),('entrance',(4.5,-18,3.8),(4.5,2,1.8),11.5),('rear-three-quarter',(-7,16,9),(4.5,3,1.8),13.7)]:
  cam(loc,target,scale);scene.render.filepath=str(out/'renders'/f'V3-{opt}-{name}.png');bpy.ops.render.render(write_still=True)
assert hashlib.sha256(base.read_bytes()).hexdigest()==basehash
reportfile=out/'geometry-verification.json'
if len(options)==1 and reportfile.exists():
 reports=[r for r in json.loads(reportfile.read_text()) if r['option'] not in options]+reports
reportfile.write_text(json.dumps(sorted(reports,key=lambda r:r['option']),indent=2));print('V3 COMPLETE',flush=True)
