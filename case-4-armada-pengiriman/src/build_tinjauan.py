"""Membangun dokumen tinjauan (review) atas draf laporan Case 4 milik mahasiswa.

Mandiri: hanya butuh python-docx.
    python3 build_tinjauan.py  ->  ../output/Tinjauan-Laporan-Case-4.docx
"""
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT = "Times New Roman"
NAVY = RGBColor(0x1F, 0x38, 0x64)
GREY = RGBColor(0x59, 0x59, 0x59)
GREEN = RGBColor(0x1E, 0x6B, 0x3A)
AMBER = RGBColor(0x9A, 0x62, 0x00)
RED = RGBColor(0xA6, 0x1B, 0x1B)
USABLE = 16.4  # lebar area teks (cm) pada margin 2,2 cm

doc = Document()
sec = doc.sections[0]
sec.page_width = Cm(21.0)
sec.page_height = Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.2)
sec.top_margin = Cm(1.9)
sec.bottom_margin = Cm(1.9)

st = doc.styles["Normal"]
st.font.name = FONT
st.font.size = Pt(10.5)
st.paragraph_format.space_after = Pt(5)
st.paragraph_format.line_spacing = 1.12
st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)


def _shade(el, hexcolor):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hexcolor)
    el.append(shd)


def _border(par, color="1F3864", size=8, side="bottom"):
    pPr = par._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    e = OxmlElement(f"w:{side}")
    e.set(qn("w:val"), "single")
    e.set(qn("w:sz"), str(size))
    e.set(qn("w:space"), "2")
    e.set(qn("w:color"), color)
    bdr.append(e)
    pPr.append(bdr)


def h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(12.5)
    r.bold = True
    r.font.color.rgb = NAVY
    _border(p)
    return p


def h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(9)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = FONT
    r.font.size = Pt(11)
    r.bold = True
    r.font.color.rgb = NAVY
    return p


def p(text="", size=10.5, italic=False, bold=False, align="just", space_after=5, indent=0):
    par = doc.add_paragraph()
    par.alignment = {"just": WD_ALIGN_PARAGRAPH.JUSTIFY,
                     "left": WD_ALIGN_PARAGRAPH.LEFT,
                     "center": WD_ALIGN_PARAGRAPH.CENTER}[align]
    par.paragraph_format.space_after = Pt(space_after)
    if indent:
        par.paragraph_format.left_indent = Cm(indent)
    # dukung **tebal** sederhana
    for i, chunk in enumerate(text.split("**")):
        if not chunk:
            continue
        r = par.add_run(chunk)
        r.font.name = FONT
        r.font.size = Pt(size)
        r.italic = italic
        r.bold = bold or (i % 2 == 1)
    return par


def bullet(text, size=10.5, indent=0.55):
    par = doc.add_paragraph(style="List Bullet")
    par.paragraph_format.left_indent = Cm(indent + 0.35)
    par.paragraph_format.first_line_indent = Cm(-0.35)
    par.paragraph_format.space_after = Pt(2)
    par.paragraph_format.line_spacing = 1.08
    for i, chunk in enumerate(text.split("**")):
        if not chunk:
            continue
        r = par.add_run(chunk)
        r.font.name = FONT
        r.font.size = Pt(size)
        r.bold = (i % 2 == 1)
    return par


def num(n, text, size=10.5):
    par = doc.add_paragraph()
    par.paragraph_format.left_indent = Cm(0.85)
    par.paragraph_format.first_line_indent = Cm(-0.85)
    par.paragraph_format.space_after = Pt(2)
    par.paragraph_format.line_spacing = 1.08
    par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = par.add_run(f"{n}. ")
    r.font.name = FONT
    r.font.size = Pt(size)
    r.bold = True
    for i, chunk in enumerate(text.split("**")):
        if not chunk:
            continue
        r = par.add_run(chunk)
        r.font.name = FONT
        r.font.size = Pt(size)
        r.bold = (i % 2 == 1)
    return par


def box(lines, fill="EEF3FA", bar="1F3864"):
    """Kotak sorotan satu sel."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    cell = t.rows[0].cells[0]
    cell.width = Cm(USABLE)
    _shade(cell._tc.get_or_add_tcPr(), fill)
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    for side, sz, col in (("left", 18, bar), ("top", 4, fill), ("bottom", 4, fill), ("right", 4, fill)):
        e = OxmlElement(f"w:{side}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), str(sz))
        e.set(qn("w:color"), col)
        borders.append(e)
    tcPr.append(borders)
    cell.paragraphs[0]._p.getparent().remove(cell.paragraphs[0]._p)
    for i, (txt, kind) in enumerate(lines):
        par = cell.add_paragraph()
        par.paragraph_format.space_after = Pt(3 if i < len(lines) - 1 else 0)
        par.paragraph_format.space_before = Pt(3 if i == 0 else 0)
        par.paragraph_format.line_spacing = 1.10
        par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for j, chunk in enumerate(txt.split("**")):
            if not chunk:
                continue
            r = par.add_run(chunk)
            r.font.name = FONT
            r.font.size = Pt(kind)
            r.bold = (j % 2 == 1)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def table(headers, rows, widths, size=8.8, caption=None, note=None, align_center_cols=(), zebra=True):
    if caption:
        c = doc.add_paragraph()
        c.paragraph_format.space_before = Pt(6)
        c.paragraph_format.space_after = Pt(2)
        c.paragraph_format.keep_with_next = True
        r = c.add_run(caption)
        r.font.name = FONT
        r.font.size = Pt(9)
        r.bold = True
        r.font.color.rgb = NAVY

    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    t.style = "Table Grid"

    # lebar tetap
    tbl = t._tbl
    tblPr = tbl.tblPr
    tblW = OxmlElement("w:tblW")
    tblW.set(qn("w:w"), str(int(sum(widths) * 567)))
    tblW.set(qn("w:type"), "dxa")
    tblPr.append(tblW)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    grid = tbl.find(qn("w:tblGrid"))
    if grid is not None:
        tbl.remove(grid)
    grid = OxmlElement("w:tblGrid")
    for w in widths:
        gc = OxmlElement("w:gridCol")
        gc.set(qn("w:w"), str(int(w * 567)))
        grid.append(gc)
    tbl.insert(list(tbl).index(tblPr) + 1, grid)

    hdr = t.rows[0]
    trPr = hdr._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:tblHeader"))
    for i, htext in enumerate(headers):
        cell = hdr.cells[i]
        cell.width = Cm(widths[i])
        _shade(cell._tc.get_or_add_tcPr(), "1F3864")
        par = cell.paragraphs[0]
        par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.space_before = Pt(1)
        par.paragraph_format.line_spacing = 1.0
        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = par.add_run(htext)
        r.font.name = FONT
        r.font.size = Pt(size)
        r.bold = True
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for ri, row in enumerate(rows):
        cells = t.add_row().cells
        for ci, val in enumerate(row):
            cell = cells[ci]
            cell.width = Cm(widths[ci])
            if zebra and ri % 2 == 1:
                _shade(cell._tc.get_or_add_tcPr(), "F2F5FA")
            par = cell.paragraphs[0]
            par.paragraph_format.space_after = Pt(0)
            par.paragraph_format.space_before = Pt(1)
            par.paragraph_format.line_spacing = 1.02
            par.alignment = WD_ALIGN_PARAGRAPH.CENTER if ci in align_center_cols else WD_ALIGN_PARAGRAPH.LEFT
            txt = str(val)
            color = None
            if txt.startswith("!"):
                txt = txt[1:]
                color = RED
                bold_all = True
            elif txt.startswith("~"):
                txt = txt[1:]
                color = AMBER
                bold_all = True
            elif txt.startswith("+"):
                txt = txt[1:]
                color = GREEN
                bold_all = True
            else:
                bold_all = False
            for j, chunk in enumerate(txt.split("**")):
                if not chunk:
                    continue
                r = par.add_run(chunk)
                r.font.name = FONT
                r.font.size = Pt(size)
                r.bold = bold_all or (j % 2 == 1)
                if color is not None:
                    r.font.color.rgb = color

    for row in t.rows:
        trPr = row._tr.get_or_add_trPr()
        if not trPr.findall(qn("w:cantSplit")):
            trPr.append(OxmlElement("w:cantSplit"))

    if note:
        n = doc.add_paragraph()
        n.paragraph_format.space_before = Pt(2)
        n.paragraph_format.space_after = Pt(6)
        r = n.add_run(note)
        r.font.name = FONT
        r.font.size = Pt(8)
        r.italic = True
        r.font.color.rgb = GREY
    else:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def footer_pages():
    par = doc.sections[0].footer.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = par.add_run("Tinjauan draf laporan Studi Kasus 4 · halaman ")
    r.font.name = FONT
    r.font.size = Pt(8)
    r.font.color.rgb = GREY
    for code in ("PAGE",):
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), code)
        run = OxmlElement("w:r")
        rpr = OxmlElement("w:rPr")
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), "16")
        rpr.append(sz)
        run.append(rpr)
        fld.append(run)
        par._p.append(fld)


# =====================================================================
# JUDUL
# =====================================================================
t = doc.add_paragraph()
t.paragraph_format.space_after = Pt(2)
r = t.add_run("TINJAUAN DRAF LAPORAN STUDI KASUS 4")
r.font.name = FONT
r.font.size = Pt(17)
r.bold = True
r.font.color.rgb = NAVY

p("Analisis Permasalahan Operasional Distribusi dan Evaluasi Alternatif Solusi Berbasis TIK",
  size=11.5, bold=True, align="left", space_after=2)
p("Oleh: Joanne Abigayle Kayla Raintung (102042600132) · MR-50-04 · Dosen: Bela Pitria Hakim",
  size=9.5, italic=True, align="left", space_after=2)
p("Berkas yang ditinjau: 15 halaman · 2.310 kata · 9 tabel · 1 diagram proses · ditinjau 30 Oktober 2026",
  size=9, italic=True, align="left", space_after=8)

box([
 ("Isinya sudah layak dikumpulkan. Akar penyebabnya tepat, semua angka konsisten, dan tiga alternatif dibandingkan dengan matriks berbobot yang benar. Yang bermasalah bukan analisisnya, melainkan kelengkapan dan kepatuhan format.", 10.5),
 ("Tiga hal membuat nilai turun tajam kalau dikumpulkan apa adanya: halaman **Ringkasan masih kosong**, **Lampiran 2 dirujuk dua kali tetapi tidak ada**, dan isinya **12 halaman padahal batas 8**. Ketiganya bisa dibereskan dalam 90 menit karena tidak menuntut analisis baru.", 10.5),
])

# =====================================================================
h1("1. Penilaian per kriteria tugas")
p("Penilaian di bawah mengikuti tujuh output wajib pada halaman 2 dokumen kasus dan ketentuan penulisan pada halaman 14–15. Ini penilaian teknis, bukan nilai dosen.", size=9.5, italic=True)

table(
    ["Kriteria", "Status", "Alasan singkat"],
    [
        ["1. Masalah utama & akar penyebab", "+ Sesuai", "Lima mengapa tajam; akar = tidak ada standar, data, dan ukuran. Bukti kuat."],
        ["2. Analisis kuantitatif & biaya", "~ Perbaiki", "16 perhitungan dicek, semuanya benar. Lima asumsi kunci belum dinyatakan."],
        ["3. Minimal tiga alternatif", "+ Sesuai", "A1/A2/A3 berjenjang logis, bukan tiga merek yang sama."],
        ["4. Rekomendasi + asumsi eksplisit", "~ Perbaiki", "A1–A5 ada, tetapi angka lain muncul tanpa asal. Cara mengumpulkan data belum ada."],
        ["5. Risiko operasional/teknologi/sosial/keamanan", "+ Sesuai", "R1–R5 mencakup keempat jenis yang diminta."],
        ["6. KPI", "+ Sesuai", "5 KPI terukur, dan jujur menyatakan baseline diukur di Fase 0."],
        ["7. Rencana 90 hari", "+ Sesuai", "4 fase dengan syarat lanjut yang jelas dan bisa diperiksa."],
        ["Sistematika bab", "~ Perbaiki", "BAB V menyimpang: 4 subbab, 5.1 tanpa judul, Lampiran hilang, Ringkasan kosong."],
        ["Format penulisan", "~ Perbaiki", "TNR 12, spasi 1,5, margin 2,54, justify: semua benar. Nomor halaman tidak ada."],
        ["Panjang 5–8 halaman isi", "! Kurang", "12 halaman isi (hal. 3–14). Kelebihan 4 halaman."],
        ["Sitasi & daftar pustaka", "! Kurang", "4 sitasi tanpa entri pustaka; 3 entri tidak pernah disitasi."],
    ],
    widths=[5.6, 2.2, 8.6],
    caption="Tabel 1  Status kepatuhan terhadap tuntutan tugas",
    note="+ sesuai · ~ perlu perbaikan kecil · ! harus diperbaiki sebelum dikumpulkan.",
    align_center_cols=(1,),
)

# =====================================================================
h1("2. Yang sudah benar — jangan diubah")
p("Bagian ini penting supaya Anda tidak memperbaiki hal yang sudah baik.")
bullet("**Akar penyebab bukan gejala.** Anda menolak dua jawaban mudah (\"belum ada aplikasi\" dan \"kurang armada\") dan berhenti pada sesuatu yang bisa diperbaiki: pengetahuan rute hanya ada di kepala orang, tanpa KPI. Ini yang membedakan analisis dari daftar keluhan.")
bullet("**Tabel 2.1 memisahkan fakta kasus dari asumsi.** Ada kolom \"status penggunaan\" yang menyatakan mana yang harga simulasi dan mana yang target, bukan hasil. Ini persis yang diminta pada catatan \"jangan mengarang data\".")
bullet("**Angkanya konsisten.** Rp610,8 juta, porsi 23,0/40,9/25,1/11,0%, NPV ketiga alternatif, dan skor 3,25/3,70/3,85 semuanya saya hitung ulang — tidak ada satu pun yang salah.")
bullet("**Matriks skor transparan.** Bobot, skala 1–5, dan hasil kali per sel ditulis lengkap, sehingga dosen bisa memeriksa tanpa menebak.")
bullet("**KPI mengakui baseline belum ada.** Anda tidak memalsukan angka awal; Anda menulis \"diukur Fase 0\". Itu justru nilai tambah.")
bullet("**Rencana 90 hari punya syarat lanjut.** \"95% toko berdata lengkap\" dan \"jarak turun ≥5%\" membuat tiap fase bisa dinilai lulus atau tidak.")

# =====================================================================
h1("3. Lima hal yang harus dibereskan lebih dulu")

h2("3.1  Halaman Ringkasan masih kosong")
p("Halaman 2 hanya berisi kata \"RINGKASAN\" dan tujuh baris kosong. Ini output wajib pertama yang dibaca dosen, dan kosong berarti kehilangan bagian yang seharusnya merangkum seluruh laporan. Teks berikut sudah memenuhi empat unsur yang diminta (permasalahan, metode, solusi, hasil) dan panjangnya satu halaman.")
box([
 ("RINGKASAN", 10.5),
 ("Perusahaan distribusi barang konsumsi mengoperasikan 20 kendaraan dengan jarak rata-rata 150 km per kendaraan per hari. Rute disusun dispatcher secara manual berdasarkan pengalaman, peta, dan urutan pesanan masuk. Akibatnya kendaraan melewati wilayah yang sama berulang kali, urutan kunjungan tidak optimal, dan keterlambatan baru diketahui setelah pengemudi menelepon kantor. Pelanggan tidak menerima perkiraan waktu kedatangan yang akurat sehingga jadwal penerimaan berubah dan waktu tunggu bertambah.", 10),
 ("Analisis dilakukan dalam empat langkah: menghitung baseline dari data kasus (3.000 km/hari; 936.000 km/tahun; 93.600 liter; Rp936 juta), menghitung biaya akibat masalah, menelusuri akar penyebab dengan teknik lima mengapa, lalu membandingkan tiga alternatif dengan lima kriteria berbobot dan analisis NPV.", 10),
 ("Hasilnya, keterlambatan (40,9%) dan waktu tunggu (25,1%) menyumbang 66,0% dari kerugian Rp610,8 juta per tahun, sedangkan bahan bakar hanya 23,0%. Karena itu menambah armada atau membeli aplikasi tanpa membenahi data tidak akan menyelesaikan masalah. Alternatif 3 — membenahi standar dan data lebih dulu, lalu memasang aplikasi rute dan pelacakan posisi — dipilih dengan skor 3,85 dari 5,00, NPV Rp232,2 juta, payback 10,1 bulan, dan modal Rp125 juta atau 83% dari pagu.", 10),
 ("Pelaksanaannya dibagi empat fase dalam 90 hari tanpa menghentikan operasional, dimulai dari pengukuran baseline dan perapian data toko. Pada 12 bulan diharapkan jarak per kiriman turun 13%, OTIF mencapai 95%, keterlambatan turun 30%, dan akurasi ETA mencapai 85%.", 10),
])

h2("3.2  \"Lampiran 2\" dirujuk dua kali, tetapi tidak ada")
p("Halaman 6 menulis \"(Lampiran 2)\" dan halaman 9 menulis \"(rincian lengkap di Lampiran 2)\", tetapi dokumen berakhir di Daftar Pustaka. Pembaca yang mencari lampiran itu akan menemukan halaman kosong, dan kesan yang muncul adalah rujukan dibuat tanpa diperiksa.")
p("Lampiran ini sekaligus menutup satu kekurangan lain: tugas meminta Anda menjelaskan **data apa yang diperlukan dan bagaimana cara mengumpulkannya**. Dua tabel berikut menjawab keduanya.")
table(
    ["Kode", "Asumsi", "Nilai", "Sumber", "Cara memvalidasi"],
    [
        ["A1", "Hari operasi setahun", "312 hari (26 × 12)", "Data kasus", "Cocokkan dengan kalender operasi perusahaan"],
        ["A2", "Titik kirim per kendaraan/hari", "8 titik → 160 kiriman/hari", "Asumsi penulis", "Hitung dari rekap surat jalan 1 bulan"],
        ["A3", "Tingkat keterlambatan", "5% dari kiriman", "Asumsi penulis", "Bandingkan jam tiba vs jam janji, 1 bulan"],
        ["A4", "Biaya satu keterlambatan", "Rp100.000/kejadian", "Asumsi penulis", "Wawancara staf penjualan; nilai komplain"],
        ["A5", "Tingkat diskonto", "12% per tahun", "Asumsi penulis", "Bandingkan bunga pinjaman modal kerja"],
        ["A6", "Waktu tunggu", "12,8 jam/hari (0,64 jam × 20 truk)", "Asumsi penulis", "Checklist pengemudi: jam tiba vs jam bongkar"],
        ["A7", "Upah per jam", "Rp38.462 (Rp7 juta ÷ 182 jam)", "Asumsi penulis", "Slip gaji bagian operasional"],
        ["A8", "Beban kerja dispatcher", "40% × 2 orang", "Asumsi penulis", "Time study 5 hari kerja"],
    ],
    widths=[1.1, 4.4, 3.7, 2.5, 4.7],
    size=8.4,
    caption="Tabel A  Delapan asumsi dan cara memvalidasinya (isi Lampiran 1)",
    align_center_cols=(0,),
)
table(
    ["Data yang belum ada", "Untuk apa", "Cara mengumpulkan", "Siapa", "Kapan"],
    [
        ["Jarak tempuh aktual per truk", "Menetapkan baseline jarak", "Catat odometer pagi–sore; atau ekspor GPS", "Dispatcher", "Fase 0, 14 hari"],
        ["Koordinat, jam buka, akses toko", "Bahan rute otomatis", "Survei 2 hari per zona + telepon konfirmasi", "Sales + dispatcher", "Fase 0"],
        ["Waktu bongkar per toko", "Menghitung jendela waktu", "Checklist pengemudi (jam tiba, jam keluar)", "Pengemudi", "Fase 0"],
        ["Frekuensi & penyebab keterlambatan", "Mengukur K3 dan OTIF", "Rekap surat jalan vs jam janji, kategorikan penyebab", "Admin operasional", "Fase 0"],
        ["Konsumsi BBM aktual (L/100 km)", "Mengganti asumsi 1:10", "Rekap struk SPBU per nomor lambung", "Keuangan", "Fase 0–1"],
        ["Harga penawaran teknologi", "Menguji asumsi Rp125 juta", "Minta 3 penawaran tertulis setara lingkup", "TI + pengadaan", "Fase 1"],
        ["Tingkat layanan pesaing", "Menilai risiko kehilangan pelanggan", "Wawancara 20 toko pelanggan", "Manajer operasional", "Fase 1"],
    ],
    widths=[4.3, 3.6, 4.9, 2.2, 1.6],
    size=8.4,
    caption="Tabel B  Rencana pengumpulan data yang belum tersedia (isi Lampiran 2)",
    align_center_cols=(4,),
)

h2("3.3  Empat sitasi tanpa entri pustaka, tiga entri tanpa sitasi")
p("Di 2.1 Anda mengutip Yu et al. (2023), Frey et al. (2023), Zong et al. (2024), dan Demirbilek (2025). Keempatnya tidak ada di Daftar Pustaka. Sebaliknya Christopher (2016), Ohno (1988), dan BPH (2025) tercantum di pustaka tetapi tidak pernah disitasi. Dosen yang memeriksa satu per satu akan menemukan keduanya dalam dua menit.")
p("Cara tercepat dan paling aman: ganti paragraf 2.1 dengan versi di bawah. Versi ini hanya memakai sumber yang entrinya lengkap, lebih pendek 40%, dan tetap memuat gagasan yang Anda butuhkan untuk 3.1 — bahwa persoalannya data dan standar, bukan algoritma.")
box([
 ("2.1  Landasan Teori", 10.5),
 ("Vehicle Routing Problem with Time Windows (VRPTW) adalah perluasan VRP yang menentukan urutan kunjungan sejumlah kendaraan agar seluruh pelanggan terlayani di dalam jendela waktu tertentu, dengan meminimalkan jarak, biaya, atau waktu tempuh (Braekers dkk., 2016; Liu dkk., 2023). Literatur pengiriman jarak pendek menunjukkan bahwa kualitas rute tidak hanya ditentukan jarak: jendela waktu, waktu bongkar, dan akses lokasi ikut menentukan apakah rute dapat dijalankan (Boysen dkk., 2021).", 10),
 ("Ada dua implikasi praktis. Pertama, manfaat optimasi hanya muncul bila data lokasi, jendela waktu, dan waktu layanan tersedia serta terintegrasi; tanpa itu algoritma terbaik pun bekerja di atas asumsi yang salah (Holland dkk., 2017). Kedua, teknologi tidak menggantikan pengetahuan lokal dispatcher dan pengemudi. Pada sistem yang berhasil, standar kerja dan pemeriksaan harian membuat penyimpangan terlihat lebih cepat, bukan menunggu laporan (Spear & Bowen, 1999). Karena itu persoalan pada kasus ini adalah persoalan data dan standar, bukan pemilihan algoritma.", 10),
])
p("Untuk Daftar Pustaka, perbaiki tiga hal: (a) tambahkan Boysen dkk. (2021) karena kini disitasi; (b) lengkapi entri Liu dkk. (2023) dengan volume, nomor, dan halaman — atau hapus dan ganti sitasinya menjadi Braekers dkk. (2016) saja kalau detailnya tidak dapat Anda pastikan; (c) samakan gaya: pilih \"dkk.\" atau \"et al.\", jangan campur (saat ini 6 \"et al.\" dan 2 \"dkk.\").")
p("Entri Boysen yang dapat dipakai: Boysen, N., Fedtke, S., & Schwerdfeger, S. (2021). Last-mile delivery concepts: A survey from an operational research perspective. OR Spectrum, 43(1), 1–58. https://doi.org/10.1007/s00291-020-00607-8", size=9.5)
p("Christopher (2016) dan Ohno (1988): sitasi di 1.1 (\"distribusi dan ketepatan rute berpengaruh terhadap efisiensi biaya\") atau hapus dari pustaka. Jangan biarkan menggantung.", size=9.5, italic=True)

h2("3.4  Susunan BAB V tidak sesuai sistematika")
p("Tugas menetapkan lima subbab: 5.1 Tahapan Implementasi, 5.2 Kebutuhan Sumber Daya, 5.3 Pembagian Tanggung Jawab, 5.4 Identifikasi Risiko dan Mitigasi, 5.5 Indikator Keberhasilan. Dokumen Anda hanya punya empat, dan judul 5.1 hilang — setelah \"BAB V RENCANA IMPLEMENTASI\" langsung masuk Tabel 5.1.")
table(
    ["Yang ada sekarang", "Seharusnya", "Tindakan"],
    [
        ["BAB V  RENCANA IMPLEMENTASI", "BAB V. PENUTUP", "Ganti judul bab"],
        ["(tidak ada judul) + Tabel 5.1", "5.1 Tahapan Implementasi", "Tambahkan judul di atas tabel"],
        ["5.2 Sumber Daya dan Tanggung Jawab", "5.2 Kebutuhan Sumber Daya", "Pecah: sisakan modal & biaya operasional"],
        ["(menyatu di 5.2)", "5.3 Pembagian Tanggung Jawab", "Beri subbab sendiri + Tabel 5.2 (di bawah)"],
        ["5.3 Risiko dan Mitigasi", "5.4 Identifikasi Risiko dan Mitigasi", "Nomori ulang; tabel jadi 5.3"],
        ["5.4 Indikator Keberhasilan (KPI)", "5.5 Indikator Keberhasilan (KPI)", "Nomori ulang; tabel jadi 5.4"],
    ],
    widths=[5.6, 5.4, 5.4],
    size=8.6,
    caption="Tabel 2  Penomoran ulang BAB V",
)
p("Tabel pembagian tanggung jawab yang bisa langsung dipakai (menggantikan satu paragraf panjang di 5.2 yang sekarang mencampur lima peran dalam satu kalimat):", size=9.5)
table(
    ["Peran", "Tanggung jawab utama", "Keluaran yang dinilai"],
    [
        ["Direktur operasional", "Memutuskan kelanjutan tiap fase", "Keputusan lanjut/henti di akhir Fase 1 dan 3"],
        ["Manajer operasional", "Mengawal pelaksanaan harian, memilik proses akhir", "Rapat KPI mingguan; dokumen serah terima"],
        ["Dispatcher", "Menyusun rute, mencatat alasan penimpaan", "Log penimpaan; usulan rute harian 20 kendaraan"],
        ["Pengemudi", "Menjalankan rute, mengisi checklist waktu", "Checklist bongkar; laporan hambatan lapangan"],
        ["TI", "Integrasi data toko & akun pengguna", "Data 95% toko lengkap dan tervalidasi"],
        ["Keuangan", "Memverifikasi manfaat nyata", "Laporan manfaat bulan ke-6 dan ke-12"],
    ],
    widths=[3.4, 6.4, 6.6],
    size=8.6,
    caption="Tabel 5.2 (baru)  Pembagian tanggung jawab",
)

h2("3.5  Panjang 12 halaman, batas 8")
p("Halaman isi Anda: BAB I (2), BAB II (3), BAB III (2), BAB IV (2), BAB V (2), BAB VI (1) = 12 halaman. Batas yang disarankan 5–8 halaman isi, tidak termasuk sampul dan lampiran. Yang menentukan bukan jumlah kata (2.310 kata masih wajar), melainkan ruang yang dihabiskan tabel dan halaman kosong: halaman 4 hanya berisi satu paragraf, halaman 9 dan 11 setengah kosong karena setiap bab dipaksa mulai di halaman baru.")
p("Ada satu jalan pintas yang sah dan paling cepat: **lampiran tidak dihitung** dalam batas halaman. Pindahkan Tabel 2.1 (fakta kasus) dan Tabel 5.3 (KPI) ke lampiran, rujuk di teks, dan Anda langsung kehilangan hampir satu halaman tanpa menghapus satu gagasan pun.")
table(
    ["Bagian", "Sekarang", "Target", "Cara memangkas"],
    [
        ["BAB I", "2,0 hal", "1,4", "1.5 digabung ke halaman sebelumnya; hapus baris kosong ganda"],
        ["BAB II", "3,0 hal", "2,0", "Ganti 2.1 (−40%); kecilkan diagram 2.3; Tabel 2.1 → Lampiran"],
        ["BAB III", "2,0 hal", "1,3", "Lima syarat 3.3 jadi satu paragraf mengalir"],
        ["BAB IV", "2,0 hal", "1,7", "Tabel 4.2–4.3 font 11 pt, spasi dalam sel rapat"],
        ["BAB V", "2,0 hal", "1,6", "Tabel 5.4 (KPI) → Lampiran; risiko dipadatkan"],
        ["BAB VI", "1,0 hal", "0,6", "Kesimpulan 4 butir, masing-masing maksimal 2 baris"],
        ["Jumlah isi", "12,0 hal", "8,6 → 8", "Tanpa memindahkan tabel ke lampiran: −1 hal lagi dari halaman kosong"],
    ],
    widths=[2.6, 2.4, 2.4, 9.0],
    size=8.6,
    caption="Tabel 3  Anggaran halaman",
    align_center_cols=(1, 2),
)
p("Tiga aturan cepat saat memangkas: (1) jangan hapus tabel, kecilkan fontnya ke 11 pt; (2) jangan hapus paragraf, gabungkan dua kalimat yang menjelaskan hal sama; (3) hilangkan page break antar bab kalau dosen tidak mewajibkan setiap bab mulai di halaman baru — ini sendiri menghemat hampir dua halaman.")

# =====================================================================
doc.add_page_break()
h1("4. Temuan sedang: benar isinya, kurang penjelasannya")
p("Sebelas hal berikut tidak membuat laporan salah, tetapi membuat dosen berhenti dan bertanya. Masing-masing bisa diperbaiki dalam 2–5 menit.")
table(
    ["No", "Temuan", "Cara memperbaiki"],
    [
        ["1", "Lima angka muncul tanpa asal: 12,8 jam/hari, Rp38.462/jam, 40% beban dispatcher, \"2 orang × Rp7 juta\", dan 49.920 kiriman/tahun. Padahal Anda sudah punya daftar asumsi A1–A5.", "Tambahkan A6–A8 di 3.4, dan tulis satu kalimat: \"49.920 = 20 kendaraan × 8 titik × 312 hari\"."],
        ["2", "Tabel 2.2 menyebut \"bahan bakar berlebih 15%\". Kasus hanya menetapkan target pengurangan 15%, bukan bahwa 15% jarak saat ini benar-benar terbuang.", "Ubah menjadi \"potensi penghematan BBM pada target −15%\" dan sebut ini batas atas, bukan kerugian terukur."],
        ["3", "Tidak ada penjelasan cara mengumpulkan data yang belum tersedia, padahal tugas memintanya eksplisit.", "Pakai Tabel B di bagian 3.2 dokumen ini (cukup satu halaman)."],
        ["4", "K3 tertulis \"tidak melebihi pagu\", tetapi skornya tidak mengikuti urutan modal: A2 Rp115 juta dapat 3, sedangkan A3 Rp125 juta dapat 4 — padahal A2 lebih murah. Dosen akan menganggap skornya disesuaikan agar A3 menang.", "Ganti nama K3 menjadi \"efisiensi penggunaan pagu (manfaat per Rp modal)\" dan tampilkan rasionya: A1 113,0 ÷ 25 = 4,5 → skor 5; A2 211,7 ÷ 115 = 1,8 → 3; A3 247,7 ÷ 125 = 2,0 → 4. Dengan begitu ketiga skor Anda jadi konsisten dan alasannya bisa diperiksa."],
        ["5", "Asal angka manfaat Rp113/212/248 juta di Tabel 4.2 tidak dijelaskan sama sekali.", "Tambahkan tabel komposisi di bawah Tabel 4.2. Rekonstruksinya cocok: A3 = 140,4 (BBM penuh) + 74,9 (30% keterlambatan) + 27,6 (18% waktu tunggu) + 4,8 = 247,7. A2 = 140,4 + 50,0 + 15,4 + 6,0 = 211,7. A1 = 46,8 + 50,0 + 15,4 + 0,8 = 113,0 (selisih Rp0,8 juta sebaiknya Anda bulatkan agar rapi)."],
        ["6", "Tidak ada analisis inkremental. A1 butuh Rp25 juta dan balik 3,4 bulan; A3 butuh Rp125 juta dan balik 10,1 bulan. Dosen akan bertanya mengapa memilih yang lima kali lebih mahal.", "Tambahkan satu paragraf: A3 − A1 = modal +Rp100 juta, arus kas +Rp59,7 juta/tahun → NPV inkremental = −100 + (59,7 × 2,4018) = +Rp43,4 juta. Tambahan investasi tetap layak, tetapi argumennya ini, bukan \"NPV tertinggi\"."],
        ["7", "Caption Tabel 5.3 tertinggal di halaman 12, tabelnya pindah ke halaman 13.", "Klik kanan caption → Paragraph → centang \"Keep with next\"."],
        ["8", "Diagram 2.3 tidak bernomor dan tidak berjudul, padahal ketentuan meminta semua gambar bernomor.", "Beri judul di bawah gambar: \"Gambar 2.1  Alur proses operasional saat ini dan titik kegagalannya\"."],
        ["9", "Teks di dalam diagram berukuran 5 pt dan kode K2/K4/K5-7 tidak dijelaskan.", "Naikkan ke minimal 8 pt; tambahkan satu kalimat: \"K2, K4, K5–7 adalah kode titik kegagalan yang dibahas pada 3.2\"."],
        ["10", "Tabel 4.1, 4.3, 5.1, 5.2, dan 5.3 tidak punya paragraf penjelasan; ketentuan meminta setiap tabel diberi penjelasan.", "Satu kalimat per tabel: apa yang dibaca pembaca dari tabel itu, bukan mengulang isinya."],
        ["11", "Keterlambatan 30% dan OTIF 95% di 4.4 tidak dijelaskan asalnya; apakah ini target realistis atau harapan.", "Sitasi benchmark (mis. penghematan 10–15% biaya BBM pada armada menengah) atau nyatakan sebagai target internal."],
    ],
    widths=[0.8, 7.9, 7.7],
    size=8.2,
    caption="Tabel 4  Temuan sedang (P1)",
    align_center_cols=(0,),
)

h1("5. Temuan kecil: cepat, tetapi terlihat")
table(
    ["No", "Temuan", "Perbaikan"],
    [
        ["1", "Tidak ada nomor halaman di seluruh dokumen.", "Insert → Page Number → Bottom, center. Sampul boleh tanpa nomor."],
        ["2", "Judul bab tidak seragam: BAB I dan BAB III rata kiri, BAB II/IV/V/VI rata tengah. \"BAB I.\" bertitik, yang lain tidak, dan \"BAB IV  HASIL\" berspasi ganda.", "Pilih satu pola: \"BAB I  PENDAHULUAN\", rata tengah, tanpa titik."],
        ["3", "Campur \"et al.\" (6×) dan \"dkk.\" (2×).", "Samakan menjadi \"dkk.\" sesuai bahasa Indonesia."],
        ["4", "Kesimpulan butir 4 terpotong dan tanpa titik: \"…izinkan penimpaan resmi\".", "Lengkapi: \"…dan mencatat alasan penimpaan agar pengetahuan itu tidak hilang lagi.\""],
        ["5", "Header Tabel 5.2 menyatu: \"SkorMitigasi\"; kolom \"Jenis\" terlalu sempit sampai \"Keamanan3\" menempel.", "Lebarkan kolom Jenis 0,6 cm; beri padding sel 0,1 cm."],
        ["6", "Isi sel tabel rata kiri-kanan sehingga spasi melebar tak wajar (\"Ukur    baseline    (jarak,    waktu,\").", "Ratakan kiri isi sel; justify hanya untuk paragraf badan."],
        ["7", "Dua angka \"per kiriman\" berbeda tanpa label: Rp18.750 (BBM) dan Rp12.236 (kerugian).", "Beri label: \"biaya BBM per kiriman\" dan \"kerugian per kiriman\"."],
        ["8", "Sumber tabel bercampur: \"rancangan penulis\", \"identifikasi penulis\", \"analisis penulis\".", "Seragamkan: \"Sumber: Penulis (2026)\"."],
    ],
    widths=[0.8, 7.9, 7.7],
    size=8.2,
    caption="Tabel 5  Temuan kecil (P2)",
    align_center_cols=(0,),
)

# =====================================================================
h1("6. Verifikasi angka")
p("Saya menghitung ulang setiap angka yang muncul, termasuk yang hanya ada di dalam tabel. **Hasilnya: 16 dari 16 pemeriksaan lolos.** Ini jarang terjadi dan layak dipertahankan.")
table(
    ["Yang diperiksa", "Hitungan", "Hasil"],
    [
        ["Jarak harian", "20 × 150", "3.000 km ✓"],
        ["Jarak setahun", "3.000 × 312", "936.000 km ✓"],
        ["Kebutuhan BBM", "936.000 ÷ 10", "93.600 liter ✓"],
        ["Belanja BBM", "93.600 × Rp10.000", "Rp936 juta ✓"],
        ["Kiriman setahun", "20 × 8 × 312", "49.920 ✓"],
        ["BBM per kiriman", "936.000.000 ÷ 49.920", "Rp18.750 ✓"],
        ["BBM berlebih", "0,15 × 936.000 ÷ 10 × 10.000", "Rp140,4 juta ✓"],
        ["Keterlambatan", "0,05 × 49.920 × 100.000", "Rp249,6 juta ✓"],
        ["Waktu tunggu", "12,8 × 38.462 × 312", "Rp153,6 juta ✓"],
        ["Perencanaan manual", "0,40 × 2 × 7.000.000 × 12", "Rp67,2 juta ✓"],
        ["Total kerugian", "140,4 + 249,6 + 153,6 + 67,2", "Rp610,8 juta ✓"],
        ["Porsi komponen", "tiap komponen ÷ 610,8", "23,0 · 40,9 · 25,1 · 11,0% ✓"],
        ["Kerugian per kiriman", "610.800.000 ÷ 49.920", "Rp12.236 ✓"],
        ["PVIFA 12%, 3 tahun", "(1 − 1,12⁻³) ÷ 0,12", "2,4018 ✓"],
        ["NPV A1 / A2 / A3", "−modal + arus kas × 2,4018", "188,9 / 170,0 / 232,2 juta ✓"],
        ["Skor terbobot", "Σ (bobot × skor)", "3,25 / 3,70 / 3,85 ✓"],
    ],
    widths=[5.2, 7.2, 4.0],
    size=8.4,
    caption="Tabel 6  Hasil pemeriksaan ulang perhitungan",
    align_center_cols=(2,),
)
p("Tiga catatan yang bukan kesalahan hitung, tetapi perlu Anda antisipasi:")
num(1, "**Emisi 37,6 ton CO2e** benar, tetapi faktor konversinya tidak ditulis. Tambahkan \"(2,68 kg CO2 per liter)\" supaya bisa diperiksa.")
num(2, "**Rp18.750 per kiriman** dihitung dengan membagi 49.920 kiriman, padahal angka 49.920 baru muncul satu halaman kemudian di Tabel 2.2. Turunkan lebih dulu: 20 kendaraan × 8 titik × 312 hari.")
num(3, "**Payback A1 3,4 bulan** terlihat terlalu bagus dibanding A3 yang 10,1 bulan. Pastikan ini memang konsekuensi modal yang kecil, bukan karena manfaat A1 dihitung dengan cakupan lebih luas dari yang wajar untuk sebuah prosedur.")

# =====================================================================
h1("7. Rencana perbaikan 90 menit")
table(
    ["Waktu", "Pekerjaan", "Hasil"],
    [
        ["0–15", "Tempel Ringkasan (bagian 3.1)", "Halaman 2 terisi, satu output wajib aman"],
        ["15–30", "Buat Lampiran 1 dan 2 dari Tabel A dan B", "Rujukan tidak menggantung; syarat data terpenuhi"],
        ["30–40", "Ganti 2.1 dan rapikan Daftar Pustaka", "Sitasi bersih, hemat 0,3 halaman"],
        ["40–55", "Ubah BAB V jadi 5.1–5.5 sesuai Tabel 2", "Sistematika sesuai tugas"],
        ["55–80", "Pangkas sesuai Tabel 3", "Isi turun ke 8 halaman"],
        ["80–90", "Nomor halaman, keep-with-next caption, samakan judul bab", "Format rapi, tabel tidak terpisah"],
    ],
    widths=[1.8, 8.0, 6.6],
    size=8.8,
    caption="Tabel 7  Urutan kerja yang paling efisien",
    align_center_cols=(0,),
)

box([
 ("Kalau hanya ada 30 menit", 10.5),
 ("Kerjakan dua hal ini saja: isi Ringkasan, dan pindahkan Tabel 2.1 + Tabel 5.3 ke lampiran sambil menghapus page break antar bab. Dua langkah itu menutup tiga temuan terbesar sekaligus — halaman kosong, panjang berlebih, dan tabel yang tidak dijelaskan.", 10),
])

footer_pages()
doc.save("../output/Tinjauan-Laporan-Case-4.docx")
print("tersimpan: ../output/Tinjauan-Laporan-Case-4.docx")
