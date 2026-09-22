Diagnostic (2026-09-21, Claude); not a certificate. See results.md.
NS-28: measures the two inputs of prop:v146-level-complexity on the even head
(N=256): the achievable level-distribution constant c and the minimum energy
Q_min(c) a state must pay for it (SDP dual = pure-state primal). c ~ 0.2-0.3 is
available at every window; Q_min(c) grows three orders of magnitude from
lambda=4 to 6, so the conditional bound has content only for K <= 2 (lambda 6)
or K <= 7-16 (lambda 8) levels, below what the NS-22 minorants use.
Run from the repo root with .venv/bin/python; min_energy_lp.py needs scipy.
