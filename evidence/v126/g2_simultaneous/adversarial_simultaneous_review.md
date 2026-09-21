# Simultaneous complete Schur verification and sharper remote bounds

This note began as a review of the simultaneous extension of the v1.24 finite-trial certificate. Sections 1--6 establish the verification method and audit its implementation without assuming a head sign. Section 8 records the subsequent strict gate for the complete even head at the fixed window lambda=4. The odd sector and growing-window scope are separate.

## 1. Simultaneous trial identity and the proposed Young bound

Let G be a matrix of finite trial columns with prescribed outer head B0. Write K=G*WG and R=Q16 WG. The complete tail T is coercive. Then

\[
 B_0^*S_\infty B_0=K-R^*T^{-1}R.
\]

The columns may be generated independently by any numerical algorithm. Once frozen they constitute one exact finite matrix, and the identity applies to all linear combinations. A simultaneous upper enclosure of the residual inverse Gram is necessary; separate scalar certificates do not prove a sign on their span.

In the certified inner decomposition let V denote the retained far-energy Gram, B the retained mixed-vector matrix, y the omitted weighted residual columns, and Y the omitted weighted inner residual columns. The old structured inverse majorant is

\[
 V+y^*y+\mu^{-1}(B-Y^*y)^*(B-Y^*y).
\]

If y*y<=E and ||Y||^2<=rho, then Delta=Y*y satisfies Delta*Delta<=rho E. Matrix Young therefore gives, for every tau>0,

\[
 U_\tau=V+E+\mu^{-1}
 \{(1+\tau)B^*B+(1+\tau^{-1})\rho E\}
 \succeq R^*T^{-1}R.
\]

The comparison with the shifted inner inverse uses the same order argument as v1.24. The source energy and residual remain unshifted. Exact square congruence followed by strict interval LDL can certify K-U_tau>0; a failed lower-bound test does not establish a negative Schur direction.

## 2. Anisotropic alternative using a full inner remote Gram

Suppose Y*Y<=E_Y. For any scalar alpha>||E_Y||,

\[
 (B-Y^*y)^*(B-Y^*y)
 \preceq B^*(I-E_Y/\alpha)^{-1}B+\alpha E.
\]

Proof: for an outer coefficient vector x, express the squared norm as the supremum over an inner-head vector z of

\[
 2\Re\langle Bx-Y^*yx,z\rangle-\|z\|^2.
\]

Use `-2 Re<yx,Yz> <= alpha ||yx||^2 + alpha^(-1)||Yz||^2`, then optimize the remaining strictly concave quadratic in z. This proves the operator inequality for every x. It respects the first-slot-linear convention through the real pairings.

Replacing E_Y by rho I recovers the scalar Young family. Retaining E_Y can improve the estimate on those inner-head directions actually reached by B. No matrix positive-part operation is justified or needed.

## 3. A joint-Gram bound retaining a remote cross centre

Suppose a **single** complete remote Gram enclosure is available:

\[
 \Gamma=
 \begin{pmatrix}\Gamma_{YY}&\Gamma_{Yk}\\
 \Gamma_{Yk}^*&\Gamma_{kk}\end{pmatrix}
 \succeq
 \begin{pmatrix}Y^*Y&Y^*y\\y^*Y&y^*y\end{pmatrix}.
\]

Let L_Y be any Hermitian lower bound on Y*Y, including zero. If

\[
 A_0:=\mu I+L_Y-\Gamma_{YY}\succ0,
\]

then the entire remote contribution obeys

\[
 \boxed{y^*y+\mu^{-1}(B-Y^*y)^*(B-Y^*y)
 \preceq \Gamma_{kk}+
 (B-\Gamma_{Yk})^*A_0^{-1}(B-\Gamma_{Yk}).}
\]

Proof: at any fixed outer vector x, the left side is

\[
 \sup_z\{\|yx-Yz\|^2-\|Yz\|^2
       +2\Re\langle Bx,z\rangle-\mu\|z\|^2\}.
\]

Apply the joint upper Gram to the vector (-z,x) and the lower bound L_Y to ||Yz||^2. The expression becomes at most

\[
 x^*\Gamma_{kk}x+
 \sup_z\{2\Re\langle(B-\Gamma_{Yk})x,z\rangle-z^*A_0z\},
\]

which is exactly the stated right side. This proves all cross terms simultaneously. The supremum is finite because A0 is strictly positive.

The scalar-safe version takes L_Y=0 and Gamma_YY<=rho I with rho<mu:

\[
 U_{\rm joint}=V+\Gamma_{kk}
      +(\mu-\rho)^{-1}(B-\Gamma_{Yk})^*(B-\Gamma_{Yk}).
\]

This may be stronger than Young, but improvement is not automatic. The centre Gamma_Yk is part of a certified *upper joint Gram*, not an asserted value of the true remote correlation. Independent diagonal upper bounds do not justify supplying an arbitrary cross block.

Implementation: concatenate the actual finite sources for Y and y, namely the padded inner source `[I;-Z] C*` and the new trial matrix G. Apply the existing remote moment routine once, on one common physical support through M, and divide the resulting entire Gram by g_(J+1). Beyond J both source supports are absent, so all diagonal/shift terms vanish in these remote output rows. The returned joint matrix has the required Loewner meaning. A positive lower L_Y can, for example, be supplied by an explicitly retained additional remote band; its complete omitted remainder is positive. No assertion about compressed powers is involved.

All operators used in these remote proofs are bounded finite-column maps after weighting. The domain issue remains only in the original finite-trial identity, already settled by the operator core and coercive tail. The head inverse A0^(-1) is finite dimensional and may be used only after its positivity is certified.

## 4. Candidate coherence and a useful exact congruence

Independent canonical-column CG runs use right-hand-side-dependent recurrence coefficients. Their finite-iteration errors can spoil a very small-energy linear combination even when each canonical-column error appears small. Higher arithmetic precision alone does not remove that truncation error.

A practical next proposal is to freeze an invertible head congruence C_X adapted to the old finite trial energy, then generate the candidate solves **directly** for columns of G_old C_X. Their energies can thereby be made comparable before the iterative solves. Verify the new complete G with head block C_X; a positive lower bound on C_X* S_infinity C_X proves the whole head after full rank is established. Transforming already-generated incoherent canonical-column trials afterward does not repair them.

Another legitimate proposal is a shared fixed polynomial iteration for all right-hand sides, which preserves linear cancellations structurally. Neither strategy supplies a proof of convergence or positivity; their frozen outputs still require the same complete matrix gate.

## 5. Initial audit of simultaneous_trial.py

Read the version implementing independent 16-step canonical-column trials and complete matrix verification. No parity, indexing, sign, or enclosure-direction blocker was found.

- Even head modes are 0..16, odd head modes 1..16. The odd offset correctly gives 240 old tail rows 17..256, while both new tail corrections act on 17..M.
- The inner dimensions and finite Z support are correct in both parity sectors. The unshifted source action and shifted inner residual action remain distinct and consistent.
- Full-action zero-mode normalization is retained in the even sector; the odd source has no zero mode. Dense selected-row checks compare the correct physical mode indices.
- K, V, the retained mixed Gram, and the remote E retain all outer-column correlations. Symmetrizing their interval enclosures is safe because their underlying exact matrices are real symmetric.
- The complete remote moment is applied to the entire trial matrix, with a common support and cutoff. The even reused rho checks its witness hash and cutoff/precision; the odd rho is recomputed from the corresponding inner source.
- Candidate midpoint iterations are not proof quantities. Every saved trial coefficient is reconstructed exactly during verification.
- The tau loop supplies alternative valid upper bounds; a strict LDL pass for any one proves the simultaneous head. Negative or unresolved pivots remain inconclusive.

For robustness, retain an explicit positive g_(N+1) gate in the simultaneous verifier, as in the directional checker. The existing fixed-window diagonal proof establishes it for both stated sectors; this additional assertion guards future parameter misuse.

## 6. Audit of the normalized proposal extension

The updated `--normalized` branch also passes the analytic/code review. It forms an inverse-square-root congruence from the positive finite trial LDL factors before the candidate iterations. The saved base columns and candidate corrections are exact dyadics. The verifier uses the actual saved base, extracts its actual head matrix, and requires its interval determinant to exclude zero. Thus a strict simultaneous gate proves the sign on the complete head, rather than on an unverified lower-dimensional span.

One descriptive nuance: taking `original.mid()` after the congruence rounds the complete base at the candidate precision. Therefore the saved base need not be literally the exact product of the old source and the previously frozen congruence. It is a nearby exact finite trial with its own recorded head. This is mathematically harmless because the verification uses those recorded coefficients and checks that actual head's full rank. Any manuscript description should say this rather than asserting an exact algebraic identity that the midpoint rounding changes.

The normalized proposal does not change the required complete sign gate, and no positivity conclusion follows from normalization or the numerical LDL used to propose it alone.

## 7. Joint-Gram code and ordinary-norm error conversion

Reviewed `joint_remote_gate.py` and `quantify_head_error.py`. No mathematical blocker was found for the matching saved inputs.

The joint routine correctly pads the inner source `[I;-Z]C*` and the full new trial source into one common physical-mode array. The moment routine therefore encloses their **joint** weighted remote Gram. Since Gamma_YY is positive semidefinite, the strict gate `trace(Gamma_YY)<mu` proves positivity of `mu I-Gamma_YY` before its inverse is used. The resulting full and scalar joint corrections have the form proved in Section 3. The retained K,V,B correspond to the same trial; a failed joint gate remains inconclusive.

The ordinary-error routine correctly uses the Gram of the actual saved head matrix B0, not an identity approximation. If its strict LDL test proves

\[
 L+\epsilon B_0^*B_0\succ0,
 \qquad B_0^*S_\infty B_0\succeq L,
\]

then invertibility of B0 gives `S_infinity >= -epsilon I` in the ordinary outer-head norm. No normalization of the candidate columns is assumed. For the complete parity form,

\[
 \langle W(h,t),(h,t)\rangle
 =\langle S_\infty h,h\rangle
  +\|T^{1/2}(t+T^{-1}Bh)\|^2
 \ge-\epsilon\|h\|^2
 \ge-\epsilon(\|h\|^2+\|t\|^2).
\]

Thus the same error extends to the entire parity operator. The finite coupling sends head vectors into the Hilbert space, and `T^{-1}Bh` lies in D(T), so this completion is valid on the closed form domain.

Reproducibility recommendation: record the **new trial witness hash** in the ingredient file and require it in the joint routine. The old outer/inner hashes alone do not detect replacing a same-named new candidate after producing ingredients. This does not invalidate the current matching run, but guards against stale-data mixtures in future reruns.

## 8. The subsequent complete even-sector pass

The reviewed 768-bit normalized run, with proposal support 4096, complete verification cutoff 65536, 16 candidate iterations, and tau=0.1, reports a strict 17-pivot pass. The smallest enclosed LDL pivot is greater than `0.76459441016` in the saved head coordinates. The verifier also proves the actual saved head matrix is invertible.

The earlier complete-tail theorem gives

\[
 T_{\rm even}\succeq10^{-8}D_{\rm arch}
 \succeq(1.794\ldots\times10^{-8})I.
\]

The new simultaneous bound therefore proves `B0* S_even B0 > 0`, hence `S_even > 0`. Completing the coercive tail square proves positivity on the **entire even form domain at lambda=4**, including every omitted Fourier mode. This is not merely a statement about the finite compression. Real symmetric matrix positivity also gives complex coefficient positivity by splitting into real and imaginary parts.

The numerical pivot quoted above certifies the sign. It is not an ordinary-norm spectral lower bound, and is not automatically the smallest eigenvalue even in the saved coordinates. Any quantitative spectral gap must include the LDL and congruence factors and the tail coupling.

The earlier failed canonical-column bound is a failed sufficient estimate, not evidence of a negative direction. This even-sector result by itself says nothing about the odd sector or the required growing-window uniformity.
