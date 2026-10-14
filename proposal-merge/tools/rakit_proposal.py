#!/usr/bin/env python3
"""
rakit_proposal.py — merakit naskah gabungan dari tiga berkas proposal + tabel terpilih.

Dokumen induk : A  = "Proposal Disertasi Michael Raintung - Revisi Seminar Proposal" (terbaru)
Transplantasi : B  = "Proposal Disertasi Michael Raintung 14 Oktober 2026"
                C  = "PROPOSAL_DISERTASI_TANPA_MODERATOR_80-100_HALAMAN (1)"

Keluaran      : hasil/proposal-gabungan.md  → dikonversi oleh tools/md_ke_docx.py
"""
from __future__ import annotations

import re
import unicodedata
import pathlib

PUSTAKA_STAT: dict = {}

TEKS = pathlib.Path("/tmp")
OUT = pathlib.Path("hasil/proposal-gabungan.md")
SRC = {k: (TEKS / f"bersih-{k}.txt").read_text(encoding="utf-8").splitlines() for k in "ABC"}

# ---------------------------------------------------------------- pengenalan judul
PAT_BAB = re.compile(r"^(BAB|BAGIAN)\s+[IVX]+\.?\s")
PAT_H2 = re.compile(r"^[A-I]\.\s+[A-Z]")
PAT_H3 = re.compile(r"^\d{1,2}\.\s+[A-Z]")
PAT_H4 = re.compile(r"^[a-i]\.\s+[A-Za-z]")
PAT_LAMPIRAN = re.compile(r"^Lampiran\s+\d+\.\s")
PAT_TOP = re.compile(r"^(DAFTAR PUSTAKA|LAMPIRAN|RINGKASAN PROPOSAL|DAFTAR ISI|DAFTAR TABEL|DAFTAR GAMBAR)\s*$")
NOISE = re.compile(r"^\s*(\d{1,3}|[ivxlcdm]{1,6})\s*$", re.I)


AWALAN_BUTIR = re.compile(r"^(Apakah|Menganalisis|Menguji|Menilai|Menetapkan|Tuliskan|Seberapa|Berapa|Kategori|"
                          r"Usia|Kabupaten|Saya|Merek|Influencer|Konten|Gaya|Kepribadian|Nilai-nilai|Tindakan|"
                          r"Informasi|Positif|Simpan|Catat|Lengkapi|Tetapkan)\b", re.I)


def _norm_judul(t: str) -> str:
    t = re.sub(r"\.{2,}\s*\d+\s*$", "", t)
    t = re.sub(r"\s+\d+\s*$", "", t)
    t = re.sub(r"^(BAB|BAGIAN)\s+[IVX]+\.?\s*", "", t, flags=re.I)
    t = re.sub(r"^([A-I]|\d{1,2}|[a-i])\.\s*", "", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def _daftar_putih(k: str) -> set[str]:
    """Ambil judul sah dari blok DAFTAR ISI berkas sumber (paling andal)."""
    baris = SRC[k]
    mulai = None
    for i, l in enumerate(baris):
        if l.strip().upper() == "DAFTAR ISI":
            mulai = i
            break
    if mulai is None:
        return set()
    pudul = set()
    for l in baris[mulai + 1: mulai + 140]:
        t = l.strip()
        if not t or len(t) > 100:
            continue
        if re.match(r"^(BAB|BAGIAN)\s+[IVX]+\.", t, re.I) and "_" not in t:
            pass
        n = _norm_judul(t)
        if 3 <= len(n) <= 80:
            pudul.add(n)
    return pudul


DAFTAR_PUTIH = {k: _daftar_putih(k) for k in "ABC"}


def level(baris: str, sebelum: str | None = None, sesudah: str | None = None) -> int:
    s = baris.strip()
    if not s or len(s) > 95 or re.search(r"\.{2,}", s):
        return 0
    if re.search(r"[.!?:;,]$", s) or "____" in s or "[" in s:
        return 0
    n = _norm_judul(s)
    # Daftar isi berkas A adalah sumber otoritatif: hanya judul yang terdaftar di sana
    # (atau yang ditanam eksplisit oleh perakit) yang diperlakukan sebagai judul.
    if not any(n[:32] == kn[:32] or kn[:32] == n[:32] for kn in DAFTAR_PUTIH.get("A", ())):
        return 0
    if PAT_BAB.match(s) or PAT_TOP.match(s):
        return 1
    if PAT_LAMPIRAN.match(s):
        return 1
    if PAT_H2.match(s) and len(s) <= 80:
        return 2
    if PAT_H3.match(s) and len(s) <= 85:
        return 3
    if PAT_H4.match(s) and len(s) <= 85:
        return 4
    return 0


def pohon(k: str):
    out = []
    baris_k = SRC[k]
    for i, l in enumerate(baris_k):
        lv = level(l, baris_k[i - 1] if i else None, baris_k[i + 1] if i + 1 < len(baris_k) else None)
        if lv:
            out.append((i, lv, l.strip()))
    idx = [j for j, (_, lv, s) in enumerate(out) if lv == 1 and "PENDAHULUAN" in s]
    return out[idx[1]:] if len(idx) >= 2 else out


def blok_dari(k: str, judul_re: str, lv_min: int | None = None, kejadian: int = 1) -> list[str]:
    p = pohon(k)
    n = 0
    target = None
    for j, (i, lv, s) in enumerate(p):
        if re.search(judul_re, s, re.I) and (lv_min is None or lv <= lv_min):
            n += 1
            if n == kejadian:
                target = (j, i, lv)
                break
    if not target:
        raise SystemExit(f"[{k}] judul tidak ditemukan: {judul_re}")
    j, i, lv = target
    akhir = len(SRC[k])
    for i2, lv2, _ in p[j + 1:]:
        if lv2 <= lv:
            akhir = i2
            break
    return SRC[k][i:akhir]


# ---------------------------------------------------------------- reflow & markdown
BATAS = re.compile(r"(?<=[.!?:])\s+(?=[A-ZÀ-Ý“\"(]|\d\.)")
BARIS_KHUSUS = re.compile(r"^(\s*[•\-–*]\s|\s*\d+[.)]\s|\s*[A-I]\.\s|\s*[a-i]\.\s|\s*(KI|HP|AM|AMD|CTL)\d|Tabel\s|Gambar\s)")


def bersih_artefak(t: str) -> str:
    t = re.sub(r"(?<=[a-z])\?(?=[a-z])", "–", t)          # "konsumen?merek" -> "konsumen–merek"
    t = re.sub(r"\b([A-Z]{1,3}) \? (?=[A-Z]{1,3}\b)", r"\1 → ", t)   # "KI ? HP" -> "KI → HP"
    t = t.replace("servicedominant", "service-dominant")
    t = re.sub(r"\s+([.,;:])", r"\1", t)
    return t


def reflow(baris: list[str]) -> list[str]:
    keluar: list[str] = []
    buf = ""
    for idx, mentah in enumerate(baris):
        s = mentah.strip()
        if not s or NOISE.match(s):
            continue
        lv = level(s, baris[idx - 1] if idx else None, baris[idx + 1] if idx + 1 < len(baris) else None)
        if lv:
            if buf:
                keluar.append(buf); buf = ""
            keluar.append(f"H{lv}|{s}")
            continue
        if BARIS_KHUSUS.match(mentah):
            if buf:
                keluar.append(buf); buf = ""
            keluar.append("L|" + s)
            continue
        buf = f"{buf} {s}".strip() if buf else s
    if buf:
        keluar.append(buf)
    return keluar


def emit(blok: list[str], geser: int = 0) -> list[str]:
    md: list[str] = []
    for b in blok:
        if re.match(r"^H[1-4]\|", b):
            lv = min(int(b[1]) + geser, 6)
            judul = re.sub(r"\s+", " ", b[3:]).strip()
            md.append("#" * lv + " " + judul)
        elif b.startswith("L|"):
            s = b[2:]
            md.append(s if re.match(r"^(\d+[.)]|[A-I]\.|[a-i]\.|KI|HP|AM|AMD|CTL)", s) else "- " + s)
        else:
            teks = b.strip()
            if len(teks) <= 900:
                md.append(teks)
            else:                                  # paragraf sangat panjang: pecah pada batas kalimat
                buf = ""
                for kal in BATAS.split(teks):
                    buf = f"{buf} {kal}".strip()
                    if len(buf) >= 500:
                        md.append(buf); buf = ""
                if buf:
                    md.append(buf)
    return md


def bagian_anak(k: str, induk_re: str, lv_induk: int = 2):
    """Kembalikan [(judul, baris)] untuk setiap sub-bagian di dalam sebuah bagian induk."""
    p = pohon(k)
    j0 = None
    for j, (i, lv, s) in enumerate(p):
        if lv == lv_induk and re.search(induk_re, s, re.I):
            j0 = j
            break
    if j0 is None:
        raise SystemExit(f"[{k}] induk tidak ditemukan: {induk_re}")
    i0, _, _ = p[j0]
    akhir = len(SRC[k])
    for i2, lv2, _ in p[j0 + 1:]:
        if lv2 <= lv_induk:
            akhir = i2
            break
    anak = [(i, lv, s) for (i, lv, s) in p if i0 < i < akhir and lv == lv_induk + 1]
    hasil = []
    for n, (i, lv, s) in enumerate(anak):
        akhir_anak = anak[n + 1][0] if n + 1 < len(anak) else akhir
        hasil.append((s, SRC[k][i:akhir_anak]))
    return hasil



def pengantar_induk(k: str, induk_re: str, lv_induk: int = 2) -> list[str]:
    """Teks pengantar sebuah bagian induk: baris antara judul induk dan anak pertamanya."""
    p = pohon(k)
    j0 = None
    for j, (i, lv, s) in enumerate(p):
        if lv == lv_induk and re.search(induk_re, s, re.I):
            j0 = j
            break
    if j0 is None:
        raise SystemExit(f"[{k}] induk tidak ditemukan: {induk_re}")
    i0, _, _ = p[j0]
    akhir = len(SRC[k])
    for i2, lv2, _ in p[j0 + 1:]:
        if lv2 <= lv_induk + 1:
            akhir = i2
            break
    return SRC[k][i0 + 1:akhir]


def judul_induk(k: str, induk_re: str, lv_induk: int = 2) -> str:
    for i, lv, t in pohon(k):
        if lv == lv_induk and re.search(induk_re, t, re.I):
            return t
    raise SystemExit(f"[{k}] induk tidak ditemukan: {induk_re}")


def blok_mentah(k: str, pola: str, kejadian: int = 1) -> list[str]:
    """Ambil blok baris mulai dari sebuah paragraf (bukan judul) sampai judul berikutnya."""
    n = 0
    mulai = None
    for i, l in enumerate(SRC[k]):
        if re.search(pola, l) and not level(l):
            n += 1
            if n == kejadian:
                mulai = i
                break
    if mulai is None:
        raise SystemExit(f"[{k}] paragraf tidak ditemukan: {pola}")
    for i in range(mulai + 1, len(SRC[k])):
        if level(SRC[k][i]):
            return SRC[k][mulai:i]
    return SRC[k][mulai:]

def sisip(md: list[str], blok_tambahan: list[str]) -> list[str]:
    return md + [""] + blok_tambahan + [""]


# ==================================================================== TABEL (renumber)
def tabel(judul: str, kepala: list[str], baris: list[list[str]], catatan: str) -> list[str]:
    md = [f"**{judul}**", "", "| " + " | ".join(kepala) + " |", "|" + "---|" * len(kepala)]
    for b in baris:
        md.append("| " + " | ".join(x.replace("|", "/") for x in b) + " |")
    md += ["", f"*{catatan}*", ""]
    return md


T1 = tabel("Tabel 1. Kesenjangan penelitian dan keputusan desain",
           ["Jenis kesenjangan", "Keadaan literatur yang menjadi perhatian", "Keputusan dalam penelitian"],
           [["Mekanisme", "Hubungan kredibilitas, kedekatan parasosial, autentisitas, dan advokasi sering ditelaah pada model yang berbeda",
             "Menguji mediasi berurutan serta melaporkan jalur alternatif yang telah ditetapkan"],
            ["Luaran", "Niat beli dan sikap merek lebih sering dipakai daripada dukungan sukarela di ruang digital",
             "Menggunakan kesediaan advokasi merek digital dan memisahkannya dari pembelian"],
            ["Batas konstruk", "Penilaian influencer dapat bercampur dengan penilaian merek atau persepsi kesamaan",
             "Menjaga sasaran orang–merek dan menguji validitas diskriminan"],
            ["Pengukuran", "Skala lintas konteks dapat berubah makna setelah diterjemahkan",
             "Melakukan telaah sumber primer, terjemahan, panel ahli, wawancara kognitif, dan pilot"],
            ["Konteks", "Bukti dari satu jenis negara, wilayah, atau kategori produk tidak otomatis berlaku pada konteks lain",
             "Menguji model pada responden yang memenuhi kriteria di Sulawesi Utara dan membatasi generalisasi"],
            ["Inferensi", "Survei satu waktu dapat menunjukkan hubungan, tetapi tidak menetapkan urutan waktu",
             "Menafsirkan mediasi sebagai asosiasi tidak langsung yang konsisten dengan teori"]],
           "Diadaptasi dari berkas Proposal Disertasi 14 Oktober 2026 (Tabel 2).")

T2 = tabel("Tabel 2. Posisi dan sasaran keempat konstruk",
           ["Simbol", "Konstruk", "Objek evaluasi", "Peran analitis", "Jumlah butir inti"],
           [["X/KI", "Kredibilitas influencer", "Orang/influencer", "Prediktor eksogen", "9"],
            ["M1/HP", "Hubungan parasosial", "Relasi pengikut–influencer", "Mediator pertama", "9"],
            ["M2/AM", "Autentisitas merek", "Merek yang dipromosikan", "Mediator kedua", "12"],
            ["Y/AMD", "Kesediaan advokasi merek digital", "Diri responden terhadap merek", "Luaran endogen", "9"]],
           "Diadaptasi dari berkas PROPOSAL_DISERTASI_TANPA_MODERATOR (Tabel 10). Jumlah butir AMD disesuaikan dengan "
           "keputusan tiga domain pada dokumen induk; lihat Catatan Integrasi butir 2.")

T3 = tabel("Tabel 3. Definisi operasional dan landasan instrumen",
           ["Konstruk", "Definisi kerja", "Cakupan dimensi", "Sumber adaptasi dan batas antarobjek"],
           [["KI", "Penilaian konsumen atas kapasitas dan kelayakan influencer sebagai penyampai rekomendasi.",
             "Keahlian, kepercayaan, daya tarik.", "Ohanian (1990); Lou & Yuan (2019). Seluruh butir menilai orang."],
            ["HP", "Rasa dekat satu arah yang relatif stabil setelah mengikuti influencer berulang.",
             "Pertemanan, kedekatan emosional, pemahaman/identifikasi.",
             "Horton & Wohl (1956); Dibble et al. (2016). Tidak menyiratkan hubungan timbal balik nyata."],
            ["AM", "Penilaian konsumen bahwa merek mempertahankan karakter, menepati janji, berintegritas, dan bermakna.",
             "Kontinuitas, kredibilitas merek, integritas, simbolisme.",
             "Napoli et al. (2014); Morhart et al. (2015). Subjek butir merek, bukan figur."],
            ["AMD", "Kesediaan melakukan tindakan mendukung merek secara sukarela di saluran digital.",
             "Rekomendasi, berbagi konten, pembelaan.",
             "Wilk et al. (2020). Hasil yang diukur adalah kesediaan yang dilaporkan, bukan catatan tindakan."]],
           "Diadaptasi dari berkas PROPOSAL_DISERTASI_TANPA_MODERATOR (Tabel 11).")

T4 = tabel("Tabel 4. Pemetaan dimensi dan isi indikator",
           ["Kelompok indikator", "Kode", "Fokus isi butir", "Objek yang dinilai"],
           [["Keahlian", "KI1–KI3", "Pengetahuan, pengalaman kategori, dan kompetensi menjelaskan rekomendasi", "Influencer"],
            ["Keterpercayaan", "KI4–KI6", "Kejujuran, keterandalan, dan dapat dipercayainya rekomendasi", "Influencer"],
            ["Daya tarik", "KI7–KI9", "Daya tarik komunikator, gaya penyampaian, dan ketertarikan terhadap konten", "Influencer"],
            ["Persepsi pertemanan", "HP1–HP3", "Rasa akrab, mengenal kepribadian, dan kenyamanan mengikuti konten", "Hubungan pengikut–influencer"],
            ["Keterikatan emosional", "HP4–HP6", "Kedekatan emosional dan keterikatan yang dirasakan setelah mengikuti figur", "Hubungan pengikut–influencer"],
            ["Pemahaman figur", "HP7–HP9", "Memahami cara berpikir dan kecenderungan pandangan influencer", "Hubungan pengikut–influencer"],
            ["Kontinuitas", "AM1–AM3", "Konsistensi karakter dan nilai merek dari waktu ke waktu", "Merek"],
            ["Kredibilitas merek", "AM4–AM6", "Pemenuhan janji dan kejujuran informasi merek", "Merek"],
            ["Integritas", "AM7–AM9", "Keselarasan klaim dan tindakan serta kepedulian yang dapat dinilai", "Merek"],
            ["Simbolisme", "AM10–AM12", "Makna identitas dan keselarasan makna merek bagi responden", "Merek"],
            ["Rekomendasi", "AMD1–AMD3", "Kesediaan merekomendasikan atau menulis ulasan", "Tindakan responden terhadap merek"],
            ["Berbagi konten", "AMD4–AMD6", "Kesediaan menyebarkan, menandai, atau mengunggah ulang konten", "Tindakan responden terhadap merek"],
            ["Pembelaan", "AMD7–AMD9", "Kesediaan meluruskan informasi keliru dan membela merek", "Tindakan responden terhadap merek"]],
           "Diadaptasi dari berkas Proposal Disertasi 14 Oktober 2026 (Tabel 5).")

BUTIR = [
 ("KI1","Keahlian","Influencer acuan saya menguasai informasi mengenai produk yang direkomendasikannya.","Ohanian (1990)"),
 ("KI2","Keahlian","Influencer acuan saya memiliki pengalaman nyata menggunakan produk yang direkomendasikannya.","Ohanian (1990); Lou dan Yuan (2019)"),
 ("KI3","Keahlian","Informasi yang disampaikan influencer acuan saya berkualitas dan dapat dipertanggungjawabkan.","Lou dan Yuan (2019)"),
 ("KI4","Kepercayaan","Influencer acuan saya memberikan opini secara jujur.","Ohanian (1990)"),
 ("KI5","Kepercayaan","Influencer acuan saya transparan mengenai kerja samanya dengan merek.","Lou dan Yuan (2019)"),
 ("KI6","Kepercayaan","Saya percaya rekomendasi influencer acuan saya tidak menyesatkan.","Ohanian (1990)"),
 ("KI7","Daya Tarik","Gaya komunikasi influencer acuan saya menarik.","Ohanian (1990)"),
 ("KI8","Daya Tarik","Kepribadian influencer acuan saya menyenangkan.","Ohanian (1990)"),
 ("KI9","Daya Tarik","Influencer acuan saya memiliki kesamaan nilai dengan saya.","Ohanian (1990); Lou dan Yuan (2019)"),
 ("HP1","Persepsi Pertemanan","Saya merasa influencer acuan saya seperti teman sendiri.","Dibble et al. (2016)"),
 ("HP2","Persepsi Pertemanan","Saya merasa mengenal kepribadian influencer acuan saya.","Dibble et al. (2016)"),
 ("HP3","Persepsi Pertemanan","Saya merasa nyaman ketika menyimak konten influencer acuan saya.","Horton dan Wohl (1956); Dibble et al. (2016)"),
 ("HP4","Keterikatan Emosional","Saya merasa dekat secara emosional dengan influencer acuan saya.","Dibble et al. (2016)"),
 ("HP5","Keterikatan Emosional","Saya merasa rindu apabila influencer acuan saya lama tidak mengunggah konten.","Dibble et al. (2016)"),
 ("HP6","Keterikatan Emosional","Konten influencer acuan saya menjadi bagian penting dalam rutinitas harian saya.","Dibble et al. (2016)"),
 ("HP7","Pemahaman dan Identifikasi","Saya dapat memahami cara berpikir influencer acuan saya.","Dibble et al. (2016)"),
 ("HP8","Pemahaman dan Identifikasi","Saya dapat memprediksi pendapat influencer acuan saya mengenai suatu isu.","Dibble et al. (2016)"),
 ("HP9","Pemahaman dan Identifikasi","Saya merasa memiliki kemiripan nilai dengan influencer acuan saya.","Dibble et al. (2016); Ki dan Kim (2019)"),
 ("AM1","Kontinuitas","Merek acuan saya konsisten mempertahankan karakter dan nilainya dari waktu ke waktu.","Morhart et al. (2015)"),
 ("AM2","Kontinuitas","Merek acuan saya tetap setia pada nilai-nilai yang menjadi warisannya.","Napoli et al. (2014); Morhart et al. (2015)"),
 ("AM3","Kontinuitas","Merek acuan saya tidak mudah mengubah identitas demi mengikuti tren sesaat.","Morhart et al. (2015)"),
 ("AM4","Kredibilitas Merek","Merek acuan saya menepati janji kualitas yang diiklankannya.","Morhart et al. (2015)"),
 ("AM5","Kredibilitas Merek","Merek acuan saya menyampaikan informasi produk secara jujur.","Napoli et al. (2014); Morhart et al. (2015)"),
 ("AM6","Kredibilitas Merek","Merek acuan saya tidak pernah mengecewakan ekspektasi saya.","Morhart et al. (2015)"),
 ("AM7","Integritas","Merek acuan saya bersikap jujur mengenai motif komersialnya.","Morhart et al. (2015)"),
 ("AM8","Integritas","Tindakan merek acuan saya selaras dengan pernyataan nilai yang diklaimnya.","Napoli et al. (2014); Morhart et al. (2015)"),
 ("AM9","Integritas","Merek acuan saya berkomitmen tidak merugikan konsumen dan lingkungan.","Morhart et al. (2015)"),
 ("AM10","Simbolisme","Merek acuan saya mencerminkan siapa diri saya.","Morhart et al. (2015)"),
 ("AM11","Simbolisme","Merek acuan saya membantu saya mengomunikasikan identitas saya kepada orang lain.","Morhart et al. (2015)"),
 ("AM12","Simbolisme","Nilai-nilai merek acuan saya selaras dengan prinsip hidup saya.","Napoli et al. (2014); Morhart et al. (2015)"),
 ("AMD1","Rekomendasi","Saya bersedia merekomendasikan merek acuan saya kepada orang lain secara daring.","Wilk et al. (2020)"),
 ("AMD2","Rekomendasi","Saya bersedia menulis ulasan positif mengenai merek acuan saya.","Wilk et al. (2020)"),
 ("AMD3","Rekomendasi","Saya bersedia mengajak teman saya mencoba merek acuan saya.","Wilk et al. (2020)"),
 ("AMD4","Berbagi Konten","Saya bersedia membagikan konten resmi merek acuan saya ke media sosial pribadi saya.","Wilk et al. (2020)"),
 ("AMD5","Berbagi Konten","Saya bersedia menandai teman saya pada unggahan menarik tentang merek acuan saya.","Wilk et al. (2020)"),
 ("AMD6","Berbagi Konten","Saya bersedia mengunggah ulang konten kampanye merek acuan saya.","Wilk et al. (2020)"),
 ("AMD7","Pembelaan","Saya bersedia meluruskan informasi yang keliru mengenai merek acuan saya.","Wilk et al. (2020)"),
 ("AMD8","Pembelaan","Saya bersedia membela merek acuan saya ketika dikritik secara tidak adil.","Wilk et al. (2020)"),
 ("AMD9","Pembelaan","Saya bersedia memberikan klarifikasi berdasarkan pengalaman pribadi saya ketika merek acuan saya diserang.","Wilk et al. (2020)"),
 ("CTL1","Familiaritas Merek","Saya mengenal baik merek acuan saya.","Butir kontrol peneliti"),
 ("CTL2","Familiaritas Merek","Merek acuan saya mudah saya kenali di antara merek lain.","Butir kontrol peneliti"),
 ("CTL3","Pengalaman Merek","Saya pernah menggunakan atau merasakan produk/layanan merek acuan saya.","Butir kontrol peneliti"),
 ("CTL4","Pengalaman Merek","Saya memiliki pengalaman langsung berinteraksi dengan merek acuan saya.","Butir kontrol peneliti"),
 ("CTL5","Influencer–Brand Fit","Influencer acuan saya merupakan figur yang cocok merepresentasikan merek acuan saya.","Butir kontrol peneliti"),
 ("CTL6","Influencer–Brand Fit","Terdapat keselarasan antara citra influencer acuan saya dengan citra merek acuan saya.","Butir kontrol peneliti"),
 ("CTL7","Paparan Disclosure","Saya pernah melihat informasi bahwa kerja sama influencer acuan saya dengan merek acuan saya bersifat bersponsor.","Butir kontrol peneliti"),
 ("CTL8","Paparan Disclosure","Influencer acuan saya menyatakan secara terbuka bahwa kontennya bersponsor.","Butir kontrol peneliti"),
]

T5 = tabel("Tabel 5. Kisi-kisi butir instrumen (draf untuk pilot)",
           ["Kode", "Dimensi", "Butir pernyataan", "Landasan adaptasi"],
           [[k, d, b, s] for k, d, b, s in BUTIR],
           "Diadaptasi dari berkas PROPOSAL_DISERTASI_TANPA_MODERATOR (Tabel 12). Butir AMD10–AMD12 pada berkas sumber "
           "(dimensi Partisipasi Sukarela) tidak dicantumkan karena dokumen induk menetapkan tiga domain advokasi; "
           "rumusannya tersimpan pada berkas sumber dan dapat diaktifkan kembali bila keputusan berbeda.")

T6 = tabel("Tabel 6. Asumsi kecukupan sampel dan keputusan sebelum pengumpulan data",
           ["Komponen", "Asumsi/ketentuan", "Makna untuk rancangan"],
           [["Uji jalur tunggal terkecil yang direncanakan", "R² increase, 1 prediktor; α=0,05; daya 0,80; f²=0,02",
             "Pendekatan kebutuhan sekitar N=395; bukan daya mediasi."],
            ["Sensitivitas efek yang lebih kecil", "R² increase; f²=0,01 pada α=0,05 dan daya 0,80",
             "Pendekatan kebutuhan sekitar N=787; melampaui target 700."],
            ["Sasaran penelitian", "Minimum 385 respons sah; sasaran perluasan 700 jawaban sah (850–900 formulir)",
             "Sasaran praktis konservatif yang harus dibandingkan hasil pilot."],
            ["Efek tidak langsung spesifik", "Produk a×b×c; asumsi tiap jalur, sebaran, dan kovariat ditetapkan dari pilot/literatur",
             "Simulasi daya Monte Carlo dilampirkan sebelum survei utama."],
            ["Kontrol dan subkelompok", "Variabel yang memiliki alasan teoretis; analisis kelompok terbatas",
             "Terlalu banyak kontrol atau kelompok kecil menurunkan ketelitian."]],
           "Diadaptasi dari berkas PROPOSAL_DISERTASI_TANPA_MODERATOR (Tabel 13); perhitungan noncentral F (2026), "
           "sejalan dengan Faul et al. (2009) dan Preacher & Selig (2012). Lihat Catatan Integrasi butir 1.")

T7 = tabel("Tabel 7. Acuan evaluasi model pengukuran",
           ["Aspek pengukuran reflektif", "Acuan awal", "Cara mengambil keputusan"],
           [["Loading indikator", "Ideal sekitar ≥0,708", "Evaluasi isi dan kontribusi; butir tidak dihapus otomatis hanya karena berada pada kisaran menengah"],
            ["Reliabilitas internal", "rho_A/komposit sekitar 0,70–0,95", "Nilai terlalu tinggi ditinjau sebagai kemungkinan repetisi butir"],
            ["Validitas konvergen", "AVE ≥0,50 sebagai sasaran", "Ditinjau bersama kualitas indikator dan definisi dimensi"],
            ["Validitas diskriminan", "HTMT <0,85 sebagai patokan konservatif, interval diperiksa", "Penilaian statistik dilengkapi pemeriksaan kesamaan makna butir"],
            ["Indikator berkinerja rendah", "Loading rendah atau ketidakjelasan isi", "Keputusan berdasarkan teori, panel, dan dampak pada domain; perubahan dicatat"]],
           "Diadaptasi dari berkas Proposal Disertasi 14 Oktober 2026 (Tabel 7). Acuan bersifat pedoman, bukan ambang mekanis untuk menghapus butir.")

T8 = tabel("Tabel 8. Aturan keputusan uji hipotesis",
           ["Hipotesis", "Estimand", "Kriteria utama", "Pelaporan bila tidak didukung"],
           [["H1", "a: KI→HP", "Interval 95% tidak melintasi nol; tanda positif.", "Laporkan koefisien, interval, dan alternatif penjelasan hubungan balik."],
            ["H2", "b: HP→AM dengan KI→AM dikendalikan", "Interval 95% tidak melintasi nol; tanda positif.", "Periksa kecocokan figur–merek, validitas butir, dan jalur d."],
            ["H3", "c: AM→AMD dengan HP dan KI dikendalikan", "Interval 95% tidak melintasi nol; tanda positif.", "Bedakan kesediaan perilaku dari loyalitas dan niat beli."],
            ["H4", "c′: KI→AMD di luar mediator", "Interval 95% tidak melintasi nol; tanda positif.", "H4 tidak didukung tidak otomatis menolak H5."],
            ["H5", "a×b×c: efek serial spesifik", "Interval bootstrap 95% tidak melintasi nol; arah positif.", "Laporkan jalur parsial dan sensitivitas; hindari klaim sebab-akibat."]],
           "Diadaptasi dari berkas PROPOSAL_DISERTASI_TANPA_MODERATOR (Tabel 14); kerangka inferensi mediasi Hayes (2018) dan Zhao et al. (2010).")

KOVARIAT = [
 "### 9. Kovariat dan Analisis Sensitivitas",
 "",
 "Familiaritas merek (CTL1–CTL2), pengalaman merek (CTL3–CTL4), kesesuaian influencer–merek (CTL5–CTL6), dan "
 "paparan pengungkapan sponsor (CTL7–CTL8) dicatat dengan target penilaian yang jelas. Usia, jenis kelamin, "
 "pendidikan, status pekerjaan, platform, frekuensi penggunaan, durasi mengikuti, dan kategori produk merupakan "
 "informasi latar untuk mendeskripsikan sampel dan dianalisis hanya bila ada argumen serta ukuran kelompok memadai. "
 "Sebagian butir kontrol lebih tepat diperlakukan sebagai variabel penjelas tambahan dalam analisis sensitivitas "
 "daripada dimasukkan ke model utama.",
 "",
 "*Disisipkan dari berkas PROPOSAL_DISERTASI_TANPA_MODERATOR, sub-bagian 5 Kovariat dan Analisis Sensitivitas.*",
 "",
]

KRITERIA_INKLUSI = [
 "> **Kriteria kelayakan responden (disisipkan dari berkas PROPOSAL_DISERTASI_TANPA_MODERATOR).** "
 "Setiap responden menetapkan satu influencer yang telah diikutinya sekurang-kurangnya **enam bulan**, "
 "dan satu merek yang pernah direkomendasikan influencer tersebut serta dikenal responden. Syarat lama "
 "mengikuti influencer dimaksudkan agar relasi yang diukur relatif stabil. Penetapan pasangan influencer–merek "
 "dilakukan sebelum responden melihat butir luaran, untuk mengurangi pemilihan merek berdasarkan preferensi jawaban. "
 "Bila tidak ada merek yang memenuhi syarat, pengisian dihentikan dan jawaban parsial tidak disimpan sebagai data utama.",
 "",
]

GAMBAR_NOTE = [
 "<!-- Gambar 1 (Model Mediasi Berurutan) dan Gambar 2 (Alur Pelaksanaan Penelitian) ditempatkan di sini. -->",
 "",
]


PUSTAKA_TAHUN = re.compile(r"\((?:19|20)\d{2}[a-z]?\)")
PUSTAKA_AWAL = re.compile(r"^[A-Z][A-Za-zÀ-ÿ’'\-]+,\s+[A-Z]\.")
PUSTAKA_NAMA = re.compile(r"^[A-Z][A-Za-zÀ-ÿ’'\-]+[.,]\s")


def _blok_pustaka(k: str) -> list[str]:
    baris = SRC[k]
    mulai = [i for i, l in enumerate(baris) if re.match(r"^DAFTAR PUSTAKA\s*$", l.strip(), re.I)]
    if not mulai:
        return []
    i = mulai[-1]
    for j in range(i + 1, len(baris)):
        if re.match(r"^(LAMPIRAN|Lampiran\s+\d+|DAFTAR LAMPIRAN)\b", baris[j].strip(), re.I):
            return baris[i + 1:j]
    return baris[i + 1:]


def _awal_entri(s: str) -> bool:
    return bool(PUSTAKA_AWAL.match(s) or (PUSTAKA_TAHUN.search(s) and PUSTAKA_NAMA.match(s)))


def pustaka_per_berkas(k: str) -> list[str]:
    entri: list[str] = []
    kini = None
    for l in _blok_pustaka(k):
        s = l.strip()
        if not s:
            continue
        if _awal_entri(s):
            if kini:
                entri.append(re.sub(r"\s+", " ", kini))
            kini = s
        elif kini is not None:
            kini += " " + s
    if kini:
        entri.append(re.sub(r"\s+", " ", kini))
    return entri


def _kunci_pustaka(e: str) -> tuple[str, str]:
    m = re.match(r"^([A-Za-zÀ-ÿ’'\-]+)", e)
    th = PUSTAKA_TAHUN.search(e)
    return (m.group(1).lower() if m else e[:20].lower(), th.group(0) if th else "?")


def gabung_pustaka() -> tuple[list[str], dict]:
    """Gabungkan daftar pustaka A+B+C; berkas induk (A) menang bila entri sama."""
    per = {k: pustaka_per_berkas(k) for k in "ABC"}
    gab: dict[tuple[str, str], tuple[str, str]] = {}
    asal: dict[tuple[str, str], set[str]] = {}
    for k in "ABC":
        for e in per[k]:
            c = _kunci_pustaka(e)
            asal.setdefault(c, set()).add(k)
            gab.setdefault(c, (e, k))

    def urut(c):
        n = unicodedata.normalize("NFKD", c[0]).encode("ascii", "ignore").decode()
        return (n, c[1])

    entri = [gab[c][0] for c in sorted(gab, key=urut)]
    stat = {
        "per_berkas": {k: len(v) for k, v in per.items()},
        "unik": len(entri),
        "tumpang_tindih": sum(1 for c, v in asal.items() if len(v) > 1),
        "hanya": {k: sum(1 for c, v in asal.items() if v == {k}) for k in "ABC"},
    }
    return entri, stat


def main() -> None:
    md: list[str] = []

    # ---------------------------------------------------------- halaman judul
    md += [
        "# MODEL PEMBENTUKAN ADVOKASI MEREK DIGITAL MELALUI KREDIBILITAS INFLUENCER PADA GENERASI Z DI SULAWESI UTARA",
        "",
        "**USULAN RISET DISERTASI**",
        "",
        "Diajukan pada Program Studi Doktor Ilmu Manajemen",
        "Pascasarjana Universitas Sam Ratulangi",
        "",
        "**Michael Ch. Raintung**",
        "NIM 252031130016",
        "",
        "PROGRAM STUDI DOKTOR ILMU MANAJEMEN",
        "PASCASARJANA UNIVERSITAS SAM RATULANGI",
        "MANADO",
        "2026",
        "",
        "<!-- pagebreak -->",
        "",
    ]

    # ---------------------------------------------------------- ringkasan
    ring = SRC["A"][14:33]
    md += ["# RINGKASAN PROPOSAL", ""] + emit(reflow(ring)) + [
        "",
        "Validitas diskriminan antarkonstruk — khususnya pasangan yang berdekatan secara konseptual — diuji dan "
        "dilaporkan dengan interval kepercayaan, bukan hanya direncanakan.",
        "",
        "<!-- pagebreak -->",
        "",
    ]

    def keluarkan(induk_re: str, sisipan: dict | None = None, akhir_tambahan: list[str] | None = None) -> None:
        nonlocal md
        md.append("## " + judul_induk("A", induk_re))
        md.append("")
        pengantar = reflow(pengantar_induk("A", induk_re))
        if pengantar:
            md += emit(pengantar) + [""]
        for judul, baris in bagian_anak("A", induk_re):
            md += emit(reflow(baris))
            if sisipan:
                for pola, blok in sisipan.items():
                    if re.match(pola, judul):
                        md += [""] + blok + [""]
            md.append("")
        if akhir_tambahan:
            md += akhir_tambahan

    # ---------------------------------------------------------- BAB I
    md += ["# BAB I. PENDAHULUAN", ""]
    keluarkan(r"^A\.\s*Latar Belakang Riset",
              sisipan={"^3\.": emit(reflow(blok_mentah("C", r"Gejala empiris di lapangan")))}) 
    keluarkan(r"^B\.\s*Rumusan Masalah")
    keluarkan(r"^C\.\s*Maksud atau Tujuan Riset")
    keluarkan(r"^D\.\s*Manfaat Riset")
    keluarkan(r"^E\.\s*Hipotesis")
    md += ["<!-- pagebreak -->", ""]

    # ---------------------------------------------------------- BAB II
    md += ["# BAB II. TINJAUAN PUSTAKA DAN KERANGKA PEMIKIRAN", ""]
    keluarkan(r"^A\.\s*Tinjauan Pustaka", sisipan={"^9\.": T1})
    keluarkan(r"^B\.\s*Kerangka Pemikiran", sisipan={"^5\.": GAMBAR_NOTE + T2 + T3 + T4})
    md += ["<!-- pagebreak -->", ""]

    # ---------------------------------------------------------- BAB III
    md += ["# BAB III. METODOLOGI RISET", ""]
    keluarkan(r"^A\.\s*Sumber Data, Subjek, Objek", sisipan={"^2\.": KRITERIA_INKLUSI})
    keluarkan(r"^B\.\s*Metode", sisipan={"^4\.": T5, "^5\.": T6})
    keluarkan(r"^C\.\s*Prosedur Riset")
    keluarkan(r"^D\.\s*Analisis Data", sisipan={"^2\.": T7, "^5\.": T8}, akhir_tambahan=KOVARIAT)
    md += ["<!-- pagebreak -->", ""]

    # ---------------------------------------------------------- daftar pustaka
    entri_pustaka, stat_pustaka = gabung_pustaka()
    PUSTAKA_STAT.update(stat_pustaka)
    md += ["<!-- pagebreak -->", "", "# DAFTAR PUSTAKA", "",
           f"*Daftar ini merupakan gabungan rujukan ketiga berkas (A: {stat_pustaka['per_berkas']['A']}, "
           f"B: {stat_pustaka['per_berkas']['B']}, C: {stat_pustaka['per_berkas']['C']} entri) yang sudah "
           f"dibersihkan dari duplikasi — {stat_pustaka['unik']} rujukan unik, urut abjad. "
           "Periksa kembali kesesuaian gaya selingkung (APA) dan keberadaan seluruh sitasi dalam teks.*", ""]
    for e in entri_pustaka:
        md += [e, ""]

    # ---------------------------------------------------------- lampiran
    md += ["<!-- pagebreak -->", "", "# LAMPIRAN", ""]
    for nama, pola in [("Lampiran 1", r"^Lampiran 1\."),
                       ("Lampiran 2", r"^Lampiran 2\."),
                       ("Lampiran 3", r"^Lampiran 3\."),
                       ("Lampiran 4", r"^Lampiran 4\."),
                       ("Lampiran 5", r"^Lampiran 5\.")]:
        blok = blok_dari("A", pola)
        md += emit(reflow(blok), geser=1) + [""]           # judul lampiran jadi Heading 2
    md += ["## Lampiran 6. Protokol Praregistrasi dan Daftar Periksa Analisis", "",
           "Butir-butir praregistrasi berikut diambil dari berkas PROPOSAL_DISERTASI_TANPA_MODERATOR dan "
           "disarankan dilampirkan utuh dari berkas sumbernya:", "",
           "1. Penetapan definisi konstruk, dimensi, dan sumber setiap butir.",
           "2. Penyimpanan versi kuesioner setelah terjemahan, penilaian ahli, dan wawancara kognitif.",
           "3. Penetapan lima hipotesis, kriteria responden, ukuran sampel, serta aturan keputusan sebelum data dikumpulkan.",
           "4. Pencatatan cara mengevaluasi kualitas pengukuran dan menguji efek tidak langsung.",
           "5. Kelengkapan persetujuan etik, lembar informasi, dan prosedur penanganan data.", ""]

    # ---------------------------------------------------------- catatan integrasi
    md += ["<!-- pagebreak -->", "", (pathlib.Path(__file__).parent.parent / "catatan-integrasi.md").read_text(encoding="utf-8")]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(bersih_artefak("\n".join(md)) + "\n", encoding="utf-8")
    print(f"Ditulis: {OUT}")
    print(f"  {len(md):,} baris markdown · {sum(len(x) for x in md):,} karakter")
    print(f"  baris tabel: {sum(1 for x in md if x.startswith('|'))}")
    if PUSTAKA_STAT:
        print(f"  daftar pustaka: {PUSTAKA_STAT['unik']} unik dari "
              f"A{PUSTAKA_STAT['per_berkas']['A']} + B{PUSTAKA_STAT['per_berkas']['B']} + "
              f"C{PUSTAKA_STAT['per_berkas']['C']} (hanya A: {PUSTAKA_STAT['hanya']['A']}, "
              f"hanya C: {PUSTAKA_STAT['hanya']['C']})")


if __name__ == "__main__":
    main()
