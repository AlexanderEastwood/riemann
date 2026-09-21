# `evidence/v126/g2_certificate/`

Manuscript v1.12 checkpoint — CERTIFICATE bundle: Arb interval certificate for the exact finite Weil matrix at lambda=3, N=64, plus a second certificate from the analytic archimedean series and a rational full-space complement (768-bit interval data included). Linked from the research map as the lambda=3 window evidence (`prop:v116-window-positive`).

The files here are byte-identical to [`evidence/v124/g2_certificate/`](../../v124/g2_certificate/).

**Start here:** [`G2_Finite_Certificate.md`](G2_Finite_Certificate.md)

## Files

- `G2_Finite_Certificate.md` (5 KB) — Certified finite Weil matrix — v1.12 checkpoint
- `certify_g2_finite.py` (7 KB) — Arb interval certificate for the exact finite Weil matrix lambda=3,N=64. Requires python-flint==0.9.0 and g2_finite_candidate.json.
- `certify_g2_series.py` (5 KB) — Second certificate: analytic arch series and a rational full-space complement. No numerical integration or Householder coordinates.
- `g2_finite_candidate.json` (8 KB) — (no description in file)
- `g2_finite_certificate.json` (11 KB) — (no description in file)
- `g2_finite_matrix_intervals.json` (1.3 MB) — (no description in file)
- `g2_finite_series_certificate.json` (11 KB) — (no description in file)
- `g2_finite_series_intervals.json` (26 KB) — (no description in file)
- `make_g2_finite_candidate.py` (1 KB) — Freeze a rational candidate. This generator is not a true-PSWF certificate. The output decimal strings DEFINE the exact rational candidate subsequently certified, regardl…
