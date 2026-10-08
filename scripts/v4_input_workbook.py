"""Build the static A4 V4 information-gathering workbook; no survey geometry is created."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/V4/pdf/dad-input-workbook-V4.pdf'
INK = HexColor('#233c3b')
MUTED = HexColor('#5c6e70')
LINE = HexColor('#c4d1cf')
PALE = HexColor('#edf3f0')
font_pairs = [
    (Path('/System/Library/Fonts/Supplemental/Arial.ttf'), Path('/System/Library/Fonts/Supplemental/Arial Bold.ttf')),
    (Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'), Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')),
]
regular, bold = next((a,b) for a,b in font_pairs if a.exists() and b.exists())
pdfmetrics.registerFont(TTFont('Workbook', str(regular)))
pdfmetrics.registerFont(TTFont('WorkbookBold', str(bold)))
style = ParagraphStyle('body', fontName='Workbook', fontSize=10, leading=14,
                       textColor=INK, spaceAfter=0)


def text(c, x, y, value, size=10, bold=False, color=INK):
    c.setFillColor(color)
    c.setFont('WorkbookBold' if bold else 'Workbook', size)
    c.drawString(x * mm, (297-y) * mm, value)


def para(c, value, x, y, width=178, size=10):
    s = ParagraphStyle('p', parent=style, fontSize=size, leading=size*1.4)
    p = Paragraph(escape(value), s)
    _, h = p.wrap(width*mm, 240*mm)
    p.drawOn(c, x*mm, (297-y)*mm-h)
    return y+h/mm


def rule(c, y, x=16, width=178):
    c.setStrokeColor(LINE)
    c.setLineWidth(.5)
    c.line(x*mm, (297-y)*mm, (x+width)*mm, (297-y)*mm)


def field(c, label, y, lines=1):
    bottom = para(c, label, 16, y, size=10)
    for n in range(lines):
        rule(c, bottom+8+n*8)
    return bottom+12+lines*8


def header(c, number, title, subtitle):
    c.setFillColor(INK)
    c.rect(0, 285*mm, 210*mm, 12*mm, fill=1, stroke=0)
    text(c, 16, 8, 'BILLEAFORD HALL  /  GARAGE REPLACEMENT  /  V4', 8, True, white)
    text(c, 16, 24, title, 20, True)
    para(c, subtitle, 16, 29, size=9)
    rule(c, 281)
    text(c, 16, 288, '23 September 2026  |  S17 answers recorded  |  Not a planning drawing', 8, color=MUTED)
    text(c, 183, 288, f'{number} / 6', 8, color=MUTED)


def table(c, headers, rows, x, y, widths, row_height=13):
    total=sum(widths)
    c.setFillColor(PALE)
    c.rect(x*mm,(297-y-row_height)*mm,total*mm,row_height*mm,fill=1,stroke=0)
    for ri,row in enumerate([headers]+rows):
        xx=x
        for col,w in zip(row,widths):
            para(c, col, xx+2, y+ri*row_height+2, w-4, size=8.5)
            xx+=w
        rule(c,y+(ri+1)*row_height,x,total)
    c.setStrokeColor(LINE)
    xx=x
    for w in [0]+widths:
        xx+=w
        c.line(xx*mm,(297-y)*mm,xx*mm,(297-y-(len(rows)+1)*row_height)*mm)


def map_page(c, number, title, instructions):
    header(c,number,title,'REFERENCE SCREENSHOT - NOT TO SCALE. Use to mark identities and intent only.')
    para(c,instructions,16,43,size=9)
    c.drawImage(str(ROOT/'Original Ref docs/overhead.jpeg'),30*mm,30*mm,
                width=150.3*mm,height=204*mm,preserveAspectRatio=True,anchor='c')
    para(c,'User-supplied reference screenshot. Original mapping, date, north and reuse rights still to verify. '
           'Do not measure from this page or submit it as an application plan.',16,269,size=8)


def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(OUT),pagesize=(210*mm,297*mm))
    c.setTitle('Billeaford Hall - Dad input workbook V4')
    c.setAuthor('Garage redesign project')
    header(c,1,'Answers and next inputs','Your answers are recorded. Remaining blanks are for evidence or unresolved details.')
    c.setFillColor(PALE); c.roundRect(16*mm,198*mm,178*mm,54*mm,3*mm,fill=1,stroke=0)
    para(c,'Confirmed: Billeaford Hall, Sloe Lane, Knodishall, IP17 1UU. Private household garage. '
           '9 x 6 m, entrance east, three equal bays, left bay enclosed with a full dividing wall, two open bays. '
           'Red clay pantiles; natural timber/doors; end framing concealed. Illustration accepted. '
           'Three brick courses preferred, adjustable if needed for a low building. General-builder route; '
           'no specific vehicle checks. Exact roof height remains to be resolved.',22,51,166,size=9.5)
    text(c,16,112,'PROMISED FILES - STILL TO BE RECEIVED',11,True)
    items=[
        'New licensed map: original file, scale, north/grid, date and licence details. Only the old screenshot is available.',
        'Building identities and boundary/access annotations (page 2); garage and driveway sketches (page 3).',
        'Photographs of all four sides of the existing garage; uncropped drawings if available.',
        'Measured ties, boundary distances and levels (pages 4-6). Give units, endpoints, date and evidence.'
    ]
    y=120
    for i,t in enumerate(items,1):
        text(c,16,y+4,str(i),11,True)
        y=para(c,t,25,y,169)+8
    y=field(c,'New map filename/location, date and licence information (when available):',213,2)
    para(c,'Pages 2-3 are rough mark-up sheets. Photos/scans of your answers are fine for communication; '
           'they will not become scaled submission plans. Keep original source files separately.',16,258,size=9)
    c.showPage()

    map_page(c,2,'Existing site and ownership',
             'Label the buildings B1-B7 (key on page 4), mark the garage and entrance, and identify land '
             'owned/controlled, shared access and the highway connection. Note uncertainty explicitly.')
    c.showPage()
    map_page(c,3,'Proposed garage and driveway',
             'Sketch the agreed 9 x 6 m footprint, entrance facing east. Draw new/retained/removed drive edges; '
             'mark the right-side limit, left fence and trees. Give ties on page 4; verify map north.')
    c.showPage()

    header(c,4,'Building key and site ties','Place these IDs on the reference pages. IDs do not assign positions in advance.')
    table(c,['ID / requested name','Confirm identity, use and any different name'],[
        ['B1 - Billeaford Hall',''],['B2 - Former dairy',''],['B3 - Timber garage',''],
        ['B4 - East Barn',''],['B5 - West Barn',''],['B6 - Other barn/store',''],['B7 - Other barn/store','']
    ],16,45,[68,110],13)
    text(c,16,161,'MEASURED SITE DISTANCES',11,True)
    para(c,'Use metres. Name both endpoints. Include garage-to-building ties, nearest curtilage-boundary '
           'distances (including roof projections), available width/depth and a cross-check.',16,166,size=9)
    table(c,['ID / endpoints','Value + unit','Method / date / evidence'],[['','',''] for _ in range(4)],
          16,184,[67,35,76],13)
    field(c,'Verified map north and ground-level datum (entrance faces east):',253,1)
    c.showPage()

    header(c,5,'Verify the buildings','Existing values below are reference values, not surveyed dimensions. Use millimetres.')
    table(c,['Existing garage','Reference','Measured value / evidence'],[
        ['Wall footprint','6800 x 3500',''],['Roof length / overhangs','7200 / TBC',''],
        ['Eaves / ridge','2200 / 3800',''],['Door clear width / height','TBC / 2000',''],
        ['Approach depth / width','1200 / TBC',''],['Roof covering','Conflicting','']
    ],16,45,[72,40,66],13)
    para(c,'Proposed agreed: 9000 x 6000, equal bays, full partition, entrance east. '
           'Clear widths depend on the detailed wall/post arrangement.',16,144,size=9)
    y=160
    y=field(c,'Roof/levels to resolve: eligible dual-pitch PD limit 4 m overall / 2.5 m eaves; '
                'within 2 m of curtilage boundary, 2.5 m overall. No final ridge selected.',y)
    y=field(c,'Plinth: prefer three courses; actual height and ground/floor relationship still needed. '
                'May reconsider for low-height intent.',y)
    y=field(c,'Designer/builder: clay tile product/pitch, frame/roof details, overhangs, clear openings '
                'and door operation. Do not guess structural sizes.',y)
    para(c,'Four-side photographs promised. Exact siting/levels and PD eligibility remain unverified; '
           'planning drawings require further technical design before construction.',16,261,size=8.5)
    text(c,16,277,'Height source: GOV.UK householders technical guidance, Class E (checked 23 Sep 2026).',7.5)
    c.linkURL('https://www.gov.uk/government/publications/permitted-development-rights-for-householders-technical-guidance/permitted-development-rights-for-householders-technical-guidance',
              (16*mm,18*mm,194*mm,23*mm),relative=0)
    c.showPage()

    header(c,6,'Driveway, levels and review','Reported fall: about 300-400 mm towards the courtyard centre. Exact extent/levels awaited.')
    y=45
    for label in [
        'Driveway width, corner/turning dimensions and surface material/colour:',
        'Permeable surface? Edge treatment, falls, drainage features and destination:',
        'Highway entrance changed, or internal drive only? Access rights, gates and constraints:',
        'Trees/hedges: positions, species, trunk/canopy sizes; excavation nearby; retained/removed:',
        'Fall endpoints; corner/perimeter levels with one datum; proposed floor; services/boundaries:',
        'Existing planning decisions/conditions and known heritage/tree/other designations:'
    ]:
        y=field(c,label,y)
    text(c,16,238,'REVIEW RECORD',11,True)
    para(c,'Reviewed by: _____________________  Date: _______________\n'
           'Still unknown / further files to follow: __________________________________',16,243,size=9)
    para(c,'Next: check the original map and evidence; agree building identities and boundaries; '
           'build the measured base; then review proposed siting/driveway before issuing the drawing set.',16,266,size=8.5)
    c.showPage();c.save()
    print(OUT)


if __name__=='__main__':
    main()
