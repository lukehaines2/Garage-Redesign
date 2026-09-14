"""Generate true-scale A3 PDF and SVG sheets; coordinates below are paper mm."""
import math, html, json
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from common import OUT,REV,ROOT,DATA,values,pitch,clear_openings,post_positions
INK='#26353c'; LIGHT='#879399'
class Sheet:
 def __init__(self,c,title,no):
  self.c=c; self.svg=[]; self.no=no
  self.rect(8,8,404,281,stroke=INK)
  self.text(16,20,'GARAGE REPLACEMENT / DESIGN REVIEW',5,bold=True)
  self.text(16,29,title,3.8)
  self.line(16,35,404,35)
  self.line(16,258,404,258)
  self.text(16,266,DATA['status'],3.2,bold=True)
  self.text(16,273,'A3 landscape | 1:50 at 100% print | Dimensions mm | Do not scale JPEG references',2.8)
  self.text(16,280,'Site/address and compass orientation unconfirmed | 14 Sep 2026 | Revision P02',2.7)
  self.text(404,280,no,3.3,anchor='end',bold=True)
  self.text(340,264,'Scale 1:50',2.5)
  for i in range(4): self.rect(340+i*10,268,10,2,fill=INK if i%2==0 else '#ffffff')
  for i in range(3): self.text(340+i*20,275,str(i)+' m',2.3)
 def line(self,x1,y1,x2,y2,color=INK,w=.25,dash=False):
  c=self.c;c.setStrokeColor(color);c.setLineWidth(w*mm);c.setDash([2*mm,1*mm] if dash else [])
  c.line(x1*mm,(297-y1)*mm,x2*mm,(297-y2)*mm)
  self.svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"'+(' stroke-dasharray="2 1"' if dash else '')+'/>')
 def rect(self,x,y,w,h,fill=None,stroke=INK):
  self.poly([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],fill,stroke)
 def poly(self,pts,fill=None,stroke=INK):
  c=self.c;c.setStrokeColor(stroke);c.setLineWidth(.25*mm);c.setDash([])
  p=c.beginPath();p.moveTo(pts[0][0]*mm,(297-pts[0][1])*mm)
  for x,y in pts[1:]:p.lineTo(x*mm,(297-y)*mm)
  p.close()
  if fill:c.setFillColor(fill)
  c.drawPath(p,stroke=1,fill=int(bool(fill)))
  self.svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="{fill or "none"}" stroke="{stroke}" stroke-width="0.25"/>')
 def text(self,x,y,t,size=3,anchor='start',bold=False,color=INK):
  c=self.c;c.setFillColor(color);c.setFont('Helvetica-Bold' if bold else 'Helvetica',size*mm)
  getattr(c,{'start':'drawString','middle':'drawCentredString','end':'drawRightString'}[anchor])(x*mm,(297-y)*mm,t)
  self.svg.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" text-anchor="{anchor}" font-weight="{"bold" if bold else "normal"}" fill="{color}">{html.escape(t)}</text>')
 def dim(self,x1,x2,y,at,label):
  for x in (x1,x2):
   self.line(x,at,x,y+2,LIGHT,.15);self.line(x-1,y+1,x+1,y-1,w=.3)
  self.line(x1,y,x2,y,w=.18);self.text((x1+x2)/2,y-2,label,2.8,'middle')
 def vdim(self,y1,y2,x,at,label):
  for y in (y1,y2):
   self.line(at,y,x+2,y,LIGHT,.15);self.line(x-1,y+1,x+1,y-1,w=.3)
  self.line(x,y1,x,y2,w=.18)
  if x<at:self.text(x-2,(y1+y2)/2,label,2.7,'end')
  else:self.text(x+3,(y1+y2)/2,label,2.7)
 def notes(self,x,y,lines):
  for i,t in enumerate(lines):self.text(x,y+i*5,t,2.9)
 def finish(self):
  (OUT/'svg'/f'{self.no}.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 420 297">'+''.join(self.svg)+'</svg>')
  self.c.showPage()

def wall_hatch(s,x,y,w,h):
 for dy in range(3,int(h),3):s.line(x,y+dy,x+w,y+dy,LIGHT,.1)

def plan(c,name):
 p=values(name);pro=name=='proposed';w=p['width']/50;d=p['depth']/50
 s=Sheet(c,f'{name.title()} building / floor plan',('PR' if pro else 'EX')+'-101')
 x,y=40,60;t=p['wall']/50
 s.rect(x,y,w,d,fill='#f7f8f8');s.rect(x,y,w,t,fill='#b9c0c3');s.rect(x,y,t,d,fill='#b9c0c3');s.rect(x+w-t,y,t,d,fill='#b9c0c3')
 if pro:
  xs=post_positions();post=p['post']/50
  for pos in xs:s.rect(x+pos/50-post/2,y+d-post,post,post,fill=INK)
  s.rect(x+p['bay']/50-t/2,y,t,d,fill='#b9c0c3')
  dw=clear_openings()[0]/50;dx=x+p['post']/50
  for i in range(2):s.rect(dx+i*dw/2,y+d-.8,dw/2-.2,.8,fill='#c6a67d')
  s.line(dx+dw/2,y+d+2,dx+dw/2,y+d+10,LIGHT,.2)
  s.text(dx+dw/2,y+d+15,'Paired doors',2.7,'middle')
  for i,label in enumerate(['ENCLOSED BAY','OPEN BAY 1','OPEN BAY 2']):
   s.text(x+30+i*60,y+d/2,label,3,'middle',True)
  s.text(x+30,y+d/2+6,'Partition assumed',2.5,'middle')
  for i in range(3):s.dim(x+i*60,x+(i+1)*60,y-8,y,'3000 nominal')
  s.notes(245,69,['FLOOR PLAN NOTES','Front is the vehicle entrance.','Left bay: paired doors.','Full partition is provisional.','Dashed outline = assumed roof extent.','','Clear openings from assumed posts:',*[f'Bay {i+1}: {v:.0f} mm (provisional)' for i,v in enumerate(clear_openings())],'','150 mm posts; 100 mm walls assumed.','Nominal bay divisions are not clear widths.','No foundations or structure specified.','Dark rainwater goods per S7; route TBC.'])
 else:
  s.rect(x,y+d-t,w,t,fill='#b9c0c3')
  dw=p['door_width']/50;dx=x+(w-dw)/2
  s.rect(dx,y+d-t,dw,t,fill='#ffffff')
  s.line(dx,y+d,dx+dw,y+d,dash=True)
  ap=p['approach']/50;s.rect(x,y+d,w,ap,fill='#edf0ee')
  s.text(x+w/2,y+d+ap/2,'Concrete approach',2.5,'middle')
  s.dim(x,x+w,y-8,y,'3500')
  s.vdim(y,y+d,x+w+10,x+w,'6800')
  s.vdim(y+d,y+d+ap,x+w+10,x+w,'1200')
  s.vdim(y,y+d+ap,x+w+35,x+w,'8000 incl. approach')
  s.notes(205,70,['EXISTING GARAGE / DEMOLITION','Building footprint: 6800 x 3500.','Roof length annotation: 7200.','Approach: 1200 beyond entrance.','','Door width is unresolved.','Dashed entrance is schematic only.','1100 source label may describe one leaf.','','Side elevations are partly cropped.','Additional openings are not established.','100 mm wall thickness is schematic.'])
  s.text(x+w/2,y+d/2,'EXISTING GARAGE',2.7,'middle',True)
 ox=(p['overhang'] if pro else p['eave_overhang'])/50;oy=(p['overhang'] if pro else p['gable_overhang'])/50
 for a,b in [((x-ox,y-oy),(x+w+ox,y-oy)),((x+w+ox,y-oy),(x+w+ox,y+d+oy)),((x+w+ox,y+d+oy),(x-ox,y+d+oy)),((x-ox,y+d+oy),(x-ox,y-oy))]:s.line(*a,*b,LIGHT,.18,True)
 if not pro:s.vdim(y-oy,y+d+oy,x-10,x-ox,'7200 roof')
 s.dim(x,x+w,239,y+d,str(p['width'])+' wall footprint')
 if pro:s.vdim(y,y+d,x+w+10,x+w,'6000')
 s.line(x+w/2,250,x+w/2,243);s.text(x+w/2,254,'FRONT / ENTRANCE',2.7,'middle')
 s.finish()

def elevation(c,name,view):
 p=values(name);pro=name=='proposed';gable=(view in ['left','right']) if pro else (view in ['front','rear'])
 width=(p['depth'] if gable else p['width']) if pro else (p['width'] if gable else p['depth'])
 w=width/50;e=p['eaves']/50;r=p['ridge']/50;x=75;y=175
 s=Sheet(c,f'{name.title()} building / {view} elevation',('PR' if pro else 'EX')+'-'+{'front':'201','rear':'202','left':'203','right':'204'}[view])
 s.rect(x,y-e,w,e,fill='#f5f6f5');wall_hatch(s,x,y-e,w,e)
 ov=(p['overhang'] if pro else p['eave_overhang'])/50
 endov=(p['overhang'] if pro else p['gable_overhang'])/50
 if gable:
  s.poly([(x,y-e),(x+w/2,y-r),(x+w,y-e)],'#f5f6f5')
  for h in range(3,int(r-e),3):
   inset=(h/(r-e))*w/2;s.line(x+inset,y-e-h,x+w-inset,y-e-h,LIGHT,.1)
 else:
  s.rect(x-endov,y-r,w+endov*2,r-e+(r-e)*ov/( (p['depth'] if pro else p['width'])/100),fill='#e6c7b5' if pro else '#e6e9e9')
  for i in range(4,int(w),5):s.line(x+i,y-r,x+i,y-e,LIGHT,.1)
  if pro:
   for row in range(4,int(r-e),4):s.line(x-endov,y-r+row,x+w+endov,y-r+row,LIGHT,.1)
 if pro and view=='front':
  s.rect(x,y-e,w,e,fill='#ffffff')
  post=p['post']/50;beam=p['beam_depth']/50
  s.rect(x,y-e,w,beam,fill='#c6a67d')
  for pos in post_positions():s.rect(x+pos/50-post/2,y-e,post,e,fill='#c6a67d')
  dw=clear_openings()[0]/50;dx=x+post
  s.rect(dx,y-e+beam,dw,e-beam,fill='#e9dcc6')
  for i in range(1,14):s.line(dx+dw*i/14,y-e+beam,dx+dw*i/14,y,LIGHT,.1)
  s.line(dx+dw/2,y-e+beam,dx+dw/2,y,w=.4)
  for bx,direction in [(p['bay']/50,1),(2*p['bay']/50,-1),(2*p['bay']/50,1),((p['width']-p['post']/2)/50,-1)]:
   pts=[]
   for u in [j/8 for j in range(9)]:pts.append((x+bx+direction*10.4*u,y-e+4.4+10*(1-u)**2))
   pts.extend((a,b-2) for a,b in reversed(pts.copy()));s.poly(pts,'#c6a67d')
  for i in [1,2]:s.text(x+30+60*i,y-18,'OPEN',3.2,'middle')
  for i in range(3):s.dim(x+60*i,x+60*(i+1),y+25,y,'3000 nominal')
 elif pro:
  s.rect(x,y-p['plinth']/50,w,p['plinth']/50,fill='#e3d3cb')
 elif view=='front':
  dw=p['door_width']/50;dh=p['door_height']/50;dx=x+(w-dw)/2
  s.rect(dx,y-dh,dw,dh,fill='#c4ded9');s.line(dx+dw/2,y-dh,dx+dw/2,y)
  s.text(x,y+35,'Door width/position schematic; verify 1100 label.',2.8)
  s.text(x,y+41,'Door height 2000 from reference.',2.8)
 if gable:
  drop=(r-e)*ov/(w/2)
  s.line(x-ov,y-e+drop,x+w/2,y-r,w=.4);s.line(x+w/2,y-r,x+w+ov,y-e+drop,w=.4)
 s.line(x-8,y,x+w+8,y,w=.5)
 s.dim(x,x+w,y+13,y,str(width)+' wall extent')
 s.vdim(y-r,y,x+w+13,x+w,str(p['ridge'])+' ridge')
 s.vdim(y-e,y,x-13,x,str(p['eaves'])+' eaves')
 s.text(x,52,'All heights relative to provisional ground datum 0.',3)
 if pro:s.notes(x,226,[f'Roof: {pitch(name):.2f} deg derived from span and heights; source 30 deg conflicts.','Traditional oak frame / natural timber boarding / red profiled roof tiles (S6/S7).','Red brick plinth retained; frame sizes, joints and clay/concrete tile product unverified.'])
 else:s.notes(x,226,['Photo S5: weathered timber and blue-green doors; roof covering still to be verified.', 'S2 labels roof corrugated; photograph appears tiled - confirm covering.', 'Side openings unresolved where original image is cropped.' if view in ['left','right'] else 'Front doors schematic; rear reference indicates no openings.'])
 s.finish()

def section(c,name):
 p=values(name);pro=name=='proposed';span=p['depth'] if pro else p['width'];w=span/50;e=p['eaves']/50;r=p['ridge']/50;x=75;y=171
 s=Sheet(c,f'{name.title()} building / schematic roof section',('PR' if pro else 'EX')+'-301')
 s.line(x,y,x,y-e,w=.6);s.line(x+w,y,x+w,y-e,w=.6)
 s.line(x,y-e,x+w/2,y-r,w=.6);s.line(x+w/2,y-r,x+w,y-e,w=.6)
 s.line(x-5,y,x+w+5,y,w=.5);s.line(x+w/2,y-r,x+w/2,y,dash=True)
 s.dim(x,x+w,y+13,y,str(span)+' span')
 s.vdim(y-r,y,x+w+12,x+w,str(p['ridge'])+' ridge')
 s.vdim(y-e,y,x-12,x,str(p['eaves'])+' eaves')
 s.text(x,53,f'Geometric section | pitch {pitch(name):.2f} deg',3.5,bold=True)
 s.notes(245,75,['DATUM / GEOMETRY NOTES','Ground = provisional 0.','Eaves = roof surface at wall line.','Ridge = highest roof surface.','No roof build-up designed.','No foundations shown.','','Section is geometric, not structural.','Verify heights and ground levels.'])
 if pro:s.notes(x,212,['30 deg in the source would give a ridge of approximately 4032 mm.','P02 preserves 4163 mm and derives approximately 31.84 deg.','Source 3572 slope dimension has unresolved endpoints.','Pantile profile/ridge illustrated; 150 mm overhang and tile product unverified.'])
 else:s.notes(x,212,['Reference roof length 7200 versus wall length 6800.', 'Model assumes 200 mm overhang at each end; distribution unverified.', 'Eave overhang 100 mm is a visual assumption.', 'Section cuts across 3500 width; length/approach shown separately on plan.'])
 s.finish()

def main():
 for name in ['existing','proposed']:
  c=canvas.Canvas(str(OUT/'pdf'/f'{name}-drawings-P02.pdf'),pagesize=(420*mm,297*mm))
  c.setTitle(f'{name.title()} garage - preliminary drawing pack P02')
  plan(c,name)
  for view in ['front','rear','left','right']:elevation(c,name,view)
  section(c,name);c.save()
 print('Created two 6-page A3 drawing packs and 12 SVG sheets.')
if __name__=='__main__':main()
