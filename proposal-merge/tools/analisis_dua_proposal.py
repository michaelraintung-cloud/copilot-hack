#!/usr/bin/env python3
"""
analisis_dua_proposal.py
========================
Menganalisis DUA dokumen proposal (A dan B) untuk menjawab tiga pertanyaan:
  1. Komponen proposal apa yang ada di masing-masing file dan mana yang kosong di keduanya?
  2. Di mana isi kedua file tumpang-tindih (duplikat) dan di mana saling melengkapi?
  3. Di mana letak konflik yang WAJIB diputuskan manusia sebelum digabung?

Keluaran (default ke ./hasil/):
  - laporan-tumpang-tindih.md   ringkasan untuk dibaca manusia (buka file ini dulu)
  - pemetaan-seksi.csv          matriks 18 komponen x {A, B} + rekomendasi
  - daftar-duplikat.md          pasangan paragraf yang mirip + versi mana yang disarankan dipakai
  - daftar-konflik.md           topik yang muncul di A dan B tapi isinya berbeda (angka/desain/RQ)
  - kerangka-gabungan.md        kerangka proposal gabungan dengan penanda asal isi [A]/[B]/[A+B]/[BARU]

Pemakaian:
  python3 analisis_dua_proposal.py --a FILE_A --b FILE_B [--out hasil]
  python3 analisis_dua_proposal.py --a proposal_v1.docx --b rencana_penelitian.pdf --nama-a "Pembimbing 1" --nama-b "Pembimbing 2"

Dukungan format: .txt .md .docx (dan .pdf bila `pypdf` terpasang: pip install pypdf)
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
import zipfile
from dataclasses import dataclass, field
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path

# ---------------------------------------------------------------------------
# 18 komponen proposal: kata kunci + pola judul seksi + saran bila hilang
# ---------------------------------------------------------------------------
@dataclass
class Komponen:
    no: int
    nama: str
    prioritas: str
    kata_kunci: tuple[str, ...]
    pola_judul: tuple[str, ...]
    saran_bila_hilang: str


KOMPONEN: list[Komponen] = [
    Komponen(2, "Ringkasan eksekutif / abstrak", "Tinggi",
             ("abstrak", "abstract", "ringkasan", "executive summary", "sinopsis"),
             (r"abstrak", r"abstract", r"ringkasan", r"sinopsis", r"executive summary"),
             "Susun abstrak 250-400 kata: masalah, gap, tujuan, metode, luaran yang diharapkan."),
    Komponen(1, "Halaman informasi & judul", "Rendah",
             ("judul", "title", "kata kunci", "keywords", "nim", "program studi", "pembimbing", "identitas"),
             (r"(halaman )?judul", r"title", r"lembar identitas", r"kata kunci", r"identitas"),
             "Tulis halaman informasi: judul (<=20 kata), identitas, pembimbing, program, tanggal versi."),
    Komponen(4, "Rumusan masalah / problem statement", "Tinggi",
             ("rumusan masalah", "problem statement", "identifikasi masalah", "permasalahan penelitian"),
             (r"rumusan masalah", r"identifikasi masalah", r"problem statement", r"permasalahan penelitian", r"masalah penelitian"),
             "Tulis problem statement sebagai kesenjangan kondisi ideal vs kondisi nyata, dengan konsekuensinya."),
    Komponen(5, "Analisis gap & kebaruan penelitian", "Sangat tinggi",
             ("gap", "novelty", "kebaruan", "state of the art", "belum diteliti", "research gap", "celah penelitian", "posisi penelitian"),
             (r"kebaruan", r"novelty", r"gap penelitian", r"analisis gap", r"research gap", r"state of the art", r"posisi penelitian"),
             "Buat tabel gap 3 kolom: sudah diteliti -> belum terjawab -> bagaimana riset ini menjawab (lacak ke RQ)."),
    Komponen(7, "Pertanyaan penelitian & hipotesis", "Sangat tinggi",
             ("pertanyaan penelitian", "research question", "rumusan pertanyaan", "hipotesis", "proposisi penelitian"),
             (r"pertanyaan penelitian", r"research question", r"hipotesis", r"rumusan pertanyaan", r"research questions"),
             "Tetapkan SATU set pertanyaan penelitian (maks 4) + hipotesis/proposisi yang 1:1 dengannya."),
    Komponen(8, "Tujuan & sasaran", "Tinggi",
             ("tujuan penelitian", "tujuan umum", "tujuan khusus", "objective", "sasaran penelitian"),
             (r"tujuan", r"objective", r"sasaran penelitian", r"tujuan dan"),
             "Buat tujuan umum + tujuan khusus yang 1:1 dengan pertanyaan penelitian."),
    Komponen(6, "Urgensi & signifikansi", "Sedang",
             ("signifikansi", "kontribusi", "manfaat penelitian", "urgensi", "significance", "kegunaan penelitian"),
             (r"urgensi", r"signifikansi", r"kontribusi penelitian", r"manfaat penelitian", r"significance"),
             "Sebutkan kontribusi teoretis, praktis, dan kebijakan secara spesifik + pemangku kepentingannya."),
    Komponen(9, "Batasan & definisi operasional", "Sedang",
             ("definisi operasional", "ruang lingkup", "batasan penelitian", "operational definition", "glosarium", "definisi istilah", "batasan istilah"),
             (r"batasan penelitian", r"ruang lingkup", r"definisi operasional", r"glosarium", r"definisi istilah", r"batasan istilah"),
             "Tambah ruang lingkup + definisi operasional setiap variabel yang bisa diukur + glosarium istilah."),
    Komponen(14, "Keterbatasan & asumsi", "Rendah",
             ("keterbatasan penelitian", "limitasi", "limitations", "asumsi penelitian", "ancaman validitas"),
             (r"keterbatasan", r"limitasi", r"limitations", r"asumsi penelitian", r"keterbatasan dan asumsi"),
             "Nyatakan keterbatasan desain, batas generalisasi, asumsi, dan mitigasinya."),
    Komponen(10, "Kerangka teori & kajian pustaka", "Tinggi",
             ("kerangka teori", "kajian pustaka", "tinjauan pustaka", "landasan teori", "literature review", "penelitian terdahulu", "studi terdahulu", "kajian teori", "teori yang digunakan", "teori utama"),
             (r"kajian pustaka", r"tinjauan pustaka", r"landasan teori", r"kerangka teori", r"literature review", r"penelitian terdahulu", r"studi terdahulu", r"teori yang digunakan", r"kajian teori"),
             "Susun kerangka teori: teori utama + teori pendukung/pesaing + posisi riset ini terhadap keduanya."),
    Komponen(11, "Kerangka berpikir & model konseptual", "Tinggi",
             ("kerangka berpikir", "kerangka konseptual", "model konseptual", "conceptual framework", "model penelitian", "kerangka penelitian", "hubungan antar variabel"),
             (r"kerangka berpikir", r"kerangka konseptual", r"model konseptual", r"conceptual framework", r"model penelitian", r"kerangka penelitian"),
             "Buat satu diagram kerangka berpikir; setiap panah diberi dasar pustaka."),
    Komponen(12, "Metodologi", "Sangat tinggi",
             ("metode penelitian", "metodologi", "desain penelitian", "populasi", "sampel", "sampling", "instrumen", "kuesioner", "wawancara", "analisis data", "validitas", "reliabilitas", "mixed method", "kualitatif", "kuantitatif"),
             (r"metode", r"metodologi", r"desain penelitian", r"populasi", r"sampel", r"instrumen", r"analisis data", r"method", r"research method", r"teknik pengumpulan"),
             "Lengkapi metodologi hingga bisa direplikasi: desain, sampel + justifikasi ukuran, instrumen (uji validitas/reliabilitas), prosedur, analisis."),
    Komponen(13, "Etika penelitian & perlindungan data", "Sedang",
             ("etika penelitian", "informed consent", "ethical clearance", "kerahasiaan", "confidentiality", "izin penelitian", "pelindungan data pribadi", "kode etik"),
             (r"etika", r"pertimbangan etik", r"ethical", r"isu etik", r"perlindungan data", r"pelindungan data"),
             "Tambah bagian etika: izin etik/ethical clearance, informed consent, penyimpanan data (UU PDP), benturan kepentingan."),
    Komponen(15, "Rencana luaran & diseminasi", "Sedang",
             ("luaran penelitian", "rencana luaran", "publikasi", "diseminasi", "konferensi", "jurnal", "hki", "policy brief", "dampak penelitian"),
             (r"luaran", r"rencana luaran", r"output", r"publikasi", r"diseminasi", r"dampak penelitian", r"target luaran"),
             "Sebut target luaran spesifik bernama (jurnal/konferensi) beserta waktu perkiraannya."),
    Komponen(16, "Jadwal, milestone & manajemen risiko", "Tinggi",
             ("jadwal penelitian", "timeline", "gantt", "milestone", "tahapan penelitian", "rencana kerja", "manajemen risiko", "risiko penelitian"),
             (r"jadwal", r"timeline", r"gantt", r"rencana kerja", r"tahapan", r"milestone", r"manajemen risiko"),
             "Buat jadwal per triwulan + milestone review + risk register (risiko, dampak, mitigasi)."),
    Komponen(17, "Anggaran & sumber daya", "Rendah",
             ("anggaran penelitian", "budget", "biaya penelitian", "dana penelitian", "pendanaan", "hibah"),
             (r"anggaran", r"budget", r"biaya penelitian", r"sumber daya", r"pendanaan", r"rincian biaya"),
             "Susun rincian anggaran yang konsisten dengan metode & jadwal yang dipilih."),
    Komponen(3, "Latar belakang & konteks", "Tinggi",
             ("latar belakang", "pendahuluan", "background", "introduction", "konteks penelitian", "fenomena", "kesenjangan"),
             (r"latar belakang", r"pendahuluan", r"background", r"introduction", r"konteks"),
             "Tulis latar belakang dengan data/fakta terbaru <=5 tahun dan sumber yang jelas."),
    Komponen(18, "Daftar pustaka & lampiran", "Sedang",
             ("daftar pustaka", "referensi", "references", "bibliografi", "lampiran", "appendix"),
             (r"daftar pustaka", r"referensi", r"references", r"bibliografi", r"lampiran", r"appendix"),
             "Satukan daftar pustaka (hapus entri ganda, selesaikan sitasi yatim), lampirkan instrumen & surat izin."),
]

# Urutan pemeriksaan judul: komponen yang lebih spesifik lebih dulu
URUTAN_JUDUL = [2, 4, 5, 7, 8, 6, 9, 14, 10, 11, 12, 13, 15, 16, 17, 3, 18, 1]

# Penanda konflik: nilai yang berbeda antar dua file
PENANDA_KONFLIK: dict[str, re.Pattern] = {
    "Angka sampel/responden": re.compile(
        r"\b(?:n\s*=\s*\d+|\d{2,5}\s*(?:responden|sampel|partisipan|subjek|informan|siswa|mahasiswa|guru|karyawan))",
        re.IGNORECASE),
    "Durasi penelitian": re.compile(r"\b\d{1,2}\s*(?:bulan|tahun|minggu)\b|\bselama\s+\d+", re.IGNORECASE),
    "Jumlah item instrumen": re.compile(
        r"\b\d{1,4}\s*(?:item|butir|pertanyaan|pernyataan)\b", re.IGNORECASE),
    "Anggaran": re.compile(r"\brp\.?\s?[\d.,]+|\bidr\s?[\d.,]+|\busd\s?[\d.,]+", re.IGNORECASE),
    "Metode yang dianut": re.compile(
        r"\b(?:kualitatif|kuantitatif|mixed[- ]methods?|eksperimen|survei|survey|studi kasus|etnografi|fenomenologi|"
        r"grounded theory|action research|longitudinal|cross[- ]sectional|regresi|anova|sem\b|pls|smartpls|"
        r"partial least squares|korelasional|deskriptif|r&d)\b", re.IGNORECASE),
}

PANJANG_MIN_KATA = 12


# ---------------------------------------------------------------------------
# Ekstraksi teks
# ---------------------------------------------------------------------------
def baca_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="replace")
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"</w:tc>", "\t", xml)
    xml = re.sub(r"</w:tr>", "\n", xml)
    teks = re.sub(r"<[^>]+>", "", xml)
    for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'")):
        teks = teks.replace(a, b)
    return teks


def baca_pdf(path: Path) -> str:
    reader_cls = None
    for modul in ("pypdf", "PyPDF2"):
        try:
            reader_cls = __import__(modul, fromlist=["PdfReader"]).PdfReader
            break
        except ImportError:
            continue
    if reader_cls is None:
        raise SystemExit(
            f"File '{path.name}' berformat PDF. Pasang dulu: pip install pypdf\n"
            "Alternatif: konversi PDF ke .docx atau .txt terlebih dahulu."
        )
    return "\n".join((h.extract_text() or "") for h in reader_cls(str(path)).pages)


def baca_dokumen(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"File tidak ditemukan: {path}")
    suffix = path.suffix.lower()
    if suffix == ".docx":
        return baca_docx(path)
    if suffix == ".pdf":
        return baca_pdf(path)
    if suffix == ".doc":
        raise SystemExit(f"Format .doc lama tidak didukung langsung. Simpan ulang '{path.name}' sebagai .docx lalu jalankan lagi.")
    return path.read_text(encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Normalisasi, blok, dan deteksi seksi
# ---------------------------------------------------------------------------
def normalisasi(teks: str) -> str:
    teks = unicodedata.normalize("NFKC", teks).replace("\u00a0", " ").lower()
    teks = re.sub(r"[^\w\s%.,/=\-]", " ", teks)
    return re.sub(r"\s+", " ", teks).strip()


@dataclass
class Blok:
    id: str
    teks: str
    normal: str
    baris: int
    komponen: int | None = None

    @property
    def kata(self) -> int:
        return len(self.normal.split())

    @property
    def potongan(self) -> set[str]:
        k = self.normal.split()
        return {" ".join(k[i:i + 4]) for i in range(max(0, len(k) - 3))}


@dataclass
class Dokumen:
    label: str
    path: Path
    teks: str
    blok: list[Blok] = field(default_factory=list)
    judul_seksi: list[tuple[int, str, int]] = field(default_factory=list)  # (komponen, judul, baris)
    cakupan: dict[int, dict] = field(default_factory=dict)
    fitur: dict[str, list[str]] = field(default_factory=dict)


def bersihkan_judul(baris: str) -> str:
    b = baris.strip().lstrip("#*•-–").strip()
    b = re.sub(r"(?:bab|bagian|chapter)\s+[ivxlcdm\d]+\s*[:.\-]?\s*", "", b, flags=re.IGNORECASE)
    b = re.sub(r"\d+(?:\.\d+)*\.?\s*", "", b)
    return b.strip(" .:;").lower()


def cocokkan_judul(baris: str) -> list[int]:
    """Kembalikan semua komponen yang cocok dengan judul seksi.

    Judul gabungan seperti "Etika dan Keterbatasan" sengaja dicatat untuk dua komponen
    sekaligus, karena bagian itu memang membahas dua hal.
    """
    b = bersihkan_judul(baris)
    if not b or len(b) > 90:
        return []
    cocok: list[int] = []
    for no in URUTAN_JUDUL:
        k = next(x for x in KOMPONEN if x.no == no)
        if any(re.search(pola, b) for pola in k.pola_judul):
            cocok.append(no)
        if len(cocok) == 3:
            break
    return cocok


def pecah_dokumen(doc: Dokumen) -> None:
    """Pecah menjadi paragraf (blok) dan catat judul seksi yang dikenali."""
    paragraf: list[tuple[int, str]] = []
    for i, baris in enumerate(doc.teks.split("\n"), start=1):
        b = baris.strip()
        if b:
            paragraf.append((i, b))

    blok: list[Blok] = []
    pending: tuple[int, str] | None = None
    for baris_ke, isi in paragraf:
        komp_list = cocokkan_judul(isi)
        if komp_list:
            for komp in komp_list:
                doc.judul_seksi.append((komp, isi.strip(), baris_ke))
            pending = (baris_ke, isi.strip())
            continue
        kalimat = isi
        baris_blok = baris_ke
        if pending and normalisasi(pending[1]) not in normalisasi(kalimat):
            kalimat = f"{pending[1]} — {kalimat}"
            baris_blok = pending[0]
            pending = None
        blk = Blok(f"{doc.label}-{len(blok)+1:03d}", kalimat, normalisasi(kalimat), baris_blok)
        if blk.kata >= PANJANG_MIN_KATA:
            blok.append(blk)
        elif len(blok) > 0:
            blok[-1] = Blok(blok[-1].id, f"{blok[-1].teks} {kalimat}", normalisasi(f"{blok[-1].teks} {kalimat}"), blok[-1].baris)
    doc.blok = blok

    # klasifikasi tiap paragraf ke komponen berbasis kata kunci (maks 2 komponen terkuat)
    for b in doc.blok:
        skor = {}
        for k in KOMPONEN:
            s = sum(1 for kw in k.kata_kunci if kw in b.normal)
            if s:
                skor[k.no] = s
        if skor:
            b.komponen = max(skor, key=lambda n: skor[n])

    # deteksi judul seksi lewat juga paragraf pendek yang bukan hasil regex
    for b in doc.blok:
        if b.kata < 25:
            for komp in cocokkan_judul(b.teks):
                if all(not (h[0] == komp and h[1] == b.teks.strip()) for h in doc.judul_seksi):
                    doc.judul_seksi.append((komp, b.teks.strip(), b.baris))

    # cakupan per komponen: bukti = judul seksi ATAU minimal 2 paragraf berisi kata kunci
    for k in KOMPONEN:
        judul = [(h, baris) for no, h, baris in doc.judul_seksi if no == k.no]
        paragraf_komp = [b for b in doc.blok if b.komponen == k.no]
        hit = sum(1 for kw in k.kata_kunci if kw in normalisasi(doc.teks))
        ada = bool(judul) or len(paragraf_komp) >= 2 or (len(paragraf_komp) >= 1 and hit >= 3)
        doc.cakupan[k.no] = {"ada": ada, "judul": judul, "paragraf": paragraf_komp, "kata_kunci_cocok": hit}

    # fitur untuk deteksi konflik
    for nama, pola in PENANDA_KONFLIK.items():
        nilai = {normalisasi(m.group(0)) for m in pola.finditer(doc.teks)}
        doc.fitur[nama] = sorted(v for v in nilai if v)


# ---------------------------------------------------------------------------
# Perbandingan
# ---------------------------------------------------------------------------
def kemiripan(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def jaccard(pa: set[str], pb: set[str]) -> float:
    return len(pa & pb) / len(pa | pb) if pa and pb else 0.0


@dataclass
class PasanganMirip:
    a: Blok
    b: Blok
    skor: float
    status: str


def bandingkan(a: Dokumen, b: Dokumen, ambang_dup: float = 0.45, ambang_identik: float = 0.85) -> list[PasanganMirip]:
    hasil: list[PasanganMirip] = []
    for ba in a.blok:
        for bb in b.blok:
            j = jaccard(ba.potongan, bb.potongan)
            s = kemiripan(ba.normal, bb.normal)
            skor = max(s, j)
            if skor >= ambang_dup:
                hasil.append(PasanganMirip(
                    ba, bb, round(skor, 3),
                    "hampir identik" if skor >= ambang_identik else "duplikat"))
    hasil.sort(key=lambda p: -p.skor)
    return hasil


def deteksi_konflik(a: Dokumen, b: Dokumen) -> list[tuple[str, list[str], list[str]]]:
    konflik = []
    for nama in PENANDA_KONFLIK:
        sa, sb = set(a.fitur.get(nama, [])), set(b.fitur.get(nama, []))
        if not (sa and sb):
            continue
        hanya_a, hanya_b = sorted(sa - sb), sorted(sb - sa)
        if hanya_a or hanya_b:
            konflik.append((nama, hanya_a, hanya_b))
    return konflik


# ---------------------------------------------------------------------------
# Keluaran
# ---------------------------------------------------------------------------
def tulis_laporan(a: Dokumen, b: Dokumen, pasangan: list[PasanganMirip], konflik, out: Path) -> dict:
    kosong = [k for k in KOMPONEN if not a.cakupan[k.no]["ada"] and not b.cakupan[k.no]["ada"]]
    hanya_a = [k for k in KOMPONEN if a.cakupan[k.no]["ada"] and not b.cakupan[k.no]["ada"]]
    hanya_b = [k for k in KOMPONEN if not a.cakupan[k.no]["ada"] and b.cakupan[k.no]["ada"]]
    keduanya = [k for k in KOMPONEN if a.cakupan[k.no]["ada"] and b.cakupan[k.no]["ada"]]
    total = len(KOMPONEN)

    L: list[str] = []
    L.append("# Laporan Analisis Tumpang-Tindih Dua Proposal\n")
    L.append(f"Tanggal analisis: {date.today().isoformat()}\n")
    L.append("| | File A | File B |")
    L.append("|---|---|---|")
    L.append(f"| Nama file | `{a.path.name}` | `{b.path.name}` |")
    L.append(f"| Jumlah kata | {len(a.teks.split()):,} | {len(b.teks.split()):,} |")
    L.append(f"| Paragraf bermakna | {len(a.blok)} | {len(b.blok)} |")
    L.append(f"| Judul seksi dikenali | {len(a.judul_seksi)} | {len(b.judul_seksi)} |")
    L.append(f"| Komponen terisi | {sum(1 for k in KOMPONEN if a.cakupan[k.no]['ada'])} / {total} | "
             f"{sum(1 for k in KOMPONEN if b.cakupan[k.no]['ada'])} / {total} |")
    L.append("")
    L.append(f"- Pasangan paragraf mirip: **{len(pasangan)}** (hampir identik: {sum(1 for p in pasangan if p.status == 'hampir identik')})")
    L.append(f"- Topik rawan konflik: **{len(konflik)}**\n")

    L.append("## 1. Jawaban singkat: apakah kedua file bisa saling melengkapi?\n")
    L.append(f"| Kelompok | Jumlah | Komponen |")
    L.append("|---|---|---|")
    L.append(f"| Hanya ada di A (nilai tambah A) | {len(hanya_a)} | {', '.join(k.nama for k in hanya_a) or '—'} |")
    L.append(f"| Hanya ada di B (nilai tambah B) | {len(hanya_b)} | {', '.join(k.nama for k in hanya_b) or '—'} |")
    L.append(f"| Ada di keduanya (rawan duplikat) | {len(keduanya)} | {', '.join(k.nama for k in keduanya) or '—'} |")
    L.append(f"| Kosong di keduanya (wajib ditulis baru) | {len(kosong)} | {', '.join(k.nama for k in kosong) or '—'} |")
    L.append("")
    if hanya_a and hanya_b and not kosong:
        L.append("> **Kesimpulan: YA, kedua file saling melengkapi.** Masing-masing memiliki komponen yang tidak dimiliki "
                 "file lain, dan tidak ada komponen yang hilang total. Rencana: pakai file dengan komponen terbanyak sebagai "
                 "*base document*, lalu transplantasikan komponen eksklusif dari file lain (lihat rekomendasi di bagian 2).\n")
    elif hanya_a and hanya_b:
        L.append("> **Kesimpulan: saling melengkapi, tetapi belum lengkap.** Selain transplantasi antar file, komponen di bawah "
                 "harus ditulis dari nol karena tidak ada di A maupun B:\n")
        for k in kosong:
            L.append(f"> - **{k.nama}** ({k.prioritas}) — {k.saran_bila_hilang}")
        L.append("")
    elif keduanya and not kosong:
        L.append("> **Kesimpulan: cakupan kedua file hampir sama.** Masalah utama bukan kekurangan isi, melainkan duplikasi. "
                 "Fokuskan pekerjaan pada memilih versi terbaik tiap komponen dan membuang duplikatnya.\n")
    else:
        L.append("> **Kesimpulan: perlu pekerjaan penggabungan yang cukup besar.** Lihat tabel di bagian 2 dan daftar lubang di bagian 3.\n")

    L.append("## 2. Peta cakupan 18 komponen\n")
    L.append("| # | Komponen | Prioritas | A | B | Bukti di A | Bukti di B | Rekomendasi |")
    L.append("|---|---|---|---|---|---|---|---|")
    for k in KOMPONEN:
        ca, cb = a.cakupan[k.no], b.cakupan[k.no]
        ta, tb = ("✔" if ca["ada"] else "—"), ("✔" if cb["ada"] else "—")
        ea = ", ".join(f"\"{h}\" (baris {baris})" for h, baris in ca["judul"][:2]) or (f"{len(ca['paragraf'])} paragraf" if ca["paragraf"] else "")
        eb = ", ".join(f"\"{h}\" (baris {baris})" for h, baris in cb["judul"][:2]) or (f"{len(cb['paragraf'])} paragraf" if cb["paragraf"] else "")
        if ca["ada"] and cb["ada"]:
            rek = "Pilih/gabungkan; buang duplikat"
        elif ca["ada"]:
            rek = "Ambil dari A"
        elif cb["ada"]:
            rek = "Ambil dari B"
        else:
            rek = "**TULIS BARU**"
        L.append(f"| {k.no} | {k.nama} | {k.prioritas} | {ta} | {tb} | {ea or '—'} | {eb or '—'} | {rek} |")
    L.append("")

    rawan = [k for k in keduanya if k.prioritas in ("Sangat tinggi", "Tinggi")]
    if rawan:
        L.append("### Komponen berprioritas tinggi yang ada di kedua file")
        L.append("Inilah titik paling berisiko: dua versi klaim penting hidup berdampingan. Periksa satu per satu.\n")
        for k in rawan:
            L.append(f"- **{k.nama}** ({k.prioritas}) — bandingkan versi A dan B sebelum memilih.")
        L.append("")

    if kosong:
        L.append("## 3. Lubang isi: komponen yang tidak ada di file A maupun B\n")
        for k in kosong:
            L.append(f"### {k.nama} ({k.prioritas})")
            L.append(f"- Saran: {k.saran_bila_hilang}")
            L.append(f"- Kata kunci yang dicari: {', '.join(k.kata_kunci[:8])}")
            L.append("")
        L.append("> Komponen berprioritas sangat tinggi/tinggi di daftar ini adalah risiko penolakan terbesar saat pengajuan.\n")

    L.append("## 4. Temuan tumpang-tindih\n")
    L.append(f"- Duplikat: {sum(1 for p in pasangan if p.status == 'duplikat')} pasangan · hampir identik: "
             f"{sum(1 for p in pasangan if p.status == 'hampir identik')} pasangan.")
    L.append("- Rincian top 20 ada di `daftar-duplikat.md`.\n")
    per_komp: dict[int, int] = {}
    for p in pasangan:
        for blk in (p.a, p.b):
            if blk.komponen:
                per_komp[blk.komponen] = per_komp.get(blk.komponen, 0) + 1
    if per_komp:
        L.append("Komponen dengan tumpang-tindih terbanyak (prioritas penggabungan):\n")
        for no in sorted(per_komp, key=lambda n: -per_komp[n])[:5]:
            nama = next(k.nama for k in KOMPONEN if k.no == no)
            L.append(f"- **{nama}**: muncul pada {per_komp[no]} baris tumpang-tindih")
        L.append("")

    L.append("## 5. Konflik yang wajib diputuskan manusia\n")
    if konflik:
        L.append("| Topik | Nilai hanya di A | Nilai hanya di B |")
        L.append("|---|---|---|")
        for nama, sa, sb in konflik:
            L.append(f"| {nama} | {', '.join(sa[:8]) or '—'}{'…' if len(sa) > 8 else ''} | {', '.join(sb[:8]) or '—'}{'…' if len(sb) > 8 else ''} |")
        L.append("")
        L.append("> Detail & aturan keputusan ada di `daftar-konflik.md`. Untuk setiap baris: pilih SATU nilai yang paling bisa "
                 "Anda pertahankan di depan penguji, lalu sinkronkan angka tersebut di abstrak, metodologi, jadwal, dan anggaran.\n")
    else:
        L.append("Tidak ada perbedaan angka/metode yang terdeteksi otomatis. Tetap periksa manual rumusan masalah, pertanyaan "
                 "penelitian, dan keputusan metodologis — script tidak bisa menilai mana yang benar.\n")

    L.append("## 6. Langkah berikutnya\n")
    L.append("1. Buka `kerangka-gabungan.md` — itu cetakan penulisan dokumen final Anda.")
    L.append("2. Lengkapi `pemetaan-seksi.csv` (tandai asal komponen, catat konflik, tentukan penanggung jawab).")
    L.append("3. Selesaikan setiap butir di `daftar-konflik.md`; catat keputusan + alasan di `changelog-gabungan.md`.")
    L.append("4. Tulis ulang setiap seksi mengikuti kerangka (jangan menempel), tambahkan paragraf penyambung antar seksi.")
    L.append("5. Jalankan checklist akhir pada `panduan-penggabungan-proposal.md` sebelum diserahkan ke pembimbing.")
    (out / "laporan-tumpang-tindih.md").write_text("\n".join(L), encoding="utf-8")

    return {"kosong": [k.nama for k in kosong], "pasangan": len(pasangan), "konflik": len(konflik)}


def tulis_pemetaan_csv(a: Dokumen, b: Dokumen, out: Path) -> None:
    with (out / "pemetaan-seksi.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["no", "komponen", "prioritas", "status", "bukti_A", "bukti_B", "paragraf_A", "paragraf_B", "rekomendasi", "keputusan_akhir", "penanggung_jawab"])
        for k in KOMPONEN:
            ca, cb = a.cakupan[k.no], b.cakupan[k.no]
            if ca["ada"] and cb["ada"]:
                status, rek = "A+B (rawan duplikat)", "Bandingkan versi A dan B, pilih terbaik, buang duplikatnya"
            elif ca["ada"]:
                status, rek = "A saja", "Ambil dari A"
            elif cb["ada"]:
                status, rek = "B saja", "Ambil dari B"
            else:
                status, rek = "KOSONG di keduanya", "TULIS BARU — " + k.saran_bila_hilang
            ea = "; ".join(f"{h} (baris {baris})" for h, baris in ca["judul"][:3])
            eb = "; ".join(f"{h} (baris {baris})" for h, baris in cb["judul"][:3])
            w.writerow([k.no, k.nama, k.prioritas, status, ea or "—", eb or "—",
                        len(ca["paragraf"]), len(cb["paragraf"]), rek, "", ""])


def tulis_duplikat(pasangan: list[PasanganMirip], out: Path) -> None:
    L = ["# Daftar Tumpang-Tindih (Duplikat) antar Paragraf\n",
         "Kolom **skor**: 1,0 = identik. Jadikan tabel ini daftar kerja: satu versi dipertahankan, versi lain dibuang — "
         "atau keduanya dilebur menjadi satu paragraf yang lebih kuat.\n"]
    if not pasangan:
        L.append("_Tidak ada pasangan paragraf yang melewati ambang kemiripan 0,45. Kedua dokumen cenderung saling melengkapi, bukan mengulang._\n")
    for i, p in enumerate(pasangan[:20], start=1):
        L.append(f"## {i}. Skor {p.skor} — {p.status}")
        L.append(f"**{p.a.id}** (baris {p.a.baris}, {p.a.kata} kata, komponen {p.a.komponen or '—'}):")
        L.append(f"> {p.a.teks[:700]}{'…' if len(p.a.teks) > 700 else ''}\n")
        L.append(f"**{p.b.id}** (baris {p.b.baris}, {p.b.kata} kata, komponen {p.b.komponen or '—'}):")
        L.append(f"> {p.b.teks[:700]}{'…' if len(p.b.teks) > 700 else ''}\n")
        if abs(p.a.kata - p.b.kata) > 25:
            saran = f"Pertahankan yang lebih lengkap ({'A' if p.a.kata > p.b.kata else 'B'}), buang versi lainnya."
        else:
            saran = "Kedua versi setara: peleburan manual menjadi satu paragraf, ambil kalimat terbaik dari masing-masing."
        L.append(f"**Saran:** {saran}\n")
    (out / "daftar-duplikat.md").write_text("\n".join(L), encoding="utf-8")


def tulis_konflik(a: Dokumen, b: Dokumen, konflik, out: Path) -> None:
    L = ["# Daftar Konflik yang Wajib Diputuskan Manusia\n",
         "Setiap item di bawah muncul di kedua file dengan isi berbeda. **Jangan diselesaikan dengan menggabungkan dua-duanya.** "
         "Pilih satu nilai, catat alasannya di `changelog-gabungan.md`, lalu sinkronkan di seluruh dokumen.\n"]
    if konflik:
        L.append("| Topik | Hanya di A | Hanya di B | Aturan keputusan |")
        L.append("|---|---|---|---|")
        aturan = {
            "Angka sampel/responden": "Pilih ukuran yang justifikasinya bisa Anda pertahankan (bukan otomatis yang terbesar); perbarui juga bagian metodologi & keterbatasan.",
            "Durasi penelitian": "Ambil durasi yang paling realistis (termasuk waktu izin & etik) lalu sesuaikan milestone lain.",
            "Jumlah item instrumen": "Samakan dengan instrumen yang benar-benar dilampirkan; jangan menyebut jumlah item yang tidak ada.",
            "Anggaran": "Rekonsiliasi dengan metode & jadwal terpilih; jangan menyisakan dua total anggaran di dokumen.",
            "Metode yang dianut": "Bila ingin mempertahankan keduanya, tulis sebagai mixed methods dengan fase, titik integrasi, dan RQ per fase — jangan menumpuk dua desain tanpa integrasi.",
        }
        for nama, sa, sb in konflik:
            L.append(f"| {nama} | {', '.join(sa) or '—'} | {', '.join(sb) or '—'} | {aturan.get(nama, 'Putuskan satu nilai dan jaga konsistensinya.')} |")
        L.append("")
    else:
        L.append("_Tidak ada perbedaan angka/metode yang terdeteksi otomatis._\n")

    L.append("## Konflik non-angka yang harus diperiksa manual\n")
    for item in (
        "Rumusan masalah & pertanyaan penelitian: berapa set yang muncul? Pilih satu set yang paling selaras dengan metode.",
        "Desain/metode: kualitatif vs kuantitatif vs mixed — mana yang benar-benar bisa dijalankan dengan waktu & akses Anda?",
        "Teori: tentukan teori utama dan teori pendukung, jelaskan peran masing-masing.",
        "Jadwal: tanggal mana yang realistis setelah memperhitungkan izin institusi, etik, dan uji instrumen?",
        "Istilah/variabel: apakah nama variabel identik di kedua file? Bila tidak, buat glosarium tunggal lalu cari-ganti.",
        "Daftar pustaka: sitasi yang hanya ada di salah satu file — dipertahankan atau dibuang?",
        "Klaim kebaruan: pastikan versi yang dipakai tidak dibantah literatur dalam file lainnya.",
    ):
        L.append(f"- [ ] {item}")
    L.append("")
    (out / "daftar-konflik.md").write_text("\n".join(L), encoding="utf-8")


def tulis_kerangka(a: Dokumen, b: Dokumen, out: Path) -> None:
    L = ["# Kerangka Proposal Gabungan (cetakan penulisan)\n",
         f"File A = `{a.path.name}` · File B = `{b.path.name}`",
         "Penanda: `[A]` hanya dari A · `[B]` hanya dari B · `[A+B]` dari keduanya (perlu dilebur) · `[BARU]` harus ditulis baru.\n",
         "> Isi setiap seksi dengan MENULIS ULANG, bukan menempel. Setelah dokumen final selesai, penanda ini dihapus "
         "atau dipindahkan ke `changelog-gabungan.md`.\n"]
    for k in KOMPONEN:
        ca, cb = a.cakupan[k.no], b.cakupan[k.no]
        if ca["ada"] and cb["ada"]:
            tanda, catatan = "[A+B]", "Berada di kedua file — bandingkan, pilih versi terbaik, buang duplikatnya."
        elif ca["ada"]:
            tanda, catatan = "[A]", "Diambil dari A; selaraskan istilah & angkanya dengan keputusan di B."
        elif cb["ada"]:
            tanda, catatan = "[B]", "Diambil dari B; selaraskan istilah & angkanya dengan keputusan di A."
        else:
            tanda, catatan = "[BARU]", "KOSONG DI KEDUANYA — " + k.saran_bila_hilang
        L.append(f"## {k.no}. {k.nama} — {tanda}")
        L.append(f"- Prioritas rubrik: {k.prioritas}")
        L.append(f"- Catatan: {catatan}")
        for label_doc, nama_doc, cak in (("A", "A", ca), ("B", "B", cb)):
            if cak["judul"]:
                L.append(f"- Judul seksi di {nama_doc}: " + "; ".join(f"\"{h}\" (baris {baris})" for h, baris in cak["judul"][:4]))
            for blk in cak["paragraf"][:2]:
                ringkas = blk.teks[:200].replace("\n", " ")
                L.append(f"- Bahan mentah {nama_doc} ({blk.id}, baris {blk.baris}): {ringkas}{'…' if len(blk.teks) > 200 else ''}")
        L.append("")
    (out / "kerangka-gabungan.md").write_text("\n".join(L), encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    p = argparse.ArgumentParser(description="Analisis tumpang-tindih dua dokumen proposal disertasi.")
    p.add_argument("--a", required=True, help="File proposal A (.txt/.md/.docx/.pdf)")
    p.add_argument("--b", required=True, help="File proposal B (.txt/.md/.docx/.pdf)")
    p.add_argument("--out", default="hasil", help="Folder keluaran (default: hasil)")
    p.add_argument("--nama-a", default="File A", help="Label file A, mis. 'Draft Pembimbing 1'")
    p.add_argument("--nama-b", default="File B", help="Label file B, mis. 'Rencana Penelitian'")
    args = p.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    a = Dokumen("A", Path(args.a), baca_dokumen(Path(args.a)))
    b = Dokumen("B", Path(args.b), baca_dokumen(Path(args.b)))
    pecah_dokumen(a)
    pecah_dokumen(b)

    pasangan = bandingkan(a, b)
    konflik = deteksi_konflik(a, b)

    ringkas = tulis_laporan(a, b, pasangan, konflik, out)
    tulis_pemetaan_csv(a, b, out)
    tulis_duplikat(pasangan, out)
    tulis_konflik(a, b, konflik, out)
    tulis_kerangka(a, b, out)

    print("Analisis selesai.")
    print(f"  {args.nama_a}: {len(a.blok)} paragraf, {len(a.judul_seksi)} judul seksi dikenali")
    print(f"  {args.nama_b}: {len(b.blok)} paragraf, {len(b.judul_seksi)} judul seksi dikenali")
    print(f"  {ringkas['pasangan']} pasangan paragraf mirip · {ringkas['konflik']} topik konflik · {len(ringkas['kosong'])} komponen kosong di keduanya")
    if ringkas["kosong"]:
        print("  Wajib ditulis baru: " + ", ".join(ringkas["kosong"]))
    print(f"  Laporan utama: {out/'laporan-tumpang-tindih.md'}")


if __name__ == "__main__":
    sys.exit(main())
