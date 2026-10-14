#!/usr/bin/env python3
"""
pipeline_proposal.py
====================
Deteksi otomatis berkas PDF proposal + keluaran LeapSpace dari beberapa lokasi
yang mungkin, ekstrak teksnya, lalu jalankan analisis tumpang-tindih antara
kedua dokumen proposal.

Lokasi yang dipindai (berurutan):
  1. /home/user/uploads
  2. proposal-merge/acuan
  3. root repositori
  4. folder yang diberikan lewat --folder

Pemakaian:
  python3 tools/pipeline_proposal.py                 # deteksi otomatis
  python3 tools/pipeline_proposal.py --folder /home/user/uploads
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # .../proposal-merge
REPO = ROOT.parent                                     # .../copilot-hack
LOKASI_DEFAULT = [Path("/home/user/uploads"), ROOT / "acuan", ROOT, REPO]

KATA_LEAPSPACE = ("leapspace", "leap space")


def klasifikasi(pdf: Path) -> str:
    nama = pdf.name.lower()
    if any(k in nama for k in KATA_LEAPSPACE):
        return "leapspace"
    if "proposal" in nama or "disertasi" in nama or "dissertation" in nama:
        return "proposal"
    return "lain"


def urutkan_proposal(pdfs: list[Path]) -> list[Path]:
    """Versi 'Revisi Seminar' dianggap A (hasil revisi seminar), sisanya B (versi bertanggal)."""
    def kunci(p: Path):
        n = p.name.lower()
        if "revisi" in n or "seminar" in n:
            return (0, n)
        m = re.search(r"(\d{1,2})\s*(januari|februari|maret|april|mei|juni|juli|agustus|september|oktober|november|desember)", n)
        bulan = ["januari", "februari", "maret", "april", "mei", "juni",
                 "juli", "agustus", "september", "oktober", "november", "desember"]
        if m:
            return (1, f"{int(m.group(1)):02d}-{bulan.index(m.group(2)):02d}")
        return (2, n)
    return sorted(pdfs, key=kunci)


def ekstrak(pdf: Path, tujuan: Path) -> str:
    from pypdf import PdfReader
    teks = "\n".join((h.extract_text() or "") for h in PdfReader(str(pdf)).pages)
    teks = teks.replace("\u00a0", " ")
    teks = re.sub(r"[ \t]+", " ", teks)
    teks = re.sub(r"\n{3,}", "\n\n", teks).strip()
    tujuan.parent.mkdir(parents=True, exist_ok=True)
    tujuan.write_text(teks, encoding="utf-8")
    return teks


def siapkan_zip(scan: list[Path]) -> Path | None:
    """Bila pengguna mengunggah satu berkas .zip berisi PDF, ekstrak dan ratakan isinya."""
    import zipfile

    tujuan = ROOT / "acuan" / "dari-zip"
    ketemu = False
    for folder in scan:
        if not folder.is_dir():
            continue
        for zpath in sorted(folder.glob("*.zip")):
            tujuan.mkdir(parents=True, exist_ok=True)
            with zipfile.ZipFile(zpath) as z:
                for nama in z.namelist():
                    if nama.lower().endswith(".pdf") and not nama.startswith("__MACOSX"):
                        berkas = Path(nama).name          # ratakan struktur folder di dalam ZIP
                        with z.open(nama) as sumber, (tujuan / berkas).open("wb") as keluar:
                            keluar.write(sumber.read())
                        print(f"  dari ZIP: {berkas}")
                        ketemu = True
    return tujuan if ketemu else None


def tarik_dari_git(ref: str, tujuan: Path) -> Path:
    """Ambil berkas PDF/ZIP dari sebuah ref git (mis. origin/main) ke folder kerja lokal."""
    import tarfile
    import tempfile

    tujuan.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryFile() as tmp:
        proses = subprocess.run(["git", "archive", ref], cwd=REPO, stdout=tmp, stderr=subprocess.PIPE)
        if proses.returncode != 0:
            raise SystemExit(f"Gagal mengambil '{ref}': {proses.stderr.decode(errors='replace').strip()}")
        tmp.seek(0)
        jumlah = 0
        with tarfile.open(fileobj=tmp) as tar:
            for anggota in tar.getmembers():
                if not (anggota.isfile() and anggota.name.lower().endswith((".pdf", ".zip"))):
                    continue
                nama = Path(anggota.name).name              # ratakan struktur folder
                sumber = tar.extractfile(anggota)
                if sumber is None:
                    continue
                (tujuan / nama).write_bytes(sumber.read())
                print(f"  dari {ref}: {nama}")
                jumlah += 1
        if not jumlah:
            print(f"  (tidak ada berkas PDF/ZIP pada {ref})")
    return tujuan


def main() -> None:
    ap = argparse.ArgumentParser(description="Pipeline deteksi + analisis berkas proposal disertasi.")
    ap.add_argument("--folder", action="append", default=[], help="Folder tambahan untuk dipindai")
    ap.add_argument("--dari-git", help="Ambil PDF/ZIP dari ref git, mis. origin/main")
    ap.add_argument("--out", default=str(ROOT / "hasil"), help="Folder keluaran")
    args = ap.parse_args()

    lokasi = [Path(f) for f in args.folder] + LOKASI_DEFAULT

    if args.dari_git:
        print(f"Mengambil berkas dari git: {args.dari_git}")
        lokasi.insert(0, tarik_dari_git(args.dari_git, REPO / "unggahan"))
        print()

    tujuan_zip = siapkan_zip(lokasi)
    if tujuan_zip:
        lokasi.insert(0, tujuan_zip)
    terlihat: dict[Path, Path] = {}
    for folder in lokasi:
        if not folder.exists():
            continue
        for pdf in sorted(folder.glob("*.pdf")):
            terlihat.setdefault(pdf.resolve(), pdf)

    if not terlihat:
        print("Tidak ada berkas PDF yang ditemukan di lokasi berikut:")
        for folder in lokasi:
            print(f"  - {folder} {'(tidak ada)' if not folder.exists() else ''}")
        print("\nLetakkan PDF di salah satu lokasi di atas, atau unggah ke repo GitHub ini,")
        print("lalu jalankan ulang perintah ini.")
        sys.exit(1)

    proposal = urutkan_proposal([p for p in terlihat.values() if klasifikasi(p) == "proposal"])
    leap = [p for p in terlihat.values() if klasifikasi(p) == "leapspace"]
    lain = [p for p in terlihat.values() if klasifikasi(p) == "lain"]

    print(f"Terdeteksi {len(terlihat)} PDF:")
    for p in proposal:
        print(f"  [proposal]  {p.name}")
    for p in leap:
        print(f"  [leapspace] {p.name}")
    for p in lain:
        print(f"  [lain-lain] {p.name}")
    print()

    if len(proposal) < 2:
        print(f"PERINGATAN: hanya {len(proposal)} berkas proposal terdeteksi; analisis tumpang-tindih butuh 2 berkas.")
        if leap:
            print("Keluaran LeapSpace tetap akan diekstrak ke teks untuk dijadikan acuan revisi.")

    out = Path(args.out)
    teks_dir = out / "teks"
    hasil_ekstraksi: dict[str, Path] = {}
    for pdf in proposal + leap + lain:
        tujuan = teks_dir / (pdf.stem + ".txt")
        teks = ekstrak(pdf, tujuan)
        status = "ok" if len(teks) > 500 else "PERLU OCR"
        print(f"  ekstrak {pdf.name[:58]:<60} {len(teks):>9,} karakter  {status}")
        if pdf in proposal:
            hasil_ekstraksi[pdf.stem] = tujuan
    print()

    if len(proposal) >= 2:
        a, b = hasil_ekstraksi[proposal[0].stem], hasil_ekstraksi[proposal[1].stem]
        print("Menjalankan analisis tumpang-tindih...\n")
        subprocess.run(
            [sys.executable, str(ROOT / "tools" / "analisis_dua_proposal.py"),
             "--a", str(a), "--b", str(b),
             "--out", str(out), "--nama-a", proposal[0].stem, "--nama-b", proposal[1].stem],
            check=False)
        print(f"\nSelesai. Buka {out / 'laporan-tumpang-tindih.md'}")
    else:
        print(f"Teks tersimpan di {teks_dir}/")

    if leap:
        print("\nAcuan LeapSpace yang siap dibaca:")
        for pdf in leap:
            print(f"  - {teks_dir / (pdf.stem + '.txt')}")


if __name__ == "__main__":
    main()
