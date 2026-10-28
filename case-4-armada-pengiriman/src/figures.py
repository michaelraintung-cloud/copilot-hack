"""Membuat gambar (figures) untuk laporan Studi Kasus 4."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import matplotlib.patheffects as pe
import model as m

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 8,
    "axes.edgecolor": "#404040",
    "axes.labelcolor": "#1F3864",
    "savefig.dpi": 300,
    "figure.dpi": 120,
})

NAVY = "#1F3864"
BLUE = "#2E75B6"
LIGHT = "#DEEAF6"
ORANGE = "#C55A11"
RED = "#C00000"
GREY = "#595959"
GREEN = "#375623"
OUT = "../figures"


def box(ax, x, y, w, h, text, fc=LIGHT, ec=NAVY, fs=6.6, bold=False, tc=NAVY):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.004,rounding_size=0.012",
                       linewidth=0.9, edgecolor=ec, facecolor=fc, zorder=3)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            color=tc, fontweight="bold" if bold else "normal", zorder=4, linespacing=1.25)


def arrow(ax, p1, p2, color=NAVY, style="-|>", ls="-", lw=0.9, rad=0.0):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=7,
                                 linewidth=lw, color=color, linestyle=ls,
                                 connectionstyle=f"arc3,rad={rad}", zorder=2,
                                 shrinkA=1, shrinkB=1))


# ---------------------------------------------------------------- Gambar 2.1
def fig_alur():
    fig, ax = plt.subplots(figsize=(6.3, 3.55))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    langkah = [
        ("1", "Pesanan diterima\n(retail & bisnis)"),
        ("2", "Pengelompokan\npesanan manual"),
        ("3", "Penyusunan rute\n(peta + daftar)"),
        ("4", "Penetapan muatan\n& keberangkatan"),
        ("5", "Pengiriman\n(kondisi lapangan)"),
        ("6", "Serah terima\n& bukti kertas"),
        ("7", "Pelaporan &\npenagihan"),
        ("8", "Evaluasi\n(tidak terukur)"),
    ]
    w, h, gx = 0.200, 0.115, 0.045
    x0, ytop, ybot = 0.035, 0.735, 0.435
    pos = []
    for i, (no, teks) in enumerate(langkah):
        row, col = divmod(i, 4)
        x = x0 + col * (w + gx)
        y = ytop if row == 0 else ybot
        # baris kedua mengalir dari kanan ke kiri
        if row == 1:
            x = x0 + (3 - col) * (w + gx)
        box(ax, x, y, w, h, teks, fc="#F2F7FC" if row else LIGHT, fs=6.4)
        ax.text(x + 0.017, y + h - 0.023, no, ha="center", va="center", fontsize=6.2,
                color="white", fontweight="bold", zorder=6,
                bbox=dict(boxstyle="circle,pad=0.22", fc=BLUE, ec="none"))
        pos.append((x, y))

    for i in range(3):
        arrow(ax, (pos[i][0] + w, pos[i][1] + h / 2), (pos[i + 1][0], pos[i + 1][1] + h / 2))
    arrow(ax, (pos[3][0] + w / 2, ytop), (pos[3][0] + w / 2, ybot + h))
    arrow(ax, (pos[4][0], ybot + h / 2), (pos[5][0] + w, ybot + h / 2))
    for i in range(4, 7):
        arrow(ax, (pos[i][0], pos[i][1] + h / 2), (pos[i + 1][0] + w, pos[i + 1][1] + h / 2))

    # penanda titik masalah
    titik = [
        (3, "P1", "Rute mengikuti urutan pesanan masuk, bukan\nkedekatan lokasi → backtracking"),
        (3, "P3", "Pelanggan tidak menerima ETA yang akurat\n→ jadwal penerimaan berubah"),
        (4, "P2", "Posisi kendaraan tidak terpantau; keterlambatan\nbaru diketahui setelah pengemudi menelepon"),
        (5, "P4", "Bukti serah terima manual → sengketa dan\nrekonsiliasi lambat"),
        (7, "P5", "Tidak ada data jarak, waktu, dan ketepatan\n→ keputusan tanpa baseline"),
    ]
    ax.text(0.035, 0.362, "Titik kegagalan proses (pain points)", fontsize=7,
            fontweight="bold", color=RED)
    for i, (_, kode, teks) in enumerate(titik):
        kol = i % 2
        baris = i // 2
        x = 0.035 + kol * 0.485
        y = 0.283 - baris * 0.088
        ax.text(x, y, kode, fontsize=6.4, fontweight="bold", color="white", va="center",
                bbox=dict(boxstyle="round,pad=0.26", fc=RED, ec="none"))
        ax.text(x + 0.055, y, teks, fontsize=6.3, color="#333333", va="center", linespacing=1.25)

    ax.annotate("", xy=(0.035, 0.735), xytext=(0.035, 0.56),
                arrowprops=dict(arrowstyle="-", lw=0.6, ls=(0, (3, 2)), color=GREY))
    plt.tight_layout(pad=0.15)
    fig.savefig(f"{OUT}/gambar-2-1-alur-proses.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Gambar 3.1
def fig_fishbone():
    import textwrap
    fig, ax = plt.subplots(figsize=(6.4, 3.95))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")

    ys, ekor = 0.505, 0.325
    x_ujung_spine = 0.735
    ax.plot([0.004, x_ujung_spine - 0.012], [ys, ys], color=NAVY, lw=1.7,
            zorder=1, solid_capstyle="round")
    arrow(ax, (x_ujung_spine - 0.020, ys), (x_ujung_spine + 0.004, ys), color=NAVY, lw=1.7)

    bx0 = 0.742
    ax.add_patch(FancyBboxPatch((bx0, ys - 0.150), 0.253, 0.300,
                 boxstyle="round,pad=0.006,rounding_size=0.02",
                 linewidth=1.0, edgecolor=RED, facecolor="#FBE9E9", zorder=3))
    ax.text(bx0 + 0.1265, ys + 0.082, "AKIBAT", ha="center", va="center",
            fontsize=6.6, fontweight="bold", color=RED)
    ax.text(bx0 + 0.1265, ys - 0.030,
            "Jarak tempuh tidak efisien,\npengiriman terlambat, dan\nbiaya layanan meningkat\n(±Rp611 juta/tahun)",
            ha="center", va="center", fontsize=5.7, color="#333333", linespacing=1.35)

    atas = [
        ("METODE", [
            "Rute mengikuti urutan pesanan masuk",
            "Tidak ada standar pengelompokan wilayah",
            "Tidak ada evaluasi rute harian",
        ], 0.105),
        ("MANUSIA", [
            "Pengetahuan rute melekat pada 2 dispatcher",
            "Pengemudi tidak dilibatkan dalam desain sistem",
            "Beban kerja memuncak pada jam sibuk",
        ], 0.295),
        ("TEKNOLOGI & DATA", [
            "Tidak ada optimasi urutan kunjungan",
            "Tidak ada pelacakan posisi kendaraan",
            "Master data toko belum terstruktur",
        ], 0.485),
    ]
    bawah = [
        ("KENDARAAN & MUATAN", [
            "Kapasitas muatan tidak dipertimbangkan",
            "Waktu bongkar muat tinggi",
        ], 0.200),
        ("LINGKUNGAN", [
            "Kemacetan tidak terprediksi",
            "Jadwal penerimaan toko berubah-ubah",
            "Akses jalan lokal sempit",
        ], 0.390),
        ("PENGUKURAN & KEBIJAKAN", [
            "Tidak ada KPI jarak dan OTIF",
            "Tidak ada insentif ketepatan waktu",
            "Umpan balik lapangan tidak tercatat",
        ], 0.580),
    ]

    def gambarkan(daftar, arah):
        for judul, butir, x in daftar:
            y_ujung = ys + arah * ekor
            ax.plot([x, x], [ys, y_ujung], color=BLUE, lw=1.3, zorder=1,
                    solid_capstyle="round")
            ax.text(x, y_ujung + arah * 0.034, judul, ha="center",
                    va="bottom" if arah > 0 else "top", fontsize=6.1, fontweight="bold",
                    color="white",
                    bbox=dict(boxstyle="round,pad=0.32", fc=NAVY, ec="none"), zorder=5)
            baris = []
            for b in butir:
                baris += textwrap.wrap(b, 21)
            if arah > 0:
                baris = baris[::-1]
            y = ys + arah * 0.038
            for t in baris:
                ax.text(x + 0.010, y, t, ha="left", va="center", fontsize=5.4,
                        color="#333333")
                y += arah * 0.0322

    gambarkan(atas, +1)
    gambarkan(bawah, -1)
    ax.text(0.004, 0.995, "Diagram sebab–akibat (fishbone) keterlambatan pengiriman",
            fontsize=6.9, fontweight="bold", color=NAVY, va="top")
    plt.tight_layout(pad=0.1)
    fig.savefig(f"{OUT}/gambar-3-1-fishbone.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Gambar 4.1
def fig_tornado():
    fig, ax = plt.subplots(figsize=(6.3, 3.05))
    data = [(lbl, lo, hi, nl, nh) for lbl, lo, hi, nl, nh in m.SENSITIVITAS]
    base = m.NPV_BASE
    ys = range(len(data))

    for y, (lbl, lo, hi, nl, nh) in zip(ys, data):
        ax.barh(y, (lo - base) / 1e6, left=base / 1e6, height=0.55,
                color="#9DC3E6", edgecolor=NAVY, linewidth=0.5, zorder=3)
        ax.barh(y, (hi - base) / 1e6, left=base / 1e6, height=0.55,
                color=BLUE, edgecolor=NAVY, linewidth=0.5, zorder=3)
        ax.text((min(lo, hi) - 3) / 1e6, y - 0.42, nl, va="center", ha="right",
                fontsize=5.5, color=GREY)
        ax.text((max(lo, hi) + 3) / 1e6, y - 0.42, nh, va="center", ha="left",
                fontsize=5.5, color=GREY)

    ax.axvline(base / 1e6, color=NAVY, lw=1.1, ls="--", zorder=4)
    ax.text(base / 1e6, -0.98, f"NPV basis Rp{base/1e6:,.0f} juta".replace(",", "."),
            ha="center", va="bottom", fontsize=6.3, color=NAVY, fontweight="bold")
    ax.set_yticks(list(ys))
    ax.set_ylim(len(data) - 0.35, -1.15)
    ax.set_yticklabels([d[0] for d in data], fontsize=6.4, color="#333333")
    ax.set_xlabel("NPV 3 tahun, diskonto 12% (Rp juta).  Batang gelap = skenario menguntungkan,\nbatang terang = skenario merugikan.", fontsize=6.4)
    ax.tick_params(axis="x", labelsize=6.2, colors=GREY)
    ax.grid(axis="x", color="#D9D9D9", lw=0.5, zorder=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#BFBFBF")
    plt.tight_layout(pad=0.2)
    fig.savefig(f"{OUT}/gambar-4-1-tornado.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Gambar 5.1
def fig_gantt():
    tugas = [
        # (label, mulai, durasi, warna)
        ("Fase 0  Pengukuran baseline & pengumpulan data", 1, 14, "#8FAADC"),
        ("Fase 1  Standar kerja, klaster wilayah, SOP rute", 15, 30, "#2E75B6"),
        ("Fase 1  Pemilihan vendor & konfigurasi sistem", 20, 26, "#2E75B6"),
        ("Fase 1  Pelatihan dispatcher & pengemudi", 30, 25, "#8FAADC"),
        ("Fase 2  Pilot 5 kendaraan (uji A/B)", 46, 25, "#375623"),
        ("Fase 2  Evaluasi pilot & kalibrasi parameter", 64, 12, "#375623"),
        ("Fase 3  Rollout 20 kendaraan & dashboard KPI", 71, 20, "#C55A11"),
        ("Fase 3  Serah terima ke operasional (handover)", 84, 7, "#C55A11"),
    ]
    fig, ax = plt.subplots(figsize=(6.3, 2.55))
    for i, (label, mulai, durasi, warna) in enumerate(tugas):
        ax.barh(i, durasi, left=mulai, height=0.52, color=warna,
                edgecolor="white", linewidth=0.6, zorder=3, alpha=0.95)
        ax.text(mulai + durasi / 2, i, f"{mulai}–{mulai+durasi-1}", ha="center", va="center",
                fontsize=5.2, color="white", fontweight="bold", zorder=4)
    ax.set_yticks(range(len(tugas)))
    ax.set_yticklabels([t[0] for t in tugas], fontsize=6.2, color="#333333")
    ax.invert_yaxis()

    gates = [(14, "G1\nKesiapan data"), (45, "G2\nBaseline & vendor"), (70, "G3\nHasil pilot"), (90, "G4\nGo/No-go")]
    for x, lbl in gates:
        ax.axvline(x, color=RED, lw=0.8, ls=(0, (2, 2)), zorder=2)
        ax.text(x, -0.85, lbl, ha="center", va="bottom", fontsize=5.4, color=RED,
                fontweight="bold", linespacing=1.2)

    ax.set_xlim(0, 95)
    ax.set_ylim(len(tugas) - 0.4, -1.35)
    ax.set_xticks([0, 15, 30, 45, 60, 75, 90])
    ax.set_xlabel("Hari kalender implementasi", fontsize=6.8)
    ax.tick_params(axis="x", labelsize=6.2, colors=GREY)
    ax.grid(axis="x", color="#E3E3E3", lw=0.5, zorder=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#BFBFBF")
    plt.tight_layout(pad=0.2)
    fig.savefig(f"{OUT}/gambar-5-1-gantt.png", bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig_alur()
    fig_fishbone()
    fig_tornado()
    fig_gantt()
    print("selesai")
