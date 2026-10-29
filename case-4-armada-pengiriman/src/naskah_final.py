# -*- coding: utf-8 -*-
"""Naskah laporan final Studi Kasus 4 (tanpa lampiran).

Satu blok = satu baris string, agar penyuntingan tepat.
Target: isi BAB I-VI tidak melebihi 8 halaman A4 (TNR 12, spasi 1,5, margin 2,54 cm).
"""

B = []

B.append(("h1", "BAB I  PENDAHULUAN"))
B.append(("h2", "1.1  Latar Belakang"))
B.append(("p", "Ketepatan rute memengaruhi konsumsi bahan bakar, biaya kerja, dan arus persediaan (Christopher, 2016).", True, 12))
B.append(("p", "Perusahaan pada studi kasus ini mengoperasikan 20 kendaraan setiap hari untuk mengirim barang ke toko ritel dan pelanggan bisnis. Rute ditentukan dispatcher berdasarkan pengalaman, masih manual dengan peta dan daftar pesanan (BPH, 2025). Ketika pesanan bertambah, beberapa kendaraan melewati wilayah berdekatan pada hari yang sama, kendaraan lain menempuh jarak lebih jauh karena urutan kunjungan tidak optimal, dan keterlambatan baru diketahui setelah pengemudi menelepon. Pelanggan tidak memperoleh perkiraan waktu kedatangan yang akurat sehingga waktu tunggu bertambah. Persoalannya karena itu bukan jumlah armada, melainkan perencanaan rute dan pemantauan pengiriman.", True, 12))
B.append(("h2", "1.2  Identifikasi Masalah"))
B.append(("bul", ["Rute disusun manual berdasarkan pengalaman, peta, dan urutan pesanan masuk.", "Urutan kunjungan belum mempertimbangkan kedekatan lokasi, jam penerimaan, dan waktu bongkar.", "Posisi kendaraan tidak terpantau sehingga keterlambatan diketahui setelah pengemudi menelepon.", "Pelanggan tidak menerima perkiraan waktu kedatangan yang akurat.", "Pengetahuan rute hanya ada pada dua dispatcher dan belum menjadi data."]))
B.append(("h2", "1.3  Rumusan Masalah"))
B.append(("num", ["Apa masalah utama dan akar penyebab tidak optimalnya rute serta lambatnya informasi keterlambatan?", "Berapa biaya akibat masalah dan potensi penghematan bahan bakar pada target 15%?", "Alternatif mana yang paling tepat ditinjau dari jarak, biaya, layanan, pagu, waktu, dan penerimaan pengguna?", "Bagaimana solusi dilaksanakan dalam 90 hari, risiko apa yang menyertainya, dan bagaimana keberhasilannya diukur?"]))
B.append(("h2", "1.4  Tujuan Analisis"))
B.append(("p", "Analisis bertujuan menemukan masalah dan akar penyebabnya, menghitung biaya akibat masalah, membandingkan minimal tiga alternatif dengan kriteria terbuka, memilih alternatif terbaik beserta justifikasinya, lalu menyusun rencana 90 hari, mitigasi risiko, dan indikator keberhasilan.", True, 12))
B.append(("h2", "1.5  Ruang Lingkup dan Batasan"))
B.append(("p", "Pembahasan dibatasi pada perencanaan rute, pemantauan perjalanan, perkiraan waktu kedatangan (ETA), dan koordinasi dispatcher–pengemudi. Data yang tersedia hanya jumlah kendaraan, jarak rata-rata, hari operasi, konsumsi bahan bakar, harga simulasi, target, dan batas investasi; sisanya menjadi asumsi terbuka pada Tabel 3.2. Denda dan kehilangan pelanggan tidak dinilai dalam rupiah.", True, 12))
B.append(("h1", "BAB II  LANDASAN TEORI"))
B.append(("h2", "2.1  Kajian Teori"))
B.append(("p", "Vehicle Routing Problem with Time Windows (VRPTW) menentukan urutan kunjungan sejumlah kendaraan agar pelanggan terlayani dalam jendela waktu tertentu dengan meminimalkan jarak, biaya, atau waktu tempuh (Braekers dkk., 2016). Pada pengiriman jarak pendek, jendela waktu, waktu bongkar, dan akses lokasi ikut menentukan apakah rute dapat dijalankan (Boysen dkk., 2021). Dua implikasinya: manfaat optimasi hanya muncul bila data lokasi dan waktu layanan terintegrasi (Holland dkk., 2017), dan teknologi tidak menggantikan pengetahuan lokal karena standar kerja membuat penyimpangan terlihat lebih cepat (Spear & Bowen, 1999).", True, 12))
B.append(("h2", "2.2  Penelitian yang Relevan (Identifikasi Fakta dan Data Kasus)"))
B.append(("p", "Dantzig dan Ramser (1959) merumuskan masalah penugasan truk, dan Braekers dkk. (2016) memetakan perkembangannya. Bukti penerapan berskala besar datang dari UPS: setelah sistem ORION diterapkan, perusahaan melaporkan pengurangan sekitar 100 juta mil tempuh dan penghematan lebih dari USD300 juta per tahun (Holland dkk., 2017). Keberhasilan itu tidak berasal dari algoritma semata, melainkan dari kelengkapan data pelanggan, alamat, dan waktu layanan yang dibangun lebih dahulu.", True, 12))
B.append(("p", "Fakta kasus sejalan: persoalannya perencanaan, tetapi data toko belum rapi dan standar kerja belum tertulis. Data kasus hanya memuat 20 kendaraan, 150 km per hari, 26 hari operasi per bulan, konsumsi 1 liter per 10 km, harga simulasi Rp10.000 per liter, target 15%, dan pagu Rp150 juta; sisanya asumsi pada subbab 3.4.", True, 12))
B.append(("h2", "2.3  Kerangka Berpikir (Gambaran Proses Operasional Saat Ini)"))
B.append(("p", "Pengiriman berjalan dalam empat tahap: pesanan diterima, dispatcher menyusun rute manual, pengemudi menjalankan rute, lalu pelanggan menerima barang. Kegagalan terjadi pada tahap kedua dan ketiga: urutan kunjungan mengikuti pesanan masuk sehingga kendaraan kembali melewati jalan yang sama, sementara posisi kendaraan tidak terpantau sehingga kemacetan tidak terlihat dari kantor. Rantai informasi inilah yang harus diperbaiki sebelum algoritma rute ditambahkan.", True, 12))
B.append(("fig", "fig_alur.png", 15.9, 3.9, "Gambar 2.1  Alur proses operasional saat ini dan titik kegagalannya"))
B.append(("h2", "2.4  Dampak Permasalahan"))
B.append(("p", "Dua puluh kendaraan menempuh 150 km per hari sehingga jarak harian 3.000 km atau 936.000 km per tahun pada 312 hari operasi. Dengan konsumsi 1 liter per 10 km, kebutuhan bahan bakar 93.600 liter per tahun senilai Rp936 juta. Bila tiap kendaraan melayani 8 titik, jumlah kiriman 49.920 per tahun dan biaya bahan bakar Rp18.750 per kiriman. Biaya akibat masalah dihitung sebagai cost of poor performance, yaitu nilai yang hilang setiap tahun pada kondisi sekarang (Tabel 2.1). Jumlah 49.920 kiriman berasal dari 20 kendaraan × 8 titik × 312 hari.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 2.1  Biaya Akibat Masalah per Tahun",
    headers=["Komponen", "Cara menghitung", "Nilai (Rp)", "Porsi"],
    widths=[3.7, 7.4, 2.9, 1.9],
    size=8,
    rows=[
        ["Potensi pemborosan bahan bakar", "15% × 936.000 km ÷ 10 × Rp10.000", "140.400.000", "23,0%"],
        ["Keterlambatan", "5% × 49.920 kiriman × Rp100.000", "249.600.000", "40,9%"],
        ["Waktu tunggu", "12,8 jam/hari × Rp38.462 × 312 hari", "153.600.000", "25,1%"],
        ["Perencanaan manual", "40% × 2 orang × Rp7.000.000 × 12 bulan", "67.200.000", "11,0%"],
        ["Jumlah", "—", "610.800.000", "100%"],
    ],
    note="Sumber: perhitungan penulis; asumsi pada Tabel 3.2.",
)))
B.append(("p", "Temuan pentingnya bukan besarnya angka, melainkan komposisinya. Keterlambatan (40,9%) dan waktu tunggu (25,1%) menyumbang 66,0% biaya, sedangkan bahan bakar hanya 23,0%, sehingga penghematan bahan bakar tidak cukup membenarkan pembelian sistem yang mahal. Biaya Rp610,8 juta setara Rp12.236 per kiriman dan merupakan batas bawah karena denda dan kehilangan pelanggan belum dihitung.", True, 12))
B.append(("h1", "BAB III  ANALISIS MASALAH"))
B.append(("h2", "3.1  Penentuan Masalah Utama"))
B.append(("p", "Masalah utama adalah perencanaan dan pemantauan rute yang masih manual dan belum mengintegrasikan lokasi, urutan kunjungan, jam penerimaan toko, serta komunikasi keterlambatan. Ini bukan kekurangan armada, sebab menambah kendaraan hanya menambah rute yang tidak efisien. Yang gagal adalah lapisan informasi: pengetahuan rute masih tersimpan pada dua dispatcher dan belum menjadi aturan kerja maupun data bersama.", True, 12))
B.append(("h2", "3.2  Analisis Akar Penyebab"))
B.append(("p", "Akar penyebab ditelusuri dengan teknik lima mengapa pada Tabel 3.1.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 3.1  Analisis Lima Mengapa",
    headers=["Ke", "Pertanyaan", "Jawaban"],
    widths=[1.0, 5.9, 9.0],
    size=8,
    rows=[
        ["1", "Mengapa kendaraan menempuh jarak tidak perlu?", "Urutan kunjungan tidak mengikuti kedekatan lokasi"],
        ["2", "Mengapa urutannya demikian?", "Rute manual mengikuti urutan pesanan masuk dan pengalaman dispatcher"],
        ["3", "Mengapa masih manual?", "Tidak ada alat bantu dan standar pengelompokan wilayah; perencana hanya dua orang"],
        ["4", "Mengapa tidak ada alat dan standar?", "Pengetahuan rute hanya pada individu, belum menjadi data atau prosedur"],
        ["5", "Mengapa belum menjadi data?", "Tidak ada indikator jarak, waktu, dan ketepatan waktu yang diukur"],
    ],
    note="Sumber: analisis penulis; baris kelima adalah akar penyebab.",
)))
B.append(("p", "Akar penyebabnya sistemik, bukan kesalahan individu, sehingga sanksi tidak akan menolong. Urutan perbaikannya: standar, data, ukuran, baru alat bantu (Ohno, 1988).", True, 12))
B.append(("h2", "3.3  Kebutuhan Perbaikan"))
B.append(("num", ["Urutan kunjungan mempertimbangkan jarak, kapasitas, dan jam penerimaan toko.", "Data toko rapi dan tervalidasi: koordinat, akses, jam buka, dan waktu layanan.", "Posisi kendaraan terlihat selama perjalanan dan pelanggan menerima ETA.", "Dispatcher boleh menimpa usulan sistem dengan alasan yang dicatat.", "Pelaksanaan bertahap tanpa menghentikan operasional, modal tidak melebihi Rp150 juta."]))
B.append(("h2", "3.4  Asumsi dan Keterbatasan Data"))
B.append(("p", "Agar tidak mengarang data, setiap angka yang bukan berasal dari kasus dinyatakan sebagai asumsi pada Tabel 3.2 beserta cara memperolehnya, dan seluruhnya dapat diganti angka aktual dalam 14 hari kerja pertama.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 3.2  Asumsi dan Cara Memperoleh Data",
    headers=["Kode", "Asumsi atau data yang dibutuhkan", "Nilai", "Dasar atau cara memperoleh"],
    widths=[1.2, 5.1, 3.3, 6.3],
    size=8,
    rows=[
        ["A1", "Hari operasi per tahun", "312 hari", "Data kasus: 26 hari/bulan × 12"],
        ["A2", "Titik kirim per kendaraan per hari", "8 titik", "Rekap surat jalan satu bulan"],
        ["A3", "Tingkat keterlambatan", "5% kiriman", "Jam tiba dibanding jam janji"],
        ["A4", "Biaya satu kejadian terlambat", "Rp100.000", "Wawancara staf penjualan"],
        ["A5", "Tingkat diskonto", "12% per tahun", "Bunga pinjaman modal kerja"],
        ["A6", "Waktu tunggu di lokasi", "12,8 jam/hari", "Checklist pengemudi: jam tiba–bongkar"],
        ["A7", "Upah per jam bagian operasional", "Rp38.462", "Slip gaji: Rp7 juta ÷ 182 jam"],
        ["A8", "Porsi waktu dispatcher menyusun rute", "40% × 2 orang", "Time study lima hari kerja"],
    ],
    note="Sumber: analisis penulis, diukur ulang pada Fase 0.",
)))
B.append(("p", "Keterbatasan yang dinyatakan terbuka: hubungan sebab-akibat antara perbaikan rute dan penurunan keterlambatan belum terbukti sehingga diuji pada Fase 2; model rute belum dikalibrasi karena koordinat toko belum ada; harga teknologi masih perkiraan.", True, 12))
B.append(("h1", "BAB IV  HASIL DAN PEMBAHASAN"))
B.append(("h2", "4.1  Alternatif Solusi"))
B.append(("p", "Tiga alternatif disusun berjenjang dan memenuhi kelima syarat pada subbab 3.3. Tabel 4.1 membandingkan isi, kelebihan, dan kekurangan ketiganya.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 4.1  Tiga Alternatif Solusi",
    headers=["Alternatif", "Isi", "Kelebihan", "Kekurangan"],
    widths=[2.6, 6.3, 3.4, 3.6],
    size=8,
    rows=[
        ["A1  Prosedur", "Zona, SOP rute, data toko pada spreadsheet, penetapan indikator", "Murah dan cepat; tanpa langganan", "Posisi tidak terlihat; ETA belum akurat"],
        ["A2  Aplikasi", "Langganan optimasi rute 20 kendaraan dan aplikasi pengemudi untuk ETA", "Rute otomatis; ETA tercatat", "Data lokal belum siap; usulan rute tidak akurat"],
        ["A3  Bertahap", "Rapikan aturan dan data 30 hari, aplikasi berisi data lokal, lalu pelacakan posisi", "Memenuhi kelima syarat; modal terkendali", "Butuh disiplin bertahap"],
    ],
    note="Sumber: rancangan penulis.",
)))
B.append(("h2", "4.2  Penentuan Kriteria Evaluasi"))
B.append(("p", "Kelima alternatif dinilai dengan lima kriteria berbobot; OTIF (on time in full) dipakai sebagai ukuran ketepatan pengiriman. Dua kriteria pertama memperoleh bobot terbesar karena tujuan kasus menyebut efisiensi jarak sebagai sasaran utama, sedangkan keluhan pelanggan menyangkut ketepatan waktu. Skala 1–5 dipakai agar penilaian kualitatif dapat dibandingkan, dan rubrik pada Tabel 4.2 membuat setiap skor dapat diperiksa ulang. K3 dirumuskan sebagai rasio manfaat terhadap modal karena ketiga alternatif sama-sama di bawah Rp150 juta.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 4.2  Kriteria, Bobot, dan Rubrik Penilaian",
    headers=["Kode", "Kriteria", "Bobot", "Skor 5", "Skor 3", "Skor 1"],
    widths=[1.0, 4.3, 1.3, 3.3, 3.0, 3.0],
    size=8,
    rows=[
        ["K1", "Penurunan jarak dan biaya", "30%", "Mencapai target −15%", "Turun 5–10%", "Tanpa dampak jarak"],
        ["K2", "Mutu layanan (OTIF dan ETA)", "25%", "ETA akurat dan terpantau", "Sebagian terpantau", "Tidak ada ETA"],
        ["K3", "Efisiensi pagu (manfaat ÷ modal)", "20%", "Rasio ≥ 4", "Rasio 1,5–2,5", "Rasio < 1"],
        ["K4", "Selesai dalam 90 hari", "15%", "Siap ≤ 30 hari", "60–90 hari", "Lebih dari 120 hari"],
        ["K5", "Fleksibel dan diterima pengguna", "10%", "Dispatcher dapat menimpa usulan", "Perlu penyesuaian", "Ditolak pengguna"],
    ],
    note="Sumber: rancangan penulis; skor akhir = Σ (bobot × skor).",
)))
B.append(("h2", "4.3  Perbandingan Alternatif Solusi"))
B.append(("p", "Kelayakan finansial dihitung dengan Net Present Value tiga tahun pada diskonto 12%, sehingga NPV = −modal + (manfaat − biaya operasional) × 2,4018. Manfaat disusun dari komponen biaya pada Tabel 2.1: A1 hanya menurunkan keterlambatan dan waktu tunggu tanpa mengubah jarak, sedangkan A2 dan A3 menurunkan jarak sehingga penghematan bahan bakar masuk seluruhnya.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 4.3  Kelayakan Finansial dan Penilaian Terbobot",
    headers=["Indikator / kriteria", "A1  Prosedur", "A2  Aplikasi", "A3  Bertahap"],
    widths=[6.5, 3.1, 3.1, 3.2],
    size=8,
    rows=[
        ["Modal awal", "25", "115", "125"],
        ["Biaya operasional per tahun", "24", "93", "99"],
        ["Total manfaat per tahun", "113,04", "211,68", "247,73"],
        ["Arus kas bersih per tahun", "89,04", "118,68", "148,73"],
        ["NPV tiga tahun", "188,86", "170,05", "232,22"],
        ["Payback (bulan)", "3,4", "11,6", "10,1"],
        ["Penilaian terbobot (skala 1–5; angka dalam kurung = bobot × skor)", "", "", ""],
        ["K1  Penurunan jarak dan biaya (30%)", "2  (0,60)", "4  (1,20)", "4  (1,20)"],
        ["K2  Mutu layanan, OTIF dan ETA (25%)", "2  (0,50)", "4  (1,00)", "4  (1,00)"],
        ["K3  Efisiensi penggunaan pagu (20%)", "5  (1,00)", "3  (0,60)", "4  (0,80)"],
        ["K4  Selesai dalam 90 hari (15%)", "5  (0,75)", "4  (0,60)", "3  (0,45)"],
        ["K5  Fleksibel dan diterima pengguna (10%)", "4  (0,40)", "3  (0,30)", "4  (0,40)"],
        ["Skor akhir / peringkat", "3,25 / 3", "3,70 / 2", "3,85 / 1"],
    ],
    note="Sumber: perhitungan penulis. Modal A3: lisensi Rp60 juta, implementasi data Rp25 juta, 12 perangkat Rp18 juta, pelatihan Rp12 juta, audit Rp10 juta. Rasio K3: 113,04 ÷ 25 = 4,5; 211,68 ÷ 115 = 1,8; 247,73 ÷ 125 = 2,0. Manfaat A3 = 140,4 (bahan bakar) + 74,9 (keterlambatan) + 27,6 (waktu tunggu) + 4,8 (kerja manual).",
)))
B.append(("p", "Hasilnya, A3 memberi NPV tertinggi (Rp232,22 juta), disusul A1 (Rp188,86 juta), sedangkan A2 paling lemah (Rp170,05 juta) karena membayar langganan penuh sementara data lokal belum siap. A1 unggul pada efisiensi modal, tetapi belum memenuhi syarat ketiga karena posisi kendaraan tetap tidak terpantau.", True, 12))
B.append(("p", "Perbandingan A1 dan A3 perlu dibaca secara inkremental sebab A3 membutuhkan modal lima kali lebih besar. Tambahan modal Rp100 juta menghasilkan tambahan arus kas Rp59,69 juta per tahun, sehingga NPV inkremental = −100 + (59,69 × 2,4018) = +Rp43,36 juta; tambahan itu layak.", True, 12))
B.append(("h2", "4.4  Pemilihan Solusi Terbaik dan Justifikasi"))
B.append(("p", "Alternatif 3 dipilih karena NPV-nya tertinggi dengan payback 10,1 bulan, modalnya menyisakan Rp25 juta dari pagu, dan pelaksanaannya bertahap sehingga manfaat diuji pada 5 kendaraan sebelum diberlakukan pada 20 kendaraan. Alternatif ini juga menjawab keberatan pengemudi karena dispatcher tetap boleh menimpa usulan sistem dengan alasan yang dicatat, dan catatan itulah yang kemudian memperbaiki data toko.", True, 12))
B.append(("p", "Keputusan diuji terhadap dua kemungkinan buruk: bila realisasi manfaat hanya 61%, NPV menjadi nol; bila manfaat turun 20% dan biaya operasional naik 10%, NPV masih positif Rp47,0 juta. Yang mengubah keputusan adalah pagu di bawah Rp125 juta atau kegagalan Fase 2, dan pada keadaan itu A1 menjadi cadangan. Target 12 bulan: jarak 130,5 km per hari, keterlambatan turun 30%, OTIF 95%, ETA 85%.", True, 12))
B.append(("h1", "BAB V  PENUTUP"))
B.append(("h2", "5.1  Tahapan Implementasi"))
B.append(("p", "Pelaksanaan dibagi empat fase dalam 90 hari dengan syarat lanjut terukur.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 5.1  Fase Pelaksanaan 90 Hari",
    headers=["Fase", "Hari", "Kegiatan", "Syarat lanjut"],
    widths=[1.3, 1.7, 6.4, 6.5],
    size=8,
    rows=[
        ["0", "1–14", "Mengukur baseline jarak, waktu, dan keterlambatan; merapikan data toko", "95% toko berdata lengkap; angka awal indikator tersedia"],
        ["1", "15–45", "Membagi zona, menyusun SOP rute, memasang aplikasi, melatih dispatcher", "Usulan rute 20 kendaraan berjalan; dispatcher mandiri"],
        ["2", "46–70", "Uji coba 5 kendaraan dengan 15 kendaraan pembanding", "Jarak turun ≥5%; OTIF tidak menurun"],
        ["3", "71–90", "Perpindahan bertahap, dashboard indikator, serah terima proses", "Indikator stabil dua minggu; pemilik proses ditunjuk"],
    ],
    note="Sumber: rancangan penulis; baseline diukur pada Fase 0, bukan diasumsikan.",
)))
B.append(("h2", "5.2  Kebutuhan Sumber Daya"))
B.append(("p", "Modal Rp125 juta terdiri atas lisensi Rp60 juta, implementasi data Rp25 juta, 12 perangkat pengemudi Rp18 juta, pelatihan Rp12 juta, dan audit data Rp10 juta. Biaya operasional Rp99 juta per tahun terdiri atas langganan Rp60 juta, kuota data Rp14 juta, pemeliharaan Rp10 juta, administrasi Rp9 juta, dan penyegaran perangkat Rp6 juta. Tidak ada penambahan pegawai.", True, 12))
B.append(("h2", "5.3  Pembagian Tanggung Jawab"))
B.append(("p", "Direktur operasional memutuskan kelanjutan tiap fase dan manajer operasional mengawal pelaksanaan harian sekaligus menjadi pemilik proses. Dispatcher menyusun rute, mencatat alasan penimpaan, dan melaporkan hambatan; pengemudi mengisi checklist waktu tiba dan selesai bongkar. TI menangani integrasi data, keuangan memverifikasi manfaat pada bulan ke-6 dan ke-12.", True, 12))
B.append(("h2", "5.4  Identifikasi Risiko dan Mitigasi"))
B.append(("p", "Skor risiko = kemungkinan (K) × dampak (D), masing-masing berskala 1–5.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 5.2  Risiko Utama dan Mitigasi",
    headers=["Kode", "Risiko", "Jenis", "K", "D", "Skor", "Mitigasi"],
    widths=[1.0, 4.0, 2.5, 0.7, 0.7, 0.9, 6.0],
    size=8,
    rows=[
        ["R1", "Dispatcher kembali menyusun rute manual", "Operasional", "4", "5", "20", "Penimpaan resmi disertai catatan alasan"],
        ["R2", "Pengemudi menolak karena merasa diawasi", "Sosial", "4", "4", "16", "Pelacakan untuk ETA dan keselamatan, bukan sanksi"],
        ["R3", "Data toko tidak lengkap atau kedaluwarsa", "Teknologi", "3", "5", "15", "Syarat Fase 0 mengikat; validasi silang"],
        ["R4", "Kebocoran data pelanggan dan posisi", "Keamanan data", "3", "5", "15", "Hak akses per peran dan enkripsi"],
        ["R5", "Kembali ke kebiasaan lama setelah proyek", "Operasional", "3", "4", "12", "Indikator masuk penilaian kinerja"],
    ],
    note="Sumber: identifikasi penulis; K = kemungkinan, D = dampak, skor = K × D.",
)))
B.append(("h2", "5.5  Indikator Keberhasilan (KPI)"))
B.append(("p", "Nilai awal diukur pada Fase 0 dan target 12 bulan dihitung terhadapnya, kecuali K1 yang sudah memiliki perkiraan awal; Tabel 5.3 mencantumkan keduanya.", True, 12))
B.append(("tbl", dict(
    caption="Tabel 5.3  Indikator Keberhasilan dan Target",
    headers=["Kode", "Indikator", "Awal", "Target 0 hari", "Target 12 bulan"],
    widths=[1.2, 5.5, 3.2, 2.9, 3.1],
    size=8,
    rows=[
        ["K1", "Jarak per kiriman (km)", "18,75 (perkiraan)", "turun 5%", "turun 13%"],
        ["K2", "OTIF (on time in full)", "diukur Fase 0", "tidak menurun", "≥ 95%"],
        ["K3", "Tingkat keterlambatan", "diukur Fase 0", "turun 15%", "turun 30%"],
        ["K4", "Akurasi ETA", "belum ada", "≥ 70%", "≥ 85%"],
        ["K5", "Waktu tunggu di lokasi", "diukur Fase 0", "turun 10%", "turun 18%"],
        ["K6", "Biaya distribusi per kiriman", "Rp12.236 (batas bawah)", "tidak naik", "turun 10%"],
    ],
    note="Sumber: rancangan penulis; OTIF = persentase kiriman tiba tepat waktu dan lengkap.",
)))
B.append(("h1", "BAB VI  KESIMPULAN DAN SARAN"))
B.append(("h2", "6.1  Kesimpulan"))
B.append(("num", ["Masalah utama bukan kekurangan armada, melainkan tidak adanya sistem perencanaan dan pengendalian; akarnya adalah standar, data, dan ukuran kinerja rute yang tidak pernah ditetapkan.", "Biaya akibat masalah Rp610,8 juta per tahun (Rp12.236 per kiriman), dengan keterlambatan (40,9%) dan waktu tunggu (25,1%) terbesar, bukan bahan bakar (23,0%).", "Alternatif 3 dipilih dengan skor 3,85 dari 5,00, NPV Rp232,22 juta, dan payback 10,1 bulan; tambahan modalnya terhadap A1 masih layak dengan NPV inkremental Rp43,36 juta.", "Keunggulan alternatif terpilih terletak pada urutannya: rapikan data, isi sistem dengan data lokal, lalu izinkan penimpaan resmi agar pengetahuan lapangan tidak hilang."]))
B.append(("h2", "6.2  Saran"))
B.append(("p", "Manajemen sebaiknya menjalankan Fase 0 sebelum membeli apa pun dan menilai keberhasilan dari turunnya jarak per kiriman serta keterlambatan, bukan dari ada atau tidaknya aplikasi. Bagi dispatcher dan pengemudi, catatan penimpaan usulan sistem adalah masukan untuk memperbaiki data, bukan kritik.", True, 12))

RINGKASAN = ["Perusahaan distribusi barang konsumsi mengoperasikan 20 kendaraan setiap hari dengan jarak rata-rata 150 km per kendaraan. Rute disusun dispatcher secara manual berdasarkan pengalaman, peta, dan urutan pesanan masuk. Akibatnya kendaraan melewati wilayah yang sama berulang kali, urutan kunjungan tidak optimal, dan keterlambatan baru diketahui setelah pengemudi menelepon kantor. Pelanggan tidak menerima perkiraan waktu kedatangan yang akurat sehingga jadwal penerimaan berubah dan waktu tunggu bertambah.", "Analisis dilakukan dengan menghitung baseline dari data kasus, memperkirakan biaya akibat masalah, menelusuri akar penyebab melalui teknik lima mengapa, lalu membandingkan tiga alternatif solusi menggunakan lima kriteria berbobot dan analisis Net Present Value.", "Baseline menunjukkan 3.000 km per hari atau 936.000 km per tahun, setara 93.600 liter bahan bakar dan Rp936 juta per tahun. Biaya akibat masalah diperkirakan Rp610,8 juta per tahun atau Rp12.236 per kiriman, dengan keterlambatan (40,9%) dan waktu tunggu (25,1%) sebagai penyumbang terbesar, sedangkan bahan bakar hanya 23,0%. Penambahan armada atau pembelian aplikasi tanpa pembenahan data karena itu tidak akan menyelesaikan masalah.", "Alternatif 3 dipilih: membenahi standar dan data lebih dahulu, kemudian memasang aplikasi rute berbasis data lokal dan pelacakan posisi. Alternatif ini memperoleh skor 3,85 dari 5,00, NPV Rp232,22 juta, payback 10,1 bulan, dan modal Rp125 juta atau 83% dari pagu. Pelaksanaannya dibagi empat fase dalam 90 hari tanpa menghentikan operasional. Pada 12 bulan diharapkan jarak per kiriman turun 13%, OTIF 95%, keterlambatan turun 30%, dan akurasi ETA 85%."]

PUSTAKA = [
    "Boysen, N., Fedtke, S., & Schwerdfeger, S. (2021). Last-mile delivery concepts: A survey from an operational research perspective. OR Spectrum, 43(1), 1–58. https://doi.org/10.1007/s00291-020-00607-8",
    "BPH. (2025). Industrial technology challenge: Studi kasus manajemen industri [Dokumen studi kasus].",
    "Braekers, K., Ramaekers, K., & Van Nieuwenhuyse, I. (2016). The vehicle routing problem: State of the art classification and review. Computers & Industrial Engineering, 99, 300–313. https://doi.org/10.1016/j.cie.2015.12.007",
    "Christopher, M. (2016). Logistics & supply chain management (5th ed.). Pearson.",
    "Dantzig, G. B., & Ramser, J. H. (1959). The truck dispatching problem. Management Science, 6(1), 80–91.",
    "Holland, C., Levis, J., Nuggehalli, R., Santilli, B., & Winters, J. (2017). UPS optimizes delivery routes. Interfaces, 47(1), 8–23.",
    "Ohno, T. (1988). Toyota production system: Beyond large-scale production. Productivity Press.",
    "Spear, S., & Bowen, H. K. (1999). Decoding the DNA of the Toyota Production System. Harvard Business Review, 77(5), 96–106.",
]
