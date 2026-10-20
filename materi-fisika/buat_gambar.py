#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Membuat gambar grafik bersih untuk dokumen pembahasan soal."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle

BASE = Path(__file__).resolve().parent
OUT = BASE / "gambar"
OUT.mkdir(exist_ok=True)

MERAH = "#8b1a1a"
BIRU = "#1f4e79"
ABU = "#4a4a4a"
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.edgecolor": "#555555",
    "axes.linewidth": 1.1,
    "axes.labelcolor": "#222222",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
})


# ---------------------------------------------------------------- Gbr 7-40
def fig_7_40():
    x_pts = [0, 1, 4, 6, 8, 9]
    a_pts = [0, 6, 6, -6, -6, 0]
    fig, ax = plt.subplots(figsize=(6.4, 3.0), dpi=220)

    for yv in (-6, 6):
        ax.annotate("", xy=(9.6, yv), xytext=(0, yv),
                    arrowprops=dict(arrowstyle="-", color="#bbbbbb",
                                    lw=0.9, linestyle=(0, (4, 3))))
    ax.axhline(0, color="#666666", lw=1.2)
    ax.axvline(0, color="#666666", lw=1.2)

    # daerah positif / negatif
    ax.fill_between([0, 1, 4, 5], [0, 6, 6, 0], color="#c9d8e8", alpha=0.55, lw=0)
    ax.fill_between([5, 6, 8, 9], [0, -6, -6, 0], color="#e8cfcf", alpha=0.6, lw=0)

    ax.plot(x_pts, a_pts, color=MERAH, lw=2.2, solid_joinstyle="miter")

    for xv in range(1, 9):
        ax.axvline(xv, color="#e2e2e2", lw=0.7, zorder=0)

    ax.set_xlim(-0.6, 9.8)
    ax.set_ylim(-8.6, 8.6)
    ax.set_xticks([2, 4, 6, 8])
    ax.set_yticks([6, 0, -6])
    ax.set_yticklabels(["$a_s$", "0", "$-a_s$"])
    ax.set_xlabel("$x$ (m)")
    ax.set_ylabel("$a$ (m/s$^2$)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="both", length=3)

    ax.text(2.5, 3.4, "luas +", color=BIRU, fontsize=8.5, ha="center")
    ax.text(7.0, -4.2, "luas −", color=MERAH, fontsize=8.5, ha="center")
    fig.tight_layout()
    fig.savefig(OUT / "gbr-7-40.png", bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- Gbr 6-38
def fig_6_38():
    x_pts = [0, 3, 7, 10, 11.5, 13.5, 15]
    f_pts = [0, 400, 400, 0, -200, -200, 0]
    fig, ax = plt.subplots(figsize=(6.4, 3.2), dpi=220)

    ax.axhline(0, color="#666666", lw=1.2)
    ax.axvline(0, color="#666666", lw=1.2)
    ax.fill_between([0, 3, 7, 10], [0, 400, 400, 0], color="#c9d8e8", alpha=0.55, lw=0)
    ax.fill_between([10, 11.5, 13.5, 15], [0, -200, -200, 0], color="#e8cfcf",
                    alpha=0.6, lw=0)
    ax.plot(x_pts, f_pts, color=MERAH, lw=2.2, solid_joinstyle="miter")

    ax.set_xlim(-0.8, 16.2)
    ax.set_ylim(-330, 520)
    ax.set_xticks(range(0, 16))
    ax.set_yticks([-200, -100, 0, 100, 200, 300, 400])
    ax.set_xlabel("$x$ (m)")
    ax.set_ylabel("$F_x$ (N)")
    ax.grid(axis="x", color="#ececec", lw=0.7)
    ax.grid(axis="y", color="#f2f2f2", lw=0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.annotate("400 N", xy=(5, 400), xytext=(5, 448),
                ha="center", fontsize=8.5, color=BIRU)
    ax.annotate("−200 N", xy=(12.5, -200), xytext=(12.5, -285),
                ha="center", fontsize=8.5, color=MERAH)
    for x0, x1, label in ((0, 10, "(a)"), (10, 15, "(b)")):
        ax.annotate("", xy=(x0, 130), xytext=(x1, 130),
                    arrowprops=dict(arrowstyle="<->", color="#777777", lw=1))
        ax.text((x0 + x1) / 2, 160, f"{label} {x1 - x0:.0f} m",
                ha="center", fontsize=8.5, color="#555555")
    fig.tight_layout()
    fig.savefig(OUT / "gbr-6-38.png", bbox_inches="tight")
    plt.close(fig)


# ------------------------------------------------------- bola dan pegas
def fig_bola_pegas():
    fig, ax = plt.subplots(figsize=(6.0, 4.2), dpi=220)
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.5, 9.0)
    ax.axis("off")

    def spring(cx, top, bottom, coils=6, width=0.5):
        ys = np.linspace(top, bottom, coils * 2 + 1)
        xs = []
        for i, _ in enumerate(ys):
            xs.append(cx if i in (0, len(ys) - 1)
                      else cx + width * (1 if i % 2 else -1))
        ax.plot(xs, ys, color="#444444", lw=1.5)

    def ground(x0):
        ax.plot([x0, x0 + 1.5], [0.6, 0.6], color="#222222", lw=2.4)

    # panel (a): bola h di atas pegas
    ground(1.3)
    ax.add_patch(plt.Circle((2.05, 7.35), 0.45, color="#b03a2e"))
    spring(2.05, 5.2, 0.6)
    ax.plot([1.3, 2.9], [5.2, 5.2], ls=(0, (3, 3)), color="#777777", lw=0.9)
    ax.annotate("", xy=(0.95, 6.9), xytext=(0.95, 5.2),
                arrowprops=dict(arrowstyle="<->", color="#444444", lw=1))
    ax.text(0.75, 6.05, "$h$", fontsize=11, ha="right",
            bbox=dict(fc="white", ec="none", pad=1))
    ax.text(2.05, -0.25, "(a) dilepas dari diam", ha="center", fontsize=8.5)

    # panel (b): tepat menyentuh pegas
    ground(4.9)
    ax.add_patch(plt.Circle((5.65, 5.65), 0.45, color="#b03a2e"))
    spring(5.65, 5.2, 0.6)
    ax.plot([4.9, 6.5], [5.2, 5.2], ls=(0, (3, 3)), color="#777777", lw=0.9)
    ax.text(6.7, 5.05, "$y_2 = 0$", fontsize=9, color="#444444")
    ax.text(5.65, -0.25, "(b) menyentuh pegas", ha="center", fontsize=8.5)

    # panel (c): pegas tertekan maksimum
    ground(8.2)
    ax.add_patch(plt.Circle((8.95, 3.65), 0.45, color="#b03a2e"))
    spring(8.95, 3.2, 0.6, coils=4)
    ax.plot([8.2, 9.8], [5.2, 5.2], ls=(0, (3, 3)), color="#777777", lw=0.9)
    ax.plot([8.2, 9.8], [3.2, 3.2], ls=(0, (3, 3)), color="#777777", lw=0.9)
    ax.annotate("", xy=(9.75, 5.2), xytext=(9.75, 3.2),
                arrowprops=dict(arrowstyle="<->", color="#444444", lw=1))
    ax.text(9.62, 4.2, "$Y$", fontsize=11, ha="right",
            bbox=dict(fc="white", ec="none", pad=1))
    ax.text(8.95, -0.25, "(c) mampatan maksimum", ha="center", fontsize=8.5)

    ax.plot([2.05, 9.9], [7.35 + 0.45, 7.35 + 0.45], ls=(0, (3, 3)),
            color="#c4c4c4", lw=0.8)
    ax.text(9.95, 7.55, "$y_1 = h$", fontsize=9, color="#888888", ha="right")
    fig.tight_layout()
    fig.savefig(OUT / "gbr-bola-pegas.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig_7_40()
    fig_6_38()
    fig_bola_pegas()
    for p in sorted(OUT.glob("*.png")):
        print(p.name, round(p.stat().st_size / 1024, 1), "KB")
