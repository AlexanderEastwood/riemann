# Growing-window sign: what is already RH-strength, and a gap-free reduction

21 September 2026. Read against the complete v1.17 manuscript and its research log. No main-manuscript edits. The monotonicity equivalence already in Section 20 is not claimed as a new result here.

## Existing equivalence and its exact scope

The semilocal forms q_a are restrictions of the same global Weil form, with compatible ordinary norms under zero extension. Their bottoms lambda_a therefore decrease as a grows. The existing source estimate gives unit trial vectors whose Rayleigh values tend to zero. These facts already prove in the manuscript that lambda_a tends to zero if and only if every finite-window form is nonnegative, the Weil positivity criterion for RH.

Only a cofinal sequence is needed: if a_j tends to infinity and the **complete** forms satisfy lambda_(a_j)>=-eta_j with eta_j tending to zero, then any fixed compactly supported test f satisfies q(f)>=-eta_j ||f||^2 for all sufficiently large j. Passing to the limit gives q(f)>=0. This implication needs no endpoint matching, ground simplicity, or source construction. Source quasimodes are needed only to obtain the matching upper limit lambda_a<=o(1).

A finite list of successful windows does not supply this infinite family. Nor does a lower bound for finite compressions replace a bound for the complete forms: the omitted complement must be included, as in v1.16--v1.17. The paper's monotonicity direction actually gives an upper, not a lower, bound at larger windows.

## A useful new block estimate: no positive complementary gap is needed

Let A be any lower-bounded self-adjoint operator with closed form q. Let P be a finite-rank orthogonal projection with range in the operator domain, and suppose

\[
 \|AP\|\le\epsilon.
\]

Put Q=I-P. Then Q preserves the form domain, and for every form-domain f,

\[
 \boxed{\left|q(f,f)-q(Qf,Qf)\right|
       \le\frac{2}{\sqrt3}\epsilon\|f\|^2.}
\]

Proof: write h=Pf and g=Qf. Since h belongs to the operator domain and h is orthogonal to g,

\[
 q(f,f)-q(g,g)
 =\langle Ah,h\rangle+2\Re\langle Ah,g\rangle
 =\Re\langle Ah,h+2g\rangle.
\]

Its absolute value is at most

\[
 \epsilon\|h\|\sqrt{\|h\|^2+4\|g\|^2}
 \le\frac{2}{\sqrt3}\epsilon(\|h\|^2+\|g\|^2),
\]

because the maximum of t sqrt(4-3t^2) on 0<=t<=1 is 2/sqrt(3), attained at t^2=2/3. This respects the first-slot-linear convention; the real part handles both cross terms.

The constant is sharp even in dimension two. Take P onto the first coordinate and

\[
 A=-\frac{\epsilon}{\sqrt3}
 \begin{pmatrix}1&\sqrt2\\\sqrt2&0\end{pmatrix}.
\]

Then ||AP||=epsilon, q vanishes on P-perp, and the lowest eigenvalue is -2epsilon/sqrt(3).

Consequently, if the complementary form satisfies q(g,g)>=-eta ||g||^2 with eta>=0, then

\[
 \boxed{\inf\sigma(A)\ge-\eta-\frac{2}{\sqrt3}\epsilon.}
\]

This differs from the manuscript's coercive Schur bound: it requires no positive complementary constant c and introduces no division by c. It is useful when competing positive levels collapse. Its premise ||AP||<=epsilon is an operator-norm bound on the entire chosen block, not an individual-vector or fixed-test estimate.

For the rank-one projection onto the actual normalized source, the existing v1.15 full residual estimate does supply ||AP||=||Ap||<=C lambda^6 exp(-2 pi lambda^2/3). Thus the source-complement problem can be stated as asymptotic nonnegativity, without requiring strict complementary coercivity. For a growing source block the needed operator-norm bound remains open.

## Negative directions survive removal of any near-radical block

Suppose a fixed unit compact test f has q(f,f)=-delta<0. Regard its zero extension in every larger window. For any family P_a as above, set g_a=(I-P_a)f. The block estimate gives

\[
 q_a(g_a,g_a)\le-\delta+\frac{2}{\sqrt3}\epsilon_a.
\]

If epsilon_a<sqrt(3)delta/2, then g_a is nonzero and has negative energy. Since ||g_a||<=1, its normalized Rayleigh quotient is also at most the displayed negative number. This statement is independent of the rank of P_a.

Hence a uniformly near-radical source block cannot absorb or conceal an RH-violating negative direction. It remains in the block's orthogonal complement with essentially the same negative Rayleigh value. In particular, for the already proved single source quasimode, asymptotic nonnegativity of its entire orthogonal complement is itself equivalent to RH: RH gives it immediately, and the boxed lower bound gives the converse. This is a useful localization of the missing sign, not a proof of that sign.

## Where the overlap argument becomes circular

At lambda=3, the manuscript correctly uses independently certified positivity and the even spectral threshold to infer sin^2(angle)<=Rayleigh/threshold. Applying that inequality uniformly while assuming the unproved positivity of all larger windows would assume the desired Weil criterion.

Without a known lower spectral bound, small Rayleigh value, small residual, simple even ground, and a positive next eigenvalue do not suffice. In a two-dimensional even sector put A=diag(-1,g), g>0, and

\[
 p=\frac{\sqrt g\,e_0+e_1}{\sqrt{1+g}}.
\]

Then q(p,p)=0, ||Ap||=sqrt(g), the ground is simple and even, and the next eigenvalue is positive, but the ground remains -1 and the overlap is sqrt(g/(1+g)). Taking g extremely small reproduces an arbitrarily strong residual bound while the source misses the negative direction. Adding a positive odd sector changes none of this. This is an abstract countermodel to the inference, not a counterexample to the actual arithmetic form.

A legitimate alternative is Temple's inequality: if an independent complete spectral certificate gives lambda_1>=b>alpha, where alpha=q(p,p) and r=(A-alpha)p, then

\[
 \lambda_0\ge\alpha-\frac{\|r\|^2}{b-\alpha}.
\]

It does not assume positivity, but along growing windows its usefulness requires ||r||^2/(b-alpha) tending to zero. The existing ordinary residual envelope alone does not show that ratio is small when the spectral thresholds also collapse. This is an independent spectral target, not a free consequence of the fixed-window result.

## Why fixed-window positivity does not extrapolate

A positive old ground value d and a new unit direction of positive energy c produce a two-dimensional enlarged form

\[
 \begin{pmatrix}d&b\\\overline b&c\end{pmatrix}.
\]

It is positive precisely when |b|^2<=dc. With d of order 10^-38, a coupling of order 10^-19 can change the sign even when c is of order one. Nesting, continuity, and positive diagonal pieces alone do not constrain this signed cross term. This models the need to retain the actual inverse-action correction in every new window; it is not evidence that the actual larger Weil window is negative.

The pure Weil-positivity route could prove RH without ground endpoint matching if its complete cofinal lower bounds were proved. The paper's alternative finite-metric route has its own graph, endpoint and full-strip requirements; the equivalence above does not discharge them.
