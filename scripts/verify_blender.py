"""Inspect saved geometry independently of the generator."""
import bpy,sys,json,math,hashlib
from pathlib import Path
from mathutils import Vector
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import OUT,REV,ROOT,values,clear_openings
p=values('proposed');q=values('existing')
def bounds(obj):
 pts=[obj.matrix_world@Vector(v) for v in obj.bound_box]
 return [[min(v[i] for v in pts),max(v[i] for v in pts)] for i in range(3)]
def near(a,b):assert abs(a-b)<.001,(a,b)
roof=bpy.data.objects['Proposed roof'];rb=bounds(roof)
near(rb[0][0],-p['overhang']/1000);near(rb[0][1],(p['width']+p['overhang'])/1000)
near(rb[1][0],-p['overhang']/1000);near(rb[1][1],(p['depth']+p['overhang'])/1000)
near(bounds(bpy.data.objects['Red profiled ridge caps'])[2][1],p['ridge']/1000)
assert bpy.data.materials.get('Natural oak frame - Dad requested')
assert bpy.data.materials.get('Natural wood weatherboarding - Dad requested')
assert sum(o.name.startswith('Red pantiles ') for o in bpy.data.objects)==2
assert sum(o.name.startswith('Curved oak knee brace') for o in bpy.data.objects)==4
fb=bounds(bpy.data.objects['Floor visual only']);near(fb[0][1]-fb[0][0],p['width']/1000);near(fb[1][1]-fb[1][0],p['depth']/1000)
posts=sorted([o for o in bpy.data.objects if o.name.startswith('Front post')],key=lambda o:o.location.x)
assert len(posts)==4
openings=[(bounds(posts[i+1])[0][0]-bounds(posts[i])[0][1])*1000 for i in range(3)]
for a,b in zip(openings,clear_openings()):near(a,b)
doors=[o for o in bpy.data.objects if o.name.startswith('Left bay double door')]
assert len(doors)==2 and all(bounds(o)[0][1]<p['bay']/1000 for o in doors)
near(bounds(bpy.data.objects['Existing roof'])[1][1]-bounds(bpy.data.objects['Existing roof'])[1][0],q['roof_length']/1000)
report={'model_sha256':hashlib.sha256(Path(bpy.data.filepath).read_bytes()).hexdigest(),'result':'PASS','checked':'Saved .blend geometry, not only parameter values','roof_support_bounds_m':rb,'roof_ridge_cap_height_m':bounds(bpy.data.objects['Red profiled ridge caps'])[2][1],'oak_frame_and_pantile_checks':'PASS','clear_openings_mm':openings,'paired_door_leaves':len(doors),'open_front_bays':len(posts)-1-1,'existing_roof_length_mm':q['roof_length'],'visual_assumptions_remain':True}
(OUT/'model/geometry-verification.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
