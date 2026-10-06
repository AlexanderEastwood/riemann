# Agent 06: final adversarial admission and stop decision

**No major finding. Publish this as an inconclusive diagnostic and stop
the screening round.** There is no admitted negative original witness,
no reason under the registered protocol to start an Arb stage, and no
positive-definiteness certificate. Further quotient falsification screens
are shelved pending independent analytic input.

Reviewed baseline `0da30a5c92203e45c452df87b68a93d86b7e5fd7` (PR80),
AGENTS, this task's BRIEF/PROPOSAL/README and review record, reviews 03--05,
the complete archived matrix and independent-replay records, results.md,
and the report HTML source. The coordinator's full 104-node and
14-demand conclusion/dependency review is inherited. I did not rerun
original theta values, historical certificates or the browser rendering.
Both historical original-evidence recovery groups remain OPEN.

**Wall check: Distinct test, inconclusive.** Closest: PR78--80 and
NS100/101. What changes is a direct real-axis finite quadratic-form test
of the original quotient `k=C/M`, with no complex-pole hypothesis. This is
a route-validation question. The original all-height signed theta
estimate is still the same open gap; no new estimating method is supplied.

## What the evidence says

The recorded protocol fixes `t_j=j/4`, `j=0,...,5`, and the matrix
`B_ij=k((i-j)/4)`. The primary archive has those six quotient arguments
at 128 and 256 bits, and the independent replay has the same six arguments.
Both precision runs reuse the exact same nonzero dyadic vector:

```text
v = (-1209425521, 3095606301, -4294967296,
      4294967296, -3095606301, 1209425521) / 4294967296.
```

The JSON reports `agreement_pass=true` and
`negative_diagnostic_candidate=false`. Its six computed eigenvalues are
positive at both precisions. The minimum is approximately `0.000528173`,
and the fixed rational form approximately `0.001688861`. The separately
implemented raw-theta/tanh-sinh replay reproduces the same form; its
largest observed relative quotient discrepancy is below `3.85e-69`.
These values are observations from ordinary high-precision arithmetic.

The independent replay is materially useful: it changes integration rule,
normalization, cutoff and implementation while preserving the exact
question and the rational vector. It reduces concern about a particular
implementation mistake. Its agreement is not a bound on common analytic
or numerical error. In particular, the lattice and two-sided integration
tail formulas are evaluated without outward rounding, and the finite
quadrature, roundoff and ratio errors are not enclosed. Neither a sampled
positive eigenvalue nor this agreement is a rigorous finite-matrix lower
bound.

## Control and implication scope

The Gaussian and entire pole-free non-PD controls share the same stencil,
matrix construction, rational-vector rule and replay gates. Their archived
outcomes check the finite-matrix/witness pipeline: it detects the negative
toy and does not manufacture a negative Gaussian candidate. They do not
validate the original theta integration or imply a positive sign for its
quotient. The NS/DH mismatches are explicitly recorded in the proposal and
review03; none is called a passed arithmetic control.

For a rigorously evaluated original matrix, a negative rational form
would directly refute positive definiteness of `k`. There is no further
asymptotic transfer needed for that rejection. This direct condition is
not already decided by PR78's failed positive sech-power mixture or
PR80's inconclusive bounded pole locator.

The sufficient implication remains one-way:

```text
k positive definite => C=M*k positive definite => L1[X](r)>=0 for all r.
```

M is an autocorrelation, so the middle inference uses the Schur product
property for its translation matrices. Its converse is not available.
Even certified failure of k-PD would only reject that sufficient
construction. Here no such failure was found. Conversely, even a
certified positive matrix on these six points would not imply k-PD on
arbitrary finite real sets. The current diagnostic establishes neither
global assertion and says nothing new about RH or G2.

## Final admission and recommendation

The controls and draft PR81 protocol at `1b9efc9` preceded the original
evaluation; review05 verifies the archived timestamps fall within the
one-hour discovery budget. The fixed stencil and rational vector were
preserved. No negative candidate satisfies the registered margin, so the
conditional two-hour certificate task is not admitted. Do not certify a
positive finite result instead: that would answer a different question
without changing the missing all-height input.

Publish the actual records, this explicit null outcome and the stop
decision. Make no research row, thaw, theorem node or manuscript version.
Do not enlarge the stencil, vary spacing, add derivative-moment tests or
restart the pole search as a follow-on from this null. The two bounded
quotient screens are separate inconclusive observations, not accumulated
evidence for global quotient positivity.

Reopening this family requires an independently specified analytic input
with a complete dependency edge and matched hypotheses. No such input
was obtained in this screen; I do not recommend or invent another
adjacent numerical mechanism. The original nonlinear theta route is
still open, and general quotient PD is unresolved rather than excluded.

The report HTML source correctly labels the numbers diagnostic, denies
a global PD inference and states the stop. As a minor wording preference,
its lead should say that no negative witness was found rather than that
the quotient "passed"; this avoids suggesting affirmative validation of
the function. This is not a mathematical or publication-blocking finding.

**Final wall check: Distinct test, inconclusive. Original signed target:
same open gap.**
