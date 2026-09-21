# G2 finite Weil spectral pilot

Alexander Eastwood working-manuscript research record — September 20, 2026

The complete manuscript remains **v1.11 (105 pages)**. This experiment does not close G2 or prove RH. It supplies a sharper conditional finite-dimensional estimate and numerical evidence that the actual repaired source is close to a finite Weil ground state. It also demonstrates a substantial endpoint-accuracy cost that ordinary-norm agreement does not address. All computational results below are **non-certified**.

## Result and change of direction

The naive residual/gap estimate is an unsuitable practical diagnostic here. For the actual matrix at lambda=3, N=64, it is approximately 4.68e14, although the numerically computed source–ground angle has sine approximately 2.159e-4. Resolving the residual through the positive complementary block gives a much sharper conditional bound, approximately 2.159e-4 on the same example.

This improvement is elementary spectral algebra, not an independent arithmetic positivity theorem. In particular, positivity of the complementary block still has to be proved. High-precision computation suggests it in the finite examples; this run has not produced interval certificates or a uniform theorem.

The physical endpoint remains a separate obstruction. At lambda=3, ordinary Fourier projection at N=64 has about 137% relative endpoint error. An independent finite-polynomial moment calculation gives about 10.5% at N=4096. The latter is an endpoint-only computation: no 8193-dimensional Weil matrix was assembled. These cutoffs are exploratory choices, not replacements for the manuscript's deterministic asymptotic cutoffs.

## The exact finite object and source

Set L=2 log(lambda), a=L/2, and t_n=2 pi n/L. The real symmetric Weil matrix W acts on the orthonormal basis

\[
U_n(x)=L^{-1/2}e^{it_nx},\qquad x\in[0,L],\quad |n|\le N.
\]

The matrix retains all prime-power terms with m<=lambda^2, the pole contribution, the archimedean integral, and the separately computed correct logarithmic diagonal. It is not the off-diagonal divided-difference formula continued onto the diagonal.

The source is the paper's n=0,4 angular PSWF combination, with c=2 pi lambda^2 and physical normalization h_n(v)=lambda^(-1/2) psi_n(v/lambda). In computation the even angular differential operator is approximated in a normalized Legendre basis. The two coefficients are formed consistently from that same finite approximation:

\[
a_0=-\int_{-\lambda}^{\lambda}h_4(v)\,dv,
\qquad a_4=\int_{-\lambda}^{\lambda}h_0(v)\,dv,
\qquad h^\circ=a_0h_0+a_4h_4.
\]

These are the manuscript's -chi_4 h_4(0), chi_0 h_0(0). Thus the integral cancellation is algebraic within the finite Galerkin construction, rather than obtained by subtracting separately rounded concentration eigenvalues.

For a specific allowed fixed repair choose b=3/4,

\[
\phi(v)=\begin{cases}
\exp\{1-[1-(v/b)^2]^{-1}\},&|v|<b,\\
0,&|v|\ge b,
\end{cases}
\quad
C=\frac{\int\phi}{\int v^2\phi},\quad
\psi(v)=\phi(v)(1-Cv^2).
\]

Then psi is even, smooth, compactly supported inside (-1,1), has psi(0)=1 and integral zero. Set h_tilde=h_circle-h_circle(0) psi. All spectral calculations retain this correction. Its scalar moments are exact in the mathematical construction; quadrature and floating evaluation of them are not certified exact numbers.

On the logarithmic window form

\[
k(x)=e^{x/2}\sum_{m\ge1}\widetilde h(me^x),\qquad
p(x)=\tfrac12\{k(x)+k(-x)\},\quad -a\le x\le a.
\]

Integrating k against cos(t_n x) computes the Fourier coefficients of p. Conversion to the translated [0,L] basis includes **(-1)^n**. There is no additional Haar weight: du/u=dx, and sqrt(u) already occurs in the co-Poisson sum. Every source arithmetic cut and repair-support cut is a quadrature breakpoint. The normalized candidate is u=P_Np/||P_Np||.

The physical endpoint is the common one-sided trace. In particular,

\[
B_\lambda=\frac12\left\{
\sqrt\lambda\,\widetilde h(\lambda^-)
+\lambda^{-1/2}\sum_{1\le m<\lambda^2}\widetilde h(m/\lambda)
\right\}.
\]

For integer lambda^2 the strict inequality is essential. The finite endpoint functional remains delta_N(x)=L^(-1/2) sum x_n. No endpoint shell is inserted in this pilot. Consequently these computations do not estimate the graph defect of the manuscript's corrected sampler or authorize dropping any of its terms.

## A sharper conditional estimate, with proof

Let W be any finite Hermitian matrix, u a unit vector, P the orthogonal projection onto u-perp, and define

\[
\alpha=\langle Wu,u\rangle,\quad r=PWu,
\quad C=PWP|_{u^\perp},\quad A=C-\alpha I.
\]

Inner products are linear in the first slot. Assume **A>=gamma I with gamma>0**. Then W has a unique lowest eigenvalue lambda_0<=alpha. If theta is the angle between u and its ground-state line, define

\[
q=\|A^{-1}r\|,\qquad E=\langle A^{-1}r,r\rangle.
\]

The exact conditional estimates are

\[
\tan\theta\le q,\qquad
\sin\theta\le\frac{q}{\sqrt{1+q^2}},\qquad
\alpha-E\le\lambda_0\le\alpha.
\]

Proof: min–max gives lambda_0<=alpha and lambda_1>=lambda_min(C)>alpha. A ground vector has nonzero u-component; write it c u+h. Its complementary equation gives h=-c(C-lambda_0 I)^(-1)r. Put t=alpha-lambda_0>=0. The scalar equation is t=< (A+tI)^(-1)r,r>. Since A is positive, spectral calculus gives t<=E and ||(A+tI)^(-1)r||<=||A^(-1)r||. The latter comparison uses functions of the *same* self-adjoint A, not a generally invalid inference about vector norms from inverse ordering. Division by |c| proves the angle bounds. If W commutes with reflection and u is even, the unique ground state is even: an odd one would lie in u-perp and contradict the complement lower bound.

The usual bound ||r||/gamma discards the residual's spectral distribution. The inverse-weighted bound retains it. These estimates are conditional finite linear algebra, not a claim of a new spectral theorem or an arithmetic sign proof.

For a trial solve z, a useful rigorous a posteriori form is

\[
q\le\|z\|+\frac{\|r-Az\|}{\gamma}.
\]

If A_tilde,r_tilde approximate A,r with error bounds delta_A,delta_r, a certified gamma_tilde>delta_A gives

\[
q\le\|z\|+
\frac{\delta_r+\delta_A\|z\|+
\|\widetilde r-\widetilde A z\|}
{\widetilde\gamma-\delta_A}.
\]

Here gamma_tilde must itself be a certified lower bound for A_tilde, not a rounded eigenvalue. For fixed exact u and ||W-W_tilde||<=eta one may use delta_r=eta and delta_A=2eta. If the numerical candidate also approximates the true source, its error must be included separately. Certifying the fixed candidate and then adding a phase-aligned source distance tau to the projector-angle bound is usually less wasteful than dividing source error by the tiny gap. A conservative joint budget, after a unitary identification of the two complements, is delta=eta+2M tau with M>=||W_tilde||, delta_r=delta and delta_A=2delta.

Failure of gamma>0 rejects this sufficient certificate; it does not disprove convergence. For example W=diag(0,d,1) and u=sqrt(1-tau^2)e_0+tau e_2, with 0<d<tau^2, have source–ground angle tending to zero as tau tends to zero, while alpha=tau^2 and gamma<=d-tau^2<0.

## Numerical results

The primary refined calculation uses 105 decimal digits, 70 even Legendre modes, and 224-point Gauss–Legendre integration on each smooth source piece and on the matrix's archimedean integral. Both parity sectors are included in the complementary spectral minimum. The N=64 refinement uses 320 quadrature points and decomposes the matrix into its two exact reflection sectors.

| lambda | N | gamma | Ordinary residual/gap | Schur q | Computed sin(theta) |
|---:|---:|---:|---:|---:|---:|
| 2 | 32 | 5.42280e-10 | 5.53598e2 | 0.00121100321 | 0.00121099977 |
| 2.5 | 32 | 9.74267e-21 | 4.55575e7 | 0.000514694790 | 0.000514694569 |
| 3 | 32 | 6.12223e-34 | 1.41142e14 | 0.000217848696 | 0.000217848671 |
| 3 | 64 | 1.31277e-34 | 4.67624e14 | 0.000215892094 | 0.000215892075 |

At lambda=3,N=64, alpha≈5.31238e-38 and the Schur expression alpha-E≈3.64339958e-38, compared with the computed lowest eigenvalue ≈3.64339966e-38. These positive numerical values do not certify positivity of the exact finite matrix or the continuum form. The complement minimum here comes from the odd sector; the residual is even. A same-parity minimum alone would miss the ordering requirement.

Small cutoffs can fail the sufficient test: at lambda=3,N=16, gamma≈-1.77130e-22, while the computed source–ground angle sine is approximately 0.016604. At N=32 gamma becomes positive. Neither observation proves anything uniform in lambda or in the required cofinal cutoff sequence.

### Precision and independent checks

- The initial double-precision matrix changed by about 4.2e-12 in observed operator norm when quadrature was refined. Its apparent positive and negative tiny eigenvalues at lambda=2.5 and 3 were below this diagnostic scale. They are discarded as sign evidence.
- Repeating the N=32 calculations at 80 digits/55 modes/160 quadrature points and at 105 digits/70 modes/224 points preserves the displayed spectral figures. The saved matrix entries agree at 70 significant digits. This is agreement at the export precision, not a zero error bound.
- Observed source coefficient-vector differences are approximately 9.17e-65, 1.91e-48 and 1.02e-36 for lambda=2,2.5,3 respectively. At lambda=3 the physical endpoint changes by about 1.68e-17 relatively under source refinement. No infinite Legendre-tail bound is supplied by these comparisons.
- Independent adaptive integration of the original correlation formula checks five diagonal and off-diagonal matrix entries at lambda=3. Discrepancies from the stored 70-digit entries are below 5e-72. This checks factors and signs without recycling the divided-difference assembly; it is still not interval certification.
- An independent adversarial agent checked the phase, Haar factors, source moments, strict endpoint convention, both parity sectors, the Schur proof, and the distinction between a failed certificate and failed convergence.

## Endpoint test by independent moments

For a finite Legendre source write h_circle(v)=sum_r d_r(v/lambda)^(2r), zero extended outside [-lambda,lambda]. Its un-repaired, symmetrized translated Fourier coefficient has the exact identity

\[
c_n=\frac1{\sqrt L}\operatorname{Re}\sum_r
\frac{d_r}{2r+\frac12+it_n}
\left\{
\sqrt\lambda\sum_{m\le\lambda^2}m^{-1/2-it_n}
-\lambda^{-4r-1/2}\sum_{m\le\lambda^2}m^{2r}
\right\}.
\]

To derive it, integrate each source summand over 1/lambda<=u<=lambda/m and integrate each monomial u^(2r+1/2+it_n) exactly. The translated phase cancels because lambda^(it_n)=(-1)^n. A summand with m=lambda^2 has zero integration length, so including it does not conflict with the strict one-sided endpoint trace.

Only this endpoint diagnostic omits the smooth repair in the coefficient calculation. The omission is explicitly bounded. Let H=||E(psi)||_(L1([-a,a])). Then

\[
|\delta_N(P_Np)-\delta_N(P_Np^\circ)|
\le |h^\circ(0)|\frac{2N+1}{L}H,
\qquad
H\le2\sqrt b\,\lfloor b\lambda\rfloor(1+Cb^2).
\]

This follows from the Dirichlet-kernel bound |D_N|<=2N+1; inversion symmetrization does not increase the L1 norm. The displayed H majorant bounds the number of nonzero terms, |psi|, and the integral of sqrt(u) du/u. These are exact inequalities for the defined source; their numerical inputs are not interval-enclosed.

At lambda=3, a 140-digit evaluation gives B≈5.58669542e-19 and h_circle(0)≈2.61009508e-39. The omitted repair's relative endpoint-bound formula evaluates to less than 4.5e-16 even at N=4096. Thus it cannot explain the endpoint errors in the table.

| N | Relative endpoint error at lambda=3 |
|---:|---:|
| 32 | 1.14022 |
| 64 | 1.37454 |
| 128 | 1.63677 |
| 256 | 1.38933 |
| 512 | 0.798989 |
| 1024 | 0.412764 |
| 2048 | 0.208431 |
| 4096 | 0.104617 |

The low moment coefficients agree with the repaired quadrature coefficients to within 4.8e-40, smaller than the conservative omitted-repair coefficient bound of 4.5e-38. This is a normalization cross-check, not a certified true-PSWF error estimate. The apparent eventual 1/N behavior is numerical evidence only; no asymptotic is inferred from this table.

The endpoint norm on the finite space is exactly sqrt((2N+1)/L). Consequently an ordinary candidate–ground distance d gives only an absolute endpoint error <=sqrt((2N+1)/L)d; division by the exponentially small B can make this useless. The existing shell repair can recover the endpoint algebraically, but introduces its already documented derivative and graph terms. This experiment supplies no justification for discarding them.

Likewise, on |Im z|<=T the transform of an L2 difference supported on [-a,a] is bounded by sqrt(2a) exp(aT) times that difference norm. Any scalar normalization toward Xi multiplies this cost. Numerical ordinary-norm agreement at four finite pairs does not establish the required full-strip, normalized convergence.

## What remains open and the next concrete test

The sharper finite estimate is proved conditionally. The experiment is encouraging for a **weighted complementary-resolvent estimate**, rather than an unweighted residual divided by the smallest spectral gap. It does not discharge any G2 arithmetic sign assumption.

The next finite task is to certify one case, preferably lambda=3,N=64, using operator-norm enclosures for the prime/pole/archimedean matrix and a lower bound on the complementary block, together with an error-controlled linear solve. Certify a fixed numerical candidate first; then account separately for the true source's Galerkin and coefficient errors. More floating-point repetitions cannot replace those bounds.

The subsequent proof target is uniform control of ||(C-alpha)^(-1)r||, with independently proved spectral ordering, along a valid growing-window/growing-cutoff sequence. That still requires signed arithmetic information. The omitted Fourier complement, closed-form/operator domain, physical endpoint normalization and complex-strip transform error remain separate obligations. The small finite matrices do not establish the sign of the full closed form, a transported positive metric, or a small Lyapunov defect.

The alternative individual-evaluator shell route still needs its independent signed estimate at p=2. The all-parameter evaluator obstruction from the preceding research record remains in force. Weak G1 and every centered-sampler graph-defect formula remain unchanged.

## Reproduction and file status

Requirements: Python, numpy, scipy, mpmath. Run in this order:

```text
python check_g2_spectral.py
python check_g2_spectral_mp.py
python check_g2_spectral_wide.py
python check_g2_endpoint_moments.py
python audit_g2_spectral.py
```

JSON outputs preserve the settings, numerical results and refined N=32 matrix/source entries. This record, the scripts, outputs and updated research log are included in the cumulative reproducibility bundle. The complete v1.11 LaTeX/PDF pair is unchanged: exploratory numerical findings and a conditional linear-algebra refinement do not justify upgrading its theorem status or issuing a new manuscript version.
