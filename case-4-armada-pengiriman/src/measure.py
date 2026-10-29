# -*- coding: utf-8 -*-
"""Mengukur perkiraan jumlah halaman naskah sebelum dibangun ke .docx."""
import re
import sys

from pagefit import Layout
import naskah_final as N

MARGIN = 2.54


def measure(verbose=False):
    L = Layout(margin_cm=MARGIN)
    L.page = 3          # halaman 1 sampul, 2 ringkasan
    L.y = 0.0
    marks = []
    for blk in N.B:
        kind = blk[0]
        if kind == "h1":
            marks.append((L.page, L.y / L.height, blk[1]))
            L.para(blk[1], 12, style="bold", multiple=1.5, space_before=6, space_after=6)
        elif kind == "h2":
            marks.append((L.page, L.y / L.height, "  " + blk[1]))
            L.para(blk[1], 12, style="bold", multiple=1.5, space_before=4, space_after=0)
        elif kind == "p":
            L.para(blk[1], 12, multiple=1.5, indent_cm=1.27 if blk[2] else 0)
        elif kind in ("num", "bul"):
            for item in blk[1]:
                L.para(item, 12, multiple=1.5, indent_cm=1.27)
        elif kind == "fig":
            L.figure(blk[3], space_before=4, space_after=2)
            L.para(blk[4], 10.5, style="bold", multiple=1.0, space_before=0, space_after=4)
        elif kind == "tbl":
            s = blk[1]
            L.para(s["caption"], 11, style="bold", multiple=1.0,
                   space_before=4, space_after=2)
            rows = [s["headers"]] + [[str(c) for c in r] for r in s["rows"]]
            L.table(rows, s["widths"], size=s.get("size", 9.0), space_before=0,
                    space_after=2, cell_pad_cm=0.13)
            if s.get("note"):
                L.para(s["note"], 9, style="italic", multiple=1.0,
                       space_before=2, space_after=0)
    body_pages = L.page - 3 + L.y / L.height
    # pustaka
    L.para("DAFTAR PUSTAKA", 12, style="bold", multiple=1.5, space_before=10, space_after=8)
    for item in N.PUSTAKA:
        L.para(item, 12, multiple=1.5, indent_cm=1.27, space_after=6)
    total = L.page - 1 + L.y / L.height

    if verbose:
        for pg, fill, name in marks:
            print(f"   hal {pg:2d} ({fill:4.2f})  {name}")
    return body_pages, total


def words():
    n = 0
    for blk in N.B:
        if blk[0] == "p":
            n += len(re.findall(r"\w+", blk[1]))
        elif blk[0] in ("num", "bul"):
            n += sum(len(re.findall(r"\w+", x)) for x in blk[1])
    return n


if __name__ == "__main__":
    body, total = measure(verbose="-v" in sys.argv)
    print(f"prosa {words()} kata | isi BAB I-VI ≈ {body:.2f} hlm | total ≈ {total:.2f} hlm")
