#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Membuat dokumen Word (A4) berisi soal-soal dari foto slide/papan tulis
beserta pembahasannya.

Keluaran: materi-fisika/Pembahasan-Soal-Energi-Usaha-Momentum.docx
"""
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BASE = Path(__file__).resolve().parent
IMG = BASE / "gambar"
OUT = BASE / "Pembahasan-Soal-Energi-Usaha-Momentum.docx"

MERAH = RGBColor(0x8B, 0x1A, 0x1A)
MERAH2 = RGBColor(0xA5, 0x2A, 0x2A)
HITAM = RGBColor(0x1C, 0x1C, 0x1C)
ABU = RGBColor(0x55, 0x55, 0x55)
ABU_MUDA = RGBColor(0x77, 0x77, 0x77)
BIRU = RGBColor(0x1F, 0x4E, 0x79)

BODY = "Cambria"
HEAD = "Calibri"

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

AFTER_PBDR = ("w:shd", "w:tabs", "w:suppressAutoHyphens", "w:kinsoku", "w:wordWrap",
              "w:overflowPunct", "w:topLinePunct", "w:autoSpaceDE", "w:autoSpaceDN",
              "w:bidi", "w:adjustRightInd", "w:snapToGrid", "w:spacing", "w:ind",
              "w:contextualSpacing", "w:mirrorIndents", "w:suppressOverlap", "w:jc",
              "w:textDirection", "w:textAlignment", "w:textboxTightWrap",
              "w:outlineLvl", "w:divId", "w:cnfStyle", "w:rPr", "w:sectPr",
              "w:pPrChange")
AFTER_SHD = AFTER_PBDR[1:]
AFTER_RPR = ("w:ins", "w:del", "w:moveFrom", "w:moveTo", "w:rPrChange")


def par_shading(par, fill):
    pPr = par._p.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    pPr.insert_element_before(shd, *AFTER_SHD)


def par_border(par, **edges):
    pPr = par._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    for name in ("top", "left", "bottom", "right"):
        if name in edges:
            sz, color, space = edges[name]
            el = OxmlElement("w:" + name)
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), str(sz))
            el.set(qn("w:space"), str(space))
            el.set(qn("w:color"), color)
            pBdr.append(el)
    pPr.insert_element_before(pBdr, *AFTER_PBDR)


def cell_shading(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def table_borders(table, color="C9C0AF", sz=6):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement("w:" + edge)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(sz))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblPr.insert_element_before(
        borders, "w:shd", "w:tblLayout", "w:tblCellMar", "w:tblLook",
        "w:tblCaption", "w:tblDescription", "w:tblPrChange")



def set_table_pct(table, pct=5000):
    """Pasang lebar tabel relatif (persen) tanpa menduplikasi elemen tblW."""
    tblPr = table._tbl.tblPr
    for el in tblPr.findall(qn("w:tblW")):
        tblPr.remove(el)
    tw = OxmlElement("w:tblW")
    tw.set(qn("w:w"), str(pct))
    tw.set(qn("w:type"), "pct")
    tblPr.insert_element_before(
        tw, "w:jc", "w:tblCellSpacing", "w:tblInd", "w:tblBorders", "w:shd",
        "w:tblLayout", "w:tblCellMar", "w:tblLook", "w:tblCaption",
        "w:tblDescription", "w:tblPrChange")


def field(par, instr, placeholder="", size=9, color=ABU_MUDA):
    r = par.add_run()
    f = OxmlElement("w:fldChar")
    f.set(qn("w:fldCharType"), "begin")
    r._r.append(f)
    r = par.add_run()
    t = OxmlElement("w:instrText")
    t.set(qn("xml:space"), "preserve")
    t.text = f" {instr} "
    r._r.append(t)
    r = par.add_run()
    f = OxmlElement("w:fldChar")
    f.set(qn("w:fldCharType"), "separate")
    r._r.append(f)
    ph = par.add_run(placeholder)
    ph.font.size = Pt(size)
    ph.font.color.rgb = color
    r = par.add_run()
    f = OxmlElement("w:fldChar")
    f.set(qn("w:fldCharType"), "end")
    r._r.append(f)


# --------------------------------------------------------------------- teks
TOKEN = re.compile(r"(\*\*.+?\*\*|\*(?!\*).+?\*)")
SUB = re.compile(r"(~[^~]+~)")


def _emit(par, text, bold, italic, size, color):
    for piece in SUB.split(text):
        if not piece:
            continue
        sub = False
        if piece.startswith("~") and piece.endswith("~") and len(piece) > 2:
            piece, sub = piece[1:-1], True
        run = par.add_run(piece)
        run.bold = bold or None
        run.italic = italic or None
        if sub:
            run.font.subscript = True
        if size:
            run.font.size = Pt(size)
        if color:
            run.font.color.rgb = color


def rich(par, text, size=None, color=None, italic=False, bold=False):
    for part in TOKEN.split(text):
        if not part:
            continue
        b, i = bold, italic
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            part, b = part[2:-2], True
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            part, i = part[1:-1], True
        _emit(par, part, b, i, size, color)
    return par


# ------------------------------------------------------------------ dokumen
def new_document():
    doc = Document()
    cp = doc.core_properties
    cp.title = "Pembahasan Soal — Energi, Usaha, dan Kekekalan Energi"
    cp.subject = "Fisika Dasar I (BEK1EAB4)"
    cp.author = "Dosen Pengasuh Mata Kuliah Fisika Dasar I"
    cp.category = "Bahan Ajar"

    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.top_margin = Cm(2.2)
    sec.bottom_margin = Cm(2.0)
    sec.left_margin = Cm(2.4)
    sec.right_margin = Cm(2.1)
    sec.header_distance = Cm(1.1)
    sec.footer_distance = Cm(1.0)
    sec.different_first_page_header_footer = True

    st = doc.styles["Normal"]
    st.font.name = BODY
    st.font.size = Pt(10.5)
    st.font.color.rgb = HITAM
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), BODY)
    lang = OxmlElement("w:lang")
    lang.set(qn("w:val"), "id-ID")
    rpr.insert_element_before(lang, *AFTER_RPR)

    pf = st.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(4)
    pf.line_spacing = 1.12
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return doc


def p(doc, text, size=None, space_after=4, indent=0.0, align=None,
      italic=False, bold=False, color=None):
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(space_after)
    par.paragraph_format.left_indent = Cm(indent)
    if align == "center":
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "left":
        par.alignment = WD_ALIGN_PARAGRAPH.LEFT
    rich(par, text, size=size, italic=italic, bold=bold, color=color)
    return par


def rumus(doc, text, note=None):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.left_indent = Cm(0.55)
    pf.right_indent = Cm(0.35)
    pf.space_before = Pt(4)
    pf.space_after = Pt(4 if note else 8)
    pf.line_spacing = 1.05
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par_shading(par, "FBF8F1")
    par_border(par, left=(12, "B8860B", 8))
    rich(par, text, size=10.5)
    if note:
        np_ = doc.add_paragraph()
        np_.paragraph_format.left_indent = Cm(0.55)
        np_.paragraph_format.space_before = Pt(0)
        np_.paragraph_format.space_after = Pt(8)
        np_.paragraph_format.line_spacing = 1.05
        rich(np_, note, size=8.8, italic=True, color=ABU)
    return par


def langkah(doc, items, start=1):
    for i, t in enumerate(items, start):
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(0.85)
        pf.first_line_indent = Cm(-0.5)
        pf.space_after = Pt(3)
        pf.line_spacing = 1.1
        r = par.add_run(f"{i}.")
        r.bold = True
        r.font.color.rgb = MERAH2
        par.add_run("\t")
        rich(par, t, size=10.3)


def poin(doc, items, indent=0.75, simbol="•"):
    for t in items:
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(indent + 0.45)
        pf.first_line_indent = Cm(-0.45)
        pf.space_after = Pt(2.5)
        pf.line_spacing = 1.1
        r = par.add_run(simbol + "\t")
        r.font.color.rgb = MERAH2
        r.bold = True
        rich(par, t, size=10.3)


def judul_bagian(doc, text, page_break=True):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.page_break_before = page_break
    pf.space_before = Pt(0)
    pf.space_after = Pt(10)
    pf.keep_with_next = True
    par_border(par, bottom=(14, "8B1A1A", 6))
    r = par.add_run(text)
    r.font.name = HEAD
    r.font.size = Pt(15)
    r.bold = True
    r.font.color.rgb = MERAH
    return par


def judul_soal(doc, nomor, judul, sumber):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_before = Pt(16)
    pf.space_after = Pt(2)
    pf.keep_with_next = True
    par_shading(par, "F1E7DA")
    par_border(par, left=(20, "8B1A1A", 7))
    r = par.add_run(f"SOAL {nomor}   ")
    r.font.name = HEAD
    r.font.size = Pt(9)
    r.bold = True
    r.font.color.rgb = MERAH2
    r = par.add_run(judul)
    r.font.name = HEAD
    r.font.size = Pt(11.5)
    r.bold = True
    r.font.color.rgb = MERAH

    src = doc.add_paragraph()
    src.paragraph_format.space_before = Pt(0)
    src.paragraph_format.space_after = Pt(6)
    src.paragraph_format.left_indent = Cm(0.1)
    src.paragraph_format.keep_with_next = True
    r = src.add_run(sumber)
    r.font.size = Pt(8.5)
    r.italic = True
    r.font.color.rgb = ABU_MUDA
    return par


def label(par, text, color=None, size=9.5):
    r = par.add_run(text)
    r.bold = True
    r.font.size = Pt(size)
    r.font.color.rgb = color or MERAH2


def soal_teks(doc, text):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.left_indent = Cm(0.35)
    pf.right_indent = Cm(0.2)
    pf.space_before = Pt(2)
    pf.space_after = Pt(9)
    pf.line_spacing = 1.13
    par_shading(par, "F7F9FB")
    par_border(par, left=(12, "1F4E79", 8))
    label(par, "Soal.  ", color=BIRU, size=10)
    rich(par, text, size=10.3)
    return par


def penyelesaian(doc):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(2)
    par.paragraph_format.space_after = Pt(4)
    par.paragraph_format.keep_with_next = True
    r = par.add_run("Penyelesaian")
    r.bold = True
    r.font.size = Pt(10.5)
    r.font.color.rgb = HITAM


def jawaban(doc, text):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.left_indent = Cm(0.25)
    pf.right_indent = Cm(0.2)
    pf.space_before = Pt(8)
    pf.space_after = Pt(10)
    pf.line_spacing = 1.1
    par_shading(par, "EEF3E8")
    par_border(par, left=(18, "4F6B3A", 8), top=(4, "C7D3BC", 4),
               bottom=(4, "C7D3BC", 4), right=(4, "C7D3BC", 4))
    r = par.add_run("Jawaban:")
    r.bold = True
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x3B, 0x53, 0x2B)
    par.add_run(" ")
    rich(par, text, size=10.3, bold=True)
    return par


def gambar(doc, path, lebar_cm, caption):
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_before = Pt(6)
    par.paragraph_format.space_after = Pt(2)
    par.paragraph_format.keep_with_next = True
    par.add_run().add_picture(str(path), width=Cm(lebar_cm))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(0)
    cap.paragraph_format.space_after = Pt(9)
    rich(cap, caption, size=8.5, italic=True, color=ABU_MUDA)


def catatan(doc, text):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.left_indent = Cm(0.25)
    pf.space_before = Pt(4)
    pf.space_after = Pt(8)
    pf.line_spacing = 1.1
    par_shading(par, "FAFAF4")
    par_border(par, left=(10, "B8860B", 8))
    label(par, "Catatan.  ", color=RGBColor(0x8A, 0x6D, 0x1F), size=9)
    rich(par, text, size=9.3, italic=True)
    return par


# ------------------------------------------------------------------- isi
def cover(doc):
    for _ in range(2):
        q = doc.add_paragraph()
        q.paragraph_format.space_after = Pt(0)

    banner = doc.add_table(rows=1, cols=1)
    banner.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_pct(banner)
    c = banner.rows[0].cells[0]
    cell_shading(c, "8B1A1A")
    c.text = ""

    p1 = c.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(20)
    p1.paragraph_format.space_after = Pt(2)
    r = p1.add_run("PEMBAHASAN SOAL")
    r.font.name = HEAD
    r.font.size = Pt(15)
    r.bold = True
    r.font.color.rgb = RGBColor(0xF6, 0xE7, 0xD0)

    p2 = c.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(4)
    r = p2.add_run("USAHA, ENERGI, DAN\nKEKEKALAN ENERGI MEKANIK")
    r.font.name = HEAD
    r.font.size = Pt(20)
    r.bold = True
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    p3 = c.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.paragraph_format.space_before = Pt(0)
    p3.paragraph_format.space_after = Pt(22)
    r = p3.add_run("Fisika Dasar I  ·  BEK1EAB4")
    r.font.name = BODY
    r.font.size = Pt(12)
    r.italic = True
    r.font.color.rgb = RGBColor(0xF3, 0xDF, 0xC4)

    gap = doc.add_paragraph()
    gap.paragraph_format.space_before = Pt(8)
    gap.paragraph_format.space_after = Pt(16)
    par_border(gap, bottom=(10, "B8860B", 1))

    info = [
        ("Sumber soal", "Delapan soal dari tayangan slide dan papan tulis "
                        "pertemuan minggu ke-4 s.d. ke-6"),
        ("Cakupan", "Energi potensial, kekekalan energi mekanik, usaha oleh "
                    "gaya berubah, dan usaha oleh gaya pegas"),
        ("Bentuk dokumen", "Soal ditulis kembali, lalu dibahas langkah demi langkah"),
        ("Jumlah soal", "8 soal (4 soal energi, 4 soal usaha)"),
    ]
    tbl = doc.add_table(rows=0, cols=2)
    tbl.autofit = False
    for k, v in info:
        row = tbl.add_row()
        c1, c2 = row.cells
        c1.width = Cm(4.0)
        c2.width = Cm(11.8)
        c1.text = ""
        c2.text = ""
        pp = c1.paragraphs[0]
        pp.paragraph_format.space_after = Pt(7)
        r = pp.add_run(k)
        r.font.name = HEAD
        r.font.size = Pt(10)
        r.bold = True
        r.font.color.rgb = MERAH
        pp = c2.paragraphs[0]
        pp.paragraph_format.space_after = Pt(7)
        r = pp.add_run(": " + v)
        r.font.name = BODY
        r.font.size = Pt(10)

    for _ in range(3):
        q = doc.add_paragraph()
        q.paragraph_format.space_after = Pt(0)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("Dosen Pengasuh Mata Kuliah")
    r.font.name = HEAD
    r.font.size = Pt(10)
    r.font.color.rgb = ABU

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(2)
    p.add_run("………………………………………")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("Oktober 2026")
    r.font.name = HEAD
    r.font.size = Pt(11)
    r.bold = True
    r.font.color.rgb = MERAH


def header_footer(doc):
    sec = doc.sections[0]
    hp = sec.header.paragraphs[0]
    hp.paragraph_format.space_after = Pt(2)
    hp.paragraph_format.tab_stops.add_tab_stop(Cm(16.5), WD_TAB_ALIGNMENT.RIGHT)
    r = hp.add_run("Pembahasan Soal — Usaha, Energi, dan Kekekalan Energi")
    r.font.name = HEAD
    r.font.size = Pt(8.5)
    r.font.color.rgb = ABU_MUDA
    r = hp.add_run("\tFisika Dasar I · BEK1EAB4")
    r.font.name = HEAD
    r.font.size = Pt(8.5)
    r.font.color.rgb = ABU_MUDA
    par_border(hp, bottom=(4, "C9C0AF", 2))

    fp = sec.footer.paragraphs[0]
    fp.paragraph_format.space_before = Pt(2)
    fp.paragraph_format.tab_stops.add_tab_stop(Cm(16.5), WD_TAB_ALIGNMENT.RIGHT)
    r = fp.add_run("Soal dari slide kuliah minggu ke-4 s.d. ke-6")
    r.font.name = HEAD
    r.font.size = Pt(8.5)
    r.font.color.rgb = ABU_MUDA
    r = fp.add_run("\tHalaman ")
    r.font.name = HEAD
    r.font.size = Pt(8.5)
    r.font.color.rgb = ABU_MUDA
    field(fp, "PAGE", "1", 8.5)
    r = fp.add_run(" dari ")
    r.font.name = HEAD
    r.font.size = Pt(8.5)
    r.font.color.rgb = ABU_MUDA
    field(fp, "NUMPAGES", "1", 8.5)
    par_border(fp, top=(4, "C9C0AF", 2))


def daftar_isi(doc):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.page_break_before = True
    pf.space_after = Pt(10)
    par_border(par, bottom=(14, "8B1A1A", 6))
    r = par.add_run("DAFTAR SOAL")
    r.font.name = HEAD
    r.font.size = Pt(15)
    r.bold = True
    r.font.color.rgb = MERAH

    items = [
        ("1", "Dua macam energi potensial: bola jatuh menekan pegas",
         "Example 6-11", "k ≈ 1,6 × 10³ N/m"),
        ("2", "Dua seluncuran air: siapa lebih cepat, siapa lebih dulu sampai",
         "Conceptual Example 6-9", "laju sama; Corinne lebih dulu"),
        ("3", "Anak meluncur di seluncuran air (h = 8,5 m)",
         "Gambar 8-8", "v ≈ 12,9 m/s"),
        ("4", "Laju kereta roller-coaster dengan kekekalan energi",
         "Example 6-8", "28 m/s dan 30 m"),
        ("5", "Grafik percepatan terhadap posisi (3 bagian)",
         "Problem 37, Fig. 7-40", "42 J; 30 J; 12 J; v = 6,5; 5,5; 3,5 m/s"),
        ("6", "Keju di lantai kabin elevator",
         "Problem 25, Fig. 7-34", "2,6 × 10⁴ J; F~N~ ≈ 2,45 N"),
        ("7", "Usaha oleh gaya bergantung posisi (integrasi dua dimensi)",
         "Sample Problem 7-08", "W = 7 J; laju bertambah"),
        ("8", "Usaha dari grafik gaya terhadap posisi",
         "Problem 13, Fig. 6-38", "2,8 × 10³ J; 2,1 × 10³ J"),
    ]
    for no, judul, sumber, hasil in items:
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(0.95)
        pf.first_line_indent = Cm(-0.95)
        pf.space_after = Pt(6)
        pf.line_spacing = 1.1
        r = par.add_run(f"{no}.")
        r.bold = True
        r.font.color.rgb = MERAH
        r.font.size = Pt(10.5)
        par.add_run("\t")
        r = par.add_run(judul)
        r.font.size = Pt(10.5)
        r = par.add_run(f"   ({sumber})")
        r.font.size = Pt(8.8)
        r.italic = True
        r.font.color.rgb = ABU_MUDA
        br = par.add_run("\n\tJawaban: ")
        br.font.size = Pt(9)
        br.font.color.rgb = RGBColor(0x3B, 0x53, 0x2B)
        rich(par, hasil, size=9, color=RGBColor(0x3B, 0x53, 0x2B), bold=True)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    r = p.add_run("Catatan: seluruh soal ditulis kembali dalam bahasa Indonesia "
                  "sesuai teks pada slide; istilah dan notasi asli dipertahankan "
                  "dalam tanda kurung bila diperlukan.")
    r.font.size = Pt(8.8)
    r.italic = True
    r.font.color.rgb = ABU_MUDA


def isi(doc):
    # ================================================== Bagian A
    judul_bagian(doc, "BAGIAN A — ENERGI POTENSIAL DAN KEKEKALAN ENERGI MEKANIK")

    p(doc, "Kelima soal pada bagian ini bertumpu pada satu gagasan yang sama: "
           "**bila hanya gaya konservatif (gravitasi dan gaya pegas) yang "
           "melakukan usaha, energi mekanik total sistem tidak berubah.** "
           "Artinya, kita cukup membandingkan keadaan awal dan keadaan akhir, "
           "tanpa perlu menelusuri gaya pada setiap titik lintasan.",
      space_after=6)
    rumus(doc, "K₁ + U₁ = K₂ + U₂      dengan      K = ½mv²,   "
               "U~gravitasi~ = mgy,   U~pegas~ = ½kx²")
    p(doc, "Yang perlu dijaga hanya dua hal: (i) **titik acuan** y = 0 harus "
           "dipilih sekali dan dipakai konsisten, dan (ii) **semua bentuk "
           "energi potensial yang terlibat harus ikut ditulis** — inilah inti "
           "Soal 1.", space_after=8)

    # ---------------------------------------------------------- SOAL 1
    judul_soal(doc, 1, "Dua macam energi potensial: bola jatuh menekan pegas",
               "Slide EXAMPLE 6-11 · Gambar 6-23 · Energi Potensial dan "
               "Kekekalan Energi Mekanik")
    soal_teks(doc, "Sebuah bola bermassa m = 2,60 kg, mulai dari keadaan diam, "
                   "jatuh sejauh vertikal h = 55,0 cm sebelum menumbuk pegas "
                   "spiral vertikal, yang kemudian dimampatkannya sebesar "
                   "Y = 15,0 cm (Gbr. 6-23). Tentukan konstanta kekakuan pegas "
                   "k tersebut. Anggap pegas tidak bermassa dan abaikan "
                   "hambatan udara. Ukur semua jarak dari titik tempat bola "
                   "pertama kali menyentuh pegas yang belum termampatkan "
                   "(y = 0 di titik ini).")
    gambar(doc, IMG / "gbr-bola-pegas.png", 12.4,
           "Gambar 1. Tiga keadaan bola: (a) dilepas dari ketinggian h di atas "
           "ujung pegas, (b) tepat menyentuh pegas yang belum termampatkan "
           "(y = 0), (c) pegas termampat maksimum sebesar Y. Acuan y = 0 "
           "diletakkan di titik (b), y positif ke atas.")

    penyelesaian(doc)
    p(doc, "**Yang bekerja hanya gaya konservatif.** Gaya gravitasi bekerja "
           "sepanjang seluruh perjalanan bola (dari keadaan a sampai c), "
           "sedangkan gaya pegas baru bekerja setelah bola menyentuh pegas "
           "(dari b ke c). Karena keduanya konservatif dan tidak ada gesekan, "
           "energi mekanik kekal. Namun perhatikan: karena ada **dua** bentuk "
           "energi potensial, keduanya harus muncul dalam persamaan.")
    langkah(doc, [
        "**Tetapkan acuan.** Ambil y = 0 di titik bola menyentuh pegas yang "
        "belum termampatkan; y positif ke atas. Maka titik lepas berada di "
        "y₁ = +h = +0,550 m, dan titik terendah (mampatan maksimum) berada di "
        "y₂ = −Y = −0,150 m.",

        "**Tuliskan keadaan 1 (titik lepas).** Bola dilepas dari keadaan diam, "
        "jadi K₁ = 0. Pegas belum termampatkan, jadi energi potensial "
        "pegasnya nol. Energi potensial gravitasinya U₁ = mgh. "
        "Energi mekanik awal: E₁ = 0 + mgh + 0 = mgh.",

        "**Tuliskan keadaan 2 (mampatan maksimum).** Bola berhenti sesaat, "
        "jadi K₂ = 0. Energi potensial gravitasinya kini U₂ = −mgY (karena "
        "berada di bawah acuan), dan energi potensial pegasnya "
        "U~pegas~ = ½kY². Energi mekanik akhir: E₂ = 0 − mgY + ½kY².",

        "**Samakan energi mekanik awal dan akhir.**",
    ])
    rumus(doc, "mgh = −mgY + ½kY²")
    rumus(doc, "mgh + mgY = ½kY²   →   mg(h + Y) = ½kY²")
    rumus(doc, "k = 2mg(h + Y) / Y²")
    langkah(doc, [
        "**Masukkan angka** (h dan Y diubah ke meter lebih dahulu: 55,0 cm = "
        "0,550 m dan 15,0 cm = 0,150 m).",
    ], start=5)
    rumus(doc, "k = 2(2,60 kg)(9,8 m/s²)(0,550 m + 0,150 m) / (0,150 m)²")
    rumus(doc, "k = (50,96 N)(0,700 m) / 0,0225 m² = 35,67 / 0,0225")
    rumus(doc, "k = 1.585 N/m ≈ 1,6 × 10³ N/m")
    jawaban(doc, "k ≈ **1,6 × 10³ N/m** (sekitar 1.600 N/m, atau 1,6 kN/m).")
    catatan(doc, "Kesalahan yang paling sering terjadi: menulis "
                 "mgh = ½kY² sehingga suku mgY hilang. Hasilnya menjadi "
                 "k = 2mgh/Y² ≈ 1,25 × 10³ N/m, yaitu terlalu kecil sekitar "
                 "21% dari nilai yang benar. "
                 "Penyebabnya, pada keadaan akhir bola masih berada 15 cm di "
                 "bawah titik sentuh, sehingga energi potensial gravitasinya "
                 "berkurang — pengurangan itu ikut menambah energi pegas. "
                 "Perhatikan juga bahwa h diukur **sampai titik sentuh**, "
                 "bukan sampai dasar pegas.")

    # ---------------------------------------------------------- SOAL 2
    judul_soal(doc, 2, "Dua seluncuran air: siapa lebih cepat, siapa lebih "
                       "dulu sampai", "Slide CONCEPTUAL EXAMPLE 6-9 · "
                       "Gambar 6-19 · Subbab 5-2 Kekekalan Energi Mekanik")
    soal_teks(doc, "Dua seluncuran air di sebuah kolam berbentuk berbeda, tetapi "
                   "keduanya dimulai pada ketinggian yang sama h (Gbr. 6-19). "
                   "Dua peluncur mulai dari keadaan diam pada waktu yang sama "
                   "di seluncuran yang berbeda. (a) Peluncur mana, Paul atau "
                   "Corinne, yang bergerak lebih cepat di dasar? (b) Peluncur "
                   "mana yang lebih dulu sampai di dasar? Abaikan gesekan dan "
                   "anggap kedua seluncuran memiliki panjang lintasan yang sama.")
    penyelesaian(doc)
    p(doc, "**(a) Siapa yang lebih cepat di dasar?**")
    p(doc, "Karena tidak ada gesekan, satu-satunya gaya yang melakukan usaha "
           "adalah gravitasi, sehingga energi mekanik kekal. Bandingkan puncak "
           "dan dasar:")
    rumus(doc, "mgh = ½mv²   →   v = √(2gh)")
    p(doc, "Massa m saling menghapus, dan **bentuk lintasan tidak muncul dalam "
           "rumus**. Yang menentukan laju di dasar hanya ketinggian h. Karena "
           "kedua peluncur mulai dari ketinggian yang sama, keduanya tiba di "
           "dasar dengan laju yang **sama besar**.")
    p(doc, "**(b) Siapa yang lebih dulu sampai?**")
    p(doc, "Ini pertanyaan yang berbeda: bukan tentang laju akhir, tetapi "
           "tentang **waktu tempuh**. Di bagian lintasan yang lebih curam, "
           "energi potensial lebih cepat berubah menjadi energi kinetik, "
           "sehingga peluncur bergerak lebih cepat pada bagian awal. "
           "Seluncuran Corinne memiliki bagian curam di awal, sedangkan "
           "seluncuran Paul menurun perlahan sehingga Paul bergerak lambat "
           "pada sebagian besar lintasan.")
    p(doc, "Karena panjang kedua lintasan sama tetapi laju rata-rata Corinne "
           "lebih besar, Corinne memerlukan waktu yang lebih singkat. Jadi "
           "**Corinne sampai lebih dulu**, walaupun laju keduanya di garis "
           "akhir sama.")
    jawaban(doc, "(a) Keduanya **sama cepat** di dasar, v = √(2gh). "
                 "(b) **Corinne** sampai lebih dulu, karena laju rata-ratanya "
                 "sepanjang lintasan lebih besar.")
    catatan(doc, "Kekekalan energi hanya memberi tahu **laju pada suatu "
                 "ketinggian**, bukan **waktu tempuh**. Waktu bergantung pada "
                 "seluruh riwayat gerak (bentuk lintasan), maka soal seperti "
                 "ini tidak boleh diselesaikan dengan kekekalan energi saja. "
                 "Inilah alasan larangan „abaikan bentuk lintasan“ hanya "
                 "berlaku untuk laju, tidak untuk waktu.")

    # ---------------------------------------------------------- SOAL 3
    judul_soal(doc, 3, "Anak meluncur di seluncuran air",
               "Slide Gambar 8-8 · Subbab 5-2 Kekekalan Energi Mekanik")
    soal_teks(doc, "Gambar 8-8 menunjukkan seorang anak bermassa m meluncur "
                   "dari keadaan diam pada puncak seluncuran air pada "
                   "ketinggian h = 8,5 m. Dengan mengasumsikan seluncuran "
                   "tersebut tanpa gesekan karena air yang mengalirinya, "
                   "tentukan laju anak di bagian dasar seluncuran.")
    penyelesaian(doc)
    p(doc, "Energi mekanik kekal karena gaya normal dari dinding seluncuran "
           "selalu tegak lurus arah gerak sehingga tidak melakukan usaha, dan "
           "gesekan diabaikan. Ambil acuan y = 0 di dasar seluncuran.")
    rumus(doc, "K~puncak~ + U~puncak~ = K~dasar~ + U~dasar~")
    rumus(doc, "0 + mgh = ½mv² + 0")
    rumus(doc, "v = √(2gh) = √(2 × 9,8 × 8,5) = √166,6")
    rumus(doc, "v ≈ 12,9 m/s")
    jawaban(doc, "v ≈ **12,9 m/s** (sekitar 46 km/jam).")
    catatan(doc, "Massa anak tidak perlu diketahui karena saling menghapus. "
                 "Bentuk lintasan (spiral) juga tidak mempengaruhi hasil — "
                 "sama seperti Soal 2 bagian (a). Jika ada gesekan, hasil ini "
                 "adalah **batas laju maksimum**; laju sesungguhnya akan lebih "
                 "kecil.")

    # ---------------------------------------------------------- SOAL 4
    judul_soal(doc, 4, "Laju kereta roller-coaster dengan kekekalan energi",
               "Slide EXAMPLE 6-8 · Gambar 6-18 · ditulis juga di papan tulis")
    soal_teks(doc, "Dengan menganggap ketinggian bukit pada Gbr. 6-18 adalah "
                   "40 m dan kereta roller-coaster mulai dari keadaan diam di "
                   "puncak, hitung (a) laju kereta di dasar bukit, dan "
                   "(b) pada ketinggian berapa kereta akan memiliki setengah "
                   "laju tersebut. Ambil y = 0 di dasar bukit.")
    penyelesaian(doc)
    p(doc, "**Diketahui:** y₁ = 40 m (puncak, v₁ = 0), y₂ = 0 (dasar), "
           "g = 9,8 m/s². **Ditanya:** (a) v₂, (b) y ketika v = ½v₂.")
    p(doc, "**(a) Laju di dasar bukit.** Kekekalan energi mekanik, dengan "
           "acuan y = 0 di dasar:")
    rumus(doc, "K₂ + U₂ = K₁ + U₁")
    rumus(doc, "½mv₂² + mgy₂ = ½mv₁² + mgy₁")
    rumus(doc, "½v₂² + (9,8)(0) = ½(0)² + (9,8)(40)")
    rumus(doc, "½v₂² = 392   →   v₂ = √784 = 28 m/s")
    p(doc, "**(b) Ketinggian saat lajunya setengah.** Setengah dari laju di "
           "dasar adalah v = ½(28) = 14 m/s. Pakai kekekalan energi lagi, "
           "kali ini dari puncak ke titik berketinggian y:")
    rumus(doc, "½mv² + mgy = ½mv₁² + mgy₁")
    rumus(doc, "½v² + gy = 0 + gy₁   →   y = y₁ − v²/(2g)")
    rumus(doc, "y = 40 − (14)²/(2 × 9,8) = 40 − 196/19,6 = 40 − 10 = 30 m")
    jawaban(doc, "(a) v₂ = **28 m/s** di dasar bukit; (b) kereta memiliki "
                 "setengah laju itu pada ketinggian **30 m** di atas dasar.")
    catatan(doc, "Perhatikan pola yang penting: energi kinetik bergantung pada "
                 "v², sehingga **setengah laju berarti seperempat energi "
                 "kinetik**. Karena itu kereta masih berada cukup tinggi "
                 "(30 m dari 40 m) ketika lajunya baru setengah. Massa kereta "
                 "tidak diperlukan karena saling menghapus.")

    # ================================================== Bagian B
    judul_bagian(doc, "BAGIAN B — USAHA OLEH GAYA YANG BERUBAH DAN USAHA "
                      "OLEH GAYA PEGAS")
    p(doc, "Tiga soal berikut menuntut keterampilan yang berbeda: **membaca "
           "grafik** dan menghitung luas di bawahnya. Untuk gaya yang besar "
           "atau arahnya berubah, rumus W = Fd cos φ tidak berlaku lagi; "
           "usaha harus dihitung sebagai **luas daerah** di bawah kurva "
           "gaya–posisi, atau melalui integral.", space_after=6)
    rumus(doc, "W = ∫ F_x dx  =  luas daerah di bawah kurva F_x terhadap x")
    p(doc, "Dua aturan praktis yang wajib diingat: luas **di atas** sumbu x "
           "bertanda **positif** (energi masuk ke benda), luas **di bawah** "
           "sumbu x bertanda **negatif** (energi keluar dari benda). "
           "Perhatikan pula bahwa satuan luas pada grafik a–x adalah m²/s², "
           "bukan joule — harus dikalikan massa lebih dahulu.", space_after=8)

    # ---------------------------------------------------------- SOAL 5
    judul_soal(doc, 5, "Grafik percepatan terhadap posisi",
               "Slide Problem 37 · Figure 7-40 (Halliday–Resnick–Walker) · "
               "Subbab 4-5 Usaha oleh Gaya Berubah")
    soal_teks(doc, "Gambar 7-40 memberikan percepatan sebuah partikel 2,00 kg "
                   "ketika sebuah gaya terpasang F~a~ menggerakkannya dari "
                   "keadaan diam sepanjang sumbu x dari x = 0 sampai "
                   "x = 9,0 m. Skala sumbu vertikal gambar ditetapkan oleh "
                   "a~s~ = 6,0 m/s². Berapa usaha yang telah dilakukan gaya itu "
                   "pada partikel ketika partikel mencapai (a) x = 4,0 m, "
                   "(b) x = 7,0 m, dan (c) x = 9,0 m? Berapa laju dan arah "
                   "gerak partikel ketika mencapai (d) x = 4,0 m, "
                   "(e) x = 7,0 m, dan (f) x = 9,0 m?")
    gambar(doc, IMG / "gbr-7-40.png", 15.2,
           "Gambar 2. Kurva percepatan a terhadap posisi x (Fig. 7-40). "
           "Skala vertikal ditetapkan oleh a~s~ = 6,0 m/s². Daerah biru "
           "bertanda positif, daerah merah bertanda negatif.")

    penyelesaian(doc)
    p(doc, "**Kunci pertama: ubah grafik a–x menjadi gaya.** Hukum II Newton "
           "memberi F_x = m a_x, sehingga")
    rumus(doc, "W = ∫ F_x dx = ∫ m a_x dx = m ∫ a_x dx = m × (luas kurva a–x)")
    p(doc, "Jadi usaha tidak sama dengan luas kurva, tetapi **massa dikali "
           "luas kurva**. Inilah jebakan utama soal ini: luas kurva bersatuan "
           "m²/s², sedangkan usaha bersatuan joule.")

    p(doc, "**Kunci kedua: baca bentuk kurvanya.** Dari gambar, kurva terdiri "
           "atas lima penggal:")
    poin(doc, [
        "0 → 1 m: naik dari 0 ke +a~s~ (segitiga)",
        "1 → 4 m: tetap +a~s~ (persegi panjang, lebar 3 m)",
        "4 → 6 m: turun dari +a~s~ ke −a~s~, memotong sumbu di x = 5 m",
        "6 → 8 m: tetap −a~s~ (persegi panjang, lebar 2 m)",
        "8 → 9 m: naik dari −a~s~ ke 0 (segitiga)",
    ])

    p(doc, "**Hitung luas kumulatif** (dalam satuan a~s~ × m):")
    rumus(doc, "L(0→1) = ½(1)(a~s~) = 0,5a~s~      L(1→4) = (3)(a~s~) = 3a~s~")
    rumus(doc, "L(4→5) = +0,5a~s~      L(5→6) = −0,5a~s~      "
               "L(6→7) = −a~s~")
    rumus(doc, "L(7→8) = −a~s~      L(8→9) = −0,5a~s~")

    p(doc, "**(a) Usaha sampai x = 4,0 m.** Luasnya = 0,5a~s~ + 3a~s~ = 3,5a~s~. "
           "Dengan a~s~ = 6,0 m/s², luas = 21,0 m²/s².")
    rumus(doc, "W = m × luas = (2,00 kg)(21,0 m²/s²) = 42 J")

    p(doc, "**(b) Usaha sampai x = 7,0 m.** Tambahkan penggal 4→7 m: "
           "+0,5a~s~ − 0,5a~s~ − a~s~ = −a~s~, sehingga luas kumulatif menjadi "
           "3,5a~s~ − a~s~ = 2,5a~s~ = 15,0 m²/s².")
    rumus(doc, "W = (2,00)(15,0) = 30 J")
    p(doc, "Perhatikan bahwa di antara x = 5 m dan x = 7 m gaya berarah "
           "berlawanan dengan gerak, sehingga usaha pada bagian itu **negatif** "
           "(benda kehilangan energi kinetik).")

    p(doc, "**(c) Usaha sampai x = 9,0 m.** Tambahkan lagi penggal 7→9 m: "
           "−a~s~ − 0,5a~s~ = −1,5a~s~. Luas kumulatif menjadi "
           "2,5a~s~ − 1,5a~s~ = 1,0a~s~ = 6,0 m²/s².")
    rumus(doc, "W = (2,00)(6,0) = 12 J")

    p(doc, "**(d)–(f) Laju dan arah gerak.** Karena partikel mulai dari diam, "
           "K₁ = 0, sehingga K = W pada setiap titik (teorema "
           "usaha–energi kinetik). Dengan K = ½mv² dan m = 2,00 kg, maka "
           "v = √W (dalam satuan SI):")
    rumus(doc, "x = 4,0 m:  ½(2,00)v² = 42  →  v = √42 = 6,5 m/s")
    rumus(doc, "x = 7,0 m:  ½(2,00)v² = 30  →  v = √30 = 5,5 m/s")
    rumus(doc, "x = 9,0 m:  ½(2,00)v² = 12  →  v = √12 = 3,5 m/s")
    p(doc, "Karena energi kinetik tetap **positif** di ketiga titik, partikel "
           "tidak pernah berhenti dan tidak berbalik arah; ketiga laju itu "
           "berarah **+x**.")
    jawaban(doc, "Usaha: (a) **42 J**, (b) **30 J**, (c) **12 J**. "
                 "Laju: (d) **6,5 m/s** searah +x, (e) **5,5 m/s** searah +x, "
                 "(f) **3,5 m/s** searah +x.")
    catatan(doc, "Perhatikan bahwa laju **menurun** dari x = 5 m sampai "
                 "x = 9 m walaupun partikel terus bergerak maju — tanda bahwa "
                 "gaya berubah arah menjadi melawan gerak. Jangan tertukar "
                 "antara „perlambatan“ dan „gerak mundur“: keduanya berbeda.")

    # ---------------------------------------------------------- SOAL 6
    judul_soal(doc, 6, "Keju di lantai kabin elevator",
               "Slide Problem 25 · Figure 7-34 (Halliday–Resnick–Walker) · "
               "Subbab 4-2 Usaha dan Teorema Usaha–Energi")
    soal_teks(doc, "Pada Gbr. 7-34, sebuah balok keju bermassa 0,250 kg "
                   "terletak di lantai kabin elevator 900 kg yang ditarik ke "
                   "atas oleh sebuah kabel sejauh d₁ = 2,40 m dan kemudian "
                   "sejauh d₂ = 10,5 m. (a) Sepanjang d₁, jika gaya normal "
                   "pada balok dari lantai memiliki besar konstan "
                   "F~N~ = 3,00 N, berapa usaha yang dilakukan pada kabin oleh "
                   "gaya dari kabel? (b) Sepanjang d₂, jika usaha yang "
                   "dilakukan pada kabin oleh gaya (konstan) dari kabel "
                   "adalah 92,61 kJ, berapa besar F~N~?")
    penyelesaian(doc)
    p(doc, "Strateginya adalah **analisis gaya dua tahap**: tinjau keju lebih "
           "dahulu untuk memperoleh percepatan, lalu tinjau kabin beserta "
           "kejunya untuk memperoleh tegangan kabel. Keju dan kabin bergerak "
           "bersama, jadi percepatannya sama.")

    p(doc, "**Bagian (a).** Pada keju bekerja dua gaya vertikal: gaya normal "
           "F~N~ ke atas dan berat m~c~ g ke bawah. Ambil arah naik sebagai "
           "positif:")
    rumus(doc, "F~N~ − m~c~ g = m~c~ a   →   a = F~N~/m~c~ − g")
    rumus(doc, "a = 3,00/0,250 − 9,8 = 12,0 − 9,8 = 2,2 m/s²")
    p(doc, "Pada kabin (beserta keju di dalamnya) bekerja tegangan kabel T ke "
           "atas dan berat total (M + m~c~)g ke bawah:")
    rumus(doc, "T − (M + m~c~)g = (M + m~c~)a")
    rumus(doc, "T = (M + m~c~)(g + a) = (900 + 0,250)(9,8 + 2,2) = 10.803 N")
    p(doc, "Kabel sejajar dengan perpindahan (φ = 0°), sehingga")
    rumus(doc, "W = T d₁ cos 0° = (1,08 × 10⁴ N)(2,40 m) = 2,59 × 10⁴ J")

    p(doc, "**Bagian (b).** Kali ini usahanya diketahui, dan yang dicari gaya "
           "normal. Dari usaha kabel diperoleh tegangan kabel:")
    rumus(doc, "T = W/d₂ = 92.610 J / 10,5 m = 8.820 N")
    p(doc, "Tegangan ini hampir sama dengan berat total sistem "
           "(900,25 × 9,8 = 8.822 N), jadi percepatannya praktis nol — kabin "
           "bergerak dengan laju hampir tetap. Masukkan ke persamaan kabin "
           "untuk memastikan:")
    rumus(doc, "a = T/(M + m~c~) − g = 8.820/900,25 − 9,8 ≈ 0 m/s²")
    p(doc, "Karena a ≈ 0, gaya normal pada keju hanya perlu menopang beratnya:")
    rumus(doc, "F~N~ = m~c~(g + a) ≈ (0,250)(9,8 + 0) = 2,45 N")
    jawaban(doc, "(a) W ≈ **2,6 × 10⁴ J** (25,9 kJ). "
                 "(b) F~N~ ≈ **2,45 N**.")
    catatan(doc, "Perhatikan bahwa gaya normal berubah dari 3,00 N menjadi "
                 "2,45 N walaupun massanya sama: gaya normal bukan sekadar "
                 "sama dengan berat, tetapi bergantung pada percepatan "
                 "(F~N~ = m(g + a)). Ketika kabin bergerak dengan laju tetap, "
                 "gaya normal tepat sama dengan berat keju. Ini contoh baik "
                 "bahwa „berat“ dan „gaya normal“ adalah dua besaran berbeda.")

    # ---------------------------------------------------------- SOAL 7
    judul_soal(doc, 7, "Usaha oleh gaya bergantung posisi (integrasi dua dimensi)",
               "Slide WORK DONE BY A GENERAL VARIABLE FORCE · "
               "Sample Problem 7-08 · Subbab 4-5")
    soal_teks(doc, "Sebuah gaya F = (3x² N) î + (4 N) ĵ, dengan x dalam meter, "
                   "bekerja pada sebuah partikel dan hanya mengubah energi "
                   "kinetik partikel tersebut. Berapa usaha yang dilakukan "
                   "gaya itu ketika partikel berpindah dari koordinat "
                   "(2 m, 3 m) ke (3 m, 0 m)? Apakah laju partikel bertambah, "
                   "berkurang, atau tetap?")
    penyelesaian(doc)
    p(doc, "Untuk gaya yang bergantung pada posisi, usaha dihitung dengan "
           "integral perkalian titik sepanjang perpindahan. Dalam dua dimensi, "
           "integral itu terpecah menjadi dua bagian:")
    rumus(doc, "W = ∫ F · dr = ∫ F_x dx + ∫ F_y dy")
    p(doc, "Karena F_y = 4 N konstan dan F_x = 3x² hanya bergantung pada x, "
           "kedua integral dapat dihitung terpisah dengan batas masing-masing:")
    rumus(doc, "W = ∫₂³ 3x² dx + ∫₃⁰ 4 dy")
    rumus(doc, "∫₂³ 3x² dx = [x³]₂³ = 27 − 8 = 19 J")
    rumus(doc, "∫₃⁰ 4 dy = 4(0 − 3) = −12 J")
    rumus(doc, "W = 19 − 12 = 7 J")
    p(doc, "Karena W bernilai positif, teorema usaha–energi kinetik "
           "(ΔK = W) memberi ΔK > 0, sehingga **laju partikel bertambah**. "
           "Jika hasilnya negatif, laju akan berkurang; jika nol, laju tetap.")
    jawaban(doc, "W = **7 J**; laju partikel **bertambah** (energi kinetiknya "
                 "naik 7 J).")
    catatan(doc, "Tanda negatif pada suku y muncul karena partikel bergerak "
                 "dari y = 3 m **turun** ke y = 0 m, sedangkan komponen gaya "
                 "F_y berarah ke +y. Jadi gaya itu justru menahan gerak pada "
                 "arah y, sementara komponen F_x membantu gerak. Hasil akhir "
                 "adalah selisih keduanya. Sering terjadi kekeliruan "
                 "menjumlahkan besar gaya lebih dahulu (|F| = √(F_x² + F_y²)) "
                 "lalu dikalikan perpindahan — cara itu salah untuk gaya yang "
                 "berubah-ubah.")

    # ---------------------------------------------------------- SOAL 8
    judul_soal(doc, 8, "Usaha dari grafik gaya terhadap posisi",
               "Slide Problem 13 · Figure 6-38 (Giancoli, Physics 7th ed.) · "
               "Subbab 4-5")
    soal_teks(doc, "Gaya pada sebuah partikel, yang bekerja sepanjang sumbu x, "
                   "berubah seperti ditunjukkan pada Gbr. 6-38. Tentukan usaha "
                   "yang dilakukan gaya ini untuk menggerakkan partikel "
                   "sepanjang sumbu x: (a) dari x = 0,0 sampai x = 10,0 m; "
                   "(b) dari x = 0,0 sampai x = 15,0 m.")
    gambar(doc, IMG / "gbr-6-38.png", 15.2,
           "Gambar 3. Kurva gaya F_x terhadap posisi x (Fig. 6-38). Daerah "
           "biru (di atas sumbu) memberi usaha positif, daerah merah (di bawah "
           "sumbu) memberi usaha negatif.")

    penyelesaian(doc)
    p(doc, "Usaha sama dengan luas daerah di bawah kurva. Karena kurva "
           "berupa garis lurus, luasnya dapat dipecah menjadi bangun-bangun "
           "sederhana: segitiga, persegi panjang, dan trapesium.")

    p(doc, "**(a) Dari x = 0,0 sampai x = 10,0 m.** Daerah ini seluruhnya di "
           "atas sumbu x dan dapat dipecah menjadi tiga bagian:")
    poin(doc, [
        "Segitiga 0 → 3 m: ½ × 3 × 400 = **600 J**",
        "Persegi panjang 3 → 7 m: 4 × 400 = **1.600 J**",
        "Segitiga 7 → 10 m: ½ × 3 × 400 = **600 J**",
    ])
    p(doc, "Cara cepat: bentuk keseluruhannya trapesium dengan sisi sejajar "
           "10 m dan 4 m serta tinggi 400 N.")
    rumus(doc, "W = ½ (10 + 4)(400) = 2.800 J")
    p(doc, "**(b) Dari x = 0,0 sampai x = 15,0 m.** Tambahkan bagian "
           "10 → 15 m yang berada **di bawah** sumbu x, sehingga usahanya "
           "negatif:")
    poin(doc, [
        "Segitiga 10 → 11,5 m: ½ × 1,5 × (−200) = **−150 J**",
        "Persegi panjang 11,5 → 13,5 m: 2 × (−200) = **−400 J**",
        "Segitiga 13,5 → 15 m: ½ × 1,5 × (−200) = **−150 J**",
    ])
    p(doc, "Jumlah bagian negatif: −150 − 400 − 150 = −700 J. Cara cepat: "
           "trapesium dengan sisi sejajar 5 m dan 2 m serta tinggi −200 N.")
    rumus(doc, "W(10→15 m) = ½ (5 + 2)(−200) = −700 J")
    rumus(doc, "W total = 2.800 J − 700 J = 2.100 J")
    jawaban(doc, "(a) W = **2,8 × 10³ J** (2.800 J); "
                 "(b) W = **2,1 × 10³ J** (2.100 J).")
    catatan(doc, "Kesalahan umum: menjumlahkan **besar** luas tanpa "
                 "memperhatikan tanda, sehingga bagian (b) dihitung "
                 "2.800 + 700 = 3.500 J. Padahal pada x = 10 m sampai 15 m "
                 "gaya berarah berlawanan dengan perpindahan, jadi energi "
                 "kinetik partikel justru berkurang. Perhatikan juga bahwa "
                 "usaha total dari 0 ke 15 m lebih kecil daripada usaha dari "
                 "0 ke 10 m — bukan berarti geraknya mundur, melainkan "
                 "partikelnya diperlambat.")

    # ================================================== Bagian C
    judul_bagian(doc, "BAGIAN C — RINGKASAN JAWABAN DAN POLA PENYELESAIAN")

    rows = [
        ("Soal", "Inti persoalan", "Langkah kunci", "Jawaban"),
        ("1", "Dua energi potensial sekaligus (gravitasi + pegas)",
         "mgh + mgY = ½kY²", "k ≈ 1,6 × 10³ N/m"),
        ("2", "Laju vs waktu tempuh pada dua lintasan",
         "v = √(2gh); waktu bergantung bentuk lintasan",
         "laju sama; Corinne lebih dulu"),
        ("3", "Seluncuran air tanpa gesekan",
         "mgh = ½mv²", "v ≈ 12,9 m/s"),
        ("4", "Roller-coaster, ketinggian 40 m",
         "½v² + gy = gy₁", "v = 28 m/s; y = 30 m"),
        ("5", "Grafik a–x, cari usaha, lalu laju",
         "W = m × luas; K = W", "42 J; 30 J; 12 J; 6,5; 5,5; 3,5 m/s"),
        ("6", "Elevator, gaya normal, tegangan kabel",
         "F~N~ − m~c~ g = m~c~ a; T = W/d", "2,6 × 10⁴ J; 2,45 N"),
        ("7", "Integrasi dua dimensi",
         "W = ∫F_x dx + ∫F_y dy", "W = 7 J; laju bertambah"),
        ("8", "Luas trapesium pada grafik F–x",
         "W = ½(a + b)h, tanda sesuai posisi", "2.800 J; 2.100 J"),
    ]
    table = doc.add_table(rows=0, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = doc.styles["Table Grid"]
    set_table_pct(table)
    table_borders(table, color="BFB5A4", sz=6)
    widths = [Cm(1.3), Cm(5.6), Cm(5.6), Cm(3.6)]

    for i, row_data in enumerate(rows):
        row = table.add_row()
        for j, txt in enumerate(row_data):
            cell = row.cells[j]
            cell.width = widths[j]
            if i == 0:
                cell_shading(cell, "7A1F1F")
            elif i % 2 == 0:
                cell_shading(cell, "FBF8F2")
            cell.text = ""
            par = cell.paragraphs[0]
            par.paragraph_format.space_before = Pt(2)
            par.paragraph_format.space_after = Pt(2)
            par.paragraph_format.line_spacing = 1.0
            par.alignment = (WD_ALIGN_PARAGRAPH.CENTER
                             if j == 0 or i == 0 else WD_ALIGN_PARAGRAPH.LEFT)
            r = par.add_run(txt)
            r.font.size = Pt(8.6 if i else 8.8)
            r.bold = (i == 0) or (j == 0 and i > 0)
            if i == 0:
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            elif j == 3:
                r.font.color.rgb = RGBColor(0x33, 0x4D, 0x24)
                r.bold = True

    p(doc, "", space_after=2)
    p(doc, "**Pola yang dapat dipakai ulang.** Lima soal pertama menunjukkan "
           "bahwa hampir semua soal energi dapat diselesaikan dengan urutan "
           "yang sama:", space_after=4)
    langkah(doc, [
        "**Tetapkan titik acuan** y = 0 dan tuliskan semua bentuk energi "
        "potensial yang terlibat (gravitasi, pegas).",
        "**Tuliskan keadaan awal dan akhir**: tinggi, laju, dan mampatan "
        "pegas di kedua keadaan.",
        "**Periksa syarat kekekalan**: apakah hanya gaya konservatif yang "
        "melakukan usaha? Jika ada gesekan, tambahkan ΔE_termal = f_k d.",
        "**Samakan energi mekanik** (atau gunakan ΔK = W_neto), lalu "
        "selesaikan secara simbolik lebih dahulu.",
        "**Masukkan angka** dan periksa satuan serta kewajaran hasilnya.",
    ])
    p(doc, "Sementara tiga soal terakhir menunjukkan pola khusus untuk gaya "
           "yang berubah: **gambar daerah di bawah kurva**, beri tanda positif "
           "atau negatif sesuai posisinya terhadap sumbu, jumlahkan, lalu "
           "gunakan ΔK = W untuk memperoleh laju. Bila gaya bergantung pada "
           "dua koordinat, integralkan per komponen — jangan dijumlahkan "
           "besar gayanya lebih dahulu.", space_after=8)

    p(doc, "**Satu hal yang paling sering diuji.** Perhatikan bahwa pada "
           "Soal 5 laju partikel menurun, pada Soal 8 usaha total lebih kecil "
           "daripada usaha pada bagian awal, dan pada Soal 2 kedua peluncur "
           "memiliki laju akhir sama tetapi waktu tempuh berbeda. Ketiganya "
           "adalah cara penguji menanyakan hal yang sama: **apakah Anda "
           "memahami bahwa energi kinetik, laju, dan waktu adalah tiga hal "
           "yang berbeda?**", space_after=10)

    penutup = doc.add_paragraph()
    penutup.paragraph_format.space_before = Pt(6)
    penutup.paragraph_format.space_after = Pt(2)
    par_border(penutup, top=(6, "C9C0AF", 6))
    r = penutup.add_run("Delapan soal di atas ditulis kembali dari tayangan "
                        "slide dan papan tulis pertemuan minggu ke-4 sampai "
                        "ke-6, lalu dibahas menggunakan notasi dan konstanta "
                        "yang sama (g = 9,8 m/s²).")
    r.font.size = Pt(8.8)
    r.italic = True
    r.font.color.rgb = ABU_MUDA


def main():
    doc = new_document()
    header_footer(doc)
    cover(doc)
    daftar_isi(doc)
    isi(doc)
    doc.save(OUT)
    print("Tersimpan:", OUT)
    print("Ukuran:", round(OUT.stat().st_size / 1024, 1), "KB")


if __name__ == "__main__":
    main()
