# NS-19 scope and proof review (same agent; not an external audit)

1. **Complete object.** The evaluator inequality applies to the even form
   domain, with the invertible head map and complete tail floor. The Schur
   residual cross term is bounded by sqrt(1-kappa), then retained in the
   positive 2-by-2 comparison. No positivity gluing without cross terms.
2. **Projection normalization.** f is unit norm; h is its nonzero orthogonal
   projection onto the complete simple even ground. h is not renormalized.
   Nonnegativity yields q[h] <= rho. The inherited derivative bound uses
   this same h, so its division into the evaluator budget is consistent.
3. **First zero.** The local simple zero comes from v1.42. The new 304
   strictly negative interval evaluations cover [0,gamma_1-0.1] exactly;
   the checker verifies dyadic coverage with rational arithmetic. Modes
   65..4096 have an explicit norm remainder and the old projection error
   covers the entire difference from the complete ground.
4. **Resolution.** R0 is a computed upper-bound budget, not a lower bound
   on the actual root error. A floor of this displayed estimate does not
   imply a no-go theorem for every possible use of the same archived data.
5. **Lower-energy direction.** For e=f-h and 0<=l<=mu0, spectral orthogonality
   gives q[e] <= b(rho-l)/(b-l). Solving its evaluator budget gives the
   threshold 3.2032006569...e-153; this is closeness to rho, not merely
   positivity or a lower bound of size 1e-153. The direct bound needs an
   upper ground-energy improvement and cannot be improved by substituting
   a lower bound. These logically different directions are explicit.
6. **Frozen trial caveat.** fhat(gamma_1) is certified about 1.0641e-40.
   Thus a tiny transfer error around this trial does not by itself give
   a gamma-centered 1e-71 bound. No claimed feasibility of the hypothetical
   energy gap and the diagnostic complete-root expectation is implied.
7. **Finite benchmark.** The +2.92504e-71 interval is for N=120 only,
   obtained during the original Task B. It is retained separately; no
   inference that the complete discrepancy actually has that scale.
8. **Preservation and replay.** Tagged v1.42 evidence stays unchanged.
   New interval gates replay at 1024/1280 bits using the archived complete
   residual inputs; no new full assembly, window or tail metric. Same-agent
   second implementation checks and Python diagnostics pass. G2/RH open.
