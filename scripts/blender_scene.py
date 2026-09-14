"""Run: blender -b --python scripts/blender_scene.py -- [--quick]
All geometry in metres. Shared source dimensions remain in millimetres.
"""
import bpy,sys,math,json,random
from pathlib import Path
from mathutils import Vector
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import OUT,REV,ROOT,DATA,values,pitch,post_positions,clear_openings
QUICK='--quick' in sys.argv
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
for d in list(bpy.data.collections):
 if d.name!='Collection':bpy.data.collections.remove(d)
scene=bpy.context.scene;scene.unit_settings.system='METRIC';scene.unit_settings.length_unit='METERS'
scene.render.engine='CYCLES';scene.cycles.samples=24 if QUICK else 64
scene.cycles.use_denoising=True;scene.render.resolution_x=1500;scene.render.resolution_y=1050;scene.render.resolution_percentage=100
scene.world.color=(.35,.35,.35)
scene.view_settings.view_transform='AgX'
scene.render.image_settings.file_format='PNG';scene.render.film_transparent=False
current=None

def collection(name):
 c=bpy.data.collections.new(name);scene.collection.children.link(c);return c

def assign(o):
 if current:
  for c in list(o.users_collection):c.objects.unlink(o)
  current.objects.link(o)
 return o

def mat(name,col,rough=.5,metal=0):
 m=bpy.data.materials.new(name);m.diffuse_color=(*col,1);m.use_nodes=True
 bs=m.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*col,1);bs.inputs['Roughness'].default_value=rough;bs.inputs['Metallic'].default_value=metal
 return m
black=mat('Natural wood weatherboarding - Dad requested',(.55,.40,.22),.72)
frame=mat('Natural oak frame - Dad requested',(.49,.34,.18),.65)
oak_beam=mat('Natural oak horizontal beam',(.49,.34,.18),.65)
brick=mat('Red brick plinth - reference finish',(.32,.115,.07),.8)
mortar=mat('Mortar',(.36,.33,.27),.9)
roof=mat('Red profiled roof tile - product unresolved',(.48,.16,.095),.76)
hardware=mat('Dark iron door hardware',(.05,.045,.04),.4,.5)
concrete=mat('Neutral concrete / visual only',(.48,.48,.44),.9)
old=mat('Existing weathered timber - photo S5',(.28,.23,.18),.85)
old_door=mat('Existing blue-green doors - photo S5',(.10,.25,.23),.8)
oldroof=mat('Existing corrugated roof - colour unverified',(.20,.22,.22),.65)
carpaint=mat('Generic car silver',(.43,.52,.55),.25,.6)
glass=mat('Car glazing',(.045,.095,.12),.15,.25)
rubber=mat('Tyres',(.018,.02,.023),.8)
wheel=mat('Wheels',(.27,.29,.31),.3,.65)
lightmat=mat('Car headlights',(.78,.87,.9),.15)

for timber,scale in [(black,(3,60,45)),(frame,(45,45,3)),(oak_beam,(3,45,45)),(old,(3,60,45))]:
 nodes=timber.node_tree.nodes;links=timber.node_tree.links;bs=nodes.get('Principled BSDF')
 tc=nodes.new('ShaderNodeTexCoord');mapping=nodes.new('ShaderNodeVectorMath');mapping.operation='MULTIPLY';mapping.inputs[1].default_value=scale;links.new(tc.outputs['Generated'],mapping.inputs[0])
 noise=nodes.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=2.8;noise.inputs['Detail'].default_value=2.0;links.new(mapping.outputs['Vector'],noise.inputs['Vector'])
 ramp=nodes.new('ShaderNodeValToRGB');base=timber.diffuse_color[:3]
 ramp.color_ramp.elements[0].color=(*(v*.78 for v in base),1);ramp.color_ramp.elements[1].color=(*(min(v*1.10,1) for v in base),1)
 links.new(noise.outputs['Fac'],ramp.inputs[0]);links.new(ramp.outputs['Color'],bs.inputs['Base Color'])
 bump=nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.15;bump.inputs['Distance'].default_value=.001;links.new(noise.outputs['Fac'],bump.inputs['Height']);links.new(bump.outputs['Normal'],bs.inputs['Normal'])

def cube(name,loc,dim,m,bevel=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=assign(bpy.context.object);o.name=name;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 o.data.materials.append(m)
 if bevel:
  b=o.modifiers.new('Small edge bevel','BEVEL');b.width=bevel;b.segments=2;o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
 return o

def mesh(name,verts,faces,m):
 me=bpy.data.meshes.new(name);me.from_pydata(verts,[],faces);me.update();o=bpy.data.objects.new(name,me);current.objects.link(o);o.data.materials.append(m);return o

def beam(name,a,b,size,m):
 a,b=Vector(a),Vector(b);o=cube(name,(a+b)/2,(size,size,(b-a).length),m,.006);o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler();return o

def plinth_wall(name,a,b,h=.3,t=.1):
 a,b=Vector(a),Vector(b);ln=(b-a).length;u=(b-a)/ln
 # Continuous mortar backing avoids open joints through the wall.
 mid=(a+b)/2;o=cube(name+' mortar backing',(mid.x,mid.y,h/2),(ln,t-.012,h),mortar);o.rotation_euler.z=math.atan2(u.y,u.x)
 # Segment bricks: simple staggered joints at visual scale.
 for row in range(4):
  step=.24;start=-.12 if row%2 else 0
  while start<ln:
   lo=max(0,start);hi=min(ln,start+step-.01)
   if hi>lo:
    mid=a+u*((lo+hi)/2);o=cube(name+f' brick {row}',(mid.x,mid.y,(row+.5)*h/4),(hi-lo,t,h/4-.008),brick,.003);o.rotation_euler.z=math.atan2(u.y,u.x)
   start+=step

def flat_boards(name,a,b,bottom,top,m):
 a,b=Vector(a),Vector(b);ln=(b-a).length;mid=(a+b)/2
 o=cube(name+' backing',(mid.x,mid.y,(bottom+top)/2),(ln,.08,top-bottom),m);o.rotation_euler.z=math.atan2(b.y-a.y,b.x-a.x)
 z=bottom
 while z<top-.001:
  height=min(.14,top-z);o=cube(name,(mid.x,mid.y,z+height/2),(ln,.10,height-.005),m,.003);o.rotation_euler.z=math.atan2(b.y-a.y,b.x-a.x);z+=.14

def gable_boards(name,axis,fixed,span,e,r,m):
 if axis=='x':verts=[(fixed,0,e),(fixed,span,e),(fixed,span/2,r)]
 else:verts=[(0,fixed,e),(span,fixed,e),(span/2,fixed,r)]
 back=mesh(name+' backing',[(a,b,c-.10) for a,b,c in verts],[(0,1,2)],m);sol=back.modifiers.new('Board backing','SOLIDIFY');sol.thickness=.075;sol.offset=0
 z=e
 while z<r-.004:
  hi=min(z+.14,r);inner=span/2*((hi-e)/(r-e));lo=inner;right=span-inner
  if right>lo:
   if axis=='x':loc=(fixed,(lo+right)/2,(z+hi)/2);dim=(.10,right-lo,hi-z-.004)
   else:loc=((lo+right)/2,fixed,(z+hi)/2);dim=(right-lo,.10,hi-z-.004)
   cube(name,loc,dim,m,.002)
  z+=.14

def roofs(name,w,d,e,r,axis,over_end,over_eave,m,thick=.06):
 # ridge height is the top surface; thickness goes inward/downwards.
 if axis=='x':
  k=(r-e)/(d/2);z=e-k*over_eave
  verts=[(-over_end,-over_eave,z),(w+over_end,-over_eave,z),(w+over_end,d/2,r),(-over_end,d/2,r),(-over_end,d+over_eave,z),(w+over_end,d+over_eave,z)]
  faces=[(0,1,2,3),(3,2,5,4)]
 else:
  k=(r-e)/(w/2);z=e-k*over_eave
  verts=[(-over_eave,-over_end,z),(w/2,-over_end,r),(w/2,d+over_end,r),(-over_eave,d+over_end,z),(w+over_eave,-over_end,z),(w+over_eave,d+over_end,z)]
  faces=[(0,1,2,3),(1,4,5,2)]
 o=mesh(name,verts,faces,m);sol=o.modifiers.new('Roof visual thickness below surface','SOLIDIFY');sol.thickness=thick;sol.offset=-1
 # Fascia trim along gable slopes only.
 if axis=='x':
  for xx in [-over_end,w+over_end]:
   beam('Roof edge trim',(xx,-over_eave,z-.04),(xx,d/2,r-.025),.055,m);beam('Roof edge trim',(xx,d/2,r-.025),(xx,d+over_eave,z-.04),.055,m)
 else:
  for yy in [-over_end,d+over_end]:
   beam('Existing roof edge',(-over_eave,yy,z-.04),(w/2,yy,r-.025),.05,m);beam('Existing roof edge',(w/2,yy,r-.025),(w+over_eave,yy,z-.04),.05,m)
 return o

def curved_brace(xx,direction,e):
 # Swept knee-brace appearance only: joinery and sizes are not engineered.
 profile=[]
 for j in range(13):
  u=j/12;profile.append((xx+direction*.52*u,e-.22-.50*(1-u)**2))
 profile += [(a,b+.10) for a,b in reversed(profile.copy())]
 verts=[(a,yy,b) for yy in [.025,.125] for a,b in profile];n=len(profile)
 faces=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
 return mesh('Curved oak knee brace - illustrative',verts,faces,frame)

def pantiles(w,d,e,r,ov):
 rv={k:v/1000 for k,v in values('roof_visual').items()};k=(r-e)/(d/2)
 slope_length=math.hypot(d/2+ov,(d/2+ov)*k);cols=math.ceil((w+2*ov)/rv['tile_width']);rows=math.ceil(slope_length/rv['course_gauge']);tw=(w+2*ov)/cols;gauge=slope_length/rows
 rng=random.Random(42);palette=[]
 for i in range(7):
  f=.90+i*.033;palette.append(mat(f'Red pantile shade {i+1}',(.48*f,.16*f,.095*f),.76))
 for side in [-1,1]:
  verts=[];faces=[];shades=[]
  for row in range(rows):
   for col in range(cols):
    shade=rng.randrange(len(palette));base=len(verts)
    for v in [0,1]:
     run=min(slope_length,(row+v)*gauge+(rv['overlap'] if v else 0))/math.sqrt(1+k*k)
     yy=(-ov+run) if side==-1 else (d+ov-run)
     for j in range(13):
      u=j/12;xx=-ov+col*tw+u*(tw-.002)
      wave=rv['profile_height']*(.5-.5*math.cos(2*math.pi*u))
      zz=r-k*abs(yy-d/2)-.046+wave+.006*(1-v)
      verts.append((xx,yy,zz))
    for j in range(12):
     face=(base+j,base+j+1,base+14+j,base+13+j)
     faces.append(face if side==-1 else face[::-1]);shades.append(shade)
  obj=mesh('Red pantiles '+('front' if side==-1 else 'rear')+' - illustrative profile',verts,faces,palette[0])
  for m in palette[1:]:obj.data.materials.append(m)
  for face,shade in zip(obj.data.polygons,shades):face.material_index=shade;face.use_smooth=True
  thick=obj.modifiers.new('Tile visual thickness','SOLIDIFY');thick.thickness=.009;thick.offset=-1
 # Half-round ridge caps terminate at the unchanged controlling ridge height.
 verts=[];faces=[];length=w+2*ov;segments=math.ceil(length/rv['ridge_length']);step=length/segments;radius=rv['ridge_radius']
 for n in range(segments):
  base=len(verts)
  for xx in [-ov+n*step,-ov+(n+1)*step-.003]:
   for j in range(17):
    theta=math.pi*j/16;verts.append((xx,d/2+radius*math.cos(theta),r-radius+radius*math.sin(theta)))
  for j in range(16):faces.append((base+j,base+17+j,base+18+j,base+j+1))
 caps=mesh('Red profiled ridge caps',verts,faces,roof)
 for poly in caps.data.polygons:poly.use_smooth=True
 thick=caps.modifiers.new('Ridge cap visual thickness','SOLIDIFY');thick.thickness=.012;thick.offset=-1
 return caps

pro=collection('PROPOSED - reference dimensions, provisional details');current=pro
p={k:(v/1000 if isinstance(v,(int,float)) and not isinstance(v,bool) else v) for k,v in values('proposed').items()};w,d,e,r=p['width'],p['depth'],p['eaves'],p['ridge']
cube('Floor visual only',(w/2,d/2,-.075),(w,d,.15),concrete)
for name,a,b in [('Rear',(0,d-.05),(w,d-.05)),('Left',(.05,0),(.05,d)),('Right',(w-.05,0),(w-.05,d)),('Partition',(p['bay'],0),(p['bay'],d-p['wall']))]:
 plinth_wall(name,a,b,p['plinth']);flat_boards(name+' horizontal boarding',a,b,p['plinth'],e,black)
for xx in [.05,w-.05]:gable_boards('Gable boarding','x',xx,d,e-.10,r-.10,black)
# Full-height partition follows the roof profile.
gable_boards('Partition upper boarding','x',p['bay'],d,e-.10,r-.10,black)
for xx in [v/1000 for v in post_positions()]:cube('Front post - 150 assumed',(xx,.075,e/2),(.15,.15,e),frame,.008)
cube('Front beam - 180 deep assumed',(w/2,.075,e-.09),(w,.15,.18),oak_beam,.008)
for xx,direction in [(p['bay'],1),(2*p['bay'],-1),(2*p['bay'],1),(w-p['post']/2,-1)]:curved_brace(xx,direction,e)
# Door leaves fill first opening, below beam. Keep two open bays.
doorw=clear_openings()[0]/1000;doorh=e-.18
for leaf in range(2):
 left=.15+leaf*doorw/2
 cube('Left bay double door '+str(leaf+1),(left+doorw/4,.085,doorh/2),(doorw/2-.012,.065,doorh-.015),black,.004)
 for k in range(8):
  cube('Door vertical board',(left+(k+.5)*(doorw/2)/8,.046,doorh/2),(doorw/16-.006,.025,doorh-.02),frame,.002)
 for zz in [.45,1.65]:cube('Door strap hinge',(left+(.25 if leaf==0 else doorw/2-.25),.02,zz),(.40,.018,.045),hardware,.005)
 cube('Door handle',(left+(doorw/2-.08 if leaf==0 else .08),.00,1.02),(.025,.035,.16),hardware,.007)
roofs('Proposed roof',w,d,e-.09,r-.09,'x',p['overhang'],p['overhang'],roof,p['roof_thickness'])
pantiles(w,d,e,r,p['overhang'])
# Rainwater goods suggested by S7; route and capacity are not designed.
for yy in [-p['overhang']-.025,d+p['overhang']+.025]:
 cube('Dark gutter - illustrative',(w/2,yy,e-(r-e)/(d/2)*p['overhang']-.10),(w+2*p['overhang'],.10,.10),hardware,.025)
beam('Downpipe - illustrative',(w-.04,-.13,.05),(w-.04,-.13,e-.18),.075,hardware)

cars=collection('SCALE CAR - generic 4500 x 1800 x 1450');current=cars
cp=values('car');cw,cl,ch=[cp[k]/1000 for k in ['width','length','height']];cx,cy=1.5*p['bay'],d/2+.15
cube('Car lower body',(cx,cy,.57),(cw-.08,cl,.57),carpaint,.17)
cube('Car bonnet',(cx,cy-cl/2+.65,.89),(cw-.14,1.25,.20),carpaint,.09)
# Tapered cabin as custom mesh.
x0=cx-(cw-.20)/2;x1=cx+(cw-.20)/2;yt=cy-1.02;yb=cy+1.2
verts=[(x0,yt,.9),(x1,yt,.9),(x1,yb,.9),(x0,yb,.9),(x0+.16,yt+.5,ch),(x1-.16,yt+.5,ch),(x1-.16,yb-.35,ch),(x0+.16,yb-.35,ch)]
mesh('Car glass cabin',verts,[(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7),(4,5,6,7)],glass)
cube('Car roof',(cx,cy+.15,ch-.035),(cw-.48,1.24,.065),carpaint,.035)
for xx in [cx-cw/2+.055,cx+cw/2-.055]:
 for yy in [cy-1.42,cy+1.42]:
  bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=.31,depth=.11,location=(xx,yy,.31),rotation=(0,math.pi/2,0));o=assign(bpy.context.object);o.name='Car tyre';o.data.materials.append(rubber)
  bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=.20,depth=.115,location=(xx,yy,.31),rotation=(0,math.pi/2,0));o=assign(bpy.context.object);o.name='Car wheel';o.data.materials.append(wheel)
for xx in [cx-.57,cx+.57]:cube('Headlight',(xx,cy-cl/2-.005,.75),(.40,.03,.12),lightmat,.02)

ex=collection('EXISTING - schematic massing, unsurveyed');current=ex
q={k:v/1000 for k,v in values('existing').items()};ew,ed,ee,er=q['width'],q['depth'],q['eaves'],q['ridge']
for a,b in [((.05,0),(.05,ed)),((ew-.05,0),(ew-.05,ed)),((0,ed-.05),(ew,ed-.05))]:flat_boards('Existing boarding',a,b,0,ee,old)
dw=q['door_width'];dx=(ew-dw)/2
flat_boards('Existing front left',(0,.05),(dx,.05),0,ee,old);flat_boards('Existing front right',(dx+dw,.05),(ew,.05),0,ee,old)
flat_boards('Existing door head',(dx,.05),(dx+dw,.05),q['door_height'],ee,old)
for yy in [.05,ed-.05]:gable_boards('Existing gable','y',yy,ew,ee,er,old)
for i in range(2):cube('Existing door - width unresolved',(dx+(i+.5)*dw/2,.045,q['door_height']/2),(dw/2-.008,.06,q['door_height']),old_door,.004)
roofs('Existing roof',ew,ed,ee,er,'y',q['gable_overhang'],q['eave_overhang'],oldroof)
cube('Existing approach',(ew/2,-q['approach']/2,-.035),(ew,q['approach'],.07),concrete)
ex.hide_render=True;ex.hide_viewport=True

current=None
floor=mat('Studio warm grey',(.69,.69,.65),.85)
cube('Neutral ground',(4,3,-.20),(200,200,.1),floor)
bpy.ops.object.light_add(type='AREA',location=(1,-5,11));key=bpy.context.object;key.name='Large softbox';key.data.energy=1900;key.data.shape='DISK';key.data.size=8
key.rotation_euler=(Vector((4,3,0))-key.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.object.light_add(type='SUN',location=(-5,-2,10));sun=bpy.context.object;sun.data.energy=2;sun.data.angle=.2;sun.rotation_euler=(.45,-.4,-.35)
bpy.ops.object.camera_add();cam=bpy.context.object;cam.name='Review camera';scene.camera=cam;cam.data.type='ORTHO';cam.data.lens=50

def camera(loc,target,scale):
 cam.location=loc;cam.rotation_euler=(Vector(target)-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.ortho_scale=scale

def render(name,loc,target,scale):
 camera(loc,target,scale);scene.render.filepath=str(OUT/'renders'/f'{name}.png');bpy.ops.render.render(write_still=True)

camera((13,-13,8),(4.5,2.7,1.8),13.7)
scene['status']=DATA['status'];scene['roof_pitch_degrees']=pitch('proposed');scene['parameter_source']='data/parameters.json';scene['open_bays']=2
readme=bpy.data.texts.new('READ ME - preliminary model');readme.write('P02 preliminary review model. All dimensions reference-only.\nLeft-hand defined facing entrance. Proposed roof top: eaves 2.3m at wall, ridge 4.163m.\nRoof 30deg source note conflicts. Oak frame, natural boarding and red pantile-style roof requested by Dad; S7 caption names concrete tiles, exact product unresolved. Members, joints, pantile product, overhangs and existing door width remain unverified.\nExisting collection hidden by default; enable for inspection. No surveyed site/context.\n')
for screen in bpy.data.screens:
 for area in screen.areas:
  if area.type=='VIEW_3D':
   area.spaces.active.region_3d.view_perspective='CAMERA'
   area.spaces.active.overlay.show_overlays=False
   area.spaces.active.shading.type='MATERIAL'
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'model'/'garage-baseline-P02.blend'))
# Machine-readable verification before rendering.
report={'proposed_pitch_deg':pitch('proposed'),'existing_pitch_deg':pitch('existing'),'clear_openings_mm':clear_openings(),'open_bays':2,'door_leaves':2,'car_body_dimensions_mm':cp,'object_count':len(bpy.data.objects),'roof_top_ridge_m':r,'materials_source':'Dad 14 Sep 2026 22:01','site_photo':'S5 - context only, unmeasured','eaves_at_wall_m':e}
(OUT/'model'/'geometry-report.json').write_text(json.dumps(report,indent=2))
render('proposed-front-three-quarter',(13,-13,8),(4.5,2.7,1.8),13.7)
render('proposed-entrance',(4.5,-18,3.8),(4.5,2,1.8),11.5)
render('proposed-rear-three-quarter',(-7,16,9),(4.5,3,1.8),13.7)
# Same camera and scale for two comparable massing renders; no car.
cars.hide_render=True
render('massing-proposed',(13,-13,8),(4.5,2.7,1.8),13.7)
pro.hide_render=True;ex.hide_render=False;ex.hide_viewport=False
# Centre existing on same plan centre and same ground datum as proposed.
for o in ex.objects:o.location.x+=(w-ew)/2;o.location.y+=(d-ed)/2
render('massing-existing',(13,-13,8),(4.5,2.7,1.8),13.7)
print('Blender model and five renders complete.')
