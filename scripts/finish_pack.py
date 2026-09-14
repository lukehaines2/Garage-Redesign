"""Compose review boards and package deliverables; does not alter source renders."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,zipfile,hashlib
from common import OUT,REV,ROOT,values,pitch
out=OUT;renders=out/'renders'
model=out/'model/garage-baseline-P02.blend'
for name in ['proposed-front-three-quarter','proposed-entrance','proposed-rear-three-quarter','massing-existing','massing-proposed']:
 assert (renders/f'{name}.png').stat().st_mtime>=model.stat().st_mtime, f'Stale render: {name}'
verification=json.loads((out/'model/geometry-verification.json').read_text())
assert verification['result']=='PASS' and verification['model_sha256']==hashlib.sha256(model.read_bytes()).hexdigest(), 'Verify current Blender model first'
fontpaths=['/System/Library/Fonts/Supplemental/Arial.ttf','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
fontpath=next((p for p in fontpaths if Path(p).exists()),None)
def font(size):return ImageFont.truetype(fontpath,size) if fontpath else ImageFont.load_default(size=size)
ink='#26353c';muted='#536268';bg='#f5f5f1'
# Two views rendered with identical camera position, target and orthographic scale.
im=Image.new('RGB',(2400,1090),bg);d=ImageDraw.Draw(im)
d.text((45,25),'EXISTING / PROPOSED - SAME CAMERA SCALE',font=font(35),fill=ink)
d.text((45,75),'P02 preliminary massing study | Centre-aligned for comparison; not a site overlay',font=font(22),fill=muted)
for i,(name,title) in enumerate([('existing','Existing garage'),('proposed','Proposed cart lodge')]):
 pic=Image.open(renders/f'massing-{name}.png').convert('RGB').resize((1200,840));im.paste(pic,(1200*i,120));d.text((45+1200*i,975),title,font=font(28),fill=ink)
 p=values(name);d.text((45+1200*i,1019),f"{p['width']/1000:g} x {p['depth']/1000:g} m walls | Ridge {p['ridge']/1000:g} m | Reference dimensions",font=font(21),fill=muted)
im.save(renders/'massing-comparison-P02.png')
# Three render views, clearly carrying provisional status and essential assumptions.
board=Image.new('RGB',(2400,1990),bg);d=ImageDraw.Draw(board)
d.text((45,26),'GARAGE REPLACEMENT / BASELINE P02',font=font(40),fill=ink)
d.text((45,85),'Natural oak frame and boarding / red profiled tiles | One enclosed bay + two open bays',font=font(27),fill=muted)
views=[('proposed-front-three-quarter','01  Front three-quarter'),('proposed-entrance','02  Entrance'),('proposed-rear-three-quarter','03  Rear three-quarter')]
for i,(name,title) in enumerate(views):
 x=(i%2)*1200;y=145+(i//2)*900
 pic=Image.open(renders/f'{name}.png').convert('RGB').resize((1200,840));board.paste(pic,(x,y));d.text((x+35,y+847),title,font=font(25),fill=ink)
x,y=1245,1120
for text,size in [('REFERENCE DIMENSIONS',31),('9.0 x 6.0 m footprint',27),('2.300 m eaves / 4.163 m ridge',27),(f"Derived roof pitch: {pitch('proposed'):.2f} degrees",27),('',20),('Source 30-degree pitch remains unresolved.',23),('Oak frame / natural timber / red profiled tiles.',23),('Car body: 4.50 x 1.80 x 1.45 m; mirrors omitted.',23),('Frame sizes, tile product and siting unverified.',23),('',20),('PRELIMINARY',31),('Reference dimensions, subject to verification.',23)]:
 d.text((x,y),text,font=font(size),fill=ink if size==31 else muted);y+=size+19
board.save(renders/'baseline-review-board-P02.png')
# Reproducible local bundle; source references included, temporary runtime excluded.
archive=out/'garage-review-pack-P02.zip'
files=[]
for folder in ['scripts','data','Original Ref docs',*[str((OUT/n).relative_to(ROOT)) for n in ['pdf','svg','model','renders']]]:
 files.extend(p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.blend1')
files.extend(ROOT/n for n in ['README.md','PROJECT_BRIEF.md','MEASUREMENTS_FOR_DAD.md','requirements.txt'])
files.extend(p for p in [out/'validation-report.json',out/'QA_NOTES.md'] if p.exists())
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(files):z.write(p,p.relative_to(ROOT))
print(f'Created two review boards and {archive.name} ({archive.stat().st_size/1e6:.1f} MB)')
