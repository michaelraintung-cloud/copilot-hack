"""Pipeline produksi laporan dua tahap.

Tahap 1: bangun DOCX tanpa daftar isi, render PDF, ekstrak halaman tiap heading.
Tahap 2: bangun ulang DOCX dengan daftar isi berisi nomor halaman hasil tahap 1,
         render PDF lagi, lalu verifikasi bahwa nomor halaman sudah konsisten.

Jalankan:  python3 build_all.py
"""
import json
import os
import re
import subprocess
import sys

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output")
DOCX = os.path.join(OUT, "laporan-studi-kasus-4.docx")
PDF = os.path.join(OUT, "laporan-studi-kasus-4.pdf")
LAYOUT = os.path.join(OUT, "laporan-studi-kasus-4.layout.json")
TOC = os.path.join(OUT, "toc-entries.json")


def run(script):
    subprocess.run([sys.executable, os.path.join(HERE, script)], check=True,
                   stdout=subprocess.DEVNULL)


def norm(t):
    return re.sub(r"\s+", " ", t).strip().lower()


def heading_pages():
    """Petakan setiap heading (dari log layout) ke nomor halaman pada PDF."""
    with open(LAYOUT, encoding="utf-8") as f:
        log = json.load(f)
    doc = pymupdf.open(PDF)
    raw = [norm(p.get_text()) for p in doc]
    doc.close()
    # halaman daftar isi memuat semua judul -> harus dikecualikan dari pencarian
    pages, nomor = [], []
    for i, t in enumerate(raw):
        if "daftarisi" in t.replace(" ", "")[:200] and "ringkasan" not in t:
            continue
        pages.append(t)
        nomor.append(i + 1)

    heads = []
    for blk in log:
        if blk["t"] == "h":
            heads.append((blk["level"], blk["text"]))

    out, start = [], 0
    for lvl, text in heads:
        needle = norm(text)
        found = None
        for i in range(start, len(pages)):
            if needle and needle in pages[i]:
                found = nomor[i]
                break
        if found is None:                      # cari mundur bila tidak ketemu
            for i in range(len(pages) - 1, -1, -1):
                if needle and needle in pages[i]:
                    found = nomor[i]
                    break
        if found is not None:
            start = found - 1
            out.append([lvl, text, found])
    return out


def main():
    # ---------- tahap 1: tanpa daftar isi
    if os.path.exists(TOC):
        os.remove(TOC)
    run("build_report.py"); run("render_pdf.py")
    first = heading_pages()
    print(f"tahap 1: {len(first)} heading, {pymupdf.open(PDF).page_count} halaman")

    # daftar isi akan menempati halaman tambahan -> geser nomor halaman heading
    with open(TOC, "w", encoding="utf-8") as f:
        json.dump([[lvl, txt, pg] for lvl, txt, pg in first], f, ensure_ascii=False)

    # ---------- tahap 2: dengan daftar isi
    run("build_report.py"); run("render_pdf.py")
    second = heading_pages()
    print(f"tahap 2: {len(second)} heading, {pymupdf.open(PDF).page_count} halaman")

    # ---------- kalibrasi: tulis nomor halaman nyata, lalu ulangi sampai stabil
    with open(TOC, "w", encoding="utf-8") as f:
        json.dump([[lvl, txt, pg] for lvl, txt, pg in second], f, ensure_ascii=False)

    sebelumnya = second
    for it in range(1, 5):
        run("build_report.py"); run("render_pdf.py")
        kini = heading_pages()
        sama = ([(l, p) for l, _, p in kini] == [(l, p) for l, _, p in sebelumnya])
        print(f"iterasi {it}: {pymupdf.open(PDF).page_count} halaman, stabil = {sama}")
        if sama:
            break
        sebelumnya = kini
        with open(TOC, "w", encoding="utf-8") as f:
            json.dump([[lvl, txt, pg] for lvl, txt, pg in kini], f, ensure_ascii=False)

    tercetak = {norm(t): p for _, t, p in json.load(open(TOC, encoding="utf-8"))}
    akurat = all(tercetak.get(norm(t)) == p for _, t, p in sebelumnya)
    print("daftar isi akurat:", akurat)

    print("selesai:", PDF)


if __name__ == "__main__":
    main()
