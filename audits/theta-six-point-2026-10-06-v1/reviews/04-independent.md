# Independent six-point replay

Diagnostic, not an interval certificate. Agent 4 of 6.

Reviewed baseline: `0da30a5c92203e45c452df87b68a93d86b7e5fd7`
(PR80), the current task BRIEF/PROPOSAL, archived primary six values and the
frozen rational vector. The parent performed this turn's full conclusion
register/dependency review; this report does not claim historical proof replay.

**Wall check: Distinct test.** Closest PR78–80. The fixed real matrix can
exclude quotient positive definiteness without complex poles. It does not
establish the original all-height signed estimate, and a finite positive
matrix cannot prove global quotient positive definiteness.

## Independent implementation

`evidence/diag_theta_six_point/independent_replay.py` imports neither the
primary evaluator nor its matrix code. It directly sums the displayed original
theta summands after the even extension and integrates the **raw** M and C
moments; it uses none of the primary evaluator's analytic normalization.

The argument guard permits exactly `0, 1/4, 1/2, 3/4, 1, 5/4`. All six were
evaluated at 256 bits with 36 lattice terms, real cutoff R=5 and adaptive
tanh-sinh quadrature (maximum degree 8). The integration is split at the
reflection point s=t. There was no additional stencil, spacing, root search,
candidate selection or refinement. The two moments share cached integrands,
but they are independently integrated with weights 1 and s^2.

The replay reconstructs the same 6-by-6 matrix from those six quotient values
and evaluates the **already frozen** dyadic vector:

```
v = (-1209425521, 3095606301, -4294967296,
      4294967296, -3095606301, 1209425521) / 4294967296.
```

It also reports the diagnostic eigenvalues of that same matrix, without
selecting a new vector. All values, primary archive hashes, code hash and
comparisons are in `independent.json`.

## Observations

- All six M, C and k values agree with the 256-bit primary evaluation. The
  largest observed relative differences are approximately `1.08e-71` for M,
  `3.84e-69` for C and `3.85e-69` for k (rounded upward here for summary).
- The maximum observed absolute matrix-entry difference is `1.25e-71`.
- The same rational form is approximately `+0.00168886096494128373566`;
  its relative difference from the primary result is approximately `1.17e-69`.
- The diagnostic minimum eigenvalue is approximately
  `+0.00052817273088790117508`; all six diagnostic eigenvalues are positive.
- The completed independent calculation took approximately 13.61 seconds.

These are ordinary high-precision numerical observations, **not error bounds**.
The final argument is the least accurate relative replay, as expected for its
very small raw moments; the agreement is nevertheless far tighter than the
registered `2^-40` diagnostic threshold.

## Complete-tail accounting and limits

For real arguments let d=pi/2 and
`S_j = sum_(n>=1) n^j exp(-pi*(n^2-1))`. Polynomial-exponential maxima give
`abs(phi(u)) <= K exp(-d exp(2 abs(u)))`, with approximately K=6.63579.
Each S_j is evaluated through n=40 plus its positive geometric tail majorant.
For n>=37 the discarded summands decrease in `exp(2 abs(u))>=1`, giving a
uniform lattice error delta. On [-R,R], the product error is bounded by
`2*K*exp(-d)*delta + delta^2`, integrated with both weights. For `abs(s)>R`,
`max(abs(s+t),abs(s-t))>=abs(s)` supplies both real tails.

The archived ordinary-number evaluations of these majorants are approximately
`1.51e-1859` and `1.26e-1858` for the discarded lattice contributions to M and
C; the corresponding integration-tail formulas are below `8.14e-15030` and
`2.04e-15028`. They retain all omitted lattice terms and both real ends.
They have **not** been outward-rounded. The tanh-sinh library error estimates
are heuristic; complete quadrature, roundoff and ratio errors remain unbounded.
None of these numbers certify positivity or absence of a negative witness.

## Validation and disposition

The typed replay passes `pyright evidence/diag_theta_six_point/independent_replay.py`
with 0 errors, 0 warnings. No callable LSP diagnostics tool was available;
the configured CLI was used from the worktree root. A serialization-schema key
was corrected before the completed replay; no mathematical range or protocol
changed.

**No negative candidate is reproduced or discovered.** Complete Arb validation
is not warranted under the preregistered decision rule. The finite screen is
inconclusive for global quotient positive definiteness. End this screen,
without an enlarged stencil, certificate, manuscript version or research row.
The original signed theta/Laguerre input remains open.
