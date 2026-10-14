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

## Catatan

- Tool ini alat bantu keputusan, bukan penilai kualitas akademik. Semua keputusan substantif tetap milik penulis dan pembimbing.
- File asli tidak pernah diubah; script hanya membaca dan menulis keluaran ke folder `hasil/`.
- Jangan letakkan data responden atau berkas rahasia di repositori publik ini.
