"""Reopen saved V3 models and verify option layout, extents and common scale."""
import bpy,json,hashlib
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'output/V3'
def bounds(o):
 pts=[o.matrix_world@Vector(v) for v in o.bound_box]
 return [[min(v[i] for v in pts),max(v[i] for v in pts)] for i in range(3)]
checks=[]
for opt in ['A','B']:
 path=out/'models'/f'garage-V3-{opt}.blend';bpy.ops.wm.open_mainfile(filepath=str(path))
 pro=bpy.data.collections['PROPOSED - reference dimensions, provisional details'];leaves=[o for o in pro.objects if 'bay double door' in o.name]
 assert len(leaves)==(4 if opt=='A' else 2)
 for o in leaves:
  bb=bounds(o)[0];lo,hi=(6.075,8.85) if bb[0]>6 else (.15,2.925)
  assert bb[0]>=lo-.001 and bb[1]<=hi+.001
 assert sum(o.name.startswith('V3 straight knee brace') for o in pro.objects)==4
 assert not any(o.name.startswith('Curved oak knee brace') for o in pro.objects)
 car=bpy.data.collections['TESLA MODEL Y - 2025+ Premium reference, simplified'];boxes=[bounds(o) for o in car.objects if o.type=='MESH']
 for axis,expected in [(0,2.129),(1,4.79),(2,1.624)]:
  extent=max(b[axis][1] for b in boxes)-min(b[axis][0] for b in boxes);assert abs(extent-expected)<.001
 assert abs(bounds(bpy.data.objects['Red profiled ridge caps'])[2][1]-4.163)<.001
 assert abs(bpy.context.scene.camera.data.ortho_scale-13.7)<.001
 checks.append({'option':opt,'result':'PASS','saved_model_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'door_leaves':len(leaves),'checks':'Door leaves fit actual post openings; straight braces; Model Y dimensions; ridge height; same saved camera scale'})
(out/'saved-model-verification.json').write_text(json.dumps(checks,indent=2));print(checks)
