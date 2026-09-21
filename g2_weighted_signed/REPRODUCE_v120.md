# Reproduce the v1.20 signed energy result

This directory contains the actual lambda=4 complete-tail certificate, analytic proofs and failed-method diagnostics. It is not a G2 or RH certificate.

Requirements: Python3, python-flint (Arb), NumPy, SciPy, threadpoolctl. PDF rebuild additionally uses latexmk/pdfLaTeX and PyMuPDF. The proof scripts never query zeros.

Run from this directory:

```bash
OPENBLAS_NUM_THREADS=2 python3 certify_weighted_tail.py --bits 320 --witness-path weighted_witness_l4_s16_even_b256.json.gz
OPENBLAS_NUM_THREADS=2 python3 certify_weighted_tail.py --parity odd --N 1536 --M 2048 --J 4096 --r 64 --bits 320 --witness-path weighted_witness_l4_s16_odd_b256.json.gz
OPENBLAS_NUM_THREADS=2 python3 certify_weighted_counterexample.py
```

The first two commands must report PASS, all_Gershgorin_rows_positive=true, positive remote_gamma and positive arch_diagonal_floor. They reconstruct the full signed lower matrix, every finite residual row and an analytic bound for every remaining row. The proof of the remote bound is in the manuscript and adversarial review, not inferred from floating truncation.

Only the b256-named dyadic witnesses need be distributed. Both precisions use those exact same entries; the verified320 reports preserve their uncompressed hashes. A witness's creation precision is not a proof hypothesis. The final assembly cache has an explicitv2 name; older exploratory caches are intentionally excluded.

The matrix generation retains all active prime powers, two pole signs and the correct separate pole and archimedean diagonals. Forty exponential-series terms suffice at this window; the omitted terms receive explicit Arb radii. The positive prime-weight endpoint maximum is checked with exact endpoint comparisons. Congruence entries are exact dyadic numbers, and every interval Gershgorin row is tested.

`weighted_pilot.py` and `weighted_pilot.json` are exploratory only. Their tiny negative lower eigenvalues at larger windows are not certified signs. `weighted_norm_counterexample.json` instead contains an exact rational vector and interval verification of a positive energy ratio exceeding2, disproving the two-sided weighted norm contraction at lambda4,N16.

The main inequality is `QW4(f,f)>=10^-8 sum(-A_n)|f_n|^2` on the full complex literal Fourier tail|n|>16. It does not include the low head. Full lambda4 positivity still needs the effective Schur sign on17 even+16 odd coordinates. Uniform growing-window G2 remains open.
