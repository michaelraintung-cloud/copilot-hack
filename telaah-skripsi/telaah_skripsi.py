#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Membangun laporan telaah naskah skripsi (A4) — Novita Derek, Manado Laundry Express."""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str((HERE / ".." / "materi-fisika").resolve()))

from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

from docx_kit import (  # noqa: E402
    ABU, BODY, HEAD, HITAM, MERAH, MERAH2, EMAS, HIJAU, BIRU,
    banner_judul, cell_shading, header_footer,
    judul_bagian, judul_item, label, new_document, p, par_border,
    par_shading, poin, rich, set_cell_margins, set_table_pct,
    table_borders, normalize_order,
)

OUT = HERE / "Telaah-Revisi-Skripsi-Novita-Derek.docx"
FONT_T = 8.4


# ------------------------------------------------------------------ utilitas
def tabel(doc, header, rows, widths=None, font=FONT_T, center=(), first_bold=False,
          header_fill="8B1A1A", zebra="F8F4EC", space_after=10):
    t = doc.add_table(rows=1, cols=len(header))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    table_borders(t, color="CFC5B4", sz=6)
    set_cell_margins(t, top=45, bottom=45, left=70, right=70)
    set_table_pct(t, 5000)
    if widths:
        for i, w in enumerate(widths):
            t.columns[i].width = Cm(w)

    hdr = t.rows[0]
    trPr = hdr._tr.get_or_add_trPr()
    trPr.append(OxmlElement("w:tblHeader"))
    for i, h in enumerate(header):
        c = hdr.cells[i]
        if widths:
            c.width = Cm(widths[i])
        c.text = ""
        par = c.paragraphs[0]
        par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.line_spacing = 1.0
        r = par.add_run(h)
        r.bold = True
        r.font.size = Pt(font)
        r.font.name = HEAD
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell_shading(c, header_fill)

    for k, row in enumerate(rows):
        cells = t.add_row().cells
        for i, val in enumerate(row):
            c = cells[i]
            if widths:
                c.width = Cm(widths[i])
            c.text = ""
            par = c.paragraphs[0]
            par.paragraph_format.space_after = Pt(0)
            par.paragraph_format.line_spacing = 1.0
            if i in center:
                par.alignment = WD_ALIGN_PARAGRAPH.CENTER
            txt = str(val)
            if first_bold and i == 0:
                txt = "**" + txt + "**"
            rich(par, txt, size=font)
            if zebra and k % 2 == 1:
                cell_shading(c, zebra)
    sp = doc.add_paragraph()
    sp.paragraph_format.space_after = Pt(space_after)
    sp.paragraph_format.space_before = Pt(0)
    return t


def temuan(doc, kode, judul, lokasi, masalah, bukti, perbaikan, warna="8B1A1A"):
    par = doc.add_paragraph()
    pf = par.paragraph_format
    pf.space_before = Pt(13)
    pf.space_after = Pt(3)
    pf.keep_with_next = True
    r = par.add_run(kode + "  ")
    r.bold = True
    r.font.name = HEAD
    r.font.size = Pt(11.5)
    r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    r2 = par.add_run(" " + judul)
    r2.bold = True
    r2.font.name = HEAD
    r2.font.size = Pt(11.5)
    r2.font.color.rgb = RGBColor.from_string(warna)
    par_shading(par, "F3EAEA")
    par_border(par, left=(18, warna, 8))

    tabel(doc, ["Aspek", "Uraian"], [
        ["Lokasi", lokasi],
        ["Masalah", masalah],
        ["Bukti", bukti],
        ["Perbaikan", perbaikan],
    ], widths=[2.9, 13.7], font=9.0, zebra=None, space_after=6)


def kotak(doc, judul, isi_paragraf, fill="F4F7FB", garis="1F4E79"):
    lab = doc.add_paragraph()
    lab.paragraph_format.space_before = Pt(7)
    lab.paragraph_format.space_after = Pt(2)
    lab.paragraph_format.keep_with_next = True
    r = lab.add_run(judul)
    r.bold = True
    r.font.size = Pt(9.2)
    r.font.name = HEAD
    r.font.color.rgb = RGBColor.from_string(garis)
    for i, t in enumerate(isi_paragraf):
        par = doc.add_paragraph()
        pf = par.paragraph_format
        pf.left_indent = Cm(0.32)
        pf.right_indent = Cm(0.2)
        pf.space_before = Pt(0 if i else 2)
        pf.space_after = Pt(2 if i < len(isi_paragraf) - 1 else 8)
        pf.line_spacing = 1.12
        par_shading(par, fill)
        par_border(par, left=(14, garis, 8))
        rich(par, t, size=9.6)


# ------------------------------------------------------------------ dokumen
def build():
    doc = new_document(
        "Telaah dan Saran Revisi Skripsi — Novita Derek",
        "Catatan pemeriksaan naskah skripsi Manado Laundry Express",
        "Arena.ai Agent",
        keywords="telaah skripsi, revisi, regresi linear berganda, kepuasan pelanggan",
        left=2.2, right=1.9,
    )
    header_footer(doc, "TELAAH NASKAH SKRIPSI", "Novita Derek · 210611020567",
                  "Pengaruh Inovasi Layanan, Service Quality, dan Persepsi Harga "
                  "terhadap Kepuasan Pelanggan Manado Laundry Express")

    # ---------------------------------------------------------------- cover
    banner_judul(
        doc,
        "CATATAN TELAAH NASKAH · 122 HALAMAN",
        "Telaah dan Saran Revisi",
        "“Pengaruh Inovasi Layanan, Service Quality dan Persepsi Harga terhadap "
        "Kepuasan Pelanggan Manado Laundry Express”",
        [
            ("Naskah", "Skripsi, 122 halaman (PDF)"),
            ("Penulis", "Novita Derek · NIM 210611020567"),
            ("Program", "Jurusan Manajemen, FEB Universitas Sam Ratulangi, 2026"),
            ("Lingkup telaah", "Seluruh 5 bab, 16 tabel, 4 gambar, 19 butir kuesioner, 35 entri pustaka"),
            ("Tanggal telaah", "Oktober 2026"),
        ],
    )

    p(doc, "", space_after=10)
    tabel(doc, ["Ringkasan putusan", "Jumlah"], [
        ["Temuan kritis — wajib diperbaiki sebelum seminar/sidang", "**6**"],
        ["Temuan sedang — metodologis, memengaruhi nilai dan tahanan penguji", "**17**"],
        ["Temuan ringan — bahasa, konsistensi, tata letak", "**12**"],
        ["Angka statistik yang diaudit ulang dan dinyatakan konsisten", "**12 dari 12**"],
    ], widths=[13.2, 3.4], font=9.6, center=(1,), zebra="F8F4EC")

    p(doc, "**Putusan umum.** Isi dan analisis datanya **layak** dan jauh di atas rata-rata: "
           "seluruh angka inti pada Bab IV lolos audit ulang, derajat kebebasan benar, nilai "
           "t tabel / F tabel / r tabel tepat, dan interpretasi arah pengaruh konsisten dari "
           "rumusan masalah sampai kesimpulan. Yang bermasalah **bukan hasil penelitiannya**, "
           "melainkan **kebersihan naskah dan beberapa sambungan antar-bab**: satu gambar model "
           "yang masih memuat variabel draf lama, indikator Service Quality yang tumpang tindih "
           "dengan variabel terikat, Daftar Pustaka yang belum sinkron, dan penomoran tabel yang "
           "kacau. Semua itu bisa diselesaikan dalam 2–3 hari kerja tanpa mengubah data.",
         size=10.4, space_after=8)

    p(doc, "**Cara membaca laporan ini.** Bagian 1 adalah audit angka (bukti bahwa hasilnya benar). "
           "Bagian 2 memuat enam temuan kritis yang berpotensi menjadi pertanyaan mematikan di "
           "sidang. Bagian 3 dan 4 memuat temuan sedang dan ringan. Bagian 5–7 berisi daftar "
           "perbaikan penomoran, daftar pustaka, dan **teks pengganti yang siap disalin** ke naskah. "
           "Bagian 8 adalah checklist kerja berurutan.",
         size=9.8, italic=True, color=ABU, space_after=6)

    # ---------------------------------------------------------------- 1
    judul_bagian(doc, "1. Audit Angka: Yang Sudah Benar",
                 "Setiap nilai pada Bab III dan Bab IV dihitung ulang dari data yang dilaporkan sendiri "
                 "(B, Std. Error, R², ANOVA). Tujuannya memastikan tidak ada angka yang saling bertentangan.")

    p(doc, "Tabel berikut menghitung ulang dua belas nilai kunci. Semuanya **cocok**. Ini penting "
           "untuk diketahui lebih dahulu: bila penguji menanyakan “apakah angka ini konsisten?”, "
           "jawabannya adalah ya, dan buktinya ada di tabel ini.", size=9.8)

    tabel(doc, ["No", "Yang diperiksa", "Nilai di naskah", "Hitung ulang", "Status"], [
        ["1", "Rumus Slovin, N = 600, e = 10%", "85,71 → 86", "600 ÷ (1 + 600 × 0,01) = 85,71", "sesuai"],
        ["2", "r tabel, N = 100, df = 98, α = 5%", "0,197", "0,1966", "sesuai"],
        ["3", "t tabel, df = 96, α = 5% (dua sisi)", "1,985", "1,9850", "sesuai"],
        ["4", "F tabel, df1 = 3, df2 = 96", "2,70", "2,699", "sesuai"],
        ["5", "R dari R² (0,739)", "0,859", "√0,739 = 0,8597", "sesuai"],
        ["6", "Adjusted R²", "0,730", "1 − (1 − 0,739)(99/96) = 0,7308", "sesuai"],
        ["7", "Std. Error of the Estimate", "1,95065", "√3,805 = 1,9506", "sesuai"],
        ["8", "Total Sum of Squares (ANOVA)", "1397,000", "99 × (3,75648)² = 1397,0", "sesuai"],
        ["9", "F hitung dari tabel ANOVA", "90,382", "343,906 ÷ 3,805 = 90,382", "sesuai"],
        ["10", "t hitung = B ÷ Std. Error (3 prediktor)", "8,053 / 9,790 / 9,522",
         "8,106 / 9,820 / 9,565 (selisih pembulatan B dan SE)", "sesuai"],
        ["11", "t konstanta", "−4,204", "−6,579 ÷ 1,565 = −4,204", "sesuai"],
        ["12", "Jumlah persentase Tabel 4.2–4.5", "100% tiap tabel", "38+62; 47+36+17; 41+27+15+11+6; "
         "39+34+27; 52+23+14+11", "sesuai"],
    ], widths=[0.9, 5.9, 3.4, 5.0, 1.4], font=8.4, center=(0, 4))

    p(doc, "**Catatan teknis yang bagus dan sebaiknya dipertahankan.** Skor minimum dan maksimum pada "
           "Tabel 4.8 tepat sesuai jumlah butir (X1 lima butir → maksimum 25; X3 empat butir → maksimum 20). "
           "Nilai β terstandar (0,420; 0,512; 0,498) juga konsisten dengan R² = 0,739 hanya jika "
           "antar-prediktor berkorelasi positif sangat kecil — persis seperti yang ditunjukkan "
           "Tolerance 0,994–0,999. Artinya datanya **koheren**, bukan hasil tempelan.", size=9.6)

    p(doc, "**Satu angka yang perlu dijelaskan, bukan diperbaiki.** Standar deviasi residual pada uji "
           "Kolmogorov–Smirnov tertulis 1,92087, sedangkan Std. Error of the Estimate 1,95065. Keduanya "
           "benar: yang pertama memakai pembagi N − 1 (√(365,283/99)), yang kedua memakai N − k − 1 "
           "(√(365,283/96)). Jika ditanya, jelaskan pembedanya — jangan diam saja.", size=9.6)

    # ---------------------------------------------------------------- 2
    judul_bagian(doc, "2. Enam Temuan Kritis",
                 "Perbaikan pada bagian ini menentukan apakah naskah lolos tanpa pertanyaan yang "
                 "menjatuhkan. Nomor halaman mengacu pada PDF 122 halaman.")

    temuan(doc, "K-1", "Gambar model penelitian masih memakai variabel draf lama",
           "Gambar 2.1 dan keterangannya, halaman 45 (juga Daftar Gambar halaman xvii).",
           "Model penelitian menampilkan **“Strategi Pemasaran Referral (X1)”** dan "
           "**“Strategi Harga (X3)”**, serta keterangan “H1: Pengaruh Pemasaran Referral…”, "
           "“H3: Pengaruh Strategi Harga…”, dan “H4: Pengaruh Pemasaran Referral, Service Quality, "
           "dan Strategi Harga…”. Ketiga variabel itu **tidak ada** dalam judul, rumusan masalah, "
           "kuesioner, maupun hasil olah data. Ini sisa naskah sebelumnya.",
           "Bandungkan dengan Tabel 3.1 (halaman 49) yang benar: X1 Inovasi Layanan, X2 Service "
           "Quality, X3 Persepsi Harga, Y Kepuasan Pelanggan. Judul skripsi pun memakai tiga "
           "variabel itu.",
           "Ganti isi ketiga elips pada gambar menjadi Inovasi Layanan (X1), Service Quality (X2), "
           "Persepsi Harga (X3). Perbaiki keterangan H1–H4 memakai kata “Inovasi Layanan” dan "
           "“Persepsi Harga”. Periksa juga apakah gambar ini disisipkan sebagai objek (bukan "
           "gambar tempel) agar mudah diedit. Teks pengganti ada di Bagian 7, kotak T-8.")

    temuan(doc, "K-2", "Artefak konversi menempel di 32 halaman",
           "Halaman xiii, xiv, 22–23, 26, 28, dan 31–56 — terutama seluruh Tabel 2.1.",
           "Ada **1.450 kemunculan huruf “ì” yang menyusup ke dalam kata** sehingga menjadi "
           "“Peìineìilitian”, “Keìpuìasan”, “Noi.”, “Kuìantitatif”, “Teìirdahuìluì”. Selain itu "
           "tersisa **13 notasi LaTeX** (`$> 0,60$`, `$R^2$`), **10 kurung kurawal ganda** "
           "(`t\\hitung`, `{{tabel}}`, `F{{hitung}}`), serta salah ketik berulang: “Noi.” (11×), "
           "“Skoir” (5×), “Loundry” (2× di halaman judul ii dan iii).",
           "Contoh persis, halaman 55: “Dinyatakan iteìm reìliabeìl apabila niai alpha cronbach-nya "
           "diatas 0,60”. Halaman 84: “koefisien Cronbach's Alpha $> 0,60$”. Halaman 77: "
           "“nilai 𝑡{\\{ℎ𝑖𝑡𝑢𝑛𝑔}} sebesar 9,790”.",
           "Ini kesan pertama yang dilihat penguji dan paling murah diperbaiki. Lakukan Find & "
           "Replace “ì” → kosong pada seluruh dokumen, lalu periksa manual kata yang memang "
           "mengandung ì (tidak ada dalam bahasa Indonesia). Ganti “$ … $” dengan teks biasa "
           "(“lebih besar dari 0,60”), “Noi.” → “No.”, “Skoir” → “Skor”, “Loundry” → “Laundry”. "
           "Setelah itu, jalankan pemeriksaan ejaan ulang satu kali dari awal.")

    temuan(doc, "K-3", "Indikator Service Quality memuat variabel terikat (tautologi)",
           "Subbab 2.4.2, halaman 17–18, dibandingkan Tabel 3.1 halaman 49 dan kuesioner butir 6–10.",
           "Subbab 2.4.2 memakai lima indikator Wardhana (2024): (1) kualitas interaksi, "
           "(2) pengalaman pelanggan, **(3) kepuasan pelanggan**, **(4) loyalitas pelanggan**, "
           "(5) kinerja layanan digital. Indikator ke-3 dan ke-4 adalah **variabel terikat dan "
           "turunanannya**. Jika dipertahankan, secara konseptual X2 “mengukur” Y — ini kelemahan "
           "pengukuran yang mudah ditembak penguji metode. Sementara itu instrumen yang benar-benar "
           "dipakai (Tabel 3.1 dan butir 6–10 kuesioner) adalah SERVQUAL: tangibles, reliability, "
           "responsiveness, assurance, empathy.",
           "Tabel 3.1 halaman 49 menulis “1. Tangibles (Kerapian kemasan & kebersihan outlet) … "
           "5. Empathy (Keramahan dan kesopanan staf)”, sedangkan subbab 2.4.2 tidak menyebut satu "
           "pun dari lima dimensi itu.",
           "Ganti subbab 2.4.2 dengan lima dimensi SERVQUAL dan rujuk sumber aslinya "
           "(Parasuraman, Zeithaml & Berry, 1988) ditambah Tjiptono (2022) yang sudah dikutip di "
           "Bab I. Setelah itu, kalimat pembuka hendaknya berbunyi “Indikator yang digunakan dalam "
           "penelitian ini adalah lima dimensi SERVQUAL…”. Teks lengkap ada di Bagian 7, kotak T-1. "
           "Pastikan Daftar Pustaka memuat sumber SERVQUAL tersebut.")

    temuan(doc, "K-4", "Daftar Pustaka belum sinkron dua arah",
           "Daftar Pustaka halaman 87–90, dibandingkan seluruh kutipan pada Bab I–V.",
           "Sebelas sumber **dikutip di batang tubuh tetapi tidak ada entrinya** di Daftar Pustaka; "
           "sebaliknya dua belas entri **tidak pernah dikutip**. Selain itu ada perbedaan ejaan dan "
           "tahun antara teks dan daftar.",
           "Lihat daftar lengkapnya di Bagian 6 (dua tabel). Contoh terberat: Tjiptono (2022) "
           "dikutip dua kali di Bab I dan Bab IV tetapi tidak ada di Daftar Pustaka; Rivai & "
           "Zulfitri (2021) dikutip tiga kali, tidak ada entrinya.",
           "Lengkapi sebelas entri yang hilang, hapus atau kutip dua belas entri yang menganggur, "
           "seragamkan nama dan tahun. Cara cepat: buka fitur “Manage Sources” Word atau periksa "
           "dengan mencari setiap nama belakang di seluruh naskah sebelum menyerahkan.")

    temuan(doc, "K-5", "Kontradiksi metode dan logika kriteria uji",
           "Subbab 3.1 halaman 46, 3.7.2 halaman 54–55, dan kriteria uji pada halaman 55–56.",
           "Empat hal: (a) subbab 3.7.2 menyatakan heteroskedastisitas diuji dengan **Uji White**, "
           "tetapi hasilnya (Tabel 4.11, halaman 73) adalah **Uji Glejser** — metode yang benar-benar "
           "dijalankan harus yang ditulis; (b) kalimat “Jika nilai Probability Chi-squared lebih "
           "kecil dari 0,05, maka **Ho diterima** dan Ha ditolak artinya **ada** masalah "
           "heteroskedastisitas” **terbalik** — jika p < 0,05 maka Ho (tidak ada masalah) ditolak; "
           "(c) halaman 46 menulis “berbeda dengan penelitian **kuantitatif** yang lebih fokus pada "
           "analisis mendalam” — yang dimaksud adalah **kualitatif**; (d) kata “generasi” seharusnya "
           "“generalisasi”.",
           "Halaman 46: “…berbeda dengan penelitian kuantitatif yang lebih fokus pada analisis "
           "mendalam terhadap objek tanpa melakukan generasi”. Halaman 54: “Metode yang digunakan "
           "untuk menguji heteroskedastisitas adalah dengan menggunakan Uji White.”",
           "Pilih satu: ubah kalimat 3.7.2 menjadi Uji Glejser (paling murah, karena hasilnya sudah "
           "Glejser), atau jalankan Uji White dan tambahkan hasilnya. Perbaiki kalimat kriteria, "
           "ganti “kuantitatif” → “kualitatif”, “generasi” → “generalisasi”. Teks pengganti: "
           "Bagian 7 kotak T-2, T-3, dan T-4.")

    temuan(doc, "K-6", "Penomoran subbab, tabel, dan rujukan silang kacau",
           "Tersebar: halaman xiv, 43, 52–53, 55, 63–64, 69, 73, 78, dan 82–92.",
           "Ada subbab bernomor ganda, nomor yang melompat, tabel bernomor kembar, dan rujukan "
           "silang yang menunjuk tabel yang salah. Daftar Tabel juga memuat “Tabel 4.16” yang tidak "
           "ada di batang tubuh, dan nomor halaman Daftar Tabel/Gambar tidak cocok dengan posisi "
           "sebenarnya (Tabel 1.1 tertulis halaman 8, kenyataannya halaman 3; Gambar 2.1 tertulis "
           "halaman 56, kenyataannya 45).",
           "Contoh: “1.4 Uji Asumsi Klasik” muncul di dalam Bab IV (halaman 69); “3.7.1” dipakai dua "
           "kali (Analisis Linear Berganda halaman 52 dan Uji R/R² halaman 53); “2.3.3 Pengaruh "
           "Persepsi Harga” seharusnya 2.7.3 (halaman 43); Tabel 4.5 dipakai dua kali (halaman 63 "
           "dan 64); teks halaman 82 menyebut “Tabel 4.7” padahal yang dibahas Tabel 4.6.",
           "Ikuti tabel perbaikan penomoran pada Bagian 5. Setelah selesai, gunakan fitur "
           "“Insert Caption” dan “Cross-reference” Word agar nomor ikut berubah otomatis, lalu "
           "perbarui Daftar Tabel/Gambar (References → Update Table).")

    # ---------------------------------------------------------------- 3
    judul_bagian(doc, "3. Tujuh Belas Temuan Sedang",
                 "Bukan salah hitung, tetapi memengaruhi nilai, kedalaman pembahasan, dan kesiapan "
                 "menjawab pertanyaan metodologi.")

    tabel(doc, ["No", "Letak", "Temuan", "Saran singkat"], [
        ["S-1", "3.2, hlm. 46",
         "Judul subbab berbunyi “Populasi, Sampel, dan Teknik Sampeìl Populasi”, tetapi **tidak ada "
         "satu paragraf pun** yang menyatakan teknik pengambilan sampel yang dipakai.",
         "Tambahkan subbab 3.2.3 “Teknik Pengambilan Sampel” dan sebut tekniknya secara eksplisit "
         "(mis. purposive sampling) beserta kriteria. Teks siap pakai: Bagian 7 kotak T-5."],
        ["S-2", "3.2.1, hlm. 46",
         "Populasi 600 = 20 pelanggan × 30 hari, padahal 20 itu disebut “estimasi **maksimal**”. "
         "Angka 600 karena itu batas atas, bukan rata-rata. Unit analisis juga ambigu: 600 "
         "“pelanggan” atau 600 “transaksi”? Response rate (berapa kuesioner dikirim vs kembali) "
         "tidak dilaporkan.",
         "Tulis asumsinya apa adanya (“batas atas”), tegaskan unit analisisnya pelanggan unik, dan "
         "tambahkan satu kalimat response rate."],
        ["S-3", "3.6, hlm. 50–51",
         "Uji validitas dan reliabilitas dijalankan pada **100 responden yang sama** dengan uji "
         "hipotesis, bukan pada sampel uji coba terpisah.",
         "Jika memang demikian, akui di Keterbatasan Penelitian. Jika ada uji coba 30 responden "
         "sebelumnya, laporkan terpisah — ini menaikkan nilai metodologi."],
        ["S-4", "4.3.1–4.3.2, hlm. 65–66",
         "Cronbach’s Alpha 0,947–0,962 dan korelasi butir-total 0,907–0,943. Nilai setinggi ini "
         "bisa berarti butir saling **redundan** atau responden menjawab seragam (straight-lining).",
         "Tambahkan tabel korelasi antar-butir (min–maks) dan, bila memungkinkan, uji Harman "
         "single factor. Jelaskan cara penyebaran (tanpa identitas, sukarela)."],
        ["S-5", "Bab IV, setelah 4.3.3",
         "**Tidak ada matriks korelasi antar variabel** (r X1–X2, X1–X3, X2–X3, dan tiap X dengan Y) — "
         "padahal ini tabel wajib pada skripsi regresi dan menjadi dasar membaca arah hubungan.",
         "Tambahkan Tabel Korelasi Pearson (4×4). Nilainya akan kecil antar-prediktor (konsisten "
         "dengan VIF ≈ 1,00), dan itu justru memperkuat argumen bebas multikolinearitas."],
        ["S-6", "4.3.3, hlm. 67–68",
         "Analisis deskriptif hanya per variabel, **tidak per butir**. Akibatnya Saran di Bab V "
         "tidak berpijak pada butir mana yang paling lemah.",
         "Tambahkan tabel mean & SD per butir (19 butir). Butir dengan mean terendah menjadi dasar "
         "saran manajerial — ini yang biasanya diminta penguji."],
        ["S-7", "4.4, hlm. 69–73",
         "Tidak ada uji linearitas dan tidak ada pemeriksaan outlier (tidak ada casewise "
         "diagnostics, tidak ada Mahalanobis).",
         "Tambahkan uji linearitas (Lavene/ANOVA atau curve fit) dan sebutkan cara penanganan "
         "outlier, walau hasilnya “tidak ada outlier”."],
        ["S-8", "4.5.1, hlm. 74",
         "Konstanta −6,579 ditafsirkan harfiah: “kepuasan pelanggan akan bernilai **negatif** "
         "sebesar 6,579 satuan”. Skala komposit hanya 5–25, sehingga nilai negatif mustahil.",
         "Nyatakan bahwa konstanta berada di luar rentang skala dan **tidak ditafsirkan secara "
         "substantif**; yang bermakna adalah tanda dan besaran koefisien."],
        ["S-9", "4.5.1, hlm. 74–75",
         "Koefisien ditafsirkan “per **satuan**”, padahal satuannya adalah skor komposit Likert.",
         "Gunakan “poin skala” atau “satu poin kenaikan skor” agar tepat dan konsisten."],
        ["S-10", "4.4.1, hlm. 70",
         "Nilai Asymp. Sig. 0,200 pada uji K-S adalah **batas bawah** (SPSS menuliskan “This is a "
         "lower bound of the true significance”). Nilai Monte Carlo Sig. 0,879 pada tabel yang "
         "sama belum dimanfaatkan.",
         "Sebutkan keduanya: “0,200 (batas bawah) dan Monte Carlo 0,879; keduanya > 0,05”. "
         "Argumen normalitas jadi jauh lebih kuat."],
        ["S-11", "Bab V",
         "**Tidak ada subbab Keterbatasan Penelitian.** Setiap skripsi empiris perlu ini; tanpa "
         "itu kesan naskah kurang jujur secara akademik.",
         "Tambahkan 5.3 Keterbatasan (sampel satu outlet, data self-report, cross-sectional, "
         "instrumen Likert, uji instrumen pada sampel yang sama). Teks: Bagian 7 kotak T-7."],
        ["S-12", "Tabel 1.2, hlm. 6",
         "Tabel 1.2 menduplikasi Tabel 4.1 (hlm. 60). Isinya juga rusak: kolom “SATUAN” tanpa "
         "harga sama sekali, “Cuci kemeja (5 kg) Rp15.000” satuan tidak jelas (kemeja atau "
         "kilogram?), dan “Setrika saja (5 kg) Rp25.000” lebih mahal daripada “Cuci kering lipat "
         "kecil Rp21.000” — penguji akan menanyakan logikanya.",
         "Pilih satu tabel saja (tarif lengkap di Bab IV, ringkasan di Bab I). Perbaiki satuan "
         "harga dan urutkan tarif secara logis, atau beri catatan mengapa setrika lebih mahal."],
        ["S-13", "Tabel 2.1, hlm. 31–41",
         "Tabel penelitian terdahulu membentang **11 halaman** dan isinya menduplikasi narasi 2.6 "
         "(setiap penelitian dijelaskan dua kali).",
         "Ringkas menjadi matriks 3–4 halaman (peneliti/tahun, variabel, metode & sampel, hasil, "
         "persamaan, perbedaan), dan pangkas narasi 2.6 menjadi 2–3 kalimat per penelitian."],
        ["S-14", "2.7, hlm. 42–44",
         "Hipotesis dirumuskan “**Diduga** berpengaruh” (tanpa arah), padahal uji t dua sisi dan "
         "pembahasan mengklaim “positif dan signifikan”. H1 dan H3 hanya bersandar pada satu "
         "penelitian. Rumusan masalah ke-4 memakai kata “strategi inovasi layanan” yang tidak ada "
         "di judul.",
         "Rumuskan “H1: Inovasi Layanan berpengaruh **positif dan signifikan**…”, tambahkan 2–3 "
         "rujukan pendukung per hipotesis, dan seragamkan istilah dengan judul."],
        ["S-15", "Gambar 1.1, hlm. 2",
         "Satu diagram batang mencampur empat satuan berbeda (persen, jumlah DPD, jumlah pelaku "
         "usaha, jumlah tenaga kerja) pada satu sumbu, sehingga “20%” tampak sebanding dengan "
         "“34.000 orang”. Sumber hanya “Data Kementerian UMKM dan ASLI” tanpa judul laporan, "
         "tahun, atau tautan.",
         "Pecah menjadi dua panel (pertumbuhan dalam %; jumlah dalam orang) atau ubah menjadi "
         "tabel. Cantumkan sumber yang bisa ditelusuri (nama laporan/berita + tahun + tautan)."],
        ["S-16", "3.3–3.4, hlm. 47–48",
         "Tidak ada pernyataan persetujuan responden (informed consent) dan kerahasiaan data, "
         "padahal kuesioner meminta identitas. Tanggal dan durasi pengambilan data juga tidak "
         "disebut.",
         "Tambahkan satu paragraf etika penelitian dan sebutkan periode pengambilan data "
         "(bulan dan tahun)."],
        ["S-17", "Bagian awal & akhir",
         "Tidak ditemukan **ABSTRAK**, **ABSTRACT**, **DAFTAR LAMPIRAN**, dan **RIWAYAT HIDUP** — "
         "empat bagian yang hampir selalu disyaratkan di FEB Unsrat.",
         "Lengkapi; abstrak 200–250 kata memuat tujuan, metode (100 responden, regresi berganda), "
         "hasil (t = 8,053; 9,790; 9,522; F = 90,382; R² = 0,739), dan kata kunci."],
    ], widths=[1.0, 2.6, 7.4, 5.6], font=7.9, center=(0,))

    # ---------------------------------------------------------------- 4
    judul_bagian(doc, "4. Dua Belas Temuan Ringan",
                 "Cepat diperbaiki, tetapi paling menentukan kesan kerapian naskah.")

    tabel(doc, ["No", "Letak", "Temuan", "Perbaikan"], [
        ["R-1", "Hlm. ii & iii", "Judul tertulis “MANADO **LOUNDRY** EXPRESS”",
         "Menjadi “LAUNDRY” (dua tempat)."],
        ["R-2", "Hlm. 2", "“**Industry** Laundry Indonesia”", "“Industri Laundry Indonesia”."],
        ["R-3", "1.3, hlm. 9", "“di **manado laundry express**” huruf kecil (4×)",
         "Kapitalkan nama usaha."],
        ["R-4", "Hlm. 26", "“Kepuasan **Konsuman**”", "“Konsumen”."],
        ["R-5", "2.7.2, hlm. 43", "“(**servive** quality)”", "“service quality”."],
        ["R-6", "Bab I–II", "Sitasi ditulis lengkap dalam kalimat: “Kotler, P., & Keller, K. L. "
         "(2021)”, “Rivai, A., & Zulfitri, D. (2021: 25-38)”",
         "Gunakan gaya APA di dalam teks: (Kotler & Keller, 2021). Nama lengkap hanya di Daftar Pustaka."],
        ["R-7", "Hlm. 4", "“Tjiptono (2022: **1**)” untuk definisi service quality",
         "Periksa halaman sumbernya; halaman 1 biasanya kata pengantar."],
        ["R-8", "Teks vs Daftar Pustaka", "Chrismadani/Chrismardani; Muryid/Mursyid; "
         "Zulfiana/Zulfina; Sugiyono/Sugiyon; Veryani 2022/2023",
         "Pilih satu ejaan dan satu tahun, samakan di seluruh naskah."],
        ["R-9", "Daftar Pustaka", "“**AI**-Gasawneh, M. A.”", "“Al-Gasawneh”."],
        ["R-10", "Hlm. 11", "Halaman hampir kosong: hanya satu baris (“khususnya pada usaha "
         "laundry.”) — sisa paragraf manfaat teoritis terpotong",
         "Rapatkan paragraf agar tidak ada halaman bersisa satu baris."],
        ["R-11", "Hlm. iv", "Lembar pengesahan: “Hari: , Tanggal: , Bulan:” dan “TANGGAL: 2026” kosong",
         "Isi sebelum dicetak, atau beri garis isian yang konsisten."],
        ["R-12", "Hlm. 1 dst.", "“BAB 1” memakai angka Arab, sedangkan “BAB II–V” memakai Romawi; "
         "Daftar Tabel menulis “Tabel 1.1 Tabel 1.1” ganda",
         "Seragamkan “BAB I” dan hapus pengulangan judul tabel."],
    ], widths=[1.0, 3.1, 7.4, 5.1], font=8.0, center=(0,))

    # ---------------------------------------------------------------- 5
    judul_bagian(doc, "5. Perbaikan Penomoran dan Rujukan Silang",
                 "Dikerjakan dari atas ke bawah; setelah selesai, perbarui Daftar Isi, Daftar Tabel, "
                 "dan Daftar Gambar secara otomatis.")

    tabel(doc, ["Halaman", "Tertulis sekarang", "Seharusnya", "Catatan"], [
        ["43", "2.3.3 Pengaruh Persepsi Harga…", "2.7.3", "Melompat ke nomor Bab II bagian 2.3."],
        ["44", "2.7.3 Pengaruh Inovasi, SQ, dan PH…", "2.7.4", "Geser satu nomor setelah perbaikan di atas."],
        ["52–53", "3.7.1 Analisis Linear Berganda; 3.7.1 Uji R dan R²", "3.7.1 dan 3.7.2",
         "Nomor kembar; 3.7.2 Uji Asumsi Klasik menjadi 3.7.3, 3.7.3 Uji Hipotesis menjadi 3.7.4."],
        ["69", "1.4 Uji Asumsi Klasik", "4.4", "Salah ketik bab."],
        ["78", "(tidak ada judul subbab sebelum Tabel 4.15)", "4.6.2 Uji Signifikansi Simultan (Uji F)",
         "Uji t sudah 4.6.1; Uji F belum punya subbab."],
        ["63 & 64", "Tabel 4.5 (dua kali)", "Tabel 4.5 dan Tabel 4.6",
         "Seluruh tabel setelahnya bergeser satu nomor (4.6→4.7 … 4.15→4.16)."],
        ["xvi", "Tabel 4.16 Uji F", "(hapus atau sesuaikan)", "Tidak ada Tabel 4.16 di batang tubuh."],
        ["12–13", "2.1 Kajian Teoritik; 2.1 Pengertian Kepuasan Pelanggan; 2.2 Kepuasan Pelanggan",
         "2.1; 2.2; 2.2.1", "Tiga judul untuk satu bagian; 2.2.2 Indikator tanpa 2.2.1."],
        ["26", "“Manfaat Penelitian” tanpa nomor", "1.4 Manfaat Penelitian", "Belum masuk Daftar Isi."],
        ["82", "“Berdasarkan Tabel 4.7…”", "Tabel 4.6", "Yang dibahas Tabel 4.6."],
        ["70", "“…pada Tabel 4.11”", "Tabel 4.9", "Rujukan ke tabel K-S."],
        ["71", "“Berdasarkan Tabel 4.12…”", "Tabel 4.10", "Rujukan ke tabel multikolinearitas."],
        ["74", "“Berdasarkan Tabel 4.9…”", "Tabel 4.12", "Rujukan ke tabel regresi."],
        ["75", "“…di Tabel 4.10”", "Tabel 4.13", "Rujukan ke Model Summary."],
        ["7", "“Berdasarkan Tabel 1.1 terlihat bahwa usaha ini sudah mulai melakukan inovasi…”",
         "Tabel 1.2", "Yang dimaksud tabel tarif."],
        ["xvi–xvii", "Nomor halaman Daftar Tabel/Gambar", "Perbarui",
         "Banyak yang tidak cocok: Tabel 1.1 tertulis 8 (asli 3), Gambar 2.1 tertulis 56 (asli 45)."],
    ], widths=[1.5, 6.4, 3.6, 5.1], font=8.0, center=(0,))

    # ---------------------------------------------------------------- 6
    judul_bagian(doc, "6. Daftar Pustaka: Dua Arah Ketidaksinkronan",
                 "Selesaikan bagian ini paling akhir, setelah semua kutipan baru dari Bagian 7 masuk.")

    label(doc, "6.1  Dikutip di batang tubuh, tetapi tidak ada entrinya di Daftar Pustaka")
    tabel(doc, ["Sumber yang dikutip", "Halaman", "Keterangan"], [
        ["Tjiptono (2022)", "4, 80", "Dikutip 2×; tidak ada entri."],
        ["Rivai & Zulfitri (2021)", "5, 18, 81", "Dikutip 3×; tidak ada entri."],
        ["Majid et al. (2021)", "17, 42", "Dikutip 2×; tidak ada entri."],
        ["Sandala, Putra & Wibowo (2021)", "18, 43", "Dikutip 2×; tidak ada entri."],
        ["Nuranti (2026)", "19", "Sumber indikator persepsi harga; tidak ada entri."],
        ["Zalianty & Sabrina (2025)", "43, 44, 80", "Dikutip 4×; tidak ada entri."],
        ["Kotler & Armstrong (2022)", "19, 81", "Hanya Kotler & Keller (2021) yang ada."],
        ["A. Muih (2023)", "46", "Nama/entri tidak ditemukan."],
        ["Pakpahan & Onaning (2025)", "24", "Dikutip; tidak ada entri."],
        ["Muryid & Praprimadani (2022)", "23", "Daftar memakai “Mursyid”."],
        ["Chrismadani (2024)", "20, 81", "Daftar memakai “Chrismardani”."],
    ], widths=[6.4, 2.8, 7.4], font=8.4)

    label(doc, "6.2  Ada entrinya, tetapi tidak pernah dikutip di batang tubuh")
    tabel(doc, ["Entri", "Saran"], [
        ["Arikunto (2021); Roflin, Liberty & Paridaya (2021)", "Kutip di 3.2 (populasi/sampel) — memang relevan."],
        ["Lovelock & Wirtz (2011)", "Kutip di 2.4 bila memakai konsep jasa."],
        ["Singh & Malik (2022); Siswanto & Maskan (2021); CMLabs (2024); "
         "Rahmawati & Mardiana (2023)", "Sisa draf “referral marketing” — hapus, atau kutip bila "
         "memang dibahas."],
        ["Sabriana & Laily (2022); Syarifah & Nazara (2022)", "Relevan sebagai penelitian terdahulu "
         "laundry — kutip di 2.6 atau Tabel 2.1."],
        ["Bramantyo (2022); Napitulu (2021); Al-Gasawneh dkk. (2021)", "Hapus bila tidak dipakai."],
        ["Sugiyon (2021-2022)", "Ejaan salah; tahun ditulis rentang. Perbaiki menjadi "
         "“Sugiyono (2021)” dan “Sugiyono (2022)” bila dua edisi."],
    ], widths=[7.2, 9.4], font=8.3)

    # ---------------------------------------------------------------- 7
    judul_bagian(doc, "7. Teks Pengganti Siap Salin",
                 "Delapan kotak berikut boleh dicopy langsung ke naskah, lalu sesuaikan nama dan "
                 "nomor halaman.")

    kotak(doc, "T-1  Subbab 2.4.2 — Indikator Service Quality (menggantikan versi Wardhana)", [
        "Indikator kualitas layanan yang digunakan dalam penelitian ini mengacu pada lima dimensi "
        "SERVQUAL yang dikemukakan Parasuraman, Zeithaml, dan Berry (1988), yaitu:",
        "1. **Tangibles (bukti fisik)** — penampilan fasilitas fisik, kebersihan outlet, kerapian "
        "kemasan hasil cucian, serta kelengkapan peralatan yang digunakan.",
        "2. **Reliability (keandalan)** — kemampuan memberikan layanan sesuai janji secara "
        "konsisten, terutama ketepatan waktu penyelesaian cucian.",
        "3. **Responsiveness (daya tanggap)** — kesigapan karyawan merespons pertanyaan, keluhan, "
        "dan permintaan khusus pelanggan.",
        "4. **Assurance (jaminan)** — pengetahuan, kesopanan, dan kemampuan karyawan menumbuhkan "
        "rasa aman bahwa pakaian tidak akan rusak, luntur, atau tertukar.",
        "5. **Empathy (empati)** — perhatian personal, keramahan, dan kesediaan mendengarkan "
        "kebutuhan khusus masing-masing pelanggan.",
        "Kelima dimensi ini dipilih karena tidak memuat unsur kepuasan maupun loyalitas pelanggan "
        "di dalamnya, sehingga variabel bebas tetap terpisah secara konseptual dari variabel terikat "
        "yang diukur, yaitu kepuasan pelanggan.",
    ])

    kotak(doc, "T-2  Subbab 3.1 — Kalimat pembanding yang benar", [
        "“…Hasil dari penelitian kuantitatif ini memungkinkan peneliti melakukan generalisasi "
        "terhadap populasi yang diteliti, berbeda dengan penelitian **kualitatif** yang lebih "
        "menekankan analisis mendalam terhadap objek tanpa melakukan generalisasi (A. Muih, 2023).”",
    ], fill="F4F7FB", garis="1F4E79")

    kotak(doc, "T-3  Subbab 3.7.2 butir c — Uji Heteroskedastisitas (Glejser)", [
        "“Uji heteroskedastisitas bertujuan menguji apakah dalam model regresi terjadi "
        "ketidaksamaan varians residual dari satu pengamatan ke pengamatan lain. Pengujian dilakukan "
        "dengan **Uji Glejser**, yaitu meregresikan nilai absolut residual (|e|) terhadap seluruh "
        "variabel independen. Dasar pengambilan keputusan: apabila nilai signifikansi setiap "
        "variabel independen **lebih besar dari 0,05**, maka tidak terdapat pengaruh yang signifikan "
        "terhadap |e|, sehingga model **bebas dari heteroskedastisitas**. Sebaliknya, apabila nilai "
        "signifikansi **lebih kecil dari 0,05**, maka Ho ditolak dan terdapat gejala "
        "heteroskedastisitas.”",
    ], fill="F4F7FB", garis="1F4E79")

    kotak(doc, "T-4  Subbab 4.5.1 — Interpretasi konstanta yang benar", [
        "“Nilai konstanta sebesar −6,579 menunjukkan titik potong garis regresi pada sumbu Y ketika "
        "seluruh variabel independen bernilai nol. Karena skor komposit kepuasan pelanggan hanya "
        "bergerak pada rentang 5 sampai 25, nilai konstanta ini berada **di luar rentang skala "
        "pengukuran** dan karenanya **tidak ditafsirkan secara substantif**. Makna konstanta di sini "
        "terbatas pada penentu posisi garis regresi, sedangkan interpretasi yang bermakna terletak "
        "pada tanda dan besaran koefisien masing-masing variabel bebas.”",
        "Untuk koefisien: “setiap kenaikan satu **poin skala** Inovasi Layanan meningkatkan Kepuasan "
        "Pelanggan sebesar 0,381 **poin skala**, dengan asumsi variabel lain tetap.”",
    ], fill="F4F7FB", garis="1F4E79")

    kotak(doc, "T-5  Subbab 3.2.3 baru — Teknik Pengambilan Sampel", [
        "“Teknik pengambilan sampel yang digunakan adalah **purposive sampling**, yaitu penentuan "
        "sampel berdasarkan pertimbangan tertentu yang sesuai dengan tujuan penelitian. Kriteria "
        "inklusi dalam penelitian ini adalah: (a) berusia minimal 17 tahun; (b) pernah menggunakan "
        "jasa Manado Laundry Express **minimal dua kali** dalam enam bulan terakhir; dan (c) "
        "bersedia mengisi kuesioner secara lengkap. Kriteria eksklusi adalah responden yang "
        "mengisi kuesioner secara tidak lengkap atau memberikan jawaban yang seluruhnya identik "
        "pada semua butir. Jumlah sampel yang berhasil dikumpulkan dan memenuhi kriteria adalah "
        "100 responden, melebihi batas minimum hasil perhitungan rumus Slovin sebesar 86 "
        "responden.”",
    ], fill="F4F7FB", garis="1F4E79")

    kotak(doc, "T-6  Subbab 4.6.2 baru — Uji Signifikansi Simultan (Uji F)", [
        "“Pengujian hipotesis keempat dilakukan secara simultan menggunakan Uji F untuk mengetahui "
        "apakah Inovasi Layanan (X1), Service Quality (X2), dan Persepsi Harga (X3) secara "
        "bersama-sama berpengaruh signifikan terhadap Kepuasan Pelanggan (Y). Kriteria pengujian: "
        "apabila F hitung > F tabel atau nilai signifikansi < 0,05, maka Ho ditolak dan Ha diterima. "
        "Hasil pengujian disajikan pada Tabel 4.15.”",
    ], fill="F4F7FB", garis="1F4E79")

    kotak(doc, "T-7  Subbab 5.3 baru — Keterbatasan Penelitian", [
        "“Penelitian ini memiliki beberapa keterbatasan yang perlu diperhatikan. **Pertama**, "
        "lingkup penelitian terbatas pada satu unit usaha di Kota Manado, sehingga hasilnya belum "
        "dapat digeneralisasikan ke seluruh industri penatu. **Kedua**, data dikumpulkan melalui "
        "kuesioner self-report sehingga persepsi responden berpotensi dipengaruhi subjektivitas dan "
        "keinginan menyenangkan peneliti. **Ketiga**, penelitian bersifat cross-sectional — data "
        "diambil pada satu titik waktu — sehingga tidak dapat menangkap perubahan kepuasan dari "
        "waktu ke waktu. **Keempat**, pengukuran variabel menggunakan skala Likert yang bersifat "
        "ordinal, meskipun dalam analisis diperlakukan sebagai data interval. **Kelima**, uji "
        "validitas dan reliabilitas instrumen dijalankan pada sampel yang sama dengan pengujian "
        "hipotesis, sehingga belum sepenuhnya terpisah dari proses uji coba instrumen.”",
    ], fill="F4F7FB", garis="1F4E79")

    kotak(doc, "T-8  Keterangan Gambar 2.1 — versi yang benar", [
        "**Keterangan:** X1 = Inovasi Layanan; X2 = Service Quality; X3 = Persepsi Harga; "
        "Y = Kepuasan Pelanggan.",
        "H1: Pengaruh Inovasi Layanan terhadap Kepuasan Pelanggan.  H2: Pengaruh Service Quality "
        "terhadap Kepuasan Pelanggan.  H3: Pengaruh Persepsi Harga terhadap Kepuasan Pelanggan.  "
        "H4: Pengaruh Inovasi Layanan, Service Quality, dan Persepsi Harga secara simultan terhadap "
        "Kepuasan Pelanggan di Manado Laundry Express.",
        "**Sumber:** Kajian teori, 2026 (diolah peneliti).",
    ], fill="FCF5F5", garis="8A1A1A")

    # ---------------------------------------------------------------- 8
    judul_bagian(doc, "8. Checklist Kerja Berurutan",
                 "Urutan ini disusun agar pekerjaan tidak berulang. Perkiraan waktu untuk satu orang "
                 "yang bekerja fokus.")

    tabel(doc, ["Urutan", "Pekerjaan", "Bagian", "Estimasi"], [
        ["1", "Ganti isi dan keterangan Gambar 2.1 (K-1)", "Bab II, hlm. 45", "20 menit"],
        ["2", "Bersihkan artefak ì, $, {}, “Noi.”, “Skoir”, “Loundry” (K-2)", "Seluruh naskah", "2–3 jam"],
        ["3", "Tulis ulang subbab 2.4.2 dengan SERVQUAL (K-3, T-1)", "Bab II, hlm. 17", "30 menit"],
        ["4", "Betulkan kontradiksi metode: Glejser, kriteria Ho, kualitatif (K-5, T-2, T-3)",
         "Bab III, hlm. 46–55", "45 menit"],
        ["5", "Tambah subbab 3.2.3 teknik sampling (S-1, T-5)", "Bab III, hlm. 46", "30 menit"],
        ["6", "Rapikan seluruh penomoran subbab dan tabel sesuai Bagian 5 (K-6)", "Bab II–IV", "2 jam"],
        ["7", "Perbaiki rujukan silang tabel (6 tempat)", "Bab I & IV", "30 menit"],
        ["8", "Tambah matriks korelasi + mean per butir (S-5, S-6)", "Bab IV", "1–1,5 jam"],
        ["9", "Perbaiki interpretasi konstanta dan “poin skala” (S-8, S-9, T-4)", "Bab IV, hlm. 74", "20 menit"],
        ["10", "Tulis subbab 4.6.2 Uji F (T-6) dan subbab Keterbatasan (S-11, T-7)", "Bab IV & V", "40 menit"],
        ["11", "Lengkapi ABSTRAK, ABSTRACT, DAFTAR LAMPIRAN, RIWAYAT HIDUP (S-17)", "Bagian awal–akhir", "1,5 jam"],
        ["12", "Sinkronkan Daftar Pustaka dua arah (K-4, Bagian 6)", "Hlm. 87–90", "1,5 jam"],
        ["13", "Perbaiki 12 temuan ringan (Bagian 4)", "Tersebar", "45 menit"],
        ["14", "Perbarui Daftar Isi, Daftar Tabel, Daftar Gambar; cetak PDF; baca ulang sekali",
         "Seluruh naskah", "1 jam"],
    ], widths=[1.4, 8.5, 4.0, 2.7], font=8.4, center=(0, 3))

    p(doc, "**Total estimasi: sekitar 2 hari kerja penuh.** Tidak ada satu pun butir di atas yang "
           "menuntut pengambilan data ulang atau penghitungan ulang regresi. Artinya, kualitas "
           "substansi yang sudah Anda miliki tidak berubah — yang berubah hanya kerapian dan "
           "konsistensi naskah.", size=9.8, space_after=10)

    # ---------------------------------------------------------------- 9
    judul_bagian(doc, "9. Tiga Tambahan yang Menaikkan Nilai",
                 "Bersifat pilihan, tetapi inilah yang membedakan skripsi “cukup” dan skripsi “bagus” "
                 "di mata penguji.")

    p(doc, "**1. Ukuran efek (effect size).** Selain signifikansi, laporkan besarnya pengaruh: "
           "f² = R²/(1 − R²) = 0,739/0,261 = **2,83** (kategori sangat besar menurut Cohen). Satu "
           "kalimat ini menjawab pertanyaan “signifikan itu seberapa penting?”.", size=9.6)

    p(doc, "**2. Sumbangan relatif tiap prediktor.** Dengan β terstandar, sumbangan efektif dapat "
           "dihitung: Service Quality 0,512 × 0,859 = 44,0%; Persepsi Harga 0,498 × 0,859 = 42,8%; "
           "Inovasi Layanan 0,420 × 0,859 = 36,1% (jumlahnya mendekati R² karena prediktor nyaris "
           "tidak berkorelasi). Ini memperkuat klaim di Bab V bahwa Service Quality paling dominan, "
           "tanpa perlu berdebat soal besaran B mentah (0,593 pada Persepsi Harga).", size=9.6)

    p(doc, "**3. Saran yang berbasis butir terlemah.** Setelah mean per butir tersedia, ubah Saran "
           "manajerial dari kalimat umum (“perlu SOP”, “perlu inovasi digital”) menjadi sasaran "
           "spesifik: sebut butir dengan mean terendah, besaran mean-nya, dan tindakan konkretnya. "
           "Penguji hampir selalu menanyakan dasar setiap saran.", size=9.6)

    p(doc, "**Skor akhir temuan.** Dari 35 butir yang diperiksa, **6 bersifat kritis, 17 sedang, "
           "12 ringan**. Enam butir kritis seluruhnya dapat diselesaikan tanpa mengubah data atau "
           "hasil analisis. Dengan memperbaiki Bagian 2 dan menjalankan checklist Bagian 8, naskah "
           "ini siap diajukan untuk seminar hasil.", size=10.2, space_after=6)

    for _ in range(2):
        q = doc.add_paragraph()
        q.paragraph_format.space_after = Pt(0)
    _p = doc.add_paragraph()
    _p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _p.paragraph_format.space_after = Pt(2)
    _r = _p.add_run("— selesai —")
    _r.font.name = HEAD
    _r.font.size = Pt(9.6)
    _r.font.color.rgb = ABU
    _p = doc.add_paragraph()
    _p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _r = _p.add_run("Telaah naskah · Oktober 2026")
    _r.font.name = HEAD
    _r.font.size = Pt(10.5)
    _r.bold = True
    _r.font.color.rgb = MERAH
    normalize_order(doc)
    doc.save(OUT)
    print("OK", OUT, round(OUT.stat().st_size / 1024, 1), "KB")


if __name__ == "__main__":
    build()
