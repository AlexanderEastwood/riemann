# Adversarial review of the source-complement cancellation test

Reviewed `check_cancellation_subspace.py`, `assembly_general.py`, `cancellation_subspace_b768.json`, the exact dyadic two-column witness, and the archived finite-candidate and exact-source certificates. No blocking mathematical error was found in the stated finite-form counterexample or its transfer to the exact repaired source.

## What the certificate establishes

There exists a unit even Fourier polynomial v in E_64, at lambda=3, with v exactly orthogonal to the full literal repaired source p_3, such that

\[
 |QW_3(v,v)|<10^{-30},\qquad
 Q_{\rm nonprime}(v,v)>0.4,\qquad
 Q_{\rm prime}(v,v)<-0.4.
\]

Here nonprime means the complete archimedean term plus both pole terms in the manuscript's fixed conventions. The computation retains the complete logarithmic diagonal, zero mode, strict prime-power cut, and normalized parity factors. All finite Fourier vectors belong to the established operator core, so their complete quadratic forms equal these finite matrix values. No approximation to an infinite operator action is required for this assertion.

## Checks

1. **Matrix decomposition.** The separate prime multiplier and diagonal have the correct signs: the diagonal is minus twice the weighted cosine sum with factor `1-log(m)/L`. The pole diagonal is `32 L h (L^2-16 pi^2 n^2)/(L^2+16 pi^2 n^2)^2`, and the pole off-diagonal comes from `32 L h n/(L^2+16 pi^2 n^2)`. In the even parity sector this agrees with the positive rank-one physical cosh term. At zero frequency its diagonal is `32h/L`; the off-zero/zero entries have the required sqrt(2) factor. Defining the arch multiplier by subtracting these exact prime/pole multipliers preserves the full arch diagonal a_n. The interval decomposition check is consistent with these analytic identities.

2. **Two-column witness.** Its entries are exact dyadics, not asserted eigenvectors. The Gram-positive gate proves that the trial span is two dimensional. The 2-by-2 positive-definiteness tests bound the whole trial span's Weil quadratic form. The eigensolver only proposed the witness; it has no role in a sign gate.

3. **Exact candidate orthogonality.** Let c be the archived exact-decimal candidate, expressed in the normalized even basis as `(c_0,sqrt(2)c_1,...,sqrt(2)c_64)`. All coefficients and witness columns are real. If a_j is the exact inner product of column j with c, then x=(-a_1,a_0) makes Vx orthogonal to c identically. The interval evaluation encloses this exact algebraic construction, and its positive norm gate proves that it is nonzero. No assertion that a numerically tiny inner product is exactly zero is used.

4. **Source provenance.** The finite candidate hash is `6d326cafbe715752f89b90cd92eb1d5a68ab0b78befb6afe074e797372b1a18e`, matching both the new script and the prior certificate's `frozen_candidate_sha256`. The copied `pswf_source_certificate.json` is byte-for-byte identical to the original source-certificate artifact, with SHA-256 `06ed429775be546fabcefa7f300615fd37ff8c00a879229e7fdbc654ad9fcc19`. Its projector bound is below 4e-36 and refers to the normalized exact P_64 p_3 and this same candidate. The copied polynomial interval artifact is also identical to its original. An explicit new-code equality gate between the prior certificate's candidate hash and the candidate file hash is recommended for automatic future provenance checking; the files actually inspected already match.

5. **Exact-source transfer.** Write P_c and P_u for the two rank-one projectors. If the normalized candidate-orthogonal vector is v_0, then `||P_u v_0||<=||P_u-P_c||<delta`, with delta=4e-36. Orthogonal projection onto u-perp followed by normalization produces v with `||v-v_0||<2delta`. For any self-adjoint finite matrix H, its unit-vector quadratic form changes by at most `4delta ||H||`. The script bounds each required finite operator norm using the largest certified absolute row sum, with comparisons of exact upper endpoints. It does not use a norm bound on the unbounded infinite operator. Since u=P_64 p_3/||P_64 p_3|| and v is in E_64, exact orthogonality to u is exact orthogonality to the full p_3.

The final transferred Weil upper bound is below 2.586e-31, while the nonprime and prime values retain magnitudes above 0.4173. The displayed thresholds therefore have substantial certified margins relative to their transfer errors.

There is also a source-independent dimension consequence. The two-dimensional complex span S of the real witness columns satisfies `|QW(f,f)|<10^-30 ||f||^2` for every nonzero f in S, by the two Gram-order gates. For any single source u in the ambient Hilbert space, S intersects u-perp in a subspace of complex dimension at least one. Hence removing any one source direction leaves a unit finite Fourier vector with this small form value. Source identification is unnecessary for this dimension statement; it is needed for the additional signed prime/nonprime magnitudes above.

## Necessary interpretation limits

This establishes strong **near-cancellation outside the single repaired-source direction**. In particular the witness has

\[
 \frac{|QW_3(v,v)|}{Q_{\rm nonprime}(v,v)}<2.5\times10^{-30}.
\]

It rejects the claim that removing this single source leaves no substantial prime/nonprime cancellation, or an appreciable fractional domination margin.

It does **not** prove an additional exact null vector: the candidate Weil energy is small positive, not identically zero. Consequently it does not by itself refute a statement about the dimension of an exact kernel. It is also compatible with positivity and with a sufficiently tiny fixed-window coercivity constant. A single fixed-window witness does not rule out every possible positive uniform constant across windows. No invariant subspace, infinite-operator quasimode, growing-window estimate, G2 conclusion, or RH conclusion follows from this calculation.

## Follow-up: finite support does settle the trial energy K_X

The finite-support point in the user's follow-up is correct. If the head lies in E_N and X maps it into the finite tail E_M intersect E_N-perp, set G=[I;-X]. Since finite Fourier vectors belong to the operator core,

\[
 K_X=F-B^*X-X^*B+X^*TX=G^*W_MG
\]

is an exact identity for the complete form. It has no omitted-tail error. In particular, if the finite tail block T_M is positive definite and its finite Schur matrix S_M is positive definite, then W_M is positive definite and K_X is positive definite for every such finite X. A direct interval certificate for K_X itself also suffices. A warning about an uncertified infinite inverse is unnecessary for this specific finite-support trial-energy conclusion.

It remains necessary for the *full* Schur conclusion. When the complete tail is strictly positive,

\[
 S_\infty=K_X-(B-TX)^*T^{-1}(B-TX)\preceq K_X.
\]

Therefore a certified K_X>=0 supplies alpha=0 in the trial-energy assumption but does not establish S_infinity>=0. The scalar example F=0, B=1, T=1 has S=-1, K_0=0, and K_1=-1. Thus alpha for a chosen K_X is not determined purely by S, and positivity of one K_X cannot be used as positivity of S.

If T is merely nonnegative, an ordinary bounded inverse need not exist. The correct unshifted form completion requires `Ran B` to be contained in `Ran T^(1/2)`. With the minimal preimage operator C=T^(-1/2)B, the form Schur correction is C* C and

\[
 q[x,y]=\|T^{1/2}y+Cx\|^2+\langle(F-C^*C)x,x\rangle.
\]

The head is finite dimensional, so C is bounded once every head column has such a preimage. The infimum in y may fail to be attained, and the formal vector T^(-1)Bx need not exist. Mere membership in the closure of the range is insufficient. For example, T=diag(n^-2) and b_n=1/n have trivial kernel and b in the Hilbert space, but T^(-1/2)b is not square summable; no finite scalar head F can make that block positive. These issues do not affect the already certified strictly positive lambda=4 tail, but they matter in an attempted growing-window argument that assumes only nonnegativity.
