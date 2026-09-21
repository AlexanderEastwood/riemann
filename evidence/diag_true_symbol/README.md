Diagnostic (2026-09-21, Claude); not a certificate. See results.md.
Correct version of the retracted "line symbol" experiment: the manuscript's β_a
validated against the assembled matrix to 2e-7 (§1), its negative set (§2),
the ground-state level split at λ=3 and λ=4 (§3–4), the ground's lattice-cell
distribution across λ (§5, selfsim.py), the lobe of β_a nearest the first zeta
ordinate against the ground's mass there (§6, nearzero.py), and the level
pencil W v = ν (W + W⁻) v showing the cancellation is a whole deep block, not
one direction (§7, pencil.py; wminus_tail.py bounds the neglected tail).
Run from the repo root with .venv/bin/python; beta_true.py runs the validation
when executed directly (~5 min); pencil.py takes cases as "lam,N,bits"
arguments. cert.py holds the Arb-to-mpmath midpoint conversion the scripts share.
