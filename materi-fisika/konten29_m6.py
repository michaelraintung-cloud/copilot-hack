# -*- coding: utf-8 -*-
"""29 soal cheatsheet — MINGGU 6 (pusat massa, momentum, impuls, tumbukan)."""

ITEMS_M6 = [

dict(
    no=17, judul="Pusat massa pada satu dimensi",
    rumus_inti="x~CM~ = Σ m~i~ x~i~ / M",
    sumber="Cheatsheet Minggu 6, poin 17 · Subbab 6-1",
    rumus=[("x~CM~ = (m~1~x~1~ + m~2~x~2~ + …)/M", None), ("M = Σ m~i~ = m~1~ + m~2~ + …", None)],
    penjabaran=[
        "**Arti rumusnya.** Pusat massa adalah titik yang mewakili seluruh sistem. Rumus di atas "
        "adalah **rata-rata berbobot**: posisi setiap partikel ditimbang menurut massanya. "
        "Partikel yang lebih berat “menarik” titik itu lebih dekat kepadanya.",
        "**Mengapa penting.** Dengan mengenal pusat massa, sistem banyak benda dapat diperlakukan "
        "sebagai **satu partikel** bermassa M yang dipengaruhi gaya luar total (Soal 20).",
        "**Sifatnya.** Pusat massa selalu berada di antara partikel terletak paling kiri dan "
        "paling kanan — tidak pernah di luar rentang itu. Untuk massa yang sama besar, titiknya "
        "tepat di tengah.",
    ],
    lambang=[
        ("x~CM~", "koordinat pusat massa sistem", "meter (m)"),
        ("m~i~", "massa partikel ke-i", "kilogram (kg)"),
        ("x~i~", "posisi partikel ke-i terhadap titik asal", "meter (m)"),
        ("M", "massa total, M = Σm~i~", "kilogram (kg)"),
        ("Σ", "penjumlahan untuk semua partikel", "—"),
    ],
    satuan="[Σm~i~x~i~/M] = (kg·m)/kg = **m** ✓. Bila hasil Anda bukan meter, ada satuan massa "
           "atau panjang yang belum seragam (gram vs kg).",
    syarat="Titik asal boleh dipilih di mana saja; bila digeser, nilai x~CM~ ikut bergeser, tetapi "
           "letak fisisnya tetap sama.",
    soal="Massa m₁ = 2 kg berada di x₁ = 0 m dan m₂ = 3 kg berada di x₂ = 4 m. Tentukan letak "
         "pusat massa sistem.",
    isi=[
        ("p", "**Langkah 1 — massa total:**"),
        ("f", "M = 2 + 3 = 5 kg"),
        ("p", "**Langkah 2 — masukkan ke rumus pusat massa:**"),
        ("f", "x~CM~ = (m₁x₁ + m₂x₂)/M = (2·0 + 3·4)/5"),
        ("f", "x~CM~ = (0 + 12)/5 = 2,4 m"),
    ],
    cek=[
        "**Batas:** hasil 2,4 m berada di antara 0 m dan 4 m ✓",
        "**Kecenderungan:** lebih dekat ke m₂ (4 m) karena m₂ lebih berat ✓ (jarak ke m₂ = 1,6 m; "
        "jarak ke m₁ = 2,4 m)",
        "**Kasus pembanding:** bila kedua massa sama, x~CM~ = 2 m (tepat di tengah) — dan 2,4 m "
        "memang bergeser ke arah massa yang lebih besar ✓",
        "**Satuan:** m ✓",
    ],
    jawaban="x~CM~ = **2,4 m** dari titik asal.",
    catatan="Pusat massa tidak harus berada **di dalam** benda. Pada cincin, huruf “F”, atau "
            "gelang, pusat massanya justru di ruang kosong.",
),

dict(
    no=18, judul="Pusat massa pada dua dimensi",
    rumus_inti="x~CM~ = Σm~i~x~i~/M ; y~CM~ = Σm~i~y~i~/M",
    sumber="Cheatsheet Minggu 6, poin 18 · Subbab 6-1",
    rumus=[("x~CM~ = Σ m~i~ x~i~ / M", None), ("y~CM~ = Σ m~i~ y~i~ / M", None)],
    penjabaran=[
        "**Arti rumusnya.** Pada bidang, posisi punya dua koordinat. Rumus pusat massa dipakai "
        "**dua kali**: sekali untuk sumbu x dan sekali untuk sumbu y, dengan bentuk yang sama.",
        "**Sifat penting.** Kedua koordinat saling bebas — hasil x tidak mempengaruhi hasil y. "
        "Karena itu soal dua dimensi tidak lebih sulit, hanya lebih panjang.",
        "**Penyederhanaan.** Bila semua partikel terletak pada satu garis (misalnya semua y = 0), "
        "maka y~CM~ = 0 dan soal kembali menjadi satu dimensi (Soal 17).",
    ],
    lambang=[
        ("x~CM~, y~CM~", "koordinat pusat massa pada bidang xy", "meter (m)"),
        ("m~i~", "massa partikel ke-i", "kilogram (kg)"),
        ("x~i~, y~i~", "koordinat partikel ke-i", "meter (m)"),
        ("M", "massa total sistem", "kilogram (kg)"),
    ],
    satuan="[Σm~i~x~i~/M] = m dan [Σm~i~y~i~/M] = m ✓ — keduanya panjang.",
    syarat="Untuk tiga dimensi, tambahkan z~CM~ = Σm~i~z~i~/M dengan bentuk yang sama.",
    soal="Tiga massa: m₁ = 1 kg di (0, 0), m₂ = 2 kg di (3, 0), dan m₃ = 3 kg di (0, 2) m. "
         "Tentukan vektor posisi pusat massanya.",
    isi=[
        ("p", "**Langkah 1 — massa total:**"),
        ("f", "M = 1 + 2 + 3 = 6 kg"),
        ("p", "**Langkah 2 — koordinat x:**"),
        ("f", "x~CM~ = (1·0 + 2·3 + 3·0)/6 = 6/6 = 1 m"),
        ("p", "**Langkah 3 — koordinat y:**"),
        ("f", "y~CM~ = (1·0 + 2·0 + 3·2)/6 = 6/6 = 1 m"),
        ("p", "**Langkah 4 — tulis sebagai vektor:** r~CM~ = (1, 1) m."),
    ],
    cek=[
        "Pusat massa (1, 1) berada di dalam segitiga yang dibentuk ketiga massa ✓",
        "Lebih dekat ke m₃ = 3 kg di (0, 2) — massa terbesar ✓",
        "Massa total 6 kg lebih berat dari jumlah dua lainnya (3 kg), sehingga titiknya condong "
        "ke m₃ ✓",
        "Satuan: m ✓",
    ],
    jawaban="r~CM~ = **(1, 1) m**.",
    catatan="Untuk benda simetris (persegi, lingkaran, bola), pusat massa ada di titik pusat "
            "geometrinya. Memakai simetri lebih cepat daripada integral.",
),

dict(
    no=19, judul="Pusat massa benda kontinu (batang homogen)",
    rumus_inti="r~CM~ = (1/M) ∫ r dm",
    sumber="Cheatsheet Minggu 6, poin 19 · Subbab 6-1",
    rumus=[("x~CM~ = (1/M) ∫ x dm", None)],
    penjabaran=[
        "**Arti rumusnya.** Untuk benda yang massanya tersebar (bukan partikel terpisah), "
        "penjumlahan Σ diganti integral. Setiap potongan kecil bermassa dm di posisi x "
        "disumbangkan, lalu dibagi massa total.",
        "**Cara praktisnya.** Nyatakan dm dalam bentuk dx. Untuk batang homogen dengan kerapatan "
        "λ = M/L, berlaku dm = (M/L)dx. Massa total M lalu **terhapus**, sehingga yang tersisa "
        "hanyalah perhitungan geometri.",
        "**Hasil yang harus diingat.** Batang homogen → x~CM~ = L/2 (di tengah). Pelat persegi "
        "homogen → di titik pusatnya. Bola homogen → di pusatnya.",
    ],
    lambang=[
        ("r~CM~", "vektor posisi pusat massa benda", "meter (m)"),
        ("dm", "elemen massa sangat kecil", "kilogram (kg)"),
        ("x", "posisi elemen massa itu", "meter (m)"),
        ("M", "massa total benda", "kilogram (kg)"),
        ("λ = M/L", "kerapatan massa linier batang", "kilogram/meter (kg/m)"),
    ],
    satuan="[(1/M)∫x dm] = (1/kg)(m·kg) = **m** ✓.",
    syarat="Berlaku untuk benda dengan kerapatan seragam. Bila kerapatan berubah (misalnya batang "
           "menebal di satu ujung), λ tidak konstan dan harus dimasukkan ke dalam integral.",
    soal="Sebuah batang homogen panjangnya L = 4 m. Tentukan letak pusat massanya diukur dari "
         "salah satu ujung.",
    isi=[
        ("p", "**Langkah 1 — nyatakan elemen massa.** Ambil ujung batang sebagai x = 0 dan "
              "kerapatan λ = M/L, sehingga:"),
        ("f", "dm = (M/L) dx"),
        ("p", "**Langkah 2 — masukkan ke rumus pusat massa:**"),
        ("f", "x~CM~ = (1/M) ∫ x (M/L) dx = (1/L) ∫ x dx, dari x = 0 sampai L"),
        ("p", "**Langkah 3 — integralkan:** antiturunan x adalah ½x², sehingga"),
        ("f", "x~CM~ = (1/L)[½x²] = (1/L)(½L²) = L/2"),
        ("p", "**Langkah 4 — masukkan angka:**"),
        ("f", "x~CM~ = 4/2 = 2 m"),
    ],
    cek=[
        "Hasil L/2 sesuai sifat simetri batang homogen ✓",
        "**Cek angka:** 2 m berada tepat di tengah batang 4 m ✓",
        "**Satuan:** m ✓",
        "**Bandingkan:** bila batang dua kali lebih panjang (8 m), x~CM~ = 4 m — tetap di tengah, "
        "menunjukkan hasilnya bergantung pada L secara proporsional ✓",
    ],
    jawaban="x~CM~ = **2 m** dari ujung batang (tepat di tengah).",
    catatan="Untuk pelat atau benda berdimensi dua/tiga, ganti dm dengan (M/A)dA atau (M/V)dV; "
            "polanya sama — massa total selalu terhapus.",
),

dict(
    no=20, judul="Hukum II Newton untuk sistem partikel",
    rumus_inti="F~ext,net~ = M a~CM~",
    sumber="Cheatsheet Minggu 6, poin 20 · Subbab 6-2",
    rumus=[("F~ext,net~ = M a~CM~", None)],
    penjabaran=[
        "**Arti rumusnya.** Pusat massa sebuah sistem bergerak persis seperti satu partikel "
        "bermassa M yang ditarik oleh **resultan gaya luar**. Gaya-gaya di dalam sistem tidak "
        "mengubah gerak pusat massa.",
        "**Mengapa gaya dalam hilang.** Gaya antarpartikel selalu berpasangan sama besar dan "
        "berlawanan arah (hukum III Newton), sehingga jumlahnya nol. Contohnya: ledakan, "
        "tabrakan antarpenumpang dalam mobil, atau gaya otot internal tubuh.",
        "**Asal rumusnya.** Dari definisi pusat massa (Soal 17), kecepatan pusat massa "
        "v~CM~ = P/M (Soal 21). Turunannya terhadap waktu memberi a~CM~ = F~ext,net~/M.",
    ],
    lambang=[
        ("F~ext,net~", "jumlah vektor semua gaya **luar** pada sistem", "newton (N)"),
        ("M", "massa total sistem", "kilogram (kg)"),
        ("a~CM~", "percepatan pusat massa", "meter/sekon² (m/s²)"),
    ],
    satuan="[Ma] = kg·m/s² = **N** ✓, sama dengan satuan gaya — rumus konsisten.",
    syarat="Hanya gaya **luar** yang boleh dimasukkan. Bila F~ext,net~ = 0, maka a~CM~ = 0: pusat "
           "massa diam atau bergerak lurus dengan laju tetap.",
    soal="Sebuah sistem bermassa total 5 kg menerima gaya eksternal neto 15 N ke kanan. Tentukan "
         "percepatan pusat massanya.",
    isi=[
        ("p", "**Diketahui:** M = 5 kg; F~ext,net~ = 15 N (ke kanan). **Ditanya:** a~CM~."),
        ("p", "**Langkah 1 — susun rumus untuk a~CM~:**"),
        ("f", "a~CM~ = F~ext,net~/M"),
        ("p", "**Langkah 2 — masukkan angka:**"),
        ("f", "a~CM~ = 15/5 = 3 m/s²"),
    ],
    cek=[
        "**Satuan:** N/kg = (kg·m/s²)/kg = m/s² ✓",
        "**Arah:** searah gaya luar neto, yaitu ke kanan ✓",
        "**Kewajaran:** gaya 15 N pada 5 kg memang memberi percepatan 3 m/s² (kira-kira "
        "sepertiga g) ✓",
        "**Kasus khusus:** bila gaya luar nol, a~CM~ = 0 walaupun bagian-bagian sistem bergerak "
        "ke segala arah (misalnya ledakan) ✓",
    ],
    jawaban="a~CM~ = **3 m/s² ke kanan**.",
    catatan="Inilah alasan orang tidak dapat “mengangkat diri sendiri dengan menarik rambutnya”: "
            "gaya itu gaya dalam, sehingga pusat massa tidak berubah geraknya.",
),

dict(
    no=21, judul="Momentum total dan kecepatan pusat massa",
    rumus_inti="P = Σ m~i~v~i~ = M v~CM~",
    sumber="Cheatsheet Minggu 6, poin 21 · Subbab 6-3",
    rumus=[("p = m v", None), ("P = Σ m~i~ v~i~ = M v~CM~   →   v~CM~ = P/M", None)],
    penjabaran=[
        "**Arti rumusnya.** Momentum sebuah partikel adalah massa dikali kecepatan. Untuk sistem, "
        "momentum total adalah jumlah **vektor** momentum semua partikel, dan jumlah itu sama "
        "dengan massa total dikali kecepatan pusat massa.",
        "**Sifat vektor.** Momentum punya arah. Benda yang bergerak ke kiri menyumbang momentum "
        "negatif. Karena itu menjumlahkan **besar** momentum tanpa memperhatikan arah adalah "
        "kesalahan mendasar.",
        "**Hubungan dengan pusat massa.** Persamaan P = M v~CM~ menyatakan bahwa seluruh momentum "
        "sistem dapat “diwakili” oleh pusat massanya. Inilah jembatan antara Bab 6-1 (pusat "
        "massa) dan Bab 6-3 (momentum).",
    ],
    lambang=[
        ("p", "momentum satu partikel (vektor)", "kg·m/s = N·s"),
        ("P", "momentum total sistem", "kg·m/s"),
        ("m~i~, v~i~", "massa dan kecepatan partikel ke-i (bertanda)", "kg; m/s"),
        ("v~CM~", "kecepatan pusat massa", "meter/sekon (m/s)"),
        ("M", "massa total sistem", "kilogram (kg)"),
    ],
    satuan="[mv] = kg·m/s = (kg·m/s²)·s = N·s ✓. Kedua satuan itu setara, sehingga momentum dan "
           "impuls dapat langsung dijumlahkan.",
    syarat="Kecepatan harus diberi tanda sesuai arah. Bila gerak terjadi pada bidang, momentum "
           "diuraikan per sumbu terlebih dahulu.",
    soal="Sebuah benda 2 kg bergerak +3 m/s, dan benda 1 kg bergerak −4 m/s pada garis yang sama. "
         "Hitunglah momentum total dan kecepatan pusat massa sistem.",
    isi=[
        ("p", "**Langkah 1 — momentum total** (jumlahkan dengan tandanya):"),
        ("f", "P = m₁v₁ + m₂v₂ = (2)(+3) + (1)(−4)"),
        ("f", "P = 6 − 4 = +2 kg·m/s"),
        ("p", "**Langkah 2 — massa total:**"),
        ("f", "M = 2 + 1 = 3 kg"),
        ("p", "**Langkah 3 — kecepatan pusat massa:**"),
        ("f", "v~CM~ = P/M = 2/3 ≈ +0,67 m/s"),
    ],
    cek=[
        "**Tanda:** hasil positif berarti pusat massa bergerak ke arah benda pertama (ke kanan) ✓",
        "**Kewajaran:** benda 2 kg bergerak +3 m/s “mengalahkan” benda 1 kg yang bergerak "
        "−4 m/s, sehingga arah gabungan ke kanan ✓",
        "**Cek lain:** bila kedua benda menempel, momentum tetap 2 kg·m/s; dengan massa 3 kg "
        "lajunya 0,67 m/s — konsisten ✓",
        "**Satuan:** kg·m/s ✓",
    ],
    jawaban="P = **+2 kg·m/s** dan v~CM~ ≈ **+0,67 m/s** (ke kanan).",
    catatan="Bila kedua benda menempel, kecepatan akhirnya persis v~CM~. Karena itu soal tumbukan "
            "sempurna tidak elastis dapat diselesaikan sebagai “cari v~CM~”.",
),

dict(
    no=22, judul="Impuls dan gaya rata-rata saat bola memantul",
    rumus_inti="J = Δp = m(v~f~ − v~i~) ; F~avg~ = J/Δt",
    sumber="Cheatsheet Minggu 6, poin 22 · Subbab 6-4",
    rumus=[("J = Δp = m(v~f~ − v~i~)", None), ("F~avg~ = J/Δt", None)],
    penjabaran=[
        "**Arti rumusnya.** Impuls adalah “jumlah gaya selama waktu” yang diberikan pada benda, "
        "dan besarnya sama dengan perubahan momentum benda. Gaya besar dalam waktu singkat dapat "
        "memberi impuls yang sama dengan gaya kecil dalam waktu lama.",
        "**Asal rumusnya.** Dari hukum II Newton F = ma = m(dv/dt), kalikan kedua ruas dengan dt "
        "lalu integralkan: ∫F dt = ∫m dv = m(v~f~ − v~i~). Ruas kiri adalah impuls, ruas kanan "
        "perubahan momentum.",
        "**Kasus pemantulan.** Bila bola datang dengan +20 m/s lalu memantul dengan −10 m/s, "
        "perubahan kecepatannya adalah (−10) − (+20) = **−30 m/s** — bukan 10 m/s. Arah berbalik, "
        "dan itu menambah besar impuls.",
    ],
    lambang=[
        ("J", "impuls", "N·s = kg·m/s"),
        ("Δp", "perubahan momentum, p~f~ − p~i~", "kg·m/s"),
        ("m", "massa bola", "kilogram (kg)"),
        ("v~i~, v~f~", "kecepatan **bervektor** sebelum/sesudah (tanda diikutkan)", "meter/sekon (m/s)"),
        ("F~avg~", "gaya rata-rata selama kontak", "newton (N)"),
        ("Δt", "lama kontak", "sekon (s)"),
    ],
    satuan="[mΔv] = kg·m/s = N·s ✓; [J/Δt] = (N·s)/s = N ✓ — jadi hasil bagi itu memang gaya.",
    syarat="Tetapkan arah positif lebih dahulu. Untuk benda yang memantul, kecepatan akhir "
           "**wajib** bertanda berlawanan dengan kecepatan datang.",
    soal="Sebuah bola bermassa 0,15 kg berubah kecepatannya dari +20 m/s menjadi −10 m/s dalam "
         "waktu 0,015 s. Hitunglah impuls yang diterima bola dan gaya rata-rata padanya.",
    isi=[
        ("p", "**Diketahui:** m = 0,15 kg; v~i~ = +20 m/s; v~f~ = −10 m/s; Δt = 0,015 s."),
        ("p", "**Langkah 1 — hitung perubahan kecepatan** (memperhatikan tanda):"),
        ("f", "v~f~ − v~i~ = (−10) − (+20) = −30 m/s"),
        ("p", "**Langkah 2 — impuls:**"),
        ("f", "J = m(v~f~ − v~i~) = (0,15)(−30) = −4,5 N·s"),
        ("p", "**Langkah 3 — gaya rata-rata:**"),
        ("f", "F~avg~ = J/Δt = −4,5/0,015 = −300 N"),
    ],
    cek=[
        "**Tanda:** negatif berarti impuls dan gaya berarah berlawanan dengan arah datang bola — "
        "memang dinding mendorongnya kembali ✓",
        "**Satuan:** N·s untuk impuls dan N untuk gaya ✓",
        "**Kewajaran:** gaya 300 N selama 15 ms memang wajar untuk tumbukan bola; bila waktunya "
        "15 s, gaya hanya 0,3 N.",
        "**Uji kesalahan umum:** bila dipakai Δv = 10 m/s, hasilnya J = −1,5 N·s dan F = −100 N — "
        "salah, karena arah bola berbalik ✗",
    ],
    jawaban="J = **−4,5 N·s**; F~avg~ = **−300 N** (berlawanan arah datang bola).",
    catatan="Helm, bantalan, dan *airbag* bekerja dengan **memperpanjang Δt**. Untuk perubahan "
            "momentum yang sama, gaya rata-rata mengecil sehingga cedera berkurang.",
),

dict(
    no=23, judul="Impuls oleh gaya konstan",
    rumus_inti="J = F Δt = Δp",
    sumber="Cheatsheet Minggu 6, poin 23 · Subbab 6-4",
    rumus=[("J = F Δt", None), ("J = Δp = m(v~f~ − v~i~)", None)],
    penjabaran=[
        "**Arti rumusnya.** Bila gaya tetap, impuls cukup dihitung sebagai gaya dikali lama "
        "bekerjanya. Hasilnya sama dengan perubahan momentum benda.",
        "**Dua arah pemakaian.** (i) Bila F dan Δt diketahui → cari J, lalu cari perubahan "
        "kecepatan. (ii) Bila perubahan momentum diketahui → J diketahui, lalu F = J/Δt.",
        "**Hubungan dengan gaya rata-rata.** Untuk gaya yang berubah-ubah, F~avg~ = J/Δt adalah "
        "gaya tetap yang memberi impuls sama. Jadi rumus ini juga berlaku sebagai definisi gaya "
        "rata-rata.",
    ],
    lambang=[
        ("J", "impuls", "N·s"),
        ("F", "gaya tetap selama Δt", "newton (N)"),
        ("Δt", "selang waktu gaya bekerja", "sekon (s)"),
        ("Δp", "perubahan momentum", "kg·m/s"),
        ("m", "massa benda", "kilogram (kg)"),
        ("v~i~, v~f~", "kecepatan sebelum dan sesudah", "meter/sekon (m/s)"),
    ],
    satuan="[FΔt] = N·s ✓, sama dengan satuan perubahan momentum kg·m/s ✓.",
    syarat="Gaya harus **tetap**. Bila gaya berubah, gunakan J = ∫F dt atau luas grafik F–t "
           "(Soal 24).",
    soal="Sebuah gaya 50 N bekerja selama 0,20 s pada benda 0,50 kg yang mula-mula diam. "
         "Hitunglah impuls yang diberikan dan laju akhir benda.",
    isi=[
        ("p", "**Langkah 1 — impuls:**"),
        ("f", "J = F Δt = (50)(0,20) = 10 N·s"),
        ("p", "**Langkah 2 — dari impuls ke laju akhir** (v~i~ = 0):"),
        ("f", "J = m(v~f~ − v~i~)   →   10 = 0,50 v~f~"),
        ("f", "v~f~ = 10/0,50 = 20 m/s"),
    ],
    cek=[
        "**Cara kedua:** a = F/m = 50/0,50 = 100 m/s², lalu v = at = 100 × 0,20 = 20 m/s ✓",
        "**Satuan:** N·s dan m/s ✓",
        "**Kewajaran:** gaya 50 N pada benda ringan 0,5 kg memang memberi percepatan besar "
        "(≈10g) selama 0,2 s ✓",
        "**Arah:** laju akhir searah gaya ✓",
    ],
    jawaban="J = **10 N·s**; v~f~ = **20 m/s** searah gaya.",
    catatan="Impuls adalah vektor: bila gayanya berarah ke kiri, J dan Δp bernilai negatif. "
            "Perhatikan juga bahwa 1 N·s = 1 kg·m/s.",
),

dict(
    no=24, judul="Impuls dari gaya yang berubah terhadap waktu",
    rumus_inti="J = ∫F dt = luas grafik F–t",
    sumber="Cheatsheet Minggu 6, poin 24 · Subbab 6-4",
    rumus=[("J = ∫ F dt  =  luas bertanda di bawah kurva F–t", None)],
    penjabaran=[
        "**Arti rumusnya.** Bila gaya tidak tetap, impuls dihitung dengan integral, yang secara "
        "grafis sama dengan **luas daerah** di bawah kurva gaya terhadap waktu.",
        "**Asal rumusnya.** Sama seperti usaha: perjalanan waktu dipecah menjadi potongan kecil "
        "dt; pada potongan itu gaya boleh dianggap tetap sehingga impuls potongannya F dt. Jumlah "
        "seluruh potongan adalah ∫F dt.",
        "**Perhatikan satuannya.** Sumbu vertikal harus gaya (N) dan sumbu horizontal harus waktu "
        "(s), sehingga luasnya N·s. Bandingkan dengan grafik F–x yang luasnya joule — dua grafik "
        "ini mirip bentuknya tetapi berbeda arti.",
    ],
    lambang=[
        ("J", "impuls total", "N·s"),
        ("F", "gaya yang bergantung waktu", "newton (N)"),
        ("dt", "selang waktu sangat kecil", "sekon (s)"),
        ("luas kurva", "luas daerah antara kurva F dan sumbu t", "N·s"),
    ],
    satuan="[∫F dt] = N × s = **N·s** ✓, sama dengan kg·m/s.",
    syarat="Kurva harus dapat dihitung luasnya (biasanya garis lurus). Daerah di bawah sumbu t "
           "memberi impuls negatif.",
    soal="Sebuah gaya naik linier dari 0 sampai 20 N selama 0,50 s, lalu berhenti. Gaya itu "
         "bekerja pada benda 0,25 kg yang mula-mula diam. Hitunglah impuls dan laju akhir benda.",
    isi=[
        ("p", "**Langkah 1 — hitung luas segitiga pada grafik F–t:**"),
        ("f", "J = ½ × alas × tinggi = ½ × (0,50 s)(20 N) = 5 N·s"),
        ("p", "**Langkah 2 — dari impuls ke laju:**"),
        ("f", "J = Δp = m v~f~   →   5 = (0,25)v~f~"),
        ("f", "v~f~ = 5/0,25 = 20 m/s"),
    ],
    cek=[
        "**Gaya rata-rata:** F~avg~ = J/Δt = 5/0,50 = 10 N — tepat setengah gaya maksimum, ciri "
        "profil segitiga ✓",
        "**Cek gaya tetap setara:** 10 N × 0,50 s = 5 N·s ✓",
        "**Satuan:** N·s dan m/s ✓",
        "**Kewajaran:** benda 0,25 kg menerima impuls 5 N·s → 20 m/s; energi kinetiknya 50 J, "
        "cukup besar tetapi wajar untuk gaya 20 N yang bekerja 0,5 s ✓",
    ],
    jawaban="J = **5 N·s**; v~f~ = **20 m/s** searah gaya.",
    catatan="Rumus luas yang sering dipakai: segitiga ½at, persegi panjang p×l, trapesium "
            "½(a + b)t. Pastikan waktu dalam sekon, bukan milisekon.",
),

dict(
    no=25, judul="Membedakan tumbukan elastis dan tidak elastis",
    rumus_inti="Momentum selalu kekal ; energi kinetik hanya bila elastis",
    sumber="Cheatsheet Minggu 6, poin 25 · Subbab 6-6",
    rumus=[("Σ m v (sebelum) = Σ m v (sesudah)", None),
           ("Elastis: K~f~ = K~i~   ·   Tidak elastis: K~f~ < K~i~", None)],
    penjabaran=[
        "**Dua besaran, dua aturan berbeda.** Pada setiap tumbukan, **momentum selalu kekal** "
        "(selama gaya luar dapat diabaikan). Tetapi **energi kinetik tidak selalu kekal** — hanya "
        "pada tumbukan elastis.",
        "**Mengapa momentum selalu kekal.** Selama tumbukan, gaya yang bekerja adalah gaya "
        "antar-benda (gaya dalam) yang berpasangan sama besar dan berlawanan arah, sehingga "
        "jumlahnya nol. Tidak ada impuls luar, maka momentum total tidak berubah.",
        "**Ke mana energi kinetik pergi.** Pada tumbukan tidak elastis, sebagian energi kinetik "
        "berubah menjadi panas, bunyi, dan deformasi bentuk benda. Semakin “lengket” tumbukannya, "
        "semakin besar energi yang berubah.",
    ],
    lambang=[
        ("p", "momentum, p = mv", "kg·m/s"),
        ("K", "energi kinetik total, K = Σ½mv²", "joule (J)"),
        ("elastis", "benda memantul sempurna; K kekal", "—"),
        ("tidak elastis", "K berkurang; sebagian menjadi panas/deformasi", "—"),
        ("sempurna tidak elastis", "benda menyatu; kehilangan K paling besar", "—"),
    ],
    satuan="Momentum kg·m/s dan energi kinetik J — dua besaran berbeda, jadi **tidak boleh** "
           "disamakan atau dijumlahkan.",
    syarat="Pemeriksaan kekekalan momentum hanya sah bila gaya luar selama tumbukan (misalnya "
           "gesekan lantai) dapat diabaikan karena waktunya sangat singkat.",
    soal="Momentum suatu sistem kekal, sedangkan energi kinetiknya turun dari 20 J menjadi 12 J. "
         "Termasuk jenis tumbukan apa, dan ke mana energi 8 J itu pergi?",
    isi=[
        ("p", "**Langkah 1 — periksa momentum.** Momentum kekal → syarat sistem terisolasi "
              "terpenuhi, jadi tidak ada impuls luar yang berarti."),
        ("p", "**Langkah 2 — periksa energi kinetik:**"),
        ("f", "ΔK = K~f~ − K~i~ = 12 − 20 = −8 J"),
        ("p", "**Langkah 3 — simpulkan.** Karena ΔK ≠ 0 (berkurang), tumbukan **tidak elastis**. "
              "Karena tidak disebutkan bendanya menyatu, belum tentu sempurna tidak elastis."),
    ],
    cek=[
        "ΔK negatif → tidak elastis ✓ (bila ΔK = 0, berarti elastis)",
        "Momentum kekal tetapi energi tidak → ciri khas tumbukan tidak elastis ✓",
        "**Kekekalan energi total:** 20 J = 12 J (kinetik) + 8 J (panas/bunyi/deformasi) ✓",
        "Bila benda disebut menyatu, klasifikasinya menjadi sempurna tidak elastis — kehilangan "
        "energi paling besar untuk massa dan laju yang sama ✓",
    ],
    jawaban="Tumbukan **tidak elastis**; 8 J berubah menjadi panas, bunyi, dan deformasi.",
    catatan="Pada bandul balistik (peluru menancap di balok), momentum kekal tetapi energi "
            "kinetik **tidak**. Menyamakan energi kinetik sebelum dan sesudah adalah kesalahan "
            "yang sangat sering terjadi.",
),

dict(
    no=26, judul="Tumbukan sempurna tidak elastis (benda menyatu)",
    rumus_inti="v~f~ = (m~1~v~1~ + m~2~v~2~)/(m~1~ + m~2~)",
    sumber="Cheatsheet Minggu 6, poin 26 · Subbab 6-7",
    rumus=[("m~1~v~1i~ + m~2~v~2i~ = (m~1~ + m~2~)v~f~", None),
           ("v~f~ = (m~1~v~1i~ + m~2~v~2i~)/(m~1~ + m~2~)", None)],
    penjabaran=[
        "**Arti rumusnya.** Bila dua benda menempel setelah tumbukan, keduanya bergerak dengan "
        "satu kecepatan bersama. Kecepatan itu adalah **rata-rata kecepatan awal yang ditimbang "
        "massa**.",
        "**Asal rumusnya.** Hanya momentum yang dipakai: momentum sebelum = momentum sesudah. "
        "Karena setelah tumbukan massanya menjadi (m₁ + m₂), persamaan langsung dapat disusun "
        "untuk v~f~.",
        "**Energi kinetik selalu berkurang.** Karena benda bergerak bersama, tidak ada gerak "
        "relatif yang tersisa; selisih energi menjadi panas dan deformasi. Kehilangan ini "
        "**maksimum** di antara semua jenis tumbukan dengan massa dan laju awal yang sama.",
    ],
    lambang=[
        ("m~1~, m~2~", "massa benda pertama dan kedua", "kilogram (kg)"),
        ("v~1i~, v~2i~", "kecepatan sebelum tumbukan (bertanda)", "meter/sekon (m/s)"),
        ("v~f~", "kecepatan bersama setelah tumbukan", "meter/sekon (m/s)"),
        ("K", "energi kinetik total", "joule (J)"),
    ],
    satuan="[(kg·m/s)/kg] = **m/s** ✓ untuk v~f~; jadi rumus ini konsisten.",
    syarat="Berlaku hanya bila benda **menyatu/menempel**. Tidak boleh dipakai untuk tumbukan "
           "yang benda-bendanya terpisah kembali.",
    soal="Benda m₁ = 1 kg bergerak +6 m/s menumbuk benda m₂ = 2 kg yang diam, lalu keduanya "
         "menyatu. Hitunglah kecepatan bersama dan energi kinetik yang hilang.",
    isi=[
        ("p", "**Langkah 1 — kekekalan momentum:**"),
        ("f", "m₁v₁ + m₂v₂ = (m₁ + m₂)v~f~"),
        ("f", "(1)(6) + (2)(0) = (1 + 2)v~f~   →   6 = 3v~f~"),
        ("f", "v~f~ = +2 m/s"),
        ("p", "**Langkah 2 — energi kinetik sebelum dan sesudah:**"),
        ("f", "K~i~ = ½(1)(6²) = 18 J"),
        ("f", "K~f~ = ½(3)(2²) = 6 J"),
        ("p", "**Langkah 3 — energi yang hilang:**"),
        ("f", "ΔK = K~f~ − K~i~ = 6 − 18 = −12 J"),
    ],
    cek=[
        "**Momentum:** sebelum 6 kg·m/s; sesudah 3 × 2 = 6 kg·m/s ✓ kekal",
        "**Energi:** 18 J → 6 J, hilang 12 J ✓ (tidak kekal, sesuai jenis tumbukannya)",
        "**Batas:** v~f~ = 2 m/s berada di antara 0 dan 6 m/s, lebih dekat ke 0 karena massa "
        "gabungan lebih berat ✓",
        "**Kewajaran fraksi hilang:** ⅔ energi awal hilang — lazim untuk tumbukan menyatu dengan "
        "massa 1 : 2 ✓",
    ],
    jawaban="v~f~ = **+2 m/s**; energi kinetik berkurang **12 J** (18 J → 6 J).",
    catatan="Perhatikan bahwa kecepatan bersama selalu berada **di antara** kecepatan awal yang "
            "paling kecil dan paling besar — bila hasil Anda di luar rentang itu, pasti ada "
            "kesalahan tanda.",
),

dict(
    no=27, judul="Tumbukan menyatu dengan arah berlawanan",
    rumus_inti="P~sebelum~ = P~sesudah~",
    sumber="Cheatsheet Minggu 6, poin 27 · Subbab 6-7",
    rumus=[("m~1~v~1~ + m~2~v~2~ = (m~1~ + m~2~)v~f~", None)],
    penjabaran=[
        "**Arti rumusnya.** Sama seperti Soal 26, tetapi kedua benda bergerak **berlawanan arah**. "
        "Karena itu salah satu kecepatan harus bertanda negatif.",
        "**Arah akhir.** Arah gerak gabungan ditentukan oleh siapa yang momentumnya lebih besar — "
        "**bukan** otomatis oleh benda yang lebih berat. Benda berat yang bergerak lambat bisa "
        "kalah momentum dari benda ringan yang cepat.",
        "**Energi yang hilang lebih besar.** Ketika kedua benda berlawanan arah, keduanya harus "
        "saling “menghentikan” lebih dahulu, sehingga energi kinetik yang berubah menjadi panas "
        "biasanya jauh lebih besar daripada kasus searah.",
    ],
    lambang=[
        ("v~1~, v~2~", "kecepatan awal, bertanda (+ ke kanan, − ke kiri)", "meter/sekon (m/s)"),
        ("m~1~, m~2~", "massa masing-masing benda", "kilogram (kg)"),
        ("v~f~", "kecepatan bersama setelah menempel", "meter/sekon (m/s)"),
        ("K", "energi kinetik total", "joule (J)"),
    ],
    satuan="[kg·m/s ÷ kg] = m/s ✓. Tanda hasil menunjukkan arah gerak akhir.",
    syarat="Tetapkan arah positif sebelum memasukkan angka, dan tulis tanda minus pada kecepatan "
           "yang berlawanan arah.",
    soal="Benda m₁ = 1 kg dengan v₁ = +4 m/s dan benda m₂ = 3 kg dengan v₂ = −2 m/s bergerak "
         "saling mendekat lalu menyatu. Hitunglah kecepatan akhir dan energi kinetik yang hilang.",
    isi=[
        ("p", "**Langkah 1 — momentum sebelum** (tanda diikutkan):"),
        ("f", "P~i~ = (1)(+4) + (3)(−2) = 4 − 6 = −2 kg·m/s"),
        ("p", "**Langkah 2 — kecepatan bersama:**"),
        ("f", "v~f~ = P~i~/(m₁ + m₂) = −2/4 = −0,5 m/s"),
        ("p", "Tanda negatif berarti gabungan bergerak **ke kiri**."),
        ("p", "**Langkah 3 — energi kinetik awal:**"),
        ("f", "K~i~ = ½(1)(4²) + ½(3)(2²) = 8 + 6 = 14 J"),
        ("p", "**Langkah 4 — energi kinetik akhir:**"),
        ("f", "K~f~ = ½(4)(0,5²) = 0,5 J"),
        ("p", "**Langkah 5 — energi yang hilang:**"),
        ("f", "ΔK = 0,5 − 14 = −13,5 J"),
    ],
    cek=[
        "**Momentum:** sesudah = 4 × (−0,5) = −2 kg·m/s → sama dengan sebelum ✓",
        "**Arah:** ke kiri, karena benda 3 kg yang bergerak ke kiri menyumbang momentum lebih "
        "besar (−6) daripada benda 1 kg (−4) ✓",
        "**Energi:** 14 J → 0,5 J, hilang 13,5 J (96%) ✓ — wajar karena keduanya hampir saling "
        "menghentikan",
        "**Batas:** v~f~ = −0,5 m/s berada di antara −2 dan +4 m/s ✓",
    ],
    jawaban="v~f~ = **−0,5 m/s** (ke kiri); energi kinetik turun **13,5 J** (14 J → 0,5 J).",
    catatan="Hati-hati: benda yang **lebih berat** belum tentu menentukan arah. Yang menentukan "
            "adalah hasil kali massa × kecepatan (momentum).",
),

dict(
    no=28, judul="Tumbukan elastis dengan massa sama",
    rumus_inti="Untuk m~1~ = m~2~: benda bertukar kecepatan",
    sumber="Cheatsheet Minggu 6, poin 28 · Subbab 6-8",
    rumus=[("v~1f~ = [(m~1~ − m~2~)/(m~1~ + m~2~)]v~1i~ + …", None),
           ("Untuk m~1~ = m~2~:  v~1f~ = v~2i~  dan  v~2f~ = v~1i~", None)],
    penjabaran=[
        "**Arti rumusnya.** Pada tumbukan elastis satu dimensi dengan massa sama, kedua benda "
        "**bertukar kecepatan**. Benda yang bergerak berhenti, dan benda yang diam bergerak "
        "dengan laju yang tadi dimiliki benda pertama.",
        "**Asal rumusnya.** Dua persamaan berlaku: kekekalan momentum "
        "mv₁ + mv₂ = mv₁f + mv₂f (m terhapus → v₁ + v₂ = v₁f + v₂f) dan kekekalan energi kinetik "
        "(m terhapus → v₁² + v₂² = v₁f² + v₂f²). Penyelesaian kedua persamaan itu menghasilkan "
        "v₁f = v₂ dan v₂f = v₁.",
        "**Bentuk umum untuk target diam.** v₁f = [(m₁ − m₂)/(m₁ + m₂)]v₁ dan "
        "v₂f = [2m₁/(m₁ + m₂)]v₁. Bila m₁ = m₂, faktor pertama menjadi 0 dan faktor kedua menjadi "
        "1 — persis seperti kesimpulan di atas.",
    ],
    lambang=[
        ("m~1~, m~2~", "massa benda pertama dan kedua (sama besar)", "kilogram (kg)"),
        ("v~1i~, v~2i~", "kecepatan sebelum tumbukan", "meter/sekon (m/s)"),
        ("v~1f~, v~2f~", "kecepatan setelah tumbukan", "meter/sekon (m/s)"),
        ("K", "energi kinetik total — kekal pada tumbukan elastis", "joule (J)"),
    ],
    satuan="Semua suku pada rumus berbentuk [(kg/kg)·(m/s)] = m/s ✓.",
    syarat="Tumbukan harus **elastis** (K kekal) dan **satu dimensi** (lurus, tanpa putaran). Bila "
           "tumbukan miring, sudut antara kedua bola setelah tumbukan 90°.",
    soal="Dua benda masing-masing bermassa 1 kg. Benda pertama bergerak +4 m/s dan benda kedua "
         "diam. Jika tumbukannya elastis, tentukan kecepatan kedua benda setelah tumbukan.",
    isi=[
        ("p", "**Langkah 1 — tulis kekekalan momentum:**"),
        ("f", "m v₁ + m v₂ = m v₁f + m v₂f   →   4 + 0 = v₁f + v₂f"),
        ("p", "**Langkah 2 — tulis kekekalan energi kinetik** (bentuk khusus elastis 1D):"),
        ("f", "v₁ − v₂ = v₂f − v₁f   →   4 − 0 = v₂f − v₁f"),
        ("p", "**Langkah 3 — selesaikan kedua persamaan.** Dari persamaan kedua v₂f = v₁f + 4; "
              "masukkan ke persamaan pertama:"),
        ("f", "v₁f + (v₁f + 4) = 4   →   2v₁f = 0   →   v₁f = 0"),
        ("f", "v₂f = v₁f + 4 = +4 m/s"),
    ],
    cek=[
        "**Momentum:** sebelum 1×4 = 4 kg·m/s; sesudah 1×0 + 1×4 = 4 kg·m/s ✓",
        "**Energi:** K~i~ = ½(1)(16) = 8 J; K~f~ = 0 + ½(1)(16) = 8 J ✓ kekal",
        "**Aturan tukar kecepatan:** v₁f = v₂i = 0 dan v₂f = v₁i = +4 m/s ✓",
        "**Kewajaran:** pada biliar, bola putih berhenti dan bola sasaran bergerak maju — sesuai "
        "pengamatan sehari-hari ✓",
    ],
    jawaban="v~1f~ = **0** (berhenti) dan v~2f~ = **+4 m/s**.",
    catatan="Pada tumbukan miring dengan massa sama, kedua bola selalu terpisah dengan sudut 90° "
            "(kecuali tumbukan lurus). Ini alat pemeriksa cepat untuk soal dua dimensi.",
),

dict(
    no=29, judul="Tumbukan elastis dengan massa berbeda",
    rumus_inti="v~1f~ = [(m~1~−m~2~)v~1i~ + 2m~2~v~2i~]/(m~1~+m~2~)",
    sumber="Cheatsheet Minggu 6, poin 29 · Subbab 6-8",
    rumus=[("v~1f~ = [(m~1~ − m~2~)v~1i~ + 2m~2~v~2i~]/(m~1~ + m~2~)", None),
           ("v~2f~ = [2m~1~v~1i~ + (m~2~ − m~1~)v~2i~]/(m~1~ + m~2~)", None)],
    penjabaran=[
        "**Arti rumusnya.** Dua rumus ini adalah penyelesaian lengkap tumbukan elastis 1D untuk "
        "massa berbeda. Penyebutnya sama (massa total); pembilangnya mencampur massa dan kecepatan "
        "awal kedua benda.",
        "**Asal rumusnya.** Kedua rumus diperoleh dengan menyelesaikan **dua** persamaan sekaligus: "
        "(i) kekekalan momentum m₁v₁ + m₂v₂ = m₁v₁f + m₂v₂f dan (ii) kekekalan energi kinetik, "
        "yang untuk 1D ditulis lebih ringkas sebagai v₁ − v₂ = −(v₁f − v₂f).",
        "**Kasus khusus yang wajib diingat.** (i) m₁ = m₂ → bertukar kecepatan (Soal 28); "
        "(ii) m₁ ≪ m₂ (bola menumbuk dinding) → bola memantul dengan laju hampir sama; "
        "(iii) m₁ ≫ m₂ → benda berat nyaris tak berubah, benda ringan terlempar dengan laju ≈ 2v₁.",
    ],
    lambang=[
        ("m~1~, m~2~", "massa benda pertama dan kedua", "kilogram (kg)"),
        ("v~1i~, v~2i~", "kecepatan sebelum tumbukan (bertanda)", "meter/sekon (m/s)"),
        ("v~1f~, v~2f~", "kecepatan setelah tumbukan", "meter/sekon (m/s)"),
        ("m~1~ + m~2~", "massa total — penyebut yang sama untuk kedua rumus", "kilogram (kg)"),
    ],
    satuan="Pembilang bersatuan kg·m/s dan penyebut kg, sehingga hasilnya m/s ✓.",
    syarat="Hanya untuk tumbukan **elastis 1D**. Untuk target yang mula-mula diam (v~2i~ = 0), "
           "rumus menyederhana: v₁f = ((m₁−m₂)/(m₁+m₂))v₁ dan v₂f = (2m₁/(m₁+m₂))v₁.",
    soal="Benda m₁ = 2 kg bergerak +5 m/s menumbuk benda m₂ = 3 kg yang diam secara elastis. "
         "Tentukan kecepatan kedua benda setelah tumbukan, lalu periksa momentum dan energinya.",
    isi=[
        ("p", "**Langkah 1 — kecepatan benda pertama** (v~2i~ = 0, sehingga suku kedua hilang):"),
        ("f", "v₁f = [(2 − 3)(5)]/(2 + 3) = (−1)(5)/5 = −1 m/s"),
        ("p", "**Langkah 2 — kecepatan benda kedua:**"),
        ("f", "v₂f = [2(2)(5)]/5 = 20/5 = +4 m/s"),
        ("p", "**Langkah 3 — periksa momentum:**"),
        ("f", "p~i~ = (2)(5) + (3)(0) = 10 kg·m/s"),
        ("f", "p~f~ = (2)(−1) + (3)(4) = −2 + 12 = 10 kg·m/s  ✓"),
        ("p", "**Langkah 4 — periksa energi kinetik:**"),
        ("f", "K~i~ = ½(2)(5²) = 25 J"),
        ("f", "K~f~ = ½(2)(1²) + ½(3)(4²) = 1 + 24 = 25 J  ✓"),
    ],
    cek=[
        "Momentum kekal (10 = 10) dan energi kinetik kekal (25 = 25) → hasilnya konsisten untuk "
        "tumbukan elastis ✓",
        "**Tanda v₁f negatif:** benda pertama memantul karena menumbuk benda yang lebih berat "
        "(m₂ > m₁) ✓",
        "**Uji syarat elastis 1D:** v₁i − v₂i = 5 − 0 = 5, sedangkan −(v₁f − v₂f) = "
        "−(−1 − 4) = 5. Keduanya sama, jadi syarat elastis memang terpenuhi ✓",
        "**Kewajaran:** benda ringan memantul, benda berat bergerak maju dengan laju lebih kecil "
        "daripada laju datang (4 < 5) ✓",
    ],
    jawaban="v₁f = **−1 m/s** (memantul) dan v₂f = **+4 m/s**.",
    catatan="Selalu periksa dengan momentum **dan** energi. Bila hanya momentum yang cocok, "
            "kemungkinan besar ada kesalahan tanda; bila keduanya cocok, hampir pasti benar.",
),
]
