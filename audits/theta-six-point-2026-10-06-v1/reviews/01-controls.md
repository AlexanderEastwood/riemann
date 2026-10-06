# Agent 1: frozen matrix protocol and synthetic controls

Diagnostic review, not a certificate. Baseline PR80, main
`0da30a5c92203e45c452df87b68a93d86b7e5fd7`; inherited coordinator's full
conclusions/dependency review. Read AGENTS.md and this audit's BRIEF.md.

## Protocol fixed before original evaluation

Only six arguments, `j/4`, `j=0,...,5`, are consumed. At each of exactly
128 and 256 bits, build the real symmetric Toeplitz matrix
`B[i,j]=k(abs(i-j)/4)`. No spacing, point count, or stencil selection occurs.

At 128 bits, take the minimum-eigenvalue eigenvector from mpmath `eigsy`.
Normalize its largest absolute component to one and choose its sign so the
first component attaining that maximum in the computed vector is positive.
Round each normalized component to the nearest multiple of `2^-32`, with
ties to even. Archive all six integer numerators and the denominator
`4294967296`. Reuse this one vector at both precisions; the 256-bit
eigendecomposition is reported but does not replace or improve it.

For both runs require the strict diagnostic margin
`q = v^T B v < -2^-40*k(0)*||v||^2`. Also require:

```
max_j abs(k128_j-k256_j) <= 2^-40*max(abs(k128_0),abs(k256_0))
abs(q128/(k128_0*||v||^2)-q256/(k256_0*||v||^2)) <= 2^-40
```

There is no artificial denominator floor of one. This protocol requires
positive `k(0)` and rejects nonfinite values; the original wrapper separately
checks the realness of values and positivity of its denominator samples.
An admitted negative diagnostic witness would still require full Arb
validation, including original integration and lattice tails. An eigensolve
cannot provide that validation. No witness means inconclusive and stop.

## Matched controls executed first

Both controls use exactly this pipeline and stencil at both precisions.
The positive control is `g(t)=exp(-t^2)`. The negative control is
`f(t)=exp(-t^2)*(1+t^2)`. Their arithmetic is evaluated in mpmath 1.3.0;
the results are diagnostics. Analytically, the Gaussian has positive Fourier
transform, whereas the second transform is
`sqrt(pi)*exp(-xi^2/4)*(3/2-xi^2/4)` and changes sign despite having no poles.
This matches the direct finite-matrix failure mode; no pole is required.

Observed Gaussian minimum eigenvalue is about `1.29537871667e-5`, and its
fixed rational quadratic form is about `3.45301662888e-5`, positive at both
precisions. The pole-free negative control has minimum eigenvalue about
`-0.110627960378` and fixed rational quadratic form about `-0.415567834556`,
negative beyond the required margin at both precisions. Its witness is

```
(4294967296,237361438,-4017960188,-4017960188,237361438,4294967296)/4294967296.
```

Both runs satisfy the prescribed precision-agreement tests. All entries,
eigenvalues, rational vectors, quadratic forms and discrepancies are archived
in `evidence/diag_theta_six_point/controls.json`. The top-level gating fields
`controls_pass`, `gaussian_positive_pass`, and `pole_free_non_pd_pass` are true.
The controls validate the matrix pipeline at this stencil, not the original
theta evaluator, complete quadrature errors, or a global PD assertion.

## Validation and handoff

`matrix_screen.py` has type hints on every function; pyright reported zero
errors, zero warnings. The API `analyze_pair(name, evaluations)` accepts
exactly the two prescribed precision records and six decimal real strings
per record. The CLI `--input` consumes existing archived values only.
No original theta computation was performed by this agent. The parent must
complete preregistration and explicitly authorize the original wrapper.
