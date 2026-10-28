"""Membangun panduan pengerjaan Studi Kasus 4 (untuk mahasiswa).

Jalankan:  python3 build_panduan.py
Keluaran:  ../output/Panduan-Mengerjakan-Case-4.docx
"""
import os

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output", "Panduan-Mengerjakan-Case-4.docx")

NAVY = RGBColor(0x1F, 0x38, 0x64)
BLUE = RGBColor(0x2E, 0x54, 0x96)
DARK = RGBColor(0x1A, 0x1A, 0x1A)
GREY = RGBColor(0x59, 0x59, 0x59)
RED = RGBColor(0xA6, 0x2B, 0x2B)
GREEN = RGBColor(0x1E, 0x6B, 0x45)
FONT = "Times New Roman"

doc = Document()

# ---------- halaman & gaya dasar ----------
sec = doc.sections[0]
sec.page_width = Cm(21.0)
sec.page_height = Cm(29.7)
for m in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
    setattr(sec, m, Cm(2.2))

st = doc.styles["Normal"]
st.font.name = FONT
st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.18


def _shade(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def _fix_layout(tbl):
    """Kunci lebar kolom agar Word tidak menyesuaikan sendiri."""
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn("w:tblLayout")):
        tblPr.remove(old)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)


def _borderless(tbl):
    tblPr = tbl._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "none")
        el.set(qn("w:sz"), "0")
        borders.append(el)
    tblPr.append(borders)


def h1(text, num=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(20)
    pf.space_after = Pt(6)
    pf.keep_with_next = True
    run = p.add_run((f"{num}. " if num else "") + text)
    run.font.name = FONT
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = NAVY
    # garis bawah tipis
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "3")
    bottom.set(qn("w:color"), "1F3864")
    pBdr.append(bottom)
    pPr.append(pBdr)
    return p


def h2(text):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(13)
    pf.space_after = Pt(4)
    pf.keep_with_next = True
    run = p.add_run(text)
    run.font.name = FONT
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = BLUE
    return p


def h3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = FONT
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = DARK
    return p


def p(text, bold_lead=None, size=11, color=None, italic=False, space_after=6,
      align=WD_ALIGN_PARAGRAPH.JUSTIFY, indent=None):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_after = Pt(space_after)
    pf.alignment = align
    if indent:
        pf.left_indent = Cm(indent)
    if bold_lead:
        r0 = par.add_run(bold_lead)
        r0.font.name = FONT
        r0.font.size = Pt(size)
        r0.font.bold = True
        r0.font.color.rgb = color or DARK
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.italic = italic
    r.font.color.rgb = color or DARK
    return par


def bullet(text, lead=None, size=11):
    par = doc.add_paragraph(style="List Bullet")
    pf = par.paragraph_format
    pf.space_after = Pt(3)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.left_indent = Cm(0.75)
    pf.first_line_indent = Cm(-0.4)
    if lead:
        r0 = par.add_run(lead)
        r0.font.name = FONT
        r0.font.size = Pt(size)
        r0.font.bold = True
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    return par


def num(text, lead=None, size=11):
    par = doc.add_paragraph(style="List Number")
    pf = par.paragraph_format
    pf.space_after = Pt(3)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.left_indent = Cm(0.85)
    pf.first_line_indent = Cm(-0.5)
    if lead:
        r0 = par.add_run(lead)
        r0.font.name = FONT
        r0.font.size = Pt(size)
        r0.font.bold = True
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    return par


def formula(text):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_before = Pt(4)
    pf.space_after = Pt(6)
    pf.left_indent = Cm(0.6)
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = par.add_run(text)
    r.font.name = "Consolas"
    r.font.size = Pt(10)
    r.font.color.rgb = NAVY
    return par


def box(title, body, fill="EEF3FA", accent=NAVY):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    _shade(cell, fill)
    cell.width = Cm(16.4)
    par = cell.paragraphs[0]
    par.paragraph_format.space_after = Pt(3)
    if title:
        r = par.add_run(title)
        r.font.name = FONT
        r.font.size = Pt(10.5)
        r.font.bold = True
        r.font.color.rgb = accent
        par2 = cell.add_paragraph()
        par2.paragraph_format.space_after = Pt(2)
        par2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r2 = par2.add_run(body)
        r2.font.name = FONT
        r2.font.size = Pt(10.5)
    else:
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        r = par.add_run(body)
        r.font.name = FONT
        r.font.size = Pt(10.5)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return tbl


def table(headers, rows, widths=None, font_size=9.5, header_fill="1F3864",
          align_center_cols=None, caption=None, note=None):
    if caption:
        cp = doc.add_paragraph()
        cp.paragraph_format.space_before = Pt(8)
        cp.paragraph_format.space_after = Pt(3)
        cp.paragraph_format.keep_with_next = True
        r = cp.add_run(caption)
        r.font.name = FONT
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = NAVY

    tbl = doc.add_table(rows=1, cols=len(headers))
    tbl.style = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False

    hdr = tbl.rows[0]
    for i, htxt in enumerate(headers):
        cell = hdr.cells[i]
        _shade(cell, header_fill)
        cell.paragraphs[0].paragraph_format.space_after = Pt(2)
        cell.paragraphs[0].paragraph_format.space_before = Pt(2)
        r = cell.paragraphs[0].add_run(htxt)
        r.font.name = FONT
        r.font.size = Pt(font_size)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for row in rows:
        cells = tbl.add_row().cells
        for i, val in enumerate(row):
            par = cells[i].paragraphs[0]
            par.paragraph_format.space_after = Pt(2)
            par.paragraph_format.space_before = Pt(2)
            if align_center_cols and i in align_center_cols:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = par.add_run(str(val))
            r.font.name = FONT
            r.font.size = Pt(font_size)

    if widths:
        for row in tbl.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
        _fix_layout(tbl)

    if note:
        np_ = doc.add_paragraph()
        np_.paragraph_format.space_before = Pt(2)
        np_.paragraph_format.space_after = Pt(8)
        r = np_.add_run(note)
        r.font.name = FONT
        r.font.size = Pt(8.5)
        r.font.italic = True
        r.font.color.rgb = GREY
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return tbl


def callout(kind, title, body):
    palette = {
        "tip": ("E9F5EE", GREEN, "TIPS"),
        "warn": ("FBEEEE", RED, "HATI-HATI"),
        "note": ("EEF3FA", NAVY, "CATATAN"),
        "step": ("F3F1FA", RGBColor(0x4B, 0x3B, 0x8F), "LANGKAH"),
    }
    fill, accent, label = palette[kind]
    box(f"{label} — {title}", body, fill=fill, accent=accent)


# ============================================================ SAMPUL
for _ in range(3):
    doc.add_paragraph()

p1 = doc.add_paragraph()
p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p1.add_run("PANDUAN LENGKAP")
r.font.name = FONT
r.font.size = Pt(13)
r.font.bold = True
r.font.color.rgb = GREY

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p2.add_run("MENGERJAKAN STUDI KASUS 4")
r.font.name = FONT
r.font.size = Pt(26)
r.font.bold = True
r.font.color.rgb = NAVY

p3 = doc.add_paragraph()
p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
p3.paragraph_format.space_after = Pt(18)
r = p3.add_run("Dari membaca kasus sampai laporan siap dikumpulkan")
r.font.name = FONT
r.font.size = Pt(14)
r.font.italic = True
r.font.color.rgb = BLUE

box("Untuk siapa panduan ini?",
    "Panduan ini ditulis untuk mahasiswa yang baru pertama kali mengerjakan studi kasus "
    "operasional dan belum tahu harus mulai dari mana. Isinya bukan laporan jadi, melainkan "
    "urutan langkah yang bisa Anda ikuti sendiri: apa yang harus dibaca, angka apa yang harus "
    "dihitung, tabel apa yang harus dibuat, dan kalimat seperti apa yang harus ditulis. "
    "Setiap langkah disertai contoh angka yang benar-benar diambil dari kasus ini.",
    fill="F0F4FA")

doc.add_paragraph()
p4 = doc.add_paragraph()
p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p4.add_run("Kasus: “Armada Banyak, Pengiriman Tetap Terlambat”\n"
               "Bidang Supply Chain & Distribution — Manajemen Industri")
r.font.name = FONT
r.font.size = Pt(11)
r.font.color.rgb = GREY

doc.add_paragraph()
p5 = doc.add_paragraph()
p5.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p5.add_run("Waktu pengerjaan yang disarankan: 5 hari kerja")
r.font.name = FONT
r.font.size = Pt(10.5)
r.font.bold = True
r.font.color.rgb = NAVY

doc.add_page_break()

# ============================================================ 1
h1("Cara memakai panduan ini", 1)

p("Sebelum masuk ke langkah pertama, pahami dulu bentuk panduannya. Setiap bagian punya pola "
  "yang sama: tujuan langkah, apa yang harus Anda lakukan, contoh dari kasus ini, dan hasil "
  "yang seharusnya Anda peroleh. Kalau Anda mengikuti urutannya, di akhir Anda akan punya "
  "draf lengkap yang tinggal dirapikan.")

p("Ada satu prinsip yang perlu dipegang sejak awal: dosen tidak menilai panjang laporan, tetapi "
  "menilai apakah cara berpikir Anda terlihat. Laporan yang tipis tetapi setiap angkanya bisa "
  "dijelaskan asalnya akan mendapat nilai lebih tinggi daripada laporan tebal yang penuh "
  "pernyataan tanpa dasar. Karena itu panduan ini menekankan tiga hal: dari mana angka berasal, "
  "mengapa sebuah pilihan diambil, dan apa risikonya kalau pilihan itu salah.", italic=False)

table(
    ["Tahap", "Yang Anda kerjakan", "Perkiraan waktu", "Hasil antara"],
    [
        ["1", "Membaca kasus tiga kali dengan tiga tujuan berbeda", "45 menit", "Daftar fakta dan daftar pertanyaan"],
        ["2", "Menghitung kondisi awal (baseline)", "1 jam", "Tabel angka dasar"],
        ["3", "Menghitung biaya akibat masalah", "1,5 jam", "Tabel biaya masalah"],
        ["4", "Mencari akar penyebab", "1,5 jam", "Diagram sebab-akibat dan lima mengapa"],
        ["5", "Menyusun alternatif solusi", "1 jam", "Empat alternatif tertulis"],
        ["6", "Menetapkan kriteria dan bobot", "45 menit", "Tabel kriteria"],
        ["7", "Menghitung kelayakan uang", "2 jam", "Tabel NPV dan payback"],
        ["8", "Menilai dan memilih", "1 jam", "Matriks skor dan justifikasi"],
        ["9", "Menyusun rencana 90 hari, risiko, KPI", "2 jam", "Tabel fase, risiko, KPI"],
        ["10", "Menulis dan memformat", "3 jam", "Draf lengkap"],
        ["11", "Memeriksa dengan daftar centang", "1 jam", "Laporan siap kumpul"],
    ],
    widths=[1.2, 7.6, 3.0, 4.6],
    caption="Tabel 1. Peta pekerjaan dan perkiraan waktu",
    align_center_cols=[0, 2],
    note="Total sekitar 15 jam kerja efektif. Bila dipecah lima hari, cukup tiga jam per hari."
)

callout("tip", "jangan menulis dulu",
        "Kesalahan paling umum mahasiswa baru adalah mulai menulis kalimat pembuka di hari pertama. "
        "Akibatnya tulisan berputar-putar karena angkanya belum ada. Selesaikan dulu langkah 2 sampai 9, "
        "baru menulis. Menulis setelah angka lengkap jauh lebih cepat karena Anda hanya menjelaskan "
        "apa yang sudah Anda temukan.")

# ============================================================ 2
h1("Pahami dulu apa yang sebenarnya diminta", 2)

p("Sebelum menyentuh Word atau kalkulator, baca ulang lembar tugas. Ada tiga lapis tuntutan yang "
  "sering tertukar: isi wajib, sistematika, dan format. Ketiganya dinilai terpisah.")

h2("2.1 Tujuh isi wajib")
p("Lembar tugas menyebut tujuh hal yang harus ada. Anggap ini sebagai daftar periksa isi, bukan "
  "sekadar saran.")

table(
    ["No", "Isi wajib", "Bentuk nyata di laporan Anda", "Ada di bab"],
    [
        ["1", "Masalah utama dan akar penyebab", "Satu paragraf rumusan masalah + diagram sebab-akibat + lima mengapa", "III"],
        ["2", "Analisis data kuantitatif dan biaya akibat masalah", "Tabel perhitungan baseline + tabel biaya masalah", "II, III"],
        ["3", "Perbandingan minimal tiga alternatif", "Empat alternatif + tabel NPV + matriks skor", "IV"],
        ["4", "Rekomendasi berbasis data dengan asumsi eksplisit", "Subbab pemilihan + tabel asumsi berkode", "IV, Lampiran"],
        ["5", "Risiko operasional, teknologi, sosial, keamanan data", "Register risiko dengan skor", "V"],
        ["6", "KPI", "Tabel KPI: baseline, target 90 hari, target 12 bulan", "V"],
        ["7", "Rencana implementasi 90 hari", "Tabel fase + gate + diagram jadwal", "V"],
    ],
    widths=[1.0, 4.6, 7.6, 2.4],
    caption="Tabel 2. Tujuh isi wajib dan wujudnya",
    align_center_cols=[0, 3]
)

h2("2.2 Sistematika yang harus diikuti")
p("Sistematika bukan hiasan; dosen sering memeriksa keberadaannya secara harfiah. Susunannya: "
  "Halaman Sampul, Ringkasan, BAB I sampai BAB VI, Daftar Pustaka, lalu Lampiran. Subbabnya sudah "
  "ditentukan: 1.1 sampai 1.5, 2.1 sampai 2.4, 3.1 sampai 3.4, 4.1 sampai 4.4, 5.1 sampai 5.5, "
  "dan 6.1 sampai 6.2. Jangan menambah subbab baru dengan nomor sendiri, dan jangan menghilangkan "
  "satu pun. Kalau Anda punya ide tambahan, taruh di dalam subbab yang sudah ada atau pindahkan ke "
  "Lampiran.")

h2("2.3 Format yang dinilai")
table(
    ["Ketentuan", "Cara memenuhinya di Word", "Cara memeriksanya"],
    [
        ["Kertas A4", "Layout > Size > A4", "Penggaris atas menunjukkan 21 cm"],
        ["Times New Roman 12 pt", "Ctrl+A lalu ubah font dan ukuran", "Klik satu paragraf, lihat kotak font"],
        ["Spasi 1,5", "Ctrl+A > Paragraph > Line spacing 1,5", "Baris terlihat renggang, bukan rapat"],
        ["Margin 2,54 cm", "Layout > Margins > Normal", "Semua sisi sama lebar"],
        ["Rata kiri-kanan (justify)", "Ctrl+A lalu Ctrl+J", "Tepi kanan rata, tanpa bergerigi"],
        ["5–8 halaman isi", "Hitung dari BAB I sampai BAB VI", "Jangan menghitung sampul dan lampiran"],
        ["Tabel dan gambar bernomor + berjudul", "Tulis “Tabel 2.1 Judul” di atas tabel", "Nomor urut tidak melompat"],
    ],
    widths=[4.2, 6.6, 5.6],
    caption="Tabel 3. Ketentuan format dan cara memeriksanya",
    font_size=9.5
)

callout("warn", "soal batas halaman",
        "Batas 5–8 halaman itu di luar sampul dan lampiran. Cara aman: tulis isi sekitar 7 halaman, "
        "lalu taruh tabel-tabel besar (rincian biaya, register risiko lengkap, jadwal) di Lampiran. "
        "Dengan begitu isi tetap padat tetapi tidak melanggar batas.")

# ============================================================ 3
h1("Langkah 1 — Baca kasus tiga kali dengan tiga tujuan", 3)

p("Membaca sekali lalu langsung menulis adalah penyebab utama laporan yang dangkal. Bacalah tiga "
  "kali, dan setiap kali dengan tujuan yang berbeda. Ini bukan pemborosan; tiga pembacaan dengan "
  "tujuan berbeda menghasilkan pemahaman yang jauh lebih baik daripada sepuluh pembacaan tanpa tujuan.")

h3("Pembacaan pertama — cari angka")
p("Ambil pena. Setiap kali melihat angka, lingkari. Anda tidak perlu memahami artinya dulu. Yang "
  "Anda cari: jumlah, satuan, tarif, target, dan batas. Pada kasus ini Anda akan menemukan: 20 "
  "kendaraan, 150 km per kendaraan per hari, 26 hari per bulan, 1 liter per 10 km, harga bahan bakar "
  "Rp10.000 per liter, target pengurangan jarak 15%, dan batas investasi Rp150 juta.")

h3("Pembacaan kedua — cari keluhan")
p("Sekarang cari kalimat yang berisi masalah, keberatan, atau kejanggalan. Tandai dengan warna lain. "
  "Pada kasus ini ada empat: rute disusun manual oleh dispatcher, kendaraan melewati jalan yang sama, "
  "keterlambatan diketahui setelah pengemudi menelepon, dan pelanggan mengubah jadwal sehingga "
  "pengemudi menunggu. Perhatikan juga dua keberatan: pengemudi merasa aplikasi tidak paham kondisi "
  "lokal, dan bagian keuangan meragukan penghematan bahan bakar cukup menutup biaya sistem.")

h3("Pembacaan ketiga — cari keputusan")
p("Pembacaan terakhir mencari apa yang sebenarnya harus Anda putuskan. Di kasus ini: apakah perusahaan "
  "perlu membeli aplikasi optimasi rute dan pelacakan, dan kalau perlu, yang mana. Sadari bahwa "
  "jawabannya belum tentu “ya, beli”. Jawaban yang sah bisa berupa “tidak sekarang, rapikan dulu "
  "datanya”. Justru jawaban seperti itu sering bernilai tinggi karena menunjukkan Anda berpikir, bukan "
  "sekadar mengikuti keinginan manajemen.")

callout("step", "hasil pembacaan",
        "Setelah tiga pembacaan, Anda seharusnya punya satu halaman coretan berisi tiga kolom: "
        "angka, keluhan, dan keputusan. Simpan coretan itu; Anda akan memakainya di langkah berikutnya.")

# ============================================================ 4
h1("Langkah 2 — Hitung kondisi awal (baseline)", 4)

p("Baseline adalah potret kondisi saat ini sebelum ada perbaikan. Ini fondasi seluruh laporan: tanpa "
  "baseline, Anda tidak bisa mengatakan “turun 15%” karena tidak ada pembanding. Kabar baiknya, "
  "baseline kasus ini bisa dihitung hanya dengan perkalian.")

h3("Hitung berurutan, jangan melompat")
p("Ikuti urutan ini. Setiap baris memakai hasil baris sebelumnya, sehingga mudah diperiksa ulang.")

formula("(1) 20 kendaraan x 150 km                    = 3.000 km per hari")
formula("(2) 3.000 km x 26 hari                        = 78.000 km per bulan")
formula("(3) 3.000 km x 312 hari                       = 936.000 km per tahun")
formula("(4) 936.000 km / 10 km per liter              = 93.600 liter per tahun")
formula("(5) 93.600 liter x Rp10.000                   = Rp936.000.000 per tahun")
formula("(6) 20 kendaraan x 8 titik                    = 160 kiriman per hari")
formula("(7) 160 kiriman x 312 hari                    = 49.920 kiriman per tahun")
formula("(8) 936.000 km / 49.920 kiriman               = 18,75 km per kiriman")
formula("(9) Rp936.000.000 / 49.920 kiriman            = Rp18.750 BBM per kiriman")

callout("note", "dari mana angka 312 hari?",
        "Kasus menyebut 26 hari operasi per bulan. Setahun ada 12 bulan, jadi 26 x 12 = 312 hari. "
        "Angka ini bukan karangan; ia diturunkan dari data kasus. Tuliskan sebagai asumsi berkode "
        "(misalnya A1) supaya pembaca tahu itu hasil turunan, bukan data mentah.")

p("Angka 18,75 km per kiriman itu penting sekali, dan sering dilewatkan mahasiswa. Ia memberi tahu "
  "Anda bahwa setiap kali satu kendaraan berangkat mengantar satu kiriman, ia menempuh hampir 19 km. "
  "Kalau delapan kiriman dikunjungi dalam satu rute, seharusnya jarak per kiriman bisa jauh lebih "
  "kecil karena kunjungan bisa dikelompokkan. Di situlah letak inefisiensinya.")

table(
    ["Ukuran", "Nilai", "Cara memperoleh"],
    [
        ["Jarak armada per hari", "3.000 km", "20 x 150"],
        ["Jarak armada per tahun", "936.000 km", "3.000 x 312"],
        ["Konsumsi bahan bakar per tahun", "93.600 liter", "936.000 / 10"],
        ["Belanja bahan bakar per tahun", "Rp936.000.000", "93.600 x Rp10.000"],
        ["Jumlah kiriman per tahun", "49.920 kiriman", "160 x 312"],
        ["Jarak per kiriman", "18,75 km", "936.000 / 49.920"],
        ["Biaya bahan bakar per kiriman", "Rp18.750", "Rp936.000.000 / 49.920"],
        ["Biaya transportasi total per tahun", "Rp5.616.000.000", "936.000 x Rp6.000 (A3 + BBM)"],
    ],
    widths=[6.0, 4.0, 6.4],
    caption="Tabel 4. Baseline operasional armada",
    align_center_cols=[0, 1],
    note="Biaya transportasi total memakai asumsi biaya non-bahan bakar Rp5.000/km (A3) ditambah biaya bahan bakar Rp1.000/km, sehingga Rp6.000/km."
)

# ============================================================ 5
h1("Langkah 3 — Hitung biaya akibat masalah", 5)

p("Ini bagian yang paling membedakan laporan bagus dari laporan biasa. Banyak mahasiswa berhenti pada "
  "“perusahaan membuang bahan bakar”. Itu benar tetapi tidak cukup, karena tidak menjelaskan mengapa "
  "manajemen harus mengeluarkan uang untuk memperbaikinya.")

h3("Konsepnya: berapa uang yang hilang setiap tahun")
p("Namanya cost of poor performance, yaitu nilai yang hilang setiap tahun karena proses berjalan "
  "seperti sekarang. Cara menyusunnya sederhana: ambil setiap gejala yang Anda temukan pada pembacaan "
  "kedua, lalu beri harga. Kalau sebuah gejala tidak bisa diberi harga, jangan dipaksakan; cukup "
  "sebutkan sebagai dampak kualitatif.")

table(
    ["Komponen", "Cara menghitung", "Hasil per tahun", "Porsi"],
    [
        ["Bahan bakar berlebih", "15% x 936.000 km / 10 x Rp10.000", "Rp140.400.000", "23,0%"],
        ["Keterlambatan", "5% x 49.920 kiriman x Rp100.000", "Rp249.600.000", "40,9%"],
        ["Waktu tunggu di lokasi", "12,8 jam/hari x Rp38.462 x 312 hari", "Rp153.600.000", "25,1%"],
        ["Perencanaan manual", "40% x 2 dispatcher x Rp7.000.000 x 12", "Rp67.200.000", "11,0%"],
        ["Total", "Penjumlahan", "Rp610.800.000", "100%"],
    ],
    widths=[4.2, 7.0, 3.6, 1.6],
    caption="Tabel 5. Biaya akibat masalah (cost of poor performance)",
    align_center_cols=[2, 3],
    note="Setara Rp12.236 per kiriman, atau 65,3% dari seluruh belanja bahan bakar perusahaan."
)

callout("tip", "inilah temuan yang membuat laporan Anda menonjol",
        "Perhatikan bahwa bahan bakar hanya 23% dari total kerugian. Keterlambatan dan waktu tunggu "
        "mencapai 66%. Artinya, kalau perusahaan hanya mengejar penghematan bahan bakar, ia mengejar "
        "bagian yang paling kecil. Kalimat ini sekaligus menjawab keraguan bagian keuangan pada kasus, "
        "dan itulah yang dicari dosen: analisis yang mengubah kesimpulan, bukan yang mengulang narasi kasus.")

h3("Cara membuat asumsi yang jujur")
p("Kasus tidak memberi tahu berapa persen kiriman yang terlambat, berapa biaya satu kejadian terlambat, "
  "atau berapa lama pengemudi menunggu. Anda harus menetapkannya. Aturannya: tetapkan angka, beri kode, "
  "jelaskan dasarnya, dan sebutkan arah pengaruhnya kalau angka itu salah.")

table(
    ["Kode", "Asumsi", "Nilai", "Dasar", "Kalau salah, apa efeknya"],
    [
        ["A1", "Hari operasi per tahun", "312 hari", "26 x 12 dari kasus", "Semua nilai tahunan ikut berubah"],
        ["A2", "Titik per kendaraan per hari", "8 titik", "Kisaran lazim rute toko", "Jumlah kiriman dan biaya per kiriman berubah"],
        ["A3", "Biaya non-BBM per km", "Rp5.000", "Pengemudi, penyusutan, perawatan", "Nilai kapasitas yang dibebaskan berubah"],
        ["A4", "Tingkat keterlambatan", "5% kiriman", "Kisaran umum tanpa jendela waktu", "Komponen biaya terbesar, wajib diukur"],
        ["A5", "Biaya per kejadian terlambat", "Rp100.000", "Komunikasi ulang, potongan harga", "Manfaat keterlambatan berubah proporsional"],
    ],
    widths=[1.2, 4.4, 2.2, 4.4, 4.2],
    caption="Tabel 6. Contoh asumsi berkode (lima dari lima belas)",
    font_size=9,
    align_center_cols=[0, 2],
    note="Buat daftar lengkap di Lampiran, jangan di badan laporan, agar isi tetap 5–8 halaman."
)

callout("warn", "jangan mengarang data",
        "Perbedaan asumsi dan karangan: asumsi dinyatakan terbuka, diberi kode, punya dasar, dan Anda "
        "bersedia menggantinya kalau ada data nyata. Karangan adalah angka yang ditulis seolah-olah data "
        "kasus, tanpa keterangan asalnya. Dosen mudah membedakan keduanya, dan yang kedua biasanya "
        "langsung memotong nilai.")

# ============================================================ 6
h1("Langkah 4 — Temukan akar penyebab", 6)

p("Setelah tahu berapa kerugiannya, pertanyaan berikutnya: mengapa ini terjadi. Di sinilah banyak "
  "mahasiswa langsung melompat ke solusi. Padahal kalau akar penyebabnya salah, seluruh bab berikutnya "
  "ikut salah.")

h2("6.1 Mulai dari rumusan masalah yang tajam")
p("Rumusan masalah yang baik punya tiga ciri: menyebut apa yang tidak berfungsi, menyebut akibatnya, "
  "dan tidak menyalahkan orang. Bandingkan tiga versi berikut.")

table(
    ["Versi", "Rumusan", "Penilaian"],
    [
        ["Lemah", "Perusahaan kekurangan kendaraan sehingga pengiriman terlambat.", "Salah arah: kasus justru menyebut 20 kendaraan, dan masalahnya bukan jumlah."],
        ["Cukup", "Rute pengiriman tidak efisien sehingga biaya bahan bakar tinggi.", "Terlalu sempit: hanya melihat bahan bakar, padahal 66% kerugian dari layanan."],
        ["Kuat", "Sistem perencanaan dan pengendalian distribusi belum mampu mengubah pengetahuan rute yang bersifat tacit menjadi aturan proses dan data, sehingga armada menempuh jarak yang tidak perlu dan janji waktu tidak dapat dipenuhi.", "Menyebut penyebab, akibat, dan lapisan yang harus diperbaiki; tidak menyalahkan individu."],
    ],
    widths=[1.6, 8.4, 6.4],
    caption="Tabel 7. Tiga tingkat rumusan masalah",
    font_size=9
)

h2("6.2 Diagram sebab-akibat (fishbone)")
p("Gambar tulang ikan dengan enam kategori. Untuk kasus distribusi, isi yang masuk akal:")
bullet("metode kerja: rute mengikuti urutan pesanan masuk, tidak ada standar pengelompokan wilayah.", lead="Manusia dan metode — ")
bullet("tidak ada alat optimasi, tidak ada pelacakan posisi, pencatatan masih manual.", lead="Mesin dan teknologi — ")
bullet("master data toko tidak terstruktur, data jarak dan waktu tidak pernah dicatat.", lead="Data dan material — ")
bullet("tidak ada KPI jarak, waktu, dan ketepatan waktu sehingga tidak ada umpan balik.", lead="Pengukuran — ")
bullet("kemacetan, cuaca, jam penerimaan toko yang berubah.", lead="Lingkungan — ")
p("Setelah gambar jadi, buat satu pernyataan penting: kategori lingkungan di luar kendali perusahaan, "
  "sedangkan sisanya masih bisa diperbaiki. Ini mencegah Anda merekomendasikan hal yang mustahil.")

h2("6.3 Lima mengapa")
p("Teknik ini memaksa Anda terus bertanya “mengapa” sampai menemukan penyebab yang tidak bisa "
  "ditanyakan lagi. Contoh untuk kasus ini:")

table(
    ["Tingkat", "Pertanyaan", "Jawaban"],
    [
        ["1", "Mengapa kendaraan menempuh jarak tidak perlu?", "Urutan kunjungan tidak mengikuti kedekatan lokasi."],
        ["2", "Mengapa urutannya begitu?", "Rute disusun manual mengikuti urutan pesanan masuk."],
        ["3", "Mengapa masih manual?", "Tidak ada alat dan standar; kapasitas perencanaan hanya dua orang."],
        ["4", "Mengapa tidak ada alat dan standar?", "Pengetahuan rute bersifat tacit, tidak pernah dijadikan data atau prosedur."],
        ["5", "Mengapa tidak pernah dijadikan data?", "Tidak ada KPI, sehingga tidak ada tekanan dan umpan balik untuk memperbaiki."],
    ],
    widths=[1.4, 6.0, 9.0],
    caption="Tabel 8. Lima mengapa sampai akar penyebab",
    align_center_cols=[0]
)

callout("tip", "ciri akar penyebab yang benar",
        "Kalau “mengapa” kelima masih berbunyi “karena manajemen kurang peduli”, itu bukan akar penyebab, "
        "melainkan penilaian terhadap orang. Akar penyebab yang baik selalu menunjuk pada sesuatu yang "
        "bisa diubah: tidak ada standar, tidak ada data, tidak ada ukuran. Itulah yang nanti bisa "
        "dijawab oleh alternatif solusi Anda.")

# ============================================================ 7
h1("Langkah 5 — Susun alternatif solusi", 7)

p("Tugas mewajibkan minimal tiga alternatif. Saran praktis: buat empat, dan susun sebagai spektrum dari "
  "yang paling sederhana ke yang paling canggih. Dengan begitu perbandingan Anda terlihat berlapis, dan "
  "pilihan tengah (hybrid) menjadi masuk akal.")

table(
    ["Alternatif", "Isi", "Kekuatan", "Kelemahan"],
    [
        ["A1 Perbaikan prosedur", "Zonasi wilayah, SOP rute, master data di spreadsheet, KPI dasar", "Murah, cepat, tidak butuh vendor", "Kapasitas perencanaan tetap terbatas, tidak ada visibilitas"],
        ["A2 Aplikasi optimasi rute", "Langganan aplikasi optimasi + aplikasi pengemudi", "Rute teroptimasi, ada bukti pengiriman", "Data lokal belum ada, biaya mendekati batas anggaran"],
        ["A3 Platform terintegrasi", "TMS + telematika + integrasi gudang + portal pelanggan", "Manfaat terbesar, data terhubung", "Modal jauh di atas batas, lebih dari 90 hari"],
        ["A4 Hybrid bertahap", "Tata kelola dulu, lalu optimasi, lalu ETA ringan", "Memenuhi seluruh syarat, modal terkendali", "Butuh disiplin pelaksanaan bertahap"],
    ],
    widths=[3.4, 5.4, 3.8, 3.8],
    caption="Tabel 9. Empat alternatif sebagai spektrum",
    font_size=9
)

h2("7.1 Buat persyaratan desain sebelum menilai")
p("Supaya penilaian tidak terasa subjektif, tetapkan dulu syarat apa yang wajib dipenuhi solusi apa pun. "
  "Persyaratan ini diturunkan dari akar penyebab. Contohnya: DR-1 urutan kunjungan mempertimbangkan "
  "jarak, kapasitas, dan jendela waktu; DR-2 master data terstruktur; DR-3 ada visibilitas posisi dan "
  "ETA; DR-4 ada mekanisme override yang tercatat; DR-5 bertahap, tanpa menghentikan operasi, maksimal "
  "Rp150 juta; DR-6 data cukup untuk mengukur KPI harian; DR-7 bisa dijalankan tim yang ada.")

p("Lalu buat tabel sederhana: baris berisi DR-1 sampai DR-7, kolom berisi keempat alternatif, isinya "
  "“Ya”, “Sebagian”, atau “Tidak”. Tabel ini sangat kuat karena menunjukkan bahwa pilihan Anda bukan "
  "selera, melainkan konsekuensi dari syarat yang sudah Anda tetapkan lebih dulu.")

callout("step", "urutan yang benar",
        "Akar penyebab  →  persyaratan desain  →  alternatif  →  kriteria penilaian. "
        "Kalau Anda membalik urutannya (menyusun alternatif dulu, baru mencari alasan membenarkan), "
        "laporan akan terasa memihak dan mudah dipatahkan dosen saat presentasi.")

# ============================================================ 8
h1("Langkah 6 — Tetapkan kriteria, bobot, dan rubrik skor", 8)

p("Tiga hal harus ada agar penilaian Anda bisa dipertanggungjawabkan: kriterianya apa, bobotnya berapa, "
  "dan bagaimana angka 1 sampai 5 diberikan. Kalau salah satu tidak ada, dosen berhak menganggap "
  "penilaian Anda asal-asalan.")

h2("8.1 Kriteria dan bobot")
table(
    ["Kode", "Kriteria", "Bobot", "Alasan bobotnya segitu"],
    [
        ["K1", "Dampak terhadap efisiensi jarak dan biaya", "25%", "Kasus menetapkan target pengurangan jarak 15%, jadi ini tujuan utama"],
        ["K2", "Kualitas layanan dan visibilitas", "20%", "Keluhan pelanggan dan perubahan jadwal adalah gejala yang paling dirasakan"],
        ["K3", "Kepatuhan batas investasi Rp150 juta", "15%", "Batas anggaran mengikat; alternatif di atas batas tidak bisa dijalankan"],
        ["K4", "Kelayakan dalam 90 hari", "15%", "Masalah mendesak dan operasional tidak boleh berhenti"],
        ["K5", "Fleksibilitas dan penerimaan pengguna", "15%", "Keberatan pengemudi harus diakomodasi"],
        ["K6", "Skalabilitas dan kesiapan integrasi", "10%", "Penting untuk tumbuh, bukan prioritas 12 bulan pertama"],
        ["", "Total", "100%", ""],
    ],
    widths=[1.2, 5.4, 1.6, 8.2],
    caption="Tabel 10. Kriteria evaluasi dan justifikasi bobot",
    font_size=9,
    align_center_cols=[0, 2]
)

callout("warn", "jangan membagi bobot rata",
        "Membagi 100% menjadi enam bagian sama besar (16,7% masing-masing) terlihat adil tetapi salah "
        "secara logika: tidak semua kriteria sama penting pada kondisi ini. Yang wajib Anda lakukan adalah "
        "menjelaskan mengapa bobotnya berbeda. Kalau ragu, uji dengan mengganti bobot dan lihat apakah "
        "peringkat berubah; itu yang disebut uji ketahanan.")

h2("8.2 Rubrik skor 1–5")
p("Rubrik adalah aturan pemberian nilai. Tanpa rubrik, angka 4 dan 5 tidak bisa dibedakan dan penilaian "
  "Anda sulit dipertahankan.")
table(
    ["Skor", "Arti"],
    [
        ["5", "Memenuhi seluruh aspek secara langsung, tanpa pekerjaan tambahan, dan bisa diverifikasi dengan data."],
        ["4", "Memenuhi sebagian besar aspek dengan kekurangan kecil."],
        ["3", "Memenuhi secara formal, tetapi menuntut pekerjaan tambahan atau kompromi besar."],
        ["2", "Hanya memenuhi sebagian kecil aspek."],
        ["1", "Tidak memenuhi, atau bertentangan dengan batasan yang ada."],
    ],
    widths=[1.6, 14.8],
    caption="Tabel 11. Rubrik skor",
    align_center_cols=[0]
)

h2("8.3 Cara menghitung skor akhir")
p("Skor akhir adalah jumlah dari bobot dikali skor setiap kriteria. Kerjakan satu alternatif penuh "
  "sebagai contoh, lalu ulangi untuk yang lain.")
formula("Skor akhir = (bobot K1 x skor K1) + (bobot K2 x skor K2) + ... + (bobot K6 x skor K6)")
p("Contoh untuk Alternatif 1, dengan skor K1=2, K2=2, K3=5, K4=5, K5=4, K6=2:")
formula("(0,25 x 2) + (0,20 x 2) + (0,15 x 5) + (0,15 x 5) + (0,15 x 4) + (0,10 x 2)")
formula("= 0,50 + 0,40 + 0,75 + 0,75 + 0,60 + 0,20 = 3,20")
p("Angka 3,20 itulah yang ditulis di baris “skor akhir”. Tulis juga kontribusi tiap kriteria dalam "
  "kurung, misalnya “2 (0,50)”, agar pembaca bisa memeriksa tanpa menghitung ulang.")

table(
    ["Kriteria", "Bobot", "A1", "A2", "A3", "A4"],
    [
        ["K1 Efisiensi", "25%", "2 (0,50)", "4 (1,00)", "5 (1,25)", "4 (1,00)"],
        ["K2 Layanan", "20%", "2 (0,40)", "4 (0,80)", "5 (1,00)", "4 (0,80)"],
        ["K3 Anggaran", "15%", "5 (0,75)", "3 (0,45)", "1 (0,15)", "4 (0,60)"],
        ["K4 90 hari", "15%", "5 (0,75)", "4 (0,60)", "1 (0,15)", "3 (0,45)"],
        ["K5 Fleksibilitas", "15%", "4 (0,60)", "3 (0,45)", "2 (0,30)", "4 (0,60)"],
        ["K6 Skalabilitas", "10%", "2 (0,20)", "3 (0,30)", "5 (0,50)", "4 (0,40)"],
        ["Skor akhir", "100%", "3,20", "3,60", "3,35", "3,85"],
        ["Peringkat", "", "4", "2", "3", "1"],
    ],
    widths=[3.6, 1.6, 2.4, 2.4, 2.4, 2.4],
    caption="Tabel 12. Matriks penilaian multikriteria",
    font_size=9,
    align_center_cols=[1, 2, 3, 4, 5],
    note="Angka dalam kurung adalah bobot dikali skor. Peringkat 1 jatuh pada Alternatif 4."
)

# ============================================================ 9
h1("Langkah 7 — Hitung kelayakan uangnya", 9)

p("Bagian ini yang paling ditakuti, padahal rumusnya hanya tiga dan semuanya bisa dikerjakan dengan "
  "kalkulator biasa. Anda tidak perlu memahami matematika keuangan secara mendalam; cukup tahu apa yang "
  "diukur oleh masing-masing angka.")

h2("9.1 Tiga alat dan artinya")
table(
    ["Alat", "Pertanyaannya", "Rumus", "Cara membaca hasil"],
    [
        ["NPV", "Setelah tiga tahun, apakah uangnya kembali lebih banyak?", "NPV = -Capex + (Manfaat - Opex) x PVIFA", "Positif = layak. Semakin besar semakin baik."],
        ["Payback", "Berapa lama modal kembali?", "Payback = Capex / arus kas bersih per tahun x 12", "Semakin kecil semakin cepat; bandingkan dengan batas yang wajar."],
        ["B/C", "Setiap Rp1 yang ditanam menghasilkan berapa?", "B/C = total manfaat / (Capex + Opex)", "Di atas 1 = untung. Mengukur efisiensi, bukan besaran."],
    ],
    widths=[1.6, 5.0, 4.6, 5.2],
    caption="Tabel 13. Tiga alat kelayakan dan cara membacanya",
    font_size=9
)

h2("9.2 Apa itu PVIFA dan dari mana angkanya")
p("PVIFA (present value interest factor of annuity) dipakai karena uang Rp1 tahun depan tidak sama "
  "nilainya dengan Rp1 hari ini. Dengan diskonto 12% per tahun, nilainya:")
formula("PVIFA(12%, 1 tahun) = 0,8929")
formula("PVIFA(12%, 2 tahun) = 1,6901")
formula("PVIFA(12%, 3 tahun) = 2,4018")
p("Untuk horizon tiga tahun, cukup pakai 2,4018. Kalau dosen meminta horizon lima tahun, angkanya "
  "3,6048. Anda tidak perlu menghitung sendiri; tabel PVIFA ada di buku mana pun, dan yang penting Anda "
  "menyebutkan tingkat diskonto serta alasannya (misalnya 12% mendekati biaya modal perusahaan distribusi).")

h2("9.3 Contoh perhitungan lengkap untuk Alternatif 4")
p("Ikuti empat baris ini. Semua angka sudah tersedia dari langkah sebelumnya.")
formula("Capex            = Rp125.000.000")
formula("Opex per tahun   = Rp99.000.000")
formula("Manfaat per tahun= Rp247.728.000")
formula("Arus kas bersih  = Rp247.728.000 - Rp99.000.000 = Rp148.728.000")
formula("NPV = -125.000.000 + (148.728.000 x 2,4018)")
formula("NPV = -125.000.000 + 357.219.561 = Rp232.219.561  -> layak")
formula("Payback = 125.000.000 / 148.728.000 x 12 = 10,1 bulan")
formula("B/C = 247.728.000 / (125.000.000 + 99.000.000) = 1,64")

callout("warn", "tiga kesalahan hitung yang paling sering",
        "Pertama, memakai manfaat kotor sebagai arus kas, lupa mengurangi opex. Kedua, menjumlahkan "
        "capex dan opex lalu memasukkannya ke rumus NPV dua kali. Ketiga, mengalikan arus kas dengan "
        "jumlah tahun (3) alih-alih PVIFA (2,4018). Periksa ketiganya sebelum menulis.")

h2("9.4 Hasil semua alternatif")
table(
    ["Indikator", "A1", "A2", "A3", "A4"],
    [
        ["Capex", "Rp25 jt", "Rp115 jt", "Rp330 jt", "Rp125 jt"],
        ["Opex per tahun", "Rp24 jt", "Rp93 jt", "Rp156 jt", "Rp99 jt"],
        ["Manfaat per tahun", "Rp113,0 jt", "Rp211,7 jt", "Rp292,1 jt", "Rp247,7 jt"],
        ["Arus kas bersih", "Rp89,0 jt", "Rp118,7 jt", "Rp136,1 jt", "Rp148,7 jt"],
        ["NPV 3 tahun", "Rp188,9 jt", "Rp170,0 jt", "Rp-3,2 jt", "Rp232,2 jt"],
        ["Payback", "3,4 bulan", "11,6 bulan", "29,1 bulan", "10,1 bulan"],
        ["B/C", "3,29", "1,50", "1,00", "1,64"],
        ["Status", "Layak, dampak kecil", "Layak", "Tidak layak", "Layak, terbaik"],
    ],
    widths=[4.0, 3.1, 3.1, 3.1, 3.1],
    caption="Tabel 14. Ringkasan kelayakan finansial",
    font_size=9,
    align_center_cols=[1, 2, 3, 4]
)

callout("tip", "temuan yang wajib Anda komentari",
        "Alternatif 3 yang paling canggih ternyata NPV-nya negatif. Ini pelajaran penting dan sering "
        "dilewatkan: teknologi paling maju belum tentu layak secara uang. Tuliskan alasannya (modal "
        "Rp330 juta tidak tertutup manfaat Rp136 juta per tahun dalam tiga tahun), lalu bandingkan "
        "dengan Alternatif 1 yang B/C-nya tertinggi tetapi manfaatnya kecil. Dari kontras itulah "
        "argumen pemilihan menjadi kuat.")

# ============================================================ 10
h1("Langkah 8 — Uji dengan sensitivitas", 10)

p("Semua angka Anda sebagian berasal dari asumsi. Dosen pasti bertanya: “kalau asumsi Anda salah, "
  "apakah kesimpulannya berubah?” Anda harus sudah punya jawabannya, dan jawaban itu disebut analisis "
  "sensitivitas.")

h3("Cara paling sederhana: ubah satu parameter, lihat efeknya")
num("Pilih tiga parameter yang paling memengaruhi hasil: persentase penurunan keterlambatan, biaya operasional sistem, dan persentase pengurangan jarak.")
num("Untuk setiap parameter, buat dua nilai: satu menguntungkan, satu merugikan (misalnya optimis +50% dan pesimistis -50% dari nilai dasar).")
num("Hitung ulang NPV untuk setiap perubahan, satu per satu, sementara parameter lain tetap.")
num("Gambar hasilnya sebagai batang horizontal (diagram tornado): parameter yang batangnya paling panjang adalah yang paling menentukan.")

p("Untuk kasus ini hasilnya: NPV paling dipengaruhi tingkat penurunan keterlambatan, lalu biaya "
  "operasional sistem, lalu pengurangan jarak. Kesimpulan yang bisa Anda tulis: meskipun parameter "
  "paling berpengaruh justru yang paling sulit diukur, seluruh skenario tetap menghasilkan NPV positif. "
  "Itu membuat rekomendasi Anda tahan banting.")

table(
    ["Skenario", "NPV Alternatif 4", "Makna"],
    [
        ["Optimis", "Rp386,7 jt", "Semua parameter bergerak menguntungkan"],
        ["Basis", "Rp232,2 jt", "Angka yang dipakai di laporan"],
        ["Pesimistis", "Rp47,0 jt", "Semua parameter bergerak merugikan, tetap positif"],
        ["Titik pulang pokok", "Rp0", "Tercapai bila manfaat hanya terealisasi 61,0% dari proyeksi"],
    ],
    widths=[3.4, 3.6, 9.4],
    caption="Tabel 15. Hasil uji skenario",
    align_center_cols=[0, 1]
)

# ============================================================ 11
h1("Langkah 9 — Pilih dan pertahankan pilihan Anda", 11)

p("Memilih itu mudah; mempertahankan pilihan di depan dosen itu yang sulit. Siapkan lima argumen yang "
  "masing-masing bersandar pada angka atau fakta, bukan pada selera.")

num("Layak secara finansial. NPV tertinggi Rp232,2 juta, arus kas bersih Rp148,7 juta per tahun, payback 10,1 bulan.", lead="")
num("Mematuhi batas anggaran. Modal Rp125 juta adalah 83,3% dari pagu Rp150 juta, masih ada ruang Rp25 juta.", lead="")
num("Selesai dalam 90 hari tanpa menghentikan operasi, karena tiap lapis berjalan paralel dengan pekerjaan harian.", lead="")
num("Menjawab keberatan pengemudi secara struktural: override manual yang tercatat membuat pengetahuan lokal tetap terpakai.", lead="")
num("Menjawab keraguan keuangan dengan data: manfaat terbesar dari keterlambatan dan waktu tunggu, dan uji A/B memberi titik henti bila manfaat tak terbukti.", lead="")

h3("Jelaskan juga mengapa bukan yang lain")
p("Dosen sering bertanya “kenapa tidak Alternatif 3 sekalian?”. Siapkan jawaban singkat: karena modalnya "
  "Rp330 juta, melewati pagu Rp150 juta, butuh lebih dari 90 hari, dan NPV-nya negatif. Alternatif 1 "
  "memang paling cepat balik modal, tetapi manfaatnya hanya 45,6% dari Alternatif 4, sehingga lebih tepat "
  "diposisikan sebagai fondasi yang dikerjakan lebih dulu, bukan sebagai pilihan akhir.")

callout("tip", "kalimat penutup yang kuat",
        "Tulis satu kalimat ini di akhir subbab pemilihan: “Yang dipilih bukan perangkatnya, melainkan "
        "urutan pelaksanaannya.” Kalimat itu menunjukkan bahwa Anda memahami Alternatif 4 sebagai "
        "gabungan bertahap dari Alternatif 1, 2, dan sebagian 3, bukan sebagai barang baru yang berdiri sendiri.")

# ============================================================ 12
h1("Langkah 10 — Susun rencana 90 hari", 12)

p("Rencana yang dinilai bukan yang paling detail, melainkan yang paling bisa dijalankan. Dua hal yang "
  "membuat rencana terasa nyata: pembagian fase yang jelas, dan titik keputusan yang mengikat.")

table(
    ["Fase", "Hari", "Kegiatan utama", "Gate (boleh lanjut kalau…)"],
    [
        ["Fase 0", "1–14", "Ukur kondisi awal: jarak, waktu tiba, durasi bongkar, penyebab terlambat; rapikan data toko", "G1: minimal 95% toko berdata lengkap dan baseline tiga KPI tersedia"],
        ["Fase 1", "15–45", "Zonasi wilayah, SOP rute, tetapkan KPI, konfigurasi aplikasi, latih dispatcher", "G2: usulan rute 20 kendaraan berjalan dan dispatcher bisa mandiri"],
        ["Fase 2", "46–70", "Pilot 5 kendaraan, 15 kendaraan sebagai pembanding; kalibrasi parameter", "G3: jarak turun minimal 5% lebih baik dari pembanding dan OTIF tidak turun"],
        ["Fase 3", "71–90", "Migrasi bertahap per wilayah, dashboard KPI, serah terima", "G4: KPI stabil dua minggu dan pemilik proses sudah ditetapkan"],
    ],
    widths=[1.6, 1.4, 7.2, 6.2],
    caption="Tabel 16. Empat fase dan empat gate",
    font_size=9,
    align_center_cols=[0, 1]
)

callout("warn", "arti penting gate",
        "Gate bukan formalitas. Kalau G1 tidak terpenuhi (data toko belum lengkap), jangan lanjut ke "
        "Fase 1. Menuliskan aturan ini menunjukkan kedewasaan berpikir: Anda sadar proyek bisa gagal "
        "dan sudah menyiapkan cara berhenti dengan rapi sebelum uang terlanjur besar.")

p("Tambahkan juga prinsip yang membuat rencana ini bisa diterima: operasional tidak boleh berhenti. "
  "Karena itu setiap fase berjalan paralel dengan pekerjaan harian, dan pilot dipakai sebagai alat "
  "pembuktian, bukan sebagai uji coba teknis. Pilih pengemudi yang paling kritis terhadap aplikasi "
  "sebagai peserta pilot; kalau mereka menerima, yang lain akan lebih mudah mengikuti.")

# ============================================================ 13
h1("Langkah 11 — Petakan risiko", 13)

p("Risiko wajib mencakup empat kategori: operasional, teknologi, sosial, dan keamanan data. Yang paling "
  "sering dilupakan mahasiswa adalah dua kategori terakhir, padahal justru di situ letak kegagalan nyata "
  "sebuah proyek distribusi.")

table(
    ["Kategori", "Contoh risiko yang masuk akal untuk kasus ini"],
    [
        ["Operasional", "Dispatcher kembali menyusun rute manual; rollout mengganggu pengiriman harian; manfaat hilang karena kembali ke kebiasaan lama."],
        ["Teknologi", "Master data tidak akurat saat mulai; integrasi dengan sistem lama gagal; kualitas usulan rute rendah di awal; ketergantungan pada satu vendor."],
        ["Sosial", "Pengemudi menolak karena merasa diawasi; beban kerja baru bagi dispatcher; kesenjangan keterampilan digital."],
        ["Keamanan data", "Kebocoran data pelanggan dan posisi kendaraan; kehilangan data karena perangkat rusak atau vendor berhenti."],
    ],
    widths=[3.4, 13.0],
    caption="Tabel 17. Empat kategori risiko dan contohnya"
)

h2("13.1 Beri skor supaya bisa diprioritaskan")
p("Gunakan skala 1–5 untuk kemungkinan (K) dan dampak (D), lalu kalikan. Hasilnya dipetakan: 1–6 rendah, "
  "8–12 sedang, 15–25 tinggi. Risiko berskor tinggi dipantau lebih sering; sebutkan frekuensinya.")
table(
    ["Kode", "Risiko", "Kategori", "K", "D", "Skor", "Mitigasi"],
    [
        ["R1", "Dispatcher kembali menyusun rute manual", "Operasional", "4", "5", "20", "Override resmi dan tercatat; target awal tidak menuntut kepatuhan 100%"],
        ["R9", "Pengemudi menolak karena khawatir diawasi", "Sosial", "4", "4", "16", "GPS dipakai untuk ETA dan keselamatan, bukan sanksi; libatkan pengemudi sejak pilot"],
        ["R5", "Master data tidak akurat saat mulai", "Teknologi", "3", "5", "15", "Gate G1 mengikat; validasi silang dengan pengemudi"],
        ["R12", "Data pelanggan dan posisi bocor", "Keamanan data", "3", "5", "15", "Kendali akses berbasis peran; enkripsi; batasi masa simpan"],
    ],
    widths=[1.1, 4.4, 2.2, 0.8, 0.8, 1.0, 6.1],
    caption="Tabel 18. Contoh empat risiko prioritas",
    font_size=8.5,
    align_center_cols=[0, 2, 3, 4, 5]
)

callout("tip", "satu kalimat yang menunjukkan kedalaman",
        "Dua dari empat risiko berskor tertinggi bersifat sosial dan keamanan data, bukan teknis. "
        "Tuliskan pengamatan itu, lalu hubungkan dengan anggaran pelatihan: biaya pelatihan Rp12 juta "
        "bukan pelengkap, melainkan mitigasi risiko utama. Dosen membaca kalimat semacam ini sebagai "
        "tanda mahasiswa memahami proyek, bukan hanya teori.")

# ============================================================ 14
h1("Langkah 12 — Tetapkan KPI", 14)

p("KPI yang baik memenuhi lima syarat: spesifik, bisa diukur, punya sumber data yang jelas, punya "
  "baseline, dan punya target waktu. Buat tabel dengan kolom itu, lalu isi.")

table(
    ["Kode", "KPI", "Baseline", "Target 90 hari", "Target 12 bulan"],
    [
        ["K1", "Jarak per kiriman", "18,75 km (estimasi)", "-5%", "-13%"],
        ["K2", "OTIF (tepat waktu dan lengkap)", "Diukur Fase 0", "Tidak turun", "min. 95%"],
        ["K3", "Tingkat keterlambatan", "Diukur Fase 0", "-15% relatif", "-30% relatif"],
        ["K4", "Akurasi ETA", "Belum ada ETA", "min. 70%", "min. 85%"],
        ["K5", "Waktu tunggu di lokasi", "Diukur Fase 0", "-10%", "-18%"],
        ["K6", "Waktu menyusun rute", "Diukur Fase 0", "-20%", "-35%"],
        ["K7", "Kepatuhan memakai sistem", "0%", "min. 80%", "min. 95%"],
        ["K8", "Kelengkapan master data", "Diukur Fase 0", "min. 95%", "100%"],
        ["K9", "Biaya per kiriman", "Rp112.500 (estimasi)", "-4%", "-10%"],
    ],
    widths=[1.2, 5.2, 4.0, 3.0, 3.0],
    caption="Tabel 19. KPI, baseline, dan target",
    font_size=9,
    align_center_cols=[0, 2, 3, 4]
)

callout("warn", "jangan mengisi baseline dengan angka karangan",
        "Menulis “baseline 5%” padahal kasus tidak memberikannya adalah kesalahan yang mudah terlihat. "
        "Cara yang benar: tulis “diukur pada Fase 0”. Ini bukan jawaban malas, melainkan pernyataan "
        "jujur bahwa pengukuran harus dilakukan sebelum implementasi. Dosen menghargai kejujuran ini.")

p("Pastikan setiap KPI punya definisi operasional. Contoh: OTIF adalah persentase kiriman yang tiba di "
  "dalam jendela waktu yang dijanjikan dan jumlahnya lengkap. Tanpa definisi, dua orang bisa mengukur "
  "hal berbeda dan angkanya tidak bisa dibandingkan antar bulan.")

# ============================================================ 15
h1("Langkah 13 — Menulis dan memformat", 15)

p("Sekarang Anda punya semua bahan. Menulis menjadi cepat karena tugasnya hanya menjelaskan apa yang "
  "sudah Anda temukan. Ikuti urutan di bawah; jangan menulis dari halaman sampul.")

h2("15.1 Urutan menulis yang paling efisien")
num("Tulis BAB III dan IV lebih dulu, karena di situ semua angka dan tabel Anda berada.")
num("Tulis BAB II (landasan teori) setelah itu, dengan menyesuaikan teori pada temuan Anda, bukan sebaliknya.")
num("Tulis BAB V (rencana, risiko, KPI) karena isinya sudah tersedia dalam bentuk tabel.")
num("Tulis BAB I dan Ringkasan paling akhir, karena keduanya merangkum yang sudah ada.")
num("Buat sampul dan daftar pustaka terakhir, lalu format seluruh dokumen sekaligus.")

h2("15.2 Format dalam hitungan klik")
num("Ctrl+A untuk memilih seluruh isi.")
num("Ubah font menjadi Times New Roman, ukuran 12.")
num("Paragraph > Line spacing 1,5, Space after 0 pt.")
num("Ctrl+J untuk rata kiri-kanan.")
num("Layout > Margins > Normal (2,54 cm), lalu Layout > Size > A4.")
num("Tandai setiap judul bab sebagai Heading 1 dan subbab sebagai Heading 2.")

h2("15.3 Penomoran tabel dan gambar")
p("Aturannya sederhana: nomor memakai bab, lalu urutan. Tabel pertama di Bab II adalah Tabel 2.1, "
  "kedua Tabel 2.2, dan seterusnya. Judul tabel diletakkan di atas tabel, sedangkan judul gambar di "
  "bawah gambar. Setiap tabel dan gambar wajib dijelaskan dalam paragraf, bukan dibiarkan berdiri sendiri.")

h2("15.4 Sitasi dan daftar pustaka")
p("Setiap kali Anda memakai gagasan orang lain, tulis sumbernya dalam kurung, misalnya (Braekers dkk., "
  "2016). Gaya APA memakai nama belakang dan tahun. Di Daftar Pustaka, tulis lengkap: nama belakang, "
  "inisial, tahun dalam kurung, judul, penerbit atau jurnal, dan DOI bila ada. Semua yang disitasi harus "
  "muncul di daftar pustaka, dan sebaliknya. Ketidakcocokan ini sering menjadi temuan pertama dosen.")

h2("15.5 Membuat daftar isi otomatis")
p("Setelah semua judul ditandai sebagai Heading, klik di halaman daftar isi, lalu References > Table of "
  "Contents > pilih gaya. Nomor halaman akan terisi sendiri. Kalau berubah setelah diedit, klik kanan "
  "pada daftar isi lalu pilih Update Field > Update entire table.")

# ============================================================ 16
h1("Langkah 14 — Periksa dengan daftar centang", 16)

p("Sisihkan satu jam khusus untuk memeriksa, jangan langsung mengumpulkan. Periksa dari daftar ini satu "
  "per satu dan centang.")

table(
    ["No", "Yang diperiksa", "Cara cepat memeriksa"],
    [
        ["1", "Sampul memuat judul, nama, NIM, kelas, mata kuliah, dosen, prodi, tahun", "Baca ulang; tidak boleh ada yang kosong atau masih berupa tanda […]"],
        ["2", "Ketujuh isi wajib ada", "Cocokkan dengan Tabel 2 di panduan ini"],
        ["3", "Sistematika sesuai (BAB I–VI, subbab 1.1–6.2)", "Lihat daftar isi, tidak ada nomor yang melompat"],
        ["4", "A4, TNR 12, spasi 1,5, margin 2,54, justify", "Klik satu paragraf dan periksa kotak font serta penggaris"],
        ["5", "Isi 5–8 halaman di luar sampul dan lampiran", "Hitung halaman BAB I sampai akhir BAB VI"],
        ["6", "Semua tabel dan gambar bernomor serta berjudul", "Pastikan urutannya 2.1, 2.2, 3.1, dan seterusnya"],
        ["7", "Setiap tabel dan gambar dijelaskan dalam paragraf", "Tidak ada tabel yang muncul tanpa kalimat pengantar"],
        ["8", "Bobot kriteria berjumlah 100%", "Jumlahkan; kalau bukan 100, perbaiki"],
        ["9", "Rubrik skor dijelaskan", "Ada penjelasan arti skor 1 sampai 5"],
        ["10", "Perhitungan skor akhir bisa diperiksa ulang", "Hitung satu baris dengan kalkulator"],
        ["11", "Asumsi diberi kode dan dijelaskan dasarnya", "Ada tabel A1, A2, dan seterusnya"],
        ["12", "Data yang belum tersedia disebutkan beserta cara mengumpulkannya", "Ada tabel data yang perlu dikumpulkan"],
        ["13", "Semua sitasi muncul di Daftar Pustaka dan sebaliknya", "Buat daftar nama, cocokkan dua arah"],
        ["14", "Tidak ada angka yang tidak bisa dijelaskan asalnya", "Untuk setiap angka, Anda bisa menjawab “dari mana ini?”"],
        ["15", "Tidak ada salah ketik pada nama, NIM, dan nama dosen", "Ini yang paling memalukan dan paling mudah dihindari"],
    ],
    widths=[1.0, 8.4, 7.0],
    caption="Tabel 20. Daftar centang sebelum mengumpulkan",
    font_size=8.5,
    align_center_cols=[0]
)

# ============================================================ 17
h1("Kesalahan yang paling sering menurunkan nilai", 17)

table(
    ["Kesalahan", "Kenapa fatal", "Perbaikan"],
    [
        ["Menulis “masalahnya kurang armada”", "Bertentangan dengan data kasus (20 kendaraan untuk 8 titik per hari)", "Arahkan masalah pada sistem perencanaan, bukan jumlah kendaraan"],
        ["Hanya menghitung bahan bakar", "Mengabaikan 66% kerugian yang berasal dari keterlambatan dan waktu tunggu", "Buat tabel biaya masalah dengan empat komponen"],
        ["Alternatif hanya dua", "Melanggar syarat minimal tiga alternatif", "Buat empat sebagai spektrum sederhana ke canggih"],
        ["Bobot dibagi rata tanpa alasan", "Terlihat adil tetapi tidak logis; tidak ada justifikasi", "Bedakan bobot dan jelaskan alasannya per kriteria"],
        ["Tidak ada rubrik skor", "Skor 4 dan 5 tidak bisa dibedakan; penilaian dianggap asal", "Tambahkan tabel arti skor 1–5"],
        ["Mengisi baseline dengan angka karangan", "Mudah terlihat karena kasus tidak menyebutkannya", "Tulis “diukur pada Fase 0” dan jelaskan cara mengukurnya"],
        ["NPV dihitung dari manfaat kotor", "Hasilnya terlalu tinggi dan tidak realistis", "Kurangi opex dulu, baru kalikan PVIFA"],
        ["Risiko hanya teknis", "Melewatkan kategori sosial dan keamanan data yang justru paling menentukan", "Isi keempat kategori"],
        ["Tabel tanpa penjelasan", "Pembaca tidak tahu apa yang harus disimpulkan", "Tambahkan satu paragraf sebelum atau sesudah tabel"],
        ["Sitasi tidak ada di daftar pustaka", "Dianggap mengutip tanpa sumber", "Cocokkan dua arah sebelum mengumpulkan"],
    ],
    widths=[5.0, 5.4, 6.0],
    caption="Tabel 21. Sepuluh kesalahan umum dan cara memperbaikinya",
    font_size=8.5
)

# ============================================================ 18
h1("Kalau data terasa kurang", 18)

p("Hampir semua mahasiswa merasa datanya kurang, dan itu wajar: studi kasus memang sengaja tidak "
  "lengkap. Yang membedakan jawaban bagus adalah sikap terhadap kekurangan itu. Jangan diam-diam "
  "mengarang; sebutkan datanya, lalu jelaskan cara memperolehnya.")

table(
    ["No", "Data yang belum ada", "Untuk apa", "Cara mengumpulkannya"],
    [
        ["1", "Koordinat dan titik akses toko", "Dasar menghitung jarak dan mengelompokkan wilayah", "Survei lapangan dan pencatatan GPS saat kunjungan"],
        ["2", "Jam penerimaan dan jendela waktu toko", "Batasan waktu pada model rute", "Wawancara terstruktur dengan sales dan toko"],
        ["3", "Durasi bongkar muat per toko", "Memperkirakan waktu layanan per titik", "Pengukuran langsung selama 10 hari kerja"],
        ["4", "Jarak dan waktu tempuh aktual", "Baseline K1 dan K5", "Odometer dan GPS, direkap harian"],
        ["5", "Tingkat dan penyebab keterlambatan", "Baseline K3 dan kalibrasi manfaat", "Log keterlambatan dengan kategori penyebab"],
        ["6", "Struktur biaya non-bahan bakar", "Memvalidasi asumsi Rp5.000/km", "Data akuntansi: penyusutan, perawatan, asuransi, upah"],
        ["7", "Riwayat rute 3–6 bulan", "Melihat pola dan sebagai pembanding", "Ekstraksi arsip daftar pesanan dan lembar rute"],
        ["8", "Kendala khusus per lokasi", "Aturan override dan parameter", "Diskusi kelompok terarah dengan pengemudi senior"],
        ["9", "Harapan pelanggan atas ketepatan waktu", "Menetapkan janji waktu dan target OTIF", "Survei singkat 30 pelanggan utama"],
        ["10", "Kapasitas muatan per kendaraan", "Batasan kapasitas pada optimasi", "Dokumen spesifikasi kendaraan dari bagian teknik"],
    ],
    widths=[1.0, 4.6, 4.4, 6.4],
    caption="Tabel 22. Data yang perlu dikumpulkan dan caranya",
    font_size=8.5,
    align_center_cols=[0]
)

callout("tip", "kalimat yang menyelamatkan Anda saat ditanya",
        "Kalau dosen bertanya “angka ini dari mana?”, jawaban yang benar bukan “perkiraan saya, Pak”. "
        "Jawablah: “Ini asumsi A4 karena kasus tidak menyediakan data tingkat keterlambatan. Nilainya "
        "saya tetapkan 5% berdasarkan kisaran umum, dan pada Fase 0 angka ini akan diganti hasil "
        "pengukuran. Pada analisis sensitivitas, perubahan asumsi ini tidak mengubah kesimpulan.” "
        "Tiga kalimat itu menunjukkan Anda tahu batas pengetahuan Anda sendiri.")

# ============================================================ 19
h1("Pembagian waktu lima hari", 19)

table(
    ["Hari", "Fokus", "Keluaran yang harus ada di akhir hari"],
    [
        ["Hari 1", "Membaca kasus, mencatat fakta, menghitung baseline", "Tabel angka dasar selesai dan bisa dipertahankan"],
        ["Hari 2", "Menghitung biaya masalah, membuat fishbone dan lima mengapa", "Rumusan masalah utama sudah satu paragraf"],
        ["Hari 3", "Menyusun empat alternatif, kriteria, bobot, rubrik", "Tabel kriteria dan tabel pemenuhan syarat selesai"],
        ["Hari 4", "Menghitung NPV, payback, B/C, matriks skor, sensitivitas", "Semua tabel angka selesai; alternatif terpilih sudah jelas"],
        ["Hari 5", "Menulis seluruh bab, memformat, memeriksa daftar centang", "Laporan siap dikumpulkan"],
    ],
    widths=[1.4, 7.4, 7.6],
    caption="Tabel 23. Rencana lima hari",
    align_center_cols=[0]
)

# ============================================================ 20
h1("Istilah yang sering muncul", 20)

table(
    ["Istilah", "Arti sederhana"],
    [
        ["Baseline", "Kondisi awal sebelum perbaikan; pembanding untuk mengukur keberhasilan."],
        ["Capex", "Belanja modal: uang yang dikeluarkan sekali di awal, misalnya lisensi dan perangkat."],
        ["Opex", "Biaya operasional: uang yang dikeluarkan berulang setiap tahun, misalnya langganan."],
        ["NPV", "Nilai sekarang bersih. Positif berarti investasi menghasilkan lebih banyak daripada modalnya."],
        ["Payback", "Waktu yang dibutuhkan agar modal kembali."],
        ["B/C ratio", "Perbandingan manfaat terhadap biaya. Di atas 1 berarti menguntungkan."],
        ["PVIFA", "Faktor pengali untuk menghitung nilai sekarang dari penerimaan yang sama setiap tahun."],
        ["OTIF", "On Time In Full: kiriman tiba tepat waktu sekaligus lengkap."],
        ["ETA", "Perkiraan waktu tiba yang dikomunikasikan ke pelanggan."],
        ["VRP / VRPTW", "Persoalan penentuan rute kendaraan; VRPTW adalah versinya yang memakai jendela waktu."],
        ["Override", "Tindakan dispatcher menimpa usulan sistem karena alasan lapangan, dan dicatat."],
        ["Gate", "Titik keputusan: fase berikutnya hanya jalan bila kriteria tertentu terpenuhi."],
        ["Tacit knowledge", "Pengetahuan yang tersimpan di kepala orang dan belum menjadi data atau prosedur."],
        ["Sensitivitas", "Uji untuk melihat apakah kesimpulan berubah bila asumsi diubah."],
    ],
    widths=[3.4, 13.0],
    caption="Tabel 24. Glosarium",
    font_size=9
)

# ============================================================ 21
h1("Penutup", 21)

p("Kalau Anda mengikuti dua puluh langkah di atas, Anda akan sampai pada laporan yang isinya sangat "
  "mirip dengan contoh yang sudah tersedia, karena memang begitulah cara menyelesaikannya: berurutan, "
  "setiap angka bisa dijelaskan, dan setiap pilihan punya alasan.")

p("Tetapi ada satu hal yang tidak bisa digantikan panduan mana pun: Anda harus benar-benar memahami "
  "angka Anda sendiri. Saat presentasi atau tanya jawab, dosen biasanya memilih satu angka secara acak "
  "dan bertanya “ini dari mana?”. Mahasiswa yang menyusun sendiri perhitungannya bisa menjawab dalam "
  "lima detik. Mahasiswa yang menyalin akan kesulitan, sekalipun laporannya terlihat rapi.")

callout("note", "tiga hal yang paling menentukan nilai",
        "Pertama, ketepatan merumuskan masalah: kalau salah di sini, semua bab setelahnya ikut melenceng. "
        "Kedua, kejujuran soal asumsi: menyatakan keterbatasan justru menaikkan kredibilitas. Ketiga, "
        "konsistensi angka: satu angka yang berubah diam-diam antar bab akan merusak kepercayaan pada "
        "seluruh laporan. Periksa ketiganya sebelum mengumpulkan.")

p("Selamat mengerjakan.", italic=True)

# ---------- properti dokumen ----------
cp = doc.core_properties
cp.title = "Panduan Lengkap Mengerjakan Studi Kasus 4"
cp.subject = "Panduan langkah demi langkah untuk mahasiswa"
cp.author = "Panduan Studi Kasus"
cp.keywords = "studi kasus, panduan, manajemen industri, distribusi, NPV, KPI"
cp.language = "id-ID"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print("tersimpan:", os.path.abspath(OUT))
print("paragraf:", len(doc.paragraphs), "| tabel:", len(doc.tables))
