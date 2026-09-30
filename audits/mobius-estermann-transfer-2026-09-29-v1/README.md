# Projected Möbius cost: cotangent/Estermann applicability audit

Reviewed base: `716ae6af503f8f2f539550ce32f9b2a398f2870a` (PR65).
[Readable report](../mobius-estermann-transfer-2026-09-29-v1.html).

**Outcome: no new arithmetic estimate admitted.** The checked Maier–Rassias
statements do not directly bound NS98's projected cost. Their original
parameter ranges leave the comparable-index region untreated, and no
uniform extension, weighted projected-kernel transfer or complete cost
bound has been supplied. This is a bounded applicability audit, not an
exhaustive literature review or a proof that such estimates are impossible.

**Wall check: Same open gap**, MOBIUS-COST and the separate MOBIUS-MARGIN
input (NS92/93/98). The target, coefficient rule, normalization and required
growing dyadic-index average are unchanged. No new numerical test,
research row, theorem node, thaw, manuscript version or RH claim.

## What changed in our assessment

NS92's literature record checked only the abstract of arXiv:1806.05070.
This audit reads its Theorem 2.1, the predecessor's Theorem 1.1, and the
survey's restatements. The original and survey PDFs were visually checked:

- Maier–Rassias, arXiv:1705.09921v1, Theorem 1.1, printed page 3:
  **`0 < delta < D/2`**, `k^(2 delta) <= B <= k^D`,
  `k^(-delta) <= eta <= 1`. It bounds the stated sum of
  `mu(h) g(h/k)` on `[Bk,(1+eta)Bk)` by `O((eta Bk)^(1-beta))`,
  with positive `beta` depending on the fixed parameters.
- Maier–Rassias, arXiv:1806.05070v1, Theorem 2.1, printed page 3:
  `D >= 2`, sum on `[k^D,2 k^D)`, bound `k^(D-z0+epsilon)` with
  the paper's explicit `z0`. No numerical value of `z0` was needed.
- Derevyanko–Kovalenko, arXiv:1811.04399v1, Theorem 6.1, printed page 20:
  the survey prints **`0 <= delta <= D/2`**. Its delta-zero endpoint is
  not a hypothesis of the original theorem. No independently justified
  endpoint extension was found in the checked passages. We neither import
  it nor claim to have proved that extension false. Theorem 6.2 retains
  the second paper's `D >= 2` restriction.

This is a source discrepancy, not a correction to a repo theorem: no
existing project argument had imported that delta-zero endpoint.
The publisher DOI was attempted but not accessible through the web reader;
the versioned arXiv statements are the reviewed primary sources.

## Exact target and conditional transfer

Keep `d_n=-mu(n) log(2N/n)` on `N<n<=2N` and the complete q=2 Gram blocks:

    H_N = D - C^T G^(-1) C,
    K_N = d^T H_N d.

The cost target is `sup_J (1/J) sum_{J<=j<2J} K_(2^j) < infinity`,
for all sufficiently large dyadic J. NS98 already bounds the diagonal;
the signed projected cross sum remains unestimated. NS93's compatible
positive average of the normalized lower numerator is still a separate
required input. No cost-only RH implication is used.

There is a valid one-sided smoothing transfer, so merely saying “the
papers use q=1, while we use q=2” would be an inadequate rejection.
Let `rho_n` be the unsmoothed atoms in `L2(0,infinity;dx)`, and let
`sigma_n=J rho_n`, with the existing NS61 Mellin operator `||J||=2`.
For the same fixed new coefficient vector d, define

    K_N^(1)(d) = min_c ||sum_new d_n rho_n + sum_old c_m rho_m||^2,
    K_N^(2)(d) = min_c ||sum_new d_n sigma_n + sum_old c_m sigma_m||^2.

Choose the q=1 minimizing old vector c in the q=2 variational problem.
Boundedness of J immediately gives

    K_N^(2)(d) <= 4 K_N^(1)(d).

This is bookkeeping from the existing bounded-map argument, not a new
arithmetic theorem or a newly proposed control inequality. The q=2
minimizer may use different coefficients; no commutation of projection
and J is asserted. A bounded average for the **complete** q=1 selected
cost would therefore supply the q=2 cost half. A sufficiently strong
complete unprojected q=1 bound would also suffice by choosing zero old
coefficients. Neither bound follows from the checked cotangent statements.

Ehm's Proposition 3.1 also expresses q=2 entries as continuous scale
averages of q=1 entries. That identity alone does not apply the rational
sum estimates uniformly through this integral or interchange the
size-dependent minimization with averaging. The bounded-J argument above
is the clean sufficient transfer already available from the repository.

## Where the literal arithmetic import stops

1. **Comparable indices.** In the new/new block, `N<m,n<=2N`, so
   `1/2<n/m<2`. In either orientation this does not reach the first
   theorem's `h/k >= k^(2 delta)` for any fixed positive delta and
   unbounded denominator k; the explicit theorem instead starts at
   `h >= k^2`. Reducing a fraction preserves its ratio. Bounded reduced
   denominators can be a separate part, but do not cover all pairs.
   This shows a missing domain of the literal application; it does not
   lower-bound that domain's contribution or say it dominates the norm.
2. **No uniform endpoint limit.** Setting delta to a size-dependent
   value tending to zero does not retain the fixed positive saving and
   constants in the statement. The required uniform dependence is absent
   from the result being imported. No limit theorem is inferred from
   the survey's weak inequality.
3. **All components of the cost.** A one-row estimate for the stated g
   sum is not an estimate for the complete quadratic cost. A transfer must
   keep tapers, gcd conventions in the rational formula, both orientations,
   elementary Gram terms, and all summation losses. Estimating a long,
   separated-index tail leaves a comparable-index remainder.
4. **Projection.** The full correction `C^T G^(-1) C` is retained in the
   target. Existing bounds on a raw cotangent row do not identify its
   weighted inverse-Gram correction. Discarding that nonnegative quadratic
   subtraction is a legitimate stronger upper-bound route, but the
   resulting complete raw cost must then actually be bounded. No such
   bound was obtained. Entrywise signs of the subtraction are not assumed.
5. **Rate and companion.** Any partial estimate must produce bounded
   means of K at the stated scales, after all these steps. Qualitative
   cancellation, a power saving for a different sum, or bounded cost with
   no compatible numerator is not that conclusion.

## Source conventions and controls

Only the stated g-sum theorem ranges are imported for comparison. No g
values, rational-point Fourier series or cotangent signs are evaluated,
and no unverified rational normalization is used to compute a Gram entry.
The scalar inequalities above do not depend on those conventions.

This is an existing-theorem applicability audit; it admits no new candidate
identity or sufficient RH condition. Davenport–Heilbronn and NS100/101
do not carry this exact Möbius coefficient rule and integer fractional-part
Gram family. They are not applicable to this literal transfer, not passed
screens. NS74's Gram-preserving changed-target control retains its force:
cost information alone cannot supply the compatible residual numerator.
No unrelated example screen was substituted for the audit.

## Decision and limits

Stop the direct Maier–Rassias substitution here. A reopening needs an actual
comparable-range estimate with its required uniformity, or another
complete bound for the selected projected/unprojected cost. This specifies
the missing input; it is not a proposed new lemma with a proof mechanism.
Do not respond to this result by enlarging a finite table, taking delta
toward zero numerically, or changing to another nearby positivity screen.

The bounded search found no applicable estimate among the checked sources.
It does not establish that none exists in the literature or that adapting
these authors' methods is impossible. Review was by the coordinator only;
no independent proof audit of the external papers was performed. Historical
documents, all registered mathematical statuses, all freezes and both
missing-original groups are preserved. RH and G2 remain open.
