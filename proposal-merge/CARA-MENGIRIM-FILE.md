# Cara Mengirim 6 File ke Saya (pilih salah satu)

Enam file yang perlu dikirim:

**Kelompok 1 — dua file proposal (bahan utama):**
1. `Proposal Disertasi Michael Raintung - Revisi Seminar Proposal.pdf`
2. `Proposal Disertasi Michael Raintung 14 Oktober 2026.pdf`

**Kelompok 2 — empat keluaran LeapSpace (acuan penilaian):**
3. `Comparison_of_research_proposal_readiness_LeapSpace.pdf`
4. `Evaluation_of_dissertation_proposal_completeness_LeapSpace.pdf`
5. `Comparison_of_dissertation_proposal_versions_LeapSpace.pdf`
6. `Integration_of_dissertation_proposal_documents_LeapSpace.pdf`

---

## ⚠️ Pertimbangan privasi (baca dulu, 20 detik)

Cara 1 (GitHub) memakai repositori **publik** — siapa pun bisa melihat file yang Anda unggah.
Naskah proposal disertasi umumnya tidak rahasia, tetapi **keputusan tetap di tangan Anda**:

- Kalau tidak masalah file terlihat publik → pakai **Cara 1**.
- Kalau ingin lebih tertutup → pakai **Cara 2** (tempel teks) atau kirim lewat tautan Drive pribadi (Cara 3).

---

## ✅ Cara 1 — Unggah lewat GitHub (±60 detik) — **paling cepat**

1. Buka: **https://github.com/michaelraintung-cloud/copilot-hack/upload/main**
2. Seret keenam PDF ke kotak unggah di halaman itu. Nama berkas **biarkan apa adanya** (saya sudah menyiapkan pengenalan otomatis berdasarkan nama).
3. Di bagian bawah halaman, klik tombol hijau **"Commit changes"**.
4. Tunggu halaman repositori muncul kembali — pastikan keenam nama PDF terlihat di daftar berkas.
5. Balas di chat: **"sudah diunggah"**

> Bingung soal branch? Tidak perlu diubah. Biarkan pada `main`.
> Ingin lebih rapi? Anda juga boleh membungkus keenam PDF menjadi **satu file `.zip`** dan mengunggah ZIP itu saja — sistem saya sudah otomatis membuka ZIP.
> Bingung lewat HP? Langkah sama; pada layar HP, tombol "Add file" ada di kanan atas halaman repo.

## ✅ Cara 2 — Tempel teks di chat — **paling privat**

1. Buka PDF-nya (Adobe Acrobat, browser, atau aplikasi HP).
2. Tekan `Ctrl+A` (pilih semua) lalu `Ctrl+C` (salin).
3. Tempel ke chat di sini, **boleh bertahap**: kirim Bab 1 dulu → saya kerjakan → lanjut Bab 2 → Bab 3.
4. Untuk 4 file LeapSpace: cukup salin **poin-poin temuannya** (daftar yang ditandai belum lengkap, saran penggabungan, skor/kriteria penilaian). Tabel boleh ditempel mentah-mentah.

## ✅ Cara 3 — Tautan unduhan

1. Unggah keenam PDF ke Google Drive / Dropbox / OneDrive.
2. Atur izin menjadi **"Siapa saja yang memiliki tautan"**.
3. Kirim keenam tautannya di chat.

> Catatan teknis: akses jaringan saya dibatasi ke beberapa host saja, jadi tautan **GitHub adalah yang paling pasti berhasil**; tautan Drive/Dropbox akan saya coba, dan bila gagal saya beri tahu segera.

---

## Setelah file masuk: apa yang saya lakukan

| # | Langkah | Hasil |
|---|---|---|
| 1 | Tarik keenam file, ekstrak teksnya | 6 berkas teks, peringatan bila ada yang hasil pindai (perlu OCR) |
| 2 | Peta cakupan 18 komponen proposal untuk kedua naskah | tabel: mana hanya di A, hanya di B, ada di keduanya, **kosong di keduanya** |
| 3 | Deteksi tumpang-tindih + konflik angka | daftar paragraf duplikat & daftar konflik (sampel, durasi, item instrumen, metode) |
| 4 | Terapkan temuan 4 file LeapSpace | daftar target revisi wajib beres, dipetakan ke seksi proposal |
| 5 | Tentukan dokumen induk + tulis naskah gabungan | satu naskah 18 komponen, RQ/tujuan/metode sudah disatukan |
| 6 | Catat setiap keputusan | `changelog-gabungan.md` (apa diambil dari mana, dan mengapa) |
| 7 | Format jadi berkas Word | `proposal-gabungan.docx`: A4, margin 4/4/3/3 cm, Times New Roman 12, spasi 1,5, tabel Word, Heading otomatis untuk daftar isi |

Perintah yang akan saya jalankan (untuk transparansi):

```bash
cd proposal-merge
python3 tools/pipeline_proposal.py                       # deteksi + ekstrak + analisis otomatis
python3 tools/pipeline_proposal.py --dari-git origin/main  # khusus bila Anda unggah lewat GitHub
python3 tools/md_ke_docx.py --masuk hasil/proposal-gabungan.md \
  --keluar hasil/proposal-gabungan.docx \
  --judul "PROPOSAL DISERTASI" --penulis "Michael Raintung"
```

---

## Kalau unggahan tetap gagal

Kirim satu pesan berisi: **halaman berapa saja yang ada di masing-masing PDF** (mis. "proposal revisi 42 halaman, versi 14 Okt 55 halaman"). Dari struktur halaman itu saya bisa menyusun kerangka gabungannya lebih dulu, sambil menunggu teks lengkapnya masuk.

Dan bila ada kendala teknis apa pun saat mengunggah, cukup bilang **"bagian mana yang macet"** — saya pandu langkah berikutnya satu per satu.
