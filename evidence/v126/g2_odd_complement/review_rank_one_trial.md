# Adversarial review: one repaired direction and the complete complement

This review concerns the lambda=4 odd-sector trial repair. Sections 1--7 preserve the initial analytic audits and failed attempts; Section 8 records the subsequently passed complete directional certificate and its combination with the complete complement. The old complete s16 upper correction has one numerically large generalized direction. Numerical eigenvalues select a candidate only.

## 1. Exact rank-one update and the actual frozen artifact

Use column coordinates with quadratic forms x*Ax; this agrees with the manuscript's first-slot-linear convention when <Ax,y>=y*Ax. Let G be a finite-support trial with fixed physical head, let T be the positive complete tail operator, and let r be its complete tail residual. Put K=G*WG. For an exact tail-only z and a column ell,

    G' = G - z ell*,       r' = r - Tz ell*.

If a=r*z and beta=z*Tz, then

    K' = K - a ell* - ell a* + beta ell ell*.

The exact inverse correction has precisely the same update:

    r'*T^-1 r' = r*T^-1r - a ell* - ell a* + beta ell ell*.

Consequently K'-r'*T^-1r'=K-r*T^-1r. These statements hold for z in D(T), or in the corresponding form setting with the required inverse/range pairings. Here all trial vectors have finite Fourier support and satisfy the manuscript's operator-domain conditions; the certified complete tail is coercive. The energy update generally has rank at most two, not one.

Before rounding, ell*v=1 makes the selected direction receive the full correction z. A Euclidean dual does not preserve v's K-orthogonal complement. The code uses a numerical Euclidean dual only as a proposal. Independent midpoint rounding of every correction entry need not preserve exact rank one or ell*v=1. This is harmless because the actual frozen trial is reverified from scratch.

Code audit of `rank_one_trial.py`: the update `oldx + x*ell` has the correct sign because the represented trial is base minus stored corrections. Only tail corrections change; copied base/head columns remain unchanged. The old-witness hash is checked against the complete ingredients; the archived inner and outer factor hashes are checked. The approximate generalized eigendirection, midpoint right-hand side, finite PCG, and preconditioner are candidate generation only. No proof may depend on their numerical convergence or on their output being an exact eigenvector. Metadata correctly distinguishes this one-direction repair from 32 independent CG iterations and records the possible full-rank rounding perturbation. No blocking sign or indexing error was found in this candidate generator.

## 2. One direction plus its complete complement

**Proposition.** Let K be positive definite on a finite-dimensional complex head space, let C be positive semidefinite, and put S=K-C. Let v have K(v,v)=1. Suppose, for real s<=1 and sigma>=0,

    S(v,v) >= s,
    C(w,w) <= sigma K(w,w)  for every w with K(w,v)=0.

Then

    S >= (s-sigma) K.

In particular s>sigma proves positivity simultaneously on the whole head.

**Proof.** Write x=tv+w with w K-orthogonal to v. Positivity of C and Cauchy-Schwarz for its possibly degenerate seminorm give

    C(x,x) <= (|t| sqrt(C(v,v)) + sqrt(C(w,w)))^2
           <= (sqrt(1-s)|t| + sqrt(sigma)||w||_K)^2
           <= (1-s+sigma)(|t|^2+||w||_K^2).

Subtract from K(x,x). This proof requires neither an eigenvector nor an estimate of the actual off-diagonal correction: positivity of the complete C supplies its cross-term bound. The coefficient is sharp with these hypotheses: for K=I on C^2 and C=uu*, u=(sqrt(1-s),sqrt(sigma)), the smallest eigenvalue of S equals s-sigma.

**Block version.** Let E be any subspace and F its K-orthogonal complement. If S restricted to E is at least sK simultaneously and C restricted to F is at most sigma K, the same proof using x=e+f gives S>=(s-sigma)K. Separate directional tests on a basis of E do not establish the simultaneous premise.

**Application to the complete Weil form.** Take the old positive trial metric K_old and its exact complete correction C_old=r_old*T^-1r_old. A new finite trial with the same physical head gives the same exact Schur matrix S, although its energy K_new differs. Thus the repaired directional certificate must be divided by v*K_old v. It cannot be divided by v*K_new v and combined with an old-K complement bound.

If U_old is the archived complete upper bound C_old<=U_old, it is enough to certify

    Z*(sigma K_old-U_old)Z >= 0,

where Z spans the exact K_old-orthogonal complement of v. One exact construction is

    Z_j=e_j-v (v*K_old e_j)/(v*K_old v),   j != k,

for any index k with v_k!=0. These columns are independent: a linear combination of e_j for j!=k cannot be a nonzero multiple of v. Interval arithmetic may enclose this exact formula. Simply freezing approximately orthogonal columns and treating them as exactly orthogonal is invalid unless the remaining cross error is bounded. The numerical second generalized eigenvalue does not replace the simultaneous complete complement gate.

## 3. Ordinary norm and low-rank negative-error conversion

Suppose V is the invertible map from saved head coordinates to the physical orthonormal Fourier head. If the actual physical Schur form satisfies

    V* S_physical V >= L >= -C C*,

then exact congruence gives

    S_physical >= -V^{-*} C C* V^-1.

The sufficient ordinary error is

    delta = ||C* V^-1||^2
          = ||C* V^-1 V^{-*} C||.

The last norm is a small matrix when C has few columns. Neither an arbitrary coordinate gap nor cond(V) alone gives this error. For a growing-window argument the needed target is delta_lambda->0. Columnwise error bounds must account for the number of bad directions; their maximum alone is insufficient.

Because the complete tail is positive and the exact Schur completion is valid on the closed form domain, S_physical>=-delta I implies the whole form is at least -delta times the ordinary full norm squared. Completing the positive tail square adds no negative error. This is a fixed-window implication; no growing-window decay is proved here.

For the direction/complement lemma, if s<sigma one may use the ordinary error (sigma-s)||K_old^(1/2)V^-1||^2. If s>sigma it gives a positive head estimate and, together with the already certified coercive complete tail, positivity of the complete form.

## 4. A low-rank error enclosure from a small bad block

In a frozen invertible coordinate basis P, suppose

    P* L P = [[A,B],[B*,D]],   A>0,
    D-B*A^-1B >= -E,          E>=0.

Completing the A square yields

    L >= -P^{-*} J* E J P^-1 = -C C*,
    C = P^{-*} J* E^(1/2),

where J selects the bad-block coordinates. For a nonunitary P one must use the dual columns P^{-*}J*, not the corresponding columns of P. This elementary reduction can certify a low-rank ordinary error without a full eigensystem; it does not itself prove that error vanishes with the window.

## 5. Scope of any ensuing certificate

A passed repaired-direction gate plus a passed complete complement gate would establish the complete odd lambda=4 sign when s>sigma. A passed complete all-column lower-matrix gate would establish the same conclusion directly. The finite candidate solve by itself proves neither. All claims must use the actual rounded artifact and its preserved physical head. No inference to larger windows, G2, or RH follows from this fixed-window result alone.

## 6. Outcome of this trial and the next justified diagnostic

The saved `simultaneous_odd_M4096_s32_normalized_report_b768.json` reports `INCONCLUSIVE_COMPLETE_HEAD_BOUND`: all tested Young-parameter complete lower-matrix gates fail, while the actual new K positivity gate passes. The witness hash is `4d702408393a7fd2793d0170be4e09f3b8fba23414b51a3d729c39edde3a25e0`. Failure of a conservative lower bound is not a negative direction of the exact Weil form.

The parent's selected-direction evaluation, normalized by the old K, gives approximate values Knew=0.9999361654, V=0.7841632100, E=0.0542997628, and retained mixed Gram=0.5125092724. The optimized Young directional lower remains about -0.42. Thus the direction/complement lemma cannot yet be applied to infer positivity, despite the separately passed old complement bound with sigma=0.001. No odd sign gap was closed by this trial.

The observed trial-energy decrease of only about 6.38e-5 gives no practical evidence that more iterations on the same support will repair the missing order-one relative margin. It is not a proof that a larger support is necessary: the complete inverse upper model and separated cross terms may be too costly. The currently running joint-Gram certificate is a justified next test because it retains information discarded by Young's inequality. If that also remains inconclusive, the next experiment should distinguish changing the finite support from tightening the inverse/cross-Gram model; neither change should be presented as guaranteed to close the gap.

## 7. Larger-support scalar verification and exact complement audit

Reviewed `directional_tail_repair.py` and `direction_complement_certificate.py`, including the imported complete residual/remote-moment machinery. This is a proof/code audit, not a claim that the pending scalar sign gate passed.

For the actual M=8192, J=65536, 24-step scalar witness, an independent Python `Fraction` calculation reconstructs all sixteen physical-head coefficients directly from the old base columns and the frozen direction. They agree exactly with the saved scalar witness. Its largest mantissa is 912 bits. Thus a 768-bit reconstruction cannot be assumed exact; the new 1536-bit verifier and explicit `is_exact()` checks address this. The scalar direction's dyadic pairs also match the complement certificate's direction exactly. The latter direction-source witness hash is `4d702408393a7fd2793d0170be4e09f3b8fba23414b51a3d729c39edde3a25e0`.

The index splits are correct for the odd sector: the physical head is modes 1..16, the inner head is 17..N, and the far prefix is N+1..J. `f_action` computes the complete original unshifted Weil-matrix action on the finite source, and the energy K uses every nonzero source coefficient. Only the structured inverse comparison uses the shifted inner operator W-c D_arch. This is the proper ordering: the proved positive archimedean diagonal on these tail modes gives shifted tail <= original tail and hence original inverse <= shifted inverse. The source residual itself is not shifted. The formula `h-Z*k-az_head+Z*az_middle` is precisely the shifted inner residual pairing with D_g^-1 k, including the retained Z term.

The original-metric denominator is correctly taken from the archived old complete K and the exact same v. In particular the scalar trial's new K is not used as its denominator. The complement program constructs an interval enclosure of the exact K-dependent projection; it does not freeze an approximately orthogonal midpoint projection. Omitting a column at a certified nonzero v component preserves full complement rank. Passing interval LDL on Z*(sigma K-U_old)Z therefore proves the stated complete complement bound.

The archived rho bounds the squared norm (via its certified Gram-trace bound) of the fixed inner residual beyond 65536. For J>=65536, restricting those same rows to n>J can only decrease this norm. Reusing rho is therefore conservative. The inner witness hash and mu checks bind the same Z,C and inverse model. The larger outer finite support does not affect rho. For the new outer source, the remote moment bound is recomputed with that source's actual support M and actual J, then divided by increasing positive g(J+1). Consequently V+E+(sqrt(H)+sqrt(rho E))^2/mu includes every omitted row and is a valid complete scalar correction upper.

No blocking sign, indexing, or interval issue was found for these actual parameters. Defensive input checks recommended for subsequent runs are J>max(M,Mi), witness parity odd, and explicit scalar/complement direction equality or a shared direction hash. All three conditions were independently checked in the current artifact. These guards prevent accidentally combining valid certificates for different directions or using the remote expansion outside its support range; they are not additional mathematical assumptions for this run.

## 8. Passed complete scalar certificate and the resulting whole odd-sector sign

The saved `directional_odd_M8192_s24_report_b1024_J65536.json` now passes. The frozen scalar witness hash is `7c9ef2808fe5db611804c94e02aca0f8bdfe63eceadc685c68942b4bef93bacf`; its old parent is `9f81eef783abc2bb1e3e654895a9492763d071287836e5a92fab9c430abe6c73`. Reconstructing the 912-bit scalar coefficients exactly at 1024 bits is sufficient, and the verifier's exactness and exact-head gates pass.

Independently recomputed the following bound from the saved outward-enclosed K,V,E,H,rho and old denominator at 512-bit precision, using multiplication for the positive square:

    (K-[V+E+(sqrt(H)+sqrt(rho E))^2/mu])/(v*K_old v)
      > 0.42914078943603974648311831026347...
      > 429/1000.

This is the complete original inverse-correction bound; E covers every outer residual row after J=65536, and the archived rho covers every corresponding remote inner row. Neither a zero-padded finite inverse nor a compressed operator power is substituted for the complete tail inverse.

Rechecked the exact Fraction physical-head identity, identical dyadic direction, and the scalar, direction-source, old-parent, and complement hashes. The archived `direction_complement_report_b896.json` passes on the exact old-K-orthogonal complement, with sigma=1/1000 and a smallest positive interval LDL pivot exceeding 0.0004086. Both pieces therefore concern the same exact Schur matrix S in the same old head coordinates. The old positive metric remains the common normalization; the new trial energy is used only to evaluate the new valid directional lower.

Let C_old=r_old*T^-1r_old, where T is the complete positive original odd tail. Then C_old>=0 and S=K_old-C_old. The direction/complement proposition with s=429/1000 and sigma=1/1000 proves simultaneously

    S >= (107/250) K_old = 0.428 K_old > 0.

This inference does not assume the frozen direction is an eigenvector. Although the stored matrices and direction are real, a real symmetric matrix inequality is also its complex Hermitian inequality. The PSD Cauchy argument consequently covers all complex head coefficients, consistently with the manuscript's first-slot-linear convention.

To pass from the complete Schur matrix to the full closed odd form, write a general form-domain vector as G_old x+z, with z in the tail and x determined by the invertible physical-head map. Its exact quadratic form is

    x*S x + ||T^(1/2)(z+T^-1 r_old x)||^2.

The finite-support trial lies in the operator domain, so r_old belongs to the tail Hilbert space. The previously certified tail coercivity makes T^-1 and T^-1 r_old bounded, and the finite-dimensional head map is invertible. Hence this completion is valid on the entire closed form domain. A nonzero vector has strictly positive form value: a nonzero head gives a positive first term, while a zero head and nonzero tail give a positive second term. The bounded invertible triangular change of variables also yields some positive ordinary-norm coercivity constant at this fixed window, although the relative number 0.428 is not itself that ordinary full-operator constant.

Thus the complete odd lambda=4 sign is established by the audited 1024-bit directional certificate and the archived complete complement certificate. Together with the separately established even sector, this supports complete fixed-window positivity. It supplies no quantitative growing-window bound and does not close G2 or prove RH. A further precision replay may confirm the same fixed witness but is not being presumed in this entry.

## 9. Localized ordinary error when the repaired block is not yet positive

The proposed refinement is valid. Under the block premises of Section 2, assume additionally 0<=sigma<1, and let P_E be the exact K-orthogonal projection onto E. For x=e+f, put a=||e||_K, b=||f||_K and t=sqrt((1-s)sigma). The PSD correction bound yields

    S(x,x) >= s a^2+(1-sigma)b^2-2t ab
             = (1-sigma)(b-t a/(1-sigma))^2
               +(s-sigma)a^2/(1-sigma).

Consequently

    S >= -eta P_E* K P_E,
    eta = max(sigma-s,0)/(1-sigma).

For s<sigma the constant is sharp under these premises: take K=I on two dimensions and C=uu*, u=(sqrt(1-s),sqrt(sigma)), and minimize the displayed quadratic over the complementary coordinate. For s=sigma the conclusion is nonnegativity only; strict positivity still requires a strict margin or another argument. The current s=0.429, sigma=0.001 has eta=0 and also satisfies the earlier strict positive bound.

With invertible physical-head map V, the resulting ordinary error can be bounded by

    delta = eta ||K^(1/2) P_E V^-1||^2.

This retains the congruence cost only on the potentially bad block. The complete positive tail square extends S_physical>=-delta I to the entire closed Weil form with the same ordinary error. A cofinal family with delta->0 would yield global nonnegativity provided the established common-form identification, zero-extension compatibility, and complete positive-tail/Schur hypotheses hold for that family. This is a sufficient reduction, not a proved growing-window estimate.


### Higher-precision completion

The same frozen8192-support witness was subsequently verified at1280bits, and `certify_odd_full_window.py` independently recomputes both saved directional bounds, confirms the exact Fraction head equality and all cross-certificate hashes, and certifies the rational thresholds429/1000 and1/1000. Both complete reports pass. The complement896-bit run reuses the certified768-bit ingredients and is not a fresh reconstruction of them.
