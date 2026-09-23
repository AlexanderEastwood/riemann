# v1.58 — NS-59 Nyman–Beurling difference budgets

Classification: exact identities, proved implications, certified finite
computations, and an open asymptotic lower-correlation input.

The adjacent family `delta_n = rho_n - (n-1)rho_(n-1)/n` has a complete raw
Gram norm `O_epsilon(N^(-5/3+epsilon))` on `N<n<=2N`, using the classical
Weyl zeta bound. This is an unconditional analytic denominator estimate,
with an unspecified constant. It does not prove NB convergence.

For the raw Gram uniformly over all coefficients, a bound
`O_epsilon(N^(-2+epsilon))` for every epsilon is equivalent to Lindelof.
Every bound `O((log N)^B/N^2)` with fixed B is false, even on dyadic blocks.
This obstruction is not asserted for the projected Gram or the particular
residual direction. No priority claim is made.

- [Analytic proof](proof.tex), included verbatim in the live manuscript
- [Research report](nb-difference-budget-2026-09-22-v1.html)
- [Local self-review](integration-review-2026-09-22-v1.html), not independent
- [Arb block verifier](nb_certify.py), with 256- and 384-bit saved reports
- [Cross-precision/table verifier](verify_replays.py)
- [Independent physical-cell formula check](check_cell_integrals.py), with
  complete positive tail bounds at both precisions
- [Exact Maxima algebra](exact-checks.mac)
- [Validation and provenance](validation.json)

All old/new cross terms are retained. The Arb finite computations test
the same matrices through index 512 at both precisions. At N=128 and
N=256 the old raw-trace gain is less than 1/400 of the true gain. After
the numerator is transformed too, the adjacent trace bound is worse
than the raw one at N=256. These are finite facts, not asymptotic claims.

The separate floating diagnostic is in
`evidence/diag_ns59_nb_budget/`, not in this certificate directory.

Replay from the repository root:

```sh
.venv/bin/python evidence/v158/nb_certify.py --bits 256 --max-index 512 --output /tmp/nb-blocks-256bits.json
.venv/bin/python evidence/v158/nb_certify.py --bits 384 --max-index 512 --output /tmp/nb-blocks-384bits.json
.venv/bin/python evidence/v158/verify_replays.py
.venv/bin/python evidence/v158/check_cell_integrals.py --bits 256 --output /tmp/cell-integrals-256bits.json
.venv/bin/python evidence/v158/check_cell_integrals.py --bits 384 --output /tmp/cell-integrals-384bits.json
maxima --no-init --quit-on-error --very-quiet --batch=evidence/v158/exact-checks.mac
./manuscript/build.sh
python3 tools/verify_manifest.py v158
```

`verify_replays.py` checks the archived reports. The block generator uses
Arb for every entry and solve and does not discard interval errors.
The separate cell check bounds the entire omitted integral by `1/65536`;
its purpose is formula/convention verification, not a matrix tail estimate.
The Maxima checks cover finite algebra only. Analytic statements are proved
in the LaTeX fragment. RH, G2 and the uniform Weil floor remain open.
