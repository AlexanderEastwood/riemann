# Adversarial assessment: one source, many near-null modes, and the endpoint

20 September 2026. Research assessment against complete manuscript v1.13; no manuscript edits. All assertions below are either proved elementary statements or explicitly limited proposals. No G2 sign estimate or RH proof is obtained.

## Main finding

The two-mode source may still approximate a unique ground state. Nothing below disproves that conjecture. However, neither a uniformly positive absolute complement gap, generic positivity-improving geometry, nor arithmetic estimates stable under a fixed error in one prime coefficient can prove the desired uniform result. There is a concrete infinite family of competing near-null sources, and the one-vector certificate is unusually sensitive to high-energy contamination. The appropriate fallback is a signed Schur complement for a growing source block, together with a separate directional endpoint estimate.

## 1. An explicit infinite family of actual near-null sources

Use the physical Fourier transform with kernel exp(-2 pi i x xi), and the manuscript's logarithmic transform

\[
H_g(s)=\int_{\mathbb R}g(y)e^{-(s-1/2)y}\,dy.
\]

Set

\[
h(x)=x^2(2\pi x^2-3)e^{-\pi x^2},\qquad
g(y)=e^{y/2}\sum_{n\ge1}h(ne^y).
\]

Direct Gaussian differentiation gives Fourier(h)=h. Also h(0)=0 and integral_R h=0. Poisson summation therefore gives g(-y)=g(y). For y>=0 every summand is positive, since ne^y>=1 and 2 pi-3>0. Hence g is strictly positive everywhere. It and all its derivatives have double-exponential tails.

Writing M h(z)=integral_0^infinity h(x)x^(z-1) dx, direct gamma integration gives

\[
Mh(z)=\frac{z(z-1)}{4\pi}\pi^{-z/2}\Gamma(z/2).
\]

For Re(s)<0, absolute summation permits the change of variable x=ne^y, and then analytic continuation gives

\[
H_g(s)=\zeta(1-s)Mh(1-s)=\frac{\xi(s)}{2\pi},
\quad
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The sign and factor 2 pi here use the manuscript's negative exponential transform. Consequently every function g_j=D_y^(2j)g satisfies

\[
H_{g_j}(s)=(s-\tfrac12)^{2j}\xi(s)/(2\pi).
\]

These functions are linearly independent: an identically vanishing finite linear combination would give a polynomial times the nonzero entire function xi equal to zero. Every transform vanishes at every nontrivial zeta zero, without assuming RH or simple zeros. This is an explicit instance of the classical co-Poisson radical; the general radical mechanism is already established in [Connes–Consani, *Spectral triples and zeta-cycles*, Section 3](https://ems.press/content/serial-article-files/44477). It is not a claim of a new discovery of that radical.

There is a useful quantitative implication for the compact problem. Choose a smooth even cutoff chi_a supported in [-a,a], equal to one on [-a+1,a-1], with derivatives uniformly bounded, and put f_(j,a)=chi_a g_j. For each fixed m and fixed integration-by-parts order k, the tail transforms satisfy, uniformly over 0<=Re(s)<=1,

\[
|H_{f_{j,a}}(s)-H_{g_j}(s)|
\le T_{m,k}(a)(1+|\Im s|)^{-k},\quad j<m,
\]

where, for suitable fixed constants C,M depending on m,k,

\[
T_{m,k}(a)\le C e^{Ma}\exp[-\pi e^{2(a-1)}].
\]

Proof: derivatives of g_j on y>=0 are bounded by a polynomial in e^y times exp(-pi e^(2y)); evenness handles y<0. Multiply by exp(-(sigma-1/2)y), whose growth is at most exp(|y|/2), and integrate by parts k times. The cutoff derivative terms are in the same tail region. At a nontrivial zero rho the whole transform H_(g_j)(rho) vanishes. The zero-side form and the unconditional zero-counting bound therefore give, for k=2,

\[
|QW(f_{j,a},f_{l,a})|\le C_0T_{m,2}(a)^2.
\]

This uses the absolutely convergent sum of (1+|Im rho|)^(-4), with multiplicities. It does not posit a globally positive closed form. The L2 Gram matrices converge to the positive-definite Gram matrix of g_0,...,g_(m-1). Thus their m-dimensional spans have absolute Rayleigh quotients tending to zero uniformly on the unit sphere.

**Consequence.** For any fixed-rank family R_a of rank r, use m=r+1. Dimension alone supplies a unit vector in span{f_(j,a):j<m} intersect R_a-perp, whose Rayleigh quotient tends to zero. Consequently a uniform estimate

\[
QW|_{R_a^\perp}\ge cI,\qquad c>0\text{ fixed},
\]

is impossible. In a compact-resolvent realization, min–max also gives lambda_(m-1)(a)<=o(1) for every fixed m. These are upper bounds, not positivity or eigenvalue asymptotics. They prove no rank~lambda^2 assertion and do not identify the exact PSWF source with a ground state. Fixed-index prolate modes can still have distinct polynomial leakage factors multiplying a common exponential scale.

## 2. Any fixed upward error in one arithmetic weight eventually destroys positivity

Let f_a=chi_a g from the preceding construction, with chi_a nonnegative. Fix an integer m>=2 at which an arithmetic coefficient is perturbed, and put

\[
A_m(f)=\int_{\mathbb R}f(y+\log m)\overline{f(y)}\,dy.
\]

The signed prime term in the manuscript is -2 Lambda(m)m^(-1/2) Re A_m(f). Increase just this coefficient by epsilon>0, leaving the rest of the form unchanged. Then exactly

\[
QW_\epsilon(f_a)=QW(f_a)-2\epsilon m^{-1/2}A_m(f_a).
\]

Here QW(f_a)->0 by Section 1, whereas A_m(f_a)->A_m(g)>0 by L2 translation continuity and strict positivity of g. Therefore QW_epsilon(f_a)<0 for all sufficiently large a. The modified arithmetic form is indefinite, irrespective of RH.

This is an adversarial perturbation of the coefficient data, not a statement that the true prime coefficients are wrong. It rules out any proposed uniform positivity argument that remains valid under fixed sign-indifferent error bars on that coefficient. Finite interval arithmetic is unaffected when it resolves the exact constants sufficiently sharply. The actual positivity problem still requires the signed arithmetic cancellation.

## 3. The exact contamination threshold for the one-vector certificate

Let W have eigenvalues lambda_0<=lambda_1<=..., and let u=sum a_j phi_j be a unit candidate. Write alpha=<Wu,u>, C=P_(u-perp) W P_(u-perp), and A=C-alpha I as in Section 20. Interlacing gives lambda_min(C)<=lambda_1. Thus A>0 requires alpha<lambda_1, or equivalently

\[
\sum_{j\ge2}(\lambda_j-\lambda_1)|a_j|^2
< (\lambda_1-\lambda_0)|a_0|^2.
\]

This is only a necessary condition, but it identifies the right failure diagnostic: measure the candidate's energy contamination above the first excited level against the lowest gap. Small L2 angle alone is inadequate when that gap collapses. Enlarging N improves Fourier representation while also introducing further directions in which this comparison must hold. The result is fully consistent with the manuscript's existing three-dimensional counterexample and strengthens its diagnostic interpretation.

Near-null source blocks by themselves also cannot exclude an orthogonal negative direction. The elementary direct sum diag(-1,epsilon_1,...,epsilon_m,1), with epsilon_j->0, makes this explicit. This is a logical countermodel, not a model of the actual Weil matrix.

## 4. Endpoint accuracy is a directional resolvent condition

Assume the manuscript's finite certificate A>0 and write t=alpha-lambda_0>=0 and r=P_(u-perp)Wu. With the ground vector's overlap normalized to one, the exact eigenvector equation gives

\[
\frac{\phi_0}{\langle\phi_0,u\rangle}
=u-z_t,\qquad z_t=(A+tI)^{-1}r.
\]

The first-slot-linear convention makes the displayed overlap the correct coefficient. Therefore the projective endpoint discrepancy is exactly

\[
\frac{|\delta_N z_t|}{|\delta_Nu|}.
\]

The norm certificate only supplies

\[
|\delta_Nz_t|\le\sqrt{(2N+1)/L}\,\|A^{-1}r\|.
\]

For the normalized physical source, the denominator is approximately |B_lambda|/||p_lambda|| once endpoint projection is separately justified. Since |B_lambda| is exponentially small, an ordinary angle estimate need not be useful here. A sufficient norm criterion would require q=o(|B_lambda|sqrt(L/(2N+1))/||p_lambda||). The sharper target is the actual signed scalar resolvent pairing, uniformly for 0<=t<=E. This is additional to, and distinct from, the Fourier truncation's endpoint error already certified in v1.13.

## 5. A positive ground state does not force real Fourier zeros

One tempting extra assumption is that a positive kernel or Perron-type theorem supplies all missing ground-state structure. A simple countermodel limits that argument. For b=4, set

\[
v(y)=e^{-y^2}+\tfrac14 e^{-(y-b)^2}+\tfrac14 e^{-(y+b)^2}>0.
\]

Its Fourier transform is sqrt(pi) exp(-t^2/4)[1+(1/2)cos(bt)]. It has simple nonreal zeros

\[
t=((2k+1)\pi\pm i\operatorname{arcosh}2)/b.
\]

The positive rank-one kernel v(y)v(z) is positivity improving, and I-P_v has v as its unique ground state, with spectral gap one. On sufficiently large finite intervals, restrict v and use the same rank-one construction. The simple nonreal Fourier zeros persist by locally uniform convergence and Rouche's theorem. Thus even a strictly positive, simple, even ground state does not by itself imply the real-zero property. The special Weil/de Branges structural theorem and its hypotheses cannot be replaced by generic Perron reasoning.

## 6. A more robust signed block target

For an orthogonal decomposition into a source block and its complement, write

\[
W=\begin{pmatrix}F&B^*\\B&C\end{pmatrix},\qquad C\ge cI>0.
\]

The exact Schur complement is K=F-B^*C^(-1)B. For any trial inverse action Z with columns in D(C), let R=B-CZ. Direct expansion gives

\[
K=F-B^*Z-Z^*B+Z^*CZ-R^*C^{-1}R
\succeq F-B^*Z-Z^*B+Z^*CZ-(\|R\|^2/c)I.
\]

If this lower bound is >=-epsilon I, completion of squares gives W>=-epsilon I. No simplicity or internal spectral separation of the source cluster is needed. This is an elementary sufficient criterion, not a proved bound for the arithmetic matrix.

The immediate proposed experiment is to retain several actual repaired prolate sources, orthonormalize with a certified Gram matrix, and inspect the signed effective block instead of fitting a single eigenvector. A negative two-by-two determinant already falsifies block positivity; positive diagonals alone do not establish it. For a proof, the complement coercivity and the inverse-action residual must be certified on the same finite/infinite object and scale.

## 7. Audit of the parent's explicit high-frequency complement argument

The proposed diagonal-plus-bounded representation passes the sign and constant checks. For H_nm=1/(n-m), H is skew-adjoint and has norm pi, so [M_b,H] is bounded self-adjoint. The archimedean sine series has its first term bounded by one and all remaining terms bounded, by decreasing integral comparison, by pi/4. Thus the stated bound on b_n is valid.

For a=min(1,L), the lower bound on w(y)=2rho(y)(1-y/L) follows from sinh y<=y e^y, hence 2rho(y)>=e^(-y/2)/y>=1/y-1/2. This gives w(y)>=1/y-1/2-1/L on (0,a), and therefore

\[
-A_n\ge\log(2\pi|n|a/L)-A_0-2-a-2a/L.
\]

The centered pole operator is 2|cosh(y/2)><cosh(y/2)|-2|sinh(y/2)><sinh(y/2)|. Its negative eigenvalue has magnitude 2 sinh(L/2)-L. The full prime operator has norm at most 2P_lambda, and the archimedean off-diagonal norm is at most 2+pi/2. Combining these yields the parent's displayed tail constant without a sign discrepancy. The logarithmically growing diagonal plus bounded perturbation also gives the explicit operator domain and finite-sequence core.

The physical closed Weil form must still be identified using the cited trigonometric form-core theorem; the matrix argument alone identifies its own unique closure. This high-frequency estimate can certify the distant complement, but supplies no sign for the remaining Schur block.

## Recommended falsification gate

Test the endpoint-directed resolvent pairing and the signed multi-source Schur matrix at the same endpoint-adequate cutoff. Reject any argument that substitutes a fixed positive complement gap, unsigned prime errors, or a small ordinary eigenvector angle for those two quantities. None of the present adverse results closes G2; they narrow what a successful proof would have to control.

## Additional audit: proposed polynomial endpoint recovery

I reviewed `endpoint_derivation.md` after the preceding assessment was complete. The proposed asymptotic bound for the literal repaired source at N=ceil(lambda^8(1+L)) passed internal analytic review, with the scope below. In particular:

- The auxiliary entire sum has the asserted normalization, bandwidth O(c), and measure variation O(lambda^3). Its lower-tail L2 estimate does not presume pointwise cancellation.
- Taylor degree A c, with a sufficiently large fixed A, controls all derivatives j<=ceil(c); the Markov and Stirling-number steps have constants uniform in this growing range. The resulting lambda^(4j) factor is conservative.
- The strict lower trace subtracts m>=lambda^2, including equality, while the inversion-even periodic source has no zeroth-order endpoint jump.
- The largest integer below lambda^2 must be removed before estimating the function-jump sine tails. The uniform O(1/lambda) allowance for that single jump handles arbitrarily close arithmetic thresholds.
- With r=ceil(c), the analytic-piece remainder has logarithm at most -6c log(lambda)+O(c)+O(log(lambda)), and is smaller than every power of lambda. The fixed smooth repair is correctly excluded from this growing-order analytic argument and restored through the projection's Lebesgue bound.

The proof should cite the already established endpoint-normalized radial bound, explicitly retain the uniform-in-j product/logarithmic derivative estimates, and state that the cutoff constant and asymptotic threshold are not numerical. This source Fourier endpoint result alone does not imply the endpoint-directed source-to-ground resolvent bound in Section 4 above, a weighted growing-band G1 estimate, or G2. It advances a genuine prerequisite without resolving the spectral sign problem.

### Separately audited coefficient-tail and weak-G1 addendum

The subsequent coefficient-tail claim also passed internal review:

\[
|\widehat p_\lambda(n)|\le C|B_\lambda|\lambda\sqrt L/|n|,
\qquad |n|>N_\lambda.
\]

The jump expansion bounds the raw-source coefficients by C|Bplus|/sqrt(L) times [lambda/|t_n|+lambda^7/|t_n|^2], plus the analytic remainder. The latter two terms are absorbed by the first at the stated cutoff, and their relative bounds decrease thereafter. For the exact compact repair, the direct variation calculation gives O(|h_circle(0)|sqrt(lambda)); its coefficient bound is therefore O(|h_circle(0)|sqrt(lambda L)/|n|), exponentially smaller than the displayed target.

I checked the existing weighted-sampler proof in the complete manuscript. Substituting this coefficient estimate for its raw-BV estimate gives, for the literal projection and every ambient K>=N=N_lambda,

\[
\frac{|QW_\lambda((P_N-I)p_\lambda,D_{\log}x)|}{|B_\lambda|}
\le C_R\|x\|_{\mathcal H_{R,L}}\lambda^2
\left[\frac LN+\left(\frac LN\right)^{R-1}(1+\log(2N))\right],
\quad R>3.
\]

The off-diagonal double sum is absolutely convergent. The diagonal is separately controlled by the existing correct logarithmic bound. The old K>=2N condition was needed for the filtered vector's support; K>=N suffices for P_N. In the fixed first-slot-linear convention, self-adjointness of the finite logarithmic derivative gives exactly <D_log W_(lambda,K)k,x>=QW_lambda(k,D_log x). The new operator-core statement independently justifies Fourier graph convergence at fixed lambda. Combining this independently checked coefficient estimate with the existing continuum weak-G1 bound supports weak G1 along the polynomial cutoff. It does not supply an unweighted residual norm, growing-prolate-block uniformity, the source-to-ground endpoint estimate, a positive signed Schur block, or G2.

The actual operator insertion has one minor wording correction: before using decreasing integral comparison for the archimedean sine series, discard the factor 1-exp(-(2k+1/2)L)<=1. The original summands need not themselves decrease; the resulting majorant does. The stated bound and constants are unchanged. The cited CCM Propositions 3.2–3.4 were checked against the primary source and do supply the physical logarithmic identification, closed lower-bounded form, and trigonometric form core.
