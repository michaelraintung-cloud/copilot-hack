"""Laporan Studi Kasus 4 — VERSI SEDERHANA.

Dirancang untuk mahasiswa baru: 3 alternatif, 9 tabel, bahasa lugas,
isi 5-8 halaman sesuai ketentuan (tanpa daftar isi, karena tidak diwajibkan).

Jalankan: python3 build_sederhana.py
Keluaran: ../output/Laporan-Case-4-Sederhana.docx
"""
import os

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output", "Laporan-Case-4-Sederhana.docx")

NAVY = RGBColor(0x1F, 0x38, 0x64)
DARK = RGBColor(0x00, 0x00, 0x00)
GREY = RGBColor(0x59, 0x59, 0x59)
FONT = "Times New Roman"
USABLE = 15.92  # cm

doc = Document()

# ---------------------------------------------------------------- halaman
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
for side in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
    setattr(sec, side, Cm(2.54))
sec.header_distance = Cm(1.25)
sec.footer_distance = Cm(1.25)


def _page_number():
    """Nomor halaman di tengah bawah, memakai field PAGE."""
    par = sec.footer.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = par.add_run()
    fld = OxmlElement("w:fldChar")
    fld.set(qn("w:fldCharType"), "begin")
    run._r.append(fld)
    run2 = par.add_run()
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    run2._r.append(instr)
    run3 = par.add_run()
    sep = OxmlElement("w:fldChar")
    sep.set(qn("w:fldCharType"), "separate")
    run3._r.append(sep)
    run4 = par.add_run("1")
    run5 = par.add_run()
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run5._r.append(end)
    for r in (run, run2, run3, run4, run5):
        r.font.name = FONT
        r.font.size = Pt(10)


# ---------------------------------------------------------------- gaya
normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(12)
normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
pf = normal.paragraph_format
pf.line_spacing = 1.5
pf.space_before = Pt(0)
pf.space_after = Pt(0)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

for name, size in (("Heading 1", 14), ("Heading 2", 12), ("Heading 3", 12)):
    st = doc.styles[name]
    st.font.name = FONT
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = NAVY if name == "Heading 1" else DARK
    st.font.italic = False
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    sp = st.paragraph_format
    sp.line_spacing = 1.5
    sp.space_before = Pt(8 if name == "Heading 1" else 7)
    sp.space_after = Pt(2 if name == "Heading 1" else 1)
    sp.keep_with_next = True
    sp.alignment = WD_ALIGN_PARAGRAPH.LEFT


def h1(text):
    return doc.add_paragraph(text, style="Heading 1")


def h2(text):
    return doc.add_paragraph(text, style="Heading 2")


def p(text, bold_lead=None, first_indent=1.0, space_after=0, align=None):
    par = doc.add_paragraph()
    par.paragraph_format.first_line_indent = Cm(first_indent)
    par.paragraph_format.space_after = Pt(space_after)
    par.alignment = align or WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_lead:
        r = par.add_run(bold_lead)
        r.font.bold = True
        r.font.name = FONT
        r.font.size = Pt(12)
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(12)
    return par


def num(text, bold_lead=None):
    par = doc.add_paragraph(style="List Number")
    par.paragraph_format.left_indent = Cm(1.2)
    par.paragraph_format.first_line_indent = Cm(-0.6)
    par.paragraph_format.space_after = Pt(2)
    par.paragraph_format.line_spacing = 1.5
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_lead:
        r = par.add_run(bold_lead)
        r.font.bold = True
        r.font.name = FONT
        r.font.size = Pt(12)
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(12)
    return par


def center(text, size=12, bold=False, color=None, space_after=0, italic=False):
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    par.paragraph_format.space_after = Pt(space_after)
    par.paragraph_format.line_spacing = 1.5
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.color.rgb = color or DARK
    return par


def width_of(table, widths):
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblLayout")):
        tblPr.remove(old)
    lay = OxmlElement("w:tblLayout")
    lay.set(qn("w:type"), "fixed")
    tblPr.append(lay)
    for row in table.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)


def table(caption, headers, rows, widths, center_cols=None, note=None, size=10):
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(5)
    cap.paragraph_format.space_after = Pt(1)
    cap.paragraph_format.keep_with_next = True
    cap.paragraph_format.line_spacing = 1.0
    r = cap.add_run(caption)
    r.font.name = FONT
    r.font.size = Pt(10)
    r.font.bold = True

    tbl = doc.add_table(rows=1, cols=len(headers))
    tbl.style = "Table Grid"
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = tbl.rows[0]
    for i, htxt in enumerate(headers):
        cell = hdr.cells[i]
        cell._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), "1F3864")
        cell._tc.get_or_add_tcPr().append(shd)
        par = cell.paragraphs[0]
        par.paragraph_format.space_after = Pt(1)
        par.paragraph_format.space_before = Pt(1)
        par.paragraph_format.line_spacing = 1.0
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        rr = par.add_run(htxt)
        rr.font.name = FONT
        rr.font.size = Pt(size)
        rr.font.bold = True
        rr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for row in rows:
        cells = tbl.add_row().cells
        for i, val in enumerate(row):
            par = cells[i].paragraphs[0]
            par.paragraph_format.space_after = Pt(1)
            par.paragraph_format.space_before = Pt(1)
            par.paragraph_format.line_spacing = 1.0
            par.alignment = (WD_ALIGN_PARAGRAPH.CENTER if center_cols and i in center_cols
                             else WD_ALIGN_PARAGRAPH.LEFT)
            rr = par.add_run(str(val))
            rr.font.name = FONT
            rr.font.size = Pt(size)

    width_of(tbl, widths)

    if note:
        np_ = doc.add_paragraph()
        np_.paragraph_format.space_before = Pt(1)
        np_.paragraph_format.space_after = Pt(4)
        np_.paragraph_format.line_spacing = 1.0
        rr = np_.add_run(note)
        rr.font.name = FONT
        rr.font.size = Pt(9)
        rr.font.italic = True
        rr.font.color.rgb = GREY
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)


def highlight(text, fill="EEF3FA"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    cell._tc.get_or_add_tcPr().append(shd)
    par = cell.paragraphs[0]
    par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.space_before = Pt(3)
    par.paragraph_format.line_spacing = 1.3
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = par.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(11.5)
    width_of(tbl, [USABLE])
    doc.add_paragraph().paragraph_format.space_after = Pt(1)


def formula(text):
    par = doc.add_paragraph()
    par.paragraph_format.left_indent = Cm(1.0)
    par.paragraph_format.space_after = Pt(1)
    par.paragraph_format.line_spacing = 1.2
    par.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = par.add_run(text)
    r.font.name = "Consolas"
    r.font.size = Pt(9.5)
    return par


# ================================================================ SAMPUL
for _ in range(2):
    doc.add_paragraph()

center("LAPORAN STUDI KASUS", 12, True, GREY, 6)
center("MANAJEMEN INDUSTRI", 12, True, GREY, 30)

center("ARMADA BANYAK,", 22, True, NAVY, 0)
center("PENGIRIMAN TETAP TERLAMBAT", 22, True, NAVY, 14)

center("Analisis Efisiensi Distribusi dan Kualitas Layanan", 12, False, DARK, 0)
center("pada Perusahaan Distribusi Barang Konsumsi", 12, False, DARK, 0)
center("(Studi Kasus 4 — Supply Chain & Distribution)", 11, False, GREY, 40)

center("Disusun oleh:", 12, False, DARK, 4)
center("[Nama Mahasiswa]", 13, True, DARK, 0)
center("NIM: [....................]     Kelas: [....................]", 11, False, DARK, 30)

center("Mata Kuliah: Manajemen Industri", 11, False, DARK, 0)
center("Dosen Pengampu: [Nama Dosen Pengampu]", 11, False, DARK, 44)

center("PROGRAM STUDI [NAMA PROGRAM STUDI]", 12, True, DARK, 0)
center("FAKULTAS [NAMA FAKULTAS]", 12, True, DARK, 0)
center("UNIVERSITAS [NAMA UNIVERSITAS]", 12, True, DARK, 0)
center("TAHUN [20XX]", 12, True, DARK, 0)

doc.add_page_break()

# ================================================================ RINGKASAN
h1("RINGKASAN")
p("Perusahaan distribusi ini memiliki 20 kendaraan dengan jarak 150 km per kendaraan per hari, "
  "selama 26 hari setiap bulan. Rute diatur manual oleh dua dispatcher berdasarkan pengalaman, "
  "sehingga kendaraan sering melewati jalan yang sama, keterlambatan baru diketahui setelah "
  "pengemudi menelepon, dan pelanggan tidak tahu kapan barang tiba.")
p("Laporan ini menghitung kerugiannya, mencari penyebabnya, lalu membandingkan tiga cara "
  "memperbaiki. Kerugian mencapai Rp610,8 juta per tahun atau Rp12.236 per kiriman, terbesar dari "
  "keterlambatan (40,9%) dan waktu tunggu (25,1%), bukan bahan bakar (23,0%). Dari tiga alternatif, "
  "Alternatif 3 (perbaikan bertahap) memperoleh skor tertinggi 3,85 dari 5,00 dan NPV tertinggi "
  "Rp232,2 juta dengan modal Rp125 juta dari pagu Rp150 juta, dikerjakan 90 hari tanpa "
  "menghentikan operasional.")

highlight("Kata kunci: optimasi rute, keterlambatan, ETA, data toko, perbaikan bertahap")

# ================================================================ BAB I
h1("BAB I  PENDAHULUAN")

h2("1.1  Latar Belakang")
p("Perusahaan mengirim barang ke toko ritel dengan 20 kendaraan, jarak 150 km per kendaraan per hari "
  "dan 26 hari operasi per bulan (BPH, 2025). Rute disusun dua dispatcher secara manual, dan "
  "pengetahuan tentang jalan serta kebiasaan pelanggan hanya tersimpan di kepala mereka. Ketika "
  "pesanan naik, urutan pesanan masuk menjadi patokan, bukan kedekatan lokasi.")
p("Manajemen berniat membeli aplikasi, tetapi pengemudi menilai aplikasi tidak memahami kondisi "
  "lapangan dan bagian keuangan meragukan apakah penghematan bahan bakar menutup biaya sistem. Karena "
  "itu laporan ini dimulai dari berapa kerugiannya dan apa syarat perbaikannya, bukan memilih "
  "aplikasi.")

h2("1.2  Identifikasi Masalah")
p("Kasus memperlihatkan lima gejala: urutan kunjungan tidak mengikuti kedekatan lokasi; keterlambatan "
  "diketahui hanya setelah pengemudi menelepon; tidak ada janji waktu tiba; kapasitas perencanaan "
  "hanya dua orang; dan tidak ada catatan jarak, waktu, serta ketepatan waktu. Semuanya bermuara pada "
  "satu hal:", space_after=3)
highlight("Masalah utama: perusahaan belum memiliki sistem perencanaan dan pengendalian distribusi "
          "yang mengubah pengetahuan rute di kepala dispatcher menjadi aturan kerja dan data. "
          "Akibatnya kendaraan menempuh jarak yang tidak perlu, dan janji waktu tiba tidak dapat "
          "dipenuhi maupun disampaikan kepada pelanggan.")
p("Masalahnya bukan jumlah kendaraan: 20 kendaraan untuk delapan titik per kendaraan setiap hari "
  "sudah memadai, yang kurang adalah mutu keputusan dalam menyusun rute.")

h2("1.3  Rumusan Masalah")
num("Apa penyebab utama keterlambatan dan pemborosan jarak tempuh?")
num("Berapa besar kerugiannya, dan komponen biaya mana yang terbesar?")
num("Alternatif mana yang paling tepat, dan bagaimana menjalankannya dalam 90 hari?")

h2("1.4  Tujuan Analisis")
num("Menemukan masalah utama dan penyebabnya.")
num("Menghitung kerugian per tahun dengan asumsi yang dinyatakan terbuka.")
num("Membandingkan tiga alternatif solusi dan memilih yang terbaik.")
num("Menyusun rencana 90 hari, daftar risiko, dan indikator keberhasilan.")

h2("1.5  Ruang Lingkup dan Batasan")
p("Cakupan: perencanaan rute, pelaksanaan pengiriman, dan pelaporan, dengan objek 20 kendaraan dan "
  "26 hari operasi per bulan; di luar cakupan pembelian kendaraan, operasi gudang, dan penetapan "
  "harga. Kasus tidak menyebutkan jumlah titik per kendaraan, tingkat keterlambatan, biaya per "
  "kejadian terlambat, maupun biaya dispatcher; nilai itu ditetapkan sebagai asumsi A1–A5 "
  "(Lampiran 2) dan diganti hasil pengukuran pada minggu pertama (Lampiran 3).")

# ================================================================ BAB II
h1("BAB II  LANDASAN TEORI")

h2("2.1  Kajian Teori")
p("Penentuan rute kendaraan dirumuskan Dantzig dan Ramser (1959): dari satu gudang, setiap pelanggan "
  "dikunjungi tepat sekali dengan biaya sekecil mungkin. Karena kemungkinan urutannya sangat banyak, "
  "dipakai cara pintar untuk mendekati hasil terbaik (Braekers dkk., 2016). Manfaatnya datang dari "
  "mengelompokkan pelanggan berdekatan lalu mengurutkan kunjungan di dalam kelompok; rute yang "
  "mengikuti urutan pesanan gagal pada keduanya. UPS menerapkannya lewat ORION dan menghemat lebih "
  "dari 300 juta dolar AS per tahun, bukan karena algoritmanya canggih melainkan karena datanya "
  "terhubung (Holland dkk., 2017).")
p("Kualitas layanan diukur dengan OTIF, yaitu persentase kiriman yang tiba tepat waktu sekaligus "
  "lengkap (Christopher, 2016), dan dilengkapi akurasi ETA. Pemborosan yang paling relevan adalah "
  "transportasi dan waktu tunggu (Ohno, 1988). Membeli aplikasi saja tidak cukup karena pengetahuan "
  "dispatcher bersifat tacit (Polanyi, 1966), sedangkan perbaikan proses harus dimulai dari standar "
  "kerja, bukan alatnya (Spear & Bowen, 1999). Kelayakan uang dinilai dengan NPV dan payback.")

h2("2.2  Penelitian yang Relevan (Identifikasi Fakta dan Data Kasus)")
p("Fakta kasus sejalan dengan literatur: ini masalah perencanaan, bukan pemilihan jalan (Dantzig & "
  "Ramser, 1959; Braekers dkk., 2016); manfaat optimasi hanya muncul bila data terintegrasi, "
  "sedangkan data toko belum rapi (Holland dkk., 2017); dan teknologi gagal bila standar kerja serta "
  "penerimaan pengemudi belum siap (Spear & Bowen, 1999). Karena itu data kasus dan asumsi "
  "dipisahkan (Lampiran 2).")

h2("2.3  Kerangka Berpikir (Gambaran Proses Operasional Saat Ini)")
p("Proses berjalan dalam delapan langkah dengan lima titik kegagalan: urutan mengikuti pesanan masuk, "
  "posisi kendaraan tidak diketahui, keterlambatan tidak terdeteksi, pelanggan tanpa perkiraan waktu, "
  "dan tidak ada data yang kembali untuk perencanaan besok. Karena itu perbaikan disusun berlapis: "
  "rapikan aturan kerja dan data toko, pasang sistem, lalu tingkatkan kemampuan orang.")

h2("2.4  Dampak Permasalahan")
p("Dua puluh kendaraan dikali 150 km adalah 3.000 km per hari atau 936.000 km per tahun. Dengan "
  "konsumsi 10 km per liter, bahan bakar yang dibutuhkan 93.600 liter atau Rp936 juta setahun. "
  "Delapan titik per kendaraan berarti 49.920 kiriman per tahun, sehingga satu kiriman menempuh 18,75 "
  "km. Kerugian setiap tahun dihitung pada Tabel 2.1.")

table("Tabel 2.1  Kerugian akibat Masalah per Tahun",
      ["Komponen", "Cara menghitung", "Nilai", "Porsi"],
      [["Bahan bakar berlebih", "15% x 936.000 km : 10 x Rp10.000", "Rp140.400.000", "23,0%"],
       ["Keterlambatan", "5% x 49.920 kiriman x Rp100.000", "Rp249.600.000", "40,9%"],
       ["Waktu tunggu", "12,8 jam/hari x Rp38.462 x 312 hari", "Rp153.600.000", "25,1%"],
       ["Perencanaan manual", "40% x 2 orang x Rp7.000.000 x 12", "Rp67.200.000", "11,0%"],
       ["Jumlah", "", "Rp610.800.000", "100%"]],
      widths=[4.0, 6.9, 3.3, 1.7],
      center_cols=[2, 3],
      note="Sumber: perhitungan penulis. Setara Rp12.236 per kiriman atau 65,3% dari belanja bahan bakar setahun.")

p("Bahan bakar hanya 23,0% dari kerugian, sedangkan keterlambatan dan waktu tunggu mencapai 66,0%. "
  "Penghematan bahan bakar 15% (Rp140,4 juta) karena itu tidak cukup membenarkan pembelian sistem. "
  "Dampak yang tidak dihitung: kepercayaan pelanggan menurun dan emisi bertambah 37,6 ton CO2e per "
  "tahun.")

# ================================================================ BAB III
h1("BAB III  ANALISIS MASALAH")

h2("3.1  Penentuan Masalah Utama")
p("Bila setiap gejala diperbaiki sendiri, masalahnya tidak hilang: menambah kendaraan hanya menambah "
  "kendaraan yang menempuh rute tidak efisien; menegur atau menambah dispatcher tidak mengubah mutu "
  "keputusan; dan dashboard di atas data yang belum rapi hanya memindahkan masalah. Yang gagal karena "
  "itu lapisan informasi dan keputusan.")

h2("3.2  Analisis Akar Penyebab")
p("Penyebab ditelusuri dengan teknik lima mengapa, yaitu bertanya mengapa berulang sampai menemukan "
  "penyebab yang tidak bisa ditanyakan lagi (Tabel 3.1).")

table("Tabel 3.1  Lima Mengapa",
      ["Ke", "Pertanyaan", "Jawaban"],
      [["1", "Mengapa kendaraan menempuh jarak tidak perlu?", "Urutan kunjungan tidak mengikuti kedekatan lokasi"],
       ["2", "Mengapa urutannya begitu?", "Rute disusun manual mengikuti urutan pesanan masuk"],
       ["3", "Mengapa masih manual?", "Tidak ada alat dan standar pengelompokan wilayah; perencana hanya dua orang"],
       ["4", "Mengapa tidak ada alat dan standar?", "Pengetahuan rute hanya di kepala orang, belum menjadi data atau prosedur"],
       ["5", "Mengapa belum menjadi data?", "Tidak ada KPI jarak, waktu, dan ketepatan waktu, sehingga tidak ada dorongan untuk memperbaiki"]],
      widths=[1.0, 6.2, 8.7],
      center_cols=[0],
      note="Sumber: analisis penulis. Baris kelima adalah akar penyebab.")

p("Akar penyebabnya sistemik, bukan kesalahan orang, sehingga sanksi tidak akan bekerja. Yang "
  "dibutuhkan adalah perubahan cara kerja: ada standar, ada data, ada ukuran, lalu ada alat bantu.")

h2("3.3  Kebutuhan Perbaikan")
p("Dari akar penyebab itu disusun lima syarat yang harus dipenuhi solusi apa pun, dan syarat ini "
  "dipakai untuk menilai alternatif pada Bab IV.", space_after=4)
num("Urutan kunjungan mempertimbangkan jarak, kapasitas muatan, dan jam penerimaan toko.")
num("Data toko tersimpan rapi di satu tempat dan sudah divalidasi.")
num("Posisi kendaraan bisa dilihat, dan pelanggan menerima perkiraan waktu tiba.")
num("Dispatcher boleh menimpa usulan sistem, asalkan alasannya dicatat.")
num("Pelaksanaan bertahap, tidak menghentikan operasional, dan tidak lebih dari Rp150 juta.")

h2("3.4  Asumsi dan Keterbatasan Data")
p("Lima asumsi terpenting adalah 312 hari operasi, 8 titik per kendaraan, 5% kiriman terlambat, "
  "Rp100.000 per kejadian, dan diskonto 12%, semuanya berkode A1–A5 pada Lampiran 2. Tiga "
  "keterbatasan: denda dan kehilangan pelanggan belum dihitung sehingga Rp610,8 juta adalah batas "
  "bawah; manfaat belum terbukti sebab-akibat sehingga perlu diuji antar kelompok; dan model rute "
  "belum dikalibrasi karena koordinat toko belum tersedia.")

# ================================================================ BAB IV
h1("BAB IV  HASIL DAN PEMBAHASAN")

h2("4.1  Alternatif Solusi")
p("Tiga alternatif disusun berjenjang, dari yang paling murah sampai yang paling lengkap "
  "(Tabel 4.1).")

table("Tabel 4.1  Tiga Alternatif Solusi",
      ["Alternatif", "Isi", "Kelebihan", "Kekurangan"],
      [["A1 Perbaikan prosedur", "Bagi wilayah menjadi zona, buat SOP rute, rapikan data toko di spreadsheet, tetapkan KPI. Tanpa perangkat berbayar.", "Murah, cepat, tidak butuh vendor", "Perencana tetap dua orang; posisi kendaraan tidak terlihat"],
       ["A2 Aplikasi optimasi rute", "Langganan aplikasi optimasi 20 kendaraan, ditambah aplikasi pengemudi untuk bukti pengiriman dan waktu tiba.", "Rute tersusun otomatis; waktu tiba tercatat", "Data lokal belum ada; biaya langganan besar"],
       ["A3 Perbaikan bertahap", "Rapikan aturan dan data lebih dulu (30 hari), pasang aplikasi berisi data lokal, lalu tambahkan pelacakan posisi dan ETA.", "Memenuhi kelima syarat; modal terkendali", "Butuh disiplin menjalankan bertahap"]],
      widths=[3.0, 6.3, 3.2, 3.4],
      size=9.5,
      note="Sumber: rancangan penulis.")

p("Alternatif 3 menggabungkan Alternatif 1 dan 2 secara berurutan. Tiga hal membedakannya dari "
  "sekadar membeli aplikasi: dispatcher tetap boleh menimpa usulan sistem dengan alasan dicatat; "
  "wilayah dibagi menjadi zona tetap agar pengemudi tetap mengenal pelanggannya; dan kondisi awal "
  "diukur lebih dulu agar manfaat bisa dibuktikan.")

h2("4.2  Penentuan Kriteria Evaluasi")
p("Penilaian memakai lima kriteria berbobot berbeda (Tabel 4.2). Skor 1–5 berarti: 5 = memenuhi "
  "seluruh aspek; 4 = ada kekurangan kecil; 3 = butuh pekerjaan tambahan; 2 = hanya sebagian kecil; "
  "1 = tidak memenuhi atau melanggar batasan.")

table("Tabel 4.2  Kriteria dan Bobot Penilaian",
      ["Kode", "Kriteria", "Bobot", "Alasan"],
      [["K1", "Menurunkan jarak dan biaya", "30%", "Kasus menetapkan target pengurangan jarak 15%, jadi ini tujuan utama"],
       ["K2", "Meningkatkan layanan (OTIF dan ETA)", "25%", "Keluhan pelanggan paling terasa di sini"],
       ["K3", "Tidak melebihi pagu Rp150 juta", "20%", "Batas anggaran mengikat"],
       ["K4", "Selesai dalam 90 hari", "15%", "Operasional tidak boleh berhenti"],
       ["K5", "Fleksibel dan diterima pengemudi", "10%", "Keberatan pengemudi harus diakomodasi"],
       ["", "Jumlah", "100%", ""]],
      widths=[1.2, 5.2, 1.6, 7.9],
      center_cols=[0, 2],
      note="Sumber: penulis.")

h2("4.3  Perbandingan Alternatif Solusi")
p("Perbandingan dilakukan dua cara: kelayakan uang lalu skor multikriteria, dengan PVIFA 12% selama "
  "tiga tahun sebesar 2,4018:", space_after=3)
formula("Arus kas bersih = manfaat per tahun - biaya operasional per tahun")
formula("NPV = -modal awal + (arus kas bersih x 2,4018)")
formula("Payback (bulan) = modal awal : arus kas bersih x 12")
p("Contoh Alternatif 3: manfaat Rp247,7 juta dikurangi biaya operasional Rp99 juta = Rp148,7 juta. "
  "NPV = -125 + (148,7 x 2,4018) = Rp232,2 juta; payback = 125 : 148,7 x 12 = 10,1 bulan.")

table("Tabel 4.3  Perbandingan Kelayakan Uang",
      ["Indikator", "A1 Prosedur", "A2 Aplikasi", "A3 Bertahap"],
      [["Modal awal", "Rp25.000.000", "Rp115.000.000", "Rp125.000.000"],
       ["Biaya operasional per tahun", "Rp24.000.000", "Rp93.000.000", "Rp99.000.000"],
       ["Manfaat per tahun", "Rp113.040.000", "Rp211.680.000", "Rp247.728.000"],
       ["Arus kas bersih per tahun", "Rp89.040.000", "Rp118.680.000", "Rp148.728.000"],
       ["NPV tiga tahun", "Rp188.859.056", "Rp170.049.335", "Rp232.219.561"],
       ["Payback", "3,4 bulan", "11,6 bulan", "10,1 bulan"],
       ["Kesimpulan", "Layak, manfaat kecil", "Layak", "Layak, NPV tertinggi"]],
      widths=[4.6, 3.7, 3.7, 3.9],
      center_cols=[1, 2, 3],
      note="Sumber: perhitungan penulis. Rincian biaya Alternatif 3 pada Lampiran 1.")

p("Alternatif 1 paling cepat balik modal tetapi manfaatnya hanya 45,6% dari Alternatif 3; Alternatif "
  "2 punya NPV terendah karena langganan mahal; Alternatif 3 memberi NPV tertinggi dengan modal 83,3% "
  "dari pagu. Berikutnya setiap alternatif diberi skor; skor akhir = jumlah bobot x skor, misalnya A1 "
  "= (0,30 x 2) + (0,25 x 2) + (0,20 x 5) + (0,15 x 5) + (0,10 x 4) = 3,25.")

table("Tabel 4.4  Penilaian Skor Terbobot",
      ["Kriteria", "Bobot", "A1", "A2", "A3"],
      [["K1 Menurunkan jarak dan biaya", "30%", "2  (0,60)", "4  (1,20)", "4  (1,20)"],
       ["K2 Meningkatkan layanan", "25%", "2  (0,50)", "4  (1,00)", "4  (1,00)"],
       ["K3 Tidak melebihi pagu", "20%", "5  (1,00)", "3  (0,60)", "4  (0,80)"],
       ["K4 Selesai dalam 90 hari", "15%", "5  (0,75)", "4  (0,60)", "3  (0,45)"],
       ["K5 Fleksibel dan diterima", "10%", "4  (0,40)", "3  (0,30)", "4  (0,40)"],
       ["Skor akhir", "100%", "3,25", "3,70", "3,85"],
       ["Peringkat", "", "3", "2", "1"]],
      widths=[6.4, 1.8, 2.6, 2.6, 2.5],
      center_cols=[1, 2, 3, 4],
      note="Sumber: perhitungan penulis. Angka dalam kurung adalah bobot dikali skor.")

p("Alternatif 1 unggul pada pelaksanaan tetapi lemah pada hasil; Alternatif 2 seimbang tetapi mahal; "
  "Alternatif 3 satu-satunya yang baik pada keduanya. Karena sebagian angka berasal dari asumsi, "
  "hasilnya diuji dengan analisis sensitivitas: bila manfaat hanya terealisasi 61% dari perkiraan, NPV "
  "menjadi nol, dan pada skenario pesimistis pun NPV masih positif Rp47,0 juta.")

h2("4.4  Pemilihan Solusi Terbaik dan Justifikasi")
p("Alternatif 3 dipilih dengan empat alasan:", space_after=4)
num("NPV tertinggi Rp232,2 juta, arus kas bersih Rp148,7 juta per tahun, payback 10,1 bulan.")
num("Modal Rp125 juta masih di bawah pagu Rp150 juta, menyisakan Rp25 juta untuk penyesuaian.")
num("Selesai 90 hari tanpa menghentikan operasional, karena tiap tahap berjalan bersamaan dengan pekerjaan harian.")
num("Menjawab kedua keberatan: pengemudi tetap boleh menimpa usulan sistem, dan manfaat dibuktikan lewat perbandingan lima kendaraan uji dengan lima belas kendaraan pembanding.")

p("Yang dipilih bukan perangkatnya, melainkan urutan pelaksanaannya. Pada 12 bulan pertama "
  "diharapkan jarak per kendaraan turun menjadi 130,5 km per hari, keterlambatan turun 30%, dan OTIF "
  "mencapai 95%.")

# ================================================================ BAB V
h1("BAB V  PENUTUP")

h2("5.1  Tahapan Implementasi")
p("Rencana 90 hari dibagi empat fase. Setiap fase diakhiri titik keputusan (gate): bila syaratnya "
  "tidak terpenuhi, fase berikutnya tidak dijalankan (Tabel 5.1).")

table("Tabel 5.1  Fase Pelaksanaan 90 Hari",
      ["Fase", "Hari", "Kegiatan", "Syarat untuk lanjut"],
      [["0", "1–14", "Ukur jarak, waktu tiba, lama bongkar muat, dan penyebab keterlambatan; rapikan data toko", "95% toko berdata lengkap; angka awal tiga KPI tersedia"],
       ["1", "15–45", "Bagi zona wilayah, buat SOP rute, tetapkan KPI, pasang aplikasi, latih dispatcher", "Usulan rute 20 kendaraan berjalan; dispatcher bisa mandiri"],
       ["2", "46–70", "Uji coba 5 kendaraan; 15 kendaraan lain sebagai pembanding", "Jarak turun minimal 5% dibanding pembanding; OTIF tidak turun"],
       ["3", "71–90", "Pindah bertahap per wilayah, pasang dashboard KPI, serah terima", "KPI stabil dua minggu; pemilik proses sudah ditunjuk"]],
      widths=[1.1, 1.5, 7.4, 5.9],
      center_cols=[0, 1],
      size=9.5,
      note="Sumber: rancangan penulis. Hari dihitung sejak keputusan proyek diambil.")

p("Operasional tidak boleh berhenti, sehingga setiap fase berjalan bersamaan dengan pekerjaan harian; "
  "uji coba bukan sekadar uji teknis, melainkan cara membuktikan manfaat.")

h2("5.2  Kebutuhan Sumber Daya")
p("Modal Rp125 juta terdiri dari lisensi dan perangkat pengemudi Rp78 juta, implementasi dan "
  "konfigurasi data Rp25 juta, pelatihan Rp12 juta, serta pengukuran awal Rp10 juta; biaya "
  "operasional Rp99 juta per tahun terbesar untuk langganan perangkat lunak Rp60 juta (Lampiran 1). "
  "Tidak ada penambahan pegawai: dua dispatcher beralih menjadi pengawas pengecualian dan pengelola "
  "data toko.")

h2("5.3  Pembagian Tanggung Jawab")
p("Direktur operasional menetapkan target dan memutuskan kelanjutan proyek; manajer operasional "
  "bertanggung jawab atas pelaksanaan harian; dispatcher dan pengemudi menjadi pelaksana pengukuran "
  "awal, uji coba, dan operasi; tim TI menyediakan integrasi dasar; bagian keuangan memverifikasi "
  "manfaat pada bulan keenam dan keduabelas.")

h2("5.4  Identifikasi Risiko dan Mitigasi")
p("Risiko dinilai dengan skala kemungkinan (K) dan dampak (D) 1–5; skornya hasil kali keduanya "
  "(1–6 rendah, 8–12 sedang, 15–25 tinggi). Lima risiko utama disajikan pada Tabel 5.2.")

table("Tabel 5.2  Risiko Utama dan Cara Menanganinya",
      ["Kode", "Risiko", "Jenis", "K", "D", "Skor", "Penanganan"],
      [["R1", "Dispatcher kembali menyusun rute manual karena sistem dianggap kaku", "Operasional", "4", "5", "20", "Izinkan penimpaan resmi yang dicatat; target awal tidak menuntut kepatuhan 100%"],
       ["R2", "Pengemudi menolak karena khawatir diawasi", "Sosial", "4", "4", "16", "Jelaskan GPS untuk ETA dan keselamatan, bukan sanksi; libatkan sejak uji coba"],
       ["R3", "Data toko tidak lengkap saat mulai", "Teknologi", "3", "5", "15", "Syarat Fase 1 mengikat; validasi silang dengan pengemudi"],
       ["R4", "Data pelanggan dan posisi bocor", "Keamanan data", "3", "5", "15", "Hak akses per peran, enkripsi, batasi masa simpan"],
       ["R5", "Manfaat hilang karena kembali ke kebiasaan lama", "Operasional", "3", "4", "12", "KPI masuk penilaian kinerja; audit kepatuhan bulanan"]],
      widths=[1.0, 4.6, 2.0, 0.7, 0.7, 1.0, 5.9],
      center_cols=[0, 2, 3, 4, 5],
      size=8.5,
      note="Sumber: identifikasi penulis. Risiko berskor 15 ke atas dipantau setiap minggu.")

p("Dua dari tiga risiko tertinggi bersifat sosial dan keamanan data, sehingga anggaran pelatihan "
  "Rp12 juta bukan pelengkap melainkan penanganan risiko utama.")

h2("5.5  Indikator Keberhasilan (KPI)")
p("KPI disusun agar terukur dan jelas sumber datanya. Karena angka awal belum tersedia, kolom itu "
  "diisi “diukur pada Fase 0” (Tabel 5.3).")

table("Tabel 5.3  KPI dan Target",
      ["Kode", "KPI", "Angka awal", "Target 90 hari", "Target 12 bulan"],
      [["K1", "Jarak per kiriman", "18,75 km (perkiraan)", "turun 5%", "turun 13%"],
       ["K2", "OTIF (tepat waktu dan lengkap)", "diukur Fase 0", "tidak turun", "minimal 95%"],
       ["K3", "Tingkat keterlambatan", "diukur Fase 0", "turun 15%", "turun 30%"],
       ["K4", "Akurasi ETA", "belum ada ETA", "minimal 70%", "minimal 85%"],
       ["K5", "Waktu tunggu di lokasi", "diukur Fase 0", "turun 10%", "turun 18%"],
       ["K6", "Biaya per kiriman", "Rp112.500 (perkiraan)", "turun 4%", "turun 10%"]],
      widths=[1.2, 5.0, 3.7, 2.9, 3.1],
      center_cols=[0, 3, 4],
      size=9.5,
      note="Sumber: rancangan penulis. Angka perkiraan K1 dan K6 berasal dari Tabel 2.1.")

p("OTIF dan tingkat keterlambatan dipisah: OTIF mengukur kepuasan pelanggan, tingkat keterlambatan "
  "mengukur frekuensi kegagalan. Seluruh KPI dihitung dari data sistem, bukan rekap manual.")

# ================================================================ BAB VI
h1("BAB VI  KESIMPULAN DAN SARAN")

h2("6.1  Kesimpulan")
num("Masalah utama bukan kekurangan armada, melainkan tidak adanya sistem perencanaan dan pengendalian distribusi; pengetahuan rute masih di kepala orang dan belum menjadi aturan kerja maupun data.")
num("Kerugiannya Rp610,8 juta per tahun atau Rp12.236 per kiriman, terbesar dari keterlambatan (40,9%) dan waktu tunggu (25,1%), sedangkan bahan bakar hanya 23,0%.")
num("Alternatif 3 terpilih dengan skor 3,85 dari 5,00 dan NPV Rp232,2 juta, dengan modal Rp125 juta atau 83,3% dari pagu.")
num("Keunggulannya terletak pada urutan: rapikan aturan dan data lebih dulu, isi sistem dengan data lokal, dan biarkan dispatcher menimpa usulan sistem sambil mencatat alasannya.")

h2("6.2  Saran")
p("Untuk manajemen: jalankan Fase 0 sebelum memutuskan pembelian apa pun, tetapkan satu pemilik "
  "proses, dan gunakan hasil uji coba Fase 2 sebagai dasar keputusan integrasi penuh. Untuk tim "
  "operasional dan pengemudi: keterlibatan mereka menentukan karena data lapangan hanya bisa diperoleh "
  "dari pengalaman; catatan penimpaan rute bukan kritik melainkan masukan yang memperbaiki usulan "
  "berikutnya.")


# ================================================================ PUSTAKA
h1("DAFTAR PUSTAKA")
refs = [
    "BPH. (2025). Industrial technology challenge: Studi kasus manajemen industri [Dokumen studi kasus].",
    "Braekers, K., Ramaekers, K., & Van Nieuwenhuyse, I. (2016). The vehicle routing problem: State of the art classification and review. Computers & Industrial Engineering, 99, 300–313. https://doi.org/10.1016/j.cie.2015.12.007",
    "Christopher, M. (2016). Logistics & supply chain management (5th ed.). Pearson Education.",
    "Dantzig, G. B., & Ramser, J. H. (1959). The truck dispatching problem. Management Science, 6(1), 80–91. https://doi.org/10.1287/mnsc.6.1.80",
    "Holland, C., Levis, J., Nuggehalli, R., Santilli, B., & Winters, J. (2017). UPS optimizes delivery routes. Interfaces, 47(1), 8–23. https://doi.org/10.1287/inte.2016.0875",
    "Ohno, T. (1988). Toyota production system: Beyond large-scale production. Productivity Press.",
    "Polanyi, M. (1966). The tacit dimension. Doubleday.",
    "Spear, S., & Bowen, H. K. (1999). Decoding the DNA of the Toyota Production System. Harvard Business Review, 77(5), 96–106.",
]
for ref in refs:
    par = doc.add_paragraph()
    par.paragraph_format.left_indent = Cm(1.0)
    par.paragraph_format.first_line_indent = Cm(-1.0)
    par.paragraph_format.space_after = Pt(3)
    par.paragraph_format.line_spacing = 1.15
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = par.add_run(ref)
    r.font.name = FONT
    r.font.size = Pt(11)

# ================================================================ LAMPIRAN
doc.add_page_break()
h1("LAMPIRAN")

h2("Lampiran 1  Rincian Perhitungan")
p("Seluruh angka pada laporan berasal dari perhitungan berikut, sehingga bisa diperiksa ulang.", space_after=3)
formula("Jarak harian      = 20 kendaraan x 150 km = 3.000 km")
formula("Jarak tahunan     = 3.000 km x 312 hari     = 936.000 km")
formula("Bahan bakar       = 936.000 km : 10        = 93.600 liter")
formula("Biaya bahan bakar = 93.600 x Rp10.000      = Rp936.000.000")
formula("Kiriman per hari  = 20 x 8 titik           = 160 kiriman")
formula("Kiriman per tahun = 160 x 312              = 49.920 kiriman")
formula("Jarak per kiriman = 936.000 : 49.920       = 18,75 km")
formula("Biaya per kiriman = Rp936.000.000 : 49.920 = Rp18.750 (bahan bakar saja)")

p("Perhitungan kerugian akibat masalah:", space_after=3)
formula("Bahan bakar berlebih = 15% x 93.600 liter x Rp10.000   = Rp140.400.000")
formula("Keterlambatan        = 5% x 49.920 x Rp100.000         = Rp249.600.000")
formula("Waktu tunggu         = 12,8 jam x Rp38.462 x 312 hari  = Rp153.600.000")
formula("Perencanaan manual   = 40% x 2 x Rp7.000.000 x 12      =  Rp67.200.000")
formula("Jumlah                                                 = Rp610.800.000")

p("Rincian modal dan biaya operasional Alternatif 3:", space_after=3)
table("Tabel L1.1  Rincian Biaya Alternatif 3",
      ["Modal awal", "Nilai", "Biaya operasional per tahun", "Nilai"],
      [["Lisensi aplikasi (20 kendaraan)", "Rp60.000.000", "Langganan perangkat lunak", "Rp60.000.000"],
       ["Implementasi dan konfigurasi data", "Rp25.000.000", "Kuota data dan komunikasi", "Rp14.000.000"],
       ["Perangkat pengemudi (12 unit)", "Rp18.000.000", "Pemeliharaan perangkat", "Rp10.000.000"],
       ["Pelatihan", "Rp12.000.000", "Administrasi dan analisis data", "Rp9.000.000"],
       ["Pengukuran awal", "Rp10.000.000", "Pelatihan penyegaran", "Rp6.000.000"],
       ["Jumlah", "Rp125.000.000", "Jumlah", "Rp99.000.000"]],
      widths=[5.4, 2.6, 5.2, 2.7],
      center_cols=[1, 3],
      size=9.5,
      note="Sumber: estimasi penulis; harga sebenarnya dikonfirmasi melalui penawaran vendor pada Fase 1.")

h2("Lampiran 2  Daftar Asumsi")
table("Tabel L2.1  Asumsi dan Alasannya",
      ["Kode", "Asumsi", "Nilai", "Alasan", "Bila berbeda"],
      [["A1", "Hari operasi per tahun", "312 hari", "26 hari per bulan x 12", "Semua angka tahunan berubah sebanding"],
       ["A2", "Titik per kendaraan per hari", "8 titik", "Kisaran lazim rute toko", "Jumlah kiriman dan biaya per kiriman berubah"],
       ["A3", "Tingkat keterlambatan", "5% kiriman", "Kisaran umum tanpa janji waktu", "Komponen biaya terbesar; wajib diukur"],
       ["A4", "Biaya per kejadian terlambat", "Rp100.000", "Komunikasi ulang dan potongan harga", "Manfaat keterlambatan berubah sebanding"],
       ["A5", "Tingkat diskonto", "12% per tahun", "Kisaran biaya modal perusahaan distribusi", "Mengubah NPV, tidak mengubah peringkat"]],
      widths=[1.1, 4.0, 2.3, 4.4, 4.1],
      center_cols=[0, 2],
      size=9,
      note="Sumber: penulis. Seluruh asumsi digantikan hasil pengukuran pada Fase 0.")

h2("Lampiran 3  Data yang Perlu Dikumpulkan")
p("Kasus tidak menyediakan seluruh data. Berikut data yang harus diambil pada Fase 0 beserta caranya.", space_after=3)
table("Tabel L3.1  Data dan Cara Mengumpulkannya",
      ["No", "Data", "Kegunaan", "Cara mengumpulkan"],
      [["1", "Koordinat dan akses toko", "Dasar menghitung jarak dan membagi zona", "Survei lapangan dan pencatatan GPS"],
       ["2", "Jam penerimaan toko", "Batasan waktu pada penyusunan rute", "Wawancara dengan sales dan toko"],
       ["3", "Lama bongkar muat per toko", "Perkiraan waktu layanan per titik", "Pengukuran langsung selama 10 hari"],
       ["4", "Jarak dan waktu tempuh nyata", "Angka awal K1 dan K5", "Odometer dan GPS, direkap harian"],
       ["5", "Tingkat dan penyebab keterlambatan", "Angka awal K3", "Catatan keterlambatan dengan kategori penyebab"],
       ["6", "Biaya non-bahan bakar", "Memeriksa asumsi biaya per km", "Data akuntansi: penyusutan, perawatan, asuransi, upah"]],
      widths=[1.0, 4.2, 4.4, 6.3],
      center_cols=[0],
      size=9.5,
      note="Sumber: rancangan penulis.")

# ---------------------------------------------------------------- properti & simpan
cp = doc.core_properties
cp.title = "Armada Banyak, Pengiriman Tetap Terlambat — Laporan Studi Kasus 4 (versi sederhana)"
cp.subject = "Analisis efisiensi distribusi dan kualitas layanan"
cp.author = "[Nama Mahasiswa]"
cp.keywords = "optimasi rute, keterlambatan, ETA, data toko, perbaikan bertahap"
cp.language = "id-ID"

_page_number()

os.makedirs(os.path.dirname(OUT), exist_ok=True)
doc.save(OUT)
print("tersimpan:", os.path.abspath(OUT))
print("tabel:", len(doc.tables))
