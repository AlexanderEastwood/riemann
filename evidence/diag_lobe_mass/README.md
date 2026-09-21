Diagnostic (2026-09-21, Claude, NS-21); not a certificate. See results.md.
Tests the candidate inequality mass_k(lobe) <= C nu_k (and the sqrt and any-lobe
variants) for the six deepest level-pencil directions of the even head at
lambda = 3, 4, 6, 8: Fourier mass and negative-level energy of each pencil vector in
every negative lobe of beta_a below xi = 60, with the lobe nearest gamma_1 singled
out. Result: every variant is killed by the ground itself (mass/nu up to 1e98); the
lobe mass is nu-blind. Replacement observations are filed as a PROPOSAL only.
Run from the repo root with .venv/bin/python; lobe_mass.py takes cases as
"lam,N,bits,dps" arguments and --pool re-prints the tables from the JSON files.
Depends on evidence/diag_true_symbol/{pencil.py,cert.py} and
evidence/v124/g2_schur_cancellation/assembly_general.py.
