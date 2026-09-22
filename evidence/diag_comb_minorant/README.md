Diagnostic (2026-09-21, Claude, board row NS-22); not a certificate. See results.md.
Step minorants for the weighted concentration criterion of prop:v131-concentration
(eq:v131-step-minorant / eq:v131-weighted-concentration) on the even head (N=256,
float quadrature on xi in [0,800]) at lambda = 3, 4, 6, 8: the loss eta_a(J) for
(A) the J deepest troughs, (B) one level set, (C) the layer-cake reference,
(D1) J-level quantization of beta_a (level sets = unions of crest cores),
(D2) a lattice-periodic comb, (D3) binary-coded quantization (J sets, 2^J levels).
Run from the repo root:  /Users/alex/riemann/.venv/bin/python evidence/diag_comb_minorant/comb_minorant.py
(~2-3 min per lambda; output in comb_minorant_output.txt, tables in comb_minorant_l3_4_6_8.json).
Imports beta_grid / Fe_grid from evidence/diag_true_symbol/pencil.py.
