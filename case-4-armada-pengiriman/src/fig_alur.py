# -*- coding: utf-8 -*-
"""Membuat Gambar 2.1 (alur proses operasional saat ini) sebagai PNG.

Ukuran kanvas 451 x 152 pt agar saat disisipkan selebar 15,9 cm,
ukuran huruf di dalam gambar sama dengan ukuran titik aslinya.
"""
import math
import os

import pymupdf

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fig_alur.png")

W, H = 451, 110
doc = pymupdf.open()
page = doc.new_page(width=W, height=H)
page.draw_rect(pymupdf.Rect(0, 0, W, H), color=None, fill=(1, 1, 1))

F, FB = "tiro", "tibo"
GREY = (0.32, 0.32, 0.32)
EDGE = (0.25, 0.31, 0.42)
BLUE = (0.90, 0.93, 0.97)


def text_c(x, y, s, size=7.6, font=F, color=(0, 0, 0)):
    w = pymupdf.Font(fontname=font).text_length(s, fontsize=size)
    page.insert_text((x - w / 2, y), s, fontname=font, fontsize=size, color=color)


def box(x, y, bw, bh, title, sub):
    page.draw_rect(pymupdf.Rect(x, y, x + bw, y + bh), color=EDGE, fill=BLUE, width=0.8,
                   radius=0.08)
    text_c(x + bw / 2, y + 12, title, size=7.8, font=FB)
    if sub:
        text_c(x + bw / 2, y + 23, sub, size=6.8, color=GREY)


def arrow(x1, y1, x2, y2, dashed=False, color=(0.35, 0.35, 0.35)):
    if dashed:
        page.draw_line(pymupdf.Point(x1, y1), pymupdf.Point(x2, y2), color=color,
                       width=0.8, dashes="[3 3] 0")
    else:
        page.draw_line(pymupdf.Point(x1, y1), pymupdf.Point(x2, y2), color=color, width=0.9)
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (0.42, -0.42):
        page.draw_line(pymupdf.Point(x2, y2),
                       pymupdf.Point(x2 - 5 * math.cos(ang + s), y2 - 5 * math.sin(ang + s)),
                       color=color, width=0.9)


BW, BH, GAP, TOP = 102, 32, 11, 6
xs = [2.5 + i * (BW + GAP) for i in range(4)]

box(xs[0], TOP, BW, BH, "Pesanan diterima", "daftar pengiriman")
box(xs[1], TOP, BW, BH, "Penyusunan rute", "manual: peta + urutan pesanan")
box(xs[2], TOP, BW, BH, "Pelaksanaan rute", "kemacetan, jadwal berubah")
box(xs[3], TOP, BW, BH, "Penerimaan barang", "jadwal penerimaan bergeser")

for i in range(3):
    arrow(xs[i] + BW + 1.5, TOP + BH / 2, xs[i + 1] - 2, TOP + BH / 2)

# penanda kegagalan di bawah kotak 2 dan 3
def flag(x, y_wire, label, lines):
    page.draw_line(pymupdf.Point(x, TOP + BH), pymupdf.Point(x, y_wire), color=(0.6, 0.2, 0.2),
                   width=0.7, dashes="[2 2] 0")
    page.draw_circle(pymupdf.Point(x, y_wire), 1.9, color=(0.6, 0.2, 0.2), fill=(0.6, 0.2, 0.2))
    text_c(x, y_wire + 10, label, size=6.9, font=FB, color=(0.55, 0.15, 0.15))
    text_c(x, y_wire + 18, lines, size=6.5, color=(0.35, 0.35, 0.35))


flag(xs[1] + BW / 2, 50, "petunjuk: urutan tidak optimal", "kembali melewati jalan yang sama")
flag(xs[2] + BW / 2, 50, "petunjuk: posisi tidak terpantau", "keterlambatan tidak terdeteksi")

# aliran balik informasi (garis putus-putus) dari kotak 4 ke kotak 1
y_low = 82
page.draw_line(pymupdf.Point(xs[3] + BW / 2, TOP + BH), pymupdf.Point(xs[3] + BW / 2, y_low),
               color=(0.45, 0.45, 0.45), width=0.8, dashes="[3 3] 0")
page.draw_line(pymupdf.Point(xs[3] + BW / 2, y_low), pymupdf.Point(xs[0] + BW / 2, y_low),
               color=(0.45, 0.45, 0.45), width=0.8, dashes="[3 3] 0")
page.draw_line(pymupdf.Point(xs[0] + BW / 2, y_low), pymupdf.Point(xs[0] + BW / 2, TOP + BH),
               color=(0.45, 0.45, 0.45), width=0.8, dashes="[3 3] 0")
arrow(xs[0] + BW / 2, y_low, xs[0] + BW / 2, TOP + BH + 1, color=(0.45, 0.45, 0.45))
text_c(W / 2, y_low - 6, "kabar keterlambatan: pengemudi menelepon kantor, lalu diteruskan ke pelanggan",
       size=6.8, color=(0.3, 0.3, 0.3))

# keterangan tambahan
text_c(W / 2, y_low + 16, "informasi mengalir mundur setelah kejadian, bukan saat kejadian",
       size=6.8, font=FB, color=(0.55, 0.15, 0.15))

pix = page.get_pixmap(dpi=400)
pix.save(OUT)
print("tersimpan:", OUT, pix.width, "x", pix.height)
