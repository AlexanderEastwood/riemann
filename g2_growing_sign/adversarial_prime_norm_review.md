# Internal adversarial review: unsigned prime norm

September 21, 2026. The separate reviewer confirmed the principal statements. This is an internal mathematical review, not external peer review or proof-assistant verification.

## Exact finite-rank statement

There are only finitely many active shifts at each fixed physical window. A simultaneous torus recurrence sequence of integer Fourier modulations makes every shift phase tend to one. Rational dependencies do not obstruct recurrence. The pigeonhole argument covers both an unbounded sequence of approximate returns and exact periodic returns.

Conjugation convergence is in operator norm, because the translation sum is finite. Weak convergence of a fixed modulated vector follows from the Riemann–Lebesgue lemma applied to an L1 product. Finite-rank projections and arbitrary compact operators therefore vanish on these vectors. This proves the norm equality for Q T Q and the lower norm bound for Q(T-C)Q. No operator-domain assumption is used or needed: the prime operator is bounded at every fixed window.

The statement is pointwise in the physical window. Thus finite ranks and cutoffs may grow arbitrarily rapidly as functions of lambda without invalidating the equality. It does not assert a uniform recurrence frequency bound.

## Actual normalization and growth

For a=e^(-x/2), b=e^(-(L-x)/2), the forward/backward prime shifts give exactly the stated S and Psi terms. Their leading terms satisfy a e^x+b e^(L-x)=lambda(a+b), with L=2log(lambda). The weighted Schur bound uses the positive phi=a+b. Its minimum can shrink with lambda; boundedness away from zero is needed only at each fixed window.

For every delta>0 the PNT gives |Psi(X)-X|<=delta X+C_delta for every X>=1, including the small-X range. The constant error is averaged with weights a,b, so remains C_delta rather than growing with their ratio. The S terms have bound O(1+L). The resulting uniform pointwise lower and upper estimates sandwich the Rayleigh quotient and norm, proving norm(T)/lambda->1. Strict prime cutoffs change no a.e. shift identity and satisfy the same PNT estimate.

## Scope restrictions retained

The exponential cutoff consequence is solely for the explicit scalar tail budget that subtracts the full unsigned prime norm and additional nonnegative errors from log((N+1)/L). This budget can only become positive above the displayed exponential scale. It is not a necessary cutoff for actual Weil positivity.

In particular, a recurrence vector recovering the prime norm may lie far above the first omitted frequency. Its logarithmic archimedean energy can then be much larger than the minimum diagonal used in the scalar bound. Frequency-weighted unsigned bounds and directional inverse-action estimates remain viable; no failure of such a method is proved here.

The pole operator is finite rank and hence compact, so it cannot reduce the essential prime norm. This does not mean that the pole and prime forms fail to cancel on selected low-frequency vectors. It precludes only a small ordinary bounded-operator norm for the combined term on the full finite-codimension complement.

The manuscript does not use the optional parity strengthening suggested by the reviewer. Its whole-space statements already suffice for the stated obstruction, avoiding unnecessary additional claims.

**Conclusion:** the two analytic propositions and the carefully scoped scalar-budget consequence pass. G2's signed arithmetic estimate remains open.
