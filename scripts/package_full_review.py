"""Build the offline family review pack. Never upload or publish anything."""
from pathlib import Path, PurePosixPath
from zipfile import ZipFile, ZIP_DEFLATED
from html import escape
from urllib.parse import quote, unquote
import json, re, shutil, hashlib, struct
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/Share'
PACK=OUT/'Billeaford-Hall-full-review'
PACK.mkdir(parents=True,exist_ok=True)

def copy_bytes(rel,content):
    rel=PurePosixPath(rel)
    assert not rel.is_absolute() and '..' not in rel.parts
    dest=PACK/str(rel);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(content)

# Historical packages retain their original records in a separate folder.
for tag,name in [('P02','output/P02/garage-review-pack-P02.zip'),('V3','output/V3/garage-V3-review-pack.zip')]:
    with ZipFile(ROOT/name) as z:
        assert z.testzip() is None
        for entry in z.namelist():
            if entry.endswith('/'):continue
            if entry in ['PROJECT_BRIEF.md','WORK_STATUS.md','MEASUREMENTS_FOR_DAD.md','README.md']:
                copy_bytes('historical-records/'+tag+'/'+entry,z.read(entry))
            else:copy_bytes(entry,z.read(entry))

# Current sources and records take precedence. Exclude redundant nested ZIPs.
with ZipFile(ROOT/'output/V4/garage-V4-preparation-pack.zip') as z:
    for entry in z.namelist():
        if entry.endswith('/'):continue
        rel=entry.removeprefix('garage-V4-preparation/')
        if Path(rel).suffix!='.zip':copy_bytes(rel,z.read(entry))
for rel in ['PROJECT_BRIEF.md','WORK_STATUS.md','MEASUREMENTS_FOR_DAD.md','README.md','data/v4-design-intent.json',
            'scripts/v4_scene.py','scripts/verify_v4_model.py','scripts/v4_viewer_template.html','scripts/package_full_review.py']:
    copy_bytes(rel,(ROOT/rel).read_bytes())
onboarding_root=ROOT/'sharing/agent-onboarding'
onboarding_files=['AGENTS.md','START-WITH-CURSOR.md','LLM-PROJECT-CONTEXT.md','SETUP-BLENDER.md']
for rel in onboarding_files:
    copy_bytes(rel,(onboarding_root/rel).read_bytes())
copy_bytes('.cursor/rules/garage-review.mdc',(onboarding_root/'garage-review.mdc').read_bytes())
starter_text=(onboarding_root/'START-WITH-CURSOR.md').read_text()
starter_prompt=re.search(r'```text\n(.*?)\n```',starter_text,re.S).group(1)
for path in (ROOT/'output/V4').rglob('*'):
    if path.is_file() and path.suffix not in ['.zip','.blend1'] and path.name!='model-data.json':
        copy_bytes(path.relative_to(ROOT).as_posix(),path.read_bytes())
data=(ROOT/'output/V4/viewer/model-data.json').read_text()
viewer=(ROOT/'scripts/v4_viewer_template.html').read_text().replace('__MODEL_DATA__',data)
(ROOT/'output/V4/viewer/garage-V4-viewer.html').write_text(viewer)
copy_bytes('output/V4/viewer/garage-V4-viewer.html',viewer.encode())

CSS='''*{box-sizing:border-box}body{margin:0;background:#f5f3ed;color:#203d38;font:16px/1.55 system-ui,sans-serif}main{max-width:1120px;margin:auto;padding:38px 24px}h1{font-size:clamp(32px,5vw,54px);line-height:1.1;margin:12px 0}h2{font-size:24px;margin-top:32px}h3{font-size:18px}p{max-width:85ch}a{color:#1a6555;text-underline-offset:3px}a:focus-visible{outline:3px solid #ba8c2f;outline-offset:4px}.eyebrow{font-size:12px;letter-spacing:.13em}.muted{color:#60716b}.notice{background:#fff4d6;border-left:4px solid #ae8127;padding:14px 18px;border-radius:6px;margin:22px 0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}.card{background:#fff;padding:20px;border:1px solid #d0d9d1;border-radius:12px}.card h3{margin:0 0 8px}.button{display:inline-block;background:#234c3e;color:white;padding:11px 16px;border-radius:7px;text-decoration:none;margin:8px 8px 8px 0}.secondary{background:#e1eae3;color:#204536}img{max-width:100%;height:auto;border-radius:8px;border:1px solid #d4dbd4}.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}figure{margin:0}figcaption{font-size:14px;color:#60716b;padding:7px 0}ul,ol{padding-left:24px}li{margin:7px 0}footer{border-top:1px solid #cad3cb;margin-top:34px;padding-top:18px;font-size:13px}.badge{display:inline-block;font-size:12px;padding:4px 8px;background:#e2ece4;border-radius:20px}.historical{background:#ece9e2}.document{max-width:1000px}.document table{border-collapse:collapse;width:100%;font-size:14px;display:block;overflow-x:auto}.document th,.document td{border:1px solid #c6d1c7;padding:9px;text-align:left;vertical-align:top}.document th{background:#e5ece5}.document code{font-family:ui-monospace,monospace;font-size:13px;overflow-wrap:anywhere}.document pre{padding:16px;background:#e7ece5;white-space:pre-wrap;overflow-wrap:anywhere}.document blockquote{margin:15px 0;border-left:3px solid #a6b9a9;padding:0 18px;color:#506259}@media(max-width:650px){main{padding:24px 16px}.button{display:block;text-align:center}.grid,.gallery{grid-template-columns:1fr}}'''
def page(title,body,document=False):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+'</title><style>'+CSS+'</style></head><body><main'+(' class="document"' if document else '')+'>'+body+'</main></body></html>'

docs=['MEASUREMENTS_FOR_DAD.md','PROJECT_BRIEF.md','WORK_STATUS.md','output/V4/HEIGHT_AND_CONSTRUCTION.md',
      'output/V4/MAPPING_FEASIBILITY.md','output/V4/POSITIONING_THE_NEW_GARAGE.md','output/V4/DRAWING_REGISTER.md',
      'output/V4/DIY_WORKFLOW.md','Original Ref docs/V4-dad-answers-2026-09-23.md',
      'START-WITH-CURSOR.md','LLM-PROJECT-CONTEXT.md','SETUP-BLENDER.md']
doc_names={rel:rel.replace('/','-').replace(' ','-').removesuffix('.md')+'.html' for rel in docs}
(PACK/'readable-notes').mkdir(exist_ok=True)
def md_html(text,source):
    def inline(s):
        tokens=[]
        def link(m):
            label,target=m.group(1),m.group(2).strip('<>')
            if target.startswith(('https://','http://')):href=target
            else:
                dest=(PACK/Path(source).parent/unquote(target)).resolve()
                try:rel=dest.relative_to(PACK.resolve()).as_posix()
                except ValueError:rel=''
                if rel in doc_names:href=doc_names[rel]
                elif dest.is_file() and rel:href='../'+quote(rel)
                else:return label
            tokens.append('<a href="'+escape(href,quote=True)+'">'+escape(label)+'</a>')
            return 'ZZLINK'+str(len(tokens)-1)+'ZZ'
        s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
        s=escape(s);s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s);s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
        for n,t in enumerate(tokens):s=s.replace('ZZLINK'+str(n)+'ZZ',t)
        return s
    lines=text.splitlines();html=[];i=0
    while i<len(lines):
        line=lines[i];s=line.strip()
        if not s:i+=1;continue
        if s.startswith('```'):
            block=[];i+=1
            while i<len(lines) and not lines[i].startswith('```'):block.append(lines[i]);i+=1
            html.append('<pre>'+escape('\n'.join(block))+'</pre>');i+=1;continue
        if s.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=lines[i].strip().strip('|').split('|')
                if not all(re.fullmatch(r'\s*:?-+:?\s*',c) for c in row):rows.append(row)
                i+=1
            html.append('<table>')
            for n,row in enumerate(rows):
                tag='th' if n==0 else 'td';html.append('<tr>'+''.join('<'+tag+'>'+inline(c.strip())+'</'+tag+'>' for c in row)+'</tr>')
            html.append('</table>');continue
        heading=re.match(r'^(#{1,6})\s+(.+)',s)
        if heading:
            level=min(4,len(heading[1]));html.append(f'<h{level}>'+inline(heading[2])+f'</h{level}>');i+=1;continue
        if re.match(r'^(- |\d+\. )',s):
            tag='ul' if s.startswith('- ') else 'ol';html.append('<'+tag+'>')
            while i<len(lines) and re.match(r'^(- |\d+\. )',lines[i].strip()):
                html.append('<li>'+inline(re.sub(r'^(- |\d+\. )','',lines[i].strip()))+'</li>');i+=1
            html.append('</'+tag+'>');continue
        if s.startswith('>'):html.append('<blockquote>'+inline(s.lstrip('> ').strip())+'</blockquote>');i+=1;continue
        html.append('<p>'+inline(s)+'</p>');i+=1
    return ''.join(html)
for source in docs:
    text=(PACK/source).read_text();title=text.splitlines()[0].lstrip('# ')
    body='<a href="../START-HERE.html">← Back to full pack</a>'+md_html(text,source)
    (PACK/'readable-notes'/doc_names[source]).write_text(page(title,body,True))

body='''<div class="eyebrow">BILLEAFORD HALL · GARAGE REPLACEMENT · 23 SEPTEMBER 2026</div>
<h1>Dad’s garage review pack</h1><p class="muted">The current V4 brief and model, with the earlier drawings and design options retained for reference.</p>
<div class="notice"><strong>This is a review pack.</strong> The measured site plans and final coordinated building drawings are still to be completed. The V4 model retains provisional roof and plinth dimensions, clearly labelled in its viewer and pictures.</div>
<p><a class="button" href="output/V4/viewer/garage-V4-viewer.html">Open the interactive 3D garage</a><a class="button secondary" href="readable-notes/MEASUREMENTS_FOR_DAD.html">Read what’s agreed and still needed</a></p>
<section class="card"><h2 style="margin-top:0">Use this pack with Cursor Agent</h2><p>Open this extracted folder in Cursor, start a <strong>local Agent chat</strong>, then copy and send the prompt below. The agent has instructions to find or install free Blender, open the V4 model and explain the project.</p><pre style="padding:16px;background:#e7ece5;white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 ui-monospace,monospace">__CURSOR_STARTER_PROMPT__</pre><p>Opening the folder alone does not run setup. Allow the normal tool or operating-system prompts when needed. The pack includes project instructions and an always-applied Cursor rule.</p><p><a href="readable-notes/START-WITH-CURSOR.html">Full Cursor guide and example questions</a> · <a href="readable-notes/LLM-PROJECT-CONTEXT.html">Project context for the agent</a> · <a href="readable-notes/SETUP-BLENDER.html">Blender setup instructions</a></p></section>
<div class="grid"><section class="card"><h3>1. Inspect the new model</h3><p>Drag to rotate; scroll or pinch to zoom. Hide the roof, doors or weatherboarding to see inside.</p><p>No Blender installation is needed for the browser viewer.</p></section><section class="card"><h3>2. Review the paperwork</h3><p><a href="output/V4/pdf/dad-input-workbook-V4.pdf">Printable input workbook</a></p><p><a href="readable-notes/output-V4-HEIGHT_AND_CONSTRUCTION.html">Height limits and construction drawings</a></p><p><a href="readable-notes/output-V4-MAPPING_FEASIBILITY.html">Mapping research</a></p></section><section class="card"><h3>3. Return the site information</h3><p>The marked map, garage/driveway sketches, four-side photos, measured offsets and ground levels unlock the next drawing stage.</p><p><a href="readable-notes/output-V4-POSITIONING_THE_NEW_GARAGE.html">How to locate the new garage</a></p></section></div>
<h2>Current V4 appearance and model</h2><p><span class="badge">Current design direction</span> 9 × 6 m; entrance east; left enclosed bay with full partition; two open bays; equal openings; natural timber and red clay pantiles.</p>
<div class="gallery"><figure><a href="output/V4/image/barn-pantiles-edit-V4-01.png"><img src="output/V4/image/barn-pantiles-edit-V4-01.png" alt="Accepted barn illustration with natural timber and red pantiles"></a><figcaption>Accepted appearance illustration. It does not establish dimensions.</figcaption></figure><figure><a href="output/V4/renders/V4-review-front-left.png"><img src="output/V4/renders/V4-review-front-left.png" alt="Updated V4 model, entrance and enclosed end"></a><figcaption>V4 model: entrance and enclosed end. Vertical dimensions remain provisional.</figcaption></figure><figure><a href="output/V4/renders/V4-review-entrance.png"><img src="output/V4/renders/V4-review-entrance.png" alt="V4 east-facing entrance with one closed and two open bays"></a><figcaption>Entrance view showing the bay arrangement.</figcaption></figure><figure><a href="output/V4/renders/V4-review-rear-right.png"><img src="output/V4/renders/V4-review-rear-right.png" alt="Rear and opposite end of the V4 garage"></a><figcaption>Rear and opposite end.</figcaption></figure></div>
<h2>Earlier technical drawings</h2><p><span class="badge historical">P02 · preliminary historical drawings</span> These contain earlier assumptions and have not been reissued to reflect V4. Read the current brief first. They are not a verified submission or construction set.</p><p><a class="button secondary" href="output/P02/pdf/existing-drawings-P02.pdf">Existing building drawings</a><a class="button secondary" href="output/P02/pdf/proposed-drawings-P02.pdf">Earlier proposed drawings</a><a class="button secondary" href="output/P02/renders/massing-comparison-P02.png">Earlier size comparison</a></p>
<h2>Previous design alternatives</h2><p><span class="badge historical">V3 · not selected</span> Option A has two enclosed end bays; option B explores weathered timber and a charcoal roof. The natural-timber/red-pantile V4 direction above is the selected appearance.</p><figure><a href="output/V3/comparison-front-three-quarter.png"><img loading="lazy" src="output/V3/comparison-front-three-quarter.png" alt="Historical V2 and V3 design comparison"></a><figcaption>Historic comparison board; its original “no option selected” caption predates the V4 decision.</figcaption></figure>
<h2>Editable files and project record</h2><div class="grid"><section class="card"><h3>3D model files</h3><p><a href="output/V4/model/garage-V4-review.blend" download>V4 Blender model (.blend)</a></p><p><a href="output/V4/model/garage-V4-review.glb" download>Portable V4 model (.glb)</a></p><p>The Blender model is editable in Blender 4.5 or later. The file includes its resources. The GLB provides an additional portable 3D format.</p><p><a href="output/V4/model/README.txt">Model notes and viewing instructions</a></p></section><section class="card"><h3>Current records</h3><p><a href="readable-notes/PROJECT_BRIEF.html">Project brief</a> · <a href="readable-notes/WORK_STATUS.html">Work status</a></p><p><a href="readable-notes/output-V4-DRAWING_REGISTER.html">Drawing register</a> · <a href="readable-notes/output-V4-DIY_WORKFLOW.html">Editing/export guide</a></p><p><a href="readable-notes/Original-Ref-docs-V4-dad-answers-2026-09-23.html">Dad’s recorded answers</a></p><p>Original source files, editable drawings, scripts and older models are included in their project folders.</p></section></div>
<h2>How to use and share this pack</h2><ol><li>Download the whole ZIP, then extract/unzip it into one folder.</li><li>Open <strong>START-HERE.html</strong> in a desktop browser. Keep the accompanying folders beside it.</li><li>To pass it on, send the ZIP as a file attachment or put it in your preferred file-sharing service and send its download link. A laptop or desktop is the easiest way to inspect the 3D viewer.</li></ol><footer>This folder is self-contained and works offline. Nothing has been uploaded or published. Full model and page checks are recorded in <a href="SHARE-CHECKS.json">SHARE-CHECKS.json</a>.</footer>'''
body=body.replace('__CURSOR_STARTER_PROMPT__',escape(starter_prompt))
(PACK/'START-HERE.html').write_text(page('Billeaford Hall - full garage review pack',body))
(PACK/'START-HERE.txt').write_text('BILLEAFORD HALL - FULL GARAGE REVIEW PACK\n\n1. Extract/unzip the complete folder.\n2. Open START-HERE.html in a browser on a laptop or desktop.\n3. Use the interactive 3D viewer or open the PDFs and pictures.\n\nWITH CURSOR AGENT\nOpen this extracted folder in Cursor and start a local Agent chat.\nRead START-WITH-CURSOR.md and send its starter prompt, also copied below.\nOpening a folder alone does not run setup. AGENTS.md, project context and a\n.cursor/rules/garage-review.mdc rule are included for the agent.\n\n'+starter_prompt+'\n\nBlender is needed only to edit/open the .blend model; the HTML viewer works without it.\nKeep all folders together. Current V4, older P02 drawings and V3 alternatives are clearly labelled.\nThis is a review pack, not a final planning or construction set. Roof, plinth and site information remain provisional.\n')

# The project-level viewer has the same relative navigation as the packaged copy.
# Provide its full-pack target when it is opened directly from the working tree.
(ROOT/'START-HERE.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=output/Share/Billeaford-Hall-full-review/START-HERE.html"><title>Garage review pack</title></head><body><a href="output/Share/Billeaford-Hall-full-review/START-HERE.html">Open the full garage review pack</a></body></html>')

# Check every local HTML link and that all GLB dependencies are embedded.
(PACK/'SHARE-CHECKS.json').write_text('{}\n')
broken=[]
for p in PACK.rglob('*.html'):
    if 'scripts' in p.relative_to(PACK).parts:continue
    for target in re.findall(r'(?:href|src)="([^"]+)"',p.read_text()):
        if target.startswith(('https:','http:','data:','#')):continue
        if not (p.parent/unquote(target.split('#')[0])).is_file():broken.append([str(p.relative_to(PACK)),target])
assert not broken,broken
model=PACK/'output/V4/model/garage-V4-review.blend'
verification=json.loads((PACK/'output/V4/model/verification.json').read_text())
assert verification['result']=='PASS'
assert hashlib.sha256(model.read_bytes()).hexdigest()==verification['model_sha256']
payload=json.loads(data);assert payload['source_model_sha256']==verification['model_sha256']
glb=(PACK/'output/V4/model/garage-V4-review.glb').read_bytes()
magic,version,length=struct.unpack_from('<4sII',glb,0);assert magic==b'glTF' and version==2 and length==len(glb)
size,kind=struct.unpack_from('<II',glb,12);assert kind==0x4e4f534a
gltf=json.loads(glb[20:20+size]);assert all('uri' not in item for item in gltf.get('buffers',[])+gltf.get('images',[]))
onboarding_paths=onboarding_files+['.cursor/rules/garage-review.mdc']
assert all((PACK/rel).is_file() for rel in onboarding_paths)
rule=(PACK/'.cursor/rules/garage-review.mdc').read_text()
assert rule.startswith('---\n') and re.search(r'^alwaysApply: true$',rule,re.M)
assert all(name in rule for name in ['AGENTS.md','LLM-PROJECT-CONTEXT.md','SETUP-BLENDER.md'])
for rel in ['AGENTS.md','SETUP-BLENDER.md','START-WITH-CURSOR.md']:
    instruction=(PACK/rel).read_text()
    assert 'output/V4/model/garage-V4-review.blend' in instruction and 'install' in instruction.lower()
assert starter_prompt in (PACK/'START-HERE.txt').read_text()
assert escape(starter_prompt) in (PACK/'START-HERE.html').read_text()
checks={'date':'2026-09-23','scope':'Complete family review pack: current V4 plus preserved P02/V3 material',
 'broken_local_html_links':broken,'model_verified':True,'model_sha256':verification['model_sha256'],'GLB_self_contained':True,
 'viewer_embeds_model':True,'no_external_viewer_dependencies':True,'site_or_construction_verified':False,
 'agent_onboarding':{'files':onboarding_paths,'cursor_rule_always_applied':True,'starter_prompt_consistent':True,
   'setup_instructions':'Install official Blender only if needed; open supplied V4 model and start page after user prompt.',
   'installation_tested_on_dads_computer':False,'model_unchanged_by_onboarding':True},
 'browser_review':'Localhost viewer loading, direction controls and roof cutaway visually checked. Direct file-URL automation was blocked by the browser tool policy; offline operation is supported by embedded geometry and no network dependencies. Final index links checked statically.'}
(PACK/'SHARE-CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n')
files=[p for p in PACK.rglob('*') if p.is_file()]
archive=OUT/'Billeaford-Hall-full-review.zip'
with ZipFile(archive,'w',ZIP_DEFLATED) as z:
    for p in sorted(files):z.write(p,Path(PACK.name)/p.relative_to(PACK))
with ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(files)
print(json.dumps({'zip':str(archive),'files':len(files),'size_MB':round(archive.stat().st_size/1e6,1),'start':str(PACK/'START-HERE.html'),'checks':checks},indent=2))
