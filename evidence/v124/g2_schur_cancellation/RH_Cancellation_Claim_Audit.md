# Audit of the “cancellation only on the source” claim

September21,2026. Comparison against the complete v1.20 manuscript and the six supplied screenshots.

**Conclusion:** the source calculation is reproducible, but the claim that strong cancellation occurs only on that source is false for the actual finite Weil form. A certified even Fourier polynomial orthogonal to the manuscript’s exact repaired source still exhibits about30 orders of cancellation. This is a small positive Weil value, not a negative direction or an additional exact null vector. G2 remains open.

## What the screenshots get right

At lambda3 and literal Fourier cutoff N64, the archived normalized rational source candidate gives

| contribution | certified value, rounded |
|---|---:|
|pure archimedean|−1.4324413623987024|
|pole|+1.4877438175417073|
|prime|−0.055302455143004872|
|archimedean plus pole|+0.055302455143004872|
|complete Weil|+5.3123817005863590e−38|

This reproduces the first source table in the screenshots, including its tiny total. It also identifies a notation issue: their displayed “arch” value agrees with **archimedean plus pole**, not with the pure archimedean contribution in the manuscript. The pole term must be explicitly included or absorbed by a declared convention.

The other displayed source total6.28e−38 does not match this candidate. Its normalization, cutoff or source choice would need to be identified before combining the two tables. A displayed matrix residual0.000e+00 by itself is not an interval certificate, especially if one summand was defined by subtraction.

## A certified direction in the exact source complement

Let W=A+P+T be the actual Weil form: A is the pure archimedean part, P the pole part, and T the signed prime part. Retain the physical Fourier scale L=2log3, the complete logarithmic diagonal, and the normalized inversion-even basis on E64. Let p3 be the literal repaired prolate source already certified in the manuscript.

The new certificate proves existence of an inversion-even unit Fourier polynomial v in E64 such that

\[
\langle v,p_3\rangle=0,\qquad
0<QW_3(v,v)<3\times10^{-31},
\]

\[
\langle(A+P)v,v\rangle>0.4,
\qquad \langle Tv,v\rangle<-0.4.
\]

Thus the positive non-prime contribution and negative prime contribution nearly cancel **inside the exact source complement**. In particular,

\[
\frac{QW_3(v,v)}{\langle(A+P)v,v\rangle}
<7.5\times10^{-31}.
\]

This directly rejects the screenshots’ assertions that on the complement “nothing needs to cancel” and that a crude separate estimate suffices everywhere else. It does not reject possible complement positivity: v has a small positive value.

For the intermediate vector orthogonal to the frozen rational candidate, the energies are

| contribution | certified value, rounded |
|---|---:|
|pure archimedean|−0.4195793594316561|
|pole|+0.8369031184491538|
|prime|−0.4173237590174977|
|archimedean plus pole|+0.4173237590174977|
|complete Weil|+2.5844134179925971e−31|

The exact-source transfer gives the strict bounds

\[
2.5829853\times10^{-31}<QW_3(v,v)
<2.5858415\times10^{-31}.
\]

The broad3e−31 bound above avoids attaching significance to unnecessary digits.

## Certificate construction and proof

The eigensolver proposes two columns only; it is not used to certify an eigenvalue. Freeze those columns to exact dyadics with denominator2^300, forming V. Their Gram matrix is rigorously positive definite. The exact coefficient witness is in `cancellation_two_mode_witness.json`.

Let c be the archived source candidate, with its exact decimal-rational coefficients converted into normalized parity coordinates (the positive-index coefficients acquire sqrt2). Set a=V*c, and form x=(-a1,a0). Since the coefficients are real, Vx is exactly orthogonal to c by algebra, not by a small floating residual. Its norm is bounded away from zero. Outward ball arithmetic evaluates all four actual quadratic forms on Vx/||Vx||. The same matrix assembly separately retains the prime and pole diagonal terms and checks the interval enclosure of W−A−P−T.

The prior exact-source certificate identifies the frozen candidate by SHA256 and proves

\[
\|P_{\widehat{P_{64}p_3}}-P_{\widehat c}\|<\delta,
\qquad\delta=4\times10^{-36}.
\]

Project the constructed unit vector away from the exact normalized P64p3 and normalize again. This changes it by less than2delta. For any of the finite Hermitian matrices H, unit-vector quadratic values therefore change by at most4delta||H||. The row-sum norm bounds, checked against every row, are

\[
\|W_{64}\|<8.926,\quad
\|T_{64}\|<5.490,\quad
\|(A+P)_{64}\|<4.176.
\]

These errors are small enough to retain every strict inequality above. Orthogonality to P64p3 is orthogonality to the full p3 because the test remains in E64. For a finite-support Fourier vector, its complete Weil quadratic form equals its finite matrix quadratic form; no infinite-tail positivity or infinite-operator residual assertion is needed for this conclusion.

The verifier replays the same dyadic witness at768 and896bits. All sign decisions use interval inequalities; midpoint eigenvalues are only proposals. The prior exact-source projector bound is a stated dependency on the manuscript’s existing source certificate. Its candidate hash is checked explicitly. This is an internal computer-assisted certificate, not external peer verification.

## Why the inference from the sampled tests fails

Positive basis-vector or random-vector Rayleigh values do not control the worst linear combination. Near-null directions are coherent combinations and can occupy a tiny fraction of the unit sphere. A simple ground eigenvalue does not preclude many further very small positive eigenvalues. Projecting out a single source removes only one direction.

Even without these computations, the inference has a simple countermodel: choose orthonormal u,v in a high-dimensional space, let the positive part be I and the negative part be−(1−epsilon)(uu*+vv*). Both u and v have total energy epsilon. Choosing v spread over many coordinates makes ordinary basis and typical random-vector energies order one, despite the additional cancellation direction in u-perp.

The screenshots report positivity on several finite windows. Those computational claims cannot be independently assessed without their exact matrices, parameter list, tail treatment and certificate files. Even valid finite-window positivity would not establish a uniform growing-window bound, and it would not prove the proposed explanation by archimedean dominance.

## What changes in the research plan

Keep the gap-free reduction and the proved source residual. Do not infer a signed lower bound on the whole source complement from a few directions. Test the smallest generalized directions on that complement and retain the signed non-prime/prime cross-cancellation. A larger near-null block may be useful, but then its full operator residual, dimension and coupling costs must be controlled uniformly.

The low-mode Schur and arithmetic inverse-refinement route remains appropriate. The latest manuscript already distinguishes fixed-source control from a growing near-null block. This audit strengthens that distinction and records a concrete counterexample to the unsupported shortcut.

**No G2 sign gap is closed, no negative Weil direction is exhibited, and no RH proof is claimed.** The complete manuscript remains the148-page v1.20; this audit is supplementary evidence for its next revision.

## Reproduction

From the evidence directory, with python-flint and mpmath installed:

```sh
python3 check_cancellation_subspace.py --bits 768
python3 check_cancellation_subspace.py --bits 896
```

The exact witness and prior candidate/source certificate are supplied. The coefficient cache includes explicit analytic series-remainder radii and can be regenerated. The first-slot-linear convention and all parity/Fourier factors are unchanged.

## Follow-up: the valid alpha=0 argument and the finite/infinite distinction

The user supplied a separate Schur argument and reported F-68 interval certificates. The algebra is correct when the tail inverse exists:

\[
K_X-S_\infty=(X-T^{-1}B)^*T(X-T^{-1}B)\succeq0,
\qquad S_\infty=F-B^*T^{-1}B.
\]

For the actual lambda4 complete Q16 tail, the manuscript already proves T>=10^(-8)D and a_n>1.7940 there. Hence T>1.7940e−8 I, so the inverse exists as a bounded operator. The semidefinite edge case does not arise at this certified split/window.

There is a stronger useful observation for a finite-support X. If X is supported in the finite tail retained by W_M, then

\[
K_X=\begin{bmatrix}I\\-X\end{bmatrix}^*W_M
       \begin{bmatrix}I\\-X\end{bmatrix}
\]

is **exactly** the complete-operator K_X: every vector in this quadratic form has finite Fourier support. Therefore a genuine finite certificate T_M>0 and S_M>0 gives K_X>0 for every X supported in that certified matrix, even without knowing S_infinity>=0. This does not extend automatically to larger supports or untested lambda.

We independently certified K_X>0 on the actual lambda4 even and odd heads, both for X=0 and for the frozen finite solves on17..256. All LDL pivots are rigorously positive at768 and896bits, with identical dyadic solve hashes in both replays. These are direct certificates for K_X; the reported F-68 files were not independently obtained or replayed. Thus **alpha=0 is established for these specific complete-operator K_X**, in both parity sectors. A pivot is not being reported as an eigenvalue lower bound.

This is compatible with the previously failed Schur lower bounds. The complete residual still obeys the exact identity

\[
S_\infty=K_X-r^*T^{-1}r,\qquad r=B-TX.
\]

For the exact finite Galerkin solve X_M=T_M^(-1)B_M embedded in the complete tail, K_(X_M)=S_M. Therefore

\[
\boxed{S_\infty=S_M-r_M^*T^{-1}r_M.}
\]

The finite matrix misses the nonnegative inverse-residual correction on omitted rows. Finite Schur complements decrease to S_infinity when the literal Fourier spaces exhaust the tail form core and T is coercive; a finite list of positive S_M does not settle the limit. Positivity for every member of a cofinal sequence at a fixed lambda would imply S_infinity>=0, though not strict positivity without a positive limiting margin.

The structured inverse estimate bounds the inverse of the same original T. Its comparison metrics do not redefine the Weil operator or the target. It supplies a lower enclosure for S_infinity, while Galerkin truncation supplies upper enclosures. Retaining r_M is exactly what makes the two approaches compatible.

For merely nonnegative T the expression T^(-1)B is not automatic. The sufficient form condition is Ran(B) contained in Ran(T^(1/2)), defining C=T^(-1/2)B; then the generalized Schur form is F−C*C and

`K_X−(F−C*C)=(T^(1/2)X−C)*(T^(1/2)X−C)`.

Orthogonality to ker(T), or membership in the closure of its range, is insufficient when the range is not closed. Thus the user's semidefinite statement requires a range condition; no such difficulty occurs for the certified coercive lambda4 tail.

Finally, the least admissible alpha for a particular K_X can depend on X: F=0,B=1,T=1 gives S=−1, K_0=0 and K_1=−1. Positivity of S is a sufficient common guarantee for all X, not an assertion that approximation quality cannot affect K_X itself. In the positive finite blocks described by the user, the sufficient guarantee is entirely valid.

**Research consequence:** alpha can be set to zero at the newly certified lambda4 instances. The unresolved target is the full inverse-residual bound, and its decay on a genuinely cofinal family of growing windows. The “only the source cancels” explanation remains false, as the separate certificate above demonstrates. Neither result settles a G2 sign gap.


## Final accounting: local sign, convergence, and the route to RH

The latest user clarification correctly distinguishes a sufficient criterion from a necessary condition, and fixed-window certificates from a growing-window theorem. Two points sharpen that accounting:

1. For finite-support X, positivity of its K_X is already a statement about the complete form. It requires no further infinite-tail transfer. Infinite Schur positivity is a different assertion; its missing term is precisely r* T^(-1) r. Local alpha=0 is not yet a theorem for a cofinal growing-window family.
2. The conditional Riesz realization is a prerequisite for the manuscript's operator route, not an unavoidable extra prerequisite for every RH route. If the complete, correctly normalized Weil forms obey W_lambda >= -epsilon_lambda I with epsilon_lambda -> 0 along unbounded windows, each fixed compactly supported smooth f satisfies QW(f,f) >= -epsilon_lambda ||f||^2 for every sufficiently large window. Sending lambda to infinity gives QW(f,f)>=0. Weil's criterion then implies RH directly. This bypasses the proposed Burnol Riesz operator and its evaluator/graph-core assumptions. The manuscript also explicitly states a finite-core metric criterion without those assumptions. None of their remaining transport or sign hypotheses has thereby been proved.

The distinction between inverse approximation and residual control also matters. A convergent geometric approximation to T^(-1) improves an enclosure of the actual residual energy r* T^(-1) r; it does not make that energy vanish for a fixed X. The substantive target is to choose and control X_lambda and all growing-window constants so that the proved residual bound tends to zero. Failure of this sufficient bound would not itself refute G2 or RH.

Primary-source cross-check: Connes, Consani and Moscovici, *Zeta Spectral Triples*, https://arxiv.org/pdf/2511.22755, Section 3 and conclusion, recalls the finite-support Weil positivity criterion and proves the Fourier core statement. The short implication above uses only fixed-support embedding, norm consistency, the assumed lower bound, and this criterion. It does not prove the lower bound.
