# NS101 bounded theta-factorization attempt

**Classification: exact identities and a scoped control; no new arithmetic
positivity estimate. The feasibility attempt reached its stop.**

The actual Jacobi completion gives the usual autocorrelation of the tilted
theta kernel. The kernel required by the growth criterion is its parameter
derivative, a difference of two positive definite kernels. The comparison
between those terms remains unproved.

A concrete reciprocal-theta control preserves positive Gaussian mixtures,
the reciprocal identity, a positive even differential kernel, order one,
and the critical-strip zero bound, while adding explicit off-axis zeros.
It changes the original single-lattice coefficients and does not assert
monotonicity, log-concavity or all modular transformations. It therefore
does not exclude a proof using those additional original properties.

Direct absolute unfolding only works beyond the classical convergence
boundary. At the boundary each Gaussian summand integrates to zero but
the complete kernel integrates to 1/4. This forbids that interchange,
not correlated resummation or the desired sign for the original function.

- `argument.tex`: self-contained completion, factorization attempt, control
  and complete integration-domain calculation.
- `checks.mac`, `checks-output.txt`: 20 exact algebra checks. These check
  identities, not the unproved sign or all analytic steps.
- `turn-review.json`: all 104 conclusion records reviewed, provenance,
  scope and Wall checks.
- `sources.json`: primary sources and an expanded, nonexhaustive literature
  screen; reported external blockwise claims are not imported as proofs.
- `self-review.json`, `validation.json`, `inventory.json`: audit and checks.

Run `maxima --very-quiet -b evidence/ns101_theta_factorization/checks.mac`.
There are no approximate numerical proof gates, cutoff experiments or new
Python files in this task. No manuscript version or theorem node is added.
Both missing-original evidence groups remain OPEN. RH and G2 remain open.

[Readable report](../../audits/theta-factorization-test-2026-09-23-v1.html).
