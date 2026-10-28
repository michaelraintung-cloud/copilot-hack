"""Merender laporan DOCX menjadi PDF memakai ReportLab + metrik Times.

Sumber konten: <laporan>.layout.json yang dihasilkan saat DOCX dibangun.
Tujuannya ganda: (1) menyediakan berkas PDF siap kirim, (2) memungkinkan
verifikasi jumlah halaman dan tata letak secara visual.

Font Times-Roman/Times-Bold/Times-Italic (core PDF) memiliki metrik identik
dengan Times New Roman, sehingga paginasi PDF ini mendekati hasil Word.
"""
import json
import os
import re
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Table, TableStyle, Image, PageBreak,
                                KeepTogether, CondPageBreak)
from reportlab.pdfbase import pdfmetrics
from PIL import Image as PILImage

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(HERE, "..", "output")
SRC = os.path.join(OUTDIR, "laporan-studi-kasus-4.layout.json")
PDF = os.path.join(OUTDIR, "laporan-studi-kasus-4.pdf")

# ---------------------------------------------------------------- tipografi
FONT_R, FONT_B, FONT_I, FONT_BI = "Times-Roman", "Times-Bold", "Times-Italic", "Times-BoldItalic"
NAVY = colors.HexColor("#1F3864")
GREY = colors.HexColor("#595959")
LINE = colors.HexColor("#8EAADB")
ROWA = colors.HexColor("#EDF2F9")
ROWB = colors.HexColor("#DCE6F1")

# Karakter yang tidak tersedia pada encoding WinAnsi -> padanan aman
SUBST = {
    "≥": "≥", "≤": "≤", "−": "–", "≈": "~", "Σ": "∑", "→": "→", "×": "x",
    "÷": "/", "±": "+/-", "\u2011": "-", "\u2212": "-",
}
# core font (WinAnsi) mendukung ≥? tidak. Ganti dengan teks.
SUBST.update({"≥": "min. ", "≤": "maks. ", "Σ": "Jumlah", "→": "-", "×": "x", "÷": ":",
              "±": "+/-", "≈": "~"})


def esc(text):
    t = text
    for k, v in SUBST.items():
        t = t.replace(k, v)
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # pemulihan entitas hasil substitusi
    # rapikan spasi ganda akibat substitusi kata
    t = t.replace("  ", " ")
    return t


def rich(text, size, bold=False, italic=False, color=None):
    """Ubah penanda **tebal** / *miring* menjadi tag reportlab."""
    out = []
    for tok in re.split(r"(\*\*.+?\*\*|\*.+?\*)", text):
        if not tok:
            continue
        b, i = bold, italic
        if tok.startswith("**") and tok.endswith("**") and len(tok) > 4:
            tok, b = tok[2:-2], True
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            tok, i = tok[1:-1], True
        body = esc(tok)
        if b and i:
            body = f"<b><i>{body}</i></b>"
        elif b:
            body = f"<b>{body}</b>"
        elif i:
            body = f"<i>{body}</i>"
        out.append(body)
    if color:
        return f'<font color="{color}">' + "".join(out) + "</font>"
    return "".join(out)


def style(size=12, leading=None, align=TA_JUSTIFY, space_before=0, space_after=0,
          first_indent=0, left_indent=0, font=FONT_R):
    return ParagraphStyle(
        name=f"s{size}{align}{space_before}", fontName=font, fontSize=size,
        leading=leading or size * 1.5, alignment=align,
        spaceBefore=space_before, spaceAfter=space_after,
        firstLineIndent=first_indent, leftIndent=left_indent,
    )


# ---------------------------------------------------------------- dokumen
class Doc(BaseDocTemplate):
    def __init__(self, path):
        super().__init__(
            path, pagesize=A4,
            leftMargin=2.54 * cm, rightMargin=2.54 * cm,
            topMargin=2.54 * cm, bottomMargin=2.54 * cm,
            title="Laporan Studi Kasus 4 - Armada Banyak, Pengiriman Tetap Terlambat",
            author="Laporan Studi Kasus Manajemen Industri",
            subject="Analisis Efisiensi Distribusi dan Kualitas Layanan",
        )
        frame = Frame(self.leftMargin, self.bottomMargin,
                      self.width, self.height, id="body",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=self.footer)])

    def footer(self, canv, doc):
        canv.saveState()
        canv.setFont(FONT_R, 10)
        canv.setFillColor(colors.HexColor("#404040"))
        canv.drawCentredString(A4[0] / 2, 1.4 * cm, str(doc.page))
        canv.restoreState()


def build_table(spec):
    headers = spec["headers"]
    rows = spec["rows"]
    widths = [w * cm for w in spec["widths"]]
    fs = spec.get("font_size", 8) or 8
    hfs = spec.get("header_size", fs) or fs
    aligns = spec.get("align") or ["center"] * len(headers)
    bold_rows = set(spec.get("bold_rows") or [])
    first_bold = spec.get("first_col_bold")

    amap = {"left": TA_LEFT, "center": TA_CENTER, "right": TA_RIGHT, "justify": TA_JUSTIFY}

    data = []
    hdr = []
    for h in headers:
        hdr.append(Paragraph(f"<b>{esc(h)}</b>",
                             ParagraphStyle("h", fontName=FONT_B, fontSize=hfs, leading=hfs * 1.15,
                                            alignment=TA_CENTER, textColor=colors.white)))
    data.append(hdr)
    for ri, row in enumerate(rows):
        cells = []
        for ci, val in enumerate(row):
            bold = (first_bold and ci == 0) or (ri in bold_rows)
            cells.append(Paragraph(rich(str(val), fs, bold=bold),
                                   ParagraphStyle(f"c{ri}{ci}", fontName=FONT_B if bold else FONT_R,
                                                  fontSize=fs, leading=fs * 1.22,
                                                  alignment=amap[aligns[ci]])))
        data.append(cells)

    t = Table(data, colWidths=widths, repeatRows=1, hAlign="CENTER")
    cmds = [
        ("GRID", (0, 0), (-1, -1), 0.4, LINE),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
        ("LEFTPADDING", (0, 0), (-1, -1), 3.2),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3.2),
    ]
    for ri in range(len(rows)):
        if ri in bold_rows:
            cmds.append(("BACKGROUND", (0, ri + 1), (-1, ri + 1), ROWB))
        elif ri % 2 == 1:
            cmds.append(("BACKGROUND", (0, ri + 1), (-1, ri + 1), ROWA))
    t.setStyle(TableStyle(cmds))
    return t


def _indent_table(tbl, left):
    outer = Table([[tbl]], colWidths=[15.9 * cm])
    outer.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), left),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return outer


def to_flow(log):
    flow = []
    for blk in log:
        t = blk["t"]
        if t == "pb":
            flow.append(PageBreak())
        elif t == "h":
            lvl = blk["level"]
            size = {1: 14, 2: 12, 3: 12}[lvl]
            txt = blk["text"].upper() if lvl == 1 else blk["text"]
            before = {1: 6, 2: 13, 3: 10}[lvl]
            after = {1: 10, 2: 5, 3: 4}[lvl]
            flow.append(Paragraph(f"<b>{esc(txt)}</b>",
                                  style(size, leading=size * 1.5, align=TA_LEFT,
                                        space_before=before, space_after=after,
                                        font=FONT_B).clone("h", textColor=NAVY)))
        elif t == "caption":
            flow.append(Paragraph(f"<b>{esc(blk['text'])}</b>",
                                  style(blk.get("size", 10), leading=12, align=TA_CENTER,
                                        space_before=8, space_after=6, font=FONT_B)))
        elif t == "p":
            size = blk.get("size", 12)
            align = {"justify": TA_JUSTIFY, "left": TA_LEFT, "center": TA_CENTER,
                     "right": TA_RIGHT}[blk.get("align", "justify")]
            ind = 1.27 * cm if blk.get("indent") else 0
            st = style(size, leading=size * (blk.get("spacing", 1.5) or 1.5), align=align,
                       space_before=blk.get("space_before", 0), space_after=blk.get("after", 0),
                       first_indent=ind)
            if blk.get("color") == "navy":
                st = st.clone("navy", textColor=NAVY)
            flow.append(Paragraph(rich(blk["text"], size), st))
        elif t == "space":
            flow.append(Spacer(1, blk.get("pts", 12)))
        elif t == "rule":
            w = blk.get("width_cm", 15.0) * cm
            t2 = Table([[""]], colWidths=[w], rowHeights=[1])
            t2.setStyle(TableStyle([
                ("LINEBELOW", (0, 0), (-1, -1), 0.9, NAVY),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
            flow.append(Spacer(1, 6))
            flow.append(t2)
            flow.append(Spacer(1, 6))
        elif t == "center":
            size = blk.get("size", 12)
            txt = blk["text"]
            style_ = style(size, leading=size * (1.0 if size >= 12 else 1.2), align=TA_CENTER,
                           space_after=blk.get("after", 2),
                           font=FONT_B if blk.get("bold") else FONT_R)
            if blk.get("color") == "navy":
                style_ = style_.clone("navycenter", textColor=NAVY)
            flow.append(Paragraph(rich(txt, size, bold=blk.get("bold"), italic=blk.get("italic")),
                                  style_))
        elif t == "tocentry":
            lvl = blk.get("level", 1)
            size = 10.5
            left = (0.0, 0.6, 1.2)[min(lvl, 3) - 1] * cm
            bold = lvl == 1
            txt = Paragraph(rich(blk["text"], size, bold=bold),
                            ParagraphStyle("toc", fontName=FONT_B if bold else FONT_R,
                                           fontSize=size, leading=size * 1.12,
                                           alignment=TA_LEFT))
            num = Paragraph(str(blk["page"]),
                            ParagraphStyle("tocn", fontName=FONT_B if bold else FONT_R,
                                           fontSize=size, leading=size * 1.12,
                                           alignment=TA_RIGHT))
            tbl = Table([[txt, num]], colWidths=[15.9 * cm - left - 1.2 * cm, 1.2 * cm])
            tbl.setStyle(TableStyle([
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 5 if lvl == 1 else 0.6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0.6),
                ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
            ]))
            flow.append(Spacer(1, 0))
            flow.append(tbl) if left == 0 else flow.append(_indent_table(tbl, left))
        elif t == "list":
            size = blk.get("size", 12)
            marker = blk["marker"]
            st = style(size, leading=size * 1.5, align=TA_JUSTIFY, left_indent=0.85 * cm,
                       first_indent=-0.85 * cm)
            flow.append(Paragraph(f"{esc(marker)}\t" + rich(blk["text"], size), st,
                                  bulletText=None))
        elif t == "table":
            flow.append(Spacer(1, 3))
            flow.append(Paragraph(f"<b>{esc(blk['title'])}</b>",
                                  style(10, leading=12, align=TA_CENTER, space_before=4,
                                        space_after=4, font=FONT_B).clone("tc", keepWithNext=1)))
            tbl = build_table(blk)
            flow.append(tbl)
            if blk.get("note"):
                flow.append(Paragraph(esc(blk["note"]),
                                      style(8, leading=10, align=TA_LEFT, space_before=3,
                                            space_after=10).clone("n", textColor=GREY)))
            else:
                flow.append(Spacer(1, 8))
        elif t == "figure":
            path = blk["path"]
            w = blk["width_cm"] * cm
            with PILImage.open(path) as im:
                iw, ih = im.size
            h = w * ih / iw
            flow.append(Spacer(1, 4))
            flow.append(KeepTogether([
                Image(path, width=w, height=h),
                Paragraph(f"<b>{esc(blk['title'])}</b>",
                          style(10, leading=12, align=TA_CENTER, space_before=3, space_after=2,
                                font=FONT_B).clone("fc", keepWithNext=1)),
            ]))
            if blk.get("note"):
                flow.append(Paragraph(esc(blk["note"]),
                                      style(8, leading=10, align=TA_LEFT, space_after=8)
                                      .clone("fn", textColor=GREY)))
    return flow


def main():
    with open(SRC, encoding="utf-8") as f:
        log = json.load(f)
    doc = Doc(PDF)
    doc.build(to_flow(log))
    print("PDF tersimpan:", os.path.abspath(PDF))


if __name__ == "__main__":
    main()
