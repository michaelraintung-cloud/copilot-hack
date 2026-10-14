#!/usr/bin/env python3
"""
rapikan_tabel.py — merapikan tabel pada naskah gabungan.

Masalah yang diperbaiki:
  1. Tabel asli berkas A (induk) terekstrak sebagai teks gepeng (kolom berimpit),
     karena PDF hasil ekspor kehilangan struktur tabel. Tabel direkonstruksi
     ulang dari PDF sumber memakai deteksi geometris PyMuPDF.
  2. Empat tabel A merupakan duplikat tabel hasil transplantasi dari berkas B/C
     (judul dan isi sama) sehingga muncul dua kali.
  3. Seluruh tabel dinomori ulang mengikuti urutan kemunculan dalam naskah.

Masukan/keluaran : hasil/proposal-gabungan.md (dirapikan di tempat)
Prasyarat        : pip install --break-system-packages pymupdf

Pemakaian:
  python3 tools/rapikan_tabel.py
  python3 tools/rapikan_tabel.py --uji     # hanya laporkan, tidak menulis
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

try:
    import pymupdf
except ImportError:  # pragma: no cover
    sys.exit("PyMuPDF belum terpasang: pip install --break-system-packages pymupdf")

DIR = pathlib.Path(__file__).resolve().parent.parent
NASKAH = DIR / "hasil" / "proposal-gabungan.md"
PDF_A = DIR.parent / "google_drive" / "Proposal Disertasi Michael Raintung - Revisi Seminar Proposal.pdf"

# Tabel A yang direkonstruksi dari PDF: (judul pada naskah, halaman, penanda baris kepala)
REKONSTRUKSI = [
    ("Sintesis bukti empiris utama", [(41, "Penulis")]),
    ("Ringkasan hipotesis penelitian", [(59, "Hipotesis"), (60, "H2")]),
    ("Operasionalisasi konstruk penelitian", [(67, "Konstruk utama")]),
    ("Sumber konseptual dan status penelusuran item", [(69, "Kode item"), (70, "AM1")]),
    ("Tahapan penilaian dan uji instrumen", [(73, "Tahap")]),
    ("Rencana biaya penelitian", [(99, "No.")]),
    ("Jadwal pelaksanaan penelitian", [(100, "Kegiatan")]),
]

# Tabel A yang dibuang karena duplikat tabel transplantasi (judul, halaman sumber)
DIBUANG = [
    ("Kesenjangan penelitian dan keputusan desain", [(47, "Jenis")]),
    ("Pemetaan dimensi dan isi indikator", [(68, "Kelompok"), (69, "Berbagi")]),
    ("Acuan evaluasi model pengukuran", [(78, "Aspek")]),
    ("Kriteria pengujian hipotesis", [(80, "Hipotesis")]),
]

CAPTION = re.compile(r"^\*{0,2}Tabel\s+\d+[a-z]?\.\s+(.+?)\*{0,2}\s*$")
CAPTION_FINAL = re.compile(r"^\*\*Tabel\s+(?:\d+|X)\.\s+.+\*\*$")


def norm(t: str) -> str:
    return re.sub(r"[^0-9A-Za-zÀ-ÿ]+", "", t).lower()


def sel(pymupdf_cell) -> str:
    return " ".join((pymupdf_cell or "").split())


def ambil_tabel(pdf: pymupdf.Document, hal: int, penanda: str) -> list[list[str]]:
    """Ambil satu tabel dari halaman tertentu, dipilih berdasarkan penanda baris kepala."""
    for t in pdf[hal].find_tables().tables:
        baris = t.extract()
        if baris and penanda.lower() in sel(baris[0][0]).lower():
            return [[sel(c) for c in r] for r in baris]
    raise SystemExit(f"Tabel dengan penanda {penanda!r} tidak ditemukan di halaman {hal}")


def md_tabel(baris: list[list[str]]) -> list[str]:
    """Ubah matriks sel menjadi baris-baris tabel markdown."""
    lebar = max(len(r) for r in baris)
    baris = [list(r) + [""] * (lebar - len(r)) for r in baris]
    kepala = baris[0]
    isi = baris[1:]
    out = ["| " + " | ".join(kepala) + " |", "|" + "---|" * lebar]
    for r in isi:
        out.append("| " + " | ".join(r) + " |")
    return out


def skor_di_dalam(blok: str, teks: str, jendela: int = 30) -> float:
    """Fraksi jendela karakter blok yang ditemukan pada teks tabel (keduanya tanpa spasi)."""
    b = norm(blok)
    if not b:
        return 0.0
    if len(b) < jendela:
        return 1.0 if b in teks else 0.0
    total = cocok = 0
    for s in range(0, len(b) - jendela + 1, 15):
        total += 1
        if b[s:s + jendela] in teks:
            cocok += 1
    return cocok / max(1, total)


def batas_blob(baris_md: list[str], i_kaption: int, teks_tabel: str, maks: int = 40) -> int:
    """Banyak baris setelah baris kaption yang masih merupakan bagian tabel gepeng."""
    k = 0
    for kk in range(1, maks + 1):
        j = i_kaption + kk
        if j >= len(baris_md):
            break
        l = baris_md[j]
        if l.startswith("#") or l.startswith("**Tabel") or (l.startswith("*") and l.rstrip().endswith("*")):
            break
        if not l.strip():
            break
        if skor_di_dalam(l, teks_tabel) >= 0.42:
            k = kk
        else:
            break
    return k


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--uji", action="store_true", help="laporkan saja, jangan tulis berkas")
    ap.add_argument("--masuk", default=str(NASKAH))
    args = ap.parse_args()

    masuk = pathlib.Path(args.masuk)
    baris_md = masuk.read_text(encoding="utf-8").splitlines()
    pdf = pymupdf.open(PDF_A)

    # ---------------------------------------------------------------- bangun tabel pengganti
    def matriks_dari(halaman: list[tuple[int, str]]) -> list[list[str]]:
        matriks: list[list[str]] = []
        for n, (hal, penanda) in enumerate(halaman):
            blok = ambil_tabel(pdf, hal, penanda)
            matriks.extend(blok if n == 0 else blok)       # halaman lanjutan: baris isi saja
        return matriks

    pengganti: list[tuple[str, list[str], str]] = []      # (judul, baris markdown, teks tabel)
    for judul, halaman in REKONSTRUKSI:
        matriks = matriks_dari(halaman)
        teks = norm(" ".join(k for r in matriks for k in r))
        pengganti.append((judul, md_tabel(matriks), teks))

    buang: list[tuple[str, str]] = []                     # (judul, teks tabel duplikat)
    for judul, halaman in DIBUANG:
        teks = norm(" ".join(k for r in matriks_dari(halaman) for k in r))
        buang.append((judul, teks))

    # ---------------------------------------------------------------- rapikan naskah
    out: list[str] = []
    laporan: list[str] = []
    i = 0
    while i < len(baris_md):
        l = baris_md[i]
        if l.startswith("**Tabel"):                        # kaption tabel final → jangan disentuh
            out.append(l)
            i += 1
            continue
        m = CAPTION.match(re.sub(r"^\s*[-•]\s+", "", l))
        if m:
            judul = m.group(1).strip().rstrip("*").strip()
            kandidat = next((p for p in pengganti if norm(p[0]) == norm(judul)), None)
            if kandidat:
                judul, tabel_md, teks = kandidat
                k = batas_blob(baris_md, i, teks)
                out += [f"**Tabel X. {judul}**", ""] + tabel_md + [""]
                laporan.append(f"REKONSTRUKSI  {judul}  (buang {k} baris teks gepeng → {len(tabel_md) - 2} baris isi)")
                i += k + 1
                continue
            kandidat_buang = next((b for b in buang if norm(b[0]) == norm(judul)), None)
            if kandidat_buang:
                k = batas_blob(baris_md, i, kandidat_buang[1])
                laporan.append(f"DIBUANG       {judul}  (duplikat tabel transplantasi; {k + 1} baris)")
                i += k + 1
                continue
        out.append(l)
        i += 1

    # ---------------------------------------------------------------- nomori ulang tabel
    out = [re.sub(r"\(Tabel (\d+)\)", r"(tabel \1 pada berkas sumber)", l)
           if l.startswith("*Diadaptasi dari berkas") else l for l in out]
    nomor = 0
    final: list[str] = []
    for l in out:
        if CAPTION_FINAL.match(l):
            nomor += 1
            l = re.sub(r"^\*\*Tabel\s+(?:\d+|X)\.\s+", f"**Tabel {nomor}. ", l)
        final.append(l)

    if not args.uji:
        masuk.write_text("\n".join(final) + "\n", encoding="utf-8")

    print(f"Tabel akhir: {nomor}")
    for x in laporan:
        print("  " + x)
    print("\nUrutan tabel pada naskah:")
    for l in final:
        if CAPTION_FINAL.match(l):
            print("  " + l.strip("*"))
    if args.uji:
        print("\n(--uji: berkas tidak diubah)")


if __name__ == "__main__":
    main()
