"""Check paper dimensions, scale geometry, text bounds, drawing identities and outputs."""
import json,math,xml.etree.ElementTree as ET
import pdfplumber
from common import OUT,REV,ROOT,DATA,values,pitch
checks=[]
for name,pre in [('existing','EX'),('proposed','PR')]:
 path=OUT/'pdf'/f'{name}-drawings-P02.pdf'
 with pdfplumber.open(path) as pdf:
  assert len(pdf.pages)==6
  for page in pdf.pages:
   assert abs(page.width-420*72/25.4)<.01 and abs(page.height-297*72/25.4)<.01
   text=page.extract_text();assert DATA['status'] in text
   assert '1:50' in text and 'P02' in text
   for c in page.chars:assert 8*72/25.4<=c['x0']<c['x1']<412*72/25.4 and c['top']>8*72/25.4 and c['bottom']<289*72/25.4,(path,c)
  # Verify actual PDF vector floor boundary, not dimension label alone.
  p=values(name);wanted=(p['width']/50*72/25.4,p['depth']/50*72/25.4)
  candidates=pdf.pages[0].curves+pdf.pages[0].rects
  assert any(abs(o['width']-wanted[0])<.02 and abs(o['height']-wanted[1])<.02 for o in candidates),'1:50 footprint missing'
  # Scale bar: four 10 mm wide, 2 mm high alternating rectangles.
  assert sum(abs(o['width']-10*72/25.4)<.02 and abs(o['height']-2*72/25.4)<.02 for o in candidates)>=4
 checks.append(f'{name}: 6 A3 pages; all text within margins; 1:50 footprint and scale bar verified')
for svg in (OUT/'svg').glob('*.svg'):
 root=ET.parse(svg).getroot();assert root.attrib['width']=='420mm' and root.attrib['height']=='297mm'
assert len(list((OUT/'svg').glob('*.svg')))==12
p=values('proposed');calculated=p['eaves']+p['depth']/2*math.tan(math.radians(pitch('proposed')));assert abs(calculated-p['ridge'])<1e-8
checks+=['12 editable SVG sheets with A3 physical dimensions','Roof geometry reconciles to chosen ridge/eaves datums']
result={'result':'PASS','checks':checks,'caveat':'Validates internal consistency and output format, not site survey accuracy or planning compliance.'}
(OUT/'validation-report.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
