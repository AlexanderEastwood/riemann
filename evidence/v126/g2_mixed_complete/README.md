# `evidence/v126/g2_mixed_complete/`

Manuscript v1.23 — CERTIFICATE bundle: complete mixed correlations and a monotone corrected head metric; `mixed_directional_check.py` is a rigorous one-direction lower test at 768/896 bits that, per its docstring, "tests a sufficient upper-bound method, not Weil positivity".

The files here are byte-identical to [`evidence/v124/g2_mixed_complete/`](../../v124/g2_mixed_complete/).

**Start here:** [`mixed_complete_integration_review.md`](mixed_complete_integration_review.md), [`adversarial_mixed_refinement.md`](adversarial_mixed_refinement.md)

## Subdirectories

- [`input/`](input/) — v1.22 input manuscript
- [`renders/`](renders/) — contact-sheet renders

## Files

- `adversarial_mixed_refinement.md` (10 KB) — Complete mixed terms and a monotone corrected head metric
- `build_complete_pdf.py` (1 KB) — Compile in a fresh directory; install only a closed, parseable full PDF.
- `finite_polynomial_diagnostics_J65536_b768.json` (2 KB) — (no description in file)
- `integrate_v123.py` (5 KB) — Integrate supported mixed-correction results into the complete v1.22.
- `mixed_complete_insert.tex` (10 KB) — Complete mixed correlations and a monotone head refinement
- `mixed_complete_integration_review.md` (5 KB) — Adversarial review of the v1.23 mixed-term insertion
- `mixed_directional_J65536_b768.json` (2 KB) — (no description in file)
- `mixed_directional_J65536_b896.json` (2 KB) — (no description in file)
- `mixed_directional_check.py` (4 KB) — Rigorous one-direction lower test for the complete first-polynomial bound. This tests a sufficient upper-bound method, not Weil positivity.
- `mixed_directional_witness_J65536.json` (24 KB) — (no description in file)
- `mixed_probe_J65536_b768.json` (3 KB) — (no description in file)
- `mixed_probe_J65536_b896.json` (3 KB) — (no description in file)
- `mixed_refinement.py` (6 KB) — Directional mixed inverse diagnostic, with exact frozen inputs and Arb actions. Finite-prefix mixed values are explicitly NOT complete-tail certificates.
- `mixed_vectors_J65536_b768.json` (228 KB) — (no description in file)
- `mixed_vectors_J65536_b896.json` (238 KB) — (no description in file)
- `package_v123.py` (5 KB) — (no description in file)
- `refine_inverse.py` (5 KB) — Reproducible Arb experiments for the complete lambda=4 tail inverse. Finite-prefix experiments are not certificates of the complete Schur sign.
