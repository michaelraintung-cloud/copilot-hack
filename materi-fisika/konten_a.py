# -*- coding: utf-8 -*-
"""Isi dokumen: Minggu 4 (usaha & energi kinetik) dan Minggu 5 (energi potensial)."""

ITEMS_A = [

# ===================================================== MINGGU 4
dict(
    no=1, judul="Usaha oleh gaya konstan",
    rumus_inti="W = F d cos θ",
    sumber="Cheatsheet poin 1 · Subbab 4-2 (KINETIC ENERGY AND WORK)",
    rumus=[("W = F d cos θ = F · d", None)],
    lambang=[
        ("W", "usaha yang dilakukan oleh gaya tersebut", "joule (J)"),
        ("F", "besar gaya yang bekerja (dianggap tetap)", "newton (N)"),
        ("d", "besar perpindahan benda", "meter (m)"),
        ("θ", "sudut antara arah gaya dan arah perpindahan", "derajat (°)"),
        ("F cos θ", "komponen gaya yang sejajar perpindahan — hanya ini yang melakukan usaha", "newton (N)"),
    ],
    syarat="Gaya harus **konstan** (besar maupun arahnya tidak berubah selama perpindahan). "
           "Jika sudut berubah atau gaya berubah, dipakai W = ∫F·dr.",
    soal="Sebuah gaya 20 N menarik sebuah benda sejauh 5 m pada sudut 60° terhadap "
         "arah perpindahan. Hitunglah usaha yang dilakukan gaya tersebut.",
    isi=[
        ("p", "**Diketahui:** F = 20 N, d = 5 m, θ = 60°. **Ditanya:** W."),
        ("p", "Masukkan besaran ke dalam rumus usaha, lalu hitung cos 60° = 0,5:"),
        ("f", "W = F d cos θ = (20 N)(5 m)(cos 60°)", None),
        ("f", "W = 100 N·m × 0,5 = 50 J"),
        ("l", [
            "**Periksa satuannya:** N × m = joule, jadi hasilnya memang dalam J.",
            "**Periksa tandanya:** θ = 60° < 90°, sehingga cos θ positif dan usahanya **positif** "
            "(gaya searah komponen gerak, energi masuk ke benda).",
            "**Tafsirkan:** gaya 20 N itu sebenarnya hanya menyumbang 20 cos 60° = 10 N "
            "sepanjang arah gerak; sisanya menekan benda ke arah lain dan tidak melakukan usaha.",
        ]),
    ],
    jawaban="W = **+50 J** (usaha positif: energi kinetik benda bertambah).",
    catatan="Tiga sudut yang wajib diingat: θ = 0° → W = +Fd (usaha maksimum); "
            "θ = 90° → W = 0 (gaya tegak lurus perpindahan, misalnya gaya normal pada "
            "lantai datar); θ = 180° → W = −Fd (gaya menghentikan benda).",
),

dict(
    no=2, judul="Usaha total oleh beberapa gaya",
    rumus_inti="W~net~ = Σ F~i~ d cos θ~i~",
    sumber="Cheatsheet poin 2 · Subbab 4-2 (KINETIC ENERGY AND WORK)",
    rumus=[("W~net~ = W~1~ + W~2~ + … = Σ F~i~ d cos θ~i~", None)],
    lambang=[
        ("W~net~", "usaha total (usaha neto) oleh semua gaya", "joule (J)"),
        ("F~i~", "besar gaya ke-i", "newton (N)"),
        ("d", "perpindahan yang sama untuk semua gaya", "meter (m)"),
        ("θ~i~", "sudut antara gaya ke-i dan arah perpindahan", "derajat (°)"),
        ("Σ", "penjumlahan aljabar — tanda positif dan negatif ikut dijumlahkan", "—"),
    ],
    syarat="Semua gaya bekerja pada perpindahan yang sama. Usaha total juga boleh dihitung "
           "sekaligus dari resultan gaya: W~net~ = (ΣF) d cos θ.",
    soal="Sebuah lemari bergeser sejauh 8,5 m. Gaya F~1~ = 12 N bekerja pada sudut 30° dan "
         "gaya F~2~ = 10 N pada sudut 40°, keduanya mengarah ke depan. Hitunglah usaha total "
         "pada lemari.",
    isi=[
        ("p", "**Diketahui:** d = 8,5 m, F₁ = 12 N, θ₁ = 30°, F₂ = 10 N, θ₂ = 40°. "
              "**Ditanya:** W~net~."),
        ("p", "Hitung usaha masing-masing gaya lebih dahulu dengan rumus yang sama seperti Soal 1:"),
        ("f", "W~1~ = F~1~ d cos θ~1~ = (12)(8,5)(cos 30°) = (102)(0,866) = 88,3 J"),
        ("f", "W~2~ = F~2~ d cos θ~2~ = (10)(8,5)(cos 40°) = (85)(0,766) = 65,1 J"),
        ("p", "Jumlahkan secara aljabar:"),
        ("f", "W~net~ = W~1~ + W~2~ = 88,3 + 65,1 = 153,4 J"),
        ("l", [
            "**Mengapa berat dan gaya normal tidak dihitung?** Keduanya berarah tegak lurus "
            "perpindahan mendatar, jadi θ = 90° dan cos 90° = 0 → usahanya nol.",
            "**Cara kedua (hasil harus sama):** ΣF cos θ = 12 cos 30° + 10 cos 40° = "
            "10,39 + 7,66 = 18,05 N, lalu W = 18,05 × 8,5 = 153,4 J. Cara ini berguna untuk "
            "memperoleh percepatan: a = (ΣF cos θ)/m.",
        ]),
    ],
    jawaban="W~net~ ≈ **153,4 J** (dibulatkan 1,5 × 10² J).",
    catatan="Usaha total adalah **jumlah aljabar**, bukan jumlah besar usaha. Jika salah satu "
            "gaya mengarah ke belakang (θ > 90°), usahanya negatif dan harus dikurangkan.",
),

dict(
    no=3, judul="Usaha oleh gaya yang berubah terhadap posisi",
    rumus_inti="W = ∫ F~x~ dx",
    sumber="Cheatsheet poin 3 · Subbab 4-5 (WORK DONE BY A GENERAL VARIABLE FORCE)",
    rumus=[("W = ∫ F~x~ dx   (batas bawah x~i~ sampai batas atas x~f~)", None),
           ("hasilnya = luas daerah di bawah kurva F~x~ terhadap x", None)],
    lambang=[
        ("W", "usaha oleh gaya yang besarnya bergantung pada posisi x", "joule (J)"),
        ("F~x~", "komponen gaya pada arah x, dapat berupa fungsi x", "newton (N)"),
        ("dx", "elemen perpindahan yang sangat kecil", "meter (m)"),
        ("x~i~, x~f~", "batas bawah (posisi awal) dan batas atas (posisi akhir)", "meter (m)"),
        ("∫", "penjumlahan kontinu (integral) — pengganti Σ untuk gaya yang berubah terus-menerus", "—"),
    ],
    syarat="Dipakai bila F tidak konstan. Bila F~x~ berbentuk grafik, integral sama dengan "
           "**luas bertanda** di bawah kurva (lihat Soal 5).",
    soal="Gaya F~x~ = 4x N bekerja pada benda 2 kg yang mula-mula diam, dari x = 0 sampai "
         "x = 3 m. Hitunglah usaha yang dilakukan gaya itu dan laju akhir benda.",
    isi=[
        ("p", "**Diketahui:** F~x~ = 4x N, x~i~ = 0, x~f~ = 3 m, m = 2 kg, v~i~ = 0. "
              "**Ditanya:** W dan v~f~."),
        ("p", "**Langkah 1 — hitung usaha dengan integral.** Karena F~x~ = 4x, antiturunan "
              "dari 4x adalah 2x²:"),
        ("f", "W = ∫~0~^3^ 4x dx = [2x²]~0~^3^ = 2(3)² − 2(0)² = 18 J"),
        ("p", "**Langkah 2 — hubungkan usaha dengan energi kinetik** (teorema usaha–energi):"),
        ("f", "W = ΔK = ½m v~f~² − ½m v~i~²"),
        ("f", "18 = ½(2)v~f~² − 0   →   v~f~² = 18   →   v~f~ = √18"),
        ("f", "v~f~ ≈ 4,24 m/s"),
        ("l", [
            "Perhatikan bahwa gaya makin besar saat x makin besar (F = 4x), jadi usaha tidak "
            "boleh dihitung dengan F × d memakai F di salah satu titik saja.",
            "Jika memakai F di x = 3 m (12 N) dikalikan 3 m, hasilnya 36 J — dua kali lipat "
            "nilai yang benar. Kesalahan ini sangat sering terjadi.",
        ]),
    ],
    jawaban="W = **18 J** dan v~f~ ≈ **4,24 m/s**.",
    catatan="Untuk gaya yang berubah linier (F = kx), hasil integral selalu ½kx², yaitu luas "
            "segitiga di bawah kurvanya. Inilah asal rumus energi potensial pegas.",
),

dict(
    no=4, judul="Usaha oleh gaya dua dimensi (perkalian titik)",
    rumus_inti="W = ∫F~x~ dx + ∫F~y~ dy",
    sumber="Cheatsheet poin 4 · Subbab 4-5 · juga di papan tulis (Sample Problem 7-08)",
    rumus=[("W = ∫ F · dr = ∫F~x~ dx + ∫F~y~ dy", None)],
    lambang=[
        ("F", "vektor gaya, ditulis F = F~x~ î + F~y~ ĵ", "newton (N)"),
        ("dr", "vektor perpindahan kecil, dr = dx î + dy ĵ", "meter (m)"),
        ("F · dr", "perkalian titik: hanya komponen gaya yang sejajar perpindahan yang dihitung", "joule (J)"),
        ("î, ĵ", "vektor satuan arah sumbu x dan sumbu y", "—"),
        ("W", "usaha total sepanjang lintasan dari titik awal ke titik akhir", "joule (J)"),
    ],
    syarat="Kedua komponen gaya diintegralkan **terpisah** dengan batasnya masing-masing. "
           "Jangan menjumlahkan besar gaya √(F~x~² + F~y~²) lebih dahulu.",
    soal="Sebuah gaya F = (3x² N) î + (4 N) ĵ bekerja pada sebuah partikel dan hanya mengubah "
         "energi kinetiknya. Berapa usaha yang dilakukan gaya itu ketika partikel berpindah dari "
         "koordinat (2 m, 3 m) ke (3 m, 0 m)? Apakah laju partikel bertambah atau berkurang?",
    isi=[
        ("p", "**Diketahui:** F~x~ = 3x², F~y~ = 4 (konstan); titik awal (2, 3) m, titik akhir "
              "(3, 0) m. **Ditanya:** W dan perubahan laju."),
        ("p", "Pecah integral menjadi dua bagian, masing-masing dengan batasnya sendiri:"),
        ("f", "W = ∫~2~^3^ 3x² dx + ∫~3~^0^ 4 dy"),
        ("p", "**Bagian x:** antiturunan 3x² adalah x³, dari 2 sampai 3."),
        ("f", "∫~2~^3^ 3x² dx = [x³]~2~^3^ = 27 − 8 = +19 J"),
        ("p", "**Bagian y:** gaya 4 N tetap, sedangkan partikel turun dari y = 3 m ke y = 0 m, "
              "sehingga perpindahannya negatif terhadap arah gaya."),
        ("f", "∫~3~^0^ 4 dy = 4(0 − 3) = −12 J"),
        ("f", "W = 19 + (−12) = +7 J"),
        ("p", "Karena W positif, maka ΔK = W > 0 sehingga **laju bertambah**."),
    ],
    jawaban="W = **+7 J**; energi kinetik naik 7 J sehingga **laju partikel bertambah**.",
    catatan="Tanda negatif pada suku y muncul karena arah gerak berlawanan dengan komponen gaya "
            "F~y~. Jika partikel justru naik dari y = 0 ke y = 3 m, sukunya menjadi +12 J dan "
            "usaha totalnya 31 J.",
),

dict(
    no=5, judul="Usaha dari luas grafik gaya–posisi",
    rumus_inti="W = luas bertanda di bawah kurva F~x~–x",
    sumber="Cheatsheet poin 5 · Subbab 4-5 (WORK DONE BY A GENERAL VARIABLE FORCE)",
    rumus=[("W = luas daerah antara kurva F~x~ dan sumbu x (tanda sesuai posisi)", None)],
    lambang=[
        ("W", "usaha; secara numerik sama dengan luas daerah pada grafik", "joule (J)"),
        ("F~x~", "gaya pada sumbu vertikal grafik", "newton (N)"),
        ("x", "posisi pada sumbu horizontal grafik", "meter (m)"),
        ("luas di atas sumbu", "usaha positif (gaya searah gerak)", "J"),
        ("luas di bawah sumbu", "usaha negatif (gaya melawan gerak)", "J"),
    ],
    syarat="Kurva harus berupa garis lurus atau bangun yang luasnya dapat dihitung "
           "(segitiga, persegi, trapesium). Jika melengkung, gunakan integral.",
    soal="Grafik gaya terhadap posisi berbentuk segitiga: F = 0 di x = 0 dan naik linier "
         "sampai 10 N di x = 4 m. Hitunglah usaha yang dilakukan gaya. Jika benda bermassa "
         "2 kg mula-mula diam, berapa lajunya di x = 4 m?",
    isi=[
        ("p", "**Langkah 1 — hitung luas segitiga.** Alas = 4 m, tinggi = 10 N:"),
        ("f", "W = ½ × alas × tinggi = ½ × (4 m)(10 N) = 20 J"),
        ("p", "**Langkah 2 — dari usaha ke laju** dengan teorema usaha–energi (K~i~ = 0):"),
        ("f", "W = ½m v²   →   20 = ½(2)v²   →   v² = 20   →   v = √20 ≈ 4,47 m/s"),
        ("l", [
            "Satuan luas grafik F–x adalah N × m = **joule**, jadi luasnya langsung merupakan usaha.",
            "Kalau kurvanya **di bawah** sumbu x (gaya melawan gerak), luasnya diberi tanda "
            "negatif, misalnya pada Soal 34 bagian (b).",
            "Kalau kurvanya berbentuk trapesium, pakai luas trapesium = ½(a + b) × tinggi, "
            "dengan a dan b adalah dua sisi sejajar.",
        ]),
    ],
    jawaban="W = **20 J**; laju benda di x = 4 m adalah v ≈ **4,47 m/s**.",
    catatan="Grafik a–x (percepatan terhadap posisi) **bukan** grafik gaya, sehingga luasnya "
            "bukan joule. Untuk grafik a–x, usaha = m × luas (lihat Soal 33).",
),

dict(
    no=6, judul="Teorema usaha–energi kinetik",
    rumus_inti="W~net~ = ½m(v~f~² − v~i~²) = ΔK",
    sumber="Cheatsheet poin 6 · Subbab 4-2 (KINETIC ENERGY AND WORK)",
    rumus=[("W~net~ = ΔK = ½m v~f~² − ½m v~i~²", None)],
    lambang=[
        ("W~net~", "usaha total oleh semua gaya pada benda", "joule (J)"),
        ("ΔK", "perubahan energi kinetik, ΔK = K~f~ − K~i~", "joule (J)"),
        ("m", "massa benda", "kilogram (kg)"),
        ("v~i~, v~f~", "besar kecepatan awal dan akhir (laju, bukan vektor)", "meter/sekon (m/s)"),
        ("K = ½mv²", "energi kinetik — besaran skalar, selalu ≥ 0", "joule (J)"),
    ],
    syarat="Berlaku untuk semua gaya (konservatif maupun tidak), asalkan W~net~ adalah usaha "
           "**total**. Berlaku juga bila lintasan melengkung atau gaya berubah.",
    soal="Sebuah benda bermassa 2 kg berubah kelajuannya dari 3 m/s menjadi 5 m/s. Hitunglah "
         "usaha total yang bekerja pada benda.",
    isi=[
        ("p", "**Diketahui:** m = 2 kg, v~i~ = 3 m/s, v~f~ = 5 m/s. **Ditanya:** W~net~."),
        ("f", "W~net~ = ½m(v~f~² − v~i~²)"),
        ("f", "W~net~ = ½(2)(5² − 3²) = 1 × (25 − 9) = 16 J"),
        ("l", [
            "Cara lain (menghitung K satu per satu): K~i~ = ½(2)(3²) = 9 J dan "
            "K~f~ = ½(2)(5²) = 25 J, maka W = 25 − 9 = 16 J. Hasilnya sama.",
            "Perhatikan bahwa yang menentukan adalah **selisih kuadrat** kecepatan, bukan "
            "selisih kecepatan. Dari 3 ke 5 m/s (selisih 2) memerlukan 16 J, sedangkan dari "
            "5 ke 7 m/s (selisih 2 juga) memerlukan 24 J.",
        ]),
    ],
    jawaban="W~net~ = **+16 J**.",
    catatan="Jika W~net~ negatif, energi kinetik berkurang (benda melambat). Jika W~net~ = 0, "
            "laju tetap — misalnya benda yang bergerak dengan laju konstan pada lintasan datar.",
),

dict(
    no=7, judul="Jarak pengereman: mengapa laju dua kali berarti jarak empat kali",
    rumus_inti="d~stop~ ∝ v²",
    sumber="Cheatsheet poin 7 · penerapan Subbab 4-2",
    rumus=[("d~stop~ ∝ v²   →   d~2~/d~1~ = (v~2~/v~1~)²", None)],
    lambang=[
        ("d~stop~", "jarak yang ditempuh benda sampai berhenti (v = 0)", "meter (m)"),
        ("v", "laju benda tepat sebelum pengereman dimulai", "meter/sekon (m/s)"),
        ("d~1~, d~2~", "jarak berhenti pada keadaan 1 dan keadaan 2", "meter (m)"),
        ("v~1~, v~2~", "laju awal pada keadaan 1 dan keadaan 2", "meter/sekon (m/s)"),
    ],
    syarat="Gaya pengereman (gaya gesek) dianggap **sama** pada kedua keadaan, dan jalan datar. "
           "Jika gaya rem berbeda, perbandingan ini tidak berlaku.",
    soal="Jarak berhenti sebuah mobil adalah 18 m pada laju 54 km/jam. Berapa jarak berhentinya "
         "pada laju 108 km/jam?",
    isi=[
        ("p", "**Diketahui:** d₁ = 18 m pada v₁ = 54 km/jam; ditanya d₂ pada v₂ = 108 km/jam."),
        ("p", "**Asal rumusnya** — dari teorema usaha–energi dengan gaya rem f yang tetap:"),
        ("f", "W = ΔK   →   −f d~stop~ = 0 − ½mv²   →   d~stop~ = mv²/(2f)"),
        ("p", "Karena m dan f tetap, satu-satunya besaran yang berubah adalah v². Maka "
              "d sebanding dengan v²:"),
        ("f", "d~2~/d~1~ = (v~2~/v~1~)² = (108/54)² = 2² = 4"),
        ("f", "d~2~ = 4 × 18 m = 72 m"),
        ("l", [
            "Periksa dengan satuan SI: 54 km/jam = 15 m/s dan 108 km/jam = 30 m/s.",
            "Energi kinetik pada 30 m/s empat kali energi kinetik pada 15 m/s, sehingga "
            "usaha yang harus diserap gaya rem juga empat kali, dan jaraknya empat kali.",
        ]),
    ],
    jawaban="Jarak berhenti menjadi **72 m** (empat kali jarak semula).",
    catatan="Inilah alasan batas kecepatan sangat penting: menambah laju 10% menambah jarak "
            "berhenti sekitar 21%, bukan 10%.",
),

dict(
    no=8, judul="Daya rata-rata dan daya sesaat",
    rumus_inti="P~avg~ = W/Δt ; P = F v cos θ",
    sumber="Cheatsheet poin 8 · Subbab 4-6 (POWER)",
    rumus=[("P~avg~ = W/Δt", None), ("P = F v cos θ", None)],
    lambang=[
        ("P~avg~", "daya rata-rata, yaitu usaha per satuan waktu", "watt (W) = J/s"),
        ("W", "usaha total yang dilakukan", "joule (J)"),
        ("Δt", "selang waktu", "sekon (s)"),
        ("P", "daya sesaat pada suatu saat", "watt (W)"),
        ("F", "gaya yang bekerja pada saat itu", "newton (N)"),
        ("v", "laju benda pada saat itu", "meter/sekon (m/s)"),
        ("θ", "sudut antara gaya dan arah kecepatan", "derajat (°)"),
    ],
    syarat="P = W/Δt untuk daya **rata-rata** pada selang waktu tertentu; P = F·v untuk daya "
           "**sesaat**. Satuan lain: 1 hp = 746 W; 1 kWh = 3,6 × 10⁶ J.",
    soal="(a) Sebuah mesin melakukan usaha 600 J dalam waktu 10 s. (b) Sebuah motor memberikan "
         "gaya 20 N searah gerak ketika lajunya 3 m/s. Hitunglah daya pada kedua contoh itu.",
    isi=[
        ("p", "**(a) Daya rata-rata** mesin:"),
        ("f", "P~avg~ = W/Δt = 600 J / 10 s = 60 W"),
        ("p", "**(b) Daya sesaat** motor, dengan θ = 0° karena gaya searah gerak:"),
        ("f", "P = F v cos θ = (20 N)(3 m/s)(cos 0°) = 60 W"),
        ("l", [
            "Kedua contoh menghasilkan angka yang sama, tetapi maknanya berbeda: (a) rata-rata "
            "selama 10 s, (b) sesaat pada saat laju 3 m/s.",
            "Jika gaya membentuk sudut terhadap gerak, misalnya 60°, maka P = 20 × 3 × 0,5 = 30 W.",
        ]),
    ],
    jawaban="Daya pada kedua contoh = **60 W** (≈ 0,08 hp).",
    catatan="Pada kendaraan, daya mesin yang tetap berarti gaya dorong menurun saat laju naik "
            "(F = P/v). Inilah sebabnya percepatan mobil melemah pada kecepatan tinggi.",
),

# ===================================================== MINGGU 5
dict(
    no=9, judul="Energi potensial gravitasi dan usaha gravitasi",
    rumus_inti="ΔU~g~ = mgΔy ; W~g~ = −ΔU~g~",
    sumber="Cheatsheet poin 9 · Subbab 5-1 (POTENTIAL ENERGY AND CONSERVATION OF ENERGY)",
    rumus=[("U~g~ = mgy", None), ("ΔU~g~ = mg(y~f~ − y~i~)", None), ("W~g~ = −ΔU~g~", None)],
    lambang=[
        ("U~g~", "energi potensial gravitasi benda pada ketinggian y", "joule (J)"),
        ("m", "massa benda", "kilogram (kg)"),
        ("g", "percepatan gravitasi, g = 9,8 m/s²", "meter/sekon² (m/s²)"),
        ("y", "ketinggian benda diukur dari titik acuan y = 0", "meter (m)"),
        ("ΔU~g~", "perubahan energi potensial gravitasi", "joule (J)"),
        ("W~g~", "usaha yang dilakukan gaya gravitasi", "joule (J)"),
    ],
    syarat="Titik acuan y = 0 **boleh dipilih di mana saja**; yang bermakna fisis hanya ΔU, "
           "bukan U itu sendiri. Naik → ΔU positif; turun → ΔU negatif.",
    soal="Sebuah benda bermassa 2 kg diangkat dari y = 2 m ke y = 5 m. Hitunglah perubahan "
         "energi potensial gravitasinya dan usaha yang dilakukan gaya gravitasi.",
    isi=[
        ("p", "**Diketahui:** m = 2 kg, y~i~ = 2 m, y~f~ = 5 m, g = 9,8 m/s². "
              "**Ditanya:** ΔU~g~ dan W~g~."),
        ("p", "**Langkah 1 — perpindahan vertikal:**"),
        ("f", "Δy = y~f~ − y~i~ = 5 − 2 = +3 m"),
        ("p", "**Langkah 2 — perubahan energi potensial:**"),
        ("f", "ΔU~g~ = mgΔy = (2)(9,8)(3) = +58,8 J"),
        ("p", "**Langkah 3 — usaha gravitasi.** Gaya gravitasi berarah ke bawah, sedangkan "
              "benda naik, jadi usahanya negatif:"),
        ("f", "W~g~ = −ΔU~g~ = −58,8 J"),
        ("l", [
            "Tanda positif pada ΔU berarti energi potensial **bertambah**: benda sekarang "
            "menyimpan 58,8 J lebih banyak.",
            "Usaha gravitasi negatif karena gaya dan perpindahan berlawanan arah (θ = 180°). "
            "Jika benda turun 3 m, ΔU = −58,8 J dan W~g~ = +58,8 J.",
            "Usaha oleh gaya **angkat** (gaya luar) justru +58,8 J, sehingga jumlahnya dengan "
            "usaha gravitasi sama dengan nol bila benda bergerak dengan laju tetap.",
        ]),
    ],
    jawaban="ΔU~g~ = **+58,8 J** dan W~g~ = **−58,8 J**.",
    catatan="Kesalahan umum: menukar tanda. Aturannya sederhana — **naik: ΔU positif, "
            "W~g~ negatif**; **turun: ΔU negatif, W~g~ positif**.",
),

dict(
    no=10, judul="Kekekalan energi mekanik pada jatuh bebas",
    rumus_inti="K~i~ + U~i~ = K~f~ + U~f~",
    sumber="Cheatsheet poin 10 · Subbab 5-2 (CONSERVATION OF MECHANICAL ENERGY)",
    rumus=[("K~i~ + U~i~ = K~f~ + U~f~", None),
           ("½m v~i~² + mgy~i~ = ½m v~f~² + mgy~f~", None)],
    lambang=[
        ("K", "energi kinetik, K = ½mv²", "joule (J)"),
        ("U", "energi potensial (di sini hanya gravitasi), U = mgy", "joule (J)"),
        ("E~mech~", "energi mekanik total, E = K + U — besaran yang kekal", "joule (J)"),
        ("v~i~, v~f~", "laju awal dan laju akhir", "meter/sekon (m/s)"),
        ("y~i~, y~f~", "ketinggian awal dan akhir terhadap acuan", "meter (m)"),
    ],
    syarat="Berlaku **hanya** bila tidak ada gaya nonkonservatif yang melakukan usaha "
           "(tanpa gesekan, tanpa dorongan luar). Jika ada gesekan, tambahkan ΔE~th~ (Soal 15).",
    soal="Sebuah benda mulai dari keadaan diam pada ketinggian 12 m. Gesekan udara diabaikan. "
         "Hitunglah lajunya ketika tiba di dasar.",
    isi=[
        ("p", "**Diketahui:** v~i~ = 0, y~i~ = 12 m, y~f~ = 0. **Ditanya:** v~f~."),
        ("p", "Terapkan kekekalan energi mekanik dari titik lepas (i) ke dasar (f):"),
        ("f", "K~i~ + U~i~ = K~f~ + U~f~"),
        ("f", "0 + mgy~i~ = ½m v~f~² + 0"),
        ("p", "Massa m ada di kedua ruas, sehingga dapat dihapus:"),
        ("f", "g y~i~ = ½v~f~²   →   v~f~ = √(2g y~i~)"),
        ("f", "v~f~ = √(2 × 9,8 × 12) = √235,2 ≈ 15,34 m/s"),
        ("l", [
            "Hasilnya tidak bergantung pada massa: bola besi dan bola kertas (tanpa gesekan) "
            "akan tiba dengan laju sama.",
            "Periksa kewajaran: jatuh 12 m butuh waktu t = √(2h/g) ≈ 1,56 s, dan "
            "v = gt = 9,8 × 1,56 ≈ 15,3 m/s. Cocok dengan hasil di atas.",
        ]),
    ],
    jawaban="v~f~ ≈ **15,34 m/s** (sekitar 55 km/jam).",
    catatan="Rumus v = √(2gh) hanya berlaku untuk **jatuh bebas dari keadaan diam**. Bila benda "
            "dilempar ke bawah dengan laju awal v~i~, hasilnya v~f~ = √(v~i~² + 2gh).",
),

dict(
    no=11, judul="Energi mekanik pada roller-coaster",
    rumus_inti="½mv² + mgy = konstan",
    sumber="Cheatsheet poin 11 · Subbab 5-2 · juga di slide (EXAMPLE 6-8)",
    rumus=[("½m v² + mgy = tetap (sama di setiap titik lintasan)", None)],
    lambang=[
        ("v", "laju kereta pada ketinggian tertentu", "meter/sekon (m/s)"),
        ("y", "ketinggian titik itu diukur dari acuan (dasar bukit)", "meter (m)"),
        ("m", "massa kereta — **hilang** dalam perhitungan", "kilogram (kg)"),
        ("½mv²", "energi kinetik kereta", "joule (J)"),
        ("mgy", "energi potensial gravitasi kereta", "joule (J)"),
    ],
    syarat="Lintasan licin (tanpa gesekan) dan kereta tidak memakai motor/rem selama bergerak. "
           "Bentuk lintasan tidak mempengaruhi hasil.",
    soal="Sebuah kereta roller-coaster mulai dari keadaan diam pada ketinggian h = 40 m. "
         "Hitunglah (a) laju kereta di dasar bukit, dan (b) ketinggian kereta ketika lajunya "
         "14 m/s.",
    isi=[
        ("p", "**Diketahui:** y₁ = 40 m, v₁ = 0, g = 9,8 m/s². **Ditanya:** (a) v di y = 0; "
              "(b) y saat v = 14 m/s."),
        ("p", "**(a) Laju di dasar.** Bandingkan puncak (1) dan dasar (2):"),
        ("f", "½m v₁² + mgy₁ = ½m v₂² + mgy₂"),
        ("f", "0 + (9,8)(40) = ½v₂² + 0"),
        ("f", "392 = ½v₂²   →   v₂ = √784 = 28 m/s"),
        ("p", "**(b) Ketinggian saat v = 14 m/s.** Pakai kekekalan energi lagi, dari puncak "
              "ke titik berketinggian y:"),
        ("f", "g y₁ = ½v² + g y   →   y = y₁ − v²/(2g)"),
        ("f", "y = 40 − (14)²/(2 × 9,8) = 40 − 196/19,6 = 40 − 10 = 30 m"),
        ("l", [
            "Perhatikan pola: laju setengah (14 dari 28 m/s) berarti energi kinetik seperempat. "
            "Karena itu kereta masih 30 m di atas dasar, bukan 20 m.",
            "Massa kereta tidak perlu diketahui karena terhapus di kedua ruas.",
        ]),
    ],
    jawaban="(a) v = **28 m/s** di dasar; (b) lajunya 14 m/s pada ketinggian **30 m**.",
    catatan="Soal seperti ini sering diberi tambahan „berapa laju di titik 3 yang tingginya "
            "25 m?” — jawabnya sama caranya: y₁ = 40 → y = 25, lalu v = √(2g(y₁ − y)) = "
            "√(2 × 9,8 × 15) ≈ 17,1 m/s.",
),

dict(
    no=12, judul="Energi pegas berubah menjadi energi gerak",
    rumus_inti="½k x² = ½m v²",
    sumber="Cheatsheet poin 12 · Subbab 5-2 dan 4-4 (WORK DONE BY A SPRING FORCE)",
    rumus=[("U~s~ = ½k x²   dan   ½k x² = ½m v²", None)],
    lambang=[
        ("U~s~", "energi potensial elastis pegas yang termampatkan/tertarik", "joule (J)"),
        ("k", "konstanta pegas (kekakuan pegas)", "newton/meter (N/m)"),
        ("x", "besar simpangan dari posisi setimbang (mampatan atau regangan)", "meter (m)"),
        ("m", "massa benda yang dilontarkan pegas", "kilogram (kg)"),
        ("v", "laju benda setelah lepas dari pegas", "meter/sekon (m/s)"),
    ],
    syarat="Pegas dianggap tidak bermassa, tanpa gesekan, dan x diukur dari panjang "
           "**relaks** (belum termampatkan). Satuan x wajib meter, bukan cm.",
    soal="Sebuah benda bermassa 0,20 kg dilontarkan oleh pegas dengan k = 200 N/m yang "
         "termampatkan 0,10 m. Hitunglah laju benda setelah lepas dari pegas (tanpa gesekan).",
    isi=[
        ("p", "**Langkah 1 — hitung energi yang tersimpan di pegas:**"),
        ("f", "U~s~ = ½k x² = ½(200)(0,10)² = 100 × 0,01 = 1,0 J"),
        ("p", "**Langkah 2 — seluruh energi itu berubah menjadi energi kinetik benda:**"),
        ("f", "½k x² = ½m v²   →   1,0 = ½(0,20)v²"),
        ("f", "1,0 = 0,10 v²   →   v² = 10   →   v = √10 ≈ 3,16 m/s"),
        ("l", [
            "Massa pegas diabaikan, jadi tidak ada energi yang “tertinggal” di pegas.",
            "Periksa satuan: k dalam N/m dan x dalam m menghasilkan J; jika x ditulis 10 cm "
            "(bukan 0,10 m), hasilnya akan salah 100 kali.",
        ]),
    ],
    jawaban="v ≈ **3,16 m/s**.",
    catatan="Energi pegas bergantung pada **x²**, sehingga memampatkan dua kali lipat "
            "menyimpan empat kali energi, dan laju lontarnya menjadi dua kali.",
),

dict(
    no=13, judul="Gaya Hooke dan usaha oleh pegas",
    rumus_inti="F~s~ = −kx ; W~s~ = ½k(x~i~² − x~f~²)",
    sumber="Cheatsheet poin 13 · Subbab 4-4 dan 5-1",
    rumus=[("F~s~ = −k x", None),
           ("W~s~ = ½k(x~i~² − x~f~²) = −ΔU~s~", None)],
    lambang=[
        ("F~s~", "gaya pegas; tanda (−) menandakan arahnya selalu menuju posisi setimbang", "newton (N)"),
        ("k", "konstanta pegas", "newton/meter (N/m)"),
        ("x", "simpangan dari posisi setimbang", "meter (m)"),
        ("W~s~", "usaha yang dilakukan oleh gaya pegas", "joule (J)"),
        ("x~i~, x~f~", "simpangan awal dan simpangan akhir", "meter (m)"),
        ("ΔU~s~", "perubahan energi potensial pegas, ΔU~s~ = ½k x~f~² − ½k x~i~²", "joule (J)"),
    ],
    syarat="Berlaku untuk pegas ideal (berlaku linier sampai batas elastis). Usaha pegas "
           "positif bila pegas **kembali** ke posisi setimbang, negatif bila makin termampatkan.",
    soal="Sebuah pegas dengan k = 200 N/m bergerak dari x~i~ = 0,10 m ke x~f~ = 0,04 m. "
         "Hitunglah (a) gaya pegas pada saat x~i~, dan (b) usaha yang dilakukan pegas.",
    isi=[
        ("p", "**(a) Gaya pegas pada x~i~ = 0,10 m:**"),
        ("f", "F~s~ = −k x~i~ = −(200)(0,10) = −20 N"),
        ("p", "Tanda negatif berarti gaya berarah **berlawanan** dengan simpangan, yaitu menuju "
              "posisi setimbang (memulihkan)."),
        ("p", "**(b) Usaha pegas** dari x~i~ = 0,10 m ke x~f~ = 0,04 m:"),
        ("f", "W~s~ = ½k(x~i~² − x~f~²) = ½(200)[(0,10)² − (0,04)²]"),
        ("f", "W~s~ = 100 × (0,0100 − 0,0016) = 100 × 0,0084 = +0,84 J"),
        ("l", [
            "Usahanya **positif** karena pegas bergerak menuju setimbang (mendorong benda ke "
            "arah gerak), sehingga energinya berkurang dan berpindah ke benda.",
            "Cek dengan energi potensial: U~i~ = ½(200)(0,10²) = 1,00 J dan "
            "U~f~ = ½(200)(0,04²) = 0,16 J. Maka W~s~ = −(0,16 − 1,00) = +0,84 J. Sama.",
        ]),
    ],
    jawaban="(a) F~s~ = **−20 N** (berarah menuju titik setimbang); (b) W~s~ = **+0,84 J**.",
    catatan="Jangan keliru memakai W = F d cos θ untuk pegas, karena F berubah selama "
            "perpindahan. Yang benar adalah W = ½k(x~i~² − x~f~²) atau integral ∫(−kx)dx.",
),

dict(
    no=14, judul="Bola jatuh menekan pegas: menentukan konstanta pegas",
    rumus_inti="mg(h + x) = ½k x²",
    sumber="Cheatsheet poin 14 · slide EXAMPLE 6-11 (Gambar 6-23)",
    rumus=[("mg(h + Y) = ½k Y²", None),
           ("k = 2mg(h + Y)/Y²", None)],
    lambang=[
        ("m", "massa bola", "kilogram (kg)"),
        ("h", "jarak jatuh **sebelum** menyentuh pegas", "meter (m)"),
        ("Y", "mampatan maksimum pegas (positif, diukur dari panjang relaks)", "meter (m)"),
        ("k", "konstanta pegas yang dicari", "newton/meter (N/m)"),
        ("g", "percepatan gravitasi, 9,8 m/s²", "meter/sekon² (m/s²)"),
        ("h + Y", "penurunan total bola dari titik lepas sampai titik terendah", "meter (m)"),
    ],
    syarat="Bola dilepas dari keadaan diam dan berhenti sesaat di mampatan maksimum; pegas "
           "tidak bermassa; tanpa gesekan udara. Acuan y = 0 di titik sentuh pegas.",
    soal="Sebuah bola bermassa 2,60 kg jatuh sejauh 0,55 m sebelum menyentuh pegas vertikal, "
         "lalu memampatkan pegas sebesar 0,15 m. Tentukan konstanta pegas k.",
    isi=[
        ("p", "**Diketahui:** m = 2,60 kg, h = 0,55 m, Y = 0,15 m. **Ditanya:** k."),
        ("p", "**Langkah 1 — tetapkan acuan dan keadaan.** Ambil y = 0 di titik bola menyentuh "
              "pegas. Keadaan 1: y₁ = +h, v₁ = 0. Keadaan 2 (mampatan maksimum): y₂ = −Y, "
              "v₂ = 0."),
        ("p", "**Langkah 2 — tulis energi mekanik kedua keadaan.** Ada dua energi potensial, "
              "keduanya harus muncul:"),
        ("f", "E₁ = mgh + 0        E₂ = −mgY + ½kY²"),
        ("p", "**Langkah 3 — samakan** karena hanya gaya konservatif yang bekerja:"),
        ("f", "mgh = −mgY + ½kY²   →   mg(h + Y) = ½kY²"),
        ("f", "k = 2mg(h + Y)/Y²"),
        ("p", "**Langkah 4 — masukkan angka.** Penurunan total h + Y = 0,55 + 0,15 = 0,70 m:"),
        ("f", "k = 2(2,60)(9,8)(0,70) / (0,15)² = 35,67 / 0,0225"),
        ("f", "k ≈ 1.585 N/m ≈ 1,59 × 10³ N/m"),
        ("l", [
            "Periksa besaran: k = N/m, dan hasil 1,59 × 10³ N/m wajar untuk pegas kursi/piston.",
            "Bandingkan dengan energi: bola kehilangan energi potensial mg(h + Y) = 17,8 J, dan "
            "seluruhnya tersimpan sebagai ½kY² = ½(1585)(0,15²) = 17,8 J. Cocok.",
        ]),
    ],
    jawaban="k ≈ **1,59 × 10³ N/m** (sekitar 1,6 kN/m).",
    catatan="Kesalahan klasik: memakai mgh = ½kY² sehingga suku mgY hilang. Hasilnya menjadi "
            "k = 2mgh/Y² ≈ 1,25 × 10³ N/m, yaitu 21% terlalu kecil, karena pada keadaan akhir "
            "bola masih 0,15 m **di bawah** titik sentuh sehingga energi potensialnya berkurang.",
),

dict(
    no=15, judul="Gesekan dan energi termal",
    rumus_inti="f~k~ = μ~k~N ; W~f~ = −f~k~d ; ΔE~th~ = f~k~d",
    sumber="Cheatsheet poin 15 · Subbab 5-4 (Usaha oleh gaya luar, gesekan)",
    rumus=[("f~k~ = μ~k~ N", None), ("W~f~ = −f~k~ d", None), ("ΔE~th~ = f~k~ d = −W~f~", None)],
    lambang=[
        ("f~k~", "besar gaya gesek kinetik", "newton (N)"),
        ("μ~k~", "koefisien gesek kinetik (tanpa satuan)", "—"),
        ("N", "gaya normal dari permukaan pada benda", "newton (N)"),
        ("d", "jarak tempuh selama bergesekan", "meter (m)"),
        ("W~f~", "usaha oleh gaya gesek — selalu **negatif**", "joule (J)"),
        ("ΔE~th~", "energi termal yang timbul (panas) — selalu **positif**", "joule (J)"),
    ],
    syarat="N = mg hanya berlaku pada permukaan **datar dan tidak ada gaya vertikal lain**. "
           "Pada bidang miring atau lift, N harus dihitung dari kesetimbangan arah tegak lurus.",
    soal="Sebuah balok bermassa 3 kg dengan μ~k~ = 0,20 bergerak 5 m pada permukaan mendatar. "
         "Energi kinetik awalnya 40 J. Hitunglah gaya gesek, usaha gesek, energi termal yang "
         "timbul, energi kinetik akhir, dan laju akhir balok.",
    isi=[
        ("p", "**Langkah 1 — gaya normal** (lantai datar, tidak ada gaya vertikal lain):"),
        ("f", "N = mg = (3)(9,8) = 29,4 N"),
        ("p", "**Langkah 2 — gaya gesek:**"),
        ("f", "f~k~ = μ~k~ N = (0,20)(29,4) = 5,88 N"),
        ("p", "**Langkah 3 — usaha gesek dan energi termal.** Gesekan berlawanan arah gerak "
              "(θ = 180°):"),
        ("f", "W~f~ = −f~k~ d = −(5,88)(5) = −29,4 J      ΔE~th~ = +29,4 J"),
        ("p", "**Langkah 4 — energi kinetik akhir** dengan teorema usaha–energi:"),
        ("f", "K~f~ = K~i~ + W~f~ = 40 − 29,4 = 10,6 J"),
        ("p", "**Langkah 5 — laju akhir:**"),
        ("f", "K~f~ = ½m v~f~²   →   10,6 = ½(3)v~f~²   →   v~f~² = 7,07"),
        ("f", "v~f~ ≈ 2,66 m/s"),
        ("l", [
            "Energi tidak hilang: 29,4 J berpindah dari energi kinetik menjadi energi termal "
            "(panas) pada balok dan lantai.",
            "Jika K~i~ lebih kecil dari 29,4 J, balok akan berhenti sebelum 5 m — jarak "
            "berhentinya d = K~i~/(f~k~).",
        ]),
    ],
    jawaban="f~k~ = **5,88 N**; W~f~ = **−29,4 J**; ΔE~th~ = **29,4 J**; "
            "K~f~ = **10,6 J**; v~f~ ≈ **2,66 m/s**.",
    catatan="Pada bidang miring, N = mg cos α sehingga f~k~ = μ~k~ mg cos α — lebih kecil "
            "daripada di lantai datar. Ini kesalahan yang paling sering terjadi pada soal "
            "bidang miring.",
),

dict(
    no=16, judul="Usaha oleh gaya nonkonservatif",
    rumus_inti="ΔE~mech~ = W~nc~",
    sumber="Cheatsheet poin 16 · Subbab 5-5 (Kekekalan energi secara umum)",
    rumus=[("ΔE~mech~ = W~nc~   →   E~f~ − E~i~ = W~nc~", None)],
    lambang=[
        ("E~mech~", "energi mekanik total, E = K + U", "joule (J)"),
        ("ΔE~mech~", "perubahan energi mekanik, E~f~ − E~i~", "joule (J)"),
        ("W~nc~", "usaha oleh gaya nonkonservatif (gesekan, tarikan, dorongan)", "joule (J)"),
        ("K", "energi kinetik", "joule (J)"),
        ("U", "energi potensial (gravitasi dan/atau pegas)", "joule (J)"),
    ],
    syarat="Bila W~nc~ = 0, persamaan kembali menjadi kekekalan energi mekanik "
           "(K~i~ + U~i~ = K~f~ + U~f~). Gaya gesek selalu memberi W~nc~ negatif.",
    soal="Energi mekanik suatu sistem turun dari 100 J menjadi 70 J karena gesekan. "
         "Berapa usaha oleh gaya nonkonservatif itu, dan ke mana energinya pergi?",
    isi=[
        ("p", "**Diketahui:** E~i~ = 100 J, E~f~ = 70 J. **Ditanya:** W~nc~."),
        ("f", "W~nc~ = E~f~ − E~i~ = 70 − 100 = −30 J"),
        ("p", "Tanda negatif berarti gaya nonkonservatif **mengambil** energi dari sistem. "
              "Energi 30 J itu tidak hilang, melainkan berubah menjadi energi termal "
              "(ΔE~th~ = +30 J) pada permukaan yang bergesekan."),
        ("l", [
            "Bentuk umum kekekalan energi: ΔK + ΔU + ΔE~th~ = W~luar~. Jika sistem terisolasi, "
            "seluruh ruas kanan nol.",
            "Perhatikan bedanya: W~nc~ negatif **bukan** berarti energinya musnah, hanya "
            "berpindah bentuk.",
        ]),
    ],
    jawaban="W~nc~ = **−30 J**; energi mekanik berkurang 30 J dan berubah menjadi energi "
            "termal (panas).",
    catatan="Jika gaya luar **melakukan** usaha positif (misalnya motor menarik), maka W~nc~ "
            "positif dan energi mekanik sistem bertambah.",
),
]
