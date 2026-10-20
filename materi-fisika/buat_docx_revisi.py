#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Membangun dokumen Word (A4) REVISI:
"Fisika Dasar I — 34 Soal & Pembahasan, Setiap Rumus Dijabarkan"

Sumber: tiga berkas kuliah (Kinetic Energy and Work; Potential Energy and
Conservation of Energy; Center of Mass – Linear Momentum and Collision),
cheatsheet Fisika I, serta foto slide dan papan tulis pertemuan minggu 4–6.
"""
from pathlib import Path

from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

import docx_kit as kit
from docx_kit import (ABU, ABU_MUDA, BIRU, HIJAU, HITAM, MERAH, MERAH2, EMAS,
                      catatan, gambar, header_footer, jawaban, judul_bagian,
                      judul_item, label, langkah, normalize_order, p, poin,
                      rich, rumus, soal_teks, syarat, tabel_lambang,
                      banner_judul, blok_penutup_cover, set_table_pct,
                      table_borders, set_cell_margins, keep_row_together,
                      cell_shading)
from konten_a import ITEMS_A
from konten_b import ITEMS_B

BASE = Path(__file__).resolve().parent
IMG = BASE / "gambar"
OUT = BASE / "Fisika-Dasar-I-34-Soal-dan-Pembahasan.docx"

ITEMS = ITEMS_A + ITEMS_B

BAGIAN = [
    ("A", "MINGGU 4 — USAHA DAN ENERGI KINETIK", 1, 8,
     "Delapan soal pertama membahas usaha oleh gaya konstan, usaha oleh gaya yang "
     "berubah (integral dan luas grafik), teorema usaha–energi kinetik, dan daya. "
     "Semua soal pada bagian ini dapat diselesaikan dengan empat rumus inti: "
     "W = F d cos θ, W = ∫F dx, W = ΔK, dan P = W/Δt."),
    ("B", "MINGGU 5 — ENERGI POTENSIAL DAN KEKEKALAN ENERGI", 9, 16,
     "Delapan soal berikut menuntut satu kebiasaan baru: menetapkan titik acuan "
     "energi potensial lebih dahulu, lalu menuliskan **semua** bentuk energi "
     "potensial yang terlibat (gravitasi dan pegas). Jika ada gesekan, energi "
     "mekanik tidak kekal dan harus ditambahkan suku energi termal."),
    ("C", "MINGGU 6 — PUSAT MASSA, MOMENTUM, DAN IMPULS", 17, 24,
     "Bagian ini berpindah dari besaran skalar (energi) ke besaran vektor "
     "(posisi, kecepatan, momentum). Satu aturan yang harus dipegang: tetapkan "
     "arah positif, lalu tuliskan tanda + atau − pada setiap kecepatan."),
    ("D", "MINGGU 6 — KEKEKALAN MOMENTUM DAN TUMBUKAN", 25, 29,
     "Lima soal terakhir pada materi wajib. Ingat pembagian tugasnya: pada setiap "
     "tumbukan **momentum selalu kekal**, tetapi **energi kinetik hanya kekal bila "
     "tumbukannya elastis**. Kesalahan paling umum adalah memakai kekekalan energi "
     "kinetik pada tumbukan yang tidak elastis."),
    ("E", "SOAL TAMBAHAN DARI SLIDE DAN PAPAN TULIS KULIAH", 30, 34,
     "Lima soal ini diambil dari foto tayangan slide pertemuan minggu ke-4 sampai "
     "ke-6 (termasuk contoh yang ditulis di papan tulis). Sebagian besar hanya "
     "variasi dari soal-soal di depan, sehingga cocok dipakai sebagai latihan "
     "mandiri sebelum ujian."),
]

RINGKAS = [
    (1, "Usaha oleh gaya konstan", "W = F d cos θ", "W = +50 J"),
    (2, "Usaha total beberapa gaya", "W~net~ = ΣF~i~d cos θ~i~", "W~net~ = 153,4 J"),
    (3, "Gaya berubah (integral)", "W = ∫F~x~ dx", "W = 18 J; v = 4,24 m/s"),
    (4, "Gaya dua dimensi", "W = ∫F~x~dx + ∫F~y~dy", "W = +7 J; laju bertambah"),
    (5, "Luas grafik F–x", "W = luas kurva", "W = 20 J; v = 4,47 m/s"),
    (6, "Teorema usaha–energi", "W = ΔK", "W = +16 J"),
    (7, "Jarak pengereman", "d ∝ v²", "d = 72 m"),
    (8, "Daya", "P = W/Δt ; P = Fv", "P = 60 W"),
    (9, "Energi potensial gravitasi", "ΔU = mgΔy", "ΔU = +58,8 J; W~g~ = −58,8 J"),
    (10, "Jatuh bebas", "K~i~+U~i~ = K~f~+U~f~", "v = 15,34 m/s"),
    (11, "Roller-coaster", "½mv² + mgy = tetap", "v = 28 m/s; y = 30 m"),
    (12, "Energi pegas → gerak", "½kx² = ½mv²", "v = 3,16 m/s"),
    (13, "Gaya Hooke & usaha pegas", "F = −kx ; W = ½k(x~i~²−x~f~²)", "F = −20 N; W = +0,84 J"),
    (14, "Bola menekan pegas", "mg(h+x) = ½kx²", "k = 1,59 × 10³ N/m"),
    (15, "Gesekan & energi termal", "f~k~ = μ~k~N ; ΔE~th~ = f~k~d", "W~f~ = −29,4 J; v = 2,66 m/s"),
    (16, "Gaya nonkonservatif", "ΔE~mech~ = W~nc~", "W~nc~ = −30 J"),
    (17, "Pusat massa 1D", "x~CM~ = Σm~i~x~i~/M", "x~CM~ = 2,4 m"),
    (18, "Pusat massa 2D", "x~CM~, y~CM~", "r~CM~ = (1, 1) m"),
    (19, "Pusat massa batang", "(1/M)∫x dm", "x~CM~ = 2 m"),
    (20, "Hukum II Newton sistem", "F~ext~ = M a~CM~", "a~CM~ = 3 m/s²"),
    (21, "Momentum & v~CM~", "P = Mv~CM~", "P = +2 kg·m/s; v~CM~ = 0,67 m/s"),
    (22, "Impuls bola memantul", "J = Δp ; F = J/Δt", "J = −4,5 N·s; F = −300 N"),
    (23, "Impuls gaya konstan", "J = FΔt", "J = 10 N·s; v = 20 m/s"),
    (24, "Impuls grafik F–t", "J = ∫F dt", "J = 5 N·s; v = 20 m/s"),
    (25, "Elastis vs tidak elastis", "ΔK = K~f~ − K~i~", "Tidak elastis; 8 J hilang"),
    (26, "Menyatu (satu arah)", "v = (m₁v₁+m₂v₂)/(m₁+m₂)", "v = 2 m/s; ΔK = −12 J"),
    (27, "Menyatu (berlawanan)", "P~i~ = P~f~", "v = −0,5 m/s; ΔK = −13,5 J"),
    (28, "Elastis, massa sama", "tukar kecepatan", "v₁ = 0; v₂ = +4 m/s"),
    (29, "Elastis, massa beda", "rumus v₁~f~, v₂~f~", "v₁ = −1 m/s; v₂ = +4 m/s"),
    (30, "Dua seluncuran air", "v = √(2gh)", "Laju sama; Corinne lebih dulu"),
    (31, "Seluncuran air h = 8,5 m", "v = √(2gh)", "v = 12,9 m/s"),
    (32, "Keju di lift", "F~N~ = m(g+a)", "W = 2,6 × 10⁴ J; F~N~ = 2,45 N"),
    (33, "Grafik a–x", "W = m × luas", "42, 30, 12 J; v = 6,5; 5,5; 3,5 m/s"),
    (34, "Grafik F–x", "W = luas trapesium", "2.800 J; 2.100 J"),
]


# ------------------------------------------------------------------ halaman
def cover(doc):
    banner_judul(
        doc,
        "FISIKA DASAR I  ·  BEK1EAB4",
        "34 SOAL & PEMBAHASAN",
        "Usaha · Energi Kinetik · Energi Potensial · Kekekalan Energi\n"
        "Pusat Massa · Momentum Linear · Impuls · Tumbukan",
        [
            ("Sumber", "Tiga berkas kuliah minggu ke-4 s.d. ke-6 (Kinetic Energy and "
                       "Work; Potential Energy and Conservation of Energy; Center of "
                       "Mass – Linear Momentum and Collision), cheatsheet Fisika I, "
                       "serta foto slide dan papan tulis"),
            ("Cakupan", "34 soal: 29 soal per rumus + 5 soal dari slide kuliah"),
            ("Ciri dokumen", "Setiap soal ditulis kembali, langsung dikerjakan, dan "
                             "setiap rumus dijabarkan lambang per lambang beserta satuannya"),
            ("Tingkat", "Minggu 4–6, Fisika Dasar I, satuan SI, g = 9,8 m/s²"),
        ])
    blok_penutup_cover(doc)


def cara_baca(doc):
    judul_bagian(doc, "CARA MEMBACA DOKUMEN INI", page_break=True)
    p(doc, "Dokumen ini disusun dengan pola yang **sama untuk setiap soal**, supaya dapat "
           "dipakai sebagai bank soal sekaligus rujukan rumus. Urutannya:", space_after=5)
    langkah(doc, [
        "**Rumus inti** — rumus yang menjadi kunci soal; ditulis di bawah judul setiap soal.",
        "**Tabel keterangan lambang** — setiap lambang dijelaskan artinya dan satuannya. "
        "Tabel ini menggantikan catatan “dengan F = gaya, d = perpindahan, …” yang biasanya "
        "ditulis berdesakan; tujuannya agar tidak ada lambang yang tertinggal tanpa penjelasan.",
        "**Syarat pemakaian** — kapan rumus itu boleh dipakai dan kapan tidak. Bagian ini "
        "sering luput dibaca, padahal justru di sinilah letak kesalahan ujian.",
        "**Soal** — ditulis kembali secara lengkap, dalam bahasa Indonesia.",
        "**Penyelesaian** — dikerjakan bertahap: rumus → substitusi angka → hasil, dengan "
        "pemeriksaan satuan dan tanda.",
        "**Jawaban** — hasil akhir dalam kotak hijau.",
        "**Catatan** — kesalahan yang sering terjadi dan hubungan dengan soal lain.",
    ])
    p(doc, "", space_after=2)
    label(doc, "Kesepakatan notasi dan satuan", space_before=8)
    poin(doc, [
        "Satuan yang dipakai adalah satuan SI. g = 9,8 m/s² (kadang dibulatkan 10 m/s² untuk "
        "perhitungan kasar).",
        "**Joule (J)** = N·m = kg·m²/s² untuk usaha dan energi; **watt (W)** = J/s untuk daya; "
        "**N·s** = kg·m/s untuk momentum dan impuls.",
        "Arah positif ditetapkan lebih dahulu (biasanya ke kanan dan ke atas). Kecepatan yang "
        "berlawanan arah ditulis dengan tanda minus.",
        "Besaran yang bertanda tebal atau ditulis dengan huruf kapital adalah vektor; "
        "contoh: **F**, **v**, **p**.",
        "Massa tidak pernah negatif, dan energi kinetik K = ½mv² selalu ≥ 0 walaupun v "
        "bertanda minus.",
        "Angka ditulis dengan koma desimal sesuai kebiasaan Indonesia (2,5 bukan 2.5), dan "
        "ribuan dipisah dengan titik (2.800 J).",
    ])
    p(doc, "", space_after=2)
    label(doc, "Berkas sumber dan pembagiannya", space_before=8)
    poin(doc, [
        "*Kinetic Energy and Work* (minggu 4) → Soal 1–8 dan 32–34.",
        "*Potential Energy and Conservation of Energy* (minggu 5) → Soal 9–16 dan 30–31.",
        "*Center of Mass – Linear Momentum and Collision* (minggu 6) → Soal 17–29.",
        "*Cheatsheet Fisika I* → menjadi kerangka 29 poin rumus yang dipakai pada Soal 1–29.",
        "Foto slide dan papan tulis kuliah → Soal 30–34.",
    ])
    p(doc, "Soal-soal lain yang ada di dalam tiga berkas kuliah (seluruhnya 58 soal) tetap dapat "
           "dibaca pada dokumen pendamping *Ringkasan Fisika Dasar I*, sedangkan dokumen ini "
           "memuat satu soal untuk **setiap rumus** dengan penjabaran lambang yang lengkap.",
      size=9.6, italic=True, color=ABU, space_after=4)


def daftar_soal(doc):
    judul_bagian(doc, "DAFTAR SOAL DAN JAWABAN SINGKAT", page_break=True,
                 sub="Gunakan daftar ini untuk memilih soal yang ingin dilatih; "
                     "jawaban singkat di kolom terakhir berguna untuk memeriksa hasil sendiri.")
    table = doc.add_table(rows=0, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = doc.styles["Table Grid"]
    set_table_pct(table)
    table_borders(table, color="CFC6B5", sz=4)
    set_cell_margins(table, top=28, bottom=28, left=70, right=70)
    widths = (Cm(1.1), Cm(5.4), Cm(5.2), Cm(4.4))

    head = table.add_row()
    keep_row_together(head)
    for j, txt in enumerate(("No", "Pokok bahasan", "Rumus inti", "Jawaban singkat")):
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
    gap.paragraph_format.space_before = Pt(0)
    gap.paragraph_format.space_after = Pt(2)


def render_item(doc, it):
    judul_item(doc, it["no"], it["judul"], it["rumus_inti"], it["sumber"])
    label(doc, "Rumus dan keterangan lambangnya", space_before=4, space_after=3)
    for line in it["rumus"]:
        rumus(doc, line[0], line[1] if len(line) > 1 else None)
    tabel_lambang(doc, it["lambang"])
    if it.get("syarat"):
        syarat(doc, it["syarat"])
    soal_teks(doc, it["soal"])
    if it.get("gambar"):
        nama, lebar, caption = it["gambar"]
        gambar(doc, IMG / nama, lebar, caption)
    label(doc, "Penyelesaian", color=HITAM, space_before=6)
    for blok in it["isi"]:
        jenis = blok[0]
        if jenis == "p":
            p(doc, blok[1], space_after=3)
        elif jenis == "f":
            rumus(doc, blok[1], blok[2] if len(blok) > 2 else None)
        elif jenis == "l":
            langkah(doc, blok[1])
        elif jenis == "b":
            poin(doc, blok[1])
    if it.get("jawaban"):
        jawaban(doc, it["jawaban"])
    if it.get("catatan"):
        catatan(doc, it["catatan"])


def bagian(doc, huruf, judul, awal, akhir, pengantar):
    judul_bagian(doc, f"BAGIAN {huruf}  ·  {judul}", page_break=True,
                 sub=f"Soal {awal} sampai {akhir} ({akhir - awal + 1} soal)")
    p(doc, pengantar, space_after=6)
    for it in ITEMS:
        if awal <= it["no"] <= akhir:
            render_item(doc, it)


# ------------------------------------------------------------------ lampiran
PETA = [
    ("4.1", "Energi kinetik: K = ½mv²", "5, 6, 25", "K selalu ≥ 0; skalar"),
    ("4.2", "Usaha gaya konstan: W = Fd cos θ; teorema usaha–energi", "1, 2, 6, 7", "hanya gaya sejajar perpindahan"),
    ("4.3", "Usaha gaya gravitasi: W = mgd cos φ", "9, 10, 31", "naik → W negatif"),
    ("4.4", "Usaha gaya pegas: W = ½k(x~i~² − x~f~²)", "12, 13, 14", "x diukur dari posisi relaks"),
    ("4.5", "Usaha gaya berubah: W = ∫F dx = luas kurva", "3, 4, 5, 33, 34", "grafik a–x harus dikali m"),
    ("4.6", "Daya: P = W/Δt ; P = Fv", "8", "1 hp = 746 W"),
    ("5.1", "Energi potensial: ΔU = −W~konservatif~", "9, 13, 14", "acuan bebas dipilih"),
    ("5.2", "Kekekalan energi mekanik", "10, 11, 12, 14, 30, 31", "tanpa gesekan"),
    ("5.3", "Kurva energi potensial: F = −dU/dx", "14, 15", "gaya = kemiringan negatif"),
    ("5.4", "Usaha gaya luar & gesekan: ΔE~th~ = f~k~d", "15, 16", "gesekan selalu mengurangi E"),
    ("6.1", "Pusat massa: r~CM~ = Σm~i~r~i~/M", "17, 18, 19", "boleh di luar benda"),
    ("6.2", "Hukum II Newton sistem: F~ext~ = Ma~CM~", "20", "hanya gaya luar"),
    ("6.3", "Momentum: p = mv ; P = Mv~CM~", "21", "besaran vektor"),
    ("6.4", "Impuls: J = ∫F dt = Δp", "22, 23, 24", "luas grafik F–t"),
    ("6.5", "Kekekalan momentum", "26, 27, 30", "syarat: gaya luar ≈ 0"),
    ("6.6", "Momentum & energi pada tumbukan", "25, 26, 27", "K kekal hanya bila elastis"),
    ("6.7", "Tumbukan elastis 1D", "28, 29", "dua persamaan: p dan K"),
    ("6.8", "Tumbukan dua dimensi", "29 (prinsip)", "uraikan per sumbu"),
]


def lampiran(doc):
    judul_bagian(doc, "LAMPIRAN 1 — PETA RUMUS TERHADAP SUBBAB KULIAH", page_break=True,
                 sub="Tabel ini memudahkan mencari soal yang sesuai dengan subbab yang "
                     "sedang dibahas di kelas.")
    table = doc.add_table(rows=0, cols=4)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = doc.styles["Table Grid"]
    set_table_pct(table)
    table_borders(table, color="CFC6B5", sz=4)
    set_cell_margins(table, top=26, bottom=26, left=70, right=70)
    widths = (Cm(1.3), Cm(8.2), Cm(3.5), Cm(3.1))
    head = table.add_row()
    keep_row_together(head)
    for j, txt in enumerate(("Subbab", "Rumus / pokok bahasan", "Soal di sini", "Kunci ingat")):
        cell = head.cells[j]
        cell.width = widths[j]
        cell_shading(cell, "7A1F1F")
        cell.text = ""
        par = cell.paragraphs[0]
        par.paragraph_format.space_before = Pt(1)
        par.paragraph_format.space_after = Pt(1)
        par.paragraph_format.line_spacing = 0.95
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER if j != 1 else WD_ALIGN_PARAGRAPH.LEFT
        r = par.add_run(txt)
        r.font.size = Pt(8.2)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    for i, baris in enumerate(PETA):
        row = table.add_row()
        keep_row_together(row)
        for j, txt in enumerate(baris):
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
            rich(par, txt, size=8.1)
            if j == 0:
                for r in par.runs:
                    r.bold = True
                    r.font.color.rgb = MERAH2
            if j == 2:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in par.runs:
                    r.bold = True
    gap = doc.add_paragraph()
    gap.paragraph_format.space_after = Pt(3)
    p(doc, "Catatan: nomor subbab mengikuti penomoran slide kuliah (4.1–4.6, 5.1–5.5, "
           "6.1–6.8). Nomor soal mengacu pada dokumen ini, bukan pada buku teks.",
      size=8.6, italic=True, color=ABU_MUDA, space_after=6)


def lampiran2(doc):
    judul_bagian(doc, "LAMPIRAN 2 — DUA BELAS KESALAHAN YANG PALING SERING TERJADI",
                 page_break=True,
                 sub="Diperiksa kembali sebelum ujian: hampir semua kehilangan nilai pada "
                     "bab ini berasal dari daftar berikut.")
    butir = [
        ("Memakai W = F d cos θ untuk gaya yang berubah",
         "Pegas dan gaya yang bergantung pada posisi memerlukan ½k(x~i~² − x~f~²) atau "
         "∫F dx. Lihat Soal 3, 5, 13, 34."),
        ("Lupa bahwa usaha total adalah jumlah **aljabar**",
         "Gaya yang berlawanan arah gerak memberi usaha negatif. Lihat Soal 2, 33, 34."),
        ("Menganggap luas grafik a–x langsung sama dengan usaha",
         "Luas a–x bersatuan m²/s², harus dikalikan massa. Lihat Soal 33."),
        ("Salah tanda usaha gravitasi",
         "Naik → ΔU positif dan W~g~ negatif; turun → sebaliknya. Lihat Soal 9, 14."),
        ("Menghilangkan suku mg(h + x) pada soal pegas",
         "Bola masih berada di bawah titik sentuh saat pegas termampat maksimum. "
         "Lihat Soal 14."),
        ("Memakai kekekalan energi mekanik padahal ada gesekan",
         "Tambahkan ΔE~th~ = f~k~d, atau gunakan ΔE~mech~ = W~nc~. Lihat Soal 15, 16."),
        ("Menganggap N selalu sama dengan mg",
         "Pada bidang miring N = mg cos α; pada lift N = m(g + a). Lihat Soal 15, 32."),
        ("Menganggap energi kinetik kekal pada semua tumbukan",
         "K hanya kekal bila elastis. Lihat Soal 25, 26, 27."),
        ("Menjumlahkan besar momentum tanpa memperhatikan arah",
         "Momentum vektor: pakai tanda, atau uraikan per sumbu. Lihat Soal 21, 27."),
        ("Lupa bahwa kecepatan berbalik tanda saat benda memantul",
         "Δv pada pemantulan = v~f~ − v~i~ dengan tanda berlawanan. Lihat Soal 22."),
        ("Tidak mengubah satuan ke SI",
         "cm → m, km/jam → m/s (bagi 3,6), gram → kg, ms → s. Lihat Soal 7, 12, 14."),
        ("Tidak memeriksa kewajaran hasil",
         "Laju 300 m/s untuk benda jatuh 2 m, atau massa negatif, pasti salah. "
         "Biasakan memeriksa satuan, tanda, dan orde besaran."),
    ]
    for i, (salah, benar) in enumerate(butir, 1):
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(0.85)
        pf.first_line_indent = Cm(-0.85)
        pf.space_before = Pt(3)
        pf.space_after = Pt(1)
        pf.line_spacing = 1.08
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
    p(doc, "Seluruh 34 soal dalam dokumen ini disusun dengan satu prinsip: **rumus tidak "
           "dihafalkan terpisah dari artinya**. Karena itu setiap rumus selalu disertai tabel "
           "lambang (apa artinya, apa satuannya), syarat pemakaian, contoh penerapan, dan "
           "kesalahan yang biasa terjadi. Jika ketiga hal itu melekat pada satu rumus, soal "
           "yang tampak baru akan tetap dapat dikerjakan.", space_after=6)
    p(doc, "Dua kebiasaan yang paling menentukan hasil ujian:", space_after=3)
    langkah(doc, [
        "**Menulis besaran yang diketahui beserta satuannya lebih dahulu**, lalu mengubahnya "
        "ke SI. Sebagian besar kesalahan hitung berhenti di langkah ini.",
        "**Memeriksa hasil**: satuannya benar? tandanya masuk akal? besarnya wajar? "
        "Pemeriksaan ini memerlukan 10 detik tetapi menyelamatkan banyak nilai.",
    ])
    p(doc, "", space_after=4)
    p(doc, "Sebagai latihan mandiri, tutup bagian **Penyelesaian** dan kerjakan kembali soal "
           "dengan hanya membaca bagian **Soal** dan **Rumus inti**. Setelah selesai, bandingkan "
           "langkah Anda dengan pembahasan — bukan hanya jawaban akhirnya. Fisika dikuasai "
           "melalui pemeriksaan kesalahan sendiri, bukan dengan membaca pembahasan berulang kali.",
      space_after=8)
    p(doc, "Dokumen ini disusun dari tiga berkas kuliah Fisika Dasar I (Kinetic Energy and "
           "Work; Potential Energy and Conservation of Energy; Center of Mass – Linear "
           "Momentum and Collision), cheatsheet Fisika I, serta foto slide dan papan tulis "
           "pertemuan minggu ke-4 sampai ke-6. Konstanta yang dipakai: g = 9,8 m/s².",
      size=9, italic=True, color=ABU_MUDA, space_after=2)


def main():
    doc = kit.new_document(
        "Fisika Dasar I — 34 Soal dan Pembahasan (Setiap Rumus Dijabarkan)",
        "Usaha, energi kinetik, energi potensial, kekekalan energi, pusat massa, "
        "momentum, impuls, dan tumbukan",
        "Dosen Pengasuh Mata Kuliah Fisika Dasar I")

    header_footer(doc,
                  "Fisika Dasar I — 34 Soal & Pembahasan",
                  "BEK1EAB4 · Minggu 4–6",
                  "Setiap rumus dijabarkan; g = 9,8 m/s²")

    cover(doc)
    cara_baca(doc)
    daftar_soal(doc)
    for huruf, judul, awal, akhir, pengantar in BAGIAN:
        bagian(doc, huruf, judul, awal, akhir, pengantar)
    lampiran(doc)
    lampiran2(doc)
    penutup(doc)

    normalize_order(doc)
    doc.save(OUT)
    print("Tersimpan:", OUT)
    print("Ukuran :", round(OUT.stat().st_size / 1024, 1), "KB")
    print("Jumlah soal:", len(ITEMS))


if __name__ == "__main__":
    main()
