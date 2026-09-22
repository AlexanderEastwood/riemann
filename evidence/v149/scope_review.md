# Internal analytic and claim audit — v1.49

Classification: internal review of exact identities, proved implications,
countermodels to general inferences, and explicitly open cofinal inputs.
No new numerical computation or independent adversarial certification.

1. The review is NS-32; the follow-up is NS-33. Original local NS-31/32
   claims were renumbered when NS-31 was assigned concurrently to a different
   audit. Claim history and both delivered audit versions are preserved.
2. PR #14's head 9b2b900 was built, not merged. Its exact weighted-cost
   implication passes; the biconditional does not. No v1.48 tag is created.
3. The density is normalized by X, has mass phi<=1, and is not normalized
   to be a probability conditional on beta<0. The coarea integral uses
   counting measure H^0. There is no extra reflection factor in m_tilde.
4. Absolute continuity is distinct from bounded density. At a critical
   value of finite analytic order r>=2, each branch contributes
   (X*r*|A|^(1/r))^(-1) |t-t0|^(1/r-1) (1+o(1)). This is locally
   integrable and essentially unbounded. It applies also at the depth
   endpoint via levels just above -D. Boundary critical points need an
   interior branch entering negative values, stated explicitly.
5. The critical-point result does not certify any diagnostic trough's
   location. It proves the structural issue whenever a complete negative
   component is in range. No fixed-window numerical gate is implied.
6. A finite density cap is an upper bound on every Borel level band. It
   requires the sum of inverse slopes, including all preimages. A lower
   slope bound at only a selected shallow bin is insufficient.
7. The derivative is of the complete corrected zero field; the displayed
   finite-prime derivative is justified directly. No interchange of
   derivative with a conditionally convergent infinite zero sum is used.
8. phi^2/R can diverge only if R->0; bounded above is not bounded below.
   Uniform density R=phi/D shows phi<=1 alone is not an obstruction.
   Critical points make the actual R infinite and the packing bound zero.
9. Countermodels comparing ZLD and the scalar are finite absolutely
   continuous measures with full support. They concern logical inference
   between general measure conditions, not the actual zeta field or
   logical independence of arithmetic conjectures.
10. QC_K uses an infimum over at most K levels including -D. No existence
    of a minimizing strictly spaced grid is assumed. Monotonicity in K
    is immediate. Positive minorant values do not create negative gaps.
11. Setwise domination of finite positive Borel measures integrates
    nonnegative Borel functions. Negative levels have no atoms at -D or
    0, so the interval endpoint convention is harmless. The source
    constraint and original energy remain explicit assumptions.
12. The packing bound is retained only with finite positive R. Uniform
    density gives exactly c=c'*phi and QC_K=phi*D/(2K).
13. QC_1 = phi*D - mean(beta^-) = integral_0^D (phi-F(t)/X) dt, with global
    depth D. The complete negative part is used only on [0,X].
14. The counterexample to QC_K>=kappa*QC_1/K has mass 1/2 and full support
    due to a bridge of mass 1/(2D^3). QC_1~D/2 but the two chosen levels
    give QC_2<=1/(4D)+1/(2D^2). This disproves the universal inference,
    not the possible arithmetic shape hypothesis.
15. QG requires QC_K->infinity for each fixed K, for a prescribed N(a).
    Together with uniform c0,Q* it forces K(a)->infinity for bounded loss,
    since any bounded-K subsequence contradicts the same lower bound.
    Linear growth requires the additional all-K shape hypothesis; linear
    in D further requires QC_1>=d0*D. Only sufficient implications claimed.
16. Source projection uses r, the full energy E, and the cross/source term.
    r^2<=1/4 and delta<=E/2 imply [E/2,2E] for E>0. Neither is provided by
    the source certificate alone. Recovering and certifying the LP vector
    and its overlap is explicitly named but not executed.
17. NS-28 raw code/output are unchanged. Only a notice correcting the
    continuum/histogram identification and lambda=4 feasibility is added.
    The source output's 0.636 ratio does not satisfy c'=1. The 200-bin DP
    uses bin-edge reconstruction levels; its costs are surrogate values.
    Extrapolations past K=32 are identified. No all-Borel WLH is certified.
18. The outcome is wrong crude scalar for critical-level measures, plus
    named exact-cost and packet inputs. No unconditional cofinal result,
    new window, tail metric, zero enclosure, optimization, G2 or RH claim.
