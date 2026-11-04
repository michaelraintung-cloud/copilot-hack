from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).parent
src=(ROOT/'sub-cmpk-11-motivasi.md').read_text(encoding='utf-8').splitlines()
doc=Document()
sec=doc.sections[0]
sec.top_margin=Inches(.7); sec.bottom_margin=Inches(.7); sec.left_margin=Inches(.82); sec.right_margin=Inches(.82)
styles=doc.styles
styles['Normal'].font.name='Aptos'; styles['Normal'].font.size=Pt(10.2); styles['Normal'].font.color.rgb=RGBColor(38,55,70)
styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'),'Aptos')
styles['Normal'].paragraph_format.space_after=Pt(5)
for name,size,color in [('Title',28,'102A43'),('Heading 1',19,'102A43'),('Heading 2',14,'0E7490'),('Heading 3',11,'6750A4')]:
 st=styles[name]; st.font.name='Aptos Display' if name!='Heading 3' else 'Aptos'; st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=RGBColor.from_string(color)
 st._element.rPr.rFonts.set(qn('w:eastAsia'),st.font.name)
 st.paragraph_format.space_before=Pt(12); st.paragraph_format.space_after=Pt(5)
# header footer
header=sec.header.paragraphs[0]; header.text='PENGANTAR MANAJEMEN  |  SUB-CMPK 11: MOTIVASI'; header.style='Caption'; header.runs[0].font.color.rgb=RGBColor(14,116,144); header.runs[0].font.bold=True
footer=sec.footer.paragraphs[0]; footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
run=footer.add_run('Bahan ajar berbasis RPS Pengantar Manajemen • Universitas Sam Ratulangi  |  '); run.font.size=Pt(8); run.font.color.rgb=RGBColor(96,113,125)
fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); footer._p.append(fld)

def set_cell_shading(cell, fill):
 tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def set_cell_margins(cell, top=90, start=110, bottom=90, end=110):
 tc=cell._tc; tcPr=tc.get_or_add_tcPr(); tcMar=tcPr.first_child_found_in('w:tcMar')
 if tcMar is None: tcMar=OxmlElement('w:tcMar'); tcPr.append(tcMar)
 for m,v in [('top',top),('start',start),('bottom',bottom),('end',end)]:
  node=tcMar.find(qn('w:'+m))
  if node is None: node=OxmlElement('w:'+m); tcMar.append(node)
  node.set(qn('w:w'),str(v)); node.set(qn('w:type'),'dxa')
def add_rich(p,text):
 # Simple Markdown emphasis, inline code, and links as readable text.
 token=re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)')
 at=0
 for m in token.finditer(text):
  if m.start()>at: p.add_run(text[at:m.start()])
  value=m.group()
  r=p.add_run(value[2:-2] if value.startswith('**') else value[1:-1])
  if value.startswith('**'): r.bold=True
  elif value.startswith('`'): r.font.name='Consolas'; r.font.size=Pt(9)
  else: r.italic=True
  at=m.end()
 if at<len(text): p.add_run(text[at:])
def add_para(text,style=None):
 p=doc.add_paragraph(style=style) if style else doc.add_paragraph()
 add_rich(p,text)
 return p

i=0; title_seen=False
while i<len(src):
 line=src[i].rstrip()
 if not line.strip() or line.strip()=='---': i+=1; continue
 if line.startswith('|'):
  rows=[]
  while i<len(src) and src[i].lstrip().startswith('|'):
   cells=[x.strip() for x in src[i].strip().strip('|').split('|')]
   if not all(re.fullmatch(r':?-{3,}:?',c or '-') for c in cells): rows.append(cells)
   i+=1
  if rows:
   n=max(map(len,rows)); table=doc.add_table(rows=0,cols=n); table.alignment=WD_TABLE_ALIGNMENT.CENTER; table.style='Light Shading Accent 1'
   for ri,row in enumerate(rows):
    cells=table.add_row().cells
    for ci in range(n):
     cell=cells[ci]; cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER; set_cell_margins(cell)
     txt=row[ci] if ci<len(row) else ''
     p=cell.paragraphs[0]; p.paragraph_format.space_after=Pt(0); add_rich(p,txt)
     for r in p.runs: r.font.size=Pt(8.5)
     if ri==0:
      set_cell_shading(cell,'0E7490')
      for r in p.runs: r.font.bold=True; r.font.color.rgb=RGBColor(255,255,255)
   doc.add_paragraph().paragraph_format.space_after=Pt(1)
  continue
 if line.startswith('# '):
  text=line[2:].strip()
  if not title_seen:
   p=doc.add_paragraph(style='Title'); add_rich(p,text); p.paragraph_format.space_before=Pt(10); title_seen=True
  else: add_para(text,'Heading 1')
  i+=1; continue
 if line.startswith('## '): add_para(line[3:].strip(),'Heading 1'); i+=1; continue
 if line.startswith('### '): add_para(line[4:].strip(),'Heading 2'); i+=1; continue
 if line.startswith('> '):
  p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.18); p.paragraph_format.right_indent=Inches(.18)
  p.paragraph_format.space_before=Pt(4); p.paragraph_format.space_after=Pt(7)
  pPr=p._p.get_or_add_pPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),'E5F3F2'); pPr.append(shd)
  add_rich(p,line[2:]); i+=1; continue
 if re.match(r'^\s*[-*] ',line):
  p=doc.add_paragraph(style='List Bullet'); add_rich(p,re.sub(r'^\s*[-*] ','',line)); p.paragraph_format.space_after=Pt(2); i+=1; continue
 if re.match(r'^\s*\d+\. ',line):
  # Preserve authored numbering exactly instead of relying on Word list restart behavior.
  p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.25); p.paragraph_format.first_line_indent=Inches(-.22)
  match=re.match(r'^\s*(\d+)\. (.*)',line); rr=p.add_run(match.group(1)+'. '); rr.bold=True; add_rich(p,match.group(2)); i+=1; continue
 # Normal paragraph; collect wrapped markdown source lines into one paragraph.
 parts=[line.strip()]; i+=1
 while i<len(src) and src[i].strip() and not src[i].startswith(('#','>','|')) and not re.match(r'^\s*[-*] ',src[i]) and not re.match(r'^\s*\d+\. ',src[i]) and src[i].strip()!='---':
  parts.append(src[i].strip()); i+=1
 p=doc.add_paragraph(); add_rich(p,' '.join(parts))

out=ROOT/'materi-lengkap-sub-cmpk-11-motivasi.docx'
doc.save(out)
print(out)
