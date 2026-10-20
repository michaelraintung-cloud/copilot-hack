# -*- coding: utf-8 -*-
"""29 soal cheatsheet — MINGGU 4 & 5 (usaha, energi kinetik, energi potensial)."""

ITEMS_M45 = [

# ======================================================== MINGGU 4
dict(
    no=1, judul="Usaha oleh gaya konstan",
    rumus_inti="W = F d cos θ",
    sumber="Cheatsheet Minggu 4, poin 1 · Subbab 4-2",
    rumus=[("W = F d cos θ = F · d", None)],
    penjabaran=[
        "**Arti rumusnya.** Usaha adalah energi yang **dipindahkan** oleh sebuah gaya ketika "
        "benda berpindah. Rumus di atas menyatakan bahwa yang berpindah energi hanyalah "
        "**bagian gaya yang sejajar dengan perpindahan**, yaitu F cos θ. Bagian gaya yang tegak "
        "lurus perpindahan tidak memindahkan energi sama sekali.",
        "**Asal rumusnya.** Usaha didefinisikan sebagai perkalian titik antara vektor gaya dan "
        "vektor perpindahan: W = **F** · **d**. Perkalian titik dua vektor menghasilkan "
        "|F||d| cos θ, sehingga W = F d cos θ. Karena cos θ hanya berupa bilangan, usaha adalah "
        "**besaran skalar** — tidak punya arah, hanya punya tanda.",
        "**Tiga kasus penting.** (i) θ = 0° → cos θ = 1 → W = +Fd, usaha paling besar; "
        "(ii) θ = 90° → cos θ = 0 → W = 0, gaya tidak melakukan usaha (contoh: gaya normal, "
        "tegangan tali pada gerak melingkar); (iii) θ = 180° → cos θ = −1 → W = −Fd, benda "
        "kehilangan energi.",
    ],
    lambang=[
        ("W", "usaha oleh gaya tersebut", "joule (J)"),
        ("F", "besar gaya yang bekerja, dianggap tetap", "newton (N)"),
        ("d", "besar perpindahan benda", "meter (m)"),
        ("θ", "sudut antara arah gaya dan arah perpindahan", "derajat (°)"),
        ("F cos θ", "komponen gaya sejajar perpindahan — satu-satunya bagian yang melakukan usaha", "newton (N)"),
    ],
    satuan="[W] = N × m = (kg·m/s²) × m = kg·m²/s² = **joule (J)**. Hasil kali F cos θ bersatuan N "
           "dan d bersatuan m, sehingga satuannya pasti joule — jika hasil Anda bukan joule, "
           "ada satuan yang belum diubah.",
    syarat="Gaya harus **konstan** (besar dan arah tidak berubah). Bila gaya berubah atau "
           "lintasannya melengkung sehingga sudut berubah, pakai W = ∫F·dr (Soal 3 dan 4).",
    soal="Sebuah gaya 20 N menarik sebuah benda sejauh 5 m pada sudut 60° terhadap arah "
         "perpindahan. Hitunglah usaha yang dilakukan gaya tersebut.",
    isi=[
        ("p", "**Diketahui:** F = 20 N; d = 5 m; θ = 60°. **Ditanya:** W."),
        ("p", "**Langkah 1 — tulis rumusnya, lalu ganti lambang dengan angka:**"),
        ("f", "W = F d cos θ"),
        ("f", "W = (20 N)(5 m) cos 60°"),
        ("p", "**Langkah 2 — hitung bagian demi bagian:** F d = 100 N·m dan cos 60° = 0,5."),
        ("f", "W = 100 N·m × 0,5 = 50 N·m = 50 J"),
    ],
    cek=[
        "**Satuan:** N·m = J ✓ (bukan N/m atau N·m²).",
        "**Tanda:** θ = 60° < 90° → cos θ positif → W positif, sesuai harapan (gaya membantu gerak).",
        "**Kewajaran:** gaya efektif hanya 20 cos 60° = 10 N sepanjang gerak; 10 N × 5 m = 50 J ✓",
        "**Batas:** jika θ = 0°, hasilnya Fd = 100 J, dan 50 J berada di antaranya — masuk akal.",
    ],
    jawaban="W = **+50 J**.",
    catatan="Kesalahan tersering: memakai cos dari sudut yang salah, atau menulis cos 60° = 0,866 "
            "(itu cos 30°). Hafalkan: cos 30° = ½√3 ≈ 0,866; cos 45° ≈ 0,707; cos 60° = 0,5.",
),

dict(
    no=2, judul="Usaha total oleh beberapa gaya",
    rumus_inti="W~net~ = Σ W~i~ = Σ F~i~ d cos θ~i~",
    sumber="Cheatsheet Minggu 4, poin 2 · Subbab 4-2",
    rumus=[("W~net~ = W~1~ + W~2~ + … + W~n~ = Σ F~i~ d cos θ~i~", None),
           ("W~net~ = (Σ F~i~ cos θ~i~) d  =  (gaya resultan sejajar gerak) × d", None)],
    penjabaran=[
        "**Arti rumusnya.** Bila beberapa gaya bekerja pada benda yang sama, masing-masing gaya "
        "memindahkan energinya sendiri. Karena usaha adalah skalar, usaha-usaha itu cukup "
        "**dijumlahkan secara aljabar** (memperhatikan tanda), bukan dijumlahkan sebagai vektor.",
        "**Dua cara yang harus memberi hasil sama.** (i) Jumlahkan usaha tiap gaya: "
        "W~net~ = Σ F~i~ d cos θ~i~; (ii) jumlahkan dulu komponen gaya yang sejajar gerak, lalu "
        "kalikan perpindahan. Cara kedua berguna bila kita juga ingin percepatan, sebab "
        "a = ΣF/m.",
        "**Gaya yang tidak melakukan usaha.** Berat dan gaya normal pada gerak mendatar selalu "
        "tegak lurus perpindahan (θ = 90°), sehingga kontribusinya nol. Inilah sebabnya keduanya "
        "tidak muncul dalam perhitungan meskipun ada.",
    ],
    lambang=[
        ("W~net~", "usaha total (usaha neto) oleh semua gaya", "joule (J)"),
        ("W~i~", "usaha oleh gaya ke-i", "joule (J)"),
        ("F~i~", "besar gaya ke-i", "newton (N)"),
        ("d", "perpindahan, sama untuk semua gaya", "meter (m)"),
        ("θ~i~", "sudut antara gaya ke-i dan perpindahan", "derajat (°)"),
        ("Σ", "penjumlahan aljabar, tanda + / − diikutkan", "—"),
    ],
    satuan="Setiap suku F~i~ d cos θ~i~ bersatuan N·m = J, sehingga jumlahnya juga joule. "
           "Gaya resultan (ΣF cos θ) bersatuan N, dan bila dikalikan d (m) hasilnya tetap J.",
    syarat="Semua gaya bekerja pada perpindahan yang **sama**. Jika gaya-gaya bekerja pada bagian "
           "perjalanan yang berbeda, jumlahkan usaha per bagian lintasan.",
    soal="Sebuah lemari bergeser 8,5 m. Gaya F₁ = 12 N bekerja pada sudut 30° dan F₂ = 10 N "
         "pada sudut 40° terhadap arah geseran, keduanya mengarah ke depan. Berapa usaha total "
         "pada lemari?",
    isi=[
        ("p", "**Diketahui:** d = 8,5 m; F₁ = 12 N, θ₁ = 30°; F₂ = 10 N, θ₂ = 40°. "
              "**Ditanya:** W~net~."),
        ("p", "**Langkah 1 — usaha gaya pertama:**"),
        ("f", "W₁ = F₁ d cos θ₁ = (12)(8,5)(0,866) = 102 × 0,866 = 88,3 J"),
        ("p", "**Langkah 2 — usaha gaya kedua:**"),
        ("f", "W₂ = F₂ d cos θ₂ = (10)(8,5)(0,766) = 85 × 0,766 = 65,1 J"),
        ("p", "**Langkah 3 — jumlahkan:**"),
        ("f", "W~net~ = W₁ + W₂ = 88,3 + 65,1 = 153,4 J"),
        ("p", "**Cara kedua (pemeriksaan):** jumlahkan komponen gaya sejajar gerak lebih dahulu."),
        ("f", "ΣF cos θ = 12(0,866) + 10(0,766) = 10,39 + 7,66 = 18,05 N"),
        ("f", "W~net~ = 18,05 × 8,5 = 153,4 J  ✓ (sama)"),
    ],
    cek=[
        "Kedua cara menghasilkan 153,4 J → perhitungan konsisten.",
        "Usaha total lebih kecil daripada (F₁ + F₂)d = 22 × 8,5 = 187 J, karena sebagian gaya "
        "miring tidak searah gerak ✓",
        "Kedua sudut < 90° sehingga kedua usaha positif, dan hasil akhirnya positif ✓",
    ],
    jawaban="W~net~ ≈ **153,4 J** (≈ 1,5 × 10² J).",
    catatan="Jika salah satu gaya mengarah ke belakang (misalnya gesekan, θ = 180°), usahanya "
            "negatif dan harus **dikurangkan**. Usaha total bisa nol walaupun benda bergerak — "
            "misalnya saat gaya dorong tepat diimbangi gesekan.",
),

dict(
    no=3, judul="Usaha oleh gaya yang berubah terhadap posisi",
    rumus_inti="W = ∫ F~x~ dx",
    sumber="Cheatsheet Minggu 4, poin 3 · Subbab 4-5",
    rumus=[("W = ∫ F~x~ dx, batas dari x~i~ (awal) sampai x~f~ (akhir)", None),
           ("W = luas daerah di bawah kurva F~x~ terhadap x", None)],
    penjabaran=[
        "**Mengapa perlu integral?** Rumus W = Fd hanya sah bila F **tetap**. Bila F berubah "
        "selama perpindahan, perjalanan harus dipecah menjadi potongan kecil Δx; pada potongan "
        "sekecil itu gaya boleh dianggap tetap, sehingga usaha potongan = F~x~ Δx. Jumlah seluruh "
        "potongan itulah integral: W = lim Σ F~x~ Δx = ∫F~x~ dx.",
        "**Arti geometris.** Integral tidak lain adalah **luas daerah** antara kurva F~x~ dan "
        "sumbu x. Karena itu soal gaya berubah sering diselesaikan tanpa integral, cukup dengan "
        "rumus luas bangun datar (lihat Soal 5).",
        "**Hubungan dengan energi kinetik.** Hasil integral ini langsung dipakai pada teorema "
        "usaha–energi: W = ΔK = ½m v~f~² − ½m v~i~².",
    ],
    lambang=[
        ("W", "usaha total oleh gaya yang bergantung posisi", "joule (J)"),
        ("F~x~", "komponen gaya pada arah x, boleh berupa fungsi x", "newton (N)"),
        ("dx", "elemen perpindahan yang sangat kecil", "meter (m)"),
        ("x~i~, x~f~", "posisi awal dan posisi akhir (batas integral)", "meter (m)"),
        ("∫", "penjumlahan kontinu — pengganti Σ bila potongan dibuat sangat kecil", "—"),
    ],
    satuan="[∫F~x~ dx] = N × m = J. Perhatikan bahwa **dx wajib dalam meter**; bila grafik "
           "memakai cm, luasnya harus dikonversi (1 cm = 10⁻² m).",
    syarat="Dipakai bila F bergantung pada posisi. Bila fungsinya linier (F = kx), hasilnya "
           "selalu ½kx² — yaitu luas segitiga di bawah kurvanya.",
    soal="Gaya F~x~ = 4x N bekerja pada benda bermassa 2 kg yang mula-mula diam, dari x = 0 "
         "sampai x = 3 m. Hitunglah usaha gaya itu dan laju akhir benda.",
    isi=[
        ("p", "**Diketahui:** F~x~ = 4x N; x~i~ = 0; x~f~ = 3 m; m = 2 kg; v~i~ = 0. "
              "**Ditanya:** W dan v~f~."),
        ("p", "**Langkah 1 — integralkan gaya.** Antiturunan 4x adalah 2x²:"),
        ("f", "W = ∫ F~x~ dx = ∫ 4x dx = [2x²], dari x = 0 sampai x = 3"),
        ("f", "W = 2(3)² − 2(0)² = 18 − 0 = 18 J"),
        ("p", "**Langkah 2 — ubah usaha menjadi laju** memakai W = ΔK dengan K~i~ = 0:"),
        ("f", "W = ½m v~f~²   →   18 = ½(2)v~f~²   →   v~f~² = 18"),
        ("f", "v~f~ = √18 ≈ 4,24 m/s"),
    ],
    cek=[
        "**Satuan:** ∫(N)dx = J ✓; ½mv² = kg·(m/s)² = J ✓",
        "**Cek dengan luas:** F naik linier 0 → 12 N sepanjang 3 m, luas segitiga = "
        "½ × 3 × 12 = 18 J ✓ (cocok dengan integral)",
        "**Kewajaran laju:** usaha 18 J pada benda 2 kg memberi v = √(2 × 18/2) = √18 ≈ 4,2 m/s; "
        "setara jatuh bebas 0,9 m — wajar untuk gaya beberapa newton.",
        "**Bandingkan dengan cara salah:** memakai F di x = 3 m (12 N) × 3 m = 36 J, dua kali "
        "lipat hasil yang benar. Inilah bukti bahwa F tidak boleh dianggap tetap.",
    ],
    jawaban="W = **18 J** dan v~f~ ≈ **4,24 m/s**.",
    catatan="Untuk gaya linier F = kx, hasil integral = ½k x². Pola inilah yang melahirkan rumus "
            "energi potensial pegas (Soal 12 dan 13).",
),

dict(
    no=4, judul="Usaha oleh gaya dua dimensi (perkalian titik)",
    rumus_inti="W = ∫F~x~ dx + ∫F~y~ dy",
    sumber="Cheatsheet Minggu 4, poin 4 · Subbab 4-5",
    rumus=[("W = ∫ F · dr = ∫F~x~ dx + ∫F~y~ dy", None)],
    penjabaran=[
        "**Arti rumusnya.** Pada bidang dua dimensi, gaya dan perpindahan masing-masing punya "
        "dua komponen. Perkalian titik **F · dr** hanya mempertemukan komponen yang sejenis: "
        "F~x~ dengan dx, dan F~y~ dengan dy. Karena itu integralnya terpecah menjadi dua bagian.",
        "**Cara mengerjakannya.** Kedua integral dihitung **terpisah** dengan batasnya "
        "masing-masing (batas x dari x awal ke x akhir; batas y dari y awal ke y akhir), kemudian "
        "hasilnya dijumlahkan. Tanda setiap suku muncul dari arah batasnya.",
        "**Yang tidak boleh dilakukan.** Menjumlahkan besar gaya lebih dahulu "
        "(|F| = √(F~x~² + F~y~²)) lalu dikalikan perpindahan. Cara itu hanya sah untuk gaya "
        "tetap; untuk gaya berubah, besar gaya berubah di setiap titik.",
    ],
    lambang=[
        ("W", "usaha total sepanjang lintasan dua dimensi", "joule (J)"),
        ("F", "vektor gaya, F = F~x~ î + F~y~ ĵ", "newton (N)"),
        ("dr", "vektor perpindahan kecil, dr = dx î + dy ĵ", "meter (m)"),
        ("F · dr", "perkalian titik — hanya komponen sejenis yang dikalikan", "joule (J)"),
        ("î, ĵ", "vektor satuan arah sumbu x dan y", "—"),
        ("F~x~, F~y~", "komponen gaya pada sumbu x dan y", "newton (N)"),
    ],
    satuan="[∫F~x~ dx] = N·m = J dan [∫F~y~ dy] = N·m = J; jumlahnya joule. Jika satu suku "
           "bersatuan lain, berarti ada komponen yang salah dimasukkan.",
    syarat="Gaya boleh bergantung pada posisi. Batas integral **wajib mengikuti arah gerak**: "
           "dari y = 3 m ke y = 0 m batasnya ditulis 3 → 0 (bukan 0 → 3).",
    soal="Gaya F = (3x² N) î + (4 N) ĵ bekerja pada sebuah partikel dan hanya mengubah energi "
         "kinetiknya. Berapa usaha gaya itu ketika partikel berpindah dari koordinat (2 m, 3 m) "
         "ke (3 m, 0 m)? Apakah laju partikel bertambah atau berkurang?",
    isi=[
        ("p", "**Diketahui:** F~x~ = 3x²; F~y~ = 4 N (tetap); dari (2, 3) m ke (3, 0) m. "
              "**Ditanya:** W dan perubahan laju."),
        ("p", "**Langkah 1 — pecah integral menjadi dua sumbu:**"),
        ("f", "W = ∫F~x~ dx + ∫F~y~ dy"),
        ("p", "**Langkah 2 — hitung suku x.** Antiturunan 3x² adalah x³, batas 2 → 3:"),
        ("f", "∫ 3x² dx = [x³] = 3³ − 2³ = 27 − 8 = +19 J"),
        ("p", "**Langkah 3 — hitung suku y.** Gaya 4 N tetap, sedangkan partikel bergerak turun "
              "dari y = 3 m ke y = 0 m, jadi batasnya 3 → 0:"),
        ("f", "∫ 4 dy = 4(0 − 3) = −12 J"),
        ("p", "**Langkah 4 — jumlahkan:**"),
        ("f", "W = 19 + (−12) = +7 J"),
        ("p", "**Langkah 5 — tentukan perubahan laju.** Karena W = ΔK dan W positif, energi "
              "kinetik bertambah sehingga laju bertambah."),
    ],
    cek=[
        "**Satuan:** kedua suku joule, jumlahnya joule ✓",
        "**Tanda:** suku y negatif karena gerak berlawanan dengan F~y~ (turun, sedangkan F~y~ ke "
        "atas) ✓",
        "**Gantian arah:** jika partikel bergerak dari (2, 0) ke (3, 3), suku y menjadi +12 J dan "
        "W = +31 J — hasilnya berubah bila lintasannya berbeda, sebagaimana mestinya.",
        "**Kesimpulan laju:** W = +7 J > 0 → v bertambah (ΔK = +7 J) ✓",
    ],
    jawaban="W = **+7 J**; laju partikel **bertambah**.",
    catatan="Soal ini sering dikira harus memakai jarak lurus dari (2,3) ke (3,0). Yang dipakai "
            "adalah **komponen** perpindahan: Δx = +1 m dan Δy = −3 m.",
),

dict(
    no=5, judul="Usaha dari luas grafik gaya–posisi",
    rumus_inti="W = luas bertanda di bawah kurva F~x~–x",
    sumber="Cheatsheet Minggu 4, poin 5 · Subbab 4-5",
    rumus=[("W = luas daerah antara kurva F~x~ dan sumbu x", None),
           ("Luas segitiga = ½ a t ·  luas persegi = p l ·  luas trapesium = ½(a + b) h", None)],
    penjabaran=[
        "**Arti rumusnya.** Karena W = ∫F~x~ dx, usaha sama dengan luas daerah di bawah kurva. "
        "Membaca grafik berarti menghitung luas, tanpa perlu mencari fungsi F(x).",
        "**Aturan tanda.** Daerah **di atas** sumbu x → usaha positif (gaya searah gerak). "
        "Daerah **di bawah** sumbu x → usaha negatif (gaya melawan gerak). Usaha total adalah "
        "**selisih** kedua luas itu.",
        "**Satuan luas.** Satu kotak pada grafik bernilai (N) × (m) = J. Karena itu luas grafik "
        "F–x **langsung** merupakan usaha, berbeda dengan grafik a–x yang harus dikalikan massa.",
    ],
    lambang=[
        ("W", "usaha, secara numerik = luas daerah pada grafik", "joule (J)"),
        ("F~x~", "gaya, digambar pada sumbu vertikal", "newton (N)"),
        ("x", "posisi, digambar pada sumbu horizontal", "meter (m)"),
        ("a, b", "sisi-sisi sejajar trapesium (panjang pada sumbu x)", "meter (m)"),
        ("h", "tinggi bangun = nilai gaya", "newton (N)"),
    ],
    satuan="[luas] = N × m = J. Jika sumbu x dinyatakan dalam cm, luas harus dikalikan 10⁻² "
           "supaya menjadi joule.",
    syarat="Kurva harus tersusun dari garis lurus sehingga luasnya dapat dihitung dengan rumus "
           "bangun datar. Bila melengkung, gunakan integral (Soal 3).",
    soal="Grafik gaya terhadap posisi berbentuk segitiga: F = 0 di x = 0 dan naik linier sampai "
         "10 N di x = 4 m. Hitunglah usaha gaya itu. Jika benda bermassa 2 kg mula-mula diam, "
         "berapa lajunya di x = 4 m?",
    isi=[
        ("p", "**Diketahui:** kurva segitiga dengan alas 4 m dan tinggi 10 N; m = 2 kg; "
              "v~i~ = 0. **Ditanya:** W dan v."),
        ("p", "**Langkah 1 — hitung luas segitiga:**"),
        ("f", "W = ½ × alas × tinggi = ½ × (4 m)(10 N) = 20 J"),
        ("p", "**Langkah 2 — ubah menjadi laju** dengan W = ΔK:"),
        ("f", "20 = ½(2)v²   →   v² = 20   →   v = √20 ≈ 4,47 m/s"),
    ],
    cek=[
        "**Satuan:** luas = m × N = J ✓",
        "**Cek dengan integral:** F = 2,5x (karena naik 0→10 N atas 4 m), maka "
        "∫2,5x dx = 1,25x² = 1,25(16) = 20 J ✓",
        "**Kewajaran:** gaya rata-ratanya 5 N sepanjang 4 m → 20 J ✓",
        "**Konsistensi laju:** v = √(2W/m) = √(40/2) = 4,47 m/s ✓",
    ],
    jawaban="W = **20 J**; v ≈ **4,47 m/s**.",
    catatan="Bila kurva turun di bawah sumbu (misalnya gaya menahan), luasnya bertanda negatif. "
            "Contoh lengkap dengan dua daerah: Soal 34 pada dokumen versi 34 soal "
            "(2.800 J lalu −700 J).",
),

dict(
    no=6, judul="Teorema usaha–energi kinetik",
    rumus_inti="W~net~ = ΔK = ½m(v~f~² − v~i~²)",
    sumber="Cheatsheet Minggu 4, poin 6 · Subbab 4-2",
    rumus=[("W~net~ = ΔK = ½m v~f~² − ½m v~i~²", None)],
    penjabaran=[
        "**Arti rumusnya.** Usaha total yang bekerja pada benda **seluruhnya** berubah menjadi "
        "perubahan energi kinetik. Tidak ada energi yang hilang: jika usaha positif, laju naik; "
        "jika negatif, laju turun; jika nol, laju tetap.",
        "**Asal rumusnya (penjabaran singkat).** Ambil gaya tetap searah gerak. Dari kinematika, "
        "v~f~² = v~i~² + 2a d sehingga a d = (v~f~² − v~i~²)/2. Karena W = F d = (ma)d, maka "
        "W = m × (v~f~² − v~i~²)/2 = ½m v~f~² − ½m v~i~². Jadi teorema ini sebenarnya gabungan "
        "hukum II Newton dan kinematika.",
        "**Kekuatan rumus ini.** Berlaku walaupun gaya berubah dan lintasannya melengkung, asalkan "
        "W~net~ adalah usaha **total** semua gaya. Karena itu ia dipakai berulang pada soal 3, 5, "
        "dan 7.",
    ],
    lambang=[
        ("W~net~", "usaha total semua gaya pada benda", "joule (J)"),
        ("ΔK", "perubahan energi kinetik, K~f~ − K~i~", "joule (J)"),
        ("m", "massa benda", "kilogram (kg)"),
        ("v~i~, v~f~", "besar kecepatan awal dan akhir (laju, bukan vektor)", "meter/sekon (m/s)"),
        ("K = ½mv²", "energi kinetik — skalar, selalu ≥ 0", "joule (J)"),
    ],
    satuan="[½mv²] = kg·(m/s)² = kg·m²/s² = J; [W] = J. Kedua ruas bersatuan sama, jadi rumus ini "
           "konsisten secara dimensi.",
    syarat="W~net~ harus usaha **total**, bukan usaha satu gaya saja. Jika ada gaya gesek, "
           "usahanya (negatif) wajib ikut dijumlahkan.",
    soal="Sebuah benda bermassa 2 kg berubah kelajuannya dari 3 m/s menjadi 5 m/s. Hitunglah "
         "usaha total yang bekerja pada benda.",
    isi=[
        ("p", "**Diketahui:** m = 2 kg; v~i~ = 3 m/s; v~f~ = 5 m/s. **Ditanya:** W~net~."),
        ("p", "**Langkah 1 — tulis rumusnya:**"),
        ("f", "W~net~ = ½m(v~f~² − v~i~²)"),
        ("p", "**Langkah 2 — hitung selisih kuadrat:** 5² = 25 dan 3² = 9, selisihnya 16."),
        ("f", "W~net~ = ½(2)(16) = 16 J"),
        ("p", "**Cara kedua (pemeriksaan):** hitung energi kinetik awal dan akhir terpisah."),
        ("f", "K~i~ = ½(2)(3²) = 9 J   dan   K~f~ = ½(2)(5²) = 25 J   →   W = 25 − 9 = 16 J  ✓"),
    ],
    cek=[
        "Kedua cara memberi 16 J ✓",
        "Tanda positif karena laju naik → usaha total memang menambah energi ✓",
        "Perhatikan: selisih laju hanya 2 m/s, tetapi usaha bergantung pada **selisih kuadrat** "
        "(16), bukan pada selisih laju (2).",
        "Jika laju turun dari 5 ke 3 m/s, hasilnya −16 J (benda kehilangan energi).",
    ],
    jawaban="W~net~ = **+16 J**.",
    catatan="Menambah laju dari 3 ke 5 m/s (Δv = 2) memerlukan 16 J, tetapi dari 5 ke 7 m/s "
            "(Δv = 2 juga) memerlukan 24 J. Karena itu kecelakaan pada laju tinggi jauh lebih "
            "merusak.",
),

dict(
    no=7, judul="Jarak pengereman: mengapa laju dua kali berarti jarak empat kali",
    rumus_inti="d~stop~ ∝ v²",
    sumber="Cheatsheet Minggu 4, poin 7 · penerapan Subbab 4-2",
    rumus=[("d~stop~ = m v²/(2f)   →   d~2~/d~1~ = (v~2~/v~1~)²", None)],
    penjabaran=[
        "**Arti rumusnya.** Jarak yang diperlukan untuk berhenti tidak sebanding dengan laju, "
        "melainkan dengan **kuadrat** laju. Akibatnya, laju dua kali lipat memerlukan jarak empat "
        "kali lipat.",
        "**Asal rumusnya.** Saat mengerem, gaya rem f melawan gerak sehingga W = −f d. Benda "
        "berhenti (v~f~ = 0), maka dari teorema usaha–energi: −f d = 0 − ½mv², sehingga "
        "d = mv²/(2f). Bila m dan f tetap, seluruh faktor lain konstan dan tinggal d ∝ v².",
        "**Bentuk perbandingan.** Karena konstanta m/(2f) sama untuk kedua keadaan, konstanta itu "
        "hilang saat dibagi: d₂/d₁ = (v₂/v₁)². Cara ini menghindari keharusan mengetahui massa "
        "dan gaya rem.",
    ],
    lambang=[
        ("d~stop~", "jarak tempuh sampai benda berhenti", "meter (m)"),
        ("v", "laju tepat saat pengereman dimulai", "meter/sekon (m/s)"),
        ("m", "massa kendaraan (boleh tidak diketahui)", "kilogram (kg)"),
        ("f", "besar gaya pengereman/gesek (dianggap tetap)", "newton (N)"),
        ("d₁, d₂", "jarak berhenti pada keadaan 1 dan 2", "meter (m)"),
        ("v₁, v₂", "laju awal pada keadaan 1 dan 2", "meter/sekon (m/s)"),
    ],
    satuan="[dv²/f] = kg·(m/s)² / N = (kg·m²/s²)/(kg·m/s²) = m ✓ — satuannya memang meter, "
           "sehingga rumus d = mv²/(2f) sah secara dimensi.",
    syarat="Gaya rem **sama** pada kedua keadaan dan jalan mendatar. Bila gaya rem berbeda "
           "(misalnya jalan licin), perbandingan kuadrat tidak berlaku.",
    soal="Jarak berhenti sebuah mobil adalah 18 m pada laju 54 km/jam. Berapa jarak berhentinya "
         "pada laju 108 km/jam?",
    isi=[
        ("p", "**Diketahui:** d₁ = 18 m pada v₁ = 54 km/jam; ditanya d₂ pada v₂ = 108 km/jam."),
        ("p", "**Langkah 1 — ubah satuan lebih dahulu** (bagi 3,6):"),
        ("f", "v₁ = 54/3,6 = 15 m/s      v₂ = 108/3,6 = 30 m/s"),
        ("p", "**Langkah 2 — pakai perbandingan kuadrat:**"),
        ("f", "d₂/d₁ = (v₂/v₁)² = (30/15)² = 2² = 4"),
        ("f", "d₂ = 4 × 18 m = 72 m"),
        ("p", "**Cara kedua (memeriksa dengan gaya rem):** dari d₁ diperoleh perlambatan "
              "a = v₁²/(2d₁) = 225/36 = 6,25 m/s²; lalu untuk v₂:"),
        ("f", "d₂ = v₂²/(2a) = 900/(2 × 6,25) = 900/12,5 = 72 m  ✓"),
    ],
    cek=[
        "Kedua cara memberi 72 m ✓",
        "Perbandingan laju = 2 → perbandingan jarak = 4 (bukan 2) ✓ sesuai d ∝ v².",
        "Kewajaran: mobil pada 108 km/jam memang memerlukan jarak pengereman yang jauh lebih "
        "panjang; 72 m kira-kira sepanjang 18 mobil.",
        "Satuan sudah SI sebelum dimasukkan, sehingga tidak ada faktor 3,6 yang tertinggal.",
    ],
    jawaban="Jarak berhenti menjadi **72 m**.",
    catatan="Karena d ∝ v², menambah laju 10% menambah jarak berhenti ≈ 21%. Inilah dasar fisis "
            "batas kecepatan di jalan raya.",
),

dict(
    no=8, judul="Daya rata-rata dan daya sesaat",
    rumus_inti="P~avg~ = W/Δt ; P = F v cos θ",
    sumber="Cheatsheet Minggu 4, poin 8 · Subbab 4-6",
    rumus=[("P~avg~ = W/Δt", None), ("P = F v cos θ", None)],
    penjabaran=[
        "**Arti rumusnya.** Daya adalah **laju** pemindahan energi: berapa joule energi "
        "dipindahkan setiap sekon. Usaha yang sama bila dilakukan lebih cepat berarti dayanya "
        "lebih besar.",
        "**Asal P = F v.** Dari P = W/Δt dan W = F d cos θ, maka P = (F d cos θ)/Δt = "
        "F cos θ × (d/Δt) = F v cos θ. Jadi daya sesaat muncul dari membagi perpindahan dengan "
        "waktu — yaitu laju.",
        "**Dua versi yang harus dibedakan.** P~avg~ = W/Δt berlaku untuk selang waktu tertentu "
        "(rata-rata). P = F·v berlaku pada satu saat, memakai gaya dan laju pada saat itu.",
    ],
    lambang=[
        ("P~avg~", "daya rata-rata selama selang Δt", "watt (W) = J/s"),
        ("W", "usaha total yang dilakukan", "joule (J)"),
        ("Δt", "selang waktu", "sekon (s)"),
        ("P", "daya sesaat", "watt (W)"),
        ("F", "gaya pada saat itu", "newton (N)"),
        ("v", "laju benda pada saat itu", "meter/sekon (m/s)"),
        ("θ", "sudut antara gaya dan arah kecepatan", "derajat (°)"),
    ],
    satuan="[P] = J/s = **watt (W)**; [F v] = N·m/s = (kg·m/s²)(m/s) = kg·m²/s³ = J/s = W ✓. "
           "Satuan lain: 1 hp = 746 W, 1 kWh = 3,6 × 10⁶ J.",
    syarat="P = W/Δt sah untuk daya rata-rata; untuk daya sesaat gunakan P = F·v. Bila gaya "
           "membentuk sudut terhadap gerak, sertakan cos θ.",
    soal="(a) Sebuah mesin melakukan usaha 600 J dalam 10 s. (b) Sebuah motor memberi gaya 20 N "
         "searah gerak ketika lajunya 3 m/s. Hitunglah daya pada kedua contoh.",
    isi=[
        ("p", "**Bagian (a) — daya rata-rata:**"),
        ("f", "P~avg~ = W/Δt = 600 J / 10 s = 60 W"),
        ("p", "**Bagian (b) — daya sesaat** dengan θ = 0° (gaya searah gerak):"),
        ("f", "P = F v cos θ = (20 N)(3 m/s)(1) = 60 W"),
    ],
    cek=[
        "Satuan: J/s = W dan N·m/s = W ✓",
        "Angka kebetulan sama (60 W), tetapi maknanya berbeda: (a) rata-rata 10 sekon, "
        "(b) sesaat pada v = 3 m/s.",
        "Kewajaran: 60 W ≈ 0,08 hp, sebanding dengan bola lampu — wajar untuk usaha 600 J "
        "dalam 10 s.",
        "Jika θ = 60°, maka P = 20 × 3 × 0,5 = 30 W (daya bergantung pada cos θ) ✓",
    ],
    jawaban="Keduanya **60 W** (≈ 0,08 hp).",
    catatan="Pada kendaraan dengan daya mesin tetap, gaya dorong menurun saat laju naik "
            "(F = P/v). Karena itu percepatan mobil melemah pada kecepatan tinggi.",
),

# ======================================================== MINGGU 5
dict(
    no=9, judul="Energi potensial gravitasi dan usaha gravitasi",
    rumus_inti="ΔU~g~ = mgΔy ; W~g~ = −ΔU~g~",
    sumber="Cheatsheet Minggu 5, poin 9 · Subbab 5-1",
    rumus=[("U~g~ = mgy", None), ("ΔU~g~ = mg(y~f~ − y~i~) = mgΔy", None), ("W~g~ = −ΔU~g~", None)],
    penjabaran=[
        "**Arti rumusnya.** Energi potensial adalah energi yang **tersimpan karena posisi**. "
        "Benda yang berada lebih tinggi menyimpan lebih banyak energi, dan energi itu baru "
        "terpakai ketika benda turun.",
        "**Asal tanda negatif.** Energi potensial didefinisikan dari usaha gaya konservatif: "
        "ΔU = −W~konservatif~. Ketika benda **naik**, gaya gravitasi menahan (usaha negatif), "
        "sehingga ΔU **positif**. Ketika benda **turun**, gravitasi membantu (usaha positif), "
        "sehingga ΔU **negatif**.",
        "**Tentang titik acuan.** Yang bermakna fisis hanyalah **selisih** ΔU, bukan nilai U "
        "sendiri. Karena itu y = 0 boleh diletakkan di mana saja; hasil ΔU tidak berubah.",
    ],
    lambang=[
        ("U~g~", "energi potensial gravitasi pada ketinggian y", "joule (J)"),
        ("m", "massa benda", "kilogram (kg)"),
        ("g", "percepatan gravitasi, 9,8 m/s²", "meter/sekon² (m/s²)"),
        ("y", "ketinggian diukur dari titik acuan y = 0", "meter (m)"),
        ("Δy", "perpindahan vertikal, y~f~ − y~i~", "meter (m)"),
        ("W~g~", "usaha oleh gaya gravitasi", "joule (J)"),
    ],
    satuan="[mgy] = kg·(m/s²)·m = kg·m²/s² = J ✓. ΔU dan W~g~ sama-sama joule, hanya tandanya "
           "berlawanan.",
    syarat="Berlaku dekat permukaan bumi (g dianggap tetap). Untuk ketinggian sangat besar, g "
           "berubah dan harus memakai bentuk −GMm/r.",
    soal="Sebuah benda bermassa 2 kg diangkat dari y = 2 m ke y = 5 m. Hitunglah perubahan "
         "energi potensial gravitasinya dan usaha yang dilakukan gaya gravitasi.",
    isi=[
        ("p", "**Diketahui:** m = 2 kg; y~i~ = 2 m; y~f~ = 5 m; g = 9,8 m/s². "
              "**Ditanya:** ΔU~g~ dan W~g~."),
        ("p", "**Langkah 1 — hitung perpindahan vertikalnya:**"),
        ("f", "Δy = y~f~ − y~i~ = 5 − 2 = +3 m"),
        ("p", "**Langkah 2 — masukkan ke rumus energi potensial:**"),
        ("f", "ΔU~g~ = mgΔy = (2)(9,8)(3) = +58,8 J"),
        ("p", "**Langkah 3 — usaha gravitasi adalah negatif dari ΔU:**"),
        ("f", "W~g~ = −ΔU~g~ = −58,8 J"),
    ],
    cek=[
        "Tanda ΔU positif karena benda **naik** ✓",
        "Tanda W~g~ negatif karena gravitasi berarah ke bawah, sedangkan perpindahan ke atas "
        "(θ = 180°) ✓",
        "Cek langsung: W~g~ = mgd cos 180° = (2)(9,8)(3)(−1) = −58,8 J, sama dengan hasil di atas ✓",
        "Jika bendanya turun 3 m: ΔU = −58,8 J dan W~g~ = +58,8 J (tanda bertukar) ✓",
    ],
    jawaban="ΔU~g~ = **+58,8 J** dan W~g~ = **−58,8 J**.",
    catatan="Usaha oleh gaya **angkat** (gaya luar) justru +58,8 J. Bila benda diangkat dengan "
            "laju tetap, W~angkat~ + W~gravitasi~ = 0 — itulah sebabnya energi kinetik tidak "
            "berubah.",
),

dict(
    no=10, judul="Kekekalan energi mekanik (jatuh bebas)",
    rumus_inti="K~i~ + U~i~ = K~f~ + U~f~",
    sumber="Cheatsheet Minggu 5, poin 10 · Subbab 5-2",
    rumus=[("K~i~ + U~i~ = K~f~ + U~f~", None),
           ("½m v~i~² + mgy~i~ = ½m v~f~² + mgy~f~", None)],
    penjabaran=[
        "**Arti rumusnya.** Bila hanya gaya konservatif (gravitasi, pegas) yang melakukan usaha, "
        "jumlah energi kinetik dan energi potensial **tetap**. Energi boleh berpindah bentuk "
        "(potensial → kinetik), tetapi jumlahnya tidak berubah.",
        "**Asal rumusnya.** Dari W~net~ = ΔK dan W~net~ = W~g~ = −ΔU, diperoleh ΔK = −ΔU, yaitu "
        "ΔK + ΔU = 0. Artinya K + U = tetap, sehingga nilai di keadaan awal sama dengan di "
        "keadaan akhir.",
        "**Bentuk praktis untuk jatuh bebas.** Dengan v~i~ = 0 dan y~f~ = 0, persamaan menyusut "
        "menjadi mgy~i~ = ½m v~f~² → v~f~ = √(2g y~i~). Massa m terhapus, sehingga laju tidak "
        "bergantung pada massa.",
    ],
    lambang=[
        ("K", "energi kinetik, K = ½mv²", "joule (J)"),
        ("U", "energi potensial (di sini gravitasi), U = mgy", "joule (J)"),
        ("E~mech~", "energi mekanik total, E = K + U", "joule (J)"),
        ("v~i~, v~f~", "laju awal dan akhir", "meter/sekon (m/s)"),
        ("y~i~, y~f~", "ketinggian awal dan akhir terhadap acuan", "meter (m)"),
    ],
    satuan="Kedua ruas joule: [½mv²] = J dan [mgy] = J ✓. Karena itu persamaan hanya sah bila "
           "semua suku ditulis dalam SI.",
    syarat="**Tidak ada** gaya nonkonservatif yang melakukan usaha (tanpa gesekan, tanpa tarikan "
           "luar). Jika ada gesekan, gunakan ΔE~mech~ = W~nc~ (Soal 16).",
    soal="Sebuah benda mulai dari keadaan diam pada ketinggian 12 m. Gesekan udara diabaikan. "
         "Hitunglah lajunya ketika tiba di dasar.",
    isi=[
        ("p", "**Diketahui:** v~i~ = 0; y~i~ = 12 m; y~f~ = 0. **Ditanya:** v~f~."),
        ("p", "**Langkah 1 — tulis kekekalan energi mekanik:**"),
        ("f", "K~i~ + U~i~ = K~f~ + U~f~"),
        ("p", "**Langkah 2 — masukkan bentuk tiap suku:**"),
        ("f", "0 + mg(12) = ½m v~f~² + 0"),
        ("p", "**Langkah 3 — hapus m di kedua ruas, lalu selesaikan:**"),
        ("f", "g(12) = ½v~f~²   →   v~f~ = √(2 × 9,8 × 12) = √235,2"),
        ("f", "v~f~ ≈ 15,3 m/s"),
    ],
    cek=[
        "**Satuan:** 2gh = (m/s²)(m) = m²/s², akarnya m/s ✓",
        "**Cek dengan kinematika:** t = √(2h/g) = √(24/9,8) = 1,56 s dan v = gt = 9,8 × 1,56 = "
        "15,3 m/s ✓",
        "**Kewajaran:** jatuh 12 m (≈ 4 lantai) menghasilkan ≈ 55 km/jam — masuk akal.",
        "Hasil tidak bergantung pada massa, sesuai sifat jatuh bebas ✓",
    ],
    jawaban="v~f~ ≈ **15,3 m/s** (√235,2 m/s).",
    catatan="Rumus v = √(2gh) hanya untuk **dilepas dari diam**. Bila dilempar ke bawah dengan "
            "laju awal v~i~, hasilnya v~f~ = √(v~i~² + 2gh).",
),

dict(
    no=11, judul="Energi mekanik pada roller-coaster",
    rumus_inti="½mv² + mgy = konstan",
    sumber="Cheatsheet Minggu 5, poin 11 · Subbab 5-2",
    rumus=[("½m v² + mgy = tetap (sama di setiap titik lintasan)", None),
           ("v = √(2g(y~1~ − y))        y = y~1~ − v²/(2g)", None)],
    penjabaran=[
        "**Arti rumusnya.** Ini bentuk lain dari Soal 10: energi mekanik total tetap sepanjang "
        "lintasan. Jika kereta turun, mgy berkurang dan ½mv² bertambah dengan jumlah yang sama.",
        "**Dua bentuk yang dipakai bergantian.** Untuk mencari laju di ketinggian tertentu: "
        "v = √(2g(y₁ − y)). Untuk mencari ketinggian saat lajunya diketahui: "
        "y = y₁ − v²/(2g). Keduanya berasal dari persamaan yang sama.",
        "**Mengapa bentuk lintasan tidak berpengaruh.** Yang bekerja hanya gravitasi (gaya "
        "konservatif) dan gaya normal rel yang selalu tegak lurus gerak. Gaya tegak lurus tidak "
        "melakukan usaha, sehingga bentuk lekuk lintasan tidak masuk ke perhitungan.",
    ],
    lambang=[
        ("v", "laju kereta pada ketinggian tertentu", "meter/sekon (m/s)"),
        ("y", "ketinggian titik itu dari acuan (dasar)", "meter (m)"),
        ("y₁", "ketinggian awal (puncak)", "meter (m)"),
        ("m", "massa kereta — terhapus dalam perhitungan", "kilogram (kg)"),
        ("½mv²", "energi kinetik", "joule (J)"),
        ("mgy", "energi potensial gravitasi", "joule (J)"),
    ],
    satuan="Kedua suku joule ✓. Pada bentuk v = √(2gΔy), satuannya √((m/s²)(m)) = m/s ✓.",
    syarat="Lintasan licin dan tidak ada motor/rem selama gerak. Jika ada gesekan, laju "
           "sesungguhnya lebih kecil daripada hasil hitungan.",
    soal="Sebuah kereta roller-coaster mulai dari keadaan diam pada ketinggian h = 40 m. "
         "Hitunglah (a) laju di dasar bukit, dan (b) ketinggian saat lajunya 14 m/s.",
    isi=[
        ("p", "**Diketahui:** y₁ = 40 m; v₁ = 0; g = 9,8 m/s². **Ditanya:** (a) v di y = 0; "
              "(b) y saat v = 14 m/s."),
        ("p", "**(a) Laju di dasar.** Bandingkan puncak (1) dengan dasar (2):"),
        ("f", "½m v₁² + mgy₁ = ½m v₂² + mgy₂"),
        ("f", "0 + (9,8)(40) = ½v₂² + 0   →   392 = ½v₂²"),
        ("f", "v₂² = 784   →   v₂ = 28 m/s"),
        ("p", "**(b) Ketinggian saat v = 14 m/s.** Pakai persamaan yang sama, dari puncak ke "
              "titik berketinggian y:"),
        ("f", "g y₁ = ½v² + g y   →   y = y₁ − v²/(2g)"),
        ("f", "y = 40 − (14)²/(2 × 9,8) = 40 − 196/19,6 = 40 − 10 = 30 m"),
    ],
    cek=[
        "**(a)** v = √(2 × 9,8 × 40) = √784 = 28 m/s ✓ (sama dengan √(2gh) pada Soal 10)",
        "**(b)** Substitusikan balik: ½(14²) + 9,8(30) = 98 + 294 = 392 J/kg — sama dengan "
        "9,8 × 40 = 392 J/kg ✓",
        "**Kewajaran:** setengah laju berarti seperempat energi kinetik, sehingga kereta masih "
        "tinggi (30 m dari 40 m), bukan di 20 m.",
        "Satuan: y dalam meter, v dalam m/s, g dalam m/s² ✓",
    ],
    jawaban="(a) v = **28 m/s**; (b) lajunya 14 m/s pada ketinggian **30 m**.",
    catatan="Bila ditanya laju di titik berketinggian 25 m: v = √(2 × 9,8 × (40 − 25)) = "
            "√294 ≈ 17,1 m/s. Pola rumusnya selalu sama.",
),

dict(
    no=12, judul="Energi pegas berubah menjadi energi gerak",
    rumus_inti="½k x² = ½m v²",
    sumber="Cheatsheet Minggu 5, poin 12 · Subbab 5-2 dan 4-4",
    rumus=[("U~s~ = ½k x²", None), ("½k x² = ½m v²   →   v = x √(k/m)", None)],
    penjabaran=[
        "**Arti rumusnya.** Pegas yang termampatkan (atau tertarik) menyimpan energi potensial "
        "elastis ½kx². Ketika dilepas, energi itu berubah menjadi energi kinetik benda yang "
        "didorongnya.",
        "**Asal rumus ½kx².** Gaya pegas F = kx bertambah besar seiring simpangan, jadi tidak "
        "boleh memakai W = Fx. Dengan integral: U~s~ = ∫kx dx = ½kx² — yaitu luas segitiga pada "
        "grafik F–x dengan tinggi kx dan alas x.",
        "**Bentuk siap pakai.** Dari ½kx² = ½mv² diperoleh v = x√(k/m). Terlihat bahwa laju "
        "lontaran sebanding dengan **simpangan**, sehingga memampatkan dua kali lipat "
        "menghasilkan laju dua kali lipat — tetapi energi empat kali lipat.",
    ],
    lambang=[
        ("U~s~", "energi potensial elastis pegas", "joule (J)"),
        ("k", "konstanta pegas (kekakuan)", "newton/meter (N/m)"),
        ("x", "simpangan dari panjang relaks (mampatan/regangan)", "meter (m)"),
        ("m", "massa benda yang didorong pegas", "kilogram (kg)"),
        ("v", "laju benda setelah lepas dari pegas", "meter/sekon (m/s)"),
    ],
    satuan="[½kx²] = (N/m)(m²) = N·m = J ✓; [½mv²] = J ✓. Perhatikan x **wajib** dalam meter: "
           "10 cm harus ditulis 0,10 m.",
    syarat="Pegas tidak bermassa, tanpa gesekan, dan x diukur dari panjang **relaks**. Bila ada "
           "gesekan, sebagian energi berubah menjadi panas (Soal 15).",
    soal="Sebuah benda bermassa 0,20 kg dilontarkan oleh pegas dengan k = 200 N/m yang "
         "termampatkan 0,10 m. Hitunglah laju benda setelah lepas dari pegas (tanpa gesekan).",
    isi=[
        ("p", "**Diketahui:** m = 0,20 kg; k = 200 N/m; x = 0,10 m. **Ditanya:** v."),
        ("p", "**Langkah 1 — hitung energi yang tersimpan di pegas:**"),
        ("f", "U~s~ = ½k x² = ½(200)(0,10)² = 100 × 0,0100 = 1,0 J"),
        ("p", "**Langkah 2 — seluruh energi itu menjadi energi kinetik:**"),
        ("f", "½k x² = ½m v²   →   1,0 = ½(0,20)v²"),
        ("f", "1,0 = 0,10 v²   →   v² = 10   →   v = √10 ≈ 3,16 m/s"),
        ("p", "**Cara kedua:** v = x√(k/m) = 0,10 × √(200/0,20) = 0,10 × √1000 ≈ 3,16 m/s ✓"),
    ],
    cek=[
        "**Satuan:** √(k/m) = √((N/m)/kg) = √(1/s²) = 1/s; dikalikan x (m) menghasilkan m/s ✓",
        "**Kedua cara** memberi 3,16 m/s ✓",
        "**Kewajaran:** pegas 200 N/m cukup kaku; benda ringan 0,2 kg terlempar ≈ 3 m/s — "
        "masuk akal.",
        "Jika x dinaikkan menjadi 0,20 m, energi menjadi 4,0 J dan laju menjadi 6,3 m/s "
        "(dua kali lipat) ✓",
    ],
    jawaban="v ≈ **3,16 m/s**.",
    catatan="Kesalahan klasik: menulis x = 10 (cm) ke dalam rumus. Hasilnya akan membesar "
            "100 kali. Selalu ubah ke meter lebih dahulu.",
),

dict(
    no=13, judul="Gaya Hooke dan usaha oleh pegas",
    rumus_inti="F~s~ = −k x ; W~s~ = ½k(x~i~² − x~f~²)",
    sumber="Cheatsheet Minggu 5, poin 13 · Subbab 4-4 dan 5-1",
    rumus=[("F~s~ = −k x", None),
           ("W~s~ = ½k(x~i~² − x~f~²) = −ΔU~s~", None)],
    penjabaran=[
        "**Arti rumus F = −kx (Hukum Hooke).** Besar gaya pegas sebanding dengan simpangannya; "
        "tanda minus menyatakan arahnya **selalu menuju posisi setimbang** (gaya pemulih). "
        "Makin jauh ditarik, makin kuat pegas menarik kembali.",
        "**Asal rumus usaha.** Karena F berubah, usaha dihitung dengan integral: "
        "W~s~ = ∫(−kx)dx dari x~i~ ke x~f~ = ½k x~i~² − ½k x~f~². Bentuk ini sama dengan "
        "−ΔU~s~, sesuai definisi energi potensial.",
        "**Tafsir tanda.** Jika pegas bergerak **menuju** setimbang (|x~f~| < |x~i~|), usahanya "
        "positif — pegas mendorong benda sehingga energi pegas berkurang. Jika pegas makin "
        "termampatkan, usahanya negatif.",
    ],
    lambang=[
        ("F~s~", "gaya pegas; tanda (−) = arah menuju posisi setimbang", "newton (N)"),
        ("k", "konstanta pegas", "newton/meter (N/m)"),
        ("x", "simpangan dari posisi setimbang", "meter (m)"),
        ("W~s~", "usaha yang dilakukan gaya pegas", "joule (J)"),
        ("x~i~, x~f~", "simpangan awal dan akhir", "meter (m)"),
        ("ΔU~s~", "perubahan energi potensial pegas, ½k x~f~² − ½k x~i~²", "joule (J)"),
    ],
    satuan="[kx] = (N/m)(m) = N ✓ untuk gaya; [½kx²] = (N/m)(m²) = J ✓ untuk energi. Keduanya "
           "konsisten.",
    syarat="Pegas ideal (berlaku linier sampai batas elastis). Untuk pegas nyata yang ditarik "
           "terlalu jauh, hukum Hooke tidak lagi berlaku.",
    soal="Sebuah pegas dengan k = 200 N/m bergerak dari x~i~ = 0,10 m ke x~f~ = 0,04 m. "
         "Hitunglah (a) gaya pegas pada saat x~i~, dan (b) usaha yang dilakukan pegas.",
    isi=[
        ("p", "**(a) Gaya pegas pada x~i~:**"),
        ("f", "F~s~ = −k x~i~ = −(200)(0,10) = −20 N"),
        ("p", "Tanda negatif berarti gaya berarah **melawan** simpangan, yaitu menuju posisi "
              "setimbang."),
        ("p", "**(b) Usaha pegas dari x~i~ ke x~f~:**"),
        ("f", "W~s~ = ½k(x~i~² − x~f~²) = ½(200)[(0,10)² − (0,04)²]"),
        ("f", "W~s~ = 100 × (0,0100 − 0,0016) = 100 × 0,0084 = +0,84 J"),
    ],
    cek=[
        "**Cek lewat energi potensial:** U~i~ = ½(200)(0,10²) = 1,00 J dan U~f~ = ½(200)(0,04²) "
        "= 0,16 J; maka W~s~ = U~i~ − U~f~ = 1,00 − 0,16 = **+0,84 J** ✓",
        "**Tanda:** |x~f~| < |x~i~|, pegas menuju setimbang → usaha harus positif ✓",
        "**Gaya:** F = −20 N pada x = 0,10 m; gaya rata-ratanya setengahnya (≈10 N) karena gaya "
        "turun linier, dan 10 N × 0,06 m ≈ 0,6 J — seorde dengan 0,84 J ✓",
        "**Satuan:** (N/m)(m²) = J ✓",
    ],
    jawaban="(a) F~s~ = **−20 N**; (b) W~s~ = **+0,84 J**.",
    catatan="Jangan memakai W = F d cos θ untuk pegas: gaya 20 N itu hanya berlaku **sesaat** di "
            "x = 0,10 m, bukan sepanjang perpindahan. Yang benar adalah bentuk selisih kuadrat.",
),

dict(
    no=14, judul="Bola jatuh menekan pegas: menentukan konstanta pegas",
    rumus_inti="mg(h + x) = ½k x²",
    sumber="Cheatsheet Minggu 5, poin 14 · slide EXAMPLE 6-11",
    rumus=[("mg(h + Y) = ½k Y²", None), ("k = 2mg(h + Y)/Y²", None)],
    penjabaran=[
        "**Arti rumusnya.** Bola jatuh dari ketinggian h di atas ujung pegas, lalu memampatkan "
        "pegas sebesar Y. Selama itu energi potensial gravitasi berubah menjadi energi potensial "
        "pegas. Karena bola juga **turun sejauh Y** saat memampatkan pegas, penurunan totalnya "
        "adalah (h + Y) — inilah bagian yang paling sering terlupakan.",
        "**Asal rumusnya.** Ambil acuan y = 0 di titik sentuh pegas. Keadaan awal: y = +h, v = 0. "
        "Keadaan akhir: y = −Y, v = 0 (berhenti sesaat). Maka mgh = −mgY + ½kY², yang disusun "
        "ulang menjadi mg(h + Y) = ½kY².",
        "**Batas keberlakuan.** Berlaku bila bola berhenti di titik terendah (mampatan maksimum). "
        "Jika yang ditanya kecepatan bola di suatu titik, gunakan bentuk energi lengkap "
        "½mv² + mgy + ½kx² = tetap.",
    ],
    lambang=[
        ("m", "massa bola", "kilogram (kg)"),
        ("h", "jarak jatuh **sebelum** menyentuh pegas", "meter (m)"),
        ("Y", "mampatan maksimum pegas", "meter (m)"),
        ("h + Y", "penurunan total bola dari titik lepas sampai titik terendah", "meter (m)"),
        ("k", "konstanta pegas yang dicari", "newton/meter (N/m)"),
        ("g", "percepatan gravitasi, 9,8 m/s²", "meter/sekon² (m/s²)"),
    ],
    satuan="[mg(h+Y)] = kg·(m/s²)·m = J dan [½kY²] = (N/m)(m²) = J ✓; hasil bagi untuk k "
           "bersatuan N/m ✓.",
    syarat="Bola dilepas dari diam, pegas tidak bermassa, tanpa gesekan udara. h diukur dari "
           "**ujung pegas**, bukan dari dasar pegas.",
    soal="Sebuah bola bermassa 2,60 kg jatuh sejauh 0,55 m sebelum menyentuh pegas vertikal, "
         "lalu memampatkan pegas sebesar 0,15 m. Tentukan konstanta pegas k.",
    isi=[
        ("p", "**Diketahui:** m = 2,60 kg; h = 0,55 m; Y = 0,15 m. **Ditanya:** k."),
        ("p", "**Langkah 1 — tentukan penurunan total bola:**"),
        ("f", "h + Y = 0,55 + 0,15 = 0,70 m"),
        ("p", "**Langkah 2 — tulis kekekalan energi (dua bentuk energi potensial):**"),
        ("f", "mg(h + Y) = ½k Y²"),
        ("p", "**Langkah 3 — susun untuk k:**"),
        ("f", "k = 2mg(h + Y)/Y²"),
        ("p", "**Langkah 4 — masukkan angka:**"),
        ("f", "k = 2(2,60)(9,8)(0,70)/(0,15)² = 35,67/0,0225"),
        ("f", "k ≈ 1.585 N/m ≈ 1,59 × 10³ N/m"),
    ],
    cek=[
        "**Cek energi:** bola kehilangan mg(h+Y) = 2,60 × 9,8 × 0,70 = 17,8 J; pegas menyimpan "
        "½(1585)(0,15²) = 17,8 J ✓",
        "**Satuan:** N/m ✓",
        "**Kewajaran:** k ≈ 1,6 kN/m setara pegas kursi; untuk mampatan hanya 15 cm diperlukan "
        "gaya maksimum kY ≈ 238 N (≈ 24 kg) — masuk akal untuk bola 2,6 kg yang jatuh 55 cm.",
        "**Bandingkan bila suku Y dilupakan:** k = 2mgh/Y² ≈ 1,25 × 10³ N/m, 21% terlalu kecil ✗",
    ],
    jawaban="k ≈ **1,59 × 10³ N/m** (1.585 N/m).",
    catatan="Kesalahan paling umum pada soal ini: menulis mgh = ½kY². Ingat bahwa bola masih "
            "turun sejauh Y setelah menyentuh pegas, sehingga energi potensial gravitasinya "
            "bertambah lagi sebesar mgY.",
),

dict(
    no=15, judul="Gesekan dan energi termal",
    rumus_inti="f~k~ = μ~k~ N ; W~f~ = −f~k~ d ; ΔE~th~ = f~k~ d",
    sumber="Cheatsheet Minggu 5, poin 15 · Subbab 5-4",
    rumus=[("f~k~ = μ~k~ N", None), ("W~f~ = −f~k~ d", None),
           ("ΔE~th~ = f~k~ d = −W~f~", None)],
    penjabaran=[
        "**Arti rumusnya.** Gaya gesek kinetik sebanding dengan gaya normal (besar tekanan benda "
        "pada permukaan) dengan faktor kesebandingan μ~k~. Gaya ini selalu melawan arah gerak, "
        "sehingga usahanya **selalu negatif**.",
        "**Ke mana energinya pergi.** Energi yang “hilang” dari gerak tidak lenyap: besarnya "
        "tepat sebesar f~k~d dan berubah menjadi **energi termal** (panas) pada kedua permukaan. "
        "Inilah isi pernyataan ΔE~th~ = f~k~d = −W~f~.",
        "**Nilai gaya normal.** Pada lantai datar tanpa gaya vertikal lain, N = mg. Pada bidang "
        "miring, N = mg cos α; pada lift, N = m(g ± a). Karena itu gaya normal tidak selalu "
        "sama dengan berat.",
    ],
    lambang=[
        ("f~k~", "besar gaya gesek kinetik", "newton (N)"),
        ("μ~k~", "koefisien gesek kinetik (bilangan tanpa satuan)", "—"),
        ("N", "gaya normal dari permukaan", "newton (N)"),
        ("d", "jarak tempuh selama bergesekan", "meter (m)"),
        ("W~f~", "usaha oleh gesek — selalu negatif", "joule (J)"),
        ("ΔE~th~", "energi termal yang timbul — selalu positif", "joule (J)"),
    ],
    satuan="[μ~k~N] = N ✓ (koefisien gesek tanpa satuan); [f~k~d] = N·m = J ✓. Karena itu "
           "W~f~ dan ΔE~th~ sama besar tetapi berlawanan tanda.",
    syarat="μ~k~ berlaku untuk benda yang **sudah bergerak**. Saat benda masih diam, yang "
           "bekerja adalah gesek statis (μ~s~), yang nilainya bisa lebih besar.",
    soal="Sebuah balok bermassa 3 kg dengan μ~k~ = 0,20 bergerak 5 m pada permukaan mendatar. "
         "Energi kinetik awalnya 40 J. Hitunglah gaya gesek, usaha gesek, energi termal, energi "
         "kinetik akhir, dan laju akhir balok.",
    isi=[
        ("p", "**Langkah 1 — gaya normal** (lantai datar, tanpa gaya vertikal lain):"),
        ("f", "N = mg = (3)(9,8) = 29,4 N"),
        ("p", "**Langkah 2 — gaya gesek:**"),
        ("f", "f~k~ = μ~k~ N = (0,20)(29,4) = 5,88 N"),
        ("p", "**Langkah 3 — usaha gesek** (gesekan berlawanan gerak, θ = 180°):"),
        ("f", "W~f~ = −f~k~ d = −(5,88)(5) = −29,4 J"),
        ("p", "**Langkah 4 — energi termal yang timbul:**"),
        ("f", "ΔE~th~ = +f~k~ d = +29,4 J"),
        ("p", "**Langkah 5 — energi kinetik akhir** dengan W = ΔK:"),
        ("f", "K~f~ = K~i~ + W~f~ = 40 − 29,4 = 10,6 J"),
        ("p", "**Langkah 6 — laju akhir:**"),
        ("f", "10,6 = ½(3)v~f~²   →   v~f~² = 7,07   →   v~f~ ≈ 2,66 m/s"),
    ],
    cek=[
        "**Kekekalan energi:** 40 J = 10,6 J (sisa kinetik) + 29,4 J (panas) ✓ — tidak ada energi "
        "yang lenyap.",
        "**Tanda:** W~f~ negatif, ΔE~th~ positif, besar keduanya sama ✓",
        "**Satuan:** N·m = J ✓",
        "**Batas:** bila K~i~ < 29,4 J, balok berhenti sebelum 5 m; jarak berhentinya "
        "d = K~i~/f~k~ = 40/5,88 ≈ 6,8 m > 5 m, jadi balok memang masih bergerak ✓",
    ],
    jawaban="f~k~ = **5,88 N**; W~f~ = **−29,4 J**; ΔE~th~ = **29,4 J**; K~f~ = **10,6 J**; "
            "v~f~ ≈ **2,66 m/s**.",
    catatan="Pada bidang miring, N = mg cos α sehingga f~k~ = μ~k~mg cos α — lebih kecil daripada "
            "di lantai datar. Memakai N = mg pada bidang miring adalah kesalahan yang sangat "
            "sering terjadi.",
),

dict(
    no=16, judul="Usaha oleh gaya nonkonservatif",
    rumus_inti="ΔE~mech~ = W~nc~",
    sumber="Cheatsheet Minggu 5, poin 16 · Subbab 5-5",
    rumus=[("E~f~ − E~i~ = W~nc~", None), ("ΔK + ΔU + ΔE~th~ = W~luar~", None)],
    penjabaran=[
        "**Arti rumusnya.** Bila ada gaya nonkonservatif (gesekan, dorongan, tarikan), energi "
        "mekanik **tidak** kekal. Perubahan energi mekanik persis sama dengan usaha gaya "
        "nonkonservatif itu.",
        "**Asal rumusnya.** Dari W~net~ = ΔK dengan W~net~ = W~konservatif~ + W~nc~ dan "
        "W~konservatif~ = −ΔU, diperoleh −ΔU + W~nc~ = ΔK, yaitu W~nc~ = ΔK + ΔU = ΔE~mech~. "
        "Jika W~nc~ = 0, kembalilah ke kekekalan energi mekanik.",
        "**Bentuk paling umum.** Bila energi termal ditulis tersendiri: "
        "ΔK + ΔU + ΔE~th~ = W~luar~. Untuk sistem terisolasi, ruas kanan nol sehingga "
        "energi total tetap.",
    ],
    lambang=[
        ("E~mech~", "energi mekanik, E = K + U", "joule (J)"),
        ("ΔE~mech~", "perubahan energi mekanik, E~f~ − E~i~", "joule (J)"),
        ("W~nc~", "usaha gaya nonkonservatif (gesek, dorong, tarik)", "joule (J)"),
        ("ΔE~th~", "energi termal akibat gesekan", "joule (J)"),
        ("W~luar~", "usaha oleh gaya luar pada sistem", "joule (J)"),
    ],
    satuan="Semua suku joule ✓; ΔE~mech~ dan W~nc~ sama satuannya sehingga pernyataan itu sah.",
    syarat="Gaya konservatif (gravitasi, pegas) tidak dimasukkan ke W~nc~ — usaha mereka sudah "
           "terwakili oleh ΔU.",
    soal="Energi mekanik suatu sistem turun dari 100 J menjadi 70 J karena gesekan. Berapa usaha "
         "oleh gaya nonkonservatif itu, dan ke mana energinya pergi?",
    isi=[
        ("p", "**Diketahui:** E~i~ = 100 J; E~f~ = 70 J. **Ditanya:** W~nc~."),
        ("p", "**Langkah 1 — pakai rumus:**"),
        ("f", "W~nc~ = E~f~ − E~i~ = 70 − 100 = −30 J"),
        ("p", "**Langkah 2 — tafsirkan tandanya.** Negatif berarti gaya itu **mengambil** energi "
              "dari sistem. Energi 30 J tidak hilang, melainkan berubah menjadi energi termal: "
              "ΔE~th~ = +30 J."),
    ],
    cek=[
        "**Kekekalan energi total:** 100 J = 70 J (mekanik) + 30 J (termal) ✓",
        "**Tanda:** gesekan selalu memberi W~nc~ negatif, sesuai hasil ✓",
        "**Satuan:** joule ✓",
        "**Kasus pembanding:** bila motor menarik sistem sehingga E naik dari 70 ke 100 J, maka "
        "W~nc~ = +30 J (energi masuk) ✓",
    ],
    jawaban="W~nc~ = **−30 J**; energi mekanik berkurang 30 J dan berubah menjadi "
            "**energi termal (panas)**.",
    catatan="W~nc~ negatif bukan berarti energi musnah — hanya berpindah bentuk. Inilah isi "
            "pernyataan “energi total kekal”.",
),
]
