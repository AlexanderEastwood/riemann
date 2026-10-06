# Diagnostic only — not a certificate

The preregistered bounded original quotient-pole locator found no stable
approximate root satisfying its threshold. General quotient PD remains
undecided; the original signed theta target remains open. No zero-free
region, negative Laguerre value, RH/G2 implication or manuscript version.

See [outcome and scope](../../audits/theta-pole-locator-2026-10-05-v1/README.md)
and [frozen protocol](../../audits/theta-pole-locator-2026-10-05-v1/PROPOSAL.md).

## Reproduce

Python3.14.6, mpmath1.3.0; pinned `requirements-replay.txt`. Existing `.venv`
was used; no dependency installation. From repository root:

```text
.venv/bin/python evidence/diag_theta_pole_locator/locator.py --output evidence/diag_theta_pole_locator/controls.json
.venv/bin/python evidence/diag_theta_pole_locator/locator.py --original --original-approved --budget-seconds 4200 --output evidence/diag_theta_pole_locator/original.json
pyright evidence/diag_theta_pole_locator/theta_eval.py evidence/diag_theta_pole_locator/locator.py
```

These commands describe the archived execution; do not overwrite the
historical outputs for a replay. Use new output filenames. The original
run was admitted only after matched controls, protocol review and draftPR80.
The full90-minute cap included preparation/controls; 4200seconds was the
conservative remaining cap supplied to the original runner. Actual original
runtime48.46seconds,171calls:81grid,10replayed corners,80refinement evaluations.
No domain extension or later root scan.

## Error status

Analytic lattice and real-tail majorants are supplied for M,C,M'. Their
numeric evaluations use ordinary mpmath, not interval rounding. Composite
Gauss-Legendre integration and roundoff errors are not rigorously enclosed.
128/256bits,24/32theta terms,48/96nodes per segment,R=4/4.5 are diagnostic
replays. Four-corner sampled phase is not an argument-principle certificate.
Positive/negative synthetic outcomes are algorithm checks only.

Original output retains every evaluated point, derivative, normalization,
majorant, selection score, stop and replay comparison. The smallest final
relative residual0.03914 is far above2^-40; it is not a regional lower bound.

## Independent endpoint replay

A separately implemented direct-term theta sum (36 terms), 256-bit adaptive
tanh-sinh quadrature to R=5, and a breakpoint at Re(z) replayed exactly the
four saved final endpoints. No extra corner, root search or scan. Runtime
65.94 seconds. The replay also independently differentiates phi and includes
the normalization derivative.

```text
.venv/bin/python evidence/diag_theta_pole_locator/independent_replay.py --approved --input evidence/diag_theta_pole_locator/original.json --output evidence/diag_theta_pole_locator/independent.json --bits 256 --max-endpoints 4
```

Largest relative differences from the 256-bit Gauss-Legendre endpoints:
M:8.374e-29; C:1.404e-26; normalized M':1.048e-26 (rounded upward for display,
not interval bounds). This supports stability of these four samples and
does not establish their full working-precision accuracy. Both methods have
unbounded finite quadrature/roundoff error. Tanh-sinh's returned integration
error is a heuristic, not a certificate. The input archive hash is retained.
