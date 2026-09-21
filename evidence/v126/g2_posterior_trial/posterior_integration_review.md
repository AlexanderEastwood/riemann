# Final adversarial review of the v1.24 insertion

Reviewed `posterior_insert.tex`, the updated verifier, and the certificate quantities used in the insertion. **No theorem-level blocking issue found.**

- The identity `S_infinity(v,v)=QW(g,g)-<T^(-1)e,e>` is exact for the stated finite graph-domain trial and coercive complete tail. Its expansion respects the first-slot-linear convention.
- The new energy and residual consistently use the unshifted Weil operator. The shifted inner operator is used only to give an inverse upper bound. No shift-energy or `cDz` term is omitted.
- The complete residual upper bound includes both the omitted far energy and the omitted mixed correlation. The fixed inner witness, source support through 4096, verification cutoff 65536, and remote moment parameters match the certificate.
- The outer head `v` is unchanged. The full-action code includes both normalized zero-mode couplings and the exact nonzero-mode diagonal. Added dense-row comparisons and the independently expanded trial-energy identity are appropriate checks; the finite iterative residual is correctly excluded from the proof.
- The old inverse-correction bounds are valid using the finer table and archived old trial interval. From the printed trial-energy and correction bounds one obtains the lower Schur value `3.0930954481e-20`, the old inverse correction between `3.2337000458e-20` and `3.3761889469e-20`, and a relative lower bound exceeding `0.47812018`. Thus the manuscript's rounded comparisons are safe.
- The conclusion is correctly restricted to one fixed even head vector. It does not infer positivity of its entire head, a negative vector from earlier failed majorants, or any growing-window/RH conclusion.

One rounding-level presentation point was sent to the parent: the coarse displayed `rho<0.165103` and the other rounded inputs yield `U<1.424889538e-21`, whereas the table's finer `U<1.424889e-21` uses the archived full intervals. That finer bound is independently valid. For arithmetic reproducible from the displayed values alone, tighten the displayed rho bound to `rho<0.165102333`, which the saved interval supports, or slightly relax the displayed U bound. This does not affect any proposition threshold.

**Resolved:** the parent applied the tighter displayed bound `rho<0.165102333` before rebuilding the complete PDF. The rounding presentation issue is closed; no outstanding correction remains from this review.
