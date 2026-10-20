# -*- coding: utf-8 -*-
"""Isi dokumen: Minggu 6 (pusat massa, momentum, impuls, tumbukan) + soal slide."""

ITEMS_B = [

dict(
    no=17, judul="Pusat massa pada satu dimensi",
    rumus_inti="x~CM~ = Σ m~i~ x~i~ / M",
    sumber="Cheatsheet poin 17 · Subbab 6-1 (CENTER OF MASS)",
    rumus=[("x~CM~ = (m~1~x~1~ + m~2~x~2~ + …)/M", None), ("M = m~1~ + m~2~ + … = Σm~i~", None)],
    lambang=[
        ("x~CM~", "koordinat pusat massa sistem", "meter (m)"),
        ("m~i~", "massa partikel ke-i", "kilogram (kg)"),
        ("x~i~", "koordinat partikel ke-i terhadap titik asal", "meter (m)"),
        ("M", "massa total sistem, M = Σm~i~", "kilogram (kg)"),
        ("Σ", "penjumlahan untuk semua partikel", "—"),
    ],
    syarat="Posisi pusat massa dihitung terhadap suatu titik asal yang dipilih; jika titik asal "
           "digeser, nilai x~CM~ ikut bergeser tetapi **letak fisisnya tetap sama**.",
    soal="Massa m₁ = 2 kg berada di x₁ = 0 m dan m₂ = 3 kg berada di x₂ = 4 m. "
         "Tentukan letak pusat massa sistem.",
    isi=[
        ("p", "**Langkah 1 — massa total:**"),
        ("f", "M = m₁ + m₂ = 2 + 3 = 5 kg"),
        ("p", "**Langkah 2 — masukkan ke rumus pusat massa:**"),
        ("f", "x~CM~ = (m₁x₁ + m₂x₂)/M = (2 × 0 + 3 × 4)/5"),
        ("f", "x~CM~ = (0 + 12)/5 = 2,4 m"),
        ("l", [
            "Pusat massa selalu lebih dekat ke massa yang **lebih besar**: di sini 2,4 m dari "
            "titik asal, lebih dekat ke m₂ (di 4 m) daripada ke m₁ (di 0 m).",
            "Periksa kewajaran: titik tengah keduanya adalah 2 m; karena m₂ lebih berat, "
            "pusat massa harus bergeser ke kanan dari 2 m. Hasil 2,4 m sesuai.",
        ]),
    ],
    jawaban="x~CM~ = **2,4 m** dari titik asal (lebih dekat ke benda yang lebih berat).",
    catatan="Pusat massa tidak harus berada di dalam benda. Contohnya cincin atau huruf “F” "
            "(lihat Latihan Soal pada berkas kuliah): pusat massanya bisa di ruang kosong.",
),

dict(
    no=18, judul="Pusat massa pada dua dimensi",
    rumus_inti="x~CM~ = Σm~i~x~i~/M ; y~CM~ = Σm~i~y~i~/M",
    sumber="Cheatsheet poin 18 · Subbab 6-1 (CENTER OF MASS)",
    rumus=[("x~CM~ = Σm~i~ x~i~/M        y~CM~ = Σm~i~ y~i~/M", None)],
    lambang=[
        ("x~CM~, y~CM~", "koordinat pusat massa pada bidang xy", "meter (m)"),
        ("m~i~", "massa partikel ke-i", "kilogram (kg)"),
        ("x~i~, y~i~", "koordinat partikel ke-i", "meter (m)"),
        ("M", "massa total sistem", "kilogram (kg)"),
    ],
    syarat="Kedua koordinat dihitung **terpisah** dengan rumus yang bentuknya sama. Untuk "
           "tiga dimensi, tambahkan z~CM~ = Σm~i~z~i~/M.",
    soal="Tiga massa: m₁ = 1 kg di (0, 0), m₂ = 2 kg di (3, 0), dan m₃ = 3 kg di (0, 2) m. "
         "Tentukan vektor posisi pusat massanya.",
    isi=[
        ("p", "**Langkah 1 — massa total:**"),
        ("f", "M = 1 + 2 + 3 = 6 kg"),
        ("p", "**Langkah 2 — koordinat x:**"),
        ("f", "x~CM~ = (1·0 + 2·3 + 3·0)/6 = 6/6 = 1 m"),
        ("p", "**Langkah 3 — koordinat y:**"),
        ("f", "y~CM~ = (1·0 + 2·0 + 3·2)/6 = 6/6 = 1 m"),
        ("l", [
            "Pusat massa di (1, 1) m — berada di dekat massa terbesar m₃ = 3 kg, yang terletak "
            "di (0, 2).",
            "Jika salah satu koordinat semua partikel sama (misalnya semua di y = 0), maka "
            "y~CM~ = 0 dan persoalan kembali menjadi satu dimensi.",
        ]),
    ],
    jawaban="r~CM~ = **(1, 1) m**.",
    catatan="Untuk benda simetris (persegi, lingkaran, bola), pusat massa berada di titik "
            "pusat geometrinya — cara pintas yang menghemat perhitungan integral.",
),

dict(
    no=19, judul="Pusat massa benda kontinu (batang homogen)",
    rumus_inti="r~CM~ = (1/M) ∫ r dm",
    sumber="Cheatsheet poin 19 · Subbab 6-1 (CENTER OF MASS)",
    rumus=[("x~CM~ = (1/M) ∫ x dm", None)],
    lambang=[
        ("r~CM~", "vektor posisi pusat massa benda", "meter (m)"),
        ("dm", "elemen massa yang sangat kecil", "kilogram (kg)"),
        ("x", "posisi elemen massa tersebut", "meter (m)"),
        ("M", "massa total benda", "kilogram (kg)"),
        ("∫", "penjumlahan kontinu, pengganti Σ untuk benda yang massanya tersebar", "—"),
    ],
    syarat="Untuk benda dengan kerapatan seragam, dm dapat diganti (M/L)dx pada batang, "
           "(M/A)dA pada pelat, sehingga M sering terhapus.",
    soal="Sebuah batang homogen panjangnya L = 4 m. Tentukan letak pusat massanya diukur dari "
         "salah satu ujung.",
    isi=[
        ("p", "**Langkah 1 — nyatakan elemen massa.** Untuk batang homogen berkerapatan "
              "λ = M/L, massa potongan sepanjang dx adalah dm = (M/L)dx."),
        ("p", "**Langkah 2 — masukkan ke rumus pusat massa.** Ambil ujung batang sebagai x = 0:"),
        ("f", "x~CM~ = (1/M)∫~0~^L^ x (M/L) dx = (1/L)∫~0~^L^ x dx"),
        ("f", "x~CM~ = (1/L)[½x²]~0~^L^ = (1/L)(½L²) = L/2"),
        ("p", "**Langkah 3 — masukkan angka:**"),
        ("f", "x~CM~ = 4/2 = 2 m"),
        ("l", [
            "Hasil L/2 masuk akal: batang homogen simetris, jadi pusat massanya di tengah.",
            "Jika batang tidak homogen (misalnya lebih tebal di satu sisi), integralnya "
            "menghasilkan angka yang lebih dekat ke sisi yang lebih berat.",
        ]),
    ],
    jawaban="x~CM~ = **2 m** dari ujung batang, yaitu tepat di tengah.",
    catatan="Pusat massa berbeda dengan pusat berat hanya bila g berubah di sepanjang benda; "
            "untuk benda berukuran biasa keduanya berimpit.",
),

dict(
    no=20, judul="Hukum II Newton untuk sistem partikel",
    rumus_inti="F~ext,net~ = M a~CM~",
    sumber="Cheatsheet poin 20 · Subbab 6-2 (Hukum II Newton untuk sistem partikel)",
    rumus=[("F~ext,net~ = M a~CM~", None)],
    lambang=[
        ("F~ext,net~", "jumlah vektor semua gaya **luar** pada sistem", "newton (N)"),
        ("M", "massa total sistem", "kilogram (kg)"),
        ("a~CM~", "percepatan pusat massa sistem", "meter/sekon² (m/s²)"),
    ],
    syarat="Gaya **dalam** (gaya antarpartikel) tidak boleh dimasukkan karena saling menghapus "
           "menurut hukum III Newton.",
    soal="Sebuah sistem bermassa total 5 kg menerima gaya eksternal neto 15 N ke kanan. "
         "Tentukan percepatan pusat massanya.",
    isi=[
        ("p", "**Diketahui:** M = 5 kg, F~ext,net~ = 15 N. **Ditanya:** a~CM~."),
        ("f", "a~CM~ = F~ext,net~/M = 15/5 = 3 m/s²"),
        ("l", [
            "Arah percepatan pusat massa selalu searah gaya eksternal neto (ke kanan).",
            "Perhatikan: walaupun partikel-partikel di dalam sistem bergerak ke berbagai arah, "
            "pusat massanya bergerak seperti satu partikel bermassa M.",
        ]),
    ],
    jawaban="a~CM~ = **3 m/s² ke kanan**.",
    catatan="Inilah alasan ledakan tidak dapat mengubah gerak pusat massa: gaya ledakan adalah "
            "gaya **dalam**, sehingga bila awalnya diam, pusat massa tetap diam (lihat Problem 44 "
            "pada berkas kuliah).",
),

dict(
    no=21, judul="Momentum total dan kecepatan pusat massa",
    rumus_inti="P = Σ m~i~v~i~ = M v~CM~",
    sumber="Cheatsheet poin 21 · Subbab 6-3 (LINEAR MOMENTUM)",
    rumus=[("p = m v", None), ("P = Σ m~i~ v~i~ = M v~CM~", None)],
    lambang=[
        ("p", "momentum sebuah partikel — besaran **vektor**", "kg·m/s (N·s)"),
        ("P", "momentum total sistem", "kg·m/s"),
        ("m~i~, v~i~", "massa dan kecepatan partikel ke-i", "kg; m/s"),
        ("v~CM~", "kecepatan pusat massa, v~CM~ = P/M", "meter/sekon (m/s)"),
        ("M", "massa total sistem", "kilogram (kg)"),
    ],
    syarat="Kecepatan bertanda: arah kanan positif, kiri negatif. Jangan menjumlahkan besar "
           "momentum bila arahnya berbeda.",
    soal="Sebuah benda 2 kg bergerak +3 m/s, dan benda 1 kg bergerak −4 m/s pada garis yang "
         "sama. Hitunglah momentum total dan kecepatan pusat massa sistem.",
    isi=[
        ("p", "**Langkah 1 — momentum total** (jumlahkan dengan tandanya):"),
        ("f", "P = m₁v₁ + m₂v₂ = (2)(+3) + (1)(−4) = 6 − 4 = +2 kg·m/s"),
        ("p", "**Langkah 2 — massa total:**"),
        ("f", "M = 2 + 1 = 3 kg"),
        ("p", "**Langkah 3 — kecepatan pusat massa:**"),
        ("f", "v~CM~ = P/M = 2/3 ≈ +0,67 m/s"),
        ("l", [
            "Tanda (+) berarti pusat massa bergerak ke arah benda pertama (ke kanan), walaupun "
            "benda kedua bergerak ke kiri.",
            "Periksa: momentum total 2 kg·m/s — jika kedua benda menempel, gabungan 3 kg akan "
            "bergerak +0,67 m/s. Konsisten.",
        ]),
    ],
    jawaban="P = **+2 kg·m/s** dan v~CM~ ≈ **+0,67 m/s** (ke arah benda pertama).",
    catatan="Satuan momentum kg·m/s sama dengan N·s. Inilah yang membuat impuls (N·s) dapat "
            "langsung disamakan dengan perubahan momentum.",
),

dict(
    no=22, judul="Impuls dan gaya rata-rata saat bola memantul",
    rumus_inti="J = Δp = m(v~f~ − v~i~) ; F~avg~ = J/Δt",
    sumber="Cheatsheet poin 22 · Subbab 6-4 (Tumbukan dan Impuls)",
    rumus=[("J = Δp = m(v~f~ − v~i~)", None), ("F~avg~ = J/Δt = Δp/Δt", None)],
    lambang=[
        ("J", "impuls — perubahan momentum yang diberikan gaya", "N·s ( = kg·m/s)"),
        ("Δp", "perubahan momentum, p~f~ − p~i~", "kg·m/s"),
        ("m", "massa bola", "kilogram (kg)"),
        ("v~i~, v~f~", "kecepatan **bervektor** sebelum dan sesudah (tanda ikut)", "meter/sekon (m/s)"),
        ("F~avg~", "gaya rata-rata selama tumbukan", "newton (N)"),
        ("Δt", "lama kontak (waktu tumbukan)", "sekon (s)"),
    ],
    syarat="Tetapkan arah positif lebih dahulu. Untuk bola yang memantul, kecepatan akhir "
           "berlawanan arah sehingga **bertanda negatif**.",
    soal="Sebuah bola bermassa 0,15 kg berubah kecepatannya dari +20 m/s menjadi −10 m/s dalam "
         "waktu 0,015 s. Hitunglah impuls yang diterima bola dan gaya rata-rata yang bekerja "
         "padanya.",
    isi=[
        ("p", "**Diketahui:** m = 0,15 kg, v~i~ = +20 m/s, v~f~ = −10 m/s, Δt = 0,015 s."),
        ("p", "**Langkah 1 — impuls** dengan memperhatikan tanda:"),
        ("f", "J = m(v~f~ − v~i~) = 0,15(−10 − 20) = 0,15(−30) = −4,5 N·s"),
        ("p", "**Langkah 2 — gaya rata-rata:**"),
        ("f", "F~avg~ = J/Δt = −4,5/0,015 = −300 N"),
        ("l", [
            "Tanda negatif berarti impuls dan gaya berarah **berlawanan** dengan arah datang "
            "bola — memang dinding mendorong bola kembali.",
            "Perhatikan bahwa perubahan kecepatan 30 m/s (bukan 10 m/s), karena arahnya berbalik. "
            "Inilah sumber kesalahan tersering pada soal pemantulan.",
        ]),
    ],
    jawaban="J = **−4,5 N·s**; F~avg~ = **−300 N** (berarah berlawanan dengan arah datang bola).",
    catatan="Gaya sebesar 300 N itu terasa besar, tetapi hanya bekerja 0,015 s. Helm dan bantalan "
            "keselamatan bekerja dengan **memperbesar Δt**, sehingga F~avg~ mengecil untuk "
            "perubahan momentum yang sama.",
),

dict(
    no=23, judul="Impuls oleh gaya konstan",
    rumus_inti="J = F Δt = Δp",
    sumber="Cheatsheet poin 23 · Subbab 6-4 (Tumbukan dan Impuls)",
    rumus=[("J = F Δt", None), ("J = Δp = m v~f~ − m v~i~", None)],
    lambang=[
        ("J", "impuls oleh gaya konstan", "N·s"),
        ("F", "besar gaya yang bekerja (tetap selama Δt)", "newton (N)"),
        ("Δt", "selang waktu gaya bekerja", "sekon (s)"),
        ("Δp", "perubahan momentum benda", "kg·m/s"),
        ("m", "massa benda", "kilogram (kg)"),
        ("v~i~, v~f~", "kecepatan sebelum dan sesudah", "meter/sekon (m/s)"),
    ],
    syarat="Gaya harus konstan. Jika gaya berubah, gunakan J = ∫F dt atau luas grafik F–t "
           "(Soal 24).",
    soal="Sebuah gaya 50 N bekerja selama 0,20 s pada benda 0,50 kg yang mula-mula diam. "
         "Hitunglah impuls yang diberikan dan laju akhir benda.",
    isi=[
        ("p", "**Langkah 1 — impuls:**"),
        ("f", "J = F Δt = (50)(0,20) = 10 N·s"),
        ("p", "**Langkah 2 — dari impuls ke laju akhir** (v~i~ = 0):"),
        ("f", "J = m(v~f~ − v~i~)   →   10 = 0,50(v~f~ − 0)"),
        ("f", "v~f~ = 10/0,50 = 20 m/s"),
        ("l", [
            "Periksa dengan cara kedua: a = F/m = 50/0,50 = 100 m/s², lalu "
            "v = at = 100 × 0,20 = 20 m/s. Sama.",
            "Arah laju akhir sama dengan arah gaya.",
        ]),
    ],
    jawaban="J = **10 N·s**; v~f~ = **20 m/s** searah gaya.",
    catatan="Impuls adalah besaran vektor: jika gaya berarah ke kiri, impuls dan perubahan "
            "momentumnya juga negatif.",
),

dict(
    no=24, judul="Impuls dari gaya yang berubah terhadap waktu",
    rumus_inti="J = ∫F dt = luas grafik F–t",
    sumber="Cheatsheet poin 24 · Subbab 6-4 (Tumbukan dan Impuls)",
    rumus=[("J = ∫ F dt  =  luas bertanda di bawah kurva F–t", None)],
    lambang=[
        ("J", "impuls total selama gaya bekerja", "N·s"),
        ("F", "gaya yang besarnya bergantung pada waktu", "newton (N)"),
        ("dt", "selang waktu sangat kecil", "sekon (s)"),
        ("luas grafik", "luas daerah antara kurva F dan sumbu t", "N·s"),
    ],
    syarat="Sumbu vertikal harus gaya (N) dan sumbu horizontal waktu (s), sehingga satuannya "
           "N·s. Bandingkan dengan grafik F–x yang luasnya joule.",
    soal="Sebuah gaya naik linier dari 0 sampai 20 N selama 0,50 s, lalu berhenti. Gaya itu "
         "bekerja pada benda 0,25 kg yang mula-mula diam. Hitunglah impuls dan laju akhir benda.",
    isi=[
        ("p", "**Langkah 1 — luas segitiga pada grafik F–t:**"),
        ("f", "J = ½ × alas × tinggi = ½ × (0,50 s)(20 N) = 5 N·s"),
        ("p", "**Langkah 2 — dari impuls ke laju:**"),
        ("f", "J = Δp = m v~f~   →   5 = (0,25)v~f~"),
        ("f", "v~f~ = 5/0,25 = 20 m/s"),
        ("l", [
            "Gaya rata-ratanya adalah J/Δt = 5/0,50 = 10 N, yaitu tepat setengah dari gaya "
            "maksimum 20 N — ciri khas profil segitiga.",
            "Jika ingin gaya konstan yang memberi impuls sama, pakailah 10 N selama 0,50 s.",
        ]),
    ],
    jawaban="J = **5 N·s**; v~f~ = **20 m/s** searah gaya.",
    catatan="Bentuk grafik menentukan luasnya: segitiga ½·a·t, persegi a·t, trapesium "
            "½(a + b)·t. Daerah di bawah sumbu waktu memberi impuls negatif.",
),

# ===================================================== TUMBUKAN
dict(
    no=25, judul="Membedakan tumbukan elastis dan tidak elastis",
    rumus_inti="Bandingkan momentum dan energi kinetik sebelum–sesudah",
    sumber="Cheatsheet poin 25 · Subbab 6-6 (Momentum dan energi kinetik dalam tumbukan)",
    rumus=[("Momentum: Σmv sebelum = Σmv sesudah (selalu, bila gaya luar ≈ 0)", None),
           ("Elastis: K~sebelum~ = K~sesudah~   ·   Tidak elastis: K~sesudah~ < K~sebelum~", None)],
    lambang=[
        ("K", "energi kinetik total sistem, K = Σ½mv²", "joule (J)"),
        ("p", "momentum, p = mv", "kg·m/s"),
        ("elastis", "energi kinetik kekal; benda memantul sempurna", "—"),
        ("tidak elastis", "energi kinetik berkurang; sebagian menjadi panas/bunyi/deformasi", "—"),
        ("sempurna tidak elastis", "benda menyatu dan bergerak bersama (kehilangan K terbesar)", "—"),
    ],
    syarat="Momentum selalu kekal pada tumbukan bila gaya luar dapat diabaikan; energi kinetik "
           "**hanya** kekal pada tumbukan elastis.",
    soal="Momentum suatu sistem kekal, sedangkan energi kinetiknya turun dari 20 J menjadi 12 J. "
         "Termasuk jenis tumbukan apa, dan ke mana energi 8 J itu pergi?",
    isi=[
        ("p", "**Langkah 1 — periksa momentum.** Momentum kekal, berarti syarat sistem "
              "terisolasi terpenuhi (gaya luar selama tumbukan dapat diabaikan)."),
        ("p", "**Langkah 2 — periksa energi kinetik:**"),
        ("f", "ΔK = K~f~ − K~i~ = 12 − 20 = −8 J"),
        ("p", "Karena ΔK ≠ 0 (energi kinetik berkurang), tumbukan **tidak elastis**. "
              "Karena bendanya tidak disebut menyatu, belum tentu sempurna tidak elastis."),
        ("l", [
            "Energi 8 J tidak hilang: berubah menjadi energi termal, bunyi, dan deformasi "
            "bentuk benda.",
            "Jika ΔK = 0 → elastis; jika ΔK < 0 dan benda menyatu → sempurna tidak elastis.",
        ]),
    ],
    jawaban="Tumbukan **tidak elastis**; 8 J berubah menjadi panas, bunyi, dan deformasi.",
    catatan="Momentum kekal bukan berarti energi kinetik kekal. Inilah jebakan utama pada soal "
            "bandul balistik: saat peluru menancap, momentum kekal tetapi energi kinetik tidak.",
),

dict(
    no=26, judul="Tumbukan sempurna tidak elastis (benda menyatu)",
    rumus_inti="v~f~ = (m~1~v~1~ + m~2~v~2~)/(m~1~ + m~2~)",
    sumber="Cheatsheet poin 26 · Subbab 6-7 (Tumbukan tidak elastis)",
    rumus=[("m~1~v~1i~ + m~2~v~2i~ = (m~1~ + m~2~)v~f~", None),
           ("v~f~ = (m~1~v~1i~ + m~2~v~2i~)/(m~1~ + m~2~)", None)],
    lambang=[
        ("m~1~, m~2~", "massa benda pertama dan kedua", "kilogram (kg)"),
        ("v~1i~, v~2i~", "kecepatan sebelum tumbukan (bertanda)", "meter/sekon (m/s)"),
        ("v~f~", "kecepatan bersama setelah tumbukan", "meter/sekon (m/s)"),
        ("K", "energi kinetik total", "joule (J)"),
    ],
    syarat="Berlaku bila kedua benda **menempel/menyatu** setelah tumbukan. Hanya momentum "
           "yang kekal; energi kinetik selalu berkurang.",
    soal="Benda m₁ = 1 kg bergerak +6 m/s menumbuk benda m₂ = 2 kg yang diam, lalu keduanya "
         "menyatu. Hitunglah kecepatan bersama dan energi kinetik yang hilang.",
    isi=[
        ("p", "**Langkah 1 — kekekalan momentum:**"),
        ("f", "m₁v₁i + m₂v₂i = (m₁ + m₂)v~f~"),
        ("f", "(1)(6) + (2)(0) = (1 + 2)v~f~   →   6 = 3v~f~"),
        ("f", "v~f~ = +2 m/s"),
        ("p", "**Langkah 2 — energi kinetik sebelum dan sesudah:**"),
        ("f", "K~i~ = ½(1)(6²) = 18 J        K~f~ = ½(3)(2²) = 6 J"),
        ("p", "**Langkah 3 — energi yang hilang:**"),
        ("f", "ΔK = 6 − 18 = −12 J"),
        ("l", [
            "Momentum sebelum = 6 kg·m/s dan sesudah = 3 × 2 = 6 kg·m/s → kekal.",
            "Dua pertiga energi kinetik awal berubah menjadi panas dan deformasi. Pada tumbukan "
            "menyatu, energi yang hilang selalu maksimum untuk massa dan laju awal yang sama.",
        ]),
    ],
    jawaban="v~f~ = **+2 m/s**; energi kinetik berkurang **12 J** (dari 18 J menjadi 6 J).",
    catatan="Pada tumbukan menyatu, kecepatan akhir adalah rata-rata kecepatan awal yang "
            "**ditimbang massa**: v~f~ = (m₁v₁ + m₂v₂)/(m₁ + m₂).",
),

dict(
    no=27, judul="Tumbukan menyatu dengan arah berlawanan",
    rumus_inti="P~sebelum~ = P~sesudah~",
    sumber="Cheatsheet poin 27 · Subbab 6-7",
    rumus=[("m~1~v~1~ + m~2~v~2~ = (m~1~ + m~2~)v~f~", None)],
    lambang=[
        ("v~1~, v~2~", "kecepatan awal, **bertanda** (+ ke kanan, − ke kiri)", "meter/sekon (m/s)"),
        ("v~f~", "kecepatan bersama setelah menempel", "meter/sekon (m/s)"),
        ("m~1~, m~2~", "massa masing-masing benda", "kilogram (kg)"),
        ("K", "energi kinetik total", "joule (J)"),
    ],
    syarat="Tetapkan arah positif sebelum memasukkan angka. Tanda hasil menunjukkan arah "
           "gerak akhir.",
    soal="Benda m₁ = 1 kg dengan v₁ = +4 m/s dan benda m₂ = 3 kg dengan v₂ = −2 m/s bergerak "
         "saling mendekat lalu menyatu. Hitunglah kecepatan akhir dan energi kinetik yang hilang.",
    isi=[
        ("p", "**Langkah 1 — momentum sebelum** (perhatikan tanda negatif):"),
        ("f", "P~i~ = (1)(+4) + (3)(−2) = 4 − 6 = −2 kg·m/s"),
        ("p", "**Langkah 2 — kecepatan bersama:**"),
        ("f", "v~f~ = P~i~/(m₁ + m₂) = −2/4 = −0,5 m/s"),
        ("p", "Tanda negatif berarti gabungan bergerak **ke kiri** (ke arah benda kedua)."),
        ("p", "**Langkah 3 — energi kinetik:**"),
        ("f", "K~i~ = ½(1)(4²) + ½(3)(2²) = 8 + 6 = 14 J"),
        ("f", "K~f~ = ½(4)(0,5²) = 0,5 J      →      ΔK = 0,5 − 14 = −13,5 J"),
        ("l", [
            "Momentum akhir: 4 × (−0,5) = −2 kg·m/s → sama dengan sebelum tumbukan.",
            "Hampir seluruh energi kinetik awal (13,5 dari 14 J) hilang — ciri tumbukan menyatu "
            "yang sangat tidak elastis.",
        ]),
    ],
    jawaban="v~f~ = **−0,5 m/s** (ke kiri); energi kinetik turun **13,5 J** "
            "(dari 14 J menjadi 0,5 J).",
    catatan="Bila hasil v~f~ bertanda positif, arah gabungan mengikuti benda yang momentumnya "
            "lebih besar — bukan otomatis mengikuti benda yang lebih berat.",
),

dict(
    no=28, judul="Tumbukan elastis dengan massa sama",
    rumus_inti="Momentum dan energi kinetik kekal",
    sumber="Cheatsheet poin 28 · Subbab 6-8 (Tumbukan elastis satu dimensi)",
    rumus=[("v~1f~ = [(m~1~ − m~2~)v~1i~]/(m~1~ + m~2~)   →   untuk m~1~ = m~2~: v~1f~ = 0", None),
           ("v~2f~ = [2m~1~v~1i~]/(m~1~ + m~2~)   →   untuk m~1~ = m~2~: v~2f~ = v~1i~", None)],
    lambang=[
        ("m~1~, m~2~", "massa kedua benda (di sini sama)", "kilogram (kg)"),
        ("v~1i~", "kecepatan benda pertama sebelum tumbukan", "meter/sekon (m/s)"),
        ("v~1f~, v~2f~", "kecepatan setelah tumbukan", "meter/sekon (m/s)"),
        ("K", "energi kinetik total — kekal pada tumbukan elastis", "joule (J)"),
    ],
    syarat="Tumbukan **elastis** (energi kinetik kekal) dan **satu dimensi** (lurus). Untuk "
           "massa sama, kedua benda bertukar kecepatan.",
    soal="Dua benda masing-masing bermassa 1 kg. Benda pertama bergerak +4 m/s dan benda kedua "
         "diam. Jika tumbukannya elastis, tentukan kecepatan kedua benda setelah tumbukan.",
    isi=[
        ("p", "**Langkah 1 — gunakan dua persamaan kekekalan.** Momentum:"),
        ("f", "1(4) + 1(0) = 1·v~1f~ + 1·v~2f~   →   v~1f~ + v~2f~ = 4"),
        ("p", "Energi kinetik (bentuk khusus untuk elastis 1D):"),
        ("f", "v~1i~ − v~2i~ = −(v~1f~ − v~2f~)   →   4 − 0 = v~2f~ − v~1f~"),
        ("p", "**Langkah 2 — selesaikan kedua persamaan.** Dari persamaan kedua "
              "v~2f~ = v~1f~ + 4; masukkan ke persamaan pertama:"),
        ("f", "v~1f~ + (v~1f~ + 4) = 4   →   2v~1f~ = 0   →   v~1f~ = 0"),
        ("f", "v~2f~ = 0 + 4 = +4 m/s"),
        ("l", [
            "Hasilnya: benda pertama **berhenti**, benda kedua bergerak dengan laju yang tadi "
            "dimiliki benda pertama — keduanya bertukar kecepatan.",
            "Periksa energi: K~i~ = ½(1)(16) = 8 J dan K~f~ = ½(1)(0) + ½(1)(16) = 8 J → kekal.",
        ]),
    ],
    jawaban="v~1f~ = **0** (berhenti) dan v~2f~ = **+4 m/s**.",
    catatan="Ini yang terjadi pada bola biliar ketika bola putih menabrak bola lain tepat di "
            "tengah: bola putih berhenti dan bola sasaran bergerak maju.",
),

dict(
    no=29, judul="Tumbukan elastis dengan massa berbeda",
    rumus_inti="v~1f~ = [(m~1~−m~2~)v~1i~ + 2m~2~v~2i~]/(m~1~+m~2~)",
    sumber="Cheatsheet poin 29 · Subbab 6-8 (Tumbukan elastis satu dimensi)",
    rumus=[("v~1f~ = [(m~1~ − m~2~)v~1i~ + 2m~2~v~2i~]/(m~1~ + m~2~)", None),
           ("v~2f~ = [2m~1~v~1i~ + (m~2~ − m~1~)v~2i~]/(m~1~ + m~2~)", None)],
    lambang=[
        ("m~1~, m~2~", "massa benda pertama dan kedua", "kilogram (kg)"),
        ("v~1i~, v~2i~", "kecepatan sebelum tumbukan (bertanda)", "meter/sekon (m/s)"),
        ("v~1f~, v~2f~", "kecepatan setelah tumbukan", "meter/sekon (m/s)"),
        ("m~1~ + m~2~", "massa total sistem (penyebut yang sama untuk kedua rumus)", "kilogram (kg)"),
    ],
    syarat="Hanya untuk tumbukan **elastis 1D**. Jika benda kedua mula-mula diam (v~2i~ = 0), "
           "rumusnya menyederhana menjadi v~1f~ = ((m~1~−m~2~)/(m~1~+m~2~))v~1i~ dan "
           "v~2f~ = (2m~1~/(m~1~+m~2~))v~1i~.",
    soal="Benda m₁ = 2 kg bergerak +5 m/s menumbuk benda m₂ = 3 kg yang diam secara elastis. "
         "Tentukan kecepatan kedua benda setelah tumbukan, lalu periksa momentum dan energinya.",
    isi=[
        ("p", "**Langkah 1 — kecepatan benda pertama** (v~2i~ = 0):"),
        ("f", "v~1f~ = [(2 − 3)(5) + 0]/(2 + 3) = (−1)(5)/5 = −1 m/s"),
        ("p", "**Langkah 2 — kecepatan benda kedua:**"),
        ("f", "v~2f~ = [2(2)(5) + 0]/5 = 20/5 = +4 m/s"),
        ("p", "**Langkah 3 — periksa momentum:**"),
        ("f", "p~i~ = (2)(5) + (3)(0) = 10 kg·m/s"),
        ("f", "p~f~ = (2)(−1) + (3)(4) = −2 + 12 = 10 kg·m/s  ✓"),
        ("p", "**Langkah 4 — periksa energi kinetik:**"),
        ("f", "K~i~ = ½(2)(5²) = 25 J"),
        ("f", "K~f~ = ½(2)(1²) + ½(3)(4²) = 1 + 24 = 25 J  ✓"),
        ("l", [
            "Benda pertama **memantul** (tanda negatif) karena menumbuk benda yang lebih berat; "
            "benda kedua terdorong maju.",
            "Kedua pemeriksaan (momentum dan energi) cocok, jadi hasilnya benar.",
        ]),
    ],
    jawaban="v~1f~ = **−1 m/s** (memantul) dan v~2f~ = **+4 m/s**.",
    catatan="Kasus khusus yang wajib diingat: bila m₁ ≪ m₂ (misalnya bola menumbuk dinding), "
            "benda ringan memantul dengan laju hampir sama besar; bila m₁ ≫ m₂, benda berat "
            "nyaris tidak berubah dan benda ringan terlempar dengan laju ≈ 2v₁.",
),

# ===================================================== SOAL SLIDE
dict(
    no=30, judul="Dua seluncuran air: siapa lebih cepat, siapa lebih dulu sampai",
    rumus_inti="v = √(2gh) — laju tidak bergantung bentuk lintasan",
    sumber="Slide kuliah CONCEPTUAL EXAMPLE 6-9 (Gambar 6-19), minggu ke-5",
    rumus=[("mgh = ½mv²   →   v = √(2gh)", None)],
    lambang=[
        ("h", "ketinggian awal peluncur (sama untuk kedua seluncuran)", "meter (m)"),
        ("v", "laju di dasar seluncuran", "meter/sekon (m/s)"),
        ("g", "percepatan gravitasi, 9,8 m/s²", "meter/sekon² (m/s²)"),
        ("m", "massa peluncur — **hilang** dalam perhitungan", "kilogram (kg)"),
    ],
    syarat="Tanpa gesekan, dan kedua peluncur mulai dari ketinggian yang sama dengan laju awal "
           "nol. Panjang/lekuk lintasan tidak boleh dipakai untuk menghitung laju.",
    soal="Dua seluncuran air di sebuah kolam berbentuk berbeda, tetapi keduanya dimulai pada "
         "ketinggian yang sama h. Dua peluncur, Paul dan Corinne, mulai dari keadaan diam pada "
         "waktu yang sama di seluncuran yang berbeda. (a) Siapa yang bergerak lebih cepat di "
         "dasar? (b) Siapa yang lebih dulu sampai di dasar? Abaikan gesekan dan anggap panjang "
         "kedua lintasan sama.",
    isi=[
        ("p", "**(a) Laju di dasar.** Hanya gravitasi yang melakukan usaha, jadi energi mekanik "
              "kekal dari puncak sampai dasar:"),
        ("f", "mgh = ½mv²   →   v = √(2gh)"),
        ("p", "Massa m terhapus dan bentuk lintasan tidak muncul dalam rumus. Karena h sama, "
              "kedua peluncur tiba di dasar dengan laju **sama besar**."),
        ("p", "**(b) Waktu tempuh.** Ini besaran yang berbeda. Pada bagian yang lebih curam, "
              "energi potensial lebih cepat berubah menjadi energi kinetik sehingga peluncur "
              "bergerak cepat sejak awal. Seluncuran Corinne memiliki bagian curam di depan, "
              "sedangkan seluncuran Paul menurun perlahan sehingga Paul bergerak lambat pada "
              "sebagian besar lintasan."),
        ("f", "t = ∫ ds/v(s)  →  bergantung pada bentuk lintasan, bukan hanya pada h"),
        ("p", "Karena panjang lintasan sama tetapi laju rata-rata Corinne lebih besar, waktu "
              "tempuh Corinne lebih singkat."),
    ],
    jawaban="(a) Keduanya **sama cepat** di dasar, v = √(2gh). (b) **Corinne sampai lebih "
            "dulu**, karena laju rata-ratanya sepanjang lintasan lebih besar.",
    catatan="Kekekalan energi hanya memberi laju pada suatu ketinggian, bukan waktu tempuh. "
            "Soal yang menanyakan “siapa lebih dulu” tidak dapat dijawab dengan rumus energi "
            "saja — perlu membayangkan riwayat geraknya.",
),

dict(
    no=31, judul="Anak meluncur di seluncuran air (h = 8,5 m)",
    rumus_inti="v = √(2gh)",
    sumber="Slide kuliah Gambar 8-8, minggu ke-5",
    rumus=[("K~i~ + U~i~ = K~f~ + U~f~   →   v = √(2gh)", None)],
    lambang=[
        ("h", "ketinggian puncak seluncuran terhadap dasar", "meter (m)"),
        ("v", "laju anak di bagian dasar", "meter/sekon (m/s)"),
        ("g", "percepatan gravitasi, 9,8 m/s²", "meter/sekon² (m/s²)"),
        ("m", "massa anak (tidak diperlukan)", "kilogram (kg)"),
    ],
    syarat="Seluncuran licin (dialiri air) sehingga gesekan diabaikan; anak mulai dari keadaan "
           "diam. Gaya normal tidak melakukan usaha karena selalu tegak lurus gerak.",
    soal="Gambar 8-8 menunjukkan seorang anak bermassa m meluncur dari keadaan diam pada puncak "
         "seluncuran air pada ketinggian h = 8,5 m. Dengan mengasumsikan seluncuran tanpa "
         "gesekan karena air yang mengalirinya, tentukan laju anak di bagian dasar seluncuran.",
    isi=[
        ("p", "**Langkah 1 — tetapkan acuan** y = 0 di dasar seluncuran, sehingga "
              "y~i~ = 8,5 m dan y~f~ = 0."),
        ("p", "**Langkah 2 — terapkan kekekalan energi mekanik:**"),
        ("f", "K~i~ + U~i~ = K~f~ + U~f~   →   0 + mgh = ½mv² + 0"),
        ("p", "**Langkah 3 — selesaikan untuk v:**"),
        ("f", "v = √(2gh) = √(2 × 9,8 × 8,5) = √166,6"),
        ("f", "v ≈ 12,9 m/s"),
        ("l", [
            "Setara dengan sekitar 46 km/jam — cukup cepat, karena itu keselamatan lintasan "
            "sangat penting.",
            "Jika ada gesekan, laju sebenarnya lebih kecil dari 12,9 m/s; nilai ini adalah "
            "batas maksimumnya.",
        ]),
    ],
    jawaban="v ≈ **12,9 m/s** di dasar seluncuran.",
    catatan="Rumusnya identik dengan Soal 10 (jatuh bebas). Perbedaannya hanya pada bentuk "
            "lintasan, yang **tidak** mempengaruhi laju akhir.",
),

dict(
    no=32, judul="Keju di lantai kabin elevator",
    rumus_inti="F~N~ − m~c~g = m~c~a ; T = W/d",
    sumber="Slide kuliah Problem 25 (Figure 7-34), minggu ke-4",
    rumus=[("F~N~ − m~c~ g = m~c~ a", None),
           ("T − (M + m~c~)g = (M + m~c~)a", None),
           ("W = T d  dan  T = W/d", None)],
    lambang=[
        ("F~N~", "gaya normal dari lantai kabin pada keju", "newton (N)"),
        ("m~c~", "massa keju (0,250 kg)", "kilogram (kg)"),
        ("M", "massa kabin elevator (900 kg)", "kilogram (kg)"),
        ("a", "percepatan kabin (sama dengan percepatan keju)", "meter/sekon² (m/s²)"),
        ("T", "tegangan gaya dari kabel pada kabin", "newton (N)"),
        ("d₁, d₂", "jarak tempuh tahap pertama dan kedua", "meter (m)"),
        ("W", "usaha oleh gaya kabel pada kabin", "joule (J)"),
    ],
    syarat="Keju dan kabin bergerak bersama (keju tidak terlepas dari lantai), sehingga "
           "percepatannya sama. Arah naik diambil positif.",
    soal="Sebuah balok keju 0,250 kg terletak di lantai kabin elevator 900 kg yang ditarik ke "
         "atas oleh kabel sejauh d₁ = 2,40 m, lalu sejauh d₂ = 10,5 m. (a) Sepanjang d₁, jika "
         "gaya normal pada keju 3,00 N, berapa usaha oleh gaya kabel pada kabin? (b) Sepanjang "
         "d₂, jika usaha oleh gaya kabel 92,61 kJ, berapa besar gaya normal pada keju?",
    isi=[
        ("p", "**(a) Langkah 1 — percepatan dari tinjauan keju:**"),
        ("f", "F~N~ − m~c~g = m~c~a   →   a = F~N~/m~c~ − g"),
        ("f", "a = 3,00/0,250 − 9,8 = 12,0 − 9,8 = +2,2 m/s²"),
        ("p", "**(a) Langkah 2 — tegangan kabel dari tinjauan kabin + keju:**"),
        ("f", "T = (M + m~c~)(g + a) = (900,25)(9,8 + 2,2) ≈ 1,08 × 10⁴ N"),
        ("p", "**(a) Langkah 3 — usaha kabel sepanjang d₁:**"),
        ("f", "W = T d₁ = (1,08 × 10⁴)(2,40) ≈ 2,59 × 10⁴ J"),
        ("p", "**(b) Langkah 1 — tegangan kabel dari usaha yang diketahui:**"),
        ("f", "T = W/d₂ = 92.610/10,5 = 8.820 N"),
        ("p", "**(b) Langkah 2 — bandingkan dengan berat total:** "
              "(900,25)(9,8) = 8.822 N. Karena T ≈ berat total, percepatannya praktis nol."),
        ("f", "a = T/(M + m~c~) − g ≈ 0 m/s²"),
        ("p", "**(b) Langkah 3 — gaya normal pada keju** saat a ≈ 0 hanya menopang beratnya:"),
        ("f", "F~N~ = m~c~(g + a) ≈ (0,250)(9,8) = 2,45 N"),
        ("l", [
            "Perhatikan: F~N~ berubah dari 3,00 N menjadi 2,45 N walaupun massanya sama, karena "
            "gaya normal bergantung pada percepatan.",
            "Pada lift yang bergerak dengan laju tetap (a = 0), F~N~ tepat sama dengan berat keju.",
        ]),
    ],
    jawaban="(a) W ≈ **2,6 × 10⁴ J** (25,9 kJ); (b) F~N~ ≈ **2,45 N**.",
    catatan="F~N~ bukan selalu sama dengan mg. Rumus umumnya F~N~ = m(g + a) untuk lift yang "
            "dipercepat ke atas; jika dipercepat ke bawah, F~N~ = m(g − a); jika jatuh bebas, "
            "F~N~ = 0 (tanpa bobot).",
),

dict(
    no=33, judul="Grafik percepatan terhadap posisi (tiga penggal)",
    rumus_inti="W = m × luas kurva a–x",
    sumber="Slide kuliah Problem 37 (Figure 7-40), minggu ke-4",
    rumus=[("F = m a   →   W = ∫F dx = m ∫a dx = m × luas kurva a–x", None),
           ("W = ΔK = ½mv² (karena v~i~ = 0)", None)],
    lambang=[
        ("a", "percepatan partikel pada posisi x", "meter/sekon² (m/s²)"),
        ("a~s~", "skala puncak grafik, a~s~ = 6,0 m/s²", "meter/sekon² (m/s²)"),
        ("m", "massa partikel (2,00 kg)", "kilogram (kg)"),
        ("luas kurva a–x", "bersatuan m²/s² — **bukan** joule", "m²/s²"),
        ("W", "usaha total sampai posisi x", "joule (J)"),
        ("v", "laju partikel pada posisi x", "meter/sekon (m/s)"),
    ],
    syarat="Grafik a–x berbeda dari grafik F–x: luasnya harus dikalikan massa lebih dahulu. "
           "Partikel mula-mula diam (v = 0 di x = 0) sehingga K = W.",
    soal="Gambar 7-40 memberikan percepatan sebuah partikel 2,00 kg ketika gaya terpasang F~a~ "
         "menggerakkannya dari keadaan diam sepanjang sumbu x dari x = 0 sampai x = 9,0 m. "
         "Skala sumbu vertikal ditetapkan oleh a~s~ = 6,0 m/s². Berapa usaha yang dilakukan "
         "gaya itu ketika partikel mencapai (a) x = 4,0 m, (b) x = 7,0 m, dan (c) x = 9,0 m? "
         "Berapa laju dan arah gerak partikel pada (d) x = 4,0 m, (e) x = 7,0 m, dan "
         "(f) x = 9,0 m?",
    gambar=("gbr-7-40.png", 14.6,
            "Gambar 1. Kurva percepatan terhadap posisi (Fig. 7-40). Daerah biru memberi "
            "kontribusi positif, daerah merah negatif. Skala puncak a~s~ = 6,0 m/s²."),
    isi=[
        ("p", "**Langkah 1 — ubah grafik a menjadi gaya.** Menurut hukum II Newton F = ma, "
              "sehingga luas kurva a–x harus dikalikan massa:"),
        ("f", "W = m × luas kurva a–x"),
        ("p", "**Langkah 2 — baca penggal kurvanya:** naik 0→1 m, datar 1→4 m (a~s~), turun "
              "4→6 m (memotong sumbu di x = 5 m), datar 6→8 m (−a~s~), lalu naik 8→9 m."),
        ("p", "**Langkah 3 — hitung luas kumulatif** (satuan a~s~ × m = m²/s²):"),
        ("f", "L(0→4) = 0,5a~s~ + 3a~s~ = 3,5a~s~ = 3,5 × 6,0 = 21,0 m²/s²"),
        ("f", "L(0→7) = 3,5a~s~ + 0,5a~s~ − 0,5a~s~ − a~s~ = 2,5a~s~ = 15,0 m²/s²"),
        ("f", "L(0→9) = 2,5a~s~ − a~s~ − 0,5a~s~ = 1,0a~s~ = 6,0 m²/s²"),
        ("p", "**Langkah 4 — kalikan dengan massa (2,00 kg):**"),
        ("f", "W(x = 4 m) = 2,00 × 21,0 = 42 J"),
        ("f", "W(x = 7 m) = 2,00 × 15,0 = 30 J"),
        ("f", "W(x = 9 m) = 2,00 × 6,0 = 12 J"),
        ("p", "**Langkah 5 — laju dari teorema usaha–energi** (K~i~ = 0, m = 2,00 kg):"),
        ("f", "½(2,00)v² = W   →   v = √W"),
        ("f", "x = 4 m: v = √42 = 6,5 m/s;   x = 7 m: v = √30 = 5,5 m/s;   x = 9 m: v = √12 = 3,5 m/s"),
        ("l", [
            "Karena K tetap positif di ketiga titik, partikel tidak pernah berhenti atau "
            "berbalik; ketiga laju berarah **+x**.",
            "Perhatikan laju menurun dari x = 5 m ke x = 9 m walaupun partikel terus maju: "
            "antara x = 5 m dan x = 9 m gaya berarah melawan gerak (a negatif), sehingga "
            "partikel diperlambat.",
        ]),
    ],
    jawaban="Usaha: (a) **42 J**, (b) **30 J**, (c) **12 J**. Laju: (d) **6,5 m/s**, "
            "(e) **5,5 m/s**, (f) **3,5 m/s** — semuanya searah **+x**.",
    catatan="Kesalahan tersering: menganggap luas grafik a–x langsung sama dengan usaha. "
            "Padahal luasnya bersatuan m²/s²; tanpa mengalikan massa, hasilnya bukan joule. "
            "Selain itu, gerak maju dengan laju menurun bukan berarti benda bergerak mundur.",
),

dict(
    no=34, judul="Usaha dari grafik gaya terhadap posisi",
    rumus_inti="W = luas bertanda di bawah kurva F~x~–x",
    sumber="Slide kuliah Problem 13 (Figure 6-38, Giancoli), minggu ke-4",
    rumus=[("W = ½(a + b) h   (luas trapesium)", None),
           ("W~total~ = W~positif~ + W~negatif~", None)],
    lambang=[
        ("F~x~", "gaya pada arah x", "newton (N)"),
        ("x", "posisi partikel", "meter (m)"),
        ("a, b", "dua sisi sejajar trapesium (panjang pada sumbu x)", "meter (m)"),
        ("h", "tinggi trapesium (nilai gaya)", "newton (N)"),
        ("W", "usaha = luas bertanda; di bawah sumbu x bertanda negatif", "joule (J)"),
    ],
    syarat="Kurva harus terdiri atas garis lurus sehingga luasnya dapat dihitung dengan rumus "
           "bangun datar. Daerah di bawah sumbu x memberi usaha negatif.",
    soal="Gaya pada sebuah partikel yang bekerja sepanjang sumbu x berubah seperti pada "
         "Gbr. 6-38. Tentukan usaha yang dilakukan gaya ini untuk menggerakkan partikel "
         "sepanjang sumbu x: (a) dari x = 0,0 sampai x = 10,0 m; (b) dari x = 0,0 sampai "
         "x = 15,0 m.",
    gambar=("gbr-6-38.png", 14.6,
            "Gambar 2. Kurva gaya terhadap posisi (Fig. 6-38). Daerah biru (di atas sumbu) "
            "memberi usaha positif, daerah merah (di bawah sumbu) memberi usaha negatif."),
    isi=[
        ("p", "**(a) Dari x = 0 sampai x = 10 m.** Pecah menjadi tiga bangun:"),
        ("f", "segitiga 0→3 m: ½(3)(400) = 600 J"),
        ("f", "persegi 3→7 m: (4)(400) = 1.600 J"),
        ("f", "segitiga 7→10 m: ½(3)(400) = 600 J"),
        ("f", "W = 600 + 1.600 + 600 = 2.800 J"),
        ("p", "Cara cepat: seluruh daerah itu trapesium dengan sisi sejajar 10 m dan 4 m, "
              "tinggi 400 N:"),
        ("f", "W = ½(10 + 4)(400) = ½(14)(400) = 2.800 J"),
        ("p", "**(b) Dari x = 10 sampai x = 15 m** — daerah **di bawah** sumbu x, jadi negatif:"),
        ("f", "segitiga 10→11,5 m: ½(1,5)(−200) = −150 J"),
        ("f", "persegi 11,5→13,5 m: (2)(−200) = −400 J"),
        ("f", "segitiga 13,5→15 m: ½(1,5)(−200) = −150 J"),
        ("f", "W(10→15 m) = −150 − 400 − 150 = −700 J"),
        ("p", "Cara cepat: trapesium dengan sisi sejajar 5 m dan 2 m, tinggi −200 N:"),
        ("f", "W = ½(5 + 2)(−200) = −700 J"),
        ("f", "W~total~ = 2.800 + (−700) = 2.100 J"),
        ("l", [
            "Momentum dan energi tidak perlu dihitung; seluruh soal diselesaikan dengan luas.",
            "Perhatikan bahwa W dari 0 ke 15 m (2.100 J) **lebih kecil** daripada W dari 0 ke "
            "10 m (2.800 J) — bukan berarti partikel mundur, melainkan partikel diperlambat "
            "pada penggal 10–15 m.",
        ]),
    ],
    jawaban="(a) W = **2,8 × 10³ J** (2.800 J); (b) W = **2,1 × 10³ J** (2.100 J).",
    catatan="Kesalahan paling sering: menjumlahkan **besar** luas sehingga bagian (b) dihitung "
            "2.800 + 700 = 3.500 J. Tanda negatif wajib diikutkan karena gaya melawan arah "
            "perpindahan pada x = 10 m sampai 15 m.",
),
]
