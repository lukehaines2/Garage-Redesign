"""Copy the validated review pack into an independent static Sites source tree."""
from pathlib import Path
from html import escape
import json, re, hashlib, shutil

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
SOURCE=SITE/'source'
PACK=ROOT/'output/Share/Billeaford-Hall-full-review'
SOURCE.mkdir(parents=True,exist_ok=True)
for path in PACK.rglob('*'):
    if path.is_file():
        dest=SOURCE/path.relative_to(PACK)
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(path,dest)

# The online document loads quickly; geometry arrives separately from the same origin.
viewer=SOURCE/'output/V4/viewer/garage-V4-viewer.html'
html=viewer.read_text()
html=re.sub(r'<script id="model" type="application/json">.*?</script>',
    '<script id="model" type="application/json" data-src="model-data.json"></script>',html,flags=re.S)
html=html.replace('No installation or internet connection required.','No Blender installation required.')
viewer.write_text(html)
shutil.copyfile(ROOT/'output/V4/viewer/model-data.json',viewer.with_name('model-data.json'))

# Keep each static file modest while offering one complete, byte-identical ZIP download.
archive=ROOT/'output/Share/Billeaford-Hall-full-review.zip'
content=archive.read_bytes()
downloads=SOURCE/'downloads';downloads.mkdir(exist_ok=True)
manifest={'filename':archive.name,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),'parts':[]}
chunk_size=8*1024*1024
for n,start in enumerate(range(0,len(content),chunk_size)):
    chunk=content[start:start+chunk_size]
    filename=f'full-pack-{n+1:02d}.bin'
    (downloads/filename).write_bytes(chunk)
    manifest['parts'].append({'url':'downloads/'+filename,'bytes':len(chunk),'sha256':hashlib.sha256(chunk).hexdigest()})
(downloads/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')

index=(SOURCE/'START-HERE.html').read_text()
index=index.replace('The current V4 brief and model, with the earlier drawings and design options retained for reference.',
    'Inspect the current V4 model and drawings, or download the complete pack for Blender and Cursor.')
index=index.replace('<div class="grid"><section class="card"><h3>1. Inspect',
    '<div class="grid"><section class="card"><h3>1. Inspect',1)
index=index.replace('<section class="card"><h2 style="margin-top:0">Use this pack with Cursor Agent</h2>',
    '<section class="card"><h2 style="margin-top:0">Use this pack with Cursor Agent</h2><p><button class="button" id="download-pack" type="button">Download complete pack · 50 MB</button><span id="download-status" role="status" aria-live="polite"></span></p>')
index=index.replace('This folder is self-contained and works offline. Nothing has been uploaded or published.',
    'This is the online review pack. The complete download also works offline.')
index=index.replace('</body>','<script src="download-pack.js"></script></body>')
(SOURCE/'index.html').write_text(index)
(SOURCE/'START-HERE.html').write_text(index)
(SOURCE/'404.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Page not found · Garage review</title><body style="font:18px/1.6 system-ui;padding:40px"><h1>This page could not be found</h1><p><a href="/">Back to the full garage review pack</a></p></body></html>')
(SOURCE/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print(json.dumps({'files':sum(p.is_file() for p in SOURCE.rglob('*')),'viewer_page_bytes':viewer.stat().st_size,'zip_parts':len(manifest['parts'])},indent=2))
