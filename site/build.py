"""Build and validate the static review site. No external dependencies."""
from pathlib import Path
from urllib.parse import unquote
import json,re,shutil,hashlib
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'source'
DEST=ROOT/'dist'
shutil.copytree(SOURCE,DEST,dirs_exist_ok=True)
shutil.copyfile(ROOT/'download-pack.js',DEST/'download-pack.js')
broken=[]
for path in DEST.rglob('*.html'):
    if 'scripts' in path.relative_to(DEST).parts:continue
    for target in re.findall(r'(?:href|src|data-src)="([^"]+)"',path.read_text()):
        if target.startswith(('https:','http:','data:','#')):continue
        clean=unquote(target.split('#')[0])
        dest=DEST/clean.lstrip('/') if clean.startswith('/') else path.parent/clean
        if dest.is_dir():dest=dest/'index.html'
        if not dest.is_file():broken.append([str(path.relative_to(DEST)),target])
assert not broken,broken
manifest=json.loads((DEST/'downloads/manifest.json').read_text())
digest=hashlib.sha256();size=0
for part in manifest['parts']:
    content=(DEST/part['url']).read_bytes()
    assert len(content)==part['bytes'] and hashlib.sha256(content).hexdigest()==part['sha256']
    size+=len(content);digest.update(content)
assert size==manifest['bytes'] and digest.hexdigest()==manifest['sha256']
assert all(path.stat().st_size<25*1024*1024 for path in DEST.rglob('*') if path.is_file())
viewer=(DEST/'output/V4/viewer/garage-V4-viewer.html').read_text()
assert '__MODEL_DATA__' not in viewer and 'data-src="model-data.json"' in viewer
assert (DEST/'START-HERE.html').read_bytes()==(DEST/'index.html').read_bytes()
print(json.dumps({'result':'PASS','broken_links':broken,'complete_zip_bytes':size,'largest_asset_bytes':max(p.stat().st_size for p in DEST.rglob('*') if p.is_file())},indent=2))
