"""Compose matched V2/V3 comparison boards and package editable options."""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1];out=ROOT/'output/V3'
fontpath='/System/Library/Fonts/Supplemental/Arial.ttf'
def font(n):return ImageFont.truetype(fontpath,n)
reports=json.loads((out/'geometry-verification.json').read_text())
saved=json.loads((out/'saved-model-verification.json').read_text())
for r in saved:
 assert r['result']=='PASS' and hashlib.sha256((out/'models'/f"garage-V3-{r['option']}.blend").read_bytes()).hexdigest()==r['saved_model_sha256']
for r in reports:
 model=out/'models'/f"garage-V3-{r['option']}.blend"
 assert r['result']=='PASS' and hashlib.sha256(model.read_bytes()).hexdigest()==r['model_sha256']
 for view in ['front-three-quarter','entrance','rear-three-quarter']:
  assert (out/'renders'/f"V3-{r['option']}-{view}.png").stat().st_mtime>=model.stat().st_mtime
labels=[('V2 / oak cart lodge','Left closed; two open bays'),('V3-A / natural timber barn','Both ends closed; centre open'),('V3-B / weathered timber','Left closed; two open bays')]
for view in ['front-three-quarter','entrance','rear-three-quarter']:
 im=Image.new('RGB',(2250,755),'#f5f5f1');d=ImageDraw.Draw(im)
 d.text((30,20),'V2 / V3 DESIGN ALTERNATIVES — '+view.replace('-',' ').upper(),font=font(30),fill='#25363b')
 d.text((30,65),'Same 9 x 6 m baseline, roof heights, Model Y, camera and lighting. Preliminary; no option selected.',font=font(22),fill='#536268')
 for i,(title,subtitle) in enumerate(labels):
  path=ROOT/'output/P02/renders'/f'proposed-{view}.png' if i==0 else out/'renders'/f"V3-{'A' if i==1 else 'B'}-{view}.png"
  pic=Image.open(path).convert('RGB').resize((750,525));im.paste(pic,(i*750,110));d.text((i*750+25,650),title,font=font(27),fill='#25363b');d.text((i*750+25,693),subtitle,font=font(22),fill='#536268')
 im.save(out/f'comparison-{view}.png')
paths=[ROOT/'data/parameters.json',ROOT/'data/v3-options.json',ROOT/'scripts/v3_scene.py',ROOT/'scripts/finish_v3.py',ROOT/'scripts/verify_v3.py',ROOT/'output/P02/model/garage-baseline-P02.blend',ROOT/'PROJECT_BRIEF.md',ROOT/'WORK_STATUS.md',ROOT/'MEASUREMENTS_FOR_DAD.md',ROOT/'Original Ref docs/V3-barn-style-timber-doors-reference.jpg']
paths += [p for p in out.rglob('*') if p.is_file() and p.suffix not in ['.zip','.blend1']]
with zipfile.ZipFile(out/'garage-V3-review-pack.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in paths:z.write(p,p.relative_to(ROOT))
with zipfile.ZipFile(out/'garage-V3-review-pack.zip') as z:assert z.testzip() is None
print('V3 comparison boards and archive complete')
