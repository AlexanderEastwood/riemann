## Current research checkpoint: September 21, 2026 — v1.19 finite-source removal cannot shrink the unsigned prime norm

**Established:** every finite-codimension compression of the actual prime-shift operator has exactly its full ordinary operator norm. Its essential norm is the same, and subtracting a compact operator, including the rank-two pole operator, cannot reduce the complementary norm below that value. The sharp leading growth is `||T_pr||=(1+o(1))lambda`. **No G2 sign gap was closed.** These results rule out a small unweighted complementary arithmetic norm, not full signed Weil positivity or RH.

### Starting point and concrete attempt

Fresh reads and materialization recovered the complete v1.18 manuscript, current research log, revision notes, validation record and cumulative evidence bundle. The saved PDF was confirmed as v1.18, 137 pages. The prior checkpoint established zero continuum eigenfunction endpoints and the sharp gap-free complement reduction. Its next obligation was a signed bound for the entire source-orthogonal complement along growing windows.

This run tests a simpler possible prerequisite: could removal of a sufficiently large finite source block, or of a finite Fourier head, make the prime term small enough for the archimedean diagonal to dominate using an ordinary operator-norm estimate? This was not assumed. It is now falsified exactly. The prime norm's previously discussed large arithmetic scale is proved for the actual operator, not just for the sum of its coefficients.

### Exact recurrence and finite-rank obstruction

At fixed lambda let L=2log(lambda) and let T_pr be the bounded self-adjoint sum of both truncated translations by log(m), weighted by Lambda(m)/sqrt(m), with 1<m<lambda^2. A full-length translation is zero. For periodic integer modulations M_k f=exp(2pi i kx/L)f, conjugation only inserts the finitely many shift phases.

Pigeonhole simultaneous recurrence provides k_j->infinity for which all active phases tend to one. The proof covers exact rational recurrences as well as approximate irrational returns, and does not require rational independence of prime logarithms. Thus

`||M_kj* T_pr M_kj - T_pr|| <= 2 sum_m w_m |exp(2pi i k_j log(m)/L)-1| -> 0`.

For each fixed L2 vector f, M_kj f tends weakly to zero by the Riemann–Lebesgue lemma. Any finite-rank projection P and any compact C consequently satisfy P M_kj f->0 and C M_kj f->0 in norm. Writing Q=I-P gives

`Q(T_pr-C)Q M_kj f - M_kj T_pr f -> 0`.

Taking norms and a supremum over unit f proves `||Q(T_pr-C)Q|| >= ||T_pr||`. With C=0, compression contractivity proves equality. With P=0, taking the infimum over compact C identifies the essential norm. No domain assumption is needed for the finite-rank source block; all operators involved here are bounded at fixed window.

The statement is pointwise in lambda and therefore applies to any family of finite-rank removals, however quickly the finite ranks grow with lambda. It does not provide a recurrence frequency bound uniform in lambda. The optional parity strengthening suggested in review is not needed and is not claimed in this release.

### Sharp actual operator scale

Use the positive physical weight `phi(x)=a(x)+b(x)`, with `a=exp(-x/2)` and `b=exp(-(L-x)/2)`. Define strict sums `Psi(X)=sum_(1<m<X) Lambda(m)` and `S(X)=sum_(1<m<X) Lambda(m)/m`. Direct substitution gives

`T_pr phi / phi = [a(S(exp(L-x))+Psi(exp(x))) + b(Psi(exp(L-x))+S(exp(x)))]/(a+b)`.

The leading constant follows from the exact identity `a exp(x)+b exp(L-x)=lambda(a+b)`. For any delta>0, the unconditional prime number theorem supplies a finite C_delta such that `|Psi(X)-X|<=delta X+C_delta` for every X>=1, including the small-X range. Chebyshev and partial summation give `0<=S(X)<=C(1+log X)`.

Uniformly in physical position,

`(1-delta)lambda-C_delta <= T_pr phi/phi <= (1+delta)lambda+C_delta+C(1+L)`.

The weighted Schur inequality proves the upper norm bound; the Rayleigh quotient of phi proves the lower. Divide by lambda, let lambda grow, and then let delta decrease to zero. This proves the exact leading asymptotic `||T_pr||/lambda->1` without RH. The finite-rank norm equality transfers it unchanged to every finite-codimension complement.

Primary reference for the classical prime number theorem: NIST DLMF Section 27.12, https://dlmf.nist.gov/27.12. The equivalence with the von Mangoldt form follows by partial summation and the smaller prime-power contribution. The operator argument and normalization are written out in the manuscript, not imported from the source.

### Consequence and explicit limits

For the paper's specific whole-space scalar tail budget, which subtracts an unsigned prime norm and other nonnegative errors from log((N+1)/L), positivity requires

`log((N+1)/L) > ||T_pr|| = (1+o(1))lambda`.

Even using the exact compressed norm cannot remove this exponential-in-lambda cutoff requirement. Enlarging a finite source block does not help that scalar-norm method. The pole operator is rank two, hence its inclusion cannot make the ordinary norm of the combined prime/pole operator small on the finite-codimension complement.

This is not a necessary cutoff for actual Weil positivity. The modulation sequence can recover the prime norm only at frequencies much higher than the first omitted mode, where the archimedean logarithmic energy is correspondingly larger. Consequently frequency-weighted unsigned estimates and directional inverse-action bounds are not excluded. The prior broadly worded sentence about every scalable complement theorem requiring signed cancellation was narrowed to avoid claiming otherwise. No negative direction of the complete Weil form is obtained.

### Independent review and computational checks

A separate adversarial agent checked recurrence, weak convergence, finite-rank removal, exact shift weights, the positive weight identity, the uniform-in-position PNT estimate and the scope of the scalar-budget conclusion. The saved review explicitly distinguishes the failed ordinary-norm shortcut from viable frequency-weighted estimates. This is internal review only.

The numerical script checks the exact autocorrelation formula for phi and independently integrates the physical quadratic form at lambda=2 and3. At 60 decimal digits the discrepancy is below 1e-50. It also evaluates trial Rayleigh values at lambda=2,3,5,10,30,100,300; the ratio to lambda is approximately 1.026889 at lambda=300. This is neither an interval norm certificate nor the asymptotic proof.

At lambda=2, a concrete integer modulation k=381074 leaves normalized P64 head norm about 9.52e-13, while the prime Rayleigh quotient differs from the unmodulated trial value by about 4.7e-14. These non-certified computations illustrate recurrence and escape from a finite head. They are not evidence of a negative complete-Weil direction or evidence for RH.

### Result of the attempted route and next step

The attempt to obtain a small unweighted prime/pole norm by finite source removal fails by theorem. The two new analytic results sharpen the obstruction and prevent repeated work on that false prerequisite. They do not establish the complementary arithmetic sign or close G2.

The next concrete test is a frequency-weighted prime comparison on the actual Fourier tail: retain the increasing positive logarithmic diagonal inside the two-sided inverse-square-root weighting instead of replacing it by its minimum. Quantify the directional weighted norm or residual Gram as lambda grows, with the exact signed pole and archimedean terms retained. A finite-window diagnostic can test this bound, but a proof requires uniform control on an unbounded family. Keep source removal, literal Fourier cut and sampler graph defect explicit. No publication or outside contact occurred.
