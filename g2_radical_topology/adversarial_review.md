# Adversarial review: dense radicals, strong-resolvent collapse, and positive comparisons

Reviewed against the complete v1.35 manuscript and cumulative log, September 21, 2026. This is a mathematical review of proposed v1.36 statements, not a certificate for G2 or RH.

## Verdict

The strongest proposed result is valid: after ordinary zero-extension, the complete fixed-window selfadjoint Weil operators converge to zero in the **strong-resolvent sense** as the window grows. Removing either the actual normalized source or the v1.35 growing radical block and assigning zero on that removed block preserves the limit. This determines no lower spectral edge and proves no G2 sign inequality.

The bounded-positive-comparison obstruction also holds, with explicit uniform boundedness, compression, and domain assumptions. A fixed closed nonnegative comparison form is annihilated on the limiting source complement, provided it is defined on the actual projected cutoff tests. It need not vanish on the source direction itself.

## 1. Setup and exact hypotheses

Let H=L²(R), H_a=L²((-a,a)), and embed H_a in H by zero extension. All inner products are linear in the first slot. Put lambda=e^a. Let W_a be the already constructed complete canonical selfadjoint Weil operator on H_a. Define the selfadjoint operator

    A_a = W_a direct-sum 0
    D(A_a) = D(W_a) direct-sum L²(R\(-a,a)).

This direct sum, rather than an unspecified restriction of a full-line operator, is essential. No globally closed positive Weil operator is assumed.

The v1.35 source phi is ordinary-L² normalized, nonzero, even, smooth and double-exponentially decreasing with all fixed derivatives. For each fixed finite complex linear combination

    h = sum_j c_j phi(.-t_j),  t_j real,

put h_a=chi_a h, with the manuscript's even smooth physical cutoff. The localization part of the v1.35 proof gives

    h_a -> h in H,    ||A_a h_a|| -> 0.

Although the displayed v1.35 growing block uses integer lattice translates, its individual-column tail estimate applies to every real center |t|<=a/2. Thus it applies eventually to each of the finitely many fixed t_j above. The lattice Gram estimate is not needed here. The complete all-prime tail, pole, and archimedean bounds remain necessary; a finite-matrix residual would not suffice.

## 2. Totality is valid in ordinary L²

The Fourier transform Phi of phi is entire because phi has every exponential moment. It is not identically zero. Its real zeros are therefore isolated and have Lebesgue measure zero.

If v is orthogonal to every real translate of phi, the inverse Fourier transform of the L¹ function v-hat times conjugate(Phi) vanishes identically. Fourier uniqueness then gives v-hat times conjugate(Phi)=0 almost everywhere. Since Phi is nonzero almost everywhere, v=0. The real-translate span is dense in H.

This is ordinary L² totality only. It is not graph-norm density for any limiting Weil operator. The spaced lattice in v1.35 is generally not total, and replacing arbitrary translates by that lattice would invalidate this density proof.

## 3. Strong-resolvent convergence

Fix nonreal z and let R_a(z)=(A_a-z)^(-1). For each h and h_a above,

    R_a(z)h + z^(-1)h
      = R_a(z)(h-h_a) + z^(-1)(h-h_a)
        + z^(-1)R_a(z)A_a h_a.

Selfadjointness gives ||R_a(z)||<=1/|Im z|, hence

    ||R_a(z)h + z^(-1)h||
      <= (1/|Im z|+1/|z|)||h-h_a||
         + ||A_a h_a||/(|z| |Im z|) -> 0.

The dense translate span and the uniform resolvent bound extend this convergence to every h in H. Therefore A_a converges to the zero operator in the strong-resolvent sense. No uniform lower bound is used.

There is no conflict with the consistency of q_a[f] for a fixed compactly supported f. Strong-resolvent convergence does not imply convergence of those unbounded quadratic values on a fixed core. The approximating graph vectors here are the moving cutoffs of noncompact radicals, not the fixed compact test itself. Ordinary density must not be upgraded to form or graph density.

## 4. Deleting small-residual blocks

Let P_a be an orthogonal finite-rank projection with range contained in D(A_a), and suppose epsilon_a=||A_a P_a||->0. Write Q_a=I-P_a. The bounded operator A_a P_a has adjoint equal to the bounded extension of P_a A_a. Set

    E_a=A_a P_a+P_a A_a-P_a A_a P_a,
    A_a^Q=A_a-E_a on D(A_a).

Then E_a is bounded selfadjoint with ||E_a||<=3 epsilon_a. On D(A_a), A_a^Q=Q_a A_a Q_a; it assigns zero on the removed block and is selfadjoint by bounded perturbation. The resolvent identity bounds the difference of its resolvent and that of A_a by 3 epsilon_a/|Im z|². Thus A_a^Q also converges strong-resolvent to zero.

This applies to the actual normalized source and to the full v1.35 growing radical projection. It does not require those projections themselves to converge. Explicitly define the compression through this bounded perturbation; writing an unbounded QAQ without its domain would leave a gap.

## 5. What this convergence does not prove

On ell², let P_n project on the nth basis vector. Both -P_n and -nP_n converge strong-resolvent to zero. Their lower spectral edges are respectively -1 and -n. Consequently even a uniform operator norm bound together with strong-resolvent convergence to zero does not establish an asymptotically nonnegative lower edge.

The desired G2 estimate is an operator-order statement, equivalently a statement excluding every fixed-depth negative spectral subspace eventually. Strong convergence only tests each fixed vector and misses moving directions.

For each delta>0, the spectral projections 1_{(-infinity,-delta]}(A_a) converge strongly to zero. Thus normalized vectors in those spectral ranges must converge weakly to zero. Persistent negative directions, if any, necessarily escape compactness. They can escape in position, frequency, or another noncompact manner; spatial escape alone is not proved.

A conditional next criterion follows: if normalized negative spectral vectors at each fixed depth delta admitted a uniformly precompact family in ordinary L², they could not exist along an unbounded sequence of windows. Uniform spatial and frequency tightness would suffice by Kolmogorov--Riesz. Such tightness is an additional unproved estimate, not supplied by the radical argument or by a tail estimate whose cutoff grows with lambda.

## 6. Uniformly bounded positive comparisons

Let u_a be the actual unit source, extended by zero, with u_a->phi and ||A_a u_a||->0. Let Q_a=I-|u_a><u_a| on H_a. Suppose B_a is positive, B_a=Q_a B_a Q_a, and sup_a||B_a||=M<infinity. Extend B_a by zero to H. Suppose eta_a->0 and

    q_a[f] >= <B_a f,f> - eta_a ||f||²

holds for all relevant source-orthogonal physical form-domain vectors; in particular, it must hold for f_a=Q_a chi_a h.

For every finite translate combination h,

    f_a -> (I-|phi><phi|)h,
    ||A_a f_a|| -> 0,
    <B_a f_a,f_a> -> 0.

Positivity and boundedness imply ||B_a f_a||²<=M <B_a f_a,f_a>. Consequently B_a annihilates in the limit the dense set of projected translates in phi-perp. Compression additionally gives ||B_a phi||<=M||phi-u_a||->0. Uniform boundedness extends the conclusion to every fixed vector: B_a->0 strongly.

If B_a is not compressed, only the compressed family Q_a B_a Q_a is forced to collapse. A rank-one positive form on the limiting source direction is not excluded.

Sharpness checks:

* Strong convergence is not operator-norm convergence: P_n->0 strongly but ||P_n||=1.
* Uniform boundedness is essential: n²P_n vanishes on every fixed finite-support test eventually, but it does not converge strongly to zero (test x_n=1/n).
* This does not rule out moving high-frequency metrics, unbounded window-dependent comparison forms, or an exact signed estimate with vanishing negative error. It rules out a nontrivial fixed ordinary-Hilbert-space positive comparison detectable on fixed vectors.

## 7. Fixed closed nonnegative form

Suppose b is a fixed densely defined closed nonnegative form on H, viewed as an extended-valued lower-semicontinuous functional, and that the preceding comparison holds with b[f] in place of <B_a f,f>. It is necessary that every actual projected cutoff test f_a belongs to D(b); an assertion only on an unspecified domain intersection is insufficient.

Then b[f_a]->0. Lower semicontinuity gives b[(I-|phi><phi|)h]=0. The zero set of b is closed in H, so density gives phi-perp contained in ker b. Because D(b) is dense, it has a vector outside phi-perp; subtracting its phi-perp component gives phi in D(b). Thus D(b)=H and

    b[f]=c |<f,phi>|²,  c>=0.

In particular b is zero on phi-perp. It need not be zero on the whole space. If the comparison instead holds on the full physical space, the unprojected cutoff tests imply b=0 globally.

## 8. Actual low-concentration complement and parity

When every removed physical deep/plunge column is even, the full odd subspace is contained in the actual C_a^low, regardless of the number or conditioning of those columns. Odd reflected translates phi(.-t)-phi(.+t) span a dense subspace of odd L²: an odd vector orthogonal to all these differences is orthogonal to every translate.

The even cutoff preserves oddness and the complete residual estimate. Therefore any uniformly bounded positive B_a compared against q_a on actual C_a^low must satisfy B_a f->0 for every fixed odd f. B_a need not preserve parity for this conclusion, because positivity turns vanishing odd test energy into vanishing full B_a action. Any fixed closed nonnegative comparison form with the required test-domain inclusion must vanish on the entire odd subspace.

No assertion is made about all of C_a^low when its changing even blocks are not controlled. If odd image columns are also removed, their relation to the odd cutoff tests must be analyzed separately. Identifying C_a^low with the source complement would be unjustified.

## 9. Prior-work and novelty screen

The nearest project result is v1.35 RAD-02, itself a continuation of the earlier derivative-radical gap obstruction. The new mathematical ingredient is ordinary-L² totality of **all real translates**, combined with graph approximants and the selfadjoint resolvent bound. It yields a full strong-resolvent limit and collapse of positive comparison forms, rather than only a growing count of near-zero eigenvalues or an upper ceiling on a positive gap.

Searches of the current complete manuscript and cumulative log found no earlier dense-translate/strong-resolvent-collapse or fixed-closed-positive-comparison statement. This remains a strengthened obstruction and continuation, not a new live positive mechanism. It is not a renamed Schur complement, altered cutoff, finite-rank repair, common-Gram factorization, or scalar prime-norm estimate. The underlying translate cyclicity and graph criterion for strong-resolvent convergence are classical; worldwide novelty is not asserted.

## 10. Stronger sufficient target: one uniform finite lower bound

The parent's subsequent strengthening is correct and is more directly useful than the convergence obstruction: **a uniform finite lower bound on any unbounded cofinal sequence of complete physical windows already implies exact Weil positivity on every compact test**. The bound need not tend to zero.

Here is an elementary constructive proof. Suppose a fixed f in C_c^infinity(R) has q[f]=-d<0. Given epsilon>0 choose a finite real-translate combination h with ||f-h||<epsilon. For sufficiently large a containing the support of f, put

    g_a=chi_a h,    w_a=f-g_a.

Then g_a is in the actual operator domain, ||A_a g_a||->0, g_a->h, and support consistency gives q_a[f]=q[f]. Therefore

    q_a[w_a]
      =q[f]-2 Re q_a[f,g_a]+q_a[g_a] -> -d,
    ||w_a|| -> ||f-h|| < epsilon.

The mixed term tends to zero because q_a[f,g_a]=<f,A_a g_a>; its use respects the first-slot-linear convention. Consequently the lowest Rayleigh quotient is eventually at most -d/(2 epsilon²), after harmlessly choosing a stricter approximation tolerance if needed. Since epsilon is arbitrary, the lower spectral edge tends to minus infinity. This works along all sufficiently large real a, not only a chosen subsequence.

Contrapositively, any cofinal sequence with a common finite lower bound excludes every negative compact test. The established C_c^infinity form-core statement near the v1.18 physical logarithmic-Laplacian decomposition then extends positivity to every fixed-window closed form. Weil's criterion gives RH only **if the new uniform arithmetic lower bound is actually established**. No such bound follows from the argument.

Equivalently, one may apply Cauchy--Schwarz to the nonnegative form q_a+C||.||², first let a tend to infinity on fixed h, and then approximate f by h. Taking C>0 by enlarging a proposed constant yields q[f]>=0. The constructive argument above needs no form-convergence theorem or common-domain spectral theorem.

### Survives the actual small-residual projection

Suppose P_a is either the actual rank-one source or any finite-rank physical projection with range in D(A_a) and ||A_a P_a||->0. Gap-free comparison gives

    |q_a[w]-q_a[(I-P_a)w]| <= (2/sqrt(3))||A_a P_a|| ||w||².

Thus the same arbitrarily negative normalized directions exist in (I-P_a)H_a whenever a negative compact test exists. A **uniform finite lower bound on this remaining complement**, with no shrinking-error rate, suffices for full positivity. It is strictly weaker as a hypothesis than the previously requested explicit eta_a->0 estimate, although it remains an RH-equivalent global arithmetic assertion in this special family.

Do not transfer this statement to arbitrary C_a^low without checking the removed block's full residual. The odd-sector version does apply on actual C_a^low when every removed physical column is even: odd reflected translates are total in odd L² and their cutoff tests stay in that complement. That proves odd positivity from a uniform odd lower bound, not the missing even comparison.

### Checks and limitations

* A lower-bound constant supplied separately at each fixed window is insufficient; the same finite C must work along an unbounded family.
* This is not a generic consequence of strong-resolvent convergence. The consistent fixed-test form and the dense graph-null approximation are essential.
* The growing lattice alone is not enough: arbitrary translates are needed for density.
* The conclusion concerns a lower bound, not a positive spectral gap, so the v1.35 gap obstruction is respected.
* A concrete sign or uniform lower-bound estimate is still missing. Calling this a proof of G2 would be incorrect.

## Conclusion

No blocking mathematical issue was found after the domain, compression, and boundedness conditions above were made explicit. The strong-resolvent statement is an unconditional obstruction to a qualitative operator-convergence shortcut. The later constructive dichotomy gives a sharper sufficient target: prove one uniform finite ordinary-norm lower bound on the required small-residual complement along a cofinal family. That missing arithmetic estimate would imply positivity; it is not proved here. No G2 gap was closed.
