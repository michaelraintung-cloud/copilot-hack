#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dokumen Word (A4): "29 SOAL + PEMBAHASAN — SETIAP RUMUS DIJABARKAN"

Isi: 29 soal dari Cheatsheet Fisika I (setiap poin rumus = satu soal), ditulis
ulang dan dikerjakan, dengan penjabaran rumus, tabel lambang, analisis satuan,
syarat pemakaian, dan pemeriksaan hasil.
"""
from pathlib import Path

from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

import docx_kit as kit
from docx_kit import (ABU, ABU_MUDA, HIJAU, HITAM, MERAH, MERAH2,
                      banner_judul, blok_penutup_cover, catatan,
                      cell_shading, header_footer, jawaban, judul_bagian,
                      judul_item, keep_row_together, label, langkah,
                      normalize_order, p, poin, rich, rumus, set_cell_margins,
                      set_table_pct, soal_teks, syarat, table_borders,
                      tabel_lambang, par_shading, par_border)

from konten29_m45 import ITEMS_M45
from konten29_m6 import ITEMS_M6

BASE = Path(__file__).resolve().parent
OUT = BASE / "Fisika-Dasar-I-29-Soal-Setiap-Rumus-Dijabarkan.docx"

ITEMS = ITEMS_M45 + ITEMS_M6

BAGIAN = [
    ("A", "MINGGU 4 · USAHA DAN ENERGI KINETIK", 1, 8,
     "Rumus acuan minggu ini: W = F d cos θ; W~net~ = ΣW~i~; K = ½mv²; W~net~ = ΔK; "
     "W = ∫F·dr; P = W/Δt dan P = F·v.",
     "Delapan soal pertama bertumpu pada satu gagasan: usaha adalah energi yang dipindahkan "
     "gaya. Semua soal berikutnya di bab energi merupakan pengembangan dari W = ΔK."),
    ("B", "MINGGU 5 · ENERGI POTENSIAL DAN KEKEKALAN ENERGI", 9, 16,
     "Rumus acuan minggu ini: U~g~ = mgy; ΔU~g~ = mgΔy; W~g~ = −ΔU~g~; U~s~ = ½kx²; "
     "W~s~ = −ΔU~s~; E~mech~ = K + U; ΔE~mech~ = W~nc~.",
     "Delapan soal berikut menuntut satu kebiasaan baru: menetapkan titik acuan lebih dahulu, "
     "lalu menuliskan **semua** bentuk energi potensial yang terlibat."),
    ("C", "MINGGU 6 · PUSAT MASSA, MOMENTUM, DAN IMPULS", 17, 24,
     "Rumus acuan: r~CM~ = Σm~i~r~i~/M; F~ext~ = Ma~CM~; P = Σm~i~v~i~ = Mv~CM~; "
     "J = ∫F dt = Δp; F~avg~ = Δp/Δt.",
     "Bagian ini berpindah dari besaran skalar (energi) ke besaran **vektor**. Satu aturan yang "
     "harus dipegang: tetapkan arah positif, lalu tuliskan tanda + atau − pada setiap kecepatan."),
    ("D", "MINGGU 6 · KEKEKALAN MOMENTUM DAN TUMBUKAN", 25, 29,
     "Rumus acuan: Σmv sebelum = Σmv sesudah; elastis: K kekal; sempurna tidak elastis: "
     "v~f~ = (m₁v₁ + m₂v₂)/(m₁ + m₂); elastis 1D: v₁f = [(m₁−m₂)v₁i + 2m₂v₂i]/(m₁+m₂).",
     "Lima soal terakhir. Ingat pembagian tugasnya: pada setiap tumbukan **momentum selalu "
     "kekal**, tetapi **energi kinetik hanya kekal bila elastis**."),
]

RINGKAS = [
    (1, "Usaha gaya konstan", "W = F d cos θ", "50 J"),
    (2, "Usaha beberapa gaya", "W~net~ = ΣF~i~d cos θ~i~", "153,4 J"),
    (3, "Gaya berubah (integral)", "W = ∫F~x~ dx", "18 J; v = 4,24 m/s"),
    (4, "Gaya dua dimensi", "W = ∫F~x~dx + ∫F~y~dy", "+7 J; laju bertambah"),
    (5, "Luas grafik F–x", "W = luas kurva", "20 J; v = 4,47 m/s"),
    (6, "Teorema usaha–energi", "W = ΔK = ½m(v~f~² − v~i~²)", "+16 J"),
    (7, "Jarak pengereman", "d ∝ v²", "72 m"),
    (8, "Daya", "P = W/Δt ; P = Fv", "60 W"),
    (9, "Energi potensial gravitasi", "ΔU = mgΔy ; W~g~ = −ΔU", "+58,8 J; −58,8 J"),
    (10, "Jatuh bebas", "K~i~+U~i~ = K~f~+U~f~", "15,3 m/s"),
    (11, "Roller-coaster", "½mv² + mgy = tetap", "28 m/s; 30 m"),
    (12, "Energi pegas → gerak", "½kx² = ½mv²", "3,16 m/s"),
    (13, "Hukum Hooke & usaha pegas", "F = −kx ; W = ½k(x~i~²−x~f~²)", "−20 N; +0,84 J"),
    (14, "Bola menekan pegas", "mg(h+x) = ½kx²", "1,59 × 10³ N/m"),
    (15, "Gesekan & energi termal", "f~k~ = μ~k~N ; ΔE~th~ = f~k~d", "−29,4 J; v = 2,66 m/s"),
    (16, "Gaya nonkonservatif", "ΔE~mech~ = W~nc~", "−30 J"),
    (17, "Pusat massa 1D", "x~CM~ = Σm~i~x~i~/M", "2,4 m"),
    (18, "Pusat massa 2D", "x~CM~, y~CM~", "(1, 1) m"),
    (19, "Pusat massa batang", "(1/M)∫x dm", "2 m"),
    (20, "Hukum II Newton sistem", "F~ext~ = Ma~CM~", "3 m/s²"),
    (21, "Momentum & v~CM~", "P = Mv~CM~", "+2 kg·m/s; 0,67 m/s"),
    (22, "Impuls bola memantul", "J = Δp ; F = J/Δt", "−4,5 N·s; −300 N"),
    (23, "Impuls gaya konstan", "J = FΔt", "10 N·s; 20 m/s"),
    (24, "Impuls grafik F–t", "J = ∫F dt", "5 N·s; 20 m/s"),
    (25, "Elastis vs tidak elastis", "ΔK = K~f~ − K~i~", "tidak elastis; 8 J"),
    (26, "Menyatu (searah)", "v = (m₁v₁+m₂v₂)/(m₁+m₂)", "2 m/s; ΔK = −12 J"),
    (27, "Menyatu (berlawanan)", "P~i~ = P~f~", "−0,5 m/s; ΔK = −13,5 J"),
    (28, "Elastis, massa sama", "bertukar kecepatan", "0 ; +4 m/s"),
    (29, "Elastis, massa beda", "rumus v₁f, v₂f", "−1 m/s; +4 m/s"),
]

# hasil hitung ulang independen (dipakai pada lampiran verifikasi)
VERIFIKASI = [
    (1, "20 × 5 × cos 60°", "50 J", "sesuai"),
    (2, "88,33 + 65,11", "153,45 J", "sesuai (dibulatkan 153,4)"),
    (3, "2(3)² = 18; √(2·18/2)", "18 J; 4,243 m/s", "sesuai"),
    (4, "(27 − 8) + 4(0 − 3)", "7 J", "sesuai"),
    (5, "½·4·10; √(2·20/2)", "20 J; 4,472 m/s", "sesuai"),
    (6, "½·2·(25 − 9)", "16 J", "sesuai"),
    (7, "(108/54)² × 18", "72 m", "sesuai"),
    (8, "600/10; 20 × 3", "60 W; 60 W", "sesuai"),
    (9, "2·9,8·3", "58,8 J; −58,8 J", "sesuai"),
    (10, "√(2·9,8·12)", "15,336 m/s", "sesuai (15,34 pada cheatsheet)"),
    (11, "√784; 40 − 196/19,6", "28 m/s; 30 m", "sesuai"),
    (12, "½·200·0,1² ; √(2·1/0,2)", "1,0 J; 3,162 m/s", "sesuai"),
    (13, "−200·0,1 ; 100(0,01 − 0,0016)", "−20 N; 0,84 J", "sesuai"),
    (14, "2·2,6·9,8·0,7/0,15²", "1.585,4 N/m", "sesuai (1,59 × 10³)"),
    (15, "0,2·29,4 ; 40 − 29,4 ; √(2·10,6/3)", "5,88 N; 10,6 J; 2,658 m/s", "sesuai"),
    (16, "70 − 100", "−30 J", "sesuai"),
    (17, "(0 + 12)/5", "2,4 m", "sesuai"),
    (18, "6/6 ; 6/6", "(1, 1) m", "sesuai"),
    (19, "L/2 = 4/2", "2 m", "sesuai"),
    (20, "15/5", "3 m/s²", "sesuai"),
    (21, "2·3 + 1·(−4) ; 2/3", "2 kg·m/s; 0,667 m/s", "sesuai"),
    (22, "0,15(−30) ; −4,5/0,015", "−4,5 N·s; −300 N", "sesuai"),
    (23, "50·0,2 ; 10/0,5", "10 N·s; 20 m/s", "sesuai"),
    (24, "½·0,5·20 ; 5/0,25", "5 N·s; 20 m/s", "sesuai"),
    (25, "12 − 20", "−8 J", "sesuai"),
    (26, "6/3 ; 18 → 6", "2 m/s; −12 J", "sesuai"),
    (27, "−2/4 ; 14 → 0,5", "−0,5 m/s; −13,5 J", "sesuai"),
    (28, "v₁f = 0 ; v₂f = 4", "0; 4 m/s", "sesuai"),
    (29, "−5/5 ; 20/5 ; p & K", "−1; 4 m/s; 10 = 10; 25 = 25", "sesuai"),
]


# ------------------------------------------------------------------ bagian
def cover(doc):
    banner_judul(
        doc,
        "FISIKA DASAR I  ·  BEK1EAB4",
        "29 SOAL & PEMBAHASAN",
        "Setiap rumus dijelaskan, setiap hasil diperiksa\n"
        "Usaha · Energi · Momentum · Pusat Massa · Tumbukan",
        [
            ("Sumber soal", "Cheatsheet Fisika I — “Setiap Rumus Ada Soal” "
                            "(29 poin rumus, Minggu 4–6)"),
            ("Sumber teori", "Tiga berkas kuliah: Kinetic Energy and Work; Potential Energy "
                             "and Conservation of Energy; Center of Mass – Linear Momentum "
                             "and Collision"),
            ("Isi tiap soal", "Penjabaran rumus → tabel lambang → analisis satuan → syarat "
                              "pemakaian → soal → penyelesaian → pemeriksaan hasil → jawaban"),
            ("Verifikasi", "Seluruh 29 jawaban dihitung ulang secara numerik; hasilnya "
                           "dicantumkan pada Lampiran A"),
        ])
    blok_penutup_cover(doc)


def cara_baca(doc):
    judul_bagian(doc, "CARA MEMBACA DOKUMEN INI", page_break=True)
    p(doc, "Dokumen ini memuat **seluruh 29 soal** dari cheatsheet Fisika I — satu soal untuk "
           "setiap poin rumus pada Minggu 4, 5, dan 6. Agar rumusnya benar-benar dipahami "
           "(bukan dihafal), setiap soal disusun dengan urutan tetap berikut:", space_after=5)
    langkah(doc, [
        "**Rumus inti** — rumus kunci soal, ditulis di bawah judul.",
        "**Penjabaran rumus** — apa arti rumus itu, dari mana asalnya, dan bagaimana bentuk "
        "khususnya muncul. Bagian inilah yang membuat rumus tidak lagi terasa “diberikan "
        "begitu saja”.",
        "**Tabel keterangan lambang** — setiap lambang dijelaskan artinya **dan** satuannya, "
        "sehingga tidak ada lambang yang muncul tanpa penjelasan.",
        "**Analisis satuan** — pemeriksaan dimensi: apakah ruas kiri dan kanan benar-benar "
        "bersatuan sama. Cara ini dapat menangkap banyak kesalahan sebelum menghitung.",
        "**Syarat pemakaian** — kapan rumus boleh dipakai dan kapan harus diganti rumus lain.",
        "**Soal** — ditulis ulang sesuai cheatsheet.",
        "**Penyelesaian** — bertahap: rumus → substitusi angka → hasil, tanpa melompat.",
        "**Pemeriksaan hasil** — dicek dengan cara kedua, batas nilai, tanda, atau kewajaran "
        "angka. Bagian ini membuktikan bahwa jawaban memang benar, bukan hanya “kelihatan benar”.",
        "**Jawaban** dan **Catatan** (kesalahan yang sering terjadi).",
    ])
    label(doc, "Kesepakatan notasi dan satuan", space_before=8)
    poin(doc, [
        "Satuan SI; g = 9,8 m/s². Angka desimal memakai koma (2,5) dan ribuan memakai titik "
        "(2.800).",
        "Joule (J) = N·m untuk usaha/energi; watt (W) = J/s untuk daya; N·s = kg·m/s untuk "
        "momentum/impuls.",
        "Arah positif ditetapkan lebih dahulu (umumnya ke kanan dan ke atas); kecepatan yang "
        "berlawanan arah diberi tanda minus.",
        "Energi kinetik K = ½mv² selalu ≥ 0 walaupun v bertanda minus, karena v dikuadratkan.",
        "Momentum dan impuls adalah **vektor**; usaha, energi, dan daya adalah **skalar**.",
    ])
    p(doc, "", space_after=2)
    label(doc, "Catatan tentang penomoran", space_before=6)
    p(doc, "Nomor soal 1–29 sama dengan nomor poin pada cheatsheet, sehingga mudah dicocokkan. "
           "Pembagiannya: Soal 1–8 (Minggu 4), 9–16 (Minggu 5), 17–24 (pusat massa, momentum, "
           "impuls), 25–29 (tumbukan).", space_after=6)


def daftar_soal(doc):
    judul_bagian(doc, "DAFTAR 29 SOAL DAN JAWABAN SINGKAT", page_break=True,
                 sub="Jawaban di kolom terakhir sudah diverifikasi ulang (lihat Lampiran A) dan "
                     "dapat dipakai untuk memeriksa hasil latihan sendiri.")
    table = doc.add_table(rows=0, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = doc.styles["Table Grid"]
    set_table_pct(table)
    table_borders(table, color="CFC6B5", sz=4)
    set_cell_margins(table, top=26, bottom=26, left=70, right=70)
    widths = (Cm(1.1), Cm(5.3), Cm(5.4), Cm(4.3))

    head = table.add_row()
    keep_row_together(head)
    for j, txt in enumerate(("No", "Pokok bahasan", "Rumus inti", "Jawaban")):
        cell = head.cells[j]
        cell.width = widths[j]
        cell_shading(cell, "7A1F1F")
        cell.text = ""
        par = cell.paragraphs[0]
        par.paragraph_format.space_before = Pt(1)
        par.paragraph_format.space_after = Pt(1)
        par.paragraph_format.line_spacing = 0.95
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0, 3) else WD_ALIGN_PARAGRAPH.LEFT
        r = par.add_run(txt)
        r.font.size = Pt(8.3)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, (no, pokok, rm, jw) in enumerate(RINGKAS):
        row = table.add_row()
        keep_row_together(row)
        for j, txt in enumerate((str(no), pokok, rm, jw)):
            cell = row.cells[j]
            cell.width = widths[j]
            if i % 2 == 1:
                cell_shading(cell, "FBF8F2")
            cell.text = ""
            par = cell.paragraphs[0]
            par.paragraph_format.space_before = Pt(1)
            par.paragraph_format.space_after = Pt(1)
            par.paragraph_format.line_spacing = 1.0
            if j == 0:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            rich(par, txt, size=8.2)
            if j == 0:
                for r in par.runs:
                    r.bold = True
                    r.font.color.rgb = MERAH
            if j == 2:
                for r in par.runs:
                    r.italic = True
            if j == 3:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in par.runs:
                    r.bold = True
                    r.font.color.rgb = HIJAU
    gap = doc.add_paragraph()
    gap.paragraph_format.space_after = Pt(2)


def render_item(doc, it):
    judul_item(doc, it["no"], it["judul"], it["rumus_inti"], it["sumber"])

    label(doc, "1. Rumus dan penjabarannya", space_before=3, space_after=3)
    for line in it["rumus"]:
        rumus(doc, line[0], line[1] if len(line) > 1 else None)
    for par in it["penjabaran"]:
        p(doc, par, space_after=3, indent=0.1)

    label(doc, "2. Keterangan lambang", space_before=6, space_after=3)
    tabel_lambang(doc, it["lambang"])

    label(doc, "3. Analisis satuan", space_before=4, space_after=3)
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.left_indent = Cm(0.15)
    pf.space_before = Pt(2)
    pf.space_after = Pt(6)
    pf.line_spacing = 1.1
    par_shading(par, "F2F6FA")
    par_border(par, left=(10, "1F4E79", 8))
    rich(par, it["satuan"], size=9.4)

    label(doc, "4. Syarat pemakaian", space_before=2, space_after=3)
    syarat(doc, it["syarat"], prefix="")

    label(doc, "5. Soal", space_before=2, space_after=3)
    soal_teks(doc, it["soal"])

    label(doc, "6. Penyelesaian", color=HITAM, space_before=6, space_after=3)
    for blok in it["isi"]:
        if blok[0] == "p":
            p(doc, blok[1], space_after=3)
        elif blok[0] == "f":
            rumus(doc, blok[1], blok[2] if len(blok) > 2 else None)
        elif blok[0] == "l":
            langkah(doc, blok[1])

    label(doc, "7. Pemeriksaan hasil", color=RGBColor(0x1F, 0x4E, 0x79),
          space_before=6, space_after=3)
    for t in it["cek"]:
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(1.1)
        pf.first_line_indent = Cm(-0.4)
        pf.space_after = Pt(2)
        pf.line_spacing = 1.08
        r = par.add_run("✓\t")
        r.font.color.rgb = RGBColor(0x2E, 0x6B, 0x3A)
        r.bold = True
        r.font.size = Pt(9.6)
        rich(par, t, size=9.6)

    jawaban(doc, it["jawaban"])
    catatan(doc, it["catatan"])


def bagian(doc, huruf, judul, awal, akhir, rumus_acuan, pengantar):
    judul_bagian(doc, f"BAGIAN {huruf}  ·  {judul}", page_break=True,
                 sub=f"Soal {awal}–{akhir} ({akhir - awal + 1} soal)")
    p(doc, pengantar, space_after=4)
    par = doc.add_paragraph()
    par.paragraph_format.left_indent = Cm(0.15)
    par.paragraph_format.space_before = Pt(2)
    par.paragraph_format.space_after = Pt(8)
    par.paragraph_format.line_spacing = 1.1
    par_shading(par, "FAF7F0")
    par_border(par, left=(12, "B8860B", 8))
    r = par.add_run("Rumus acuan bagian ini:  ")
    r.bold = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x8A, 0x6D, 0x1F)
    rich(par, rumus_acuan, size=9.2, italic=True)
    for it in ITEMS:
        if awal <= it["no"] <= akhir:
            render_item(doc, it)


def lampiran_a(doc):
    judul_bagian(doc, "LAMPIRAN A — VERIFIKASI ULANG SELURUH 29 JAWABAN", page_break=True,
                 sub="Setiap jawaban dihitung ulang secara numerik (bukan disalin), memakai "
                     "rumus dan angka yang sama seperti pada pembahasan.")
    p(doc, "Tabel berikut memuat perhitungan ulang untuk setiap soal. Kolom terakhir "
           "menunjukkan kesesuaian dengan jawaban pada cheatsheet. Pemeriksaan dilakukan "
           "dengan kalkulator (bukan perkiraan), memakai g = 9,8 m/s².", space_after=6)

    table = doc.add_table(rows=0, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = doc.styles["Table Grid"]
    set_table_pct(table)
    table_borders(table, color="CFC6B5", sz=4)
    set_cell_margins(table, top=24, bottom=24, left=70, right=70)
    widths = (Cm(1.0), Cm(6.6), Cm(4.6), Cm(3.8))

    head = table.add_row()
    keep_row_together(head)
    for j, txt in enumerate(("No", "Perhitungan ulang", "Hasil", "Status")):
        cell = head.cells[j]
        cell.width = widths[j]
        cell_shading(cell, "7A1F1F")
        cell.text = ""
        par = cell.paragraphs[0]
        par.paragraph_format.space_before = Pt(1)
        par.paragraph_format.space_after = Pt(1)
        par.paragraph_format.line_spacing = 0.95
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0, 3) else WD_ALIGN_PARAGRAPH.LEFT
        r = par.add_run(txt)
        r.font.size = Pt(8.2)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for i, (no, hitung, hasil, status) in enumerate(VERIFIKASI):
        row = table.add_row()
        keep_row_together(row)
        for j, txt in enumerate((str(no), hitung, hasil, status)):
            cell = row.cells[j]
            cell.width = widths[j]
            if i % 2 == 1:
                cell_shading(cell, "FBF8F2")
            cell.text = ""
            par = cell.paragraphs[0]
            par.paragraph_format.space_before = Pt(1)
            par.paragraph_format.space_after = Pt(1)
            par.paragraph_format.line_spacing = 1.0
            if j in (0, 3):
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            rich(par, txt, size=8.1)
            if j == 0:
                for r in par.runs:
                    r.bold = True
                    r.font.color.rgb = MERAH
            if j == 2:
                for r in par.runs:
                    r.bold = True
            if j == 3:
                for r in par.runs:
                    r.bold = True
                    r.font.color.rgb = RGBColor(0x2E, 0x6B, 0x3A)
    gap = doc.add_paragraph()
    gap.paragraph_format.space_after = Pt(4)

    label(doc, "Kesimpulan verifikasi", space_before=8)
    poin(doc, [
        "**29 dari 29 jawaban sesuai** dengan hasil hitung ulang. Tidak ada kesalahan angka "
        "pada cheatsheet.",
        "Beberapa pembulatan berbeda tipis dan tidak mengubah hasil: Soal 10 (15,336 → 15,34 m/s), "
        "Soal 2 (153,45 → 153,4 J), Soal 15 (2,658 → 2,66 m/s), Soal 14 (1.585,4 → 1,59 × 10³ N/m).",
        "**Soal 29 diperiksa dua kali**: momentum (10 = 10 kg·m/s) dan energi kinetik "
        "(25 = 25 J) sama-sama kekal, sesuai syarat tumbukan elastis.",
        "**Soal 26 dan 27 diperiksa dengan hukum kekekalan energi total**: energi kinetik yang "
        "hilang (12 J dan 13,5 J) sama dengan energi yang berubah menjadi panas + deformasi.",
        "**Soal 7** diperiksa dengan dua cara (perbandingan kuadrat dan perhitungan perlambatan); "
        "keduanya memberi 72 m.",
    ])
    p(doc, "Dengan demikian, seluruh jawaban pada dokumen ini dapat dipakai sebagai acuan "
           "pembanding ketika mahasiswa mengerjakan latihan secara mandiri.", size=9.6,
      italic=True, color=ABU, space_after=4)


def lampiran_b(doc):
    judul_bagian(doc, "LAMPIRAN B — KARTU RUMUS (29 RUMUS DALAM SATU HALAMAN)",
                 page_break=True,
                 sub="Untuk dibaca ulang sebelum ujian. Kolom kanan menunjukkan soal tempat "
                     "rumus itu dipakai, sehingga dapat langsung dilatih.")
    kartu = [
        ("MINGGU 4 — USAHA DAN ENERGI KINETIK", None, None),
        ("W = F d cos θ", "usaha gaya konstan", "1"),
        ("W~net~ = ΣW~i~ = ΣF~i~d cos θ~i~", "usaha beberapa gaya", "2"),
        ("W = ∫F~x~ dx", "gaya berubah terhadap posisi", "3"),
        ("W = ∫F~x~ dx + ∫F~y~ dy", "gaya dua dimensi", "4"),
        ("W = luas kurva F–x", "membaca grafik", "5"),
        ("K = ½mv²", "energi kinetik", "6"),
        ("W~net~ = ΔK = ½m(v~f~² − v~i~²)", "teorema usaha–energi", "6"),
        ("d~stop~ = mv²/(2f)", "jarak pengereman", "7"),
        ("P = W/Δt ; P = Fv cos θ", "daya rata-rata & sesaat", "8"),
        ("MINGGU 5 — ENERGI POTENSIAL DAN KEKEKALAN", None, None),
        ("U~g~ = mgy ; ΔU~g~ = mgΔy", "energi potensial gravitasi", "9"),
        ("W~g~ = −ΔU~g~", "usaha gravitasi", "9"),
        ("K~i~ + U~i~ = K~f~ + U~f~", "kekekalan energi mekanik", "10, 11"),
        ("v = √(2gh)", "jatuh bebas / lintasan licin", "10, 11"),
        ("U~s~ = ½kx²", "energi potensial pegas", "12, 13"),
        ("F~s~ = −kx", "hukum Hooke", "13"),
        ("W~s~ = ½k(x~i~² − x~f~²) = −ΔU~s~", "usaha oleh pegas", "13"),
        ("mg(h + Y) = ½kY²", "bola jatuh menekan pegas", "14"),
        ("f~k~ = μ~k~N ; ΔE~th~ = f~k~d", "gesekan dan energi termal", "15"),
        ("ΔE~mech~ = W~nc~", "usaha nonkonservatif", "16"),
        ("MINGGU 6 — PUSAT MASSA, MOMENTUM, IMPULS", None, None),
        ("x~CM~ = Σm~i~x~i~/M", "pusat massa 1D", "17"),
        ("x~CM~ = Σm~i~x~i~/M ; y~CM~ = Σm~i~y~i~/M", "pusat massa 2D", "18"),
        ("r~CM~ = (1/M)∫r dm", "benda kontinu", "19"),
        ("F~ext,net~ = Ma~CM~", "hukum II Newton sistem", "20"),
        ("p = mv ; P = Σm~i~v~i~ = Mv~CM~", "momentum", "21"),
        ("J = Δp = m(v~f~ − v~i~) ; F~avg~ = J/Δt", "impuls & gaya rata-rata", "22, 23"),
        ("J = ∫F dt = luas grafik F–t", "impuls gaya berubah", "24"),
        ("MINGGU 6 — TUMBUKAN", None, None),
        ("Σmv (sebelum) = Σmv (sesudah)", "kekekalan momentum", "25–29"),
        ("v~f~ = (m₁v₁ + m₂v₂)/(m₁ + m₂)", "sempurna tidak elastis", "26, 27"),
        ("v₁f = [(m₁−m₂)v₁ + 2m₂v₂]/(m₁+m₂)", "elastis 1D (benda 1)", "29"),
        ("v₂f = [2m₁v₁ + (m₂−m₁)v₂]/(m₁+m₂)", "elastis 1D (benda 2)", "29"),
        ("m₁ = m₂ → bertukar kecepatan", "kasus khusus elastis", "28"),
    ]
    for kiri, tengah, kanan in kartu:
        if tengah is None:
            par = doc.add_paragraph()
            pf = par.paragraph_format
            pf.space_before = Pt(9)
            pf.space_after = Pt(3)
            pf.keep_with_next = True
            par_border(par, bottom=(6, "D8CFC0", 2))
            r = par.add_run(kiri)
            r.bold = True
            r.font.name = kit.HEAD
            r.font.size = Pt(9.4)
            r.font.color.rgb = MERAH2
            continue
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(3.4)
        pf.first_line_indent = Cm(-3.4)
        pf.space_before = Pt(0)
        pf.space_after = Pt(3.5)
        pf.line_spacing = 1.05
        pf.tab_stops.add_tab_stop(Cm(9.6))
        rich(par, kiri, size=9.4, bold=False)
        par.add_run("\t")
        rich(par, tengah, size=8.8, italic=True, color=ABU)
        if kanan:
            rich(par, f"  (soal {kanan})", size=8.4, color=ABU_MUDA)


def lampiran_c(doc):
    judul_bagian(doc, "LAMPIRAN C — SEPULUH KESALAHAN YANG PALING SERING TERJADI",
                 page_break=True,
                 sub="Diperiksa sebelum ujian; hampir semua kehilangan nilai pada bab ini "
                     "berasal dari daftar berikut.")
    butir = [
        ("Memakai W = F d cos θ untuk gaya yang berubah",
         "Pegas dan gaya bergantung posisi memerlukan ½k(x~i~² − x~f~²) atau ∫F dx. Lihat Soal 3, 5, 13."),
        ("Menjumlahkan besar usaha tanpa memperhatikan tanda",
         "Usaha total adalah **jumlah aljabar**; gaya yang melawan gerak memberi usaha negatif. Lihat Soal 2."),
        ("Salah tanda pada energi potensial dan usaha gravitasi",
         "Naik → ΔU positif, W~g~ negatif; turun → sebaliknya. Lihat Soal 9."),
        ("Menghilangkan suku mgY pada soal bola–pegas",
         "Penurunan total adalah h + Y, bukan h saja. Lihat Soal 14."),
        ("Memakai kekekalan energi mekanik padahal ada gesekan",
         "Tambahkan ΔE~th~ = f~k~d atau gunakan ΔE~mech~ = W~nc~. Lihat Soal 15, 16."),
        ("Menganggap gaya normal selalu sama dengan mg",
         "Pada bidang miring N = mg cos α; pada lift N = m(g ± a). Lihat Soal 15."),
        ("Menganggap energi kinetik kekal pada semua tumbukan",
         "Hanya tumbukan elastis yang mengekalkan K. Lihat Soal 25–27."),
        ("Lupa bahwa kecepatan berubah tanda saat memantul",
         "Δv = v~f~ − v~i~ dengan tanda berlawanan, sehingga Δv bisa lebih besar dari laju datang. "
         "Lihat Soal 22."),
        ("Tidak mengubah satuan ke SI lebih dahulu",
         "cm → m, km/jam → m/s (bagi 3,6), gram → kg, ms → s. Lihat Soal 7, 12, 14."),
        ("Tidak memeriksa kewajaran hasil",
         "Periksa satuan, tanda, dan orde besaran. Laju 300 m/s untuk benda jatuh 2 m pasti salah."),
    ]
    for i, (salah, benar) in enumerate(butir, 1):
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(0.85)
        pf.first_line_indent = Cm(-0.85)
        pf.space_before = Pt(3)
        pf.space_after = Pt(1)
        pf.keep_with_next = True
        r = par.add_run(f"{i}.")
        r.bold = True
        r.font.color.rgb = MERAH
        r.font.size = Pt(9.8)
        par.add_run("\t")
        rich(par, salah, size=10, bold=True)
        par2 = doc.add_paragraph()
        par2.paragraph_format.left_indent = Cm(0.85)
        par2.paragraph_format.space_before = Pt(0)
        par2.paragraph_format.space_after = Pt(6)
        par2.paragraph_format.line_spacing = 1.05
        rich(par2, "→ " + benar, size=9.4, color=ABU)


def penutup(doc):
    judul_bagian(doc, "PENUTUP", page_break=True)
    p(doc, "Dua puluh sembilan soal dalam dokumen ini mewakili **dua puluh sembilan rumus** yang "
           "menjadi inti Minggu 4 sampai Minggu 6. Setiap rumus tidak hanya ditulis, tetapi "
           "dijabarkan: apa artinya, dari mana asalnya, satuan apa yang dihasilkan, kapan boleh "
           "dipakai, dan bagaimana hasilnya diperiksa.", space_after=6)
    p(doc, "Tiga kebiasaan yang paling menentukan keberhasilan pada bab ini:", space_after=3)
    langkah(doc, [
        "**Selalu mulai dari rumus, bukan dari angka.** Tulis rumusnya, susun ulang untuk besaran "
        "yang dicari, baru masukkan angka — cara ini mengurangi kesalahan pembulatan dan "
        "memudahkan pemeriksaan.",
        "**Periksa satuan setiap kali.** Analisis satuan (bagian 3 pada setiap soal) dapat "
        "menangkap kesalahan sebelum hasil akhir dihitung.",
        "**Periksa kewajaran hasil.** Bandingkan dengan nilai batas: apakah lajunya masuk akal? "
        "Apakah tandanya sesuai arah gerak? Apakah energinya seorde dengan energi yang "
        "seharusnya?",
    ])
    p(doc, "", space_after=4)
    p(doc, "Untuk latihan mandiri: tutup bagian **Penyelesaian** dan **Pemeriksaan hasil**, lalu "
           "kerjakan ulang soal hanya dengan membaca bagian **Soal** dan **Rumus inti**. Setelah "
           "selesai, bandingkan **langkah** Anda — bukan hanya jawaban akhirnya.", space_after=8)
    p(doc, "Dokumen ini disusun dari Cheatsheet Fisika I (“Setiap Rumus Ada Soal”, 29 poin rumus "
           "Minggu 4–6) dengan rujukan teori pada tiga berkas kuliah Fisika Dasar I: Kinetic "
           "Energy and Work; Potential Energy and Conservation of Energy; Center of Mass – "
           "Linear Momentum and Collision. Konstanta: g = 9,8 m/s². Seluruh jawaban telah "
           "diverifikasi ulang (Lampiran A).", size=9, italic=True, color=ABU_MUDA,
      space_after=2)


def main():
    doc = kit.new_document(
        "Fisika Dasar I — 29 Soal dan Pembahasan (Setiap Rumus Dijabarkan)",
        "Usaha, energi kinetik, energi potensial, kekekalan energi, pusat massa, momentum, "
        "impuls, dan tumbukan",
        "Dosen Pengasuh Mata Kuliah Fisika Dasar I")

    header_footer(doc,
                  "Fisika Dasar I — 29 Soal & Pembahasan",
                  "BEK1EAB4 · Minggu 4–6",
                  "Setiap rumus dijabarkan · g = 9,8 m/s²")

    cover(doc)
    cara_baca(doc)
    daftar_soal(doc)
    for huruf, judul, awal, akhir, acuan, pengantar in BAGIAN:
        bagian(doc, huruf, judul, awal, akhir, acuan, pengantar)
    lampiran_a(doc)
    lampiran_b(doc)
    lampiran_c(doc)
    penutup(doc)

    normalize_order(doc)
    doc.save(OUT)
    print("Tersimpan:", OUT)
    print("Ukuran  :", round(OUT.stat().st_size / 1024, 1), "KB")
    print("Jumlah soal:", len(ITEMS))


if __name__ == "__main__":
    main()
