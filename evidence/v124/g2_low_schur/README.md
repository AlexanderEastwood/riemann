# `evidence/v124/g2_low_schur/`

Manuscript v1.20 — CERTIFICATE bundle: the low-mode Schur revision at lambda=4 — certified far-inverse iteration constants (320/384 bits), the actual low-head Schur certificate and a structured inverse bound (768 bits), with frozen witnesses and Arb Weil-sequence enclosures. `check_structured_ceiling.py` replays exact dyadic counter-witnesses and, per its docstring, "does NOT certify a negative direction".

**Start here:** [`README_schur_revision.md`](README_schur_revision.md), [`adversarial_uniform_review.md`](adversarial_uniform_review.md)

## Subdirectories

- [`current/`](current/) — manuscript source snapshot

## Files

- `README_schur_revision.md` (2 KB) — v1.20 Schur revision: reproduction and scope
- `adversarial_uniform_review.md` (19 KB) — Adversarial review: the low Schur correction and growing-window scales
- `assembly_general.py` (3 KB) — Arb enclosures of the actual Weil Fourier coefficients at integer lambda.
- `build_complete_pdf.py` (1 KB) — Compile in a fresh directory; install only a closed, parseable full PDF.
- `certify_far_inverse.py` (2 KB) — Certify the complete far-operator inverse iteration constants at lambda=4. Analytic inputs: the manuscript's two-sided diagonal bound and commutator norm bound, with the…
- `certify_low_schur.py` (4 KB) — Actual low-head Schur certificate using the proved complete lambda4 tail metric.
- `check_structured_ceiling.py` (3 KB) — Replay exact dyadic obstructions to three structured lower-bound candidates. This checks K - V from the saved interval ingredients.
- `checkpoint.md` (9 KB) — Current research checkpoint: September 21, 2026 — v1.20 low-mode Schur revision
- `far_inverse_contraction_b320.json` (2 KB) — (no description in file)
- `far_inverse_contraction_b384.json` (2 KB) — (no description in file)
- `far_inverse_insert.tex` (4 KB) — (no description in file)
- `integrate_v120_schur.py` (6 KB) — (no description in file)
- `low_matrix_even_M256_b768.json` (114 KB) — (no description in file)
- `low_schur_even_M256_J2048_r64_b768.json` (682 B) — (no description in file)
- `low_witness_even_M256_b768.json.gz` (368 KB) — (no description in file)
- `package_revision.py` (4 KB) — (no description in file)
- `render_review.py` (1 KB) — (no description in file)
- `sequences_v3_l4_J2048_b768_k96.json` (1.5 MB) — (no description in file)
- `sequences_v3_l4_J4096_b768_k96.json` (2.9 MB) — (no description in file)
- `structured_ceiling_counterwitness.json` (2 KB) — (no description in file)
- `structured_ceiling_counterwitness_M1024.json` (2 KB) — (no description in file)
- `structured_ceiling_counterwitness_M512.json` (2 KB) — (no description in file)
- `structured_even_M1024_J4096_ingredients.json` (243 KB) — (no description in file)
- `structured_even_M1024_J4096_r64_b768_t0.json` (815 B) — (no description in file)
- `structured_even_M1024_J4096_r64_b768_t0_matrix.json` (121 KB) — (no description in file)
- `structured_even_M256_J4096_ingredients.json` (243 KB) — (no description in file)
- `structured_even_M256_J4096_r64_b768_t0.json` (815 B) — (no description in file)
- `structured_even_M256_J4096_r64_b768_t0_matrix.json` (121 KB) — (no description in file)
- `structured_even_M256_J4096_r64_b768_t8.json` (723 B) — (no description in file)
- `structured_even_M256_J4096_r64_b768_t8_matrix.json` (120 KB) — (no description in file)
- `structured_even_M256_midpoint_diagnostic.json` (1 KB) — (no description in file)
- `structured_even_M512_J4096_ingredients.json` (243 KB) — (no description in file)
- `structured_even_M512_J4096_r64_b768_t0.json` (814 B) — (no description in file)
- `structured_even_M512_J4096_r64_b768_t0_matrix.json` (121 KB) — (no description in file)
- `structured_even_M512_midpoint_diagnostic.json` (272 B) — (no description in file)
- `structured_inverse_insert.tex` (12 KB) — Reusing the signed tail certificate in the low-mode correction
- `structured_low_schur.py` (5 KB) — Structured inverse bound on the actual lambda=4 low-head Schur residual. All arithmetic entering a sign decision is Arb; frozen witnesses are dyadic.
