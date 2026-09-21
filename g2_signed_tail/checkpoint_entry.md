## Current research checkpoint: September 21, 2026 — v1.15 ordinary operator residual and sharp positive Fourier tail

**Closed: the ordinary source-mass, Rayleigh-value and full operator-residual prerequisites for the actual repaired fixed-order source and its literal polynomial Fourier projection. Improved: a positive entire omitted Fourier complement at lambda=3 already beyond N=256. The signed low-block/G2 gap is not closed; RH remains open.** The complete manuscript is now v1.15, 123 pages, with all 32 main sections, two appendices and 72 historical claim dispositions retained.

### Starting point and work selected

The current saved v1.14 manuscript and persistent log were checked before this continuation. The earlier fixed-window matrix certificate at lambda=3,N=64 does not control the infinite Fourier complement. v1.14's conservative complement bound only became useful at tens of millions of modes. This pass targeted two actual dependencies: a practical positive tail for a signed Schur solve, and the previously separate ordinary Rayleigh/residual assumptions. Three research/review agents participated at the user's explicit request; no positivity or RH assumption was introduced.

### Proved: nonzero ordinary source mass

Lemma 20.27 derives the exact Hermite limit of the unit-angular-normalized, repaired source:

`h_infinity(u)=(4*pi/sqrt(3))*u^2*(2*pi*u^2-3)*exp(-pi*u^2)`.

Its co-Poisson image f_infinity is inversion-even and square integrable in du/u. The actual p_lambda, zero-extended outside the physical window, converges to f_infinity in ordinary L2 at O(lambda^(-1/2)). The uniform fixed-mode approximation is the primary-source input from Connes–Consani–Moscovici, Lemma 7.2. The proof explicitly transfers their suitable normalization to the manuscript's exact unit norm using the squared-norm expansion; a naive L2 triangle estimate would lose the needed rate. The actual source coefficients and the exponentially small zero-value repair are included.

At u>=1 all limiting summands are positive, so the limiting norm is bounded below by the positive square root of integral_1^2 h_infinity(u)^2 du. A quarter of this value is an eventual common lower bound for p_lambda and k_lambda=P_N p_lambda. Here and throughout `N=ceil(lambda^8(1+L))`, `L=2 log lambda`. No effective threshold at lambda=3 is claimed.

### Proved: an absolute full operator residual on the same source

Proposition 20.28 gives, for c=2*pi*lambda^2 and all sufficiently large lambda,

`||W_lambda p_lambda|| + ||W_lambda k_lambda|| + ||W_(lambda,N) k_lambda|| <= C lambda^6 exp(-c/3)`.

This is the actual closed semilocal Weil operator, with the original physical scale, Fourier projection, separate logarithmic diagonal and first-slot-linear convention. It is an unweighted norm of the whole output, not merely fixed-band weak G1 or a numerical residual.

The proof uses v1.14's already-proved endpoint-normalized coefficient tail for every |n|>N. With W=D_d+[M_b,H], the weighted Chebyshev bound gives a commutator norm O(lambda), while the complete diagonal is bounded by C[lambda+1+log(2+|n|/L)]. Consequently the specific source's omitted input e=(I-P_N)p obeys the uniform graph bound

`||W_lambda e|| <= C |B_lambda| lambda^(-2)`.

The output, not the candidate, is then split at an auxiliary `M=ceil(exp(2c/3))`. Existing Proposition g1-sobolev is uniform over all periodic H1 test functions. Taking the dual supremum over unit vectors in E_M yields

`||P_M Wp|| <= C |B| r(lambda)[1+M/L+sqrt(M/L)]`.

There is no extra sqrt(M) from summing individual mode bounds. The complete off-diagonal matrix gives the Hilbert–Schmidt high-low estimate

`||Q_M W P_N|| <= C lambda sqrt(N/M)`.

Since the actual source norm is bounded, this is at most C lambda^5 sqrt(1+L) exp(-c/3). The physical endpoint size |B|<=C lambda^(11/2)exp(-c) and bounded r(lambda) finish the proof. The auxiliary exponentially large M is used only analytically and is not a new finite matrix or source cutoff.

Ordinary unit normalization is now justified by Lemma 20.27. Both the Rayleigh value alpha and the centered residual (W-alpha)u tend to zero at the stated rate. This closes the separate hypotheses in the G2 overlap calibration; it does not establish ground-state overlap. Dividing this upper bound by the exponentially smaller endpoint leaves a growing bound. No endpoint-normalized graph claim, growing-prolate-block operator estimate, or derivative norm estimate for the unbounded output is inferred.

### Proved: the whole omitted Fourier tail is positive at lambda=3,N=256

Proposition 20.21 keeps three previously discarded structures. First, truncated prime shifts have lower bound minus their maximum physical weighted degree, rather than minus twice their total mass. At lambda=3 the full-length m=9 shift is zero and the exact degree is

`M3=sum_(m=2,3,4,5,7,8) Lambda(m)/sqrt(m)=3.171298718...`.

Second, the negative pole is the rank-one sinh(x/2) term. Its Fourier-tail norm costs at most `4 sinh^2(L/4)L/(pi^2 N)` and vanishes in the even sector. Third, the archimedean sine sequence has an explicit uniform approximation to (pi/4)sgn(n), derived from its positive exponential series. The limiting even-sector commutator is the positive Hilbert matrix 1/[2(n+m)], while the whole-space norm loss is pi/2. The phase change between centered and unshifted Fourier bases was checked by both reviewers.

With `R_L=exp(-L/2)/(1-exp(-2L))`, `C_L=max(1,1/4+R_L)` and `t_*=2pi(N+1)/L`, the complete diagonal satisfies

`-A_n >= log(|n|/L)-E_L(|t_n|)`,

`E_L(t)=1/(15t)+7/(2t^2)+pi/(2Lt)+(2+2R_L)/(Lt^2)`.

This uses Binet's exact digamma formula, its recurrence and the convergent trigamma series; no differentiated asymptotic remainder is used. Every finite-L and logarithmic constant remains in the exact diagonal identity. Combining the three pieces yields

`Gamma_even=log((N+1)/L)-M_lambda-2C_L/t_*-E_L(t_*)`,

`Gamma_all=Gamma_even-pi/2-4sinh^2(L/4)L/(pi^2N)`.

The proof extends from finite Fourier sums to the entire omitted form domain using the established core. Independent 256-bit Arb evaluation certifies

`Gamma_all(3,256)>0.0148329`, `Gamma_even(3,256)>1.5867887`, `Gamma_all(3,512)>0.7085077`.

The scalar script and output are retained. No new head matrix was assembled and no full-window positivity was claimed. The older N=64 matrix certificate cannot be combined with this tail while ignoring the intervening modes or coupling.

### Exact signed certificate and what remains

For W=[[F,B*],[B,T]] with T>=Gamma I>0, let Z map the finite head into D(T), R=B-TZ, and K_Z=F-B*Z-Z*B+Z*TZ. The exact identity is retained with a sharper matrix-valued error:

`K=F-B*T^(-1)B=K_Z-R*T^(-1)R >= K_Z-Gamma^(-1)R*R >= K_Z-||R||^2/Gamma I`.

Keeping R*R preserves the directions in which the source residual is tiny; replacing it by its largest eigenvalue can destroy this information. This is an exact finite lower-bound criterion, not a proved sign for the actual K.

The revised overlap calibration now has a quantified remaining assumption. With epsilon_lambda=C lambda^6 exp(-c/3), an independent ground-space overlap kappa satisfying epsilon_lambda/kappa ->0 along unbounded windows would suffice. For example kappa>=exp(-theta*c), theta<1/3, would suffice. No such lower bound is known here. If the actual bottom level is <=-delta, then delta*kappa<=||Wu||; it can therefore coexist with the new near-zero source through exponentially small overlap. The diagonal countermodel diag(-1,epsilon), source (0,1), rejects the false inference from tiny residual to ground-state positivity.

### Adversarial review and discarded work

The adverse agent and an independent second reviewer checked the norm limit, exact Hermite scalar, all lambda and L factors, zero Fourier mode, the crucial dual low-output estimate, graph-tail bound and high-low Hilbert–Schmidt sum. No blocking error was found using the existing v1.14 inputs. The sharp-tail proof was separately checked for Binet constants, physical prime degree, full-length shift, pole scale, first-slot convention and even-sector phase. The scalar interval calculation was rerun independently with the same result.

An alternative first-order Hermite-quasimode route was explored but not completed, because the stronger direct proof made it unnecessary. It is recorded only as an abandoned backup in the adverse report, not as an additional result. A LaTeX escape typo was corrected during review. These are internal checks, not external peer review or a formal proof-assistant verification.

### Integration, validation and next concrete step

The full abstract, status, Section 20 proofs and G2 calibration, Section 32 goals and appendix are consistent. New material is on pages 65–68 and 73–76; the scalar certificate summary is on 118. All 123 pages were rendered and visually reviewed, with close inspection of new proof pages and the final bibliography. The final build has 392 unique labels and no warnings, unresolved references, overfull or underfull boxes. The 72 historical ledger rows are unchanged apart from version headings. The cumulative bundle preserves all prior certificates and adds the current derivations, proof inserts, adverse/independent reviews, scalar script and output, and reproduction guide.

**Next task:** construct a verified inverse-action approximation Z for the lambda=3,|n|<=256 head (even 257 and odd 256 dimensions) and its infinite complement, retaining the full residual Gram R*R. Derive a directional omitted-mode Gram bound from the exact divided-difference entries, using Fourier moment cancellations near the source directions rather than a scalar norm penalty. A finite certificate at one window would still need extension to lower errors tending to zero along unbounded windows for G2. Do not assume a fixed spectral gap, extrapolate finite eigenvalue signs, or omit the corrected sampler graph defect. The alternative arithmetic shell sign at p=2 and the metric/Lyapunov route remain open.

