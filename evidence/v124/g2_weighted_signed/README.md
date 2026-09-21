# `evidence/v124/g2_weighted_signed/`

Manuscript v1.20 — CERTIFICATE bundle: one-sided signed energy certificates on the complete lambda=4 Fourier tail (`weighted_tail_l4_s16_{even,odd}` at 256/320 bits with frozen witnesses up to 41 MB) and the exact rational counterexample to two-sided norm contraction (`prop:v120-norm-counterexample`). `REPRODUCE_v120.md`: "It is not a G2 or RH certificate."

The files here are byte-identical to [`evidence/v126/g2_weighted_signed/`](../../v126/g2_weighted_signed/).

**Start here:** [`REPRODUCE_v120.md`](REPRODUCE_v120.md), [`adversarial_weighted_review.md`](adversarial_weighted_review.md)

## Files

- `REPRODUCE_v120.md` (2 KB) — Reproduce the v1.20 signed energy result
- `adversarial_weighted_review.md` (15 KB) — Adversarial audit of the frequency-weighted signed target
- `assembly_general.py` (3 KB) — Arb enclosures of the actual Weil Fourier coefficients at integer lambda.
- `build_complete_pdf.py` (1 KB) — Compile in a fresh directory; install only a closed, parseable full PDF.
- `certify_weighted_counterexample.py` (2 KB) — Exact finite rational witness against a two-sided energy norm contraction.
- `certify_weighted_tail.py` (5 KB) — One-sided verified-solve certificate on a literal Fourier tail. No RH input.
- `checkpoint_entry.md` (10 KB) — Current research checkpoint: September 21, 2026 — v1.20 signed energy control on the complete lambda=4 Fourier tail
- `finish_checkpoint.py` (11 KB) — (no description in file)
- `integrate_v120.py` (5 KB) — (no description in file)
- `sequences_v2_l4_J256_b256.json` (73 KB) — (no description in file)
- `sequences_v2_l4_J4096_b256.json` (1.1 MB) — (no description in file)
- `sequences_v2_l4_J4096_b320.json` (1.4 MB) — (no description in file)
- `weighted_norm_counterexample.json` (5 KB) — claim: An exact finite rational vector has W energy >2 times its exact archimedean diagonal energy. Thus the signed weighted remainder has norm >1; no negative Weil di
- `weighted_pilot.json` (4 KB) — (no description in file)
- `weighted_pilot.py` (2 KB) — Exploratory signed energy-normalized Fourier-tail matrices. Not a certificate.
- `weighted_signed_insert.tex` (11 KB) — Retaining the archimedean energy in a one-sided estimate
- `weighted_tail_l4_s16_even_b256.json` (946 B) — claim: W restricted to |n|>start in selected parity >= c times the exact positive archimedean diagonal; fixed window only.
- `weighted_tail_l4_s16_even_b320.json` (1017 B) — claim: W restricted to |n|>start in selected parity >= c times the exact positive archimedean diagonal; fixed window only.
- `weighted_tail_l4_s16_odd_b320.json` (1016 B) — claim: W restricted to |n|>start in selected parity >= c times the exact positive archimedean diagonal; fixed window only.
- `weighted_witness_l4_s16_even_b256.json.gz` (10.5 MB) — (no description in file)
- `weighted_witness_l4_s16_odd_b256.json.gz` (39.2 MB) — (no description in file)
