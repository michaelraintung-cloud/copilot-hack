# Panduan Menggabungkan Dua Dokumen Proposal Disertasi Menjadi Satu Proposal Lengkap

> **Status dokumen:** kerangka kerja siap pakai + rubrik evaluasi.
> Dokumen ini disusun **sebelum** kedua file proposal diterima, sehingga bersifat *template-agnostik*:
> berlaku untuk pasangan file apa pun (draft lama vs draft baru, bab akademik vs rencana penelitian,
> versi kualitatif vs kuantitatif, naskah Indonesia vs naskah Inggris).
> Begitu kedua file tersedia, langkah 3–6 di bawah dijalankan otomatis oleh
> `tools/analisis_dua_proposal.py` dan hasil gabungannya ditulis ke `hasil/`.

---

## 0. Ringkasan jawaban atas tiga pertanyaan Anda

| Pertanyaan Anda | Jawaban singkat |
|---|---|
| Apa saran atas kedua file itu? | Belum bisa dinilai isinya karena file belum tersedia. Yang bisa saya berikan sekarang: **18 komponen wajib proposal disertasi + rubrik penilaian penguji** (Bagian 2 & 3). Kirimkan kedua file, lalu saya nilai per komponen. |
| Apakah kedua file bisa saling melengkapi? | **Hampir selalu bisa, dan biasanya memang dirancang begitu.** Hasil analisis tumpang-tindih (Bagian 4 + script) akan memecah setiap paragraf menjadi empat status: *hanya di A*, *hanya di B*, *duplikat (digabung)*, *bertentangan (harus diputuskan)*. Yang menentukan proposal gabungan "lengkap" atau tidak adalah **seksi yang berstatus "tidak ada di keduanya"** — itulah lubang yang harus ditulis baru. |
| Saran dari halaman ScienceDirect/LeapSpace? | Halaman itu di balik login institusi (saya tidak punya akses). Namun kemampuan LeapSpace yang relevan sudah publik dan saya pakai di Bagian 7: unggah ≤5 PDF per percakapan, Trust Cards + *link-to-statement*, Claim Radar, Deep Research. Sumber acuan yang dipakai di dokumen ini tercantum di Bagian 9. |

---

## 1. Aturan emas sebelum mulai menggabungkan (baca ini dulu)

1. **Satu dokumen harus menang.** Tentukan *base document*: file yang kerangka besarnya paling dekat dengan format institusi Anda. File kedua diperlakukan sebagai **sumber transplantasi**, bukan sebagai dokumen tandingan. Tanpa aturan ini, penggabungan selalu berakhir jadi "karangan dua kepala" yang tidak punya garis merah.
2. **Hanya boleh ada SATU dari setiap hal berikut di dokumen akhir:** satu set rumusan masalah, satu set pertanyaan penelitian, satu desain metodologi, satu timeline, satu daftar pustaka, satu sistem penomoran. Semua duplikat konseptual harus dilebur.
3. **Konflik tidak boleh diselesaikan dengan "digabung dua-duanya".** Misalnya A menyebut sampel 120 orang dan B menyebut 40 orang, atau A memakai regresi dan B memakai studi kasus. Pilih satu (atau rancang mixed-methods secara sadar), lalu **ubah seluruh dokumen agar konsisten** dengan pilihan itu.
4. **Setiap paragraf harus punya pekerjaan.** Nama pekerjaan itu ada di rubrik (Bagian 3). Paragraf yang tidak menambah penilaian apa pun = hapus.
5. **Jangan pernah menempelkan teks AI mentah-mentah.** Semua kalimat hasil AI wajib diverifikasi ke sumber aslinya dan ditulis ulang dengan suara Anda sendiri; cantumkan pernyataan penggunaan AI (Bagian 7.3). Ini juga melindungi Anda dari tuduhan plagiarisme.
6. **Simpan jejak audit.** Buat `changelog-gabungan.md`: apa yang diambil dari A, dari B, apa yang dibuang, dan **alasan**nya. Ini yang akan Anda tunjukkan ke pembimbing ketika beliau bertanya "kok bagian ini hilang?".

---

## 2. Anatomi proposal disertasi yang benar-benar lengkap (18 komponen)

Kolom **Status di file Anda** diisi lewat matriks `matriks-pemetaan-seksi.csv`.
Kolom panjang bersifat indikatif; **aturan resmi program Anda selalu menang.**

| # | Komponen | Isi minimum | "Tes penguji" (indikator lulus) | Panjang indikatif |
|---|---|---|---|---|
| 1 | **Halaman informasi** | Judul, nama/NIM, program, pembimbing, tanggal versi | Judul ≤ 20 kata, mengandung variabel + konteks + desain | 1 hlm |
| 2 | **Ringkasan eksekutif / abstrak** | Masalah, gap, tujuan, metode, luaran yang diharapkan | Bisa dibaca berdiri sendiri; tidak ada klaim tanpa dasar di bab isi | 250–400 kata |
| 3 | **Latar belakang** | Konteks, data/fenomena terbaru (≤5 tahun), definisi masalah | Ada angka/fakta konkret, bukan hanya "sangat penting" | 3–6 hlm |
| 4 | **Problem statement** | Kesenjangan antara kondisi nyata dan kondisi ideal | Ditulis sebagai *masalah*, bukan *topik* | 1–2 hlm |
| 5 | **Analisis gap penelitian** | Tabel 3 kolom: *sudah diteliti → belum terjawab → bagaimana riset ini menjawab* | Setiap pertanyaan penelitian bisa dilacak ke satu baris gap | 2–4 hlm |
| 6 | **Urgensi/signifikansi** | Nilai teoretis, praktis, kebijakan | Menyebut pemangku kepentingan konkret + manfaat spesifik | 1–2 hlm |
| 7 | **Rumusan & pertanyaan penelitian** | 1 pertanyaan utama + 2–4 sub-pertanyaan; kalimat tanya | Tidak ada pertanyaan yang mustahil dijawab dengan metode yang dipilih | 0,5–1 hlm |
| 8 | **Tujuan & sasaran** | Tujuan umum + tujuan khusus, paralel dengan pertanyaan penelitian (1:1) | Jumlah tujuan = jumlah pertanyaan penelitian | 0,5 hlm |
| 9 | **Batasan & definisi operasional** | Ruang lingkup, batas (waktu, wilayah, populasi), glosarium variabel | Setiap variabel punya definisi yang bisa diukur | 1–2 hlm |
| 10 | **Kerangka teori & state of the art** | Teori utama (≥2), penelitian terdahulu, peta posisi riset | Ada sintesis, bukan daftar ringkasan berurutan | 6–12 hlm |
| 11 | **Kerangka berpikir & model konseptual** | Diagram alur, hipotesis atau proposisi | Setiap panah di diagram punya dasar teori/pustaka | 1–3 hlm |
| 12 | **Metodologi** | Paradigma & desain; populasi–sampel (teknik + ukuran + justifikasi); instrumen (validitas & reliabilitas); prosedur; analisis data; **tabel pemetaan RQ → data → teknik analisis → luaran** | Bisa direplikasi orang lain dari deskripsinya saja | 8–15 hlm |
| 13 | **Etika penelitian & perlindungan data** | Izin etik, informed consent, kerahasiaan, penyimpanan data, UU PDP, pernyataan benturan kepentingan | Ada nomor/status protokol etik atau rencana pengajuannya | 1–2 hlm |
| 14 | **Keterbatasan & asumsi** | Keterbatasan desain, generalisasi, ancaman validitas | Dinyatakan jujur + mitigasinya | 1 hlm |
| 15 | **Rencana luaran & diseminasi** | Target publikasi (jurnal, quartile), konferensi, HKI, policy brief, dataset | Target jurnal spesifik, bukan "jurnal internasional" | 1 hlm |
| 16 | **Jadwal, milestone & manajemen risiko** | Gantt per triwulan, milestone review, *risk register* (risiko → dampak → mitigasi) | Realistis terhadap beban kerja; ada jalur cadangan | 1–2 hlm |
| 17 | **Anggaran & sumber daya** | Rincian biaya, sumber dana/beasiswa, kebutuhan alat | Jumlah cocok dengan timeline & metode | 1 hlm |
| 18 | **Daftar pustaka & lampiran** | Referensi (APA/IEEE/format program), instrumen lengkap, surat izin, pernyataan orisinalitas & penggunaan AI | ≥60–70% referensi primer dari 5 tahun terakhir; tidak ada referensi "hantu" | 10+ hlm |

**Aturan penautan (garis merah).** Semua komponen di atas harus membentuk satu rantai yang bisa dilacak nomor demi nomor:

```
Konteks (3) → Masalah (4) → Gap (5) → RQ (7) → Tujuan (8) → Variabel/fokus (9,11)
   → Metode & instrumen (12) → Analisis (12) → Luaran yang dijanjikan (15) → Kontribusi (6)
```
Bila satu mata rantai bisa diputus tanpa merusak yang lain, berarti rantai itu palsu — dan penguji akan menemukannya.

---

## 3. Rubrik evaluasi: apa yang sebenarnya dinilai penguji

Bobot di bawah adalah sintesis indikatif dari panduan lembaga (lihat Bagian 9), bukan rubrik resmi LeapSpace. Gunakan sebagai daftar periksa, lalu sesuaikan dengan rubrik program Anda.

| Kriteria | Bobot | Pertanyaan yang diajukan penguji | Sinyal gagal |
|---|---|---|---|
| Relevansi & urgensi masalah | 10% | Mengapa harus sekarang? Untuk siapa? | Masalah "penting" tanpa bukti |
| Kejelasan masalah & pertanyaan penelitian | 10% | Bisakah RQ dijawab "ya/tidak" atau terlalu luas? | RQ kabur, terlalu banyak (≥6) |
| Kebaruan & analisis gap | 15% | Apa yang belum dikerjakan orang lain? | Mengklaim "belum ada penelitian" padahal ada |
| Landasan teori & literatur | 15% | Apakah sintesisnya kritis atau hanya katalog? | Referensi tua, sumber sekunder, tidak ada teori rival |
| Metodologi & ketelitian | 20% | Apakah metode benar-benar mengukur yang ditanyakan? | Sampel tanpa justifikasi, instrumen tanpa validitas |
| Kelayakan (waktu, akses, biaya, keterampilan) | 10% | Selesai dalam batas waktu studi? Akses data ada? | Klaim data yang belum diizinkan pemiliknya |
| Etika & manajemen risiko | 5% | Apa yang terjadi bila responden sensitif/data bocor? | Tidak ada bagian etika sama sekali |
| Kontribusi & dampak | 10% | Kontribusi teoretis DAN praktis spesifik? | "Menambah khazanah ilmu" tanpa rincian |
| Kejelasan penulisan, koherensi, kepatuhan format | 5% | Bisa diikuti tanpa membaca dua kali? | Istilah berganti-ganti, nomor tidak sinkron |

**Alasan penolakan/revisi mayor yang paling sering ditemui:**

1. Gap hanya berupa klaim, bukan hasil analisis literatur.
2. Tujuan tidak 1:1 dengan pertanyaan penelitian.
3. Metode mengukur konstruk yang berbeda dari yang dijanjikan RQ.
4. Timeline tidak realistis (etika + izin + pengumpulan data dijadwalkan terlalu pendek).
5. Dokumen hasil "jahit dua file": ada dua definisi variabel, dua set RQ, dua daftar pustaka.
6. Tidak ada jejak kontribusi terhadap praktik/kebijakan padahal itu tujuan disertasi terapan.
7. Tidak ada pernyataan etika & penggunaan AI (makin banyak lembaga mewajibkan pada 2025–2026).

**Dua tes cepat sebelum dikirim ke pembimbing**

- **Tes 90 detik.** Minta orang lain membaca hanya halaman 1–2 dan menuturkan kembali: masalah, gap, RQ, metode, kontribusi. Bila ada satu saja yang salah, bagian tersebut ditulis kurang jelas.
- **Reverse outline.** Tulis satu kalimat di margin untuk setiap paragraf. Bila ada dua kalimat sama dari paragraf berbeda → duplikat; bila ada kalimat yang tidak terkait judul → kandidat hapus.

---

## 4. Apakah dua file itu saling melengkapi? Cara mengujinya secara objektif

Pola pasangan file yang paling sering terjadi, dan strategi gabungannya:

| Pola pasangan | Isi File A | Isi File B | Strategi gabung | Risiko utama |
|---|---|---|---|---|
| **Draft lama vs draft baru** | Kerangka lengkap tapi data literatur usang | Bab teori baru, sitasi baru, revisi RQ | Pakai B sebagai basis, transplantasi bagian A yang belum tergantikan (metode, lampiran) | Kehilangan detail valid yang hilang saat B dibuat ulang |
| **Naskah akademik vs rencana pendanaan** | Bab 1–3 akademik (teori berat) | Research plan ringkas dengan timeline, anggaran, luaran | Bidang akademik jadi inti; impor timeline/anggaran/luaran dari B ke komponen 15–17 | Kalender B tidak cocok dengan tenggat studi A |
| **Kualitatif vs kuantitatif** | Studi kasus/wawancara mendalam | Survei/eksperimen dengan RQ berbeda | Putuskan: pilih satu, atau rancang *mixed methods* dengan fase & titik integrasi eksplisit | "Menggabung dua-duanya" tanpa integrasi = dua proposal di satu dokumen |
| **Naskah Indonesia vs naskah Inggris** | Versi lengkap cerita lokal, data konteks | Versi disetujui pembimbing berbahasa Inggris | Satukan struktur, pilih satu bahasa utama, jadikan versi kedua bahan sinkronisasi istilah | Istilah teknis berbeda terjemahan → variabel tampak berbeda |
| **Teori vs metode** | Bab 2 lengkap, bab 3 kosong | Protokol penelitian & instrumen, bab 2 tipis | Gabungan ideal: A bag. 2 + B bag. 3, tapi RQ harus disatukan dulu | RQ A tidak sejalan dengan instrumen B |
| **Dua domain/objek berbeda** | Unit analisis X | Unit analisis Y | Buat desain komparatif; hanya gabungkan bila ada kerangka bersama | Kontribusi pecah jadi dua yang lemah |

**Metode uji cakupan (dijalankan otomatis oleh `tools/analisis_dua_proposal.py`):**

1. Kedua dokumen dipecah menjadi blok (judul/bab/paragraf/list).
2. Setiap blok dikaitkan ke salah satu dari 18 komponen Bagian 2 lewat pencocokan kata kunci + manual review.
3. Setiap blok A dibandingkan dengan semua blok B (kemiripan teks berbasis `difflib`/shingle) untuk mendapat status:
   - **`A-saja` / `B-saja`** → kandidat transplantasi (inilah nilai tambah masing-masing file),
   - **`duplikat`** (≈0,45–0,85) → pilih versi terbaik, buang yang lain,
   - **`hampir identik`** (>0,85) → ambil satu,
   - **`konflik`** (topik sama, angka/metode/kesimpulan berbeda) → masuk daftar keputusan, wajib diputuskan manusia.
4. Hasil akhirnya: **peta cakupan 18 komponen × {A, B}**. Sel yang kosong di kedua file = **lubang yang harus ditulis baru**; sel yang terisi di keduanya = **tempat pemborosan/redundansi**.
5. Lubang kosong itu kemudian dibandingkan lagi dengan rubrik Bagian 3: seksi dengan bobot penilaian tinggi (gap 15%, metodologi 20%, kebaruan) tidak boleh kosong.

---

## 5. Protokol penggabungan dalam 9 langkah

**Langkah 0 — Bekukan dan konversi.** Simpan salinan asli (jangan pernah edit file asli). Konversi ke teks: `.docx` → teks (script mengekstrak otomatis), `.pdf` → teks (`pip install pypdf`, atau *Print to text*). Catat nomor versi & tanggal setiap file di `changelog-gabungan.md`.

**Langkah 1 — Tetapkan struktur kanonik.** Salin `template-proposal-gabungan.md`; ini daftar 18 komponen Bagian 2 yang sudah diberi placeholder. Struktur ini adalah "cetakan" tempat kedua file dituang.

**Langkah 2 — Inventarisasi per seksi.** Isi `matriks-pemetaan-seksi.csv`: untuk tiap komponen, tandai `A-saja`, `B-saja`, `A+B`, `konflik`, atau `kosong`. Kesampingkan dulu gaya penulisan; yang penting kelengkapan isi.

**Langkah 3 — Analisis tumpang-tindih menyeluruh.** Jalankan:
```bash
python3 tools/analisis_dua_proposal.py --a FILE_A --b FILE_B --out hasil/
```
Hasil: `hasil/laporan-tumpang-tindih.md` (ringkasan + peta cakupan), `hasil/pemetaan-seksi.csv`, `hasil/daftar-duplikat.md`, `hasil/daftar-konflik.md`, `hasil/kerangka-gabungan.md`.

**Langkah 4 — Putuskan konflik satu per satu.** Untuk setiap item di `daftar-konflik.md`, pakai aturan keputusan berikut lalu tulis keputusannya di changelog:

| Jenis konflik | Aturan keputusan |
|---|---|
| Angka (n sampel, durasi, anggaran) | Pilih yang paling *defensible* + bisa Anda pertahankan di depan penguji; angka dari file yang lebih baru belum tentu benar |
| Rumusan masalah / RQ | Pilih set RQ yang paling selaras dengan metode yang benar-benar bisa Anda jalankan |
| Metode | Pilih yang mengukur konstruk RQ (bukan yang paling canggih); bila tetap ingin keduanya → tulis sebagai *mixed methods* dengan fase, titik integrasi, dan RQ per fase |
| Teori | Jangan buang salah satunya: susun sebagai "teori utama + teori pendukung" dan jelaskan perannya |
| Timeline | Gunakan timeline paling ketat (yang realistis) dan tambahkan *buffer*; revisi tanggal milestone lain agar konsisten |
| Istilah/variabel | Buat glosarium, pilih satu istilah resmi, lalu cari-ganti di seluruh dokumen |

**Langkah 5 — Tulis dokumen baru, jangan tempel-tempel.** Susun ulang dari `kerangka-gabungan.md`, seksi demi seksi sesuai urutan 18 komponen. Wajib: setiap akhir seksi diberi **satu paragraf penyambung** yang menutup dengan "oleh karena itu, penelitian ini…" agar alur antar-penulis tidak terasa.

**Langkah 6 — Seragamkan.** Satu gaya sitasi (APA 7/IEEE), satu glosarium istilah, penomoran tabel/gambar/simbol konsisten, satuan konsisten, nama variabel identik di RQ, instrumen, dan analisis. Satukan juga daftar pustaka (hapus entri ganda; pastikan sitasi "yatim" diselesaikan).

**Langkah 7 — Lima pemeriksaan mutu.**
1. **Uji tracetabilitas:** isi tabel `RQ → tujuan → variabel → instrumen/item → teknik analisis → luaran`. Setiap baris harus lengkap; baris kosong = kerja belum selesai.
2. **Uji konsistensi angka:** n sampel, jumlah item, durasi, anggaran muncul identik di semua tempat (termasuk abstrak).
3. **Uji kelengkapan:** bandingkan dengan 18 komponen + rubrik Bagian 3.
4. **Uji keterbacaan & plagiarisme/AI:** cek kemiripan, cek kalimat yang "berbau AI" (frasa kosong, daftar tanpa pengembangan), dan pastikan pernyataan penggunaan AI ada.
5. **Tes 90 detik & reverse outline** (Bagian 3).

**Langkah 8 — Catat & minta validasi.** Simpan `changelog-gabungan.md` + `kerangka-gabungan.md` sebagai lampiran internal, lalu kirim versi final ke **kedua** pihak yang punya file asli (pembimbing A & B) beserta ringkasan "apa yang saya ubah dan mengapa". Ini mencegah revisi bolak-balik.

**Langkah 9 — Arsipkan.** Simpan versi final bernomor (`v1.0`, `v1.1`) di repositori Git agar setiap perubahan punya riwayat. Jangan menyimpan data sensitif/responden di repositori publik.

---

## 6. Kerangka koherensi: tabel yang wajib ada di proposal jadi

Tanpa tabel ini, proposal gabungan akan terasa seperti dua dokumen yang dijahit. Sertakan tabel berikut (bisa di lampiran) sebelum pengajuan:

| RQ | Tujuan | Variabel/fokus | Instrumen (item) | Sumber data | Teknik analisis | Luaran yang menjawab RQ |
|---|---|---|---|---|---|---|
| RQ1 | | | | | | |
| RQ2 | | | | | | |
| RQ3 | | | | | | |

Bila satu kolom kosong, itu bukan kekurangan kosmetik: itu celah yang akan ditanyakan penguji.

---

## 7. Memakai LeapSpace / ScienceDirect AI secara aman dan produktif

### 7.1 Kemampuan yang relevan (dari informasi publik Elsevier)
- **Unggah file:** sampai 5 PDF per percakapan, digabungkan dengan 100M+ sumber terindeks Scopus dalam satu percakapan — berguna untuk **menguji draft gabungan terhadap literatur terbaru dan menemukan celah yang belum Anda tangani**.
- **Trust Cards + `link to statement`:** menunjukkan seberapa dekat klaim AI dengan kalimat sumber aslinya.
- **Claim Radar:** menguji apakah satu klaim masih bertahan di seluruh korpus literatur, bukan pada satu sumber.
- **Deep Research:** menyusun rencana penelitian & tinjauan literatur bertahap lintas konten terkurasi.
- File dienkripsi, tidak dipakai melatih model, tidak dibagikan. Publikasi/institusi memakainya sebagai lapisan validasi pra-submisi.

### 7.2 Cara memakainya untuk pekerjaan penggabungan ini (urutan yang disarankan)
1. Gabungkan dulu kedua file secara internal (Langkah 0–6), baru unggah **versi gabungan** + 3–4 artikel kunci sebagai PDF.
2. Prompt pemeriksaan gap (contoh):
   - "Berdasarkan dokumen yang saya unggah, sebutkan klaim tentang kebaruan yang tidak didukung literatur 2022–2026, dan tunjukkan sumbernya."
   - "Literatur apa yang menjawab pertanyaan penelitian ini namun belum disitasi di dokumen? Sebutkan hanya yang benar-benar relevan."
   - "Periksa apakah desain metodologi ini benar-benar dapat menjawab RQ1–RQ3, dan di mana mata rantainya terputus."
3. Verifikasi setiap jawaban lewat Trust Card / tautan sumber. Klaim tanpa sumber = dianggap belum ada.
4. Jangan pernah mengunggah: data responden, dokumen embargo, atau materi rahasia mitra/pemilik data.

### 7.3 Pernyataan penggunaan AI (wajib dicantumkan)
Cantumkan di halaman pernyataan/etika, contoh kalimat:

> "Penulis menggunakan alat bantu AI generatif (nama alat, versi, tanggal) untuk [memeriksa koherensi bahasa / menyusun kerangka pencarian literatur / memeriksa tumpang-tindih dua draf]. Semua klaim faktual, sitasi, dan keputusan metodologis diverifikasi ulang oleh penulis terhadap sumber aslinya. Tidak ada data penelitian atau data pribadi yang diunggah ke alat tersebut. Alat AI tidak dicantumkan sebagai penulis."

Periksa juga kebijakan program studi dan kebijakan penerbit target (Elsevier dan banyak penerbit lain mewajibkan pengungkapan penggunaan AI generatif, dan melarang AI sebagai penulis).

---

## 8. Checklist akhir sebelum diserahkan

**Kelengkapan**
- [ ] 18 komponen Bagian 2 ada semua (atau pengecualian resmi dari program dicatat)
- [ ] Tidak ada dua versi RQ/tujuan/metode/timeline/daftar pustaka
- [ ] Abstrak memuat masalah, gap, tujuan, metode, luaran

**Koherensi**
- [ ] Rantai Konteks → Masalah → Gap → RQ → Tujuan → Variabel → Metode → Analisis → Luaran utuh
- [ ] Jumlah tujuan = jumlah pertanyaan penelitian
- [ ] Setiap RQ punya instrumen, teknik analisis, dan luaran
- [ ] Setiap panah di diagram kerangka punya dasar pustaka

**Metodologi**
- [ ] Teknik & ukuran sampel dijustifikasi (bukan hanya disebut)
- [ ] Instrumen punya rencana uji validitas & reliabilitas
- [ ] Definisi operasional variabel bisa diukur
- [ ] Keterbatasan & ancaman validitas dinyatakan

**Administratif & etika**
- [ ] Status izin etik jelas (sudah/pada tahap pengajuan)
- [ ] Timeline memuat waktu izin, etik, uji instrumen, dan pengumpulan data
- [ ] Anggaran konsisten dengan metode & timeline
- [ ] Target luaran spesifik (nama jurnal/konferensi)
- [ ] Pernyataan orisinalitas, benturan kepentingan, penggunaan AI
- [ ] Sitasi primer ≥60–70%, dominan 5 tahun terakhir, tanpa referensi hantu

**Kualitas dokumen**
- [ ] Tes 90 detik dan reverse outline lulus
- [ ] Gaya sitasi, penomoran, glosarium istilah konsisten
- [ ] `changelog-gabungan.md` dibuat dan siap ditunjukkan ke pembimbing

---

## 9. Sumber acuan

- Elsevier — LeapSpace / ScienceDirect AI (kemampuan, Trust Cards, Claim Radar, Deep Research, unggah PDF, keamanan data): [researcher.elsevier.com](https://researcher.elsevier.com/), [peluncuran LeapSpace](https://librarytechnology.org/pr/31956), [LeapSpace go-live](https://librarytechnology.org/document/32162)
- Panduan proposal disertasi & evaluasinya: [Stanford GSE Doctoral Handbook](https://ed.stanford.edu/academics/doctoral-handbook/milestones/dissertation-proposal), [SDSU JDP Dissertation Proposal](https://psychology.sdsu.edu/doctoral/clinical/student-handbook/program-requirements/dissertation/dissertation-proposal/), [University of Sydney — Writing a Thesis Proposal (termasuk bagian Evaluation of the Proposal)](https://www.sydney.edu.au/content/dam/students/documents/learning-resources/learning-centre/writing-a-thesis-proposal.pdf), [UNT — Review the Literature](https://guides.library.unt.edu/Dissertation-thesis-proposal/review-literature), [The Dissertation Research Proposal Process: A Systematic Approach (Journal of Research Initiatives)](https://digitalcommons.uncfsu.edu/cgi/viewcontent.cgi?article=1398&context=jri)
- Catatan: halaman "Dissertation proposal review and evaluation – LeapSpace – ScienceDirect.com" yang Anda sebut berada di balik autentikasi institusi, sehingga isinya tidak dapat diverifikasi langsung dari sini. Bila Anda menempelkan teksnya ke chat, rubrik Bagian 3 akan saya selaraskan dengan kriteria halaman tersebut.

---

## 10. Yang saya perlukan untuk melanjutkan (menggabungkan yang sebenarnya)

1. **Kedua file** — lampirkan langsung di chat (`.docx`, `.pdf`, `.md`, atau `.txt`), atau beri tautan publik/letakkan di repositori ini lalu sebutkan jalurnya. Beri label **A** dan **B**.
2. **Fakta konteks:** program & jenjang, institusi, format resmi/template program (bila ada), tenggat, bahasa utama, gaya sitasi, dan siapa pemilik masing-masing file (pembimbing mana).
3. **Hasil yang diinginkan:** naskah gabungan penuh berbahasa Indonesia/Inggris, atau naskah + laporan audit tumpang-tindih untuk didiskusikan dengan pembimbing.

Setelah itu saya akan menjalankan analisis tumpang-tindih pada file asli, menandai setiap konflik, dan menyusun draf gabungan seksi demi seksi sesuai 18 komponen di atas.
