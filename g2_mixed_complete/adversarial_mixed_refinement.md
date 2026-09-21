# Complete mixed terms and a monotone corrected head metric

These are exact analytic statements for the already certified fixed-window tail. They do not certify the low Schur sign. Adjoints have their usual coordinate meaning with the manuscript's first-slot-linear convention; real parts of paired cross terms are unchanged.

## 1. Setup and the complete mixed-vector remainder

In the inner decomposition let

\[
 T=\begin{pmatrix}K_0&B^*\\B&U\end{pmatrix},\quad
 D\preceq U\preceq mD,\quad D\succeq\gamma I>0,
\]

and retain the finite solve Z, residual R=B-UZ, trial head K_Z, and old certificate

\[
 C(K_Z-R^*D^{-1}R)C^*\succeq\mu I,\qquad\mu>0.
\]

Put

\[
 A=D^{-1/2}UD^{-1/2},\quad H=A-I,\quad
 F=D^{-1/2}RC^*,\quad y=D^{-1/2}k,
 \quad a_0=C(h-Z^*k).
\]

Here A is the bounded operator of the preconditioned closed form, with I<=A<=mI. Write Q_1=D^(-1/2)(I-H/m)D^(-1/2). The complete mixed vector is

\[
 b_1=a_0-F^*(I-H/m)y.
\]

Take an orthogonal Fourier prefix P past the support of Z, Q=I-P, and abbreviate p=Py, q=Qy, F_p=PF and F_q=QF. Its computed finite-prefix version is

\[
 b_J=a_0-F_p^*(I-H_{PP}/m)p.
\]

The exact omitted difference is

\[
 b_1-b_J=
 m^{-1}F_p^*H_{PQ}q+
 m^{-1}F_q^*H_{QP}p-
 F_q^*(I-H_{QQ}/m)q.
 \tag{1}
\]

Thus both omitted input q and the output H_QP p matter. Merely bounding q does not remove the second term.

Suppose

\[
 QHQ\preceq\nu Q,\quad \|q\|^2\le E,
 \quad F_q^*F_q\preceq E_F,\quad\|E_F\|\le\rho,
 \quad a=\langle Hp,p\rangle,
 \quad\|F_p^*H_{PP}F_p\|\le\eta.
\]

Then

\[
 \boxed{\|b_1-b_J\|\le
 \frac{\sqrt{\nu\eta E}+\sqrt{\nu a\rho}}m+
 \sqrt{\rho E}.}
 \tag{2}
\]

Proof: positive-semidefinite Cauchy bounds the first term of (1) by sqrt(nu eta E)/m. It also gives `||QHp||^2<=nu a`, bounding the second term by sqrt(nu a rho)/m. Since 0<=I-H_QQ/m<=I, the third term has norm at most sqrt(rho E). All these statements concern bounded H.

For a single head test vector z, replace eta by
`eta_z=<H P Fz,P Fz>` and rho by a certified
`rho_z>=||QFz||^2`. Formula (2) then bounds
`|<b_1-b_J,z>|`; no normalization of z is needed. This costs only one scalar probe action and one remote moment column and can be far sharper than a trace bound on the entire F tail.

## 2. The corrected head metric and monotonicity

Let P_j(A) be any positive bounded upper inverses satisfying

\[
 A^{-1}\preceq P_{j+1}(A)\preceq P_j(A)\preceq I.
\]

The geometric inverse polynomials are one such sequence. Set

\[
 M_j=\mu I+F^*(I-P_j(A))F,
 \quad b_j=a_0-F^*P_j(A)y,
\]

and define

\[
 \mathcal E_j=
 \langle P_j(A)y,y\rangle+
 \langle M_j^{-1}b_j,b_j\rangle.
 \tag{3}
\]

Then

\[
 \boxed{\langle T^{-1}(h,k),(h,k)\rangle
       \le\mathcal E_{j+1}\le\mathcal E_j.}
 \tag{4}
\]

For the first polynomial, the improved metric is exactly

\[
 M_1=\mu I+F^*HF/m.
 \tag{5}
\]

This is an additional certified positive contribution to the head metric; it is not an assumption about the missing Schur sign.

**Proof and domains.** The two-sided form order implies
`D(U^(1/2))=D(D^(1/2))`. Use the original triangular change of variables `(x,w-Zx)`, followed by x=C*xi and w=D^(-1/2)zeta. The latter sends the entire auxiliary Hilbert space onto the tail form domain. The old certificate gives the bounded block lower form

\[
 L(A)=\begin{pmatrix}
 \mu I+F^*F&F^*\\F&A
 \end{pmatrix}
\]

for the transformed complete form. The transformed right-hand side is exactly (a_0,y). This lower block is strictly positive: its head Schur matrix is `mu I+F*(I-A^-1)F>=mu I`. Define

\[
 L_j=\begin{pmatrix}
 \mu I+F^*F&F^*\\F&P_j(A)^{-1}
 \end{pmatrix}.
\]

Because `m^-1 I<=P_j(A)<=I`, every inverse is bounded. Moreover
`L_j<=L_{j+1}<=L(A)` and all blocks are bounded below by the common strictly positive L_0 obtained with P_0=I. Inverse order proves (4). Exact block inversion of L_j gives (3), with head Schur matrix M_j. This proves that updating both b_j and M_j preserves monotonicity; freezing the old scalar head metric need not preserve it.

If P_j converges in norm to A^-1, then L_j converges in norm to L(A), and E_j decreases to the corresponding inverse quadratic form of L(A). That limiting upper bound need not equal the true inverse quadratic form of T: slack in the original certified head lower bound remains. Convergence of the inverse polynomials therefore does not guarantee a final low Schur sign.

The same proof applies with any already certified positive head matrix M_0 in place of mu I, using `M_j=M_0+F*(I-P_j)F`. None of the argument changes the physical endpoint, Fourier cut, operator domain, or signed arithmetic matrix.

## 3. Rigorous finite probes for the positive head improvement

For the first polynomial, take finite-prefix probe columns V, and suppose their exact H-Gram matrix

\[
 G=V^*HV
\]

is positive definite. Define the complete pairing B_H=V*HF. Orthogonal projection onto the span of H^(1/2)V gives

\[
 F^*HF\succeq B_H^*G^{-1}B_H.
 \tag{6}
\]

The pairings in B_H must include the omitted rows. If V=PV, compute

\[
 B_J=V^*HPF,\qquad
 B_H-B_J=V^*HQF.
\]

Positive-semidefinite Cauchy and QHQ<=nu Q give

\[
 (QHV)^*(QHV)\preceq\nu G.
\]

Consequently the omitted pairing satisfies the matrix bound

\[
 (B_H-B_J)^*G^{-1}(B_H-B_J)
       \preceq\nu F_q^*F_q\preceq\nu E_F.
 \tag{7}
\]

Indeed `||QHV G^-1/2||^2<=nu`, so its adjoint composed with QF has exactly the bound (7). This contains no head-dimension or Gram-conditioning factor.

For every fixed 0<theta<1, the lower Young inequality and (6)-(7) now prove

\[
 \boxed{F^*HF\succeq
 (1-\theta)B_J^*G^{-1}B_J
 -(\theta^{-1}-1)\nu E_F.}
 \tag{8}
\]

Hence a rigorous lower matrix for M_1 is

\[
 \underline M_1=\mu I+
 \frac{1-\theta}{m}B_J^*G^{-1}B_J
 -\frac{(\theta^{-1}-1)\nu}{m}E_F.
 \tag{9}
\]

If only E_F<=rho I is retained, positivity is automatic whenever

\[
 \mu-\frac{(\theta^{-1}-1)\nu\rho}{m}>0.
\]

The remaining positive term is a finite-rank Gram and can be inverted using finite matrix operations. Keeping the actual E_F instead of rho I can improve the enclosure further, but positivity of the resulting lower metric must still be certified. Do not take the positive part of the indefinite lower bound (8); adding mu I and checking (9) is the valid route.

For a higher polynomial, the same probe lemma applies to the positive operator I-P_j(A). However, a finite-prefix power of the compressed A is not automatically the compression of the full power. Higher powers can leave the prefix and return. Their probe Grams and pairings require a complete remote enclosure before (6) can be used. The first-polynomial H-Gram of finite probes has no such hidden intermediate excursion.

## 4. A directional lower test for failure of the refined bound

Failure of an upper enclosure does not prove that the underlying refined bound is too large. A lower certificate can make that distinction. For any frozen head vector z, metric duality gives

\[
 \langle M_1^{-1}b_1,b_1\rangle
 \ge2\Re\langle b_1,z\rangle-\mu\|z\|^2
      -\langle HFz,Fz\rangle/m.
\]

Let epsilon_z be the directional version of (2), let
`eta_z=<H P Fz,P Fz>`, and let `rho_z>=||QFz||^2`.
Then

\[
 \langle HFz,Fz\rangle
 \le(\sqrt{\eta_z}+\sqrt{\nu\rho_z})^2.
\]

If ell_far is any rigorous lower bound for the complete first-polynomial far energy, it follows that

\[
 \mathcal E_1\ge\ell_{\rm far}
 +2\Re\langle b_J,z\rangle-2\epsilon_z
 -\mu\|z\|^2
 -\frac{(\sqrt{\eta_z}+\sqrt{\nu\rho_z})^2}{m}.
 \tag{10}
\]

One may take
`ell_far=V-(sqrt(a)+sqrt(nu E))^2/m`, or use a sharper positive-contraction lower bound. A trial z suggested by the finite metric solve should be frozen before interval verification. Equation (10) needs only one additional directional probe, not the whole matrix F*HF. If its lower bound exceeds K_X in the selected direction, the complete first-polynomial certificate fails there. This still does not imply a negative Weil direction or failure of the limiting true inverse correction.

## 5. Sharper far lower bound by optimizing the omitted norm

When nu<m, positivity gives, for x=||q||,

\[
 \langle Hy,y\rangle
 \le a+2\sqrt{a\nu}\,x+\nu x^2.
\]

Since ||y||^2=v+x^2 exactly,

\[
 \begin{aligned}
 \langle(I-H/m)y,y\rangle
 &\ge v-a/m-2\sqrt{a\nu}\,x/m+(1-\nu/m)x^2\\
 &\ge \boxed{v-a/(m-\nu)}.
 \end{aligned}
 \tag{11}
\]

The second inequality is completion of the scalar square, with minimizer x=sqrt(a nu)/(m-nu). If the certified x<=sqrt(E) is retained, minimize at the smaller of sqrt(E) and that minimizer. Thus (11) is valid even without an omitted-norm estimate.

Combining (11) with a directional lower bound for ||b_1||^2/mu can prove that the complete first-polynomial **scalar-mu** upper majorant exceeds K_X. Such a conclusion is an exact failure diagnosis for that majorant, not for the smaller corrected-head quantity (3). The latter uses M_1 rather than mu I and may still improve the outcome.

## 6. Code review of the mixed prefix and complete error bound

Read `mixed_refinement.py` after the finite-prefix calculation. The source action includes the zero-mode coupling separately with the correct sqrt(2) factor. Its h/k split is at the inner N=512. The helper `pair_R(w)` applies the shifted matrix to a vector vanishing on the inner head, then contracts with the finite graph matrix and C; this gives exactly C R* w for the finite-prefix input w. The first-polynomial prefix q uses the correct diagonal factors in D^-1(U-D)D^-1 k.

The complete F metric bound is also legitimate: the old certificate implies
`F*F <= C K_Z C* - mu I`. That right side is positive semidefinite, so either its trace or a certified absolute row-sum bound controls ||F||^2. The script uses this to bound eta in (2) by `(m-1)||F||^2`, retaining both omitted input and omitted output errors. No unsafe floating minimum enters the norm choice; each available bound is independently valid. The displayed higher-polynomial iterations are powers of the finite compression, and the script correctly labels them as finite diagnostics rather than complete-tail certificates.

No blocking index, adjoint, shift, or norm-bound defect was found in this implementation. Any claim that a scalar-mu majorant is intrinsically too large must use a complete lower bound such as (11) plus the complete mixed lower, not only the finite-prefix total.

## Current scope

The finite-prefix scalar-mu total reported by the parent exceeds the available trial energy. That observation alone is not a complete-tail failure certificate, and the improved head metric in (5) may lower the total. The present note supplies rigorous ways to enclose the remaining remote terms and the metric improvement. No full low-head sign or G2 conclusion has been proved here.
