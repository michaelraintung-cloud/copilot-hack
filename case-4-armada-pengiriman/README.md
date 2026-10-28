# Laporan Studi Kasus 4 — "Armada Banyak, Pengiriman Tetap Terlambat"

Bidang: **Supply Chain & Distribution** · Mata kuliah: Manajemen Industri
Sumber kasus: `INDUSTRIAL TECHNOLOGY CHALLENGE case.pdf` (halaman 10–11).

## Berkas hasil

| Berkas | Keterangan |
|---|---|
| `output/laporan-studi-kasus-4.docx` | **Berkas utama**. A4, Times New Roman 12 pt, spasi 1,5, margin 2,54 cm, rata kiri-kanan. Halaman sampul masih memakai penanda `[...]` untuk nama, NIM, kelas, dosen, dan institusi. |
| `output/laporan-studi-kasus-4.pdf` | Versi PDF untuk dibaca/dicetak (pratinjau tata letak). |
| `figures/*.png` | Empat gambar: alur proses + *pain points*, *fishbone*, tornado sensitivitas, Gantt 90 hari. |
| `src/model.py` | Model perhitungan: seluruh angka laporan dihitung dari satu sumber agar konsisten dan dapat diaudit. |
| `src/build_report.py` | Pembangun dokumen DOCX (isi, tabel, gambar). |
| `src/docx_utils.py` | Utilitas format DOCX sesuai ketentuan penulisan. |
| `src/render_pdf.py` | Perender PDF (ReportLab, metrik Times) untuk pratinjau dan pemeriksaan paginasi. |
| `src/figures.py` | Pembuat gambar. |

## Struktur laporan

Sampul → Ringkasan → Bab I–VI → Daftar Pustaka → Lampiran 1–8.

Kedelapan output wajib pada petunjuk studi kasus terpenuhi:

1. Identifikasi masalah & akar penyebab — Bab I.2, Bab III.1–3.2, Lampiran 3 (lima mengapa)
2. Analisis kuantitatif & biaya masalah — Bab II.4 (Tabel 2.2), Lampiran 1
3. Perbandingan ≥3 alternatif — Bab IV.1, IV.3 (4 alternatif, Tabel 4.2 & 4.3)
4. Rekomendasi + asumsi eksplisit — Bab IV.4, Lampiran 2 (A1–A15)
5. Risiko operasional/teknologi/sosial/keamanan data — Bab V.4, Lampiran 7 (14 risiko)
6. KPI — Bab V.5, Lampiran 8 (definisi operasional)
7. Rencana implementasi 90 hari — Bab V.1, Lampiran 8 (Gantt + gate)

## Angka kunci (dapat direproduksi)

```
python3 src/model.py     # cetak seluruh perhitungan
python3 src/figures.py   # regenerasi gambar
python3 src/build_report.py && python3 src/render_pdf.py
```

| Besaran | Nilai |
|---|---|
| Jarak tempuh armada | 936.000 km/tahun |
| Konsumsi BBM | 93.600 liter/tahun (Rp936 juta) |
| Biaya akibat masalah (*cost of poor performance*) | Rp610,8 juta/tahun (±Rp12.240/kiriman) |
| Alternatif terpilih | A4 — hybrid bertahap |
| Capex / Opex A4 | Rp125 juta / Rp99 juta per tahun |
| NPV 3 tahun @12% | Rp232,2 juta · payback 10,1 bulan · B/C 1,64 |
| Titik pulang pokok | realisasi manfaat 61,0% dari proyeksi |

## Catatan

* **Data vs asumsi.** Seluruh data dari kasus dipakai apa adanya. Data yang tidak tersedia
  tidak diisi angka rekaan: dinyatakan sebagai asumsi berkode A1–A15 (Lampiran 2) dan
  digantikan hasil pengukuran Fase 0 (Lampiran 5).
* **Panjang isi.** Petunjuk menyarankan 5–8 halaman isi; berkas ini berisi ±13 halaman isi
  (Bab I–VI) ditambah 6 halaman lampiran. Kedalaman analisis dipertahankan sesuai permintaan;
  tabel pendukung dan rincian perhitungan sudah dipindahkan ke lampiran. Versi yang lebih
  ringkas dapat dibuat dengan memindahkan Tabel 4.1/4.3/5.3 ke lampiran.
* **PDF vs DOCX.** PDF dirender dengan sumber huruf Times (metrik identik dengan Times New
  Roman), sehingga paginasi mendekati hasil Word; perbedaan kecil dapat terjadi pada Word.
* **Tingkat diskonto 12%** dan **harga BBM Rp10.000/liter** bersifat asumsi/simulasi sesuai
  ketentuan kasus, bukan data pasar aktual.
