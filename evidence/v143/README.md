# v1.43 — NS-19: complete first-zero enclosure and archived resolution

**Certified computation + proved implications. G2 and RH remain open.**
The first positive zero of the complete lambda=4 ground transform is simple
and lies in `(gamma_1 - 8.752082e-33, gamma_1 + 8.752082e-33)`.
The two precisions, 1024 and 1280 bits, give a displacement budget
`8.75208157392882826...e-33`, hence the simpler outward radius `9e-33`.
This is the best enclosure extracted here from the archived comparison;
no optimality claim over every possible use of the archive is made.

The limiting quantity is `C_ell * rho`: the evaluator dual constant
`C_ell = 79920.06156776...` times the upper ground-energy budget
`rho = 2.45361754930714...e-75`. It is not the old ordinary projection
error `sqrt(rho/b) = 1.5664...e-4`. The new bound is `sqrt(C_ell*rho)/d`,
with `d=0.0016`. All complete tail cross terms are retained.

A hypothetical lower bound `0 <= l <= mu0` would instead control the
trial-to-ground error energy by `b*(rho-l)/(b-l)`, where `b=1e-67`.
For its value-to-zero uncertainty to reach `1e-71`, the scalar budget
requires `rho-l <= 3.20320065696758...e-153` (relative gap about `1.3055e-78`).
The outward condition `rho-l <= 3.2031e-153` suffices for that transfer term.
The archive does not contain such a lower bound. It would not alone
produce a gamma-centered enclosure at this scale: the frozen trial has
`fhat(gamma_1)` in `(1.0641,1.0642)e-40`. The former ordinary-norm transfer
would require a much smaller Rayleigh gap, about `9.233248e-216`.

The complete discrepancy has **no certified sign or nonzero magnitude
lower bound**. The separately certified N=120 finite benchmark is about
`+2.92504e-71`; it is not a complete-ground value. Its scale lies below
the resolution of the displayed archived comparisons. This is a failure
of those bounds, not a failure of the object or a universal impossibility
theorem for the data. The revised task closes NS-19's accounting and ends
the pursuit of the former sign/factor-ten target.

## Files

- `sharpening_section.tex`: complete proof and explicit hypotheses.
- `archive.py`: loads the unchanged v1.42 coarse verifier by reference.
- `certify_discrepancy_budget.py`, `discrepancy_budget_b1024.json`,
  `discrepancy_budget_b1280.json`: evaluator dual bound and all 304 earlier-zero exclusions.
- `certify_resolution.py`, `resolution_b1024.json`, `resolution_b1280.json`:
  precise energy-gap thresholds, full two-sided endpoints and trial-center caveat.
- `check_discrepancy_budget.py`, `discrepancy_cross_checks.json`: second
  implementation of the dual solve, rational dyadic coverage, resolution
  algebra, saved signs and cross-precision agreement; no external audit.
- `certify_finite_lambda4.py`, `finite_lambda4_N120_b1024.json`,
  `finite_lambda4_N120_b1280.json`: the finite benchmark prepared during
  the original Task B, retained separately and replayed after relocation.
- `scope_review.md`: claim and proof review.
- `build_report.json`, `integration_checks.json`: actual build and preservation checks.
- `research-report-2026-09-21-v1.html`: user-facing report.

The planning midpoint diagnostic is labelled under `../diag_ns18_sharpening/`.
It supplies no proof bound. Tagged v1.42 artifacts are unchanged.

## Replay

Python 3.14.6, python-flint 0.9.0, mpmath 1.4.1. Run from the repository
root. Every command requires a fresh output path; saved outputs are not overwritten.

```sh
.venv/bin/python -B evidence/v143/certify_discrepancy_budget.py --bits 1024 --output /tmp/ns19-budget-1024.json
.venv/bin/python -B evidence/v143/certify_discrepancy_budget.py --bits 1280 --output /tmp/ns19-budget-1280.json
.venv/bin/python -B evidence/v143/certify_resolution.py --bits 1024 --output /tmp/ns19-resolution-1024.json
.venv/bin/python -B evidence/v143/certify_resolution.py --bits 1280 --output /tmp/ns19-resolution-1280.json
.venv/bin/python -B evidence/v143/certify_finite_lambda4.py --bits 1024 --output /tmp/ns19-finite-1024.json
.venv/bin/python -B evidence/v143/certify_finite_lambda4.py --bits 1280 --output /tmp/ns19-finite-1280.json
.venv/bin/python -B evidence/v143/check_discrepancy_budget.py --output /tmp/ns19-second-check.json
python3 tools/verify_manifest.py v143
./manuscript/build.sh
```

The resolution script and second checker read the saved reports and bind
them by hashes; the first two commands independently recompute the complete
small gates. Full historical residual assemblies at 768/896 bits are inherited,
not freshly recomputed. Their analytic bounds cover the infinite tail.
No window, tail metric, cutoff or trial support is changed. NS-1's two
missing historical evidence groups remain OPEN and are not dependencies.
