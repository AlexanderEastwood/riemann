# G2 continuation: primary-source audit and a form-core reduction

Alexander Eastwood working manuscript, v1.13 starting point. Research date: September 20, 2026.

## Result

The source audit does not supply the missing large-window arithmetic ordering or approximation theorem. It does support a useful reduction: **the continuum real-zero argument needs a trigonometric form core, not a separately proved operator core**, once the canonical semibounded closed Weil form and its simple isolated even ground state are specified. The latter spectral hypothesis remains open at general windows. A self-contained proof and its exact rate are below.

There is also a direct finite consequence of the existing v1.12–v1.13 certificate: the Fourier transform of the **actual** certified finite ground vector has only real zeros, and that vector's physical endpoint is nonzero. These assertions concern the exact ground vector, not the repaired source or its close rational approximation. No endpoint comparison, growing-window theorem, G2, or RH follows from them.

## Primary-source check

* **CCM, November 27, 2025, v1.** Proposition 3.4 gives the trigonometric form core, and Theorem 3.6 gives the canonical semilocal operator's discrete lower-bounded spectrum. Theorem 5.10 requires a simple even finite ground state. Section 8 explicitly leaves large-window ground-state ordering and sufficiently strong approximation by the prolate/co-Poisson candidate unresolved. Lemma 7.3 supplies strip convergence for their specified source candidate, not identification with the ground eigenfunction. [Connes–Consani–Moscovici, *Zeta Spectral Triples*](https://arxiv.org/html/2511.22755v1).
* **CvS, November 28, 2025, v1.** Theorem 5.6 proves real-zero localization for the transform arising from a real symmetric divided-difference matrix with a one-dimensional even lowest eigenspace. Theorem 6.1 states an essential-self-adjointness/core hypothesis for the continuum version. Its finite-to-continuum argument uses Rayleigh approximation, min–max and Fourier continuity; the direct form-core argument below makes clear which hypotheses actually suffice. [Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*](https://arxiv.org/html/2511.23257v1).
* **Suzuki, August 17, 2026, v2.** Theorems 1.1–1.4 establish the canonical realization, continuity of the lowest eigenvalue, and simple even positive ground states for sufficiently small windows. Small-window positivity does not give large-window ordering. The self-adjoint differential extensions use a shift strictly below the actual lowest eigenvalue; that construction cannot supply an independent proof that the unshifted Weil form is positive. [Suzuki, *Weil's quadratic form via the screw function*](https://arxiv.org/html/2606.09096v2).
* **Zhu, September 2, 2026, v2.** Theorems 1.1 and 6.2 provide a finite reduction and reported certified full-window ordering at half-width 0.8. Theorem 1.4 bounds the cost of its pointwise prime-comb envelope method. This controls the whole window, unlike positivity of one Fourier section. Its large-window upper-bound theorem assumes RH; its empirical Landau–Widom law is not a proved uniform asymptotic. The released certificates were not rerun here. [Zhu, *Weil positivity in compact windows*](https://arxiv.org/html/2608.24827v2).
* **Kim et al., July 29, 2026, v2.** This additional numerical paper does not provide the missing theorem. Its claimed archimedean spectral law is explicitly classified as a symbol-level heuristic in Section 3.1, and its FEM/Richardson results are not an omitted-complement certificate. No large-window positivity or source-identification assertion is imported. [*A Numerical Realization of Suzuki's Weil-Quadratic-Form Operator*](https://arxiv.org/pdf/2607.24830v2).

The audit found no primary theorem proving that the actual semilocal Weil ground state converges, in the required normalized complex-strip topology, to the repaired prolate/co-Poisson source. This is a search finding, not a claim to have exhausted all literature.

## A self-contained form-core theorem

### Stronger operator-core route checked during collaboration

The parent analysis identifies the exact all-index matrix as W=D_d+[M_b,H], where d_n=W_nn, b is real and bounded, and H_nm=1/(n−m) off the diagonal, H_nn=0. The discrete Hilbert transform satisfies ||H||≤π and H*=−H. Consequently [M_b,H] is bounded self-adjoint with norm at most 2π||b||∞. Once the actual entry formulas establish b∈ℓ∞ and d_n=log|n|+O_L(1), the consequences are unconditional at each fixed L:

* D_d+[M_b,H] is self-adjoint on D(D_d), and finite sequences form an operator core, by the bounded perturbation argument.
* Its operator domain is {x: Σlog²(2+|n|)|x_n|²<∞}; its closed form domain is {x: Σlog(2+|n|)|x_n|²<∞}.
* It is the canonical semilocal Weil operator: both closed forms agree on all finite Fourier sums, and that subspace is a form core for both. Uniqueness of form closure prevents a different boundary realization from entering silently.

Thus this exact matrix decomposition proves the operator-core condition itself, rather than merely bypassing it. CCM's form-core theorem applies to its actual zero-extension/distribution convention, so no additional endpoint condition is required to identify these two forms. This concerns the semilocal Weil operator only; it does not establish the closed arithmetic generator/domain realization in Section 18. The proof below remains useful because it separately displays the fixed-window Ritz rate and the assumptions still needed for simple even ordering.

Use a first-slot-linear inner product. Fix one interval length L>0. Work on H=L²([0,L]), translating to [-L/2,L/2] only when taking the entire Fourier transform. Let q be a densely defined closed Hermitian form bounded below. Assume:

1. Reflection Rf(x)=f(L-x) and conjugation preserve the form domain and commute with the form.
2. The nested trigonometric spaces E_N=span{L^(-1/2)exp(2πinx/L): |n|≤N} lie in the form domain, and their union is a form core.
3. The canonical self-adjoint operator A associated with q has a simple ground eigenvalue λ0, with unit real even eigenfunction u. There is a gap g>0 such that q[h]≥(λ0+g)||h||² on the form-domain vectors perpendicular to u.
4. Each matrix W_N representing q on E_N has the exact divided-difference/rank-two structure

   [D_N,W_N]=β_N η_N*−η_N β_N*,

   where D_N e_n=n e_n, η_N=Σe_n is even and β_N is real odd. Here x y* means v↦〈v,y〉x.

Let λ_N be the smallest eigenvalue of W_N. Then λ_N decreases to λ0. For all sufficiently large N, λ_N is simple and its unit real eigenvector u_N is even. After sign alignment,

\[
 \|u_N-u\|_2^2\le \frac{2(\lambda_N-\lambda_0)}g.
\]

Each sufficiently large N has an entire centered Fourier transform with only real zeros. The same is true of the nonzero transform of u. No essential-self-adjointness assertion about the operator restricted to the trigonometric polynomials is required.

### Proof of the Ritz statements

Choose b such that q_b=q+b〈·,·〉 is positive definite. Form-core density gives p_j∈∪E_N with ||p_j−u||²+q_b[p_j−u]→0. Thus ||p_j||→1 and q[p_j]/||p_j||²→λ0. The lower variational bound λ_N≥λ0 and nesting give λ_N↓λ0.

For large N, λ_N<λ0+g. The subspace E_N∩u⊥ has codimension at most one and q≥λ0+g there. The finite min–max principle therefore gives λ_2(W_N)≥λ0+g, so λ_N is simple. Reflection commutes with W_N. Hence its simple ground vector has parity +1 or −1. Odd parity would make it perpendicular to the even u, forcing λ_N≥λ0+g, a contradiction. Reality follows by choosing a real eigenvector of the real matrix.

Write u_N=c_Nu+h_N, h_N⊥u, c_N≥0. The form eigenrelation q(u,h_N)=λ0〈u,h_N〉=0 gives

\[
 \lambda_N=q[u_N]\ge\lambda_0+g\|h_N\|_2^2.
\]

Since c_N=√(1−||h_N||²),

\[
 \|u_N-u\|_2^2=2(1-c_N)
 \le2\|h_N\|_2^2
 \le2(\lambda_N-\lambda_0)/g.
\]

Only form-domain vectors and the canonical form eigenrelation were used. Compact resolvent is a convenient sufficient source of the gap when the lowest eigenvalue is simple; the explicit gap assumption suffices for this proof.

### Direct finite endpoint and real-zero argument

Set Q_N=W_N−λ_NI. It is positive semidefinite with kernel span{u_N}. Suppose η_N(u_N)=0. Applying the commutator to the even u_N gives

\[
 Q_ND_Nu_N=-\beta_N\eta_N(u_N)=0,
\]

because 〈u_N,β_N〉=0. Therefore D_Nu_N lies in span{u_N}. But D_Nu_N is odd and u_N is even, so D_Nu_N=0. The zero eigenspace of D_N is span{e_0}, where η_N is nonzero, a contradiction. Thus the physical endpoint δ_N(u_N)=η_N(u_N)/√L is nonzero. This gives existence, not a cutoff-uniform lower bound.

Normalize k_N=u_N/η_N(u_N), so η_N(k_N)=1, and put

\[
 T_N=D_N-(D_Nk_N)\eta_N^*.
\]

The preceding identity and the commutator give Q_N T_N=T_N* Q_N. Also T_N k_N=0. Thus T_N induces a self-adjoint operator on E_N/span{k_N}, in the positive inner product induced by Q_N. Its eigenvalues are real, and the remaining eigenvalue on span{k_N} is zero. The rank-one determinant identity then shows that all roots of

\[
 P_N(z)=\sum_{n=-N}^N k_{N,n}\prod_{j\ne n}(j-z)
\]

are real. Indeed det(T_N−zI) is, up to a nonzero constant sign, z P_N(z), and P_N has degree 2N because Σk_{N,n}=1.

For the centered function associated with the uncentered Fourier coefficients k_{N,n}, direct integration yields

\[
 \widehat{k_N^{\rm c}}(z)
 =\frac{2\sin(Lz/2)}{\sqrt L}
   \sum_{n=-N}^N\frac{k_{N,n}}{z-2\pi n/L}.
\]

All apparent poles are removable. Away from the real Fourier nodes its zeros are the scaled real roots of P_N, and any zeros at Fourier nodes are also real. Thus the entire transform has only real zeros. The transform convention with positive exponential gives the same conclusion after z↦−z. The argument reproduces the finite rank-two mechanism directly; it does not require Q_N itself to be the unshifted Weil form or λ_N≥0.

### Fixed-window continuum passage

For |Im z|≤T, Cauchy–Schwarz gives

\[
 |\widehat{u_N^{\rm c}}(z)-\widehat{u^{\rm c}}(z)|
 \le\sqrt L e^{LT/2}\|u_N-u\|_2
 \le\sqrt{\frac{2L(\lambda_N-\lambda_0)}g}\,e^{LT/2}.
\]

At fixed L, this tends to zero uniformly on each closed horizontal strip, hence locally uniformly in C. The limit is not identically zero, by Fourier injectivity and ||u||=1. Hurwitz on each nonreal half-plane shows that the limit has no nonreal zero.

For the actual canonical semilocal Weil form, CCM's cited form-core and lower-semibounded closed-form statements supply hypotheses 1–2, and the exact finite matrix supplies hypothesis 4. General-window simplicity and evenness in hypothesis 3 remain unproved. This conclusion does not assert that every self-adjoint extension of an informal distributional kernel is the same operator; the closed form is fixed throughout.

## Consequence of the existing λ=3, N=64 certificate

The earlier certificate establishes a simple even lowest eigenvalue for the actual 129-dimensional W. Its exact rank-two identity is part of the manuscript. The finite argument above therefore establishes, without any further floating-point calculation:

* the exact finite ground vector's physical endpoint is nonzero;
* its entire centered transform has only real zeros;
* subtraction of the true finite lowest eigenvalue yields the positive quotient metric required by the finite construction.

These statements do not make the exact projected source the ground vector. The certified angle bound compares the two, but an ordinary-norm angle bound does not transfer real-zero localization or relative endpoint accuracy to the source.

An optional quantitative endpoint consequence, using the same exact finite objects, is

\[
 |\eta_N(u_N)|
 =\frac{\|Q_ND_Nu_N\|}{\|\beta_N\|}
 \ge\frac{g_{\rm odd}\|D_Nu_N\|}{\|\beta_N\|}
\]

when β_N≠0 and g_odd is a proved positive lower bound for Q_N on the odd sector. If β_N=0 the identity instead forces u_N to be the zero mode. With D_log=(2π/L)D_N and b_N=(2π/L)β_N, the physical version is |δ_N(u_N)|≥g_odd||D_log u_N||/(√L||b_N||). This is exact scale bookkeeping, not an asserted asymptotically useful lower bound.

## Why the growing-window task is still arithmetic

The above convergence holds with L fixed. Suppose one has an unbounded sequence L_j, exact source proxies p_j, and nonzero scalar normalizers c_j such that c_j hat p_j→Xi locally uniformly on the open critical strip. The sufficient ground-state identification requirement on every fixed substrip |Im z|≤T<1/2 is

\[
 |c_j|\sqrt{L_j}\,e^{L_jT/2}\|u_j-p_j\|_2\longrightarrow0.
\]

If the source is first projected into E_N, that error splits into source Fourier tail and projected-source/finite-ground error; a third finite-to-continuum error is needed if the target uses the continuum ground state. The rate established above controls this third term only after a **proved** lower bound for the continuum gap and an upper bound on the Ritz error λ_N−λ0. A finite positive matrix supplies no such lower bound for λ0: Ritz approximations approach it from above.

Physical endpoint normalization is not needed just to infer real zeros of the exact finite or continuum ground transform. It remains needed for the manuscript's specific boundary-normalized comparison and graph identities. The distinction avoids spending effort proving an unnecessary endpoint condition for one theorem while retaining the actual endpoint obligation where it enters G1/G2.

## A concrete omitted-complement cost at the current window

An independent diagnostic, computed here from the pointwise-envelope formula, uses a=log3 and

\[
 A_a=\sum_{n<9}\frac{2\Lambda(n)}{\sqrt n}
 =6.342597436087091\ldots,
 \qquad T_1=2\pi e^{A_a}=3570.548493101019\ldots.
\]

The n=9 endpoint correlation vanishes, so the strict inequality in this symbol is appropriate. The current Fourier edge is t_64=π·64/log3=183.0144555123281…, about 19.51 times smaller. These are double-precision scale calculations, not interval certificates. The pointwise-envelope route would involve a first discarded Legendre order on the scale e·a·T1/2≈5331, or roughly 2666 even modes before adding safety margin. This does not prove those dimensions necessary for other methods. It explains why the cited full-window method cannot be imported into our existing 129-dimensional certificate unchanged.

The desired improvement is a signed arithmetic or inverse-weighted complement estimate that retains prime/pole/archimedean cancellation. A bound derived by replacing the prime comb with its absolute total mass still pays the exponential-in-λ envelope threshold. The parent calculation of an explicit Fourier-index diagonal-minus-bounded-remainder inequality would add useful quantitative control at fixed windows, but by itself would not supply the tiny low-energy Schur margin or a large-window ground-state identification theorem.

## Adversarial conclusions and next gate

1. No argument here presumes positivity of the full growing-window Weil form.
2. The finite quotient is positive because one subtracts its actual lowest eigenvalue; this operation does not show that eigenvalue is nonnegative in other windows.
3. Simplicity and parity of Ritz minima are derived only after the continuum simple-even gap assumption. Finite simplicity at N=64 cannot be reversed into that assumption.
4. Form-core density proves convergence, not a usable convergence rate. The displayed rate exposes exactly the missing Ritz-error/gap ratio.
5. Endpoint nonvanishing is proved; endpoint stability under approximation is not. The source's 137.4%–137.5% projected endpoint error remains fully compatible with every result above.
6. A sharper uniform residual/correlation theorem must pass the prior nonzero-evaluator w=1/4 falsification gate before being treated as a G2 sign argument.

Next concrete obligation: combine the explicit omitted-Fourier-complement lower bound with a verified *signed* Schur-complement budget at the actual λ=3 window, proving that the continuum odd sector and second even level remain above one independently enclosed even Rayleigh quotient. This is smaller than proving RH, but genuinely upgrades the finite ground certificate to an entire-window statement if successful. The present research pass closes a form-core prerequisite and a finite structural consequence; it does not close that entire-window spectral gap, G2, or RH.
