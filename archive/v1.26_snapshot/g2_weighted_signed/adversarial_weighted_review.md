# Adversarial audit of the frequency-weighted signed target

21 September 2026. Starting manuscript: v1.19, freshly recovered complete source and research log in `current/`. No main-manuscript edits. The results below are exact functional-analytic consequences of the actual prime matrix and the already proved phase recurrence; no originality claim is made. They do not establish the growing-window sign.

## 1. The correct signed target and its ordinary-norm scaling

Fix a window and a Fourier tail on which the chosen archimedean diagonal D=diag(a_n) is strictly positive. The natural choice is a_n=-A_n, retaining the complete logarithmic diagonal and its constant. At fixed window a_n~log|n|. Write the actual restricted operator as W=D+R, with all prime, pole and archimedean off-diagonal terms in the bounded self-adjoint remainder R. Put

\[
 B=D^{-1/2}R D^{-1/2}.
\]

D^(-1/2) is bounded and compact, so B is compact and self-adjoint. For f in the closed form domain,

\[
 q_W(f,f)=\langle (I+B)D^{1/2}f,D^{1/2}f\rangle.
\]

The map D^(1/2) is a bijection from this form domain onto the tail Hilbert space, with inverse D^(-1/2). Thus positivity is equivalent to B>=-I, or ||B_-||<=1. An estimate ||B||<1 is only sufficient; a large positive eigenvalue of B is harmless for the desired sign. The real arithmetic matrix must be used before taking its negative spectral part. Separate unsigned bounds on prime, pole and archimedean pieces can lose the needed cancellation.

A significant normalization pitfall occurs when allowing an error. The bound B>=-(1+eta)I yields W>=-eta D, not W>=-eta I. If an independent signed bound R>=-C I is also available, then the two inequalities W>=-eta D and W>=D-C I combine to give

\[
 \boxed{W\succeq-\frac{\eta C}{1+\eta}I.}
\]

Multiply the first inequality by 1/(1+eta) and the second by eta/(1+eta) and add. The constant is sharp: the one-dimensional example D=C/(1+eta), R=-C has B=-(1+eta) and attains equality. Therefore eta_lambda tending to zero does not suffice for an ordinary growing-window lower error when C_lambda grows. The sufficient scalar conversion requires eta_lambda C_lambda tending to zero, or a sharper directional energy estimate. Taking C_lambda=lambda and eta_lambda=1/lambda gives a limiting negative ordinary value -1 despite eta_lambda tending to zero.

This exact reformulation does not prove the sign. A complete signed finite-section/tail certificate remains an independent arithmetic obligation.

## 2. Compact does not mean a finite Hilbert--Schmidt tail budget exists

Assume at least one active prime shift, equivalently lambda>sqrt(2). Let T=T_pr be the actual positive-coefficient prime translation sum on L2(0,L), L=2log(lambda). For the normalized physical Fourier basis its diagonal is

\[
 \tau_n=\langle T U_n,U_n\rangle
   =2\sum_{1<m<e^L}w_m\left(1-\frac{\log m}{L}\right)
               \cos\left(\frac{2\pi n\log m}{L}\right),
 \qquad w_m=\frac{\Lambda(m)}{\sqrt m}.
\]

Set c_m=w_m(1-log(m)/L)>0 for the nonzero terms and z_m=exp(2 pi i log(m)/L). Collect equal frequencies in

\[
 \tau_n=\sum_{z\in F}c_z z^n,
\]

where F contains the distinct z_m and their inverses. Every collected c_z is positive. Consequently

\[
 \lim_{X\to\infty}\frac1X\sum_{n=1}^X|\tau_n|^2
   =\sum_{z\in F}c_z^2=:\nu_\lambda>0.
\]

This is the finite geometric-series identity: different unit-circle frequencies have vanishing Cesaro cross average. No rational independence is needed. Since |tau_n|<=M_lambda:=sum_z c_z, there is a positive lower-density set of n on which |tau_n|>=sqrt(nu_lambda/2). For example, once the mean square is at least 3nu_lambda/4, the number of such indices up to X is at least nu_lambda X/(4 M_lambda^2).

Choose any positive diagonal a_n~log n on a fixed Fourier tail, and define the weighted prime operator

\[
 B_{\rm pr}=D^{-1/2}T D^{-1/2}.
\]

It is compact, but its diagonal is tau_n/a_n. For every p>=1,

\[
 \sum_n |\langle B_{\rm pr}U_n,U_n\rangle|^p=\infty,
\]

because the partial sum over the positive-density set is bounded below by a positive constant times X/(log X)^p. If B_pr belonged to the Schatten class S_p, convexity in its spectral measure would imply

\[
 \sum_n|\langle B_{\rm pr}U_n,U_n\rangle|^p
 \le\operatorname{Tr}|B_{\rm pr}|^p<\infty,
\]

a contradiction. Since S_p is contained in S_1 when 0<p<1, it belongs to no finite Schatten class at all. In particular its whole-tail Frobenius/Hilbert--Schmidt sum is infinite, regardless of the fixed starting Fourier cut.

For the natural exact arch diagonal a_n=-A_n, the complete signed B above has diagonal

\[
 B_{nn}=\frac{(\text{pole})_{nn}-\tau_n}{a_n}.
\]

The pole diagonal is O_lambda(n^-2), while the archimedean remainder has zero diagonal by this definition. Thus the same positive-density argument shows that this complete B is not in any finite Schatten class either. This last statement specifically uses the exact arch diagonal; a different reference diagonal that absorbs oscillatory prime entries needs a separate analysis.

There is no conflict with the manuscript's successful separated head-to-remote residual Grams. In those matrices n and m lie in disjoint ranges, the diagonal is absent, and the exact divided difference supplies decay 1/(n-m). With finitely many input columns their squared tail sums converge. The obstruction concerns a proposed Frobenius budget for the entire infinite-by-infinite weighted remainder.

## 3. Sharp fixed-window weighted-tail norm asymptotic

At each fixed lambda, let a_n>0 on a fixed tail and assume a_n/log|n| tends to one as |n| tends to infinity. Let Q_R remove |n|<=R. Then

\[
 \boxed{\lim_{R\to\infty}(\log R)
       \|Q_R D^{-1/2}T D^{-1/2}Q_R\|=\|T\|.}
\]

The factor log(R/L) is equivalent at this fixed window. The proof requires a stronger recurrence observation than merely an unbounded subsequence: every fixed neighborhood of the identity in the finite phase orbit has relatively dense return times.

To prove this, let z be the vector of all active phases and let G be the closure of its cyclic orbit in the finite torus. For any neighborhood U of the identity, the sets z^j U, j in the integers, cover G. A finite subcover uses indices j_1,...,j_s. For any integer r, z^r belongs to some z^(j_i)U, so r-j_i is a return time. Taking r=R+M+1+max_i j_i gives a return k in the interval [R+M+1,R+M+1+K], with K=max_i j_i-min_i j_i independent of R. The cyclic closure is a compact group; this also follows from the previously established return-to-identity sequence, which approximates inverse powers by positive powers. No effective bound on K uniform in lambda is asserted.

Now fix eta>0. By boundedness and self-adjointness of T, choose a unit finite Fourier polynomial f supported on |m|<=M with

\[
 |\langle Tf,f\rangle|>\|T\|-\eta.
\]

Choose U small enough that each return k in U satisfies ||M_k^* T M_k-T||<eta, using the exact finite phase estimate from v1.19. For each sufficiently large R choose such a k in the bounded-length interval just constructed. Put g_R=M_k f and x_R=D^(1/2)g_R. Their Fourier supports lie strictly beyond R, and

\[
 \|x_R\|^2=\sum_{|m|\le M}a_{k+m}|\widehat f(m)|^2
          =(1+o(1))\log R.
\]

The weighted Rayleigh numerator is exact:

\[
 \langle D^{-1/2}T D^{-1/2}x_R,x_R\rangle
     =\langle Tg_R,g_R\rangle.
\]

Its absolute value exceeds ||T||-2eta. This proves the lower limit after dividing by ||x_R||^2 and then letting eta decrease to zero. The upper limit follows immediately from

\[
 \|Q_R D^{-1/2}T D^{-1/2}Q_R\|
 \le\frac{\|T\|}{\inf_{|n|>R}a_n}
 =\frac{\|T\|}{(1+o(1))\log R}.
\]

The same leading constant survives any fixed compact subtraction before weighting. Indeed

\[
 (\log R)\|Q_R D^{-1/2}C D^{-1/2}Q_R\|
 \le\frac{\log R}{\inf_{|n|>R}a_n}\|Q_R C Q_R\|\to0
\]

for compact C. This includes the signed rank-two pole operator, bounded integral-kernel corrections, or a fixed finite-rank source removal applied to T before weighting.

**Quantifier limitation:** lambda is held fixed throughout this limit. The recurrence length K depends on lambda, the approximation tolerance, and the chosen norm-testing polynomial. The theorem supplies no bound for K as lambda grows. One must not combine this result with ||T_lambda||~lambda to infer a uniform lower bound lambda/log(R_lambda), nor an exponential cutoff obstruction for the simultaneous limit. Such a claim would need a quantitative recurrence bound on that same scale, which has not been proved. The finite-window statement does establish that the ordinary weighted-tail norm decays only logarithmically at each fixed window, and it prevents a falsely rapid generic remainder estimate.

## 4. Consequences for the proposed next computation

1. Test the lower spectrum of I+B; do not use a large harmless positive eigenvalue to reject Weil positivity. A certified norm-contraction failure rejects that sufficient method only.
2. Keep the exact signed finite arithmetic block. For a moderate finite block, use complete residual rows and the existing separated directional moment machinery for coupling to distant rows.
3. Do not estimate the whole infinite weighted remainder by a Hilbert--Schmidt tail. Its diagonal alone makes that sum divergent. A finite block coupling Gram remains legitimate.
4. A remote signed lower estimate is still needed. Bounding it only by ||T||/min(a_n) reproduces the scalar cutoff; a new frequency-sensitive arithmetic estimate must improve that step, not merely re-express it as a generic Birman--Schwinger theorem.
5. Convert dimensionless errors into ordinary form errors with the correct scale. An error eta_lambda on I+B is not automatically the error needed by the cofinal Weil criterion.

No growing-window sign has been proved here. The v1.18 zero continuum endpoint theorem and graph-trace obstruction are unchanged, and none of these frequency estimates removes the corrected sampler's explicit graph defect.

## 5. Audit addendum: the concrete lambda=4 signed-tail certificate

Reviewed `assembly_general.py`, `certify_weighted_tail.py`, and `certify_weighted_counterexample.py` as implemented during this run. The proposed signed inequality is W>=10^-8 D_arch on the **literal** Fourier tail |n|>16 in the selected parity sector. It is not positivity of the complete lambda=4 window, which also includes its low head and cross coupling.

The generalized assembly now uses the correct pole diagonal denominator `(den*den)` with den=L^2+16 pi^2 n^2. Earlier cache files without the `v2` marker arose before correction and are not valid evidence for this certificate. The current exact arch diagonal, prime-power enumeration, strict full-length cut, sine sequence, and uniform exponentially weighted arch series remainder match the manuscript formulas. The diagonal identity uses a_n=-A_n, including the complete logarithmic constant.

Subtracting c D_arch changes the diagonal to (1-c)a_n plus the actual prime/pole diagonal. It leaves every off-diagonal entry unchanged. Therefore the correct independent far-tail lower function is

\[
g(n)=(1-c)[\log(n/L)-E_L(t_n)]-\kappa,
\]

where kappa contains the unchanged off-diagonal arch loss, the actual weighted prime bound, and the negative pole/limiting-commutator losses in the odd case. The code implements exactly this. It retains the base cut N in those losses, all middle residual rows after subtracting c D_arch, the real even/odd normalization factors, and both remote signs in the moment Gram. The c_Mr sum includes unused indices 1 through 16, which only makes the bound more conservative. A positive lower bound for the exact arch diagonal at index 17 is separately checked through its increasing analytic lower function; this justifies calling D_arch positive on the whole literal tail.

The trial inverse Z is frozen to exact dyadic entries. The real inverse-Cholesky matrix is likewise used only as an exact dyadic congruence witness, not as a floating-point proof. If Y=C L_lower C^T has all interval Gershgorin row lower margins positive, the exact Y is positive definite. Since it is square, this also proves C invertible; alternatively the code now checks its exact lower-triangular shape and nonzero diagonal. Positive definiteness transfers by congruence to L_lower. The usual signed Schur identity with the independently positive entire far tail then proves the inequality for the closed form, including every omitted Fourier mode.

Two numerical-selection pitfalls identified in review were corrected before accepting the tightened verifier:

1. The weighted prime bound must take a maximum using exact upper-endpoint comparisons, not `key=float`. The current code also verifies that its selected upper endpoint dominates every candidate breakpoint enclosure.
2. The Gershgorin certificate must check **every** row margin as an interval. A float-selected smallest midpoint is not enough. The current code checks every row and reports the minimum of certified lower endpoints separately.

The prime breakpoint computation is rigorous: its active sets are decided at exact rational midpoints, and on each interval the chosen physical weight gives a ratio (A u+B)/(u+lambda), which is monotone or constant. Evaluating both one-sided endpoints therefore bounds the entire interval. All active shorter prime-power shifts are included.

The separate exact rational even vector on modes 17 through 256 has certified W-energy/D_arch-energy ratio 2.05254409540345269..., with positive denominator. For x=D_arch^(1/2)f, this gives a Rayleigh quotient of the weighted remainder greater than 1.052544. Thus its ordinary two-sided norm is greater than one. This is a rigorous rejection of norm contraction on the actual natural tail, not a negative Weil direction. It is fully compatible with a positive one-sided signed-tail certificate.

At the time of this audit the parent was completing tightened-gate replays and the odd-sector computation. A full both-parity conclusion requires the corresponding passed outputs; the analytic and code audit itself does not stand in for those results. No independent software implementation or external peer review is claimed.

## 6. Final insertion review

Reviewed `weighted_signed_insert.tex` against the current corrected verifier. No blocking defect was found in its five propositions. In particular:

- The non-Schatten diagonal proof uses collected distinct unit-circle frequencies with positive coefficients, so rational relations do not invalidate the positive mean-square limit. The pole diagonal is O_lambda(n^-2); the exact arch remainder has zero diagonal.
- The compact-subtraction argument in the fixed-window weighted asymptotic uses norm convergence of Q_J C Q_J to zero. It asserts no uniformity in the window and explicitly forbids an unsupported joint-limit inference.
- The signed-error conversion has the necessary factor eta C/(1+eta).
- The real even and odd matrices represent the two complex orthogonal reducing subspaces of reflection. Both sector bounds therefore imply the claimed inequality for arbitrary complex vectors, not just real coefficients.
- The finite-vector norm-contraction counterexample is a positive direction; its claim is compatible with the signed inequality.

The tightened even replay at 320 bits passed every Gershgorin row, with exact arch lower floor at n=17 greater than 1.7940 and positive row-margin lower bound greater than 0.9999999999326. Its witness SHA-256 is `7bd24903f7c9616cb87530c7f8bf17f87b6b7c968677e6cb5740cec32cf44cf3`, unchanged under the same-witness replay. At this review the tightened odd replay was still running; only its successful output can complete the both-parity computational premise. The omitted low space has 17 even and 16 odd coordinates, and its inverse-tail Schur correction remains essential.
