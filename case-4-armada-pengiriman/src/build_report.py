"""Pembangun laporan Studi Kasus 4 -> laporan-studi-kasus-4.docx

Struktur mengikuti petunjuk format (sampul, ringkasan, Bab I-VI, daftar
pustaka, lampiran). Isi dijaga ±9 halaman; kedalaman analisis, tabel
pendukung, dan rincian perhitungan ditempatkan pada lampiran.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import model as m
from docx_utils import Report, FONT
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "figures")
OUT = os.path.join(HERE, "..", "output", "laporan-studi-kasus-4.docx")

B, C, F, A = m.BASE, m.COST, m.FIN, m.ALTERNATIF
NAVY = RGBColor(0x1F, 0x38, 0x64)


# ============================================================ HALAMAN SAMPUL
def sampul(r: Report):
    line = r.center_line

    r.space(20)
    line("INDUSTRIAL TECHNOLOGY CHALLENGE", 13, True)
    line("STUDI KASUS MANAJEMEN INDUSTRI", 13, True)
    r.rule()

    r.space(56)
    line("ARMADA BANYAK, PENGIRIMAN TETAP TERLAMBAT", 18, True, NAVY)
    r.space(8)
    line("Analisis Efisiensi Distribusi dan Kualitas Layanan", 12)
    line("pada Perusahaan Distribusi Barang Konsumsi", 12)
    r.space(4)
    line("(Studi Kasus 4 — Bidang Supply Chain & Distribution)", 11, False, colors_grey())
    r.space(26)
    line("LAPORAN STUDI KASUS", 12, True)

    r.space(72)
    line("Disusun oleh:", 11)
    line("[Nama Mahasiswa]", 12, True)
    line("NIM: [....................]          Kelas: [....................]", 11)
    r.space(18)
    line("Mata Kuliah: Manajemen Industri", 11)
    line("Dosen Pengampu: [Nama Dosen Pengampu]", 11)

    r.space(64)
    line("PROGRAM STUDI [NAMA PROGRAM STUDI]", 12, True)
    line("FAKULTAS [NAMA FAKULTAS]", 12, True)
    line("UNIVERSITAS [NAMA UNIVERSITAS]", 12, True)
    line("TAHUN [20XX]", 12, True)


def colors_grey():
    return RGBColor(0x59, 0x59, 0x59)


# ============================================================ RINGKASAN
def ringkasan(r: Report):
    r.page_break()
    r.caption("RINGKASAN", size=12, space_before=0, space_after=8)

    r.p(f"Perusahaan distribusi barang konsumsi mengoperasikan 20 kendaraan setiap hari dengan jarak "
        f"rata-rata 150 km per kendaraan. Rute disusun manual oleh dispatcher berdasarkan pengalaman dan "
        f"daftar pesanan. Ketika pesanan meningkat, cara kerja ini menimbulkan tiga gejala yang saling "
        f"menguatkan: kendaraan kembali melewati jalan yang sama karena urutan kunjungan mengikuti urutan "
        f"pesanan masuk, keterlambatan baru diketahui setelah pengemudi menelepon kantor, dan pelanggan "
        f"tidak menerima ETA sehingga jadwal penerimaan berubah dan pengemudi menunggu lebih lama.")

    r.p("Metode yang digunakan adalah analisis kuantitatif deskriptif atas data kasus (normalisasi jarak, konsumsi bahan bakar, dan biaya), analisis akar penyebab dengan diagram sebab-akibat dan teknik lima mengapa, penilaian kelayakan investasi (NPV, payback, rasio manfaat-biaya), serta penilaian multikriteria terbobot yang dilengkapi analisis sensitivitas. Data yang tidak tersedia dinyatakan sebagai asumsi eksplisit A1–A15, bukan diisi angka rekaan.")
    r.p(f"Analisis atas data kasus menunjukkan armada menempuh {m.angka(B['km_tahun'])} km dan membakar "
        f"{m.angka(B['liter_tahun'])} liter bahan bakar per tahun senilai {m.juta(B['biaya_bbm_tahun'],0)}. "
        f"Total konsekuensi ekonomi masalah mencapai {m.juta(C['total'],0)} per tahun atau "
        f"{m.rp(C['total']/B['kiriman_tahun'])} per kiriman, dengan komponen terbesar keterlambatan "
        f"({m.persen(C['keterlambatan']/C['total'])}) dan waktu tunggu ({m.persen(C['waktu_tunggu']/C['total'])}), "
        f"bukan bahan bakar ({m.persen(C['bbm_berlebih']/C['total'])}). Penghematan bahan bakar pada target "
        f"15% hanya {m.juta(C['bbm_berlebih'],1)} per tahun, sehingga kelayakan investasi harus dibangun di "
        f"atas perbaikan layanan dan produktivitas perencanaan.")

    r.p(f"Akar penyebab bukan jumlah armada, melainkan tidak adanya sistem perencanaan dan pengendalian "
    f"distribusi yang mengubah pengetahuan rute yang bersifat tacit menjadi aturan proses dan data. Dari "
    f"empat alternatif yang dinilai dengan enam kriteria berbobot, **Alternatif 4 (hybrid bertahap)** "
    f"memperoleh skor tertinggi ({m.angka(m.SKOR_AKHIR['A4'],2)} dari 5,00) dan NPV tiga tahun tertinggi "
    f"({m.juta(F['A4']['npv'],1)}) dengan modal {m.juta(A['A4']['capex'],0)} atau "
    f"{m.persen(A['A4']['capex']/m.KASUS['batas_investasi'])} dari batas investasi, payback "
    f"{m.angka(F['A4']['payback_bulan'],1)} bulan, dan tetap layak pada seluruh skenario sensitivitas. "
    f"Implementasi dirancang 90 hari dalam empat fase dan empat titik keputusan tanpa menghentikan "
    f"operasional, dengan target penurunan jarak {m.persen(0.13)}, penurunan keterlambatan "
    f"{m.persen(0.30)}, dan OTIF ≥95% pada 12 bulan pertama.")

    r.p("Kata kunci: optimasi rute, keterlambatan pengiriman, ETA, tata kelola data, hybrid",
        italic=True, size=10, first_line_indent=False, space_before=4)


# ============================================================ BAB I
def bab1(r: Report):
    r.h1("BAB I  PENDAHULUAN")

    r.h2("1.1  Latar Belakang")
    r.p("Perusahaan distribusi barang konsumsi pada studi kasus (BPH, 2025) melayani toko ritel dan pelanggan "
        "bisnis dengan 20 "
        "kendaraan yang beroperasi setiap hari dari pusat distribusi, jarak rata-rata 150 km per kendaraan "
        "dan 26 hari operasi per bulan. Rute ditentukan dispatcher berdasarkan pengalaman, menggunakan peta "
        "dan daftar pesanan. Cara kerja ini menimbulkan dua konsekuensi struktural: pengetahuan tentang "
        "jalan, akses toko, dan kebiasaan pelanggan bersifat tacit sehingga kapasitas perencanaan praktis "
        "sebesar kapasitas dua orang; dan ketika pesanan meningkat, urutan pesanan masuk menjadi acuan "
        "termudah, bukan kedekatan lokasi. Akibatnya, seperti tercatat dalam kasus, kendaraan kembali "
        "melewati jalan yang telah dilalui, keterlambatan baru diketahui setelah pengemudi menelepon, dan "
        "pelanggan mengubah jadwal penerimaan sehingga pengemudi menunggu lebih lama.")
    r.p("Manajemen mempertimbangkan aplikasi optimasi rute dan pelacakan kendaraan, tetapi pengemudi menilai "
        "aplikasi tidak memahami kondisi lokal, sementara keuangan meragukan apakah penghematan bahan bakar "
        "cukup menutupi biaya sistem. Kedua keberatan itu sah dan harus dijawab dengan data, sehingga "
        "laporan ini dimulai dari pertanyaan “berapa biaya masalahnya dan syarat apa yang harus dipenuhi”, "
        "bukan “teknologi apa yang dibeli”.")

    r.h2("1.2  Identifikasi Masalah")
    r.p("Lima gejala dapat diidentifikasi dari fakta kasus: (1) **urutan kunjungan tidak mengikuti kedekatan "
        "lokasi**, sehingga terjadi backtracking dan tumpang tindih wilayah antar kendaraan; (2) "
        "**keterlambatan tidak terdeteksi secara real-time** karena baru diketahui setelah pengemudi "
        "menelepon; (3) **tidak ada janji waktu yang dapat dikomunikasikan**, sehingga toko mengubah jadwal "
        "penerimaan; (4) **kapasitas perencanaan bergantung pada individu**, dengan beban memuncak pada jam "
        "sibuk; dan (5) **tidak tersedia data jarak, waktu, dan ketepatan waktu**, sehingga perbaikan tidak "
        "dapat diukur. Seluruh gejala bermuara pada satu masalah inti:")
    box = r.p("**Masalah utama:** sistem perencanaan dan pengendalian distribusi belum mampu menerjemahkan "
              "pengetahuan rute yang bersifat tacit menjadi aturan proses dan data yang dapat dieksekusi, "
              "dipantau, dan diperbaiki, sehingga armada menempuh jarak yang tidak perlu dan janji waktu "
              "tidak dapat dipenuhi maupun dikomunikasikan.",
              first_line_indent=False, size=11.5)
    box.paragraph_format.left_indent = Cm(0.6)
    r.p(f"Rumusan itu sengaja tidak menempatkan jumlah kendaraan sebagai masalah: setiap kiriman rata-rata "
        f"menempuh {m.angka(B['km_per_kiriman'],2)} km karena kunjungan tidak dikelompokkan, sehingga “armada "
        f"banyak” adalah gejala perencanaan yang tidak efisien, bukan penyebabnya.")

    r.h2("1.3  Rumusan Masalah")
    r.numbered([
        "Apa akar penyebab dominan keterlambatan dan inefisiensi jarak tempuh, dan sejauh mana berasal dari "
        "metode kerja, kapasitas perencanaan, kualitas data, atau keterbatasan sistem informasi?",
        "Berapa besar konsekuensi ekonomi masalah dan komponen biaya mana yang menjadi prioritas?",
        "Alternatif solusi mana yang paling tepat berdasarkan kriteria dampak, layanan, kepatuhan anggaran, "
        "kelayakan implementasi, fleksibilitas, dan skalabilitas?",
        "Bagaimana rancangan solusi menjaga fleksibilitas operasional, dan bagaimana keberhasilan diukur "
        "serta diimplementasikan dalam 90 hari?",
    ])

    r.h2("1.4  Tujuan Analisis")
    r.p("Tujuan laporan ini: mengidentifikasi masalah utama dan akar penyebabnya; menghitung konsekuensi "
        "ekonomi dengan asumsi eksplisit; membandingkan minimal tiga alternatif solusi dengan kriteria "
        "berbobot yang transparan; menentukan solusi terpilih beserta justifikasinya; mengidentifikasi risiko "
        "operasional, teknologi, sosial, dan keamanan data; serta menetapkan KPI terukur dan rencana "
        "implementasi 90 hari.")

    r.h2("1.5  Ruang Lingkup dan Batasan")
    r.p("Cakupan: perencanaan rute, pelaksanaan pengiriman, dan pelaporan pada lini distribusi dengan objek 20 "
        "kendaraan dan 26 hari operasi per bulan. Di luar cakupan: pengadaan kendaraan, operasi gudang, "
        "penetapan harga, serta pajak dan inflasi. Studi kasus tidak menyediakan data jumlah titik "
        "pengiriman, waktu tempuh, tingkat keterlambatan, biaya non-bahan bakar, biaya dispatcher, serta "
        "koordinat dan jam toko; nilai itu ditetapkan sebagai asumsi A1–A15 (Lampiran 2) dan digantikan "
        "hasil pengukuran Fase 0. Sesuai petunjuk, laporan ini tidak mengarang data: kebutuhan data dan "
        "metode pengumpulannya diuraikan pada Lampiran 5.")


# ============================================================ BAB II
def bab2(r: Report):
    r.h1("BAB II  LANDASAN TEORI", page_break=False)

    r.h2("2.1  Kajian Teori")
    r.p("**Vehicle routing problem.** Persoalan penentuan rute diformulasikan Dantzig dan Ramser (1959) dan "
        "berkembang menjadi salah satu bidang riset operasi paling produktif. Intinya menentukan rute "
        "berbiaya minimum dari depot, melayani setiap pelanggan tepat satu kali dengan batasan kapasitas "
        "(Toth & Vigo, 2014); bila pelanggan menetapkan jendela waktu, persoalan menjadi VRPTW. Karena "
        "NP-hard, optimalitas sulit dijamin pada skala nyata, tetapi heuristik menghasilkan solusi jauh "
        "lebih baik daripada penyusunan manual (Braekers dkk., 2016). Nilai ekonomisnya berasal dari "
        "*clustering* dan *sequencing*—dan rute yang mengikuti urutan pesanan masuk gagal pada keduanya. "
        "Holland dkk. (2017) melaporkan ORION di UPS melayani sekitar 55.000 pengemudi setiap hari dan, pada "
        "implementasi penuh, memangkas sekitar 100 juta mil serta lebih dari 300 juta dolar AS biaya per "
        "tahun—manfaat yang hanya terealisasi karena data pelanggan, pengemudi, dan kendaraan terintegrasi.")
    r.p("**Kualitas layanan, standardisasi, dan penilaian investasi.** Mutu layanan distribusi diukur melalui "
        "kemampuan memenuhi janji, umumnya dengan *On Time In Full* (OTIF): proporsi pengiriman yang tiba "
        "dalam jendela waktu yang dijanjikan sekaligus lengkap (Christopher, 2016; Rushton dkk., 2017). OTIF "
        "bersifat *outcome* dan tidak diagnostik sehingga perlu dilengkapi akurasi ETA. Tanpa visibilitas "
        "posisi dan status, organisasi hanya dapat bereaksi setelah kegagalan terjadi; dalam kerangka "
        "*service quality gap* (Parasuraman dkk., 1985), ketidakmampuan menyampaikan ETA yang akurat "
        "merupakan kegagalan komunikasi eksternal yang membentuk persepsi pelanggan. Dua pemborosan pada "
        "Toyota Production System paling relevan: transportasi dan waktu tunggu (Ohno, 1988), dan Spear & "
        "Bowen (1999) menunjukkan keunggulannya terletak pada standardisasi aktivitas, bukan pada alatnya—"
        "digitalisasi atas proses yang belum terstandar hanya memperbesar variasi. Tradisi sosio-teknis "
        "(Trist & Bamforth, 1951) menegaskan kinerja ditentukan optimasi bersama subsistem teknis dan sosial, "
        "sehingga keberatan pengemudi adalah informasi desain yang valid. Pembedaan pengetahuan tacit dan "
        "eksplisit (Polanyi, 1966; Nonaka & Takeuchi, 1995) menjelaskan mengapa pengalaman dispatcher harus "
        "dieksternalisasi menjadi data dan aturan. Kelayakan investasi dinilai dengan NPV, *payback*, dan "
        "rasio manfaat-biaya.")

    r.h2("2.2  Penelitian yang Relevan (Identifikasi Fakta dan Data Kasus)")
    r.p("Fakta kasus diinventarisasi agar batas antara data dan asumsi tetap jelas (Tabel 2.1), lalu "
        "diposisikan terhadap bukti literatur: rute optimal bergantung pada clustering dan sequencing, bukan "
        "pada pemilihan jalur antar dua titik (Dantzig & Ramser, 1959; Braekers dkk., 2016); manfaat optimasi "
        "berskala besar hanya muncul bila data terintegrasi (Holland dkk., 2017; Boysen dkk., 2021); dan "
        "standardisasi mendahului perbaikan sedangkan teknologi gagal bila subsistem sosial tidak dioptimasi "
        "(Spear & Bowen, 1999; Trist & Bamforth, 1951).")
    r.table(
        ["Sumber", "Fakta Kunci", "Implikasi bagi Analisis"],
        [
            ["Data kasus", "20 kendaraan; 150 km/hari; 26 hari/bulan; 1 liter/10 km; BBM simulasi "
             "Rp10.000/liter; target pengurangan jarak 15%; batas investasi Rp150 juta",
             "Dasar perhitungan jarak, konsumsi, dan biaya; tolok ukur manfaat dan kriteria anggaran"],
            ["Fakta kualitatif", "Rute manual; keterlambatan diketahui setelah telepon; pelanggan tanpa ETA "
             "akurat; pengemudi menilai aplikasi tidak paham kondisi lokal",
             "Absennya optimasi, visibilitas, dan pengelolaan janji waktu; menuntut mekanisme override"],
            ["Dantzig & Ramser (1959); Braekers dkk. (2016)", "Rute optimal bergantung pada clustering dan "
             "sequencing; batasan nyata harus dimodelkan", "Masalah bukan navigasi, melainkan perencanaan "
             "rute"],
            ["Holland dkk. (2017); Boysen dkk. (2021)", "ORION mengurangi 6–8 mil per rute; manfaat besar "
             "hanya muncul bila data terintegrasi", "Manfaat ditentukan kualitas data, bukan kecanggihan "
             "algoritma"],
        ],
        widths=[4.0, 6.3, 5.5], chapter="2",
        title="Inventarisasi Fakta Kasus dan Posisinya terhadap Literatur",
        note="Sumber: studi kasus dan literatur pada Daftar Pustaka, diolah.",
        align=["left", "left", "left"], font_size=7.5)

    r.h2("2.3  Kerangka Berpikir (Gambaran Proses Operasional Saat Ini)")
    r.p("Proses distribusi saat ini dipetakan dalam delapan langkah beserta titik kegagalannya (Gambar 2.1) "
        "agar analisis tidak melompat ke solusi teknologi sebelum proses yang hendak diperbaiki dipahami.")
    r.figure(os.path.join(FIG, "gambar-2-1-alur-proses.png"), 11.6, "2",
             "Alur Proses Distribusi Saat Ini dan Titik Kegagalannya",
             note="Sumber: diolah dari narasi studi kasus. P1–P5 menjadi objek analisis pada Bab III.")
    r.p("Tiga kesimpulan dapat dibaca. Pertama, titik kegagalan tersebar pada tahap perencanaan (P1), eksekusi "
        "(P2, P3), dan penutupan (P4, P5). Kedua, seluruhnya berada pada lapisan informasi dan keputusan, "
        "bukan lapisan fisik. Ketiga, lingkaran umpan balik terputus: langkah 8 tidak menghasilkan data yang "
        "kembali ke langkah 2 dan 3. Karena itu kerangka berpikir disusun dalam empat lapis yang diperbaiki "
        "berurutan—tata kelola, data, sistem, dan kapabilitas—dengan hipotesis bahwa solusi yang hanya "
        "menyentuh satu lapis tidak akan bertahan.")

    r.h2("2.4  Dampak Permasalahan")
    r.p(f"Perhitungan dimulai dari data kasus: 20 kendaraan × 150 km = {m.angka(B['km_hari'])} km/hari atau "
        f"{m.angka(B['km_tahun'])} km/tahun pada {m.angka(m.ASUMSI['A1_hari_operasi_tahun'])} hari operasi "
        f"(A1). Pada konsumsi 10 km/liter, kebutuhan bahan bakar {m.angka(B['liter_tahun'])} liter per tahun "
        f"senilai {m.juta(B['biaya_bbm_tahun'],0)}, atau {m.rp(B['biaya_bbm_tahun']/B['kiriman_tahun'])} per "
        f"kiriman. Dampak ekonomi masalah dihitung sebagai *cost of poor performance*, yaitu nilai yang "
        f"hilang setiap tahun akibat proses berjalan pada kondisi saat ini (Tabel 2.2).")
    r.table(
        ["Komponen Biaya", "Dasar Perhitungan", "Nilai per Tahun", "Porsi"],
        [
            ["Bahan bakar berlebih", f"15% × {m.angka(B['km_tahun'])} km ÷ 10 × Rp10.000",
             m.rp(C['bbm_berlebih']), m.persen(C['bbm_berlebih']/C['total'])],
            ["Keterlambatan pengiriman", f"5% × {m.angka(B['kiriman_tahun'])} kiriman × Rp100.000 (A4, A5)",
             m.rp(C['keterlambatan']), m.persen(C['keterlambatan']/C['total'])],
            ["Waktu tunggu di lokasi",
             f"{m.angka(B['jam_tunggu_hari'],1)} jam/hari × {m.rp(B['tarif_jam_pengemudi'])}/jam × 312",
             m.rp(C['waktu_tunggu']), m.persen(C['waktu_tunggu']/C['total'])],
            ["Produktivitas perencanaan manual", "40% × 2 dispatcher × Rp7.000.000 × 12 (A6–A8)",
             m.rp(C['perencanaan_manual']), m.persen(C['perencanaan_manual']/C['total'])],
            ["**Total dampak ekonomi**", "Penjumlahan seluruh komponen", f"**{m.rp(C['total'])}**", "**100,0%**"],
        ],
        widths=[4.3, 6.6, 3.1, 1.8], chapter="2",
        title="Estimasi Biaya Akibat Masalah (Cost of Poor Performance)",
        note=f"Sumber: perhitungan penulis. Setara {m.persen(C['total']/B['biaya_bbm_tahun'])} dari belanja "
             f"bahan bakar dan {m.rp(C['total']/B['kiriman_tahun'])} per kiriman.",
        align=["left", "left", "right", "center"], font_size=8, bold_rows=(4,))
    r.p(f"Keterlambatan dan waktu tunggu bersama-sama menyumbang "
        f"{m.persen((C['keterlambatan']+C['waktu_tunggu'])/C['total'])} dari total dampak, sedangkan bahan "
        f"bakar berlebih hanya {m.persen(C['bbm_berlebih']/C['total'])}. Ini menjawab keberatan tim keuangan "
        f"secara langsung—investasi tidak dapat dibenarkan dari bahan bakar saja—dan menunjukkan bahwa "
        f"prioritas perbaikan adalah mutu layanan dan produktivitas perencanaan. Dampak kualitatifnya: "
        f"menurunnya kepercayaan pelanggan, ketidakmampuan membuktikan manfaat investasi karena tidak ada "
        f"*baseline*, risiko personel kunci, serta pemborosan energi yang berbanding lurus dengan emisi "
        f"(sekitar {m.angka(B['co2_hemat_ton'],1)} ton CO2e per tahun pada target 15%).")


# ============================================================ BAB III
def bab3(r: Report):
    r.h1("BAB III  ANALISIS MASALAH", page_break=False)

    r.h2("3.1  Penentuan Masalah Utama")
    r.p("Setiap gejala diuji dengan tiga pertanyaan: apakah memiliki bukti langsung dalam kasus, apakah dapat "
        "diatasi tanpa menyentuh penyebabnya, dan apakah muncul kembali dalam bentuk lain bila diintervensi "
        "terpisah. Hasilnya konsisten: menambah kendaraan hanya memperbanyak kendaraan yang menempuh rute "
        "tidak efisien; menegur dispatcher tidak menghasilkan perbaikan permanen; laporan manual yang lebih "
        "sering tetap menghasilkan informasi terlambat; menambah dispatcher menaikkan biaya tetap tanpa "
        "menaikkan kualitas keputusan; dan *dashboard* di atas data yang tidak bersih hanya memindahkan "
        "masalah ke perangkat baru. Seluruh gejala karena itu merupakan kegagalan pada lapisan keputusan dan "
        "informasi, bukan pada sumber daya fisik. Masalah utama karenanya adalah **tidak adanya sistem "
        "perencanaan dan pengendalian distribusi yang mengubah pengetahuan rute yang bersifat tacit menjadi "
        "aturan proses dan data yang dapat dieksekusi, dipantau, dan diperbaiki.** Judul kasus dapat "
        "menyesatkan bila dibaca sebagai persoalan jumlah armada: 20 unit untuk delapan titik per kendaraan "
        "per hari adalah kapasitas memadai, sedangkan yang tidak memadai adalah mutu keputusan "
        "perencanaannya.")

    r.h2("3.2  Analisis Akar Penyebab")
    r.p("Akar penyebab ditelusuri dengan diagram sebab-akibat pada enam kategori (Gambar 3.1); kategori "
        "lingkungan disertakan untuk memisahkan faktor di luar kendali perusahaan dari faktor yang berada "
        "dalam kendali manajemen.")
    r.figure(os.path.join(FIG, "gambar-3-1-fishbone.png"), 12.8, "3",
             "Diagram Sebab-Akibat Keterlambatan dan Inefisiensi Jarak Tempuh",
             note="Sumber: analisis penulis. Kategori “lingkungan” tidak dijadikan dasar rekomendasi.")
    r.p("Hanya kategori lingkungan yang berada di luar kendali perusahaan dan porsinya kecil; sebagian besar "
        "penyebab bersifat *manageable*. Kategori teknologi dan data pun bukan penyebab tunggal: ketiadaan "
        "optimasi urutan adalah konsekuensi dari tidak adanya standar dan data. Temuan ini membalik urutan "
        "intervensi yang lazim diusulkan—perusahaan cenderung memulai dari pembelian perangkat lunak, padahal "
        "urutan yang benar dimulai dari standardisasi dan data. Penelusuran lima mengapa (Lampiran 3) "
        "memastikan penyebabnya **sistemik, bukan individual**: solusi berbasis sanksi tidak akan bekerja, "
        "sedangkan solusi yang mengubah sistem kerja berpotensi bekerja meskipun personelnya sama.")

    r.h2("3.3  Kebutuhan Perbaikan")
    r.p("Akar penyebab membentuk rantai ketergantungan empat lapis—standar tanpa data tidak dapat dieksekusi, "
        "data tanpa instrumen tidak dapat diproses konsisten, dan instrumen tanpa pengukuran tidak akan "
        "dirawat setelah proyek selesai. Rantai itu diterjemahkan menjadi tujuh persyaratan desain yang "
        "mengikat bagi solusi apa pun: **DR-1** urutan kunjungan mempertimbangkan jarak, kapasitas, dan "
        "jendela waktu; **DR-2** master data toko terstruktur dan tervalidasi sebagai sumber tunggal; "
        "**DR-3** visibilitas posisi dan status bagi dispatcher serta ETA bagi pelanggan; **DR-4** override "
        "manual yang tercatat; **DR-5** implementasi bertahap tanpa menghentikan operasional dalam batas "
        "Rp150 juta; **DR-6** data yang cukup untuk mengukur KPI harian; dan **DR-7** dapat dioperasikan tim "
        "yang ada tanpa ketergantungan baru pada personel kunci. Pemenuhan persyaratan ini oleh setiap "
        "alternatif disajikan pada Lampiran 3.")

    r.h2("3.4  Asumsi dan Keterbatasan Data")
    r.p("Data yang tidak tersedia dinyatakan sebagai asumsi eksplisit yang dapat diuji, bukan diisi angka "
        "rekaan. Lima asumsi paling berpengaruh: 8 titik per kendaraan per hari (A2), tingkat keterlambatan "
        "5% kiriman (A4), biaya per kejadian terlambat Rp100.000 (A5), biaya non-bahan bakar Rp5.000/km (A3), "
        "dan diskonto 12% per tahun (A14); daftar lengkap A1–A15 beserta arah dampaknya ada pada Lampiran 2. "
        "Tiga keterbatasan: struktur biaya belum mencakup biaya peluang hilangnya pelanggan, denda, dan "
        "sengketa sehingga Tabel 2.2 dibaca sebagai batas bawah; manfaat bersifat kausal-semu sehingga "
        "dikendalikan melalui uji A/B; serta model optimasi belum dapat dikalibrasi karena data koordinat dan "
        "waktu tempuh belum tersedia.")


# ============================================================ BAB IV
def bab4(r: Report):
    r.h1("BAB IV  HASIL DAN PEMBAHASAN", page_break=False)

    r.h2("4.1  Alternatif Solusi")
    r.p("Empat alternatif disusun agar mencakup spektrum lengkap—dari perbaikan non-teknologi hingga teknologi "
        "terintegrasi—karena konflik manajemen pada kasus justru terletak pada ketegangan keduanya.")
    r.p("**A1 (perbaikan prosedur)** menetapkan zonasi wilayah, SOP urutan kunjungan, master data toko pada "
        "*spreadsheet* terstruktur, dan KPI dasar tanpa perangkat berbayar. Biaya sangat rendah dan "
        "implementasi cepat, tetapi kapasitas perencanaan tetap terbatas pada dua orang dan tidak ada "
        "visibilitas posisi; memenuhi DR-1, DR-2, dan DR-7, tetapi tidak DR-3 dan DR-6.")
    r.p("**A2 (aplikasi optimasi rute standalone)** memakai aplikasi optimasi berbasis langganan untuk 20 "
        "kendaraan dan aplikasi pengemudi untuk bukti pengiriman serta pencatatan waktu tiba. Memenuhi DR-1, "
        "DR-2, DR-3, dan DR-6, tetapi perangkat komersial umumnya belum memuat data lokal sehingga usulan "
        "rute berpotensi tidak dapat dijalankan persis, dan biaya langganan membuat modal mendekati batas "
        "anggaran.")
    r.p("**A3 (platform terintegrasi)** menggabungkan TMS, telematika kendaraan, integrasi gudang dan "
        "penagihan, serta portal pelacakan pelanggan. Manfaat terbesar karena data terhubung lintas proses, "
        "tetapi modal melampaui batas investasi, implementasi melebihi 90 hari, dan teknologi ditempatkan di "
        "depan tata kelola: membangun integrasi di atas master data yang belum terstruktur berisiko "
        "menghasilkan sistem mahal dengan keputusan yang tetap salah. Gagal pada DR-5.")
    r.p("**A4 (hybrid bertahap)** menggabungkan ketiganya secara berurutan: tata kelola dan master data pada 30 "
        "hari pertama, aplikasi optimasi rute dan bukti digital dengan konfigurasi yang telah diisi data "
        "lokal, lalu visibilitas ringan berupa pelacakan posisi berbasis telepon pintar dan penyampaian ETA "
        "tanpa integrasi penuh. Tiga elemen desain membedakannya dari sekadar “membeli aplikasi”: **override "
        "manual yang tercatat** sehingga pengetahuan lokal tetap terpakai sekaligus menjadi data perbaikan "
        "model; **klaster wilayah yang relatif stabil** agar pengemudi tetap mengenal pelanggannya sementara "
        "urutan di dalam klaster dioptimasi harian; serta **pengukuran sebelum intervensi** agar manfaat "
        "dibuktikan dengan uji A/B. A4 memenuhi seluruh DR-1 sampai DR-7 secara bertahap.")

    r.h2("4.2  Penentuan Kriteria Evaluasi")
    r.p("Kriteria diturunkan dari persyaratan desain dan konflik manajemen pada kasus. Bobot tidak dibagi rata "
        "karena tidak semua kriteria sama penting pada kondisi saat ini: efisiensi 25%, kualitas layanan 20%, "
        "kepatuhan anggaran, kelayakan 90 hari, dan fleksibilitas operasional masing-masing 15%, serta "
        "skalabilitas 10%. Justifikasi setiap bobot disajikan pada Tabel 4.1; rubrik skor 1–5 diuraikan pada "
        "Lampiran 3 agar penilaian dapat direplikasi.")
    r.table(
        ["Kode", "Kriteria", "Bobot", "Justifikasi Bobot"],
        [
            ["K1", "Dampak terhadap efisiensi jarak dan biaya", "25%",
             "Kasus menetapkan target pengurangan jarak 15%; efisiensi adalah tujuan utama"],
            ["K2", "Kualitas layanan dan visibilitas (OTIF/ETA)", "20%",
             "Keluhan pelanggan dan perubahan jadwal menunjukkan layanan masalah kedua yang paling dirasakan"],
            ["K3", "Kepatuhan batas investasi Rp150 juta", "15%",
             "Batas anggaran mengikat; alternatif di atas batas tidak dapat dijalankan"],
            ["K4", "Kelayakan implementasi dalam 90 hari", "15%",
             "Masalah mendesak dan operasional tidak boleh berhenti"],
            ["K5", "Fleksibilitas operasional dan penerimaan pengguna", "15%",
             "Keberatan pengemudi dan situasi tak terduga harus diakomodasi"],
            ["K6", "Skalabilitas dan kesiapan integrasi data", "10%",
             "Penting untuk pertumbuhan, bukan prioritas 12 bulan pertama"],
            ["", "**Total**", "**100%**", ""],
        ],
        widths=[1.1, 5.0, 1.4, 8.3], chapter="4",
        title="Kriteria Evaluasi, Bobot, dan Justifikasinya",
        note="Sumber: penulis. Ketahanan bobot diuji pada Lampiran 3.",
        align=["center", "left", "center", "left"], font_size=7.5, bold_rows=(6,))

    r.h2("4.3  Perbandingan Alternatif Solusi")
    r.p("Perbandingan memakai tiga pendekatan yang saling melengkapi—kelayakan finansial, penilaian "
        "multikriteria, dan analisis sensitivitas—karena NPV tertinggi belum tentu dapat dijalankan dan skor "
        "tertinggi belum tentu layak secara finansial. Manfaat setiap alternatif dihitung dari empat komponen "
        "biaya masalah pada Tabel 2.2 dengan persentase realisasi sesuai pemenuhan persyaratan desain "
        "(rincian pada Lampiran 1).")
    r.table(
        ["Indikator", "A1 Prosedur", "A2 Aplikasi", "A3 Terintegrasi", "A4 Hybrid"],
        [
            ["Capex (Rp)", m.angka(A["A1"]["capex"]), m.angka(A["A2"]["capex"]),
             m.angka(A["A3"]["capex"]), m.angka(A["A4"]["capex"])],
            ["Opex per tahun (Rp)", m.angka(A["A1"]["opex"]), m.angka(A["A2"]["opex"]),
             m.angka(A["A3"]["opex"]), m.angka(A["A4"]["opex"])],
            ["Total manfaat per tahun (Rp)", m.angka(F["A1"]["total_manfaat"]),
             m.angka(F["A2"]["total_manfaat"]), m.angka(F["A3"]["total_manfaat"]),
             m.angka(F["A4"]["total_manfaat"])],
            ["Arus kas bersih per tahun (Rp)", m.angka(F["A1"]["arus_neto"]), m.angka(F["A2"]["arus_neto"]),
             m.angka(F["A3"]["arus_neto"]), m.angka(F["A4"]["arus_neto"])],
            ["NPV 3 tahun @12% (Rp)", m.angka(F["A1"]["npv"]), m.angka(F["A2"]["npv"]),
             m.angka(F["A3"]["npv"]), m.angka(F["A4"]["npv"])],
            ["Payback (bulan)", m.angka(F["A1"]["payback_bulan"], 1), m.angka(F["A2"]["payback_bulan"], 1),
             m.angka(F["A3"]["payback_bulan"], 1), m.angka(F["A4"]["payback_bulan"], 1)],
            ["Rasio manfaat/biaya (B/C)", m.angka(F["A1"]["rasio_manfaat_biaya"], 2),
             m.angka(F["A2"]["rasio_manfaat_biaya"], 2), m.angka(F["A3"]["rasio_manfaat_biaya"], 2),
             m.angka(F["A4"]["rasio_manfaat_biaya"], 2)],
            ["Status kelayakan", "Layak, dampak terbatas", "Layak", "Tidak layak (NPV negatif)",
             "**Layak, NPV tertinggi**"],
        ],
        widths=[4.7, 2.9, 2.6, 3.0, 2.6], chapter="4",
        title="Perbandingan Indikator Kelayakan Finansial",
        note="Sumber: perhitungan penulis. NPV = −Capex + (Manfaat − Opex) × PVIFA(12%,3); "
             "PVIFA(12%,3) = 2,4018.",
        align=["left", "right", "right", "right", "right"], font_size=7.5, bold_rows=(4,))
    r.p(f"Tiga temuan perlu ditekankan. Pertama, A3 yang paling canggih menghasilkan NPV negatif "
        f"({m.juta(F['A3']['npv'],1)}) karena modal {m.juta(A['A3']['capex'],0)} tidak tertutup manfaat "
        f"{m.juta(F['A3']['arus_neto'],1)} per tahun dalam horizon tiga tahun. Kedua, A1 memiliki B/C "
        f"tertinggi ({m.angka(F['A1']['rasio_manfaat_biaya'],2)}) dan payback tercepat "
        f"({m.angka(F['A1']['payback_bulan'],1)} bulan), tetapi manfaatnya hanya "
        f"{m.persen(F['A1']['total_manfaat']/F['A4']['total_manfaat'])} dari A4—rasio mengukur efisiensi per "
        f"rupiah, bukan besaran masalah yang diselesaikan, sehingga A1 lebih tepat diposisikan sebagai fondasi "
        f"wajib. Ketiga, A4 menghasilkan NPV tertinggi ({m.juta(F['A4']['npv'],1)}) dengan modal "
        f"{m.persen(A['A4']['capex']/m.KASUS['batas_investasi'])} dari batas investasi.")

    rows = []
    for i, (nama, bobot) in enumerate(m.KRITERIA):
        row = [f"K{i+1}", nama, f"{int(bobot*100)}%"]
        for kode in ("A1", "A2", "A3", "A4"):
            sk = m.SKOR[kode][i]
            row.append(f"{sk} ({sk*bobot:.2f})")
        rows.append(row)
    rows.append(["", "**Skor akhir tertimbang**", "**100%**"] +
                [f"**{m.angka(m.SKOR_AKHIR[k],2)}**" for k in ("A1", "A2", "A3", "A4")])
    rows.append(["", "Peringkat", "", "4", "2", "3", "1"])
    r.table(
        ["Kode", "Kriteria", "Bobot", "A1", "A2", "A3", "A4"],
        rows,
        widths=[1.1, 5.5, 1.3, 2.0, 2.0, 2.0, 1.9], chapter="4",
        title="Matriks Penilaian Multikriteria Terbobot",
        note="Sumber: perhitungan penulis. Angka dalam tanda kurung adalah kontribusi tertimbang "
             "(bobot × skor).",
        align=["center", "left", "center", "center", "center", "center", "center"], font_size=7.5,
        bold_rows=(6, 7))

    r.p(f"A3 turun ke peringkat ketiga meskipun memperoleh skor sempurna pada K1, K2, dan K6: skornya terendah "
        f"pada K3 dan K4. A3 unggul pada kriteria berorientasi hasil tetapi gagal pada kriteria berorientasi "
        f"eksekusi, dan bagi perusahaan dengan batas investasi serta larangan menghentikan operasional, "
        f"kegagalan pada kriteria eksekusi bersifat menentukan. A1 sebaliknya unggul pada eksekusi tetapi "
        f"lemah pada hasil, sedangkan A4 satu-satunya yang memadai pada keduanya—inilah alasan struktural "
        f"pemilihannya, bukan preferensi terhadap teknologi.")

    r.figure(os.path.join(FIG, "gambar-4-1-tornado.png"), 13.8, "4",
             "Analisis Sensitivitas NPV Alternatif 4",
             note="Sumber: perhitungan penulis. Batang gelap = kondisi menguntungkan, batang terang = "
                  "merugikan; garis putus-putus adalah NPV basis.")

    r.p(f"Karena sebagian parameter berasal dari asumsi, kesimpulan diuji melalui analisis sensitivitas "
        f"terhadap A4 (Gambar 4.1). NPV paling dipengaruhi persentase penurunan keterlambatan, disusul biaya "
        f"operasional sistem, lalu pengurangan jarak—parameter paling berpengaruh justru yang paling sulit "
        f"diukur. Seluruh skenario yang diuji menghasilkan NPV positif, dan titik pulang pokok tercapai bila "
        f"arus kas bersih minimal {m.juta(m.BEP_ARUS_NETO,1)} per tahun, yaitu realisasi "
        f"{m.persen(m.BEP_REALISASI)} dari proyeksi basis. Bahkan pada skenario pesimistis gabungan NPV tetap "
        f"positif sebesar {m.juta(m.SKENARIO['Pesimistis'],1)}; uji ketahanan bobot pada Lampiran 3 juga "
        f"menempatkan A4 pada peringkat pertama di semua skenario.")

    r.h2("4.4  Pemilihan Solusi Terbaik dan Justifikasi")
    r.p("**A4 (hybrid bertahap)** dipilih dengan lima argumen yang bersandar pada perhitungan sebelumnya:")
    r.numbered([
        f"**Layak dan paling menguntungkan.** NPV tiga tahun tertinggi ({m.juta(F['A4']['npv'],1)}), arus kas "
        f"bersih {m.juta(F['A4']['arus_neto'],1)} per tahun, payback {m.angka(F['A4']['payback_bulan'],1)} "
        f"bulan, B/C {m.angka(F['A4']['rasio_manfaat_biaya'],2)}.",
        f"**Mematuhi batas investasi.** Modal {m.juta(A['A4']['capex'],0)} = "
        f"{m.persen(A['A4']['capex']/m.KASUS['batas_investasi'])} dari Rp150 juta, menyisakan "
        f"{m.juta(m.KASUS['batas_investasi']-A['A4']['capex'],0)} untuk penyesuaian.",
        "**Selesai dalam 90 hari tanpa menghentikan operasional** karena setiap lapis berjalan paralel dengan "
        "operasi harian.",
        "**Menjawab keberatan pengemudi secara struktural.** Override manual yang tercatat membuat "
        "pengetahuan lokal tetap terpakai dan menjadi bahan perbaikan model—sistem belajar dari lapangan.",
        "**Menjawab keberatan keuangan dengan data.** Manfaat terbesar berasal dari penurunan keterlambatan "
        "dan waktu tunggu, dan uji A/B pada Fase 2 memberi titik henti bila manfaat tidak terbukti.",
    ])
    r.p(f"Pemilihan ini tidak meninggalkan A1 dan A2 karena keduanya komponen dari A4: yang dipilih adalah "
        f"**urutan pelaksanaan**, bukan perangkatnya. Hasil yang diharapkan pada 12 bulan pertama adalah "
        f"pengurangan jarak dari 150 km menjadi {m.angka(150*0.87,1)} km per kendaraan per hari (setara "
        f"{m.angka(B['kendaraan_setara']*0.13/0.15,2)} kendaraan penuh yang dibebaskan tanpa penambahan "
        f"armada), penurunan keterlambatan {m.persen(0.30)}, dan OTIF menuju 95%. Rancangan teknisnya "
        f"diuraikan pada Lampiran 4.")


# ============================================================ BAB V
def bab5(r: Report):
    r.h1("BAB V  PENUTUP", page_break=False)

    r.h2("5.1  Tahapan Implementasi")
    r.p("Rencana 90 hari disusun dengan prinsip tidak menghentikan operasional, sehingga setiap fase berjalan "
        "paralel dengan operasi harian dan dipisahkan titik keputusan (gate) yang mengikat: bila kriteria gate "
        "tidak terpenuhi, fase berikutnya tidak dijalankan (Tabel 5.1; jadwal rinci pada Lampiran 8).")
    r.table(
        ["Fase", "Hari", "Aktivitas Kunci", "Kriteria Gate"],
        [
            ["Fase 0\nBaseline & data", "1–14",
             "Pengukuran jarak aktual, waktu tiba, durasi bongkar muat, dan penyebab keterlambatan; "
             "pembersihan master data toko",
             "G1: min. 95% toko berdata lengkap; baseline tiga KPI tersedia"],
            ["Fase 1\nStandardisasi & konfigurasi", "15–45",
             "Zonasi wilayah, SOP rute, KPI, konfigurasi aplikasi, pelatihan berbasis pendampingan",
             "G2: usulan rute 20 kendaraan berjalan; dispatcher mandiri"],
            ["Fase 2\nPilot 5 kendaraan (A/B)", "46–70",
             "Lima kendaraan memakai sistem dan lima belas sebagai pembanding; kalibrasi parameter",
             "G3: pengurangan jarak minimal 5% lebih baik dari pembanding; OTIF tidak turun"],
            ["Fase 3\nRollout & penyerahan", "71–90",
             "Migrasi bertahap per wilayah, dashboard KPI, ritme evaluasi, serah terima",
             "G4: KPI stabil dua minggu; kepemilikan proses ditetapkan"],
        ],
        widths=[3.2, 1.4, 6.6, 4.6], chapter="5",
        title="Rincian Fase Implementasi dan Kriteria Gate",
        note="Sumber: rancangan penulis. Hari dihitung sebagai hari kalender.",
        align=["left", "center", "left", "left"], font_size=7.5)
    r.p("Pilot tidak diperlakukan sebagai uji coba teknis, melainkan alat pembuktian manfaat dan pembangunan "
        "kepercayaan—karena itu pengemudi yang terlibat dipilih dari mereka yang paling kritis terhadap "
        "aplikasi. Override manual dicatat sejak hari pertama pilot sehingga perusahaan memiliki data bagian "
        "mana dari kondisi lapangan yang belum terwakili sistem.")

    r.h2("5.2  Kebutuhan Sumber Daya")
    r.p(f"Belanja modal {m.juta(A['A4']['capex'],0)} mencakup lisensi aplikasi dan perangkat pengemudi "
        f"({m.juta(78000000,0)}), implementasi dan konfigurasi ({m.juta(25000000,0)}), pelatihan "
        f"({m.juta(12000000,0)}), serta audit baseline ({m.juta(10000000,0)}); biaya operasional "
        f"{m.juta(A['A4']['opex'],0)} per tahun didominasi langganan perangkat lunak ({m.juta(60000000,0)}) "
        f"disusul kuota data, pemeliharaan perangkat, administrasi analisis, dan pelatihan penyegaran "
        f"(Lampiran 6). Personel bersifat **realokasi, bukan penambahan**: dua dispatcher beralih peran "
        f"menjadi pengawas eksepsi dan pengelola master data, satu supervisor menjadi pemilik proses, tim TI "
        f"internal menangani integrasi dasar, dan seluruh pengemudi dilatih. Kebutuhan data diuraikan pada "
        f"Lampiran 5.")

    r.h2("5.3  Pembagian Tanggung Jawab")
    r.p("Pembagian tanggung jawab menggunakan matriks RACI agar tidak terjadi tumpang tindih kewenangan, yang "
        "pada proyek distribusi sering menjadi penyebab utama kegagalan implementasi. Direktur operasional "
        "menetapkan target dan memutuskan kelanjutan proyek; manajer operasional menjadi penanggung jawab "
        "pelaksanaan harian; dispatcher dan pengemudi menjadi pelaksana pada pengukuran baseline, pilot, dan "
        "operasi; tim TI menyediakan integrasi dasar; fungsi keuangan memverifikasi manfaat (matriks lengkap "
        "pada Lampiran 8).")

    r.h2("5.4  Identifikasi Risiko dan Mitigasi")
    r.p("Risiko diidentifikasi pada empat kategori yang disyaratkan—operasional, teknologi, sosial, dan "
        "keamanan data—lalu dinilai dengan skala kemungkinan (K) dan dampak (D) 1–5; skor adalah hasil "
        "perkaliannya (1–6 rendah, 8–12 sedang, 15–25 tinggi). Empat risiko prioritas disajikan pada Tabel "
        "5.2; register lengkap empat belas risiko ada pada Lampiran 7.")
    r.table(
        ["Kode", "Risiko", "Kategori", "K", "D", "Skor", "Mitigasi"],
        [
            ["R1", "Sistem dianggap kaku sehingga dispatcher kembali menyusun rute manual", "Operasional",
             "4", "5", "20", "Override resmi dan tercatat; target awal tidak menuntut kepatuhan 100%"],
            ["R9", "Penolakan pengemudi karena khawatir diawasi", "Sosial", "4", "4", "16",
             "GPS untuk ETA dan keselamatan, bukan sanksi; pelibatan pengemudi pada pilot"],
            ["R5", "Master data tidak akurat atau tidak lengkap saat go-live", "Teknologi", "3", "5", "15",
             "Gate G1 mengikat; validasi silang dengan pengemudi; mekanisme koreksi cepat"],
            ["R12", "Kebocoran atau penyalahgunaan data pelanggan dan posisi", "Keamanan data", "3", "5", "15",
             "Kendali akses berbasis peran; enkripsi; retensi terbatas"],
        ],
        widths=[1.1, 4.9, 1.9, 0.7, 0.7, 1.0, 5.5], chapter="5",
        title="Register Risiko Prioritas dan Mitigasi",
        note="Sumber: identifikasi penulis. Risiko berskor minimal 15 dipantau mingguan oleh manajer "
             "operasional.",
        align=["center", "left", "left", "center", "center", "center", "left"], font_size=7.5)
    r.p("Dua dari empat risiko prioritas bersifat sosial dan keamanan data, bukan teknis. Ini sejalan dengan "
        "kerangka sosio-teknis pada subbab 2.1—kegagalan proyek distribusi lebih sering disebabkan penerimaan "
        f"pengguna dan tata kelola data daripada kemampuan algoritma—sehingga anggaran pelatihan dan manajemen "
        f"perubahan {m.juta(12000000,0)} bukan pos pelengkap, melainkan mitigasi risiko utama. Mitigasi R1 "
        f"juga bersifat desain: dengan menjadikan override sebagai fitur resmi, resistensi berubah menjadi "
        f"umpan balik yang terekam.")

    r.h2("5.5  Indikator Keberhasilan (KPI)")
    r.p("KPI disusun agar terukur, dapat diatribusikan kepada solusi, memiliki sumber data yang jelas, dan "
        "memiliki *baseline*. Karena baseline belum tersedia saat laporan disusun, kolom baseline diisi status "
        "“diukur pada Fase 0” dan bukan angka rekaan—sesuai ketentuan bahwa pengukuran awal harus dilakukan "
        "sebelum implementasi (Tabel 5.3).")
    r.table(
        ["Kode", "KPI", "Baseline", "Target 90 Hari", "Target 12 Bulan"],
        [
            ["K1", "Jarak per kiriman", "18,75 km (estimasi)", "−5% dari baseline", "−13%"],
            ["K2", "On-Time In Full (OTIF)", "Diukur Fase 0", "Tidak turun", "min. 95%"],
            ["K3", "Tingkat keterlambatan", "Diukur Fase 0", "−15% relatif", "−30% relatif"],
            ["K4", "Akurasi ETA", "Belum ada ETA", "min. 70%", "min. 85%"],
            ["K5", "Waktu tunggu di lokasi", "Diukur Fase 0", "−10%", "−18%"],
            ["K6", "Waktu penyusunan rute", "Diukur Fase 0", "−20%", "−35%"],
            ["K7", "Kepatuhan penggunaan sistem", "0%", "min. 80%", "min. 95%"],
            ["K8", "Kelengkapan master data", "Diukur Fase 0", "min. 95%", "100%"],
            ["K9", "Biaya per kiriman", "Rp112.500 (estimasi)", "−4%", "−10%"],
        ],
        widths=[1.1, 4.4, 3.6, 3.3, 3.4], chapter="5",
        title="Indikator Kinerja Utama dan Target",
        note="Sumber: rancangan penulis. Target 12 bulan relatif terhadap baseline Fase 0; angka estimasi K1 "
             "dan K9 berasal dari Tabel 2.2. Definisi operasional, utilisasi kapasitas, dan emisi diuraikan "
             "pada Lampiran 8.",
        align=["center", "left", "center", "center", "center"], font_size=8)
    r.p("Tiga catatan metodologis: K2 dan K3 dipisahkan secara sengaja karena OTIF mengukur kepuasan pelanggan "
        "secara agregat sedangkan K3 mengukur frekuensi kegagalan; K7 bukan indikator teknologi melainkan "
        "indikator manajemen perubahan, dan dipantau paling awal karena menjadi prasyarat realisasi K1 sampai "
        "K6; serta seluruh KPI dihitung dari data sistem, bukan rekap manual, dan manfaat finansial pada Tabel "
        "4.2 diverifikasi ulang oleh fungsi keuangan pada bulan ke-6 dan ke-12.")


# ============================================================ BAB VI
def bab6(r: Report):
    r.h1("BAB VI  KESIMPULAN DAN SARAN", page_break=False)

    r.h2("6.1  Kesimpulan")
    r.numbered([
        "Masalah utama bukan kekurangan armada, melainkan tidak adanya sistem perencanaan dan pengendalian "
        "distribusi yang mengubah pengetahuan rute yang bersifat tacit menjadi aturan proses dan data. Akar "
        "penyebabnya sistemik: tidak ada standar pengelompokan wilayah, master data toko belum terstruktur, "
        "tidak ada instrumen optimasi dan visibilitas, serta tidak ada KPI yang membuat kinerja distribusi "
        "terlihat.",
        f"Dampak ekonomi masalah mencapai {m.juta(C['total'],0)} per tahun atau "
        f"{m.rp(C['total']/B['kiriman_tahun'])} per kiriman, dengan komponen terbesar keterlambatan "
        f"({m.persen(C['keterlambatan']/C['total'])}) dan waktu tunggu "
        f"({m.persen(C['waktu_tunggu']/C['total'])}), sedangkan bahan bakar berlebih hanya "
        f"{m.persen(C['bbm_berlebih']/C['total'])}; penghematan bahan bakar maksimum "
        f"{m.juta(C['bbm_berlebih'],1)} per tahun tidak akan cukup membenarkan investasi.",
        f"A4 (hybrid bertahap) terpilih dengan skor {m.angka(m.SKOR_AKHIR['A4'],2)}, NPV "
        f"{m.juta(F['A4']['npv'],1)}, payback {m.angka(F['A4']['payback_bulan'],1)} bulan, dan modal "
        f"{m.persen(A['A4']['capex']/m.KASUS['batas_investasi'])} dari batas investasi; A3 yang paling canggih "
        f"tidak layak secara finansial dan melampaui anggaran.",
        "Keunggulan A4 terletak pada urutan pelaksanaan: standardisasi dan master data lebih dahulu, sistem "
        "diisi data lokal, dan override manual dijadikan fitur resmi sehingga pengetahuan pengemudi tetap "
        "terpakai sekaligus menjadi bahan perbaikan model.",
        f"Rekomendasi bersifat robust: titik pulang pokok tercapai bila manfaat terealisasi "
        f"{m.persen(m.BEP_REALISASI)} dari proyeksi, dan NPV tetap positif pada skenario pesimistis gabungan "
        f"({m.juta(m.SKENARIO['Pesimistis'],1)}) maupun pada seluruh uji ketahanan bobot.",
    ])

    r.h2("6.2  Saran")
    r.p("**Bagi manajemen.** Jalankan Fase 0 sebelum keputusan pembelian apa pun; tetapkan pemilik proses pada "
        "tingkat manajerial; gunakan K7 dan K8 sebagai indikator kemajuan awal, bukan ukuran finansial; dan "
        "gunakan hasil Gate G3 sebagai dasar keputusan menuju integrasi penuh—setelah manfaat terbukti, bukan "
        "sebelum.")
    r.p("**Bagi tim operasional dan pengemudi.** Partisipasi pada Fase 0 dan Fase 2 bersifat menentukan karena "
        "data lapangan—akses masuk toko, jam penerimaan, durasi bongkar muat, dan kendala lokal—hanya dapat "
        "diperoleh dari pengalaman mereka; catatan override bukan kritik terhadap sistem, melainkan kontribusi "
        "yang memperbaiki usulan rute berikutnya.")
    r.p("**Bagi peneliti selanjutnya.** Persoalan ini dapat dimodelkan formal sebagai VRPTW dengan jendela "
        "waktu penerimaan dan durasi bongkar muat stokastik setelah data primer tersedia; evaluasi manfaat "
        "sebaiknya menggunakan rancangan eksperimen berlapis seperti pada Fase 2; dan aspek perilaku—insentif "
        "ketepatan waktu serta persepsi pengemudi terhadap pemantauan—layak diteliti terpisah.")


# ============================================================ DAFTAR PUSTAKA
def daftar_pustaka(r: Report):
    r.h1("DAFTAR PUSTAKA")
    refs = [
        "Boysen, N., Fedtke, S., & Schwerdfeger, S. (2021). Last-mile delivery concepts: A survey from an "
        "operational research perspective. *OR Spectrum*, 43(1), 1–58. "
        "https://doi.org/10.1007/s00291-020-00607-8",
        "Braekers, K., Ramaekers, K., & Van Nieuwenhuyse, I. (2016). The vehicle routing problem: State of "
        "the art classification and review. *Computers & Industrial Engineering*, 99, 300–313. "
        "https://doi.org/10.1016/j.cie.2015.12.007",
        "Christopher, M. (2016). *Logistics & supply chain management* (5th ed.). Pearson Education.",
        "Dantzig, G. B., & Ramser, J. H. (1959). The truck dispatching problem. *Management Science*, 6(1), "
        "80–91. https://doi.org/10.1287/mnsc.6.1.80",
        "Holland, C., Levis, J., Nuggehalli, R., Santilli, B., & Winters, J. (2017). UPS optimizes delivery "
        "routes. *Interfaces*, 47(1), 8–23. https://doi.org/10.1287/inte.2016.0875",
        "Nonaka, I., & Takeuchi, H. (1995). *The knowledge-creating company*. Oxford University Press.",
        "Ohno, T. (1988). *Toyota production system: Beyond large-scale production*. Productivity Press.",
        "Parasuraman, A., Zeithaml, V. A., & Berry, L. L. (1985). A conceptual model of service quality and "
        "its implications for future research. *Journal of Marketing*, 49(4), 41–50.",
        "Polanyi, M. (1966). *The tacit dimension*. Doubleday.",
        "Rushton, A., Croucher, P., & Baker, P. (2017). *The handbook of logistics and distribution "
        "management* (6th ed.). Kogan Page.",
        "Spear, S., & Bowen, H. K. (1999). Decoding the DNA of the Toyota Production System. *Harvard "
        "Business Review*, 77(5), 96–106.",
        "Toth, P., & Vigo, D. (Eds.). (2014). *Vehicle routing: Problems, methods, and applications* "
        "(2nd ed.). Society for Industrial and Applied Mathematics.",
        "Trist, E. L., & Bamforth, K. W. (1951). Some social and psychological consequences of the longwall "
        "method of coal-getting. *Human Relations*, 4(1), 3–38.",
        "BPH. (2025). *Industrial technology challenge: Studi kasus manajemen industri* [Dokumen studi "
        "kasus].",
    ]
    for ref in refs:
        par = r.p(ref, first_line_indent=False, spacing=1.15, after=6, align="justify")
        par.paragraph_format.left_indent = Cm(1.0)
        par.paragraph_format.first_line_indent = Cm(-1.0)
        for run in par.runs:
            run.font.size = Pt(10.5)


# ============================================================ LAMPIRAN
def lampiran(r: Report):
    r.h1("LAMPIRAN")

    r.h3("Lampiran 1  Rekapitulasi Perhitungan")
    r.p("Seluruh angka dihasilkan dari satu model perhitungan sehingga konsisten dan dapat diaudit. "
        "Rumus utama: NPV = −Capex + (Manfaat − Opex) × PVIFA(12%,3), dengan PVIFA = 2,4018; payback = "
        "Capex ÷ arus kas bersih; skor kriteria = Σ (bobot × skor). Tabel L1.1 merinci komponen manfaat "
        "setiap alternatif.", first_line_indent=False, size=10.5)
    rows = []
    for kode in ("A1", "A2", "A3", "A4"):
        f = F[kode]
        rows.append([A[kode]["nama"].split("(")[0].strip(),
                     m.angka(f["manfaat"]["bbm"]), m.angka(f["manfaat"]["keterlambatan"]),
                     m.angka(f["manfaat"]["perencanaan"]), m.angka(f["manfaat"]["tunggu"]),
                     m.angka(f["total_manfaat"]), m.angka(A[kode]["opex"]),
                     m.angka(f["arus_neto"]), m.angka(f["npv"])])
    r.table(
        ["Alternatif", "Manfaat BBM", "Manfaat Terlambat", "Manfaat Perencanaan", "Manfaat Waktu Tunggu",
         "Total Manfaat", "Opex", "Arus Kas", "NPV 3 Th"],
        rows,
        widths=[3.1, 1.5, 1.6, 1.7, 1.6, 1.5, 1.3, 1.4, 1.5], chapter="L1",
        title="Rincian Komponen Manfaat, Arus Kas, dan NPV per Alternatif (Rp/tahun)",
        note="Sumber: perhitungan penulis. Persentase realisasi manfaat: A1 5/15/20/10; A2 10/30/30/15; "
             "A3 15/35/50/20; A4 13/30/35/18 (BBM/keterlambatan/perencanaan/waktu tunggu).",
        align=["left"] + ["right"] * 8, font_size=7)
    r.p(f"Dampak ekonomi masalah: bahan bakar berlebih {m.rp(C['bbm_berlebih'])}; keterlambatan "
        f"{m.rp(C['keterlambatan'])}; waktu tunggu {m.rp(C['waktu_tunggu'])}; produktivitas perencanaan "
        f"{m.rp(C['perencanaan_manual'])}; total {m.rp(C['total'])} per tahun "
        f"({m.rp(C['total']/20)} per kendaraan; {m.rp(C['total']/m.ASUMSI['A1_hari_operasi_tahun'])} per "
        f"hari operasi). Rekonsiliasi: 15% × {m.angka(B['km_tahun'])} km = {m.angka(B['km_hemat_target'])} "
        f"km = {m.angka(B['liter_hemat_target'])} liter = {m.rp(B['rp_hemat_bbm_target'])}; setara "
        f"{m.angka(B['kendaraan_setara'])} kendaraan dan {m.angka(B['co2_hemat_ton'],1)} ton CO2e.",
        first_line_indent=False, size=10.5, space_before=4)
    r.p("Titik pulang pokok A4: arus kas bersih minimum "
        f"{m.rp(m.BEP_ARUS_NETO)}/tahun = total manfaat {m.rp(m.BEP_MANFAAT)}/tahun = "
        f"{m.persen(m.BEP_REALISASI)} realisasi. Skenario: optimis {m.rp(m.SKENARIO['Optimis'])}; basis "
        f"{m.rp(m.SKENARIO['Basis'])}; pesimistis {m.rp(m.SKENARIO['Pesimistis'])}.", 
        first_line_indent=False, size=10.5)

    r.h3("Lampiran 2  Daftar Asumsi")
    r.p("Asumsi diberi kode A1–A15, dinyatakan terbuka, dan digantikan hasil pengukuran Fase 0. Arah "
        "dampak menunjukkan pengaruh perubahan nilai terhadap kesimpulan.", first_line_indent=False, size=10.5)
    r.table(
        ["Kode", "Asumsi", "Nilai", "Dasar Penetapan", "Dampak bila Berbeda"],
        [
            ["A1", "Hari operasi per tahun", "312 hari", "26 hari/bulan × 12 (data kasus)",
             "Proporsional terhadap seluruh nilai tahunan"],
            ["A2", "Titik pengiriman per kendaraan/hari", "8 titik", "Kisaran lazim rute distribusi toko",
             "Mengubah jumlah kiriman dan biaya per kiriman"],
            ["A3", "Biaya non-bahan bakar per km", "Rp5.000/km",
             "Pengemudi, penyusutan, perawatan, asuransi", "Mengubah nilai kapasitas yang dibebaskan"],
            ["A4", "Tingkat keterlambatan", "5% kiriman", "Kisaran umum tanpa manajemen jendela waktu",
             "Komponen biaya terbesar; wajib diukur pada Fase 0"],
            ["A5", "Biaya per kejadian terlambat", "Rp100.000",
             "Komunikasi ulang, penjadwalan ulang, potongan harga", "Proporsional terhadap manfaat K3"],
            ["A6", "Jumlah dispatcher", "2 orang", "Narasi kasus", "Mengubah nilai biaya perencanaan"],
            ["A7", "Biaya dispatcher per bulan", "Rp7.000.000", "Upah dan beban posisi staf perencanaan",
             "Proporsional terhadap manfaat efisiensi perencanaan"],
            ["A8", "Porsi waktu untuk perencanaan rute", "40%", "Sisanya koordinasi dan administrasi",
             "Batas atas penghematan waktu perencanaan"],
            ["A9", "Porsi titik yang tertunda", "20%", "Konsisten dengan narasi perubahan jadwal toko",
             "Proporsional terhadap biaya waktu tunggu"],
            ["A10", "Waktu tunggu per titik tertunda", "0,4 jam", "Perkiraan bongkar dan verifikasi dokumen",
             "Proporsional terhadap biaya waktu tunggu"],
            ["A11", "Jam kerja pengemudi per hari", "10 jam", "Termasuk bongkar muat dan perjalanan",
             "Mengubah tarif jam dan nilai waktu tunggu"],
            ["A12", "Biaya pengemudi per bulan", "Rp10.000.000", "Upah, tunjangan, dan beban",
             "Proporsional terhadap nilai waktu tunggu"],
            ["A13", "Faktor emisi diesel", "2,68 kg CO2e/liter", "Faktor emisi pembakaran",
             "Hanya memengaruhi perhitungan emisi"],
            ["A14", "Tingkat diskonto tahunan", "12%", "Kisaran biaya modal perusahaan distribusi",
             "Diskonto lebih tinggi menurunkan NPV, tidak mengubah peringkat"],
            ["A15", "Horizon evaluasi", "3 tahun", "Umur ekonomis perangkat lunak",
             "Horizon lebih panjang menaikkan NPV seluruh alternatif"],
        ],
        widths=[1.0, 3.8, 2.3, 4.3, 4.4], chapter="L2",
        title="Daftar Asumsi dan Batasannya",
        note="Sumber: penulis.",
        align=["center", "left", "center", "left", "left"], font_size=7.5)

    r.h3("Lampiran 3  Lima Mengapa, Pemenuhan Persyaratan Desain, Rubrik, dan Uji Ketahanan")
    r.p("Penelusuran akar penyebab dengan teknik lima mengapa (Tabel L3.1) memastikan bahwa penyebab yang "
        "diidentifikasi bersifat mendasar dan berada dalam kendali manajemen.",
        first_line_indent=False, size=10.5)
    r.table(
        ["Tingkat", "Pertanyaan", "Jawaban Berbasis Bukti Kasus"],
        [
            ["Mengapa 1", "Mengapa kendaraan menempuh jarak tidak perlu?",
             "Urutan kunjungan tidak mengikuti kedekatan lokasi sehingga kendaraan kembali melewati jalan "
             "yang sama"],
            ["Mengapa 2", "Mengapa urutan tidak mengikuti kedekatan lokasi?",
             "Rute disusun manual mengikuti urutan masuknya pesanan—cara tercepat yang tersedia bagi "
             "dispatcher"],
            ["Mengapa 3", "Mengapa masih manual meski volume meningkat?",
             "Tidak ada alat dan standar pengelompokan; kapasitas perencanaan terbatas pada dua orang dan "
             "tertekan pada jam sibuk"],
            ["Mengapa 4", "Mengapa tidak ada alat dan standar?",
             "Pengetahuan rute bersifat tacit dan tidak pernah dieksternalisasi menjadi master data, aturan "
             "clustering, atau prosedur baku"],
            ["Mengapa 5", "Mengapa tidak pernah dieksternalisasi? (akar penyebab)",
             "Tidak ada KPI jarak, waktu, dan ketepatan waktu, sehingga tidak ada tekanan maupun umpan "
             "balik yang memicu perbaikan; lingkaran evaluasi terputus"],
        ],
        widths=[1.9, 5.4, 8.5], chapter="L3",
        title="Penelusuran Akar Penyebab dengan Teknik Lima Mengapa",
        note="Sumber: analisis penulis. Baris terakhir merupakan akar penyebab yang menjadi dasar "
             "kebutuhan perbaikan pada subbab 3.3.",
        align=["center", "left", "left"], font_size=8, bold_rows=(4,))


    r.table(
        ["Persyaratan Desain", "A1", "A2", "A3", "A4"],
        [
            ["DR-1 Urutan kunjungan berbasis jarak, kapasitas, jendela waktu", "Sebagian", "Ya", "Ya", "Ya"],
            ["DR-2 Master data terstruktur sebagai sumber tunggal", "Sebagian", "Ya", "Ya", "Ya"],
            ["DR-3 Visibilitas posisi dan ETA kepada pelanggan", "Tidak", "Ya", "Ya", "Ya (bertahap)"],
            ["DR-4 Override manual tercatat", "Ya", "Sebagian", "Sebagian", "Ya"],
            ["DR-5 Bertahap, tanpa henti operasi, ≤Rp150 juta", "Ya", "Sebagian", "Tidak", "Ya"],
            ["DR-6 Data cukup untuk pengukuran KPI harian", "Sebagian", "Ya", "Ya", "Ya"],
            ["DR-7 Dapat dioperasikan tim yang ada", "Ya", "Ya", "Sebagian", "Ya"],
        ],
        widths=[8.4, 1.9, 1.9, 1.9, 1.7], chapter="L3",
        title="Pemenuhan Persyaratan Desain oleh Setiap Alternatif",
        note="Sumber: analisis penulis. “Sebagian” berarti terpenuhi untuk sebagian kasus atau memerlukan "
             "pekerjaan tambahan di luar lingkup alternatif.",
        align=["left", "center", "center", "center", "center"], font_size=8)
    r.p("Rubrik skor 1–5: **5** memenuhi seluruh aspek secara langsung tanpa pekerjaan tambahan dan dapat "
        "diverifikasi dengan data; **4** memenuhi sebagian besar aspek dengan kekurangan minor; **3** "
        "memenuhi secara formal tetapi menuntut pekerjaan tambahan atau kompromi signifikan; **2** hanya "
        "memenuhi sebagian kecil aspek; **1** tidak memenuhi atau bertentangan dengan batasan.",
        first_line_indent=False, size=10.5, space_before=4)
    rows = []
    for nama, hasil in m.SKENARIO_BOBOT_HASIL.items():
        terbaik = max(hasil, key=hasil.get)
        rows.append([nama] + [m.angka(hasil[k], 2) for k in ("A1", "A2", "A3", "A4")] + [terbaik])
    r.table(
        ["Skenario Bobot", "A1", "A2", "A3", "A4", "Peringkat 1"],
        rows,
        widths=[6.4, 1.8, 1.8, 1.8, 1.8, 2.0], chapter="L3",
        title="Uji Ketahanan Peringkat terhadap Perubahan Bobot",
        note="Sumber: perhitungan penulis. Alternatif 4 tetap pada peringkat pertama pada seluruh skenario.",
        align=["left", "center", "center", "center", "center", "center"], font_size=8.5)

    r.h3("Lampiran 4  Uraian Rancangan Solusi Terpilih")
    r.p("**Klaster wilayah dan urutan harian.** Wilayah layanan dibagi menjadi klaster relatif stabil "
        "berdasarkan kedekatan lokasi, kepadatan pesanan, dan akses jalan. Klaster menjaga pengemudi tetap "
        "mengenal pelanggan dan kondisi lokal, sedangkan urutan kunjungan di dalam klaster dioptimasi "
        "setiap hari berdasarkan jarak, kapasitas muatan, dan jendela waktu. Pemisahan ini menjawab "
        "kekhawatiran pengemudi tanpa mengorbankan efisiensi.", first_line_indent=False, size=10.5)
    r.p("**Mekanisme override dan pembelajaran.** Dispatcher dapat menimpa usulan sistem dengan memilih "
        "alasan terstruktur (akses ditutup, toko tutup lebih awal, kemacetan, kondisi kendaraan). Setiap "
        "penimpaan tercatat dan direkap mingguan; alasan yang berulang menjadi kandidat parameter baru "
        "(misalnya penambahan durasi layanan atau larangan jam pada lokasi tertentu). Dengan cara ini "
        "pengetahuan tacit berpindah ke sistem secara bertahap tanpa memaksa pengguna mengikuti rencana "
        "yang tidak realistis.", first_line_indent=False, size=10.5)
    r.p("**Penyampaian ETA dan penanganan eksepsi.** ETA dikirim kepada pelanggan pada pagi hari dalam "
        "bentuk rentang waktu, diperbarui bila deviasi melebihi ambang tertentu. Dispatcher memantau papan "
        "eksepsi: kiriman yang diproyeksikan melewati jendela waktu diberi tindakan (hubungi pelanggan, "
        "ubah urutan, atau realokasi). Protokol ini mengubah keterlambatan dari kejadian yang baru "
        "diketahui setelah terjadi menjadi kejadian yang dikelola sebelum terjadi.",
        first_line_indent=False, size=10.5)
    r.p("**Rancangan uji A/B.** Lima kendaraan kelompok uji dan lima belas kelompok pembanding dipilih acak "
        "berlapis menurut wilayah; KPI dibandingkan dengan uji Mann-Whitney pada tingkat signifikansi 5%. "
        "Kriteria keberhasilan gate bersifat ganda—efisiensi membaik dan layanan tidak memburuk—agar "
        "penghematan tidak diperoleh dengan mengorbankan ketepatan waktu.",
        first_line_indent=False, size=10.5)

    r.h3("Lampiran 5  Data yang Belum Tersedia dan Cara Pengumpulannya")
    r.table(
        ["No", "Data", "Kegunaan", "Metode Pengumpulan", "Sumber", "Waktu"],
        [
            ["1", "Koordinat dan titik akses toko", "Dasar jarak dan clustering",
             "Survei lapangan dan pencatatan GPS", "Tim distribusi + pengemudi", "Fase 0"],
            ["2", "Jam penerimaan dan jendela waktu", "Batasan waktu pada model rute",
             "Wawancara terstruktur dan verifikasi kunjungan", "Sales dan toko", "Fase 0"],
            ["3", "Durasi bongkar muat per toko", "Estimasi waktu layanan per titik",
             "Pengukuran langsung selama 10 hari", "Pengemudi", "Fase 0"],
            ["4", "Jarak dan waktu tempuh aktual", "Baseline K1, K5, K7",
             "Odometer dan GPS; rekap harian", "Armada", "Fase 0"],
            ["5", "Tingkat dan penyebab keterlambatan", "Baseline K3 dan kalibrasi manfaat",
             "Log keterlambatan dengan kategori penyebab", "Dispatcher + pengemudi", "Fase 0"],
            ["6", "Kapasitas muatan per kendaraan", "Batasan kapasitas optimasi",
             "Dokumen spesifikasi kendaraan", "Bagian teknik", "Fase 0"],
            ["7", "Struktur biaya non-bahan bakar", "Validasi A3 dan K10",
             "Data akuntansi: penyusutan, perawatan, asuransi, upah", "Keuangan", "Fase 0"],
            ["8", "Riwayat rute 3–6 bulan", "Analisis pola dan pembanding",
             "Ekstraksi arsip daftar pesanan dan lembar rute", "Dispatcher", "Fase 0"],
            ["9", "Kendala khusus per lokasi", "Aturan override dan parameter",
             "FGD dengan pengemudi senior", "Pengemudi", "Fase 1"],
            ["10", "Harapan pelanggan atas ketepatan waktu", "Penetapan janji waktu dan target K2",
             "Survei singkat 30 pelanggan utama", "Pelanggan ritel", "Fase 1"],
        ],
        widths=[0.8, 3.4, 3.2, 4.2, 2.6, 1.4], chapter="L5",
        title="Daftar Data yang Perlu Dikumpulkan Sebelum Implementasi",
        note="Sumber: rancangan penulis. Seluruh data ini menggantikan asumsi A2 serta A4–A12.",
        align=["center", "left", "left", "left", "left", "center"], font_size=7.5)

    r.h3("Lampiran 6  Rincian Biaya")
    r.table(
        ["Komponen Belanja Modal (Capex)", "Nilai (Rp)", "Komponen Biaya Operasional (Opex/tahun)",
         "Nilai (Rp)"],
        [
            ["Lisensi aplikasi optimasi dan aplikasi pengemudi (20 kendaraan, tahun pertama)",
             "60.000.000", "Langganan perangkat lunak (20 kendaraan)", "60.000.000"],
            ["Implementasi, konfigurasi master data, integrasi dasar", "25.000.000",
             "Kuota data dan komunikasi", "14.000.000"],
            ["Perangkat pengemudi: 12 unit telepon pintar/tablet, dudukan, pengisi daya", "18.000.000",
             "Pemeliharaan dan penggantian perangkat", "10.000.000"],
            ["Pelatihan dan manajemen perubahan", "12.000.000",
             "Administrasi distribusi dan analisis data (0,5 FTE)", "9.000.000"],
            ["Audit baseline dan pengukuran awal", "10.000.000",
             "Pelatihan penyegaran dan audit kepatuhan", "6.000.000"],
            ["**Total capex**", f"**{m.angka(A['A4']['capex'])}**", "**Total opex**",
             f"**{m.angka(A['A4']['opex'])}**"],
        ],
        widths=[5.5, 2.4, 5.4, 2.5], chapter="L6",
        title="Rincian Belanja Modal dan Biaya Operasional Alternatif 4",
        note="Sumber: estimasi penulis; harga aktual dikonfirmasi melalui penawaran vendor pada Fase 1.",
        align=["left", "right", "left", "right"], font_size=7.5, bold_rows=(5,))

    r.h3("Lampiran 7  Register Risiko Lengkap")
    r.table(
        ["Kode", "Risiko", "Kategori", "K", "D", "Skor", "Mitigasi"],
        [
            ["R1", "Sistem dianggap kaku sehingga dispatcher kembali menyusun rute manual", "Operasional",
             "4", "5", "20", "Override resmi dan tercatat; tinjauan harian atas penimpaan"],
            ["R2", "Keterlambatan tetap terjadi karena faktor eksternal", "Operasional", "4", "3", "12",
             "ETA berbasis rentang; protokol pemberitahuan dini"],
            ["R3", "Rollout mengganggu pengiriman harian", "Operasional", "2", "5", "10",
             "Migrasi bertahap per wilayah; kapasitas cadangan"],
            ["R4", "Manfaat tidak terealisasi karena kembali ke kebiasaan lama", "Operasional", "3", "4", "12",
             "KPI masuk penilaian kinerja; audit kepatuhan bulanan"],
            ["R5", "Master data tidak akurat saat go-live", "Teknologi", "3", "5", "15",
             "Gate G1 mengikat; validasi silang; koreksi cepat"],
            ["R6", "Integrasi dengan sistem lama gagal atau menunda jadwal", "Teknologi", "3", "3", "9",
             "Integrasi dasar saja; integrasi penuh ditunda ke G4"],
            ["R7", "Kualitas usulan rute rendah pada awal penggunaan", "Teknologi", "4", "3", "12",
             "Kalibrasi parameter pada pilot; pembelajaran dari override"],
            ["R8", "Ketergantungan berlebih pada satu vendor", "Teknologi", "3", "3", "9",
             "Data dapat diekspor; klausul kepemilikan data; evaluasi tahunan"],
            ["R9", "Penolakan pengemudi karena khawatir diawasi", "Sosial", "4", "4", "16",
             "GPS untuk ETA dan keselamatan, bukan sanksi; pelibatan pengemudi"],
            ["R10", "Beban kerja baru bagi dispatcher pada masa transisi", "Sosial", "3", "3", "9",
             "Pelatihan bertahap; target sementara diturunkan"],
            ["R11", "Kesenjangan keterampilan digital", "Sosial", "3", "3", "9",
             "Pendampingan lapangan dan pendampingan sebaya"],
            ["R12", "Kebocoran atau penyalahgunaan data pelanggan dan posisi", "Keamanan data", "3", "5", "15",
             "Kendali akses berbasis peran; enkripsi; retensi terbatas"],
            ["R13", "Kehilangan data akibat kegagalan perangkat atau vendor", "Keamanan data", "2", "5", "10",
             "Pencadangan otomatis harian; ekspor berkala"],
            ["R14", "Perubahan lingkup tidak terkendali", "Teknologi", "4", "3", "12",
             "Batas lingkup 90 hari; permintaan baru dievaluasi pada G4"],
        ],
        widths=[1.0, 5.4, 1.9, 0.7, 0.7, 1.0, 5.1], chapter="L7",
        title="Register Risiko Lengkap dengan Penilaian dan Mitigasi",
        note="Sumber: identifikasi penulis. K = kemungkinan, D = dampak (skala 1–5); skor = K × D. "
             "1–6 rendah, 8–12 sedang, 15–25 tinggi.",
        align=["center", "left", "left", "center", "center", "center", "left"], font_size=7)


    r.h3("Lampiran 8  Jadwal, RACI, dan Definisi Operasional KPI")
    r.p("Jadwal implementasi 90 hari beserta empat titik keputusan (gate) disajikan pada Gambar L8.1. "
        "Seluruh tanggal dihitung sebagai hari kalender sejak keputusan proyek diambil.",
        first_line_indent=False, size=10.5)
    r.figure(os.path.join(FIG, "gambar-5-1-gantt.png"), 14.5, "L8",
             "Jadwal Implementasi 90 Hari dan Titik Keputusan (Gate)",
             note="Sumber: rancangan penulis.")
    r.p("Matriks RACI memastikan setiap aktivitas memiliki tepat satu pihak *Accountable*, sehingga tidak "
        "terjadi tumpang tindih kewenangan (Tabel L8.1).",
        first_line_indent=False, size=10.5)
    r.table(
        ["Aktivitas Kunci", "Dir. Ops", "Mgr. Ops", "Dispatcher", "Pengemudi", "Tim TI", "Keuangan"],
        [
            ["Penetapan target dan anggaran", "A", "R", "I", "I", "I", "C"],
            ["Pengukuran baseline dan master data", "I", "A", "R", "C", "C", "I"],
            ["Zonasi wilayah dan SOP rute", "I", "A", "R", "C", "I", "I"],
            ["Pemilihan dan konfigurasi sistem", "I", "A", "C", "I", "R", "C"],
            ["Pelatihan dispatcher dan pengemudi", "I", "A", "C", "R", "C", "I"],
            ["Pilot dan uji A/B", "I", "A", "R", "R", "C", "I"],
            ["Evaluasi pilot dan keputusan lanjut", "A", "R", "C", "C", "C", "C"],
            ["Rollout dan stabilisasi operasi", "I", "A", "R", "R", "C", "I"],
            ["Pemantauan KPI dan tinjauan berkala", "A", "R", "C", "I", "C", "I"],
            ["Verifikasi manfaat finansial", "I", "C", "I", "I", "I", "A"],
        ],
        widths=[6.2, 1.7, 1.7, 1.7, 1.7, 1.3, 1.5], chapter="L8",
        title="Matriks RACI Implementasi",
        note="Sumber: rancangan penulis. R = pelaksana, A = penanggung jawab akhir, C = dimintai pendapat, "
             "I = diberi informasi.",
        align=["left", "center", "center", "center", "center", "center", "center"], font_size=8)
    r.p("Definisi operasional KPI disamakan agar pengukuran konsisten antar periode dan antar pengukur "
        "(Tabel L8.2). Seluruh KPI dihitung dari data sistem, bukan rekap manual.",
        first_line_indent=False, size=10.5)
    r.table(
        ["Kode", "KPI", "Definisi Operasional", "Sumber Data", "Frekuensi"],
        [
            ["K1", "Jarak per kiriman", "Total km armada ÷ jumlah kiriman selesai", "Odometer/GPS", "Harian"],
            ["K2", "OTIF", "% kiriman tiba dalam jendela waktu dan lengkap (kuantitas dan kondisi)",
             "Aplikasi pengemudi", "Harian"],
            ["K3", "Tingkat keterlambatan", "% kiriman tiba di luar komitmen waktu", "Aplikasi pengemudi",
             "Harian"],
            ["K4", "Akurasi ETA", "% kiriman tiba dalam rentang ETA yang dikirim ke pelanggan",
             "Log ETA + waktu tiba", "Harian"],
            ["K5", "Waktu tunggu", "Rata-rata jam tunggu di lokasi per titik", "Aplikasi pengemudi", "Harian"],
            ["K6", "Waktu penyusunan rute", "Jam perencanaan per hari (mulai sampai rute final)",
             "Log sistem/dispatcher", "Harian"],
            ["K7", "Kepatuhan penggunaan sistem", "% rute dijalankan sesuai rencana sistem atau override tercatat",
             "Log sistem", "Harian"],
            ["K8", "Kelengkapan master data", "% toko aktif dengan data lengkap dan tervalidasi",
             "Audit master data", "Bulanan"],
            ["K9", "Biaya per kiriman", "Biaya transportasi (BBM + non-BBM) ÷ jumlah kiriman",
             "Akuntansi + operasi", "Bulanan"],
            ["K10", "Utilisasi kapasitas", "% pemakaian kapasitas muatan per rute", "Manifest + kapasitas",
             "Harian"],
            ["K11", "Emisi CO2e", "Liter bahan bakar × faktor emisi (A13)", "Pencatatan BBM", "Bulanan"],
        ],
        widths=[1.1, 3.3, 6.0, 3.4, 2.0], chapter="L8",
        title="Definisi Operasional, Sumber Data, dan Frekuensi Pengukuran KPI",
        note="Sumber: rancangan penulis.",
        align=["center", "left", "left", "left", "center"], font_size=7.5)

# ============================================================ MAIN
TOC_ENTRIES = os.path.join(HERE, "..", "output", "toc-entries.json")


def load_toc():
    """Entri daftar isi hasil pass sebelumnya (level, teks, halaman)."""
    if os.path.exists(TOC_ENTRIES):
        import json
        with open(TOC_ENTRIES, encoding="utf-8") as f:
            return [tuple(e) for e in json.load(f)]
    return None


def main():
    r = Report()
    r.setup_properties(
        title="Armada Banyak, Pengiriman Tetap Terlambat — Laporan Studi Kasus 4",
        subject="Analisis Efisiensi Distribusi dan Kualitas Layanan pada Perusahaan Distribusi "
                "Barang Konsumsi (Supply Chain & Distribution)",
        author="[Nama Mahasiswa]",
        keywords="optimasi rute; keterlambatan pengiriman; ETA; tata kelola data; supply chain",
        comments="Laporan Studi Kasus Manajemen Industri — Industrial Technology Challenge",
    )
    sampul(r)
    entries = load_toc()
    if entries:
        r.toc(entries)
    ringkasan(r)
    bab1(r)
    bab2(r)
    bab3(r)
    bab4(r)
    bab5(r)
    bab6(r)
    daftar_pustaka(r)
    lampiran(r)
    r.enable_field_update()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    r.save(OUT)
    print("Laporan tersimpan:", os.path.abspath(OUT))


if __name__ == "__main__":
    main()
