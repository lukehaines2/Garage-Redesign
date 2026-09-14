import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/parameters.json').read_text())
REV=DATA['revision']
OUT=ROOT/'output'/REV
for folder in ['pdf','svg','model','renders']:(OUT/folder).mkdir(parents=True,exist_ok=True)
def values(name): return {k:v['value'] for k,v in DATA[name].items()}
def pitch(name):
 p=values(name); span=p['depth'] if name=='proposed' else p['width']
 return math.degrees(math.atan2(p['ridge']-p['eaves'],span/2))
def post_positions():
 p=values('proposed'); return [p['post']/2,p['bay'],2*p['bay'],p['width']-p['post']/2]
def clear_openings():
 p=values('proposed'); xs=post_positions(); return [xs[i+1]-xs[i]-p['post'] for i in range(3)]
