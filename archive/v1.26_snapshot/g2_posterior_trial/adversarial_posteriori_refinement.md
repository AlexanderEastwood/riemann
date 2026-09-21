# Complete residual verification after a finite higher-degree proposal

This note began as an audit of the proposed next computation after v1.23. Sections 1--5 supply a rigorous route around the distinction between compressed polynomial powers and complete operator powers; the initial analytic assessment did not assert a Schur sign. Section 6 records the subsequently completed certificate proving positivity on one fixed complete even Schur direction. No full-head sign or uniform estimate is established. Algebraically the method reuses the existing verified-solve identity with a better frozen trial.

## 1. Exact identity and the correct use of the shifted certificate

Let T be the coercive positive complete, **unshifted** tail operator. For r in its Hilbert space and any finite trial z in D(T), put e=r-Tz. Then

\[
 \langle T^{-1}r,r\rangle
 =2\operatorname{Re}\langle r,z\rangle-\langle Tz,z\rangle
   +\langle T^{-1}e,e\rangle.
\]

Proof: write r=Tz+e and expand the quadratic form of the bounded positive inverse. The real cross term makes the identity agree with the first-slot-linear convention. Finite Fourier vectors lie in the already established operator core, so Tz is a Hilbert vector.

Let S=T-cD be the positive shifted tail certified by the saved inner factors. Inverse order permits

\[
 \langle T^{-1}e,e\rangle\le\langle S^{-1}e,e\rangle
 \le\mathcal U_S(e),
\]

where the last expression is any of the existing complete structured inverse upper bounds. Thus only the **new residual inverse** needs the shifted bound. The energy and the residual should be evaluated with T.

Applying the identity to S instead is valid but different: its residual is r-Sz=e+cDz, and its trial budget has the additional subtraction c<Dz,z>. It is incorrect to combine the S-based identity with the T-based residual without these terms. The T-based version avoids that unnecessary shift penalty.

## 2. Direct source form and simultaneous head version

Let f=[v;-Xv] be the old complete finite source, with outer trial energy K=<Wf,f> and r=P_tail Wf. Extend z by zero on the outer head and set g=f-z. Then

\[
 e=P_{\rm tail}Wg,
 \qquad K-2\operatorname{Re}\langle r,z\rangle+\langle Tz,z\rangle
       =\langle Wg,g\rangle.
\]

Consequently

\[
 K-\langle T^{-1}r,r\rangle
 \ge \langle Wg,g\rangle-\mathcal U_S(P_{\rm tail}Wg).
\]

This gives an especially simple implementation: freeze g exactly, evaluate its complete finite energy, then certify the complete inverse energy of its new residual. Evaluate the energy directly from g to preserve cancellation instead of subtracting large separately rounded terms.

For simultaneous head columns, replace z by a finite matrix Z_new and X by X'=X+Z_new. With R_X=B-TX,

\[
 R_{X'}=R_X-TZ_{\rm new},\qquad
 K_{X'}=K_X-R_X^*Z_{\rm new}-Z_{\rm new}^*R_X
                  +Z_{\rm new}^*TZ_{\rm new},
\]
\[
 K_X-R_X^*T^{-1}R_X
   =K_{X'}-R_{X'}^*T^{-1}R_{X'}.
\]

These are exact Hermitian identities, not entrywise inequalities. A directional pass proves only that direction; the full low-head Schur sign still requires a simultaneous upper Gram and a complete matrix sign gate.

## 3. Complete, implementable residual enclosure

Reuse the certified shifted inner factors Z, R, C, mu and D_g. Split the new residual e=(h,k). Choose J above both the support of g and the support of Z. On the inner far tail let P retain rows through J and Q omit the rest. Define

\[
 V_J=k_P^*D_{g,P}^{-1}k_P,
 \quad b_J=C(h-Z^*k-R_P^*D_{g,P}^{-1}k_P).
\]

The Z term needs only its finite support. Put

\[
 y_Q=D_g^{-1/2}Qk,\qquad
 Y_Q=D_g^{-1/2}QRC^*.
\]

The exact complete old structured bound is

\[
 V_J+\|y_Q\|^2+\mu^{-1}\|b_J-Y_Q^*y_Q\|^2.
\]

If ||y_Q||^2 <= u and ||Y_Q||^2 <= rho, then the scalar direction has the rigorous enclosure

\[
 \boxed{\mathcal U_S(e)\le
 V_J+u+\mu^{-1}(\|b_J\|+\sqrt{\rho u})^2.}
\]

For multiple residual columns, if y_Q^*y_Q <= U_e, then for any tau>0,

\[
 \boxed{\mathcal U_S(e)\preceq V_J+U_e+
 \mu^{-1}\bigl((1+\tau)b_J^*b_J
 +(1+\tau^{-1})\rho U_e\bigr).}
\]

The remote moment routine applies to the actual finite source g. Since n>J lies outside its support, there is no diagonal contribution there; the existing divided-difference moment formula encloses every omitted row. If its unweighted Gram bound is U_raw, monotonicity of g_n gives U_e=U_raw/g_(J+1). The fixed inner source [I;-Z]C* supplies the old Y_Q bound by the same routine. This covers all omitted correlations; it does not identify a prefix product with a complete product.

A cheap alternative, worth checking first if the new residual is small, follows directly from the proved T>=10^(-8)D_arch:

\[
 \langle T^{-1}e,e\rangle\le10^8\langle D_{\rm arch}^{-1}e,e\rangle.
\]

This last weighted residual still needs its complete remote bound. It is only a sufficient gate and may remain too crude.

## 4. Generating a finite proposal without losing the head term

Any numerical method may propose z; correctness comes from freezing it and verifying its complete residual. For example, a finite Galerkin solve T_M z approximately r_M makes the retained residual small. A finite polynomial proposal also works, but it should include the head reconstruction.

In the preconditioned inner variables, let A_M=P_M A P_M on the retained far space, Y_M=P_M Y, p=P_M y, and J_k=P_k(A_M). Set

\[
 \xi=\{M_0+Y_M^*(I-J_k)Y_M\}^{-1}
             (d-Y_M^*J_kp),
 \quad \zeta=J_k(p-Y_M\xi).
\]

The physical proposal is

\[
 z_{\rm head}=C^*\xi,\qquad
 z_{\rm far}=D_{g,M}^{-1/2}\zeta-ZC^*\xi.
\]

The proposal head matrix is positive because J_k<=I and M_0>0. After every coefficient is frozen as an exact dyadic value, this is merely a finite trial. No assertion that it equals the infinite polynomial, the exact inverse, or an exact eigenvector is needed. Omitting the head component would leave the important mixed correction untreated.

Using a proposal support M well below the verification cutoff J preserves a favorable ratio in the existing remote moment remainder. For example M=4096 and J=65536 are compatible; expanding the proposal support all the way to J invalidates that particular remainder estimate and requires a larger verification cutoff or a different enclosure.

## 5. A valid direct polynomial excursion bound, if needed

Let S=I-A/m, s=1-1/m, P be the prefix projection, p=Py, q=(I-P)y. Embed the finite sequence

\[
 v_0=p,\qquad v_{j+1}=p/m+PSPv_j
\]

in the complete space, and let u_j=P_j(A)y. The exact error satisfies

\[
 e_0=q,\qquad e_{j+1}=Se_j+q/m+QSPv_j.
\]

Therefore

\[
 \|u_k-v_k\|\le\|q\|
 +\sum_{j=0}^{k-1}s^{k-1-j}\|QSPv_j\|.
\]

If QHQ<=nu Q, then

\[
 \|QSPv_j\|\le m^{-1}\sqrt{\nu\langle Hv_j,v_j\rangle}.
\]

This explicitly accounts for every exit and return: the complete propagation S of each leakage term includes subsequent excursions. It is rigorous but can be less sharp than the a posteriori residual method. In particular, powers of A_M must still never be relabeled as compressions of powers of A.

## Initial analytic assessment, before the computation

The proposed residual route has no domain or algebraic obstruction. It preserves the unshifted outer energy, the complete mixed term, the fixed first-slot convention, and the existing shifted-tail certificate. It provides a sound next computation; it does not guarantee that any chosen support or polynomial degree will pass. The current first-degree failure certificate remains valid, while a better finite trial followed by complete residual verification is a different estimate.

## 6. Audit of the completed 16-step directional certificate

Reviewed `posterior_trial.py` and the saved 768-bit result for proposal support M=4096 and verification cutoff J=65536. The parent subsequently reported a same-witness 896-bit replay with the same strict pass. No blocking mathematical or code issue was found.

- Only coefficients 17..4096 are changed. The original outer head v, including coefficient zero, is preserved.
- `full_action` includes d_0 at the zero diagonal and the correct normalized even couplings sqrt(2)b_n/n in both zero-mode directions. Its nonzero-mode action is the already audited divided-difference/Hankel convolution.
- Both the new trial energy and its residual use the unshifted Weil operator. The saved inner inverse factors, R action, diagonal lower bound, and shifted-tail certificate consistently use the shifted operator. There is no omitted cD correction because the shift is used only for inverse order.
- The retained mixed vector is exactly C(h-Z*k-R_J*D_g^(-1)k_J). In particular, the code's `-az_head + Z*az_far` is `-R_J*D_g^(-1)k_J` with the correct signs.
- The new remote moment uses the entire finite source g through 4096. Since J is larger than its support, the diagonal vanishes in every omitted output row, and the prior moment theorem applies. Division by g_(J+1) is justified by the established increasing diagonal bound.
- The reused remote inner Gram has the same entire inner-witness hash, the same J, and the same factors C,Z. Its trace is a valid bound for the square of the remote Y operator norm.
- The candidate preconditioner has the intended head reconstruction and far correction. Its recursive CG residual is not used as a proof quantity; only the frozen exact dyadic trial and recomputed complete residual enter the sign gate. Candidate iteration quality therefore cannot create a false pass.

The saved 16-step result gives

\[
 K_{X'}=3.23558434813281795\ldots\,10^{-20},\qquad
 \mathcal U_S(R_{X'}v)<1.424888810223207\,10^{-21},
\]
\[
 S_\infty(v,v)>3.093095467110497\,10^{-20}.
\]

The positivity of the complete tail also gives S_infinity(v,v)<=K_(X'). This is a genuine complete Schur certificate at the unchanged one even head vector. It is neither a certificate for the entire 17-dimensional even head nor an odd-sector or growing-window assertion.

For standalone fail-closed operation, the verifier should explicitly check J>M>=1024, the saved candidate dimensions/M/step fields, exact dyadic reconstruction, and the J/precision fields of the cached remote-Gram record. These are provenance and misuse guards; the reviewed instance uses the matching data and satisfies the required mathematical conditions.
