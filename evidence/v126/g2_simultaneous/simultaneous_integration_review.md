# Final adversarial integration review: v1.25

Reviewed `simultaneous_insert.tex`, its integrated abstract/status and downstream scope statements, the complete relative-margin verifier and both saved precision reports, and the updated growing-window diagnostic gates.

**Outcome: no outstanding mathematical correction.** One statement-level issue was identified and corrected before this review was finalized: the joint-Gram proposition now explicitly requires `0 <= L_Y <= Y*Y`, which justifies its scalar inverse replacement. The implemented certificates already used L_Y=0 and were unaffected.

1. **Complete even sign.** The simultaneous trial identity, full-rank actual head check, and complete residual upper bound correctly imply positivity of the complete even Schur form at lambda=4. The previously certified coercive complete tail then gives strict positivity and a positive fixed-window coercivity constant for the entire even form domain. No coordinate LDL pivot is identified with an ordinary-norm spectral gap.

2. **Relative margin.** `complete_margin.py` certifies the exact rational threshold by strict LDL of `(1-62629/100000)K-U_(1/10)`. Both 768- and 896-bit reports give positive pivots for the same new trial witness hash. Consequently the strict generalized margin exceeds 0.62629. This is invariant under a common invertible congruence of K and U; it is not invariant under changing the finite trial itself. The manuscript makes the latter distinction when comparing single-direction headrooms.

3. **Rounded numbers.** The stated positive-pivot thresholds, joint-Gram pivot thresholds, and headroom greater than 12.1284 agree with the saved enclosures. The general joint bound and its scalar simplification now have sufficient hypotheses. Its cross centre is taken from one complete joint upper Gram, not invented from separate bounds.

4. **Scopes.** The abstract, version status, theorem, and downstream discussion consistently restrict the new complete positivity result to the even sector at lambda=4. The odd matrix tests are described as inconclusive, and no positivity on both parity sectors or growing-window estimate is asserted. The exponential cutoff proposition is correctly restricted to the present scalar far majorant.

5. **Finite window diagnostics.** The missing finite-tail prerequisite identified in the earlier review is now explicitly certified. For lambda=3,4,5,6 the saved 4096-bit reports distinguish their positive finite-tail/head gates from the numerical finite generalized margins, approximately 0.7816, 0.5455, 0.3420, and 0.1911. Each report explicitly states that a complete inverse upper bound is unavailable in this probe. The unresolved lambda=8 interval metric is not treated as a negative direction or as a complete certificate. These finite data support no broad conclusion about G2 or RH.

6. **Safe local LDL.** The new local LDL uses `x*x` for interval coefficient squares. This is a valid enclosure even for an interval containing zero. The reported earlier generic-power NaN issue could cause a strict positivity gate to fail; a NaN pivot cannot satisfy the prior `p>0` acceptance condition. The change does not turn a previously accepted positive gate into an unjustified one.

The retained open objective is a justified cofinal ordinary-error estimate, including the signed complete correction and its window dependence. The new fixed-window even result does not supply that estimate.
