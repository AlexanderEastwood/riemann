# Agent 05: code, provenance and archived-result review

**No major finding. The recorded outcome is an inconclusive diagnostic,
with no admitted negative witness.** This review performed no new original
theta evaluation and no certificate. It supports the stated stop rule.

Reviewed baseline `0da30a5c92203e45c452df87b68a93d86b7e5fd7` (PR80),
AGENTS.md, this audit's BRIEF/PROPOSAL/README, reviews 01--04, the three new
scripts, their complete JSON records, and the inherited evaluator's
normalization/integration implementation. The coordinator's current full
register and dependency review is inherited; this is not a replay of all
historical proofs or certificates. Both original-evidence recovery groups
remain OPEN.

**Wall check: Distinct test.** Closest PR78--80. The direct real finite
matrix condition does not require complex poles. No all-height estimate
or new arithmetic lower bound follows; the original signed target remains
the same open gap.

## Fixed scope and numerical logic

`original_screen.py` requests exactly six arguments `j/4`, `j=0,...,5`, at
128 and 256 bits. The archived record contains exactly those twelve
evaluations. The initial/replay lattice cutoffs, quadrature orders and real
cutoffs agree with registration: 24/32, 48/96 and 4/4.5. Each six-value list
is used to form `B[i,j]=k(abs(i-j)/4)`, preserving the declared stencil and
the original even quotient. No coefficient, spacing or size scan occurs.

Both moments use the same analytic nonzero normalization
`B(t)=exp(2*pi*exp(2*t)-9*t)/(4*pi^4)`, so the ratio is unchanged. Direct
arithmetic on the archived normalized moments reproduced each stored
quotient to its working precision. The realness checks occur before the
real part is consumed, and nonfinite or nonpositive denominator samples
stop the run. These checks are numerical sanity checks only.

The 128-bit eigensolver selects the one vector. Its maximum-magnitude
normalization and sign orientation precede nearest-dyadic rounding, with
ties to even. A rounded tie can therefore put a negative maximum before
the positive maximum, as it does here; that is consistent with the stated
selection order and cannot affect the quadratic form. The nonzero frozen
vector is

```text
(-1209425521, 3095606301, -4294967296,
  4294967296, -3095606301, 1209425521) / 4294967296.
```

The same exact integer numerators are reused at 256 bits and by the
independent replay. No later eigenvector replaces them. The strict negative
margin and the two non-strict agreement gates match the preregistered
code/proposal. Both form and threshold scale quadratically with the vector;
no freely adjustable normalization creates an apparent gain. The correction
in review03 from `<` to `<=` for agreement does not change the computation.

## Reproducibility checks using existing values only

I recomputed the matrix analysis from `original.json`, without importing or
calling a theta evaluator. The entire resulting object agrees exactly with
`original-screen.json`, including all matrices, eigenvalues, the selected
rational vector, quadratic forms and gate booleans. I independently reran
the two synthetic controls through the actual pipeline; their entire
result object agrees exactly with `controls.json`.

All six recorded provenance checks match the current files:

- Original record: controls archive, inherited evaluator, and original
  wrapper SHA256 digests.
- Independent record: original archive, original matrix archive, and
  independent replay source SHA256 digests.

The original record is complete. Its archived start/finish are
`2026-10-06T15:12:36.138990Z` and `2026-10-06T15:12:39.229178Z`, inside the
fixed discovery interval ending `15:59:00Z`. The independent record is also
complete and uses exactly the same six original arguments. Its implementation
imports neither primary numerical script; it uses direct summands, raw
moments, a different integration rule and a larger fixed cutoff.

The archived-data recomputation confirms `agreement_pass=true` and
`negative_diagnostic_candidate=false`. At 256 bits the computed minimum
eigenvalue is about `+0.00052817273088790117508` and the frozen rational form
about `+0.00168886096494128373566`. The largest recorded relative independent
quotient discrepancy is about `3.84269e-69`. These statements report floating
observations, not rigorous intervals or error bounds.

Static diagnostics for all three new scripts, run from the configured
worktree root, report **0 errors, 0 warnings**. No code was modified by
this reviewer; ownership is limited to this review file.

## Error status and decision

The original and independent records retain analytic lattice and two-sided
real-integration tail formulas, but their ordinary arithmetic values are not
outward-rounded. Neither fixed Gauss-Legendre nor adaptive tanh-sinh supplies
the complete rigorous finite-integration error needed here. Floating
roundoff and the quotient error are likewise not enclosed. Agreement between
the implementations supports reproduction of the diagnostic only; a shared
bias cannot be bounded by the observed discrepancy alone.

The current reports respect those limits. No midpoint eigensolve is used as
a certificate, no global PD conclusion is drawn, and no conditional Arb
stage was invoked without a negative candidate. The matched controls check
the finite-matrix pipeline, not the original theta arithmetic or its error
budget. The stated NS/DH mismatches are not represented as passed controls.

**Disposition: stop this screen and shelve further quotient falsification
screens pending independent analytic input.** No enlarged stencil, positive
finite-matrix certificate, research row, thaw or manuscript version is
warranted by this result. General quotient PD and the original first-Laguerre
inequality remain undecided. Final wall check: Distinct test, inconclusive.
