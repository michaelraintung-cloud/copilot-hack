"""Panduan sederhana mengerjakan Studi Kasus 4 — versi lugas untuk mahasiswa baru.

Jalankan: python3 build_panduan_sederhana.py
Keluaran: ../output/Panduan-Sederhana-Case-4.docx
"""
import os

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output", "Panduan-Sederhana-Case-4.docx")

NAVY = RGBColor(0x1F, 0x38, 0x64)
BLUE = RGBColor(0x2E, 0x54, 0x96)
DARK = RGBColor(0x1A, 0x1A, 0x1A)
GREY = RGBColor(0x59, 0x59, 0x59)
GREEN = RGBColor(0x1E, 0x6B, 0x45)
RED = RGBColor(0xA6, 0x2B, 0x2B)
FONT = "Times New Roman"
USABLE = 16.4

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
for side in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
    setattr(sec, side, Cm(2.3))

st = doc.styles["Normal"]
st.font.name = FONT
st.font.size = Pt(11)
st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
st.paragraph_format.space_after = Pt(5)
st.paragraph_format.line_spacing = 1.15


def _shade(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color)
    tcPr.append(shd)


def _fix(tbl, widths):
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn("w:tblLayout")):
        tblPr.remove(old)
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tblPr.append(lay)
    for row in tbl.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)


def h1(text):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_before = Pt(16)
    pf.space_after = Pt(5)
    pf.keep_with_next = True
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = NAVY
    pPr = par._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "3")
    bottom.set(qn("w:color"), "1F3864")
    pBdr.append(bottom)
    pPr.append(pBdr)
    return par


def h2(text):
    par = doc.add_paragraph()
    par.paragraph_format.space_before = Pt(10)
    par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.keep_with_next = True
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(11.5)
    r.font.bold = True
    r.font.color.rgb = BLUE
    return par


def p(text, lead=None, size=11, space_after=5, italic=False):
    par = doc.add_paragraph()
    par.paragraph_format.space_after = Pt(space_after)
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if lead:
        r0 = par.add_run(lead)
        r0.font.name = FONT
        r0.font.size = Pt(size)
        r0.font.bold = True
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.italic = italic
    return par


def num(text, lead=None, size=11):
    par = doc.add_paragraph(style="List Number")
    pf = par.paragraph_format
    pf.space_after = Pt(3)
    pf.left_indent = Cm(0.9)
    pf.first_line_indent = Cm(-0.5)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
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
    pf.left_indent = Cm(0.8)
    pf.space_after = Pt(2)
    pf.line_spacing = 1.1
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
    par = cell.paragraphs[0]
    par.paragraph_format.space_after = Pt(3)
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
    _fix(tbl, [USABLE])
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def table(headers, rows, widths, caption=None, note=None, size=9.5, center=None,
          head_fill="1F3864"):
    if caption:
        cp = doc.add_paragraph()
        cp.paragraph_format.space_before = Pt(6)
        cp.paragraph_format.space_after = Pt(2)
        cp.paragraph_format.keep_with_next = True
        r = cp.add_run(caption)
        r.font.name = FONT
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = NAVY

    tbl = doc.add_table(rows=1, cols=len(headers))
    tbl.style = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, htxt in enumerate(headers):
        cell = tbl.rows[0].cells[i]
        _shade(cell, head_fill)
        par = cell.paragraphs[0]
        par.paragraph_format.space_after = Pt(1)
        par.paragraph_format.space_before = Pt(1)
        par.paragraph_format.line_spacing = 1.0
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = par.add_run(htxt)
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for row in rows:
        cells = tbl.add_row().cells
        for i, val in enumerate(row):
            par = cells[i].paragraphs[0]
            par.paragraph_format.space_after = Pt(1)
            par.paragraph_format.space_before = Pt(1)
            par.paragraph_format.line_spacing = 1.0
            if center and i in center:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = par.add_run(str(val))
            r.font.name = FONT
            r.font.size = Pt(size)

    _fix(tbl, widths)
    if note:
        np_ = doc.add_paragraph()
        np_.paragraph_format.space_before = Pt(1)
        np_.paragraph_format.space_after = Pt(6)
        np_.paragraph_format.line_spacing = 1.0
        r = np_.add_run(note)
        r.font.name = FONT
        r.font.size = Pt(8.5)
        r.font.italic = True
        r.font.color.rgb = GREY
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(3)


# ---------------------------------------------------------------- SAMPUL
for _ in range(2):
    doc.add_paragraph()
par = doc.add_paragraph()
par.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = par.add_run("PANDUAN RINGKAS")
r.font.name = FONT
r.font.size = Pt(12)
r.font.bold = True
r.font.color.rgb = GREY

par = doc.add_paragraph()
par.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = par.add_run("MENGERJAKAN STUDI KASUS 4")
r.font.name = FONT
r.font.size = Pt(24)
r.font.bold = True
r.font.color.rgb = NAVY

par = doc.add_paragraph()
par.alignment = WD_ALIGN_PARAGRAPH.CENTER
par.paragraph_format.space_after = Pt(20)
r = par.add_run("Sepuluh langkah, tanpa istilah yang membingungkan")
r.font.name = FONT
r.font.size = Pt(13)
r.font.italic = True
r.font.color.rgb = BLUE

box("Untuk siapa panduan ini?",
    "Untuk mahasiswa yang baru pertama kali mengerjakan studi kasus dan merasa laporan contoh "
    "terlalu rumit. Panduan ini memakai bahasa sehari-hari, angkanya sedikit, dan setiap langkah "
    "langsung diberi contoh. Kalau Anda bisa tambah, kali, dan bagi, Anda bisa mengerjakan "
    "seluruh perhitungan di sini memakai kalkulator telepon.",
    fill="F0F4FA")

doc.add_paragraph()
par = doc.add_paragraph()
par.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = par.add_run("Waktu pengerjaan: 3 hari\nTotal perhitungan: 9 rumus sederhana")
r.font.name = FONT
r.font.size = Pt(11)
r.font.color.rgb = GREY

doc.add_page_break()

# ---------------------------------------------------------------- 0
h1("Baca ini dulu")
p("Sebelum menghitung apa pun, ketahuilah satu hal: dosen tidak menilai panjang laporan. Yang "
  "dinilai adalah apakah Anda tahu angka Anda berasal dari mana, dan apakah pilihan Anda punya "
  "alasan. Laporan delapan halaman yang setiap angkanya bisa Anda jelaskan lebih baik daripada "
  "dua puluh halaman hasil salin.")
p("Karena itu panduan ini hanya meminta Anda melakukan lima hal: menghitung kondisi awal, "
  "menghitung kerugian, mencari penyebab, membandingkan tiga pilihan, lalu memilih satu dengan "
  "alasan. Sisanya adalah menulis dan merapikan format.")
box("Yang paling sering ditanyakan dosen",
    "“Angka ini dari mana?” — Kalau Anda menyusun sendiri perhitungannya, Anda bisa menjawab dalam "
    "lima detik. Kalau menyalin, Anda akan diam. Itulah alasan panduan ini menuntun Anda menghitung, "
    "bukan menyuruh Anda menyalin.",
    fill="E9F5EE", accent=GREEN)

# ---------------------------------------------------------------- 1
h1("Langkah 1 — Pahami yang diminta")
p("Tugas meminta tujuh hal. Anggap ini daftar belanja: kalau satu tidak ada, nilainya berkurang.")

table(["No", "Yang diminta", "Wujudnya di laporan Anda"],
      [["1", "Masalah utama dan penyebabnya", "Satu paragraf rumusan masalah + tabel lima mengapa"],
       ["2", "Hitungan kerugian", "Tabel kerugian empat komponen"],
       ["3", "Minimal tiga alternatif solusi", "Tiga alternatif + tabel perbandingan"],
       ["4", "Rekomendasi dengan asumsi jelas", "Subbab pemilihan + tabel asumsi"],
       ["5", "Risiko (operasional, teknologi, sosial, keamanan data)", "Tabel risiko dengan skor"],
       ["6", "KPI", "Tabel KPI: angka awal dan target"],
       ["7", "Rencana 90 hari", "Tabel empat fase dengan syarat lanjut"]],
      widths=[1.0, 7.4, 8.0],
      caption="Tabel 1. Tujuh hal yang diminta tugas",
      center=[0])

p("Selain itu ada tiga hal yang sering membuat nilai bocor tanpa disadari:")
num("Sistematika. Bab harus I sampai VI, subbab 1.1–1.5, 2.1–2.4, 3.1–3.4, 4.1–4.4, 5.1–5.5, 6.1–6.2. Jangan menambah atau mengurangi.")
num("Format. A4, Times New Roman 12, spasi 1,5, margin 2,54 cm, rata kiri-kanan.")
num("Panjang. Isi 5–8 halaman, dihitung dari Bab I sampai Bab VI. Sampul dan lampiran tidak dihitung.")

# ---------------------------------------------------------------- 2
h1("Langkah 2 — Baca kasus tiga kali")
p("Membaca sekali lalu langsung menulis adalah penyebab laporan berputar-putar. Bacalah tiga kali, "
  "dan setiap kali mencari hal berbeda.")
table(["Bacaan", "Yang dicari", "Contoh dari kasus ini"],
      [["Pertama", "Angka", "20 kendaraan; 150 km per hari; 26 hari per bulan; 1 liter per 10 km; Rp10.000 per liter; target turun 15%; pagu Rp150 juta"],
       ["Kedua", "Keluhan", "Rute disusun manual; kendaraan lewat jalan yang sama; terlambat baru diketahui setelah menelepon; pengemudi menolak aplikasi; keuangan meragukan penghematan"],
       ["Ketiga", "Keputusan", "Apakah perlu beli aplikasi optimasi rute, dan kalau perlu, yang mana"]],
      widths=[2.2, 3.4, 10.8],
      caption="Tabel 2. Tiga pembacaan, tiga tujuan")

p("Hasil akhirnya satu halaman coretan: daftar angka, daftar keluhan, dan satu keputusan yang harus "
  "Anda ambil. Simpan halaman itu; semua langkah berikutnya hanya memakai isi halaman tersebut.")

# ---------------------------------------------------------------- 3
h1("Langkah 3 — Hitung kondisi awal (6 rumus)")
p("Kondisi awal disebut baseline: potret keadaan sekarang sebelum ada perbaikan. Tanpa baseline Anda "
  "tidak bisa bilang “turun 15%”, karena tidak ada pembanding. Kabar baiknya, semuanya hanya "
  "perkalian dan pembagian.")
formula("1)  20 kendaraan x 150 km            = 3.000 km per hari")
formula("2)  3.000 km x 312 hari              = 936.000 km per tahun")
formula("3)  936.000 km : 10 km per liter    = 93.600 liter per tahun")
formula("4)  93.600 liter x Rp10.000         = Rp936.000.000 per tahun")
formula("5)  20 kendaraan x 8 titik x 312    = 49.920 kiriman per tahun")
formula("6)  936.000 km : 49.920 kiriman     = 18,75 km per kiriman")
box("Dari mana angka 312 hari?",
    "Kasus menyebut 26 hari operasi per bulan. Setahun 12 bulan, jadi 26 x 12 = 312 hari. Angka ini "
    "bukan karangan, tetapi hasil turunan. Tulis di laporan sebagai asumsi berkode, misalnya "
    "(A1), supaya pembaca tahu itu hasil hitungan Anda, bukan data dari kasus.",
    fill="FFF7E6", accent=RGBColor(0x8A, 0x5A, 0x00))
p("Angka 18,75 km per kiriman itu penting dan sering dilewatkan. Artinya setiap kali satu kendaraan "
  "berangkat, ia menempuh hampir 19 km. Kalau delapan kiriman dikunjungi dalam satu rute, seharusnya "
  "jaraknya bisa jauh lebih pendek karena kunjungan bisa dikelompokkan. Di situlah letak "
  "pemborosannya.")

# ---------------------------------------------------------------- 4
h1("Langkah 4 — Hitung kerugiannya")
p("Ini bagian yang membedakan laporan bagus dari laporan biasa. Banyak mahasiswa berhenti pada "
  "“perusahaan membuang bahan bakar”. Itu benar, tetapi belum menjawab pertanyaan dosen: kalau hanya "
  "membuang bahan bakar, kenapa harus beli sistem mahal?")
p("Caranya: ambil setiap keluhan dari bacaan kedua, lalu beri harga. Kalau tidak bisa diberi harga, "
  "jangan dipaksakan; sebut saja sebagai dampak yang tidak dihitung.")
table(["Komponen", "Cara menghitung", "Hasil per tahun", "Porsi"],
      [["Bahan bakar berlebih", "15% x 936.000 km : 10 x Rp10.000", "Rp140.400.000", "23,0%"],
       ["Keterlambatan", "5% x 49.920 kiriman x Rp100.000", "Rp249.600.000", "40,9%"],
       ["Waktu tunggu", "12,8 jam/hari x Rp38.462 x 312 hari", "Rp153.600.000", "25,1%"],
       ["Perencanaan manual", "40% x 2 orang x Rp7.000.000 x 12", "Rp67.200.000", "11,0%"],
       ["Jumlah", "", "Rp610.800.000", "100%"]],
      widths=[3.8, 7.2, 3.5, 1.9],
      caption="Tabel 3. Kerugian akibat masalah",
      center=[2, 3],
      note="Setara Rp12.236 per kiriman, atau 65,3% dari belanja bahan bakar setahun.")

box("Inilah temuan yang membuat laporan Anda menonjol",
    "Bahan bakar hanya 23% dari kerugian. Keterlambatan dan waktu tunggu mencapai 66%. Artinya kalau "
    "perusahaan hanya mengejar penghematan bahan bakar, ia mengejar bagian yang paling kecil. Kalimat "
    "ini sekaligus menjawab keraguan bagian keuangan pada kasus.",
    fill="E9F5EE", accent=GREEN)

p("Perhatikan empat angka yang tidak ada di kasus: 8 titik per kendaraan, 5% keterlambatan, Rp100.000 "
  "per kejadian, dan 40% waktu dispatcher. Anda yang menetapkan. Aturannya: tetapkan angkanya, beri "
  "kode (A1, A2, dan seterusnya), tulis alasannya, dan sebutkan akibatnya kalau angka itu salah. Itu "
  "namanya asumsi, bukan karangan.")

# ---------------------------------------------------------------- 5
h1("Langkah 5 — Cari penyebabnya")
p("Sebelum melompat ke solusi, jawab dulu: mengapa ini terjadi. Kalau penyebabnya salah, seluruh bab "
  "berikutnya ikut salah. Pakai teknik lima mengapa: tanyakan “mengapa” lima kali.")
table(["Ke", "Pertanyaan", "Jawaban"],
      [["1", "Mengapa kendaraan menempuh jarak tidak perlu?", "Urutan kunjungan tidak mengikuti kedekatan lokasi"],
       ["2", "Mengapa urutannya begitu?", "Rute disusun manual mengikuti urutan pesanan masuk"],
       ["3", "Mengapa masih manual?", "Tidak ada alat dan standar; perencana hanya dua orang"],
       ["4", "Mengapa tidak ada alat dan standar?", "Pengetahuan rute hanya di kepala orang, belum jadi data"],
       ["5", "Mengapa belum jadi data?", "Tidak ada KPI, sehingga tidak ada dorongan untuk memperbaiki"]],
      widths=[1.0, 6.6, 8.8],
      caption="Tabel 4. Lima mengapa sampai akar penyebab",
      center=[0])

box("Ciri akar penyebab yang benar",
    "Kalau “mengapa” kelima masih berbunyi “karena manajemen kurang peduli”, itu bukan akar penyebab, "
    "melainkan penilaian terhadap orang. Akar penyebab selalu menunjuk sesuatu yang bisa diubah: "
    "tidak ada standar, tidak ada data, tidak ada ukuran. Itulah yang nanti dijawab oleh solusi Anda.",
    fill="FBEEEE", accent=RED)

# ---------------------------------------------------------------- 6
h1("Langkah 6 — Buat tiga alternatif")
p("Tugas minta minimal tiga. Susun berjenjang dari paling murah ke paling lengkap; dengan begitu "
  "pilihan tengah terlihat masuk akal, bukan asal pilih.")
table(["Alternatif", "Isinya", "Kelebihan", "Kekurangan"],
      [["A1 Prosedur", "Bagi zona wilayah, buat SOP rute, rapikan data toko di spreadsheet, tetapkan KPI. Tanpa perangkat berbayar", "Murah dan cepat", "Perencana tetap dua orang; posisi kendaraan tidak terlihat"],
       ["A2 Aplikasi", "Langganan aplikasi optimasi 20 kendaraan + aplikasi pengemudi", "Rute otomatis; waktu tiba tercatat", "Data lokal belum ada; langganan mahal"],
       ["A3 Bertahap", "Rapikan data dulu (30 hari), pasang aplikasi berisi data lokal, lalu tambah pelacakan posisi dan ETA", "Memenuhi semua syarat; modal terkendali", "Butuh disiplin menjalankan bertahap"]],
      widths=[2.6, 7.2, 3.4, 3.2],
      caption="Tabel 5. Tiga alternatif",
      size=9)

# ---------------------------------------------------------------- 7
h1("Langkah 7 — Hitung NPV (cuma 2 rumus)")
p("NPV terdengar menakutkan, padahal gunanya hanya menjawab: setelah tiga tahun, apakah uang yang "
  "kembali lebih banyak daripada modal yang keluar?")
formula("Arus kas bersih = manfaat per tahun - biaya operasional per tahun")
formula("NPV = -modal awal + (arus kas bersih x 2,4018)")
p("Angka 2,4018 adalah faktor pengali untuk tiga tahun dengan diskonto 12%. Anda tidak perlu "
  "menghitungnya; cukup pakai angka itu dan sebutkan alasannya.")
p("Contoh lengkap Alternatif 3:", space_after=3)
formula("Manfaat Rp247.728.000 - biaya operasional Rp99.000.000 = Rp148.728.000")
formula("NPV = -Rp125.000.000 + (Rp148.728.000 x 2,4018)")
formula("NPV = -Rp125.000.000 + Rp357.219.561 = Rp232.219.561   -> layak")
formula("Payback = Rp125.000.000 : Rp148.728.000 x 12 = 10,1 bulan")
table(["Indikator", "A1 Prosedur", "A2 Aplikasi", "A3 Bertahap"],
      [["Modal awal", "Rp25.000.000", "Rp115.000.000", "Rp125.000.000"],
       ["Biaya operasional/tahun", "Rp24.000.000", "Rp93.000.000", "Rp99.000.000"],
       ["Manfaat/tahun", "Rp113.040.000", "Rp211.680.000", "Rp247.728.000"],
       ["Arus kas bersih/tahun", "Rp89.040.000", "Rp118.680.000", "Rp148.728.000"],
       ["NPV tiga tahun", "Rp188.859.056", "Rp170.049.335", "Rp232.219.561"],
       ["Payback", "3,4 bulan", "11,6 bulan", "10,1 bulan"]],
      widths=[4.4, 3.9, 3.9, 4.2],
      caption="Tabel 6. Hasil perhitungan ketiga alternatif",
      center=[1, 2, 3])
box("Tiga kesalahan hitung yang paling sering",
    "Pertama, memakai manfaat kotor tanpa mengurangi biaya operasional. Kedua, memasukkan modal ke "
    "dalam arus kas tahunan. Ketiga, mengalikan arus kas dengan 3 (jumlah tahun) alih-alih 2,4018. "
    "Periksa ketiganya sebelum menulis.",
    fill="FBEEEE", accent=RED)

# ---------------------------------------------------------------- 8
h1("Langkah 8 — Beri skor dan pilih")
p("NPV tertinggi belum tentu bisa dijalankan, dan skor tertinggi belum tentu layak secara uang. "
  "Karena itu perlu penilaian kedua: beri skor 1–5 pada lima kriteria, lalu kalikan dengan bobotnya.")
table(["Kriteria", "Bobot", "A1", "A2", "A3"],
      [["K1 Menurunkan jarak dan biaya", "30%", "2 (0,60)", "4 (1,20)", "4 (1,20)"],
       ["K2 Meningkatkan layanan", "25%", "2 (0,50)", "4 (1,00)", "4 (1,00)"],
       ["K3 Tidak melebihi pagu", "20%", "5 (1,00)", "3 (0,60)", "4 (0,80)"],
       ["K4 Selesai dalam 90 hari", "15%", "5 (0,75)", "4 (0,60)", "3 (0,45)"],
       ["K5 Fleksibel dan diterima", "10%", "4 (0,40)", "3 (0,30)", "4 (0,40)"],
       ["Skor akhir", "100%", "3,25", "3,70", "3,85"],
       ["Peringkat", "", "3", "2", "1"]],
      widths=[6.6, 1.8, 2.6, 2.6, 2.8],
      caption="Tabel 7. Skor terbobot",
      center=[1, 2, 3, 4],
      note="Angka dalam kurung adalah bobot x skor. Jumlahkan untuk mendapat skor akhir.")

p("Cara menghitung satu baris, contoh A1:", space_after=3)
formula("(0,30 x 2) + (0,25 x 2) + (0,20 x 5) + (0,15 x 5) + (0,10 x 4)")
formula("= 0,60 + 0,50 + 1,00 + 0,75 + 0,40 = 3,25")
p("Alternatif 3 menang karena satu-satunya yang cukup baik pada hasil maupun pelaksanaan. Tulis juga "
  "alasan mengapa bukan yang lain: Alternatif 1 cepat balik modal tetapi manfaatnya hanya 45,6% dari "
  "Alternatif 3; Alternatif 2 mahal untuk manfaat yang diperoleh.")

# ---------------------------------------------------------------- 9
h1("Langkah 9 — Tulis dan rapikan")
p("Sekarang semua bahan sudah ada, jadi menulis jadi cepat. Urutan yang paling hemat waktu:")
num("Tulis Bab III dan IV lebih dulu, karena semua angka ada di situ.")
num("Tulis Bab II, menyesuaikan teori pada temuan Anda.")
num("Tulis Bab V (rencana, risiko, KPI), karena isinya tabel.")
num("Tulis Bab I dan Ringkasan paling akhir, karena keduanya merangkum.")
num("Sampul dan Daftar Pustaka terakhir, lalu format seluruh dokumen sekaligus.")
h2("Format dalam enam klik")
num("Ctrl+A untuk memilih semua.")
num("Ubah font ke Times New Roman, ukuran 12.")
num("Paragraph > Line spacing 1,5.")
num("Ctrl+J untuk rata kiri-kanan.")
num("Layout > Margins > Normal (2,54 cm), lalu Layout > Size > A4.")
num("Tandai tiap judul bab sebagai Heading 1 agar bisa dibuat daftar isi otomatis.")
p("Penomoran tabel memakai nomor bab: Tabel 2.2 berarti tabel kedua di Bab II. Judul tabel di atas "
  "tabel, judul gambar di bawah gambar. Setiap tabel harus dijelaskan dalam kalimat, jangan berdiri "
  "sendiri.")

# ---------------------------------------------------------------- 10
h1("Langkah 10 — Periksa sebelum mengumpulkan")
table(["", "Yang diperiksa"],
      [["1", "Sampul lengkap: judul, nama, NIM, kelas, mata kuliah, dosen, prodi, tahun"],
       ["2", "Ketujuh hal yang diminta tugas ada semua"],
       ["3", "Bab I–VI lengkap, subbab tidak ada yang melompat"],
       ["4", "A4, Times New Roman 12, spasi 1,5, margin 2,54, rata kiri-kanan"],
       ["5", "Isi 5–8 halaman (dihitung dari Bab I sampai Bab VI)"],
       ["6", "Bobot kriteria berjumlah 100%"],
       ["7", "Ada penjelasan arti skor 1–5 dan contoh perhitungan skor akhir"],
       ["8", "Setiap tabel dan gambar bernomor, berjudul, dan dijelaskan"],
       ["9", "Asumsi diberi kode dan alasannya"],
       ["10", "Setiap angka bisa Anda jelaskan asalnya kalau ditanya"]],
      widths=[1.0, 15.4],
      caption="Tabel 8. Daftar centang",
      center=[0])

h1("Kalau ditanya dosen")
table(["Pertanyaan", "Jawaban singkat yang benar"],
      [["“Angka 5% keterlambatan dari mana?”", "Itu asumsi A3, karena kasus tidak menyediakan. Saya pakai kisaran umum, dan pada Fase 0 akan diganti hasil pengukuran. Pada uji sensitivitas, perubahan angka ini tidak mengubah kesimpulan."],
       ["“Kenapa tidak pilih aplikasi terintegrasi sekalian?”", "Modalnya Rp330 juta, melewati pagu Rp150 juta, butuh lebih dari 90 hari, dan NPV-nya negatif."],
       ["“Kenapa bukan Alternatif 1 saja, kan paling cepat?”", "Manfaatnya hanya 45,6% dari Alternatif 3. Alternatif 1 tetap dikerjakan, tetapi sebagai tahap pertama, bukan pilihan akhir."],
       ["“Buktinya manfaat ini nyata?”", "Belum terbukti, karena itu ada uji coba 5 kendaraan dengan 15 pembanding, dan keputusan lanjut diambil hanya bila jarak turun minimal 5%."],
       ["“Kenapa NPV dianggap layak?”", "NPV positif Rp232 juta, payback 10 bulan, dan tetap positif pada skenario pesimistis Rp47 juta."]],
      widths=[4.6, 11.8],
      caption="Tabel 9. Lima pertanyaan yang sering muncul")

h1("Istilah yang perlu Anda tahu")
table(["Istilah", "Arti sederhana"],
      [["Baseline", "Kondisi awal sebelum perbaikan; pembanding untuk mengukur keberhasilan"],
       ["Capex", "Uang yang keluar sekali di awal, misalnya lisensi dan perangkat"],
       ["Opex", "Uang yang keluar berulang tiap tahun, misalnya langganan"],
       ["NPV", "Nilai sekarang bersih; positif berarti investasi menghasilkan lebih dari modalnya"],
       ["Payback", "Berapa lama modal kembali"],
       ["PVIFA", "Angka pengali untuk menghitung nilai uang tiga tahun ke depan (2,4018 untuk 12%, 3 tahun)"],
       ["OTIF", "Kiriman tiba tepat waktu sekaligus lengkap"],
       ["ETA", "Perkiraan jam kedatangan yang disampaikan ke pelanggan"],
       ["Gate", "Titik keputusan; fase berikutnya hanya jalan bila syaratnya terpenuhi"],
       ["Tacit", "Pengetahuan yang masih di kepala orang, belum jadi data atau prosedur"]],
      widths=[3.0, 13.4],
      caption="Tabel 10. Glosarium mini",
      size=9)

box("Satu nasihat terakhir",
    "Kerjakan perhitungannya sendiri dengan kalkulator, walaupun lambat. Saat angka itu Anda hitung "
    "sendiri, Anda akan ingat asalnya. Itu yang membuat Anda bisa menjawab saat ditanya, dan itu yang "
    "membedakan nilai A dari nilai B.",
    fill="F0F4FA")

cp = doc.core_properties
cp.title = "Panduan Ringkas Mengerjakan Studi Kasus 4"
cp.subject = "Panduan sepuluh langkah untuk mahasiswa baru"
cp.author = "Panduan Studi Kasus"
cp.language = "id-ID"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print("tersimpan:", os.path.abspath(OUT))
print("tabel:", len(doc.tables))
