#!/usr/bin/env python3
"""
tangkap_pdf.py
==============
Mengekstrak teks dari semua PDF di sebuah folder agar bisa dianalisis oleh
`analisis_dua_proposal.py`. Berguna untuk file proposal hasil ekspor (Word/LaTeX)
maupun laporan keluaran LeapSpace.

Pemakaian:
  python3 tools/tangkap_pdf.py --folder acuan --out acuan/teks
  python3 tools/tangkap_pdf.py --folder . --out teks --ringkas   # hanya cetak inventaris

Catatan:
  - PDF hasil pindai (scan) tidak punya lapisan teks; script akan menandainya
    sebagai "perlu OCR" dan tidak menghasilkan teks yang berguna.
  - Instalasi dependensi bila belum ada:  pip install --break-system-packages pypdf
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def muat_pembaca():
    for modul in ("pypdf", "PyPDF2"):
        try:
            return __import__(modul, fromlist=["PdfReader"]).PdfReader
        except ImportError:
            continue
    raise SystemExit("Modul pypdf belum terpasang. Jalankan: pip install --break-system-packages pypdf")


def bersihkan(teks: str) -> str:
    teks = teks.replace("\u00a0", " ")
    teks = re.sub(r"[ \t]+", " ", teks)
    teks = re.sub(r"\n{3,}", "\n\n", teks)
    return teks.strip()


def main() -> None:
    ap = argparse.ArgumentParser(description="Ekstrak teks dari PDF untuk analisis proposal.")
    ap.add_argument("--folder", default="acuan", help="Folder berisi PDF (default: acuan)")
    ap.add_argument("--out", default="acuan/teks", help="Folder keluaran .txt (default: acuan/teks)")
    ap.add_argument("--ringkas", action="store_true", help="Hanya cetak inventaris, tanpa menulis file")
    args = ap.parse_args()

    folder = Path(args.folder)
    if not folder.exists():
        raise SystemExit(f"Folder tidak ditemukan: {folder}")

    pdfs = sorted(p for p in folder.rglob("*.pdf") if "teks" not in p.parts)
    if not pdfs:
        raise SystemExit(f"Tidak ada berkas .pdf di {folder}. Letakkan PDF di folder itu lalu jalankan ulang perintah ini.")

    PdfReader = muat_pembaca()
    out = Path(args.out)
    if not args.ringkas:
        out.mkdir(parents=True, exist_ok=True)

    print(f"Ditemukan {len(pdfs)} PDF di {folder}:\n")
    print(f"{'no':>3}  {'berkas':<62} {'hlm':>5} {'karakter':>10}  status")
    print("-" * 100)
    inventaris = []
    for i, pdf in enumerate(pdfs, start=1):
        try:
            reader = PdfReader(str(pdf))
            teks = bersihkan("\n".join((h.extract_text() or "") for h in reader.pages))
            hlm = len(reader.pages)
        except Exception as exc:  # noqa: BLE001
            print(f"{i:>3}  {pdf.name[:60]:<62} {'-':>5} {'-':>10}  GAGAL DIBACA: {exc}")
            continue
        status = "ok" if len(teks) > 500 else "PERLU OCR (tanpa lapisan teks)"
        print(f"{i:>3}  {pdf.name[:60]:<62} {hlm:>5} {len(teks):>10,}  {status}")
        inventaris.append((pdf, teks))
        if not args.ringkas:
            tujuan = out / (pdf.stem + ".txt")
            tujuan.write_text(teks, encoding="utf-8")

    if not args.ringkas:
        print(f"\nTeks tersimpan di: {out}/  ({len(inventaris)} berkas .txt)")
        print("Langkah berikutnya: jalankan analisis tumpang-tindih, contoh:")
        print("  python3 tools/analisis_dua_proposal.py --a acuan/teks/proposal-A.txt --b acuan/teks/proposal-B.txt --out hasil")


if __name__ == "__main__":
    main()
