# Growing-window diagnostics for v1.25

The complete even certificate at lambda=4 is separate from this finite study. Its rigorous generalized margin exceeds 0.62629 and includes every residual row. The following margins instead compare **finite** Schur complements at retained/test cutoffs 256/384, with even heads through lambda squared. They omit all modes beyond 384 and are not complete inverse upper bounds. In particular, the finite lambda4 margin below is not supposed to equal the complete-trial margin.

| Window | Head dimension | Finite relative margin | log10 cond(V) | Reference-column headroom | First admissible even N | First admissible odd N |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 10 | 0.781598 | 18.96343 | 521.339 | 44 | 209 |
| 4 | 17 | 0.545521 | 37.51866 | 93.717 | 283 | 1360 |
| 5 | 26 | 0.341968 | 61.60390 | 710.489 | 1502 | 7224 |
| 6 | 37 | 0.191097 | 91.13502 | 1204.37 | 7488 | 36021 |
| 8 | 65 | 5.75469e-101 | 139.45064 | 1.59185 | 124442 | 598623 |

The finite eliminations and head signs are interval-positive at 4096 bits with 192 archimedean series terms. Displayed condition numbers and margins are midpoint numerical diagnostics, except any separately stated rational or interval threshold in the JSON records. The far-cut columns are rigorous scalar analytic thresholds, freshly verified at each window at both 320 and 384 bits. They certify only the remote block, not the growing intervening head or inner inverse factors.

The generalized relative margin is invariant under a common invertible head congruence. Separate ratios of minimum eigenvalues and the displayed condition of V depend on coordinates. The reference column is the first canonical head direction after its specified energy normalization; it is not the archived v1.24 physical direction. The latter has complete headroom >12.1284 for the new lambda4 trial, compared with about22.71 for the old single-column trial. Trial dependence is distinct from congruence dependence.

The finite margins decline from lambda3 through lambda6. At lambda8, computing 1-theta in double precision rounds the margin to zero and produces tiny signed artifacts; these are not negative-form certificates. The interval head test is positive. An independently replayed frozen-vector Rayleigh upper and interval LDL lower give the rigorous finite bracket 5.697e-101 < margin < 5.755e-101. This resolves the finite scale without interpreting binary64 signs. It is not an infinite-tail or asymptotic conclusion. Large head condition numbers mean ordinary coordinates cannot be compared by raw pivots. Neither the observed decline nor the positive finite signs settle the complete growing-window estimate.

The method-specific cutoff theorem is stronger than extrapolating this table: for fixed c<1 the present scalar far weights require N+1 > L exp(M_phi/(1-c)), hence liminf log((N+1)/L)/lambda >= 1/(1-c). This proves an exponential cost for this majorant, not a general impossibility result.

Next: improve the signed far comparison or build and bound the growing inner witnesses at this cost. A complete odd lambda4 certificate remains a separate local target. A cofinal ordinary-error estimate tending to zero remains the RH target. No unverified lambda4 constants were transferred to another window.
