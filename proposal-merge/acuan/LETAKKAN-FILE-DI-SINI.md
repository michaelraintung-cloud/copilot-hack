# Letakkan berkas PDF di folder ini

Keenam berkas berikut dikelompokkan seperti ini:

**Kelompok 1 — dua file proposal (bahan penggabungan):**
- Proposal A: `Proposal Disertasi Michael Raintung - Revisi Seminar Proposal.pdf`
- Proposal B: `Proposal Disertasi Michael Raintung 14 Oktober 2026.pdf`

**Kelompok 2 — keluaran LeapSpace (acuan penilaian):**
- `Comparison_of_research_proposal_readiness_LeapSpace.pdf`
- `Evaluation_of_dissertation_proposal_completeness_LeapSpace.pdf`
- `Comparison_of_dissertation_proposal_versions_LeapSpace.pdf`
- `Integration_of_dissertation_proposal_documents_LeapSpace.pdf`

Setelah berkas ada di sini, jalankan:

```bash
cd proposal-merge
python3 tools/tangkap_pdf.py --folder acuan --out acuan/teks        # 1. ekstrak teks
python3 tools/analisis_dua_proposal.py \
  --a "acuan/teks/Proposal Disertasi Michael Raintung - Revisi Seminar Proposal.txt" \
  --b "acuan/teks/Proposal Disertasi Michael Raintung 14 Oktober 2026.txt" \
  --out hasil --nama-a "Revisi Seminar Proposal" --nama-b "Versi 14 Oktober 2026"
```

Berkas keluaran ada di `hasil/`. Mulai dari `hasil/laporan-tumpang-tindih.md`.
