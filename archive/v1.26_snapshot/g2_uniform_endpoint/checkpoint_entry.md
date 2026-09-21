## Current research checkpoint: September 21, 2026 — v1.18 continuum endpoint proof and complementary sign reduction

**Established:** every eigenfunction of the complete canonical fixed-window Weil operator has a bounded representative with continuous zero physical boundary trace. Its boundary decay is at most a constant times the inverse square root of the logarithm of inverse boundary distance. This settles the continuum endpoint question and **falsifies the proposed nonzero endpoint comparison with the repaired source**. A sharp complementary-form estimate removes an unnecessary positive-gap hypothesis from one growing-window route. **The growing-window arithmetic sign, G2 and RH remain open.**

### Starting point and selected obligations

Fresh saved-file reads confirmed the complete v1.17 manuscript and persistent log. That release had already certified positivity, simple even ground ordering and an ordinary source-to-ground overlap at lambda=3 for the complete operator. Its open targets were control as the physical window grows and the physical endpoint of the actual ground state. This checkpoint addresses both analytically. The valid cumulative v1.17 archive was read and checked locally; no missing historical result was reconstructed by assumption.

The endpoint goal needed correction. Small ordinary residual and ordinary overlap do not themselves transfer an endpoint. Instead of extrapolating a finite endpoint numerically, we identified the singular part of the actual operator and proved its boundary regularity. The analysis uses the actual first-slot-linear convention, physical logarithmic interval (0,L), L=2log(lambda), normalized basis L^(-1/2) exp(2pi i n x/L), exact prime/pole signs and logarithmic diagonal. It does not modify the literal Fourier cut or remove the corrected sampler's graph defect.

### Exact operator identity and domain gate

Write A=(1/2)L_Delta^Dir for the restricted, exterior-Dirichlet logarithmic Laplacian, with full-line symbol log|t|. This is not the spectral logarithm of the Dirichlet Laplacian. The complete operator equals A+K_lambda, with equality of operator domains. K_lambda consists of:

- the scalar -log(2pi);
- the symmetric kernel minus k(|x-y|), k(y)=exp(y/2)/(2sinh(y))-1/(2y), with k(0)=1/4;
- the actual negative truncated prime shifts, including both orientations;
- the signed pole contribution 2cosh((x-y)/2), retaining its negative sinh rank-one part.

The scalar follows exactly from the integral of csch(y)-1_(y<1)/y, which is log(2). A common bound on all L^p norms of K_lambda is log(2pi)+2 integral_0^L |k(y)|dy+2P_lambda+4sinh(L/2). Compactly supported smooth functions form a common closed-form core: smooth endpoint tapers of a finite periodic Fourier sum converge in H^s for every fixed 0<s<1/2, hence in the logarithmic form norm. This identifies the realizations without imposing the endpoint conclusion as a premise.

### Bounded eigenfunctions, then the boundary theorem

An arbitrary L2 eigenfunction is not assumed bounded. For small epsilon, split

`A = A_epsilon + (log(1/epsilon)-gamma)I - J_epsilon`,

where A_epsilon is the nonnegative killed small-jump generator and J_epsilon integrates f(y)/(2|x-y|) over |x-y|>=epsilon. The first resolvent is a contraction on both L2 and L-infinity, while J_epsilon maps L2 to L-infinity with norm at most (2epsilon)^(-1/2). Choose a=log(1/epsilon)-gamma-mu>||K_lambda||. The same convergent Neumann series in L2 and L-infinity solves (A_epsilon+a+K_lambda)u=J_epsilon u. Uniqueness identifies its bounded solution with the original eigenfunction.

Consequently L_Delta u=2(mu u-K_lambda u) has bounded right-hand side. The interval satisfies the exterior uniform sphere hypothesis of Hernandez-Santamaria, Lopez Rios and Saldana, Theorem 1.1. Their theorem now applies and gives continuous zero extension and

`|u(x)| <= C sqrt(ell(d(x)))`, `ell(r)=1/|log(min(r,.1))|`, `d(x)=min(x,L-x)`.

The argument applies to every eigenfunction, without positivity or spectral-order assumptions. For complex functions it applies to real and imaginary parts. The constant is fixed-window and may depend on lambda, the eigenvalue and the eigenfunction. No useful uniform growing-window constant was established.

### Endpoint consequences and the failure of graph-norm transfer

Since the repaired source has nonzero physical endpoint B_lambda, the complete eigenfunction has exact relative endpoint mismatch `|p_lambda(0)-c u(0)|/|B_lambda|=1` for every scalar c. This falsifies nonzero continuum endpoint matching. It does not negate the prior ordinary overlap certificate or the finite source endpoint calculations.

A positive Fejer kernel gives the quantitative filtered endpoint estimate

`|sigma_(N-1) u(0)| <= C sqrt(ell(L/sqrt(N))) + ||u||_infinity/(2sqrt(N))`.

The normalization is the actual physical L^(-1/2) Fourier factor. The proof splits at distance L/sqrt(N), with far-kernel mass bounded by 1/(2sqrt(N)). This is an O((log N)^(-1/2)) fixed-window filtered estimate. It does not assert convergence of sharp Fourier endpoint sums or supply a joint cutoff/window estimate for finite-compression eigenvectors.

There is an exact counterexample to physical trace continuity in the Weil graph norm. The real even shell `h_N=sqrt(L)/(2N) sum_(N<|n|<=2N) U_n` has endpoint one and norm sqrt(L/(2N)), whereas its complete Weil operator norm is O_lambda(log N/sqrt(N)). Thus the endpoint map on the polynomial core is not even closable in that graph norm. This does not preclude the independently obtained zero continuous trace on actual eigenfunctions; it explains why graph convergence alone cannot prove it. The distinct logarithmic-derivative graph defect in the sampler is retained.

### Sharp complement bound, and what it does not prove

For a lower-bounded self-adjoint A, a finite-rank orthogonal P with range in D(A), Q=I-P and ||AP||<=epsilon, the exact form expansion yields

`|q(f,f)-q(Qf,Qf)| <= (2/sqrt(3)) epsilon ||f||^2`.

Indeed, with h=Pf and g=Qf, the difference equals Re<Ah,h+2g>. The maximum of t sqrt(4-3t^2) is 2/sqrt(3). The constant is sharp, witnessed by `A=-(epsilon/sqrt(3))*[[1,sqrt(2)],[sqrt(2),0]]`. Therefore a complementary lower bound q|Q>=-eta I implies `inf spectrum(A)>=-eta-2epsilon/sqrt(3)`, without a positive complementary gap.

The prior full operator residual supplies epsilon_lambda->0 for the rank-one projection onto either normalized repaired source considered in Proposition 20.39. The remaining input can therefore be phrased as asymptotic nonnegativity of the whole source-orthogonal complement. A growing source block would need an additional uniform ||W_lambda P_lambda||->0 estimate.

This reduction does not establish the complementary sign. A fixed negative compact test of energy -delta remains negative after projection off any block whose operator residual tends to zero: its projected energy is <=-delta+2epsilon/sqrt(3). Thus source removal cannot hide an RH-violating compact direction. The desired cofinal complementary sign remains RH-strength by the paper's existing nested-support criterion. The nested-window and RH-strength observations were already in the paper and are not counted as new results.

### Adversarial review, sources and diagnostics

Two independent agent reviews checked the exact kernel normalization, form-domain identification, boundedness bootstrap and the boundary theorem hypotheses. The complementary inequality and the graph-trace counterexample were separately checked. These are internal reviews, not external referee validation.

Primary sources consulted:

- Chen and Weth, *The Dirichlet Problem for the Logarithmic Laplacian*, Theorems 1.1 and 3.1: https://arxiv.org/pdf/1710.03416.
- Hernandez-Santamaria, Lopez Rios and Saldana, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, Theorem 1.1, version 2 (July 3, 2024): https://arxiv.org/pdf/2401.18033.

The archived 90-decimal diagnostic compares the original and decomposed constant-mode archimedean diagonal at lambda=1.2,2,3,10. The largest discrepancy is below 5e-91. This detects normalization mistakes but is not a proof; the exact integral establishes the identity. No numerical endpoint extrapolation is used in the boundary theorem.

### Failed approaches, scope and next concrete step

1. Nonzero endpoint transfer from the source to the complete ground is false, not merely unproved.
2. Ordinary operator residual or graph-norm control cannot by itself control the physical trace; the shell above disproves that implication.
3. Continuity of a periodic representative does not alone justify sharp Fourier endpoint convergence. Only the specified positive filter is estimated here.
4. The new block inequality removes a gap denominator but leaves the arithmetic complementary sign unresolved. It is not a positivity proof.

Next, seek a signed lower estimate for the entire source-orthogonal complement as lambda grows, using the existing physical prime/pole/archimedean decomposition and retaining the directional Schur residual. A larger-window certificate can test the proposed bound but cannot replace the unbounded-window argument. Finite-compression endpoint control, when needed for a sampler construction, must be estimated on that actual finite object rather than through a nonzero continuum ground endpoint. G2 and RH remain open; no G2 sign gap was closed. No publication or outside contact occurred.
