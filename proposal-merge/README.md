# proposal-merge — Perangkat Penggabungan Dua Dokumen Proposal Disertasi

Folder ini menyiapkan pekerjaan penggabungan dua file proposal menjadi **satu proposal yang lengkap**:
panduan, rubrik evaluasi, template, matriks pemetaan, dan script analisis otomatis.

## Isi folder

| File | Fungsi |
|---|---|
| `panduan-penggabungan-proposal.md` | **Baca ini dulu.** 18 komponen wajib proposal, rubrik penilaian penguji, strategi per pola pasangan file, protokol penggabungan 9 langkah, checklist akhir, penggunaan LeapSpace/ScienceDirect AI secara aman. |
| `template-proposal-gabungan.md` | Cetakan penulisan dokumen final (18 seksi + tabel koherensi RQ → instrumen → analisis → luaran). |
| `matriks-pemetaan-seksi.csv` | Matriks kerja 18 komponen × {A, B}: status, catatan konflik, penanggung jawab. |
| `tools/analisis_dua_proposal.py` | Script analisis tumpang-tindih otomatis (tanpa dependensi eksternal untuk .txt/.md/.docx). |
| `tools/tangkap_pdf.py` | Ekstraksi teks dari PDF proposal / laporan LeapSpace ke `.txt` agar bisa dianalisis. |
| `tools/md_ke_docx.py` | Konversi naskah gabungan (Markdown) menjadi `.docx` berformat akademik: A4, margin 4/4/3/3 cm, Times New Roman 12 pt, spasi 1,5, tabel Word, gaya Heading otomatis. |
| `acuan/` | Tempat menaruh PDF proposal dan keluaran LeapSpace; lihat `acuan/LETAKKAN-FILE-DI-SINI.md`. |
| `contoh/` | Dua file proposal contoh + hasil analisisnya, untuk melihat cara kerja tool sebelum memakai file asli. |

## Cara pakai (3 langkah)

```bash
cd proposal-merge

# 1. Analisis dua file Anda (boleh .docx / .txt / .md; .pdf perlu: pip install pypdf)
python3 tools/analisis_dua_proposal.py \
  --a /jalur/proposal-A.docx --b /jalur/proposal-B.docx \
  --out hasil --nama-a "Draft Pembimbing 1" --nama-b "Rencana Penelitian"

# 2. Baca ringkasannya
cat hasil/laporan-tumpang-tindih.md

# 3. Kerjakan daftar tindak lanjut
#    hasil/daftar-konflik.md     -> keputusan yang harus Anda ambil
#    hasil/kerangka-gabungan.md  -> cetakan penulisan dokumen final
#    hasil/pemetaan-seksi.csv    -> peta asal isi & lubang yang harus diisi
```

Contoh hasil analisis pada file di `contoh/` sudah tersedia di `contoh/hasil-demo/`.

## Apa yang dijawab tool ini

1. **Apakah dua file itu saling melengkapi?** — dengan memetakan 18 komponen proposal, lalu menunjukkan mana yang hanya ada di A, hanya di B, ada di keduanya, dan **kosong di keduanya**.
2. **Di mana tumpang-tindihnya?** — daftar pasangan paragraf mirip (skor kemiripan) untuk dipilih/dilebur, bukan ditempel dua kali.
3. **Di mana konfliknya?** — perbedaan angka sampel, durasi, jumlah item instrumen, anggaran, dan metode yang wajib diputuskan manusia; script sengaja **tidak** memutuskan sendiri.

## Alur lengkap (yang dijalankan pada file asli Anda)

```bash
cd proposal-merge
python3 tools/tangkap_pdf.py --folder acuan --out acuan/teks     # 1. enam PDF -> teks
python3 tools/analisis_dua_proposal.py \                          # 2. analisis tumpang-tindih
  --a "acuan/teks/Proposal Disertasi Michael Raintung - Revisi Seminar Proposal.txt" \
  --b "acuan/teks/Proposal Disertasi Michael Raintung 14 Oktober 2026.txt" \
  --out hasil --nama-a "Revisi Seminar Proposal" --nama-b "Versi 14 Oktober 2026"
# 3. naskah gabungan ditulis mengikuti template-proposal-gabungan.md
python3 tools/md_ke_docx.py --masuk hasil/proposal-gabungan.md \
  --keluar hasil/proposal-gabungan.docx --judul "PROPOSAL DISERTASI" \
  --penulis "Michael Raintung"                                    # 4. -> .docx siap edit
```

## Catatan

- Tool ini alat bantu keputusan, bukan penilai kualitas akademik. Semua keputusan substantif tetap milik penulis dan pembimbing.
- File asli tidak pernah diubah; script hanya membaca dan menulis keluaran ke folder `hasil/`.
- Jangan letakkan data responden atau berkas rahasia di repositori publik ini.

## Merakit naskah gabungan (pipeline dua langkah)

Naskah gabungan final dihasilkan dari tiga berkas sumber (A = induk, B dan C = sumber
transplantasi) dengan dua perintah berurutan:

```bash
python3 tools/rakit_proposal.py     # merakit naskah: struktur A + sisipan B/C + tabel + daftar pustaka
python3 tools/rapikan_tabel.py      # merekonstruksi tabel A dari PDF, membuang tabel duplikat, menomori ulang
python3 tools/md_ke_docx.py --masuk hasil/proposal-gabungan.md --keluar hasil/proposal-gabungan.docx \
        --judul "..." --penulis "..."
```

Catatan penting:

- `rakit_proposal.py` membaca teks bersih `/tmp/bersih-{A,B,C}.txt` (hasil `tools/tangkap_pdf.py`)
  dan catatan `catatan-integrasi.md`, lalu menulis `hasil/proposal-gabungan.md`.
- `rapikan_tabel.py` memerlukan `pymupdf` (`pip install --break-system-packages pymupdf`) dan
  membaca PDF berkas A dari folder `../google_drive/`.
- `md_ke_docx.py` menyisipkan halaman **Daftar Isi otomatis** (field TOC Word) dan menandai
  dokumen agar Word memperbarui bidang saat dibuka. Gunakan `--tanpa-daftar-isi` bila tidak diinginkan.
- Perapian hanya dijalankan sekali per regenerasi: urutannya selalu rakit → rapikan → konversi.
