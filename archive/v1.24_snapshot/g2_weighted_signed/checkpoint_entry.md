## Current research checkpoint: September 21, 2026 — v1.20 signed energy control on the complete lambda=4 Fourier tail

**Established:** at lambda=4, for every complex vector in the closed Weil form domain supported on literal Fourier indices |n|>16,

`QW_4(f,f) >= 10^(-8) sum_(|n|>16) (-A_n)|f_n|^2`.

The exact archimedean diagonal is retained and is positive on this tail; its proved lower bound is greater than 1.7940. Both complex parity sectors and every omitted Fourier mode are covered by interval certificates and analytic remote moment bounds. This closes a **larger fixed-window tail-sign obligation**. It does not prove full positivity at lambda=4, and **no growing-window G2 sign gap was closed**. G2 and RH remain open.

### Current input and selected target

Fresh saved-file reads confirmed v1.19, its current log and revision notes. Remote materialization returned transient HTTP502 errors; the exact just-saved local working copies remained available with matching authoritative file identities, versions and byte sizes. Those current copies were retained, not reconstructed from an earlier scratch state. The cumulative archive is preserved and validated. The prior checkpoint's next target was a frequency-weighted comparison retaining the increasing logarithmic diagonal and the signed arithmetic matrix.

We set `D=diag(a_n)`, `a_n=-A_n` exactly, on a tail where it is positive. Write the actual compressed operator as `W=D+R`, retaining prime, signed pole and off-diagonal archimedean terms in R. The exact positivity target is `D^(-1/2) R D^(-1/2) >= -I`. A two-sided norm contraction is stronger and need not hold.

### First attempt: a two-sided energy norm bound fails

A floating exploration assembled the actual Fourier matrices at lambda=3,4,5,8,10,16,24 with literal cutoffs and separate diagonals. At lambda=4, N=16, M=256, the even normalized matrix had a positive top eigenvalue about 2.05254. At several larger windows the computed lower eigenvalues reached double-precision noise. Those tiny negative values are unresolved roundoff, not negative Weil directions.

An exact dyadic vector suggested by the positive eigenvector was then certified in Arb. It is supported on 17<=|n|<=256 and satisfies

`2.05254409540345 < QW_4(v,v)/<Dv,v> < 2.05254409540346`.

Its energy minus twice its exact diagonal energy exceeds0.0525 in the saved normalization. This disproves `||D^(-1/2)(W-D)D^(-1/2)||<=1` at that tail, because of a positive direction. It does not disprove the desired one-sided sign. This correction motivated the successful signed calculation.

### Successful one-sided certificate

Apply the existing directional verified-solve machinery to `W_4-cD` with exact c=1/100000000 on Q16. All finite rows use the full actual arithmetic matrix. The exponential archimedean-series tails are bounded explicitly. The exact pole diagonal has denominator `(L^2+16*pi^2*n^2)^2`; it is never a divided-difference limit.

A physical weight `phi(x)=exp(-x/2)+exp(-(L-x)/2)` yields a prime norm upper bound below4.624042316766478. The ratio is a linear-fractional function of u=exp(x) between rational breakpoints1,16,m,16/m. Every one-sided breakpoint is evaluated and the selected upper endpoint is rigorously checked against every candidate. The active prime powers are2,3,4,5,7,8,9,11,13; m16 is a zero full-length translation.

Use R_L=64/255, C_L=1 and h_L=9/16. The remote inverse weights are

`g_n=(1-c)(log(n/L)-E_L(2*pi*n/L))-kappa`,

with `kappa=M_phi+2/t_*` for even parity and the additional `pi/2+4h_LL/(pi^2N)` for odd parity. Only the archimedean diagonal is scaled by1-c. The off-diagonal losses remain unscaled.

Parameters:

| sector | finite head indices | solve support | remote starts after | moment order |
|---|---|---|---|---|
| even |17..512 |513..1024 |4096 |48 |
| odd |17..1536 |1537..2048 |4096 |64 |

The respective remote lower constants exceed0.59418 and0.12179. The finite heads have496 and1520 coordinates. These are internal certification blocks; the literal tail being proved starts at17 throughout. The large remote cutoff is not claimed to have disappeared.

The exact frozen dyadic solve Z gives G=I-Z, signed K_Z and residual R. All rows through4096 are computed. The existing full-index moment formula supplies an upper Gram for both infinite tails, with squared geometric remainder constants about1.025e-60 (even) and4.716e-41 (odd). The lower matrix is

`L_cert=K_Z-sum(R_n*R_n/g_n)-U_J/g_(J+1)`.

An inverse-Cholesky matrix proposed in double precision is frozen to exact dyadics C. It is only a witness. Outward interval evaluation verifies every row of `C L_cert C*` is strictly diagonally dominant with positive diagonal. This proves positivity of L_cert independently of how C or Z were computed. Square completion proves the complete infinite-tail bound. Reflection decomposes the complex Hilbert space into orthogonal even and odd reducing sectors, so the two certificates prove the assertion for arbitrary complex vectors.

The even witness was replayed at256 and320 bits with every positivity gate checked. The odd witness was formed at256 bits and replayed at320 bits with the tightened gates. The same dyadic witness hashes must match. The current reports, rather than the preliminary floating pilot, are the proof artifacts.

### Adversarial corrections and discarded intermediates

An independent assembly comparison found an early coding error: the new pole diagonal used the square of an already squared denominator. The error was corrected before any result was integrated. All old `sequences_l...` caches and their preliminary outputs are excluded from the evidence archive; only `sequences_v2...` can be read by the final verifier. The corrected Arb and independently assembled double sequences agree to below1.8e-13 through index256. This comparison is a diagnostic, not the proof of those entries.

The adversarial reviewer also tightened two gates: choose the prime bound by comparing exact upper endpoints, not floating midpoint ordering; verify every Gershgorin row is positive, not merely the row chosen by a floating minimum. The certificate directly checks that the analytic archimedean lower estimate at n17 is positive. The final runs use these gates. Full residual rows, all scale factors and the correct first-slot-linear interpretation are retained.

### Analytic results that delimit the weighted route

1. **Ordinary-error conversion.** If D>=d0I>0, R>=-CI and D^(-1/2)RD^(-1/2)>=-(1+eta)I, then `W>=-eta*C/(1+eta) I`. The proof combines W>=-eta D and W>=D-CI. The scalar model D=C/(1+eta), R=-C proves sharpness. Thus eta_lambda->0 alone is insufficient when C_lambda grows; the sufficient ordinary-error scale is eta_lambda*C_lambda->0. No signed arithmetic estimate is assumed to follow from this reduction.

2. **Compact but not Schatten.** For every fixed window with an active prime shift and every positive diagonal a_n~log|n|, the weighted prime operator is compact but in no finite Schatten class. Its diagonal is a nonzero finite cosine sum divided by a_n. The numerator has a strictly positive Cesaro mean square, without any rational-independence assumption, and is bounded away from zero on a positive-density set. Its pth-power diagonal sum therefore diverges. For the exact archimedean diagonal the complete signed remainder has the same obstruction: the pole correction is O(n^-2) and the archimedean remainder has zero diagonal. A global weighted Frobenius tail budget is impossible. This does not affect separated finite-column residual Grams, which retain off-diagonal decay.

3. **Sharp fixed-window weighted-tail scale.** At each fixed lambda, `(log J)||Q_J D^(-1/2) T_pr D^(-1/2) Q_J|| -> ||T_pr||`. Compact subtraction before weighting leaves the leading constant unchanged. The lower bound uses a fixed norm-testing Fourier polynomial and relatively dense returns of the finite vector of shift phases; the upper bound follows from the minimum diagonal. The recurrence gap depends on the window and tolerance. This theorem cannot be combined with ||T_pr||~lambda to claim a uniform lambda/log(J_lambda) lower bound in a joint limit. No such quantitative recurrence rate is proved.

### Primary-source research and scope

The actual Fourier matrix was checked against Connes, Consani and Moscovici, *Zeta Spectral Triples*, arXiv2511.22755v1, Sections3–4: https://arxiv.org/html/2511.22755v1. Their opposite sesquilinear convention is translated as already fixed in the manuscript; the real Hermitian entries and quadratic signs are unchanged.

A relevant new comparison is Xuefeng Zhu, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom decay law*, arXiv2608.24827v2, revised September2,2026: https://arxiv.org/abs/2608.24827v2. It studies finite-window certification and a pointwise prime-comb envelope barrier. This is contextual related work; no external computational certificate or conjectured asymptotic is imported into our proof. Its finite-window conclusions do not supply uniform G2.

### Next concrete obligation

At lambda4 the positive tail reduces full positivity to the signed effective matrix `F-B*T^(-1)B` on E16, with17 even and16 odd coordinates. This is a33-dimensional effective problem with an infinite inverse correction, not the raw33-by33 Weil matrix. Next compute and certify an inverse-action enclosure for these remaining columns using the newly proved tail lower weights. A failure of a lower enclosure must not be called a negative Weil direction.

For G2 itself, the remaining task is an ordinary lower bound tending to zero along an unbounded family of windows, with the arithmetic scale in the weighted-to-ordinary conversion retained. The known weak G1, the zero continuum endpoint, the literal physical evaluation and Fourier cut, the separate logarithmic diagonal, and the sampler's explicit graph defect are unchanged. No publication or outside contact occurred.
