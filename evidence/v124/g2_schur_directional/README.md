# `evidence/v124/g2_schur_directional/`

Manuscript v1.16 — CERTIFICATE bundle: the directional infinite-complement certificate at lambda=3 (complete fixed-window positivity), even and odd, at 768 and 896 bits, with frozen witnesses (`schur_witness_*.json.gz`, up to 29 MB), Arb Weil-sequence enclosures, finite-output pilots (no remote-tail bound, per `pilot_schur.py`) and the weighted prime-tail certificate.

The files here are byte-identical to [`evidence/v126/g2_schur_directional/`](../../v126/g2_schur_directional/).

**Start here:** [`G2_v116_Research_and_Reproduction.md`](G2_v116_Research_and_Reproduction.md), [`fixed_window_certificate_report.md`](fixed_window_certificate_report.md), [`adversarial_schur_report.md`](adversarial_schur_report.md)

## Files

- `G2_v116_Research_and_Reproduction.md` (5 KB) — Reproducing complete fixed-window positivity — manuscript v1.16
- `adversarial_schur_report.md` (11 KB) — Adversarial Schur assessment and a stronger certified tail
- `assembly.py` (3 KB) — Exact lambda=3 Weil sequences; Arb enclosures and reusable parity blocks. Fixed first-slot-linear convention; unshifted normalized Fourier basis.
- `assembly_independent_overlap.json` (211 B) — (no description in file)
- `certify_infinite_schur.py` (7 KB) — Directional infinite-complement certificate at lambda=3. All arithmetic enclosures use Arb.
- `certify_weighted_prime_tail.py` (3 KB) — Arb certificate of a positive-weight Schur bound for lambda=3 prime shifts. Only scalar exact rational coefficient comparisons and analytic tail constants are certified.
- `checkpoint_entry.md` (10 KB) — Current research checkpoint: September 21, 2026 — v1.16 complete fixed-window positivity
- `directional_schur_insert.tex` (6 KB) — A directional certificate for the entire Fourier complement
- `directional_tail_derivation.md` (12 KB) — A moment-preserving PSD enclosure of the infinite remote Weil residual
- `directional_tail_gram.py` (3 KB) — Certified real-matrix remote Gram majorants for the actual Weil commutator. Conditional inputs: exact matrices are enclosed by G and b; B bounds |b_n| for all n; optional…
- `finish_checkpoint.py` (10 KB) — (no description in file)
- `fixed_window_certificate_report.md` (8 KB) — Complete fixed-window Weil positivity certificate at lambda=3
- `fixed_window_insert.tex` (5 KB) — A certificate for the complete fixed-window form
- `infinite_schur_N256_M512_J1024_r128_even_b768.json` (1 KB) — (no description in file)
- `infinite_schur_N256_M512_J4096_r80_even_b768.json` (1 KB) — (no description in file)
- `infinite_schur_N256_M512_J4096_r80_even_b768_diagonal.json` (24 KB) — (no description in file)
- `infinite_schur_N256_M512_J4096_r80_even_b896_diagonal.json` (24 KB) — (no description in file)
- `infinite_schur_N256_M512_J4096_r80_odd_b768_diagonal.json` (1 KB) — (no description in file)
- `infinite_schur_N512_M1024_J2048_r128_odd_b768.json` (1 KB) — (no description in file)
- `infinite_schur_N512_M1024_J4096_r100_odd_b768_diagonal.json` (46 KB) — (no description in file)
- `infinite_schur_N512_M1024_J4096_r100_odd_b896_diagonal.json` (46 KB) — (no description in file)
- `integrate_v116.py` (7 KB) — (no description in file)
- `pilot_N256_M512_J1024_even.json` (943 B) — (no description in file)
- `pilot_N256_M512_J1024_odd.json` (935 B) — (no description in file)
- `pilot_N512_M1024_J2048_odd.json` (940 B) — (no description in file)
- `pilot_gamma_sensitivity_odd.json` (953 B) — (no description in file)
- `pilot_improved_gamma_odd.json` (743 B) — (no description in file)
- `pilot_schur.py` (4 KB) — Finite-output pilot for the residual Schur certificate. No remote-tail bound. An adverse sign here invalidates this particular Gamma-only budget, not W.
- `schur_pilot_report.md` (7 KB) — Directional Schur pilots at the exact window lambda = 3
- `schur_witness_N256_M512_even_b768.json.gz` (7.0 MB) — (no description in file)
- `schur_witness_N512_M1024_odd_b768.json.gz` (27.9 MB) — (no description in file)
- `weighted_prime_inverse_insert.tex` (7 KB) — A positive weight for the prime shifts and a diagonal inverse bound
- `weighted_prime_tail_certificate.json` (7 KB) — (no description in file)
- `weil_sequences_n1024_b768_k128.json` (498 KB) — (no description in file)
- `weil_sequences_n2048_b768_k128.json` (995 KB) — (no description in file)
- `weil_sequences_n4096_b768_k128.json` (1.9 MB) — (no description in file)
- `weil_sequences_n4096_b896_k128.json` (2.1 MB) — (no description in file)
