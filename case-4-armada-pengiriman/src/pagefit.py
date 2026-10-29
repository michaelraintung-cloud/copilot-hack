"""Estimator tata letak halaman untuk dokumen Word (A4, Times New Roman).

Memakai tabel lebar glyph Times (metrik identik dengan Times New Roman) sehingga
pemenggalan baris meniru Word: baris dipecah pada spasi hingga lebar area teks
habis. Tinggi baris dihitung dari metrik font:
    tinggi satu spasi = (ascent - descent + lineGap) / unitsPerEm * ukuran
Untuk Times: (1825 + 443 + 87) / 2048 = 1,1499 em.
Spasi 1,5 pada 12 pt karenanya 20,7 pt — sama dengan dokumen acuan.

Dipakai build_final.py untuk memastikan isi BAB I-VI tidak melewati batas halaman
sebelum berkas .docx benar-benar dibuka di Word.
"""
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_HERE, "font_metrics.json"), encoding="utf-8") as fh:
    WIDTHS = json.load(fh)

LINE_FACTOR = 1.1499           # tinggi baris satu spasi, dalam em
A4_W, A4_H = 595.276, 841.890  # pt


def text_width(text, size=12.0, style="regular"):
    table = WIDTHS[style]
    total = 0.0
    for ch in text:
        total += table.get(ch, 0.5)
    return total * size


def count_lines(text, width, size=12.0, style="regular"):
    """Jumlah baris hasil pemenggalan rakus (greedy) seperti Word."""
    if not text.strip():
        return 1
    lines, cur = 1, 0.0
    space = WIDTHS[style].get(" ", 0.25) * size
    for word in text.split():
        w = text_width(word, size, style)
        if cur == 0.0:
            cur = w
        elif cur + space + w <= width:
            cur += space + w
        else:
            lines += 1
            cur = w
    return lines


class Layout:
    """Simulasi aliran blok pada halaman A4 dengan margin dan spasi tertentu."""

    def __init__(self, margin_cm=2.54, top_cm=None, bottom_cm=None):
        self.left = self.right = margin_cm / 2.54 * 72
        self.top = (top_cm if top_cm is not None else margin_cm) / 2.54 * 72
        self.bottom = (bottom_cm if bottom_cm is not None else margin_cm) / 2.54 * 72
        self.width = A4_W - self.left - self.right
        self.height = A4_H - self.top - self.bottom
        self.page = 1
        self.y = 0.0          # terpakai dari atas area teks
        self.blocks = []      # catatan untuk debug

    # --- inti -----------------------------------------------------------
    def _line_h(self, size, multiple=1.5):
        return LINE_FACTOR * size * multiple

    def space(self, pts):
        """Ruang vertikal murni (spasi antar paragraf)."""
        if pts:
            self.y += pts

    def new_page(self):
        self.page += 1
        self.y = 0.0

    def _ensure(self, h):
        if self.y + h > self.height and self.y > 0:
            self.new_page()

    def para(self, text, size=12.0, style="regular", multiple=1.5,
             space_before=0.0, space_after=0.0, indent_cm=0.0,
             keep_with_next=False, debug=""):
        indent = indent_cm / 2.54 * 72
        lines = count_lines(text, self.width - indent, size, style)
        h = lines * self._line_h(size, multiple)
        self.y += space_before
        # paragraf harus utuh di satu halaman bila muat; jika tidak, ia mengalir
        self._ensure(min(h, self.height))
        start_page = self.page
        remaining = lines
        while remaining:
            avail = self.height - self.y
            fit = int(avail // self._line_h(size, multiple))
            if fit <= 0:
                self.new_page()
                continue
            take = min(fit, remaining)
            self.y += take * self._line_h(size, multiple)
            remaining -= take
            if remaining:
                self.new_page()
        self.y += space_after
        self.blocks.append((start_page, self.page, len(text), lines, debug))
        return lines

    def heading(self, text, size=12.0, space_before=12.0, space_after=6.0,
                multiple=1.5, debug=""):
        self.y += space_before
        self._ensure(self._line_h(size, multiple))
        lines = self.para(text, size=size, style="bold", multiple=multiple,
                          space_after=space_after, debug=debug or "heading")
        return lines

    def table(self, rows, widths_cm, size=10.0, header=True, cell_pad_cm=0.19,
              multiple=1.0, space_before=4.0, space_after=6.0, repeat_header=True):
        """rows: list of list of str. widths_cm: lebar kolom (cm)."""
        pad = 2 * cell_pad_cm / 2.54 * 72
        line_h = self._line_h(size, multiple)
        heights = []
        for row in rows:
            n = 1
            for cell, w in zip(row, widths_cm):
                n = max(n, count_lines(str(cell), w / 2.54 * 72 - pad, size))
            heights.append(n * line_h + 2.0)  # + padding vertikal sel
        self.y += space_before

        i = 0
        while i < len(rows):
            h = heights[i]
            if self.y + h > self.height:
                self.new_page()
                if repeat_header and header and i > 0:
                    self.y += heights[0]
                    if self.y + heights[i] > self.height:
                        self.new_page()
            if self.y + h > self.height:
                self.new_page()
            self.y += h
            i += 1
        self.y += space_after
        self.blocks.append((None, None, 0, 0, f"tabel {len(rows)}x{len(widths_cm)}"))

    def figure(self, height_cm, space_before=6.0, space_after=6.0):
        h = height_cm / 2.54 * 72
        self.y += space_before
        self._ensure(h)
        self.y += h
        self.y += space_after

    def page_break(self):
        self.new_page()

    def summary(self):
        return self.page, self.y / self.height
