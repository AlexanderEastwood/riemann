# G2: deep research and adversarial assessment

Alexander Eastwood working manuscript — research assessment, September 20, 2026

## Conclusion

The strongest outcome is a correction to the proposed research strategy, not a proof of G2. The two Sonine support conditions, nested evaluation and the Riesz minimum-norm characterization hold for evaluators at every spectral parameter. At the ordinary point w=1/4 they produce the strictly negative normalized shell limit 1−sqrt(2). Thus these geometric ingredients cannot independently establish the desired sign.

The arithmetic source equation distinguishes zeros from nonzeros, but on a Riesz evaluator it does so by reproducing exactly a factor of zeta(w). A new arithmetic inequality is still required. The adversarial analysis below rules out several attempts to obtain that inequality from symmetry or generic positivity alone.

My recommended next experiment is a **gap-relative ground-state identification test on the actual finite Weil form**. Measure the explicit source's full residual against a certified lower bound on the rest of the spectrum, and then include the amplification required for complex-strip convergence. This is a concrete go/no-go test, not a claim that the ratio is small. A continuous-kernel representation is a useful independent way of assembling and auditing the same form, not a new source of positivity.

No G2 sign gap was closed. Weak G1 retains its fixed-band/Sobolev scope. The complete manuscript remains v1.11; speculative results have not been inserted into its proofs.

## 1. Scope and conventions

The starting documents were the current complete v1.11 LaTeX manuscript and its current research log. Relevant parts were Sections 2–9, 18–20 and the prior failed-metric checkpoints. Primary-source research covered evaluator geometry, canonical systems, classical positivity counterexamples, finite Weil ground states, continuous-kernel formulations and recent certification methods. Relevant theorem statements and proof steps were inspected; this is not an independent verification of every proof or computational certificate in those papers.

The Hermitian product is first-slot linear. Retain

\[
v_w^R=k_{\bar w}^R,\qquad
\langle f,v_w^R\rangle=Mf(\bar w),\qquad
D_pf(x)=p^{-1/2}f(x/p).
\]

Here H_R is the ambient double-support Sonine space, W_R is the closed co-Poisson source space, and Q_R=H_R\ominus W_R. The arithmetic adjoint \(\mathscr A\) is the distributional limit of

\[
\mathscr A_My(t)=\sum_{n\le M}\frac{y(t/n)}n
                  -\int_{t/M}^{\infty}\frac{y(x)}x\,dx.
\]

The integral counterterm is indispensable. None of this changes the physical endpoint, logarithmic diagonal, Fourier cutoff or centered sampler's endpoint-shell graph defect. The integer M is not the Fourier cutoff K.

## 2. What the literature actually supplies

The following are scoped source summaries; subsequent calculations are our own checks and deductions, not claims attributed to the papers.

| Primary source | Relevant result and boundary of applicability |
|---|---|
| [Burnol, *Sur certains espaces de Hilbert…*, 2001, Proposition 2.2](https://arxiv.org/pdf/math/0105120) | Completed Mellin evaluation is continuous at all complex parameters in the ambient Sonine space. This supports the all-parameter hostile test below. It does not single out arithmetic zero evaluators by a positivity condition. |
| [Burnol, *On some bound and scattering states associated with the cosine kernel*, 2008, Sections 2–4](https://arxiv.org/pdf/0801.0530v2) | Explicit reproducing kernels, Dirac-type systems and self-adjoint spectral models exist for cosine-kernel spaces. Matching the asymptotic density of zeta zeros is not identification of the actual zeros. |
| [Conrey–Li, *A Note on Some Positivity Conditions Related to Zeta and L-Functions*, IMRN 2000, Sections 3–4](https://aimath.org/~kaur/publications/41.pdf) | Specific proposed de Branges shift-positivity conditions fail for the zeta-associated spaces. Equation (3.4) gives a negative real xi-ratio at height 282; Section 4 also records a nonnumerical argument supplied by Sarnak. This is a warning against overstrong positivity, not a disproof of de Branges methods generally. |
| [Suzuki, *A canonical system of differential equations arising from the Riemann zeta-function*, revision September 23, 2016, Theorems 2.2–2.3](https://arxiv.org/pdf/1204.1827v2) | Innerness has explicit equivalent conditions. The stated canonical-system construction is proved for omega>1; the critical smaller-shift range cannot simply inherit the same unconditional conclusion. A positive canonical-system representation is a hypothesis to earn, not an automatic consequence of the functional equation. |
| [Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, 2020 preprint / 2021 publication](https://arxiv.org/pdf/2006.13771) | A Sonin-trace/prolate comparison proves restricted-support archimedean positivity. The support restrictions that exclude prime contributions are essential; this does not prove the growing-prime G2 estimate. |
| [Connes–Consani–Moscovici, *Zeta Spectral Triples*, November 27, 2025, Theorem 5.10 and Section 8](https://arxiv.org/pdf/2511.22755v1) | The finite self-adjoint construction requires its stated simple/even ground-state and boundary normalization hypotheses. The paper explicitly leaves ground-state identification and sufficient approximation by the prolate-based candidate unresolved. Numerical spectral agreement is not the needed convergence theorem. |
| [Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, Theorem 6.1](https://arxiv.org/pdf/2511.23257v1) | A precisely defined distributional form with the required core/essential-self-adjointness and simple isolated even ground state yields a ground-state Fourier transform with only real zeros. Remark 4.3 warns that the distribution-at-the-boundary convention matters. The theorem cannot be imported using only an informal convolution kernel. |
| [Suzuki, *Weil's quadratic form via the screw function*, arXiv v2, revised August 17, 2026, Theorems 1.1, 1.3–1.5](https://arxiv.org/html/2606.09096v2) | The paper gives a continuous-kernel/Friedrichs formulation, continuity of the lowest eigenvalue, and positive/simple/even ground state for sufficiently small windows. Shifted positive Hilbert spaces yield self-adjoint extensions. The proposed arithmetic limiting identification remains conjectural. These are useful analytic tools, not an unconditional growing-window sign theorem. |
| [Groskin, *A finite Guinand–Weil dictionary and archimedean tail order…*, revision August 14, 2026, Theorem 3.2 / Corollary 3.3](https://arxiv.org/pdf/2607.02828v3) | For the specified finite frequency matrix, the omitted archimedean tail has positive order and an explicit norm budget. A negative value within that budget is inconclusive. This controls an integration cutoff, not all omitted Fourier modes and not a Lyapunov commutator. Its released certificates were not rerun here. |
| [Zhu, *Weil positivity in compact windows…*, arXiv v2, revised September 2, 2026, Theorems 1.1–1.4](https://arxiv.org/pdf/2608.24827v2) | This recent preprint reports a certified lower bound for support [-0.8,0.8], including parity-sector separation, and a doubly exponential cost barrier for its pointwise-envelope method. Its reported tiny variational upper bounds do not themselves prove positivity at larger windows. The certificates were not independently rerun; the empirical decay law and RH-conditional result must not be treated as unconditional asymptotics. |

Versions are pinned where available. The author of the last item is taken from the current v2 PDF/metadata, not an inconsistent search snippet.

Two cautions from the source audit deserve special emphasis:

* Suzuki's 2026 conjectural limit involves a meromorphic xi-ratio. Before using a Hurwitz argument we must specify pole-free domains and holomorphic, nonvanishing normalizers. Ordinary locally uniform convergence of entire functions on all of C cannot have a genuine pole in its finite-valued limit. No limiting corollary is being adopted here without that audit.
* Real zeros of finite approximating functions do not force the target's zeros to be real unless a nonzero holomorphic limit is justified in the required complex domain. Real-axis agreement alone is insufficient.

## 3. Exact adversarial result: the all-parameter evaluator test

This calculation uses the manuscript's ambient evaluator foundations, not RH or a zero list. Fix w in the open critical strip, off the critical line. Both identities

\[
S_Rv_w^{pR}=v_w^R,\qquad
S_RD_pv_w^{pR}=p^{1/2-w}v_w^R
\]

hold whether or not zeta(w)=0. To check the second, for f in H_R use D_(1/p)f in H_(pR):

\[
\begin{aligned}
\langle f,S_RD_pv_w^{pR}\rangle
 &=\langle D_{1/p}f,v_w^{pR}\rangle\\
 &=p^{1/2-\bar w}Mf(\bar w)
 =\langle f,p^{1/2-w}v_w^R\rangle.
\end{aligned}
\]

Consequently the exact ambient difference is

\[
\|S_Rv_w^{pR}\|^2-\|S_RD_pv_w^{pR}\|^2
 =(1-p^{1-2\Re w})\|v_w^R\|^2.
\]

The Fredholm shell calculation and elementary normalization bounds of v1.10 need only support, reflection and nested nonzero evaluation, and thus apply here too. With q_R=Iv_w^(pR), d=|Re w−1/2|, they give

\[
\frac{\int_{1/R}^{p/R}|q_R|^2-
             \int_{1/(pR)}^{1/R}|\mathcal F_+q_R|^2}
     {\|v_w^R\|^2}
 =1-p^{1-2\Re w}+O_{w,p}(R^{2d-1}).
\]

At w=1/4 and p=2, the limit is 1−sqrt(2)<0. These are actual ambient Sonine evaluators with both supports and their minimum-norm property. They are not arbitrary functions chosen to evade those constraints.

This falsifies source-independent variational positivity, **not G2**: zeta(1/4) is nonzero. More generally, for real 0<w<1, the alternating eta series is positive while 1−2^(1−w)<0, so zeta(w)<0.

### What arithmetic orthogonality adds—and what it does not

For phi in V_R, Mellin integration by parts and the first-slot convention yield

\[
\begin{aligned}
\langle\mathcal D\phi,\mathscr A v_w^R\rangle
 &=\langle E\mathcal D\phi,v_w^R\rangle\\
 &=c_0(\bar w)\zeta(\bar w)\bar w(\bar w-1)
     \int\phi(t)t^{\bar w-1}\,dt.
\end{aligned}
\]

Since \(\mathcal D=(t^2\partial_t)'\) is formally self-adjoint,

\[
\boxed{\mathscr A v_w^R(t)
 =c_0(w)\zeta(w)t^{w-1}+a_{w,R}+b_{w,R}/t}
\]

as distributions on (1/R,R). The constants are not assumed zero. In the open strip w(w−1)c_0(w) is nonzero, so

\[
v_w^R\in Q_R\quad\Longleftrightarrow\quad\zeta(w)=0.
\]

Thus the homogeneous adjoint equation on an evaluator is exactly zero incidence. This does not rule out proving a new inequality from arithmetic orthogonality; it identifies why simply combining the equation with the Riesz characterization is not already such a proof.

**Mandatory falsification gate:** apply every proposed shell-sign derivation to w=1/4. Identify the exact step at which the nonzero arithmetic forcing blocks the conclusion. That step must be a proved quantitative estimate, not division by zeta or assumed spectral positivity.

## 4. Wild assumptions tested by the adversarial agent

### A. Reflection and positive multi-prime averaging

Let w#=1−conjugate(w), d=Re w−1/2 and N_R=||v_w^R||². The antiunitary obtained from conjugation and G maps the evaluator to its reflected partner, preserving its norm. Summing their exact defect diagonals gives

\[
[2-p^{2d}-p^{-2d}]N_R=-(p^d-p^{-d})^2N_R.
\]

It is negative off the line. Any nontrivial nonnegative finite weighting over primes preserves that sign. This concerns diagonal sums, not the norm of a superposition, where cross terms remain. A signed or genuinely cross-prime construction is a different, unproved proposal.

### B. An invariant indefinite metric can coexist with growth

For d nonzero and gamma real, set

\[
B=\operatorname{diag}(d+i\gamma,-d+i\gamma),\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Then B*J+JB=0; conjugation followed by J reflects B to −B. All prime exponentials commute and preserve J. But J has one negative direction. For every positive definite G, testing on a B-eigenvector proves

\[
\frac{\|B^*G+GB\|}{\lambda_{\min}(G)}\ge2|d|.
\]

Scalar repair G_c=cI+J, c>1, gives ratio 2|d|c/(c−1), not zero. Squaring J gives I and ratio 2|d|. Symmetry and positive-metric construction cannot alone eliminate the growing branch.

### C. A positive completion has a quantitative cost

For K_z=[[0,z],[conjugate(z),0]], every positive semidefinite P obeys

\[
\|P-K_z\|\ge |z|.
\]

Use the negative unit eigenvector of K_z; equality is attained by P=K_z+|z|I. Thus a nonzero off-diagonal defect with zero diagonal cannot be made positive by an arbitrarily small correction. This is a finite-model diagnostic for full-Pick-matrix proposals, not a negative result about the individual-evaluator target.

### D. Orthogonal quotients do not inherit the de Branges division axiom

Use the finite de Branges model E(z)=(z+i)^3 with polynomial vectors of degree at most two and norm

\[
\|f\|^2=\int_{\mathbb R}\frac{|f(x)|^2}{(1+x^2)^3}\,dx.
\]

Let W=span{z²+1} and Q=H\ominus W. Evaluators at i and −i are nonzero and in Q. For f=a+bz+cz² one has

\[
\langle f,z^2+1\rangle=\frac\pi2(a+c).
\]

The vector f=1−z²+(5i/2)z=−(z−2i)(z−i/2) lies in Q. Its ambient norm-preserving Blaschke transform

\[
\frac{z+2i}{z-2i}f(z)=-z^2-(3i/2)z-1
\]

does not: its source pairing is −pi. Both norms squared are 41pi/32. Positive ambient geometry, conjugation and source orthogonality therefore do not imply quotient division stability. This is not a model of the actual co-Poisson source; any application there needs its own compatibility theorem.

### E. An absolute residual is not ground-state identification

The matrices W_s=s[[0,1],[1,1]] with u=(1,0) have residual s→0 and comparison gap s→0, but the ground-state angle does not improve: its sine is approximately 0.5257311121 for every s>0. Worse, u=(0,1) is an exact eigenvector of diag(−1,0), with zero residual, but is not the ground state. An ordering estimate is indispensable.

## 5. A precise, testable ground-state certificate

The following is elementary finite-dimensional spectral algebra, not a new RH theorem. Let W=W* be the **actual** finite Weil matrix in an orthonormal basis and u a unit candidate source. Set

\[
\alpha=\langle Wu,u\rangle,\quad r=(W-\alpha I)u,\quad
\varepsilon=\|r\|,\quad
C=P_{u^\perp}WP_{u^\perp}|_{u^\perp}.
\]

The proposed missing estimate is

\[
C\succeq(\alpha+\gamma)I,\qquad\gamma>0,
\]

with control of epsilon/gamma at growing scales. If it holds, min–max gives exactly one ground eigenvalue lambda_0≤alpha and all other eigenvalues ≥alpha+gamma. Splitting a ground eigenvector as c u+h gives

\[
h=-c(C-\lambda_0 I)^{-1}r.
\]

Since C−lambda_0 I≥gamma I, the scalar Schur equation gives

\[
\alpha-\frac{\varepsilon^2}{\gamma}\le\lambda_0\le\alpha,
\qquad
\sin\angle(u,\xi_0)\le\frac{\varepsilon}{\gamma}.
\]

If W commutes with reflection and u is exactly even, its simple ground state is even: an odd ground state would be orthogonal to u and contradict the complement bound. This does not require lambda_0≥0. It does require checking the parity of our actual repaired source; silent symmetrization would change the object and demand new endpoint and transfer checks.

For a fixed, exactly normalized u and an approximation W_tilde with ||W−W_tilde||≤eta, safe bounds are

\[
\varepsilon\le\widetilde\varepsilon+\eta,\qquad
\gamma\ge\widetilde\gamma-2\eta.
\]

Thus the certified diagnostic is

\[
\frac{\widetilde\varepsilon+\eta}
     {\widetilde\gamma-2\eta},\qquad
\widetilde\gamma>2\eta.
\]

This identifies a concrete estimate that weak G1 does not supply: full residual smallness relative to arithmetic spectral separation. If the candidate is only an approximate low-energy vector in a collapsing cluster, its small absolute residual proves little.

### The complex-strip cost cannot be omitted

For functions supported in [−a,a], with transform \(\widehat f(z)=\int f(x)e^{izx}dx\), Cauchy–Schwarz gives

\[
|\widehat f(z)-\widehat g(z)|
 \le\sqrt{2a}\,e^{a|\Im z|}\|f-g\|_2.
\]

After phase alignment of unit ground state and unit candidate,
\(\|\xi_0-u\|\le\sqrt2\,\varepsilon/\gamma\).
If an independently justified scalar c_a normalizes the candidate toward Xi, a sufficient error budget on |Im z|≤T is therefore

\[
|c_a|\sqrt{4a}\,e^{aT}\frac{\varepsilon}{\gamma}\longrightarrow0.
\]

For zero exclusion inside the critical strip, each fixed T<1/2 is the relevant requirement. The candidate's own locally uniform transform limit, source repairs, endpoint normalization and finite-to-continuum passage must also be proved. This displayed bound is sufficient, not necessary: a sharper direct weighted transform estimate might replace it.

For the finite CCM boundary normalization, L2 closeness alone is not enough at growing dimension. The bound on the actual physical endpoint functional applied to the eigenvector error must be compared to its nonzero value on the candidate. Keep delta=L^(−1/2)eta_partial distinct from eta_B.

## 6. Prioritized next work

1. **Build two independently normalized assemblies of a feasible finite Weil matrix:** the current logarithmic-diagonal/prime/pole formula and, if its domain bookkeeping is verified, an integrated continuous-kernel formulation. Compare entries and quadratic values before interpreting spectra.
2. **Compute the gap certificate for the existing explicit source.** Record alpha, the full residual, even/odd complement lower bounds, physical endpoint and the normalization toward Xi. Do not replace the full residual with fixed-test G1 pairings.
3. **Certify all errors.** Separate archimedean integration tail, omitted Fourier modes, source approximation, numerical roundoff and any inverse conditioning. The positive tail result controls only its named cutoff. Matrix-free or GPU eigenvectors can propose candidates; rigorous lower bounds require validated arithmetic and analytic tails.
4. **Test growth, not one successful window.** Inspect epsilon/gamma and its complex-strip amplification across increasing scales. Feasible pilot cutoffs are diagnostics, not substitutes for the manuscript's much larger deterministic cutoff. If the ratio fails, record that failure and do not call more decimal precision progress.
5. **Only then choose the proof target.** If a stable relative bound is plausible, attempt an arithmetic lower bound for the orthogonal complement, possibly through a Schur complement retaining signed prime/pole/archimedean terms. If not, return to the individual shell criterion with a genuinely new arithmetic estimate that passes the w=1/4 gate.

The finite-core metric route remains available. It must keep the exact identity

\[
GB+B^*G=-iJ^*[D,S]J-J^*SY-Y^*SJ,
\quad Y=z^{\mathrm c}\eta_{\mathrm B}+\mathcal R.
\]

A positive omitted tail cannot simply be discarded from this expression: its commutator need not have a sign. Likewise, for approximations with bounds delta_G and delta_L, a valid relative certificate is

\[
\frac{\|\widetilde{GB+B^*G}\|+\delta_L}
     {\lambda_{\min}(\widetilde G)-\delta_G},
\quad\lambda_{\min}(\widetilde G)>\delta_G.
\]

No independent estimate making either research ratio vanish has been obtained.

## 7. Checks performed and status labels

`checks/check_g2_adversarial.py` and its JSON output are reproducible supporting checks.

* **Exact rational algebra:** polynomial norm coefficients and source pairings in the quotient toy; indefinite-metric cancellation; an exact eigenvector that is not the ground state.
* **Floating-point illustrations, not certificates:** reflected negative squares and the spectral-gap examples.
* **Published counterexample reproduced numerically:** at 40 and 80 working digits, Re[xi(1+282i)/xi(2+282i)] agrees as −0.00013195729337208344071313530228861814. This supports a convention check against Conrey–Li, not a new numerical theorem.
* **Analytic derivations:** the all-parameter compression and arithmetic-forcing identities; the finite-model obstructions; the elementary gap and transform error budgets.
* **Not done in this pass:** no actual finite Weil matrix was assembled; no recent preprint's interval certificate was rerun; no growing-scale lower spectral bound was proved.

Bottom line: the research rules out some insufficient proof mechanisms and specifies a sharper next obligation. G2 and RH remain open. These conclusions concern the tested assumptions, not the impossibility of the overall program.
