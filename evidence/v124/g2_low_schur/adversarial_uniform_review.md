# Adversarial review: the low Schur correction and growing-window scales

This review starts from the recovered v1.20 manuscript and its signed lambda=4 tail certificates. It gives exact operator reductions and sufficient quantitative conditions. It does not prove a new growing-window arithmetic sign, or assume that the known single-window sign persists.

## 1. A sharper inverse bound from the existing signed factorization

The scalar consequence `T >= 10^-8 D_arch` is not all the information in the tail certificate. Its finite signed factorization gives a structured upper bound on the inverse. This can be reused to estimate the correction on the new 33-dimensional low space.

Write the already positive tail in a second head/far-tail decomposition,

\[
 T=\begin{pmatrix}F&B^*\\B&U\end{pmatrix},\qquad
 U\succeq D_g\succeq\gamma I>0.
\]

Here the inner head is finite, the far-tail diagonal is positive, and all forms use the manuscript's fixed first-slot-linear convention. Let Z have finite support in the far-tail operator domain and set

\[
 R=B-UZ,\qquad K_Z=F-B^*Z-Z^*B+Z^*UZ.
\]

Suppose the finite certificate proves

\[
 0\prec\underline L\preceq K_Z-R^*D_g^{-1}R,
 \qquad C\underline L C^*\succeq\mu I,\quad\mu>0.
\]

The saved inverse-Cholesky congruence C is an exact numerical witness; its construction method has no proof role. For every right-hand side r=(h,k),

\[
 \boxed{
 \langle T^{-1}r,r\rangle
 \le \|D_g^{-1/2}k\|^2+
 \mu^{-1}\|C(h-Z^*k-R^*D_g^{-1}k)\|^2. }
 \tag{1}
\]

Both signs inside the last parentheses are minus signs.

**Proof.** Set the original tail variable equal to `(x,y-Zx)`. The exact form is

\[
 \langle K_Zx,x\rangle+2\Re\langle Rx,y\rangle+q_U[y].
\]

Its lower bound is

\[
 \langle\underline Lx,x\rangle+
 \|D_g^{1/2}(y+D_g^{-1}Rx)\|^2.
\]

This is a strictly positive closed form: its diagonal factors have positive lower bounds, and its triangular factors are bounded invertible because the inner head is finite and D_g^{-1}R is bounded. The linear functional for r becomes

\[
 \langle h-Z^*k,x\rangle+\langle k,y\rangle.
\]

Taking the variational supremum for the inverse of the lower form gives

\[
 \|D_g^{-1/2}k\|^2+
 \langle\underline L^{-1}
 (h-Z^*k-R^*D_g^{-1}k),
 h-Z^*k-R^*D_g^{-1}k\rangle.
\]

The congruence bound implies
`L_lower^-1 <= mu^-1 C* C`, proving (1). This is a form argument and is valid for the unbounded logarithmic far-tail operator. All terms are well-defined for k in the ambient Hilbert space; D_g^-1/2 and D_g^-1R are bounded.

If the archived factors belong to `T-cD_arch`, as in the current certificate, they already give an upper bound on `T^-1`: inverse order gives `T^-1 <= (T-cD_arch)^-1`. Alternatively recompute the same factors and residual rows for unshifted T; no new floating solve is required. Do not silently reuse shifted residual rows as unshifted ones.

For a matrix of right-hand sides r, (1) is a matrix Gram inequality. It preserves cancellation in `h-Z* k-R*D_g^-1 k` and charges small directions only through the actual certified finite inverse, rather than multiplying every direction by 10^8. It is not guaranteed to dominate the diagonal inverse bound in every direction; both are valid upper bounds and can be compared directionally.

## 2. Computing the structured inverse bound with finite rows

Split k and R into rows up to J and beyond J, with J beyond the support of Z. Define

\[
 H_J=h-Z^*k-\sum_{n\le J}R_n^*k_n/g_n,
 \quad V_J=\sum_{n\le J}k_n^*k_n/g_n.
\]

The sums here range only over indices in the inner far tail, with both Fourier signs or the correctly normalized parity coordinates. Suppose rigorous remote Grams satisfy

\[
 \sum_{n>J}R_n^*R_n/g_n\preceq U_R,
 \qquad
 \sum_{n>J}k_n^*k_n/g_n\preceq U_k.
\]

These are the existing separated, finite-column moment estimates, not a whole infinite Hilbert--Schmidt estimate. Put `rho >= ||C U_R C*||`. Then for every tau>0 the correction in (1) is bounded by

\[
 \boxed{
 V_J+U_k+\mu^{-1}\left\{
 (1+\tau)H_J^*C^*CH_J+
 (1+\tau^{-1})\rho U_k\right\}. }
 \tag{2}
\]

Indeed, for the omitted mixed sum E, write
`CE=(D_g^-1/2 R C*)* (D_g^-1/2 k)` on the remote rows. Consequently
`E* C* C E <= rho U_k`, and matrix Young's inequality finishes the estimate. No factor equal to the number of outer head columns appears. Keeping a joint moment Gram for R and k can further improve the mixed term; merely discarding it with an unsigned scalar bound may lose useful cancellation.

## 3. A precise dimension-free sufficient criterion along growing windows

For each window lambda, split the full form into an outer head and its positive tail T_lambda. The head dimension may grow arbitrarily. Let an outer finite solve X_lambda give

\[
 S_{X,\lambda}=F_\lambda-B_\lambda^*X_\lambda-
 X_\lambda^*B_\lambda+X_\lambda^*T_\lambda X_\lambda,
 \qquad r_\lambda=B_\lambda-T_\lambda X_\lambda.
\]

Then the exact Schur matrix is

\[
 S_\lambda=S_{X,\lambda}-r_\lambda^*T_\lambda^{-1}r_\lambda.
\]

Apply (1) to r_lambda=(h_lambda,k_lambda). If independently

\[
 S_{X,\lambda}\succeq-\alpha_\lambda I,
 \quad
 \|D_{g,\lambda}^{-1/2}k_\lambda\|\le e_\lambda,
 \quad
 \|C_\lambda(h_\lambda-Z_\lambda^*k_\lambda-
 R_\lambda^*D_{g,\lambda}^{-1}k_\lambda)\|\le t_\lambda,
\]

then completion of the outer form square proves

\[
 \boxed{\mathsf W_\lambda\succeq
 -\left(\alpha_\lambda+e_\lambda^2+
 t_\lambda^2/\mu_\lambda\right)I.}
 \tag{3}
\]

Thus `alpha_lambda + e_lambda^2 + t_lambda^2/mu_lambda -> 0` is a sufficient ordinary-norm criterion along any cofinal family. This statement is uniform in the head dimension because it uses operator norms/Gram orders, not bounds on selected source columns. It does not remove the need to prove the signed head bound or to control the actual inner inverse factors uniformly. Those assumptions contain the unresolved arithmetic content.

The older coarse tail estimate gives the simpler sufficient condition

\[
 S_{X,\lambda}\succeq-\alpha_\lambda I,
 \quad \|D_\lambda^{-1/2}r_\lambda\|\le\delta_\lambda,
 \quad T_\lambda\succeq c_\lambda D_\lambda
 \quad\Longrightarrow\quad
 \mathsf W_\lambda\succeq-
 (\alpha_\lambda+\delta_\lambda^2/c_\lambda)I.
 \tag{4}
\]

The division by c_lambda cannot be improved using only these hypotheses. Already a one-dimensional tail with `T=cD` and a right-hand side in that direction attains the bound exactly. Retaining the signed factors is additional information; positivity alone cannot supply it.

## 4. Two hidden growth factors that must not be discarded

### Column bounds versus a growing head

If the outer head has d_lambda columns and only the bound
`||D^-1/2 r e_j|| <= delta_lambda` is known for every column, the valid operator estimate is

\[
 \|D^{-1/2}r\|^2\le d_\lambda\delta_\lambda^2.
\]

This factor is sharp: take all columns equal to the same tail vector. Pairwise correlation or a direct Gram bound is necessary to remove it. A bound for the single two-mode source does not establish a bound for a growing head. In particular, if a coarse arithmetic cutoff makes d_lambda exponential, columnwise tolerances must compensate for that growth; saying that each column residual tends to zero is insufficient.

### Congruence errors versus ordinary errors

A certificate `C L C* >= -eta I` yields

\[
 L\succeq-\eta C^{-1}C^{-*}
 \succeq-\eta\|C^{-1}\|^2 I.
\]

A tiny negative error after a well-scaled congruence is therefore not automatically a tiny ordinary spectral error. Positivity is invariant under invertible congruence; the magnitude of a negative error is not. The same issue occurs if a weighted head energy replaces I. Finally, the manuscript's relative signed bound `D^-1/2 R D^-1/2 >= -(1+eta)I`, together with `R>=-C_lambda I`, converts to ordinary error `eta C_lambda/(1+eta)`. All three scale factors must be distinguished.

## 5. An explicit remote approximation budget

There is a simple fallback bound for the separated remote rows that is uniform in the number of output columns. If G has Fourier support |m|<=M, J>M, and `|b_n|<=B_*`, then the actual divided-difference off-diagonal gives

\[
 (Q_J\mathsf W_\lambda G)^*(Q_J\mathsf W_\lambda G)
 \preceq
 \frac{8B_*^2(2M+1)}{J-M}\,G^*G.
 \tag{5}
\]

To prove this, the squared Hilbert--Schmidt norm of the *separated* matrix is at most

\[
 4B_*^2(2M+1)\sum_{|n|>J}(|n|-M)^{-2}
 \le\frac{8B_*^2(2M+1)}{J-M}.
\]

The diagonal never enters. Dividing the right side by g_(J+1) gives the corresponding weighted Gram bound when g is increasing. For `G=[I;-X]`, its exact final factor is `I+X*X`, not the number of head columns. The directional moment estimate in the manuscript is usually much sharper than (5); (5) identifies explicitly which quantities any uniform truncation claim must control. With polynomial bounds on B_*, M, ||X||, and g_(J+1)^-1, polynomially larger J can make this remainder polynomially small. Such bounds do not prove the remaining signed head inequality.

Increasing the moment order controls the geometric remainder, but does not make the leading moment Gram disappear. A claim of exponentially small *whole* remote residual based only on a high moment order is invalid unless the actual leading moments have separately been controlled.

## 6. Assessment and next concrete use

The useful immediate experiment is to evaluate the old tail factors on the new low-head residuals through (1) or (2), alongside the coarse `10^8 D_arch^-1` upper bound. The stronger estimate needs the existing exact dyadic Z and congruence C, the certified row margin mu, and the same complete residual rows and remote moments; it requires no new positivity assumption. Apply it separately in the two parity sectors and retain their exact normalizations.

If this proves the complete lambda=4 low Schur sign, it is a new single-window result. It still cannot be extrapolated to arbitrary windows. For uniform work, (3) gives an ordinary-error target with every inverse, coupling, and growing-dimension cost visible. At present no argument here proves its signed head hypothesis or its inverse-factor scales along an unbounded family. No G2 or RH claim follows from this review alone.

## 7. Concrete implementation audit and a certified failed-candidate gate

Reviewed `structured_low_schur.py`, the new zero-mode-aware `assembly_general.py`, and the archived exact tail witnesses. The implementation correctly splits the outer residual into h on rows 17 through N and k on rows N+1 through J, and uses the first Mi-N rows of k in Z* k. The inner residual uses W-cD, while the outer trial energy and residual use the unshifted W; inverse order justifies exactly this use. The selected mu=0.9999999999 is strictly below both archived 320-bit congruence margins, and the witness hashes match. The zero Fourier mode contributes only S_0=1 to the remote moments, while its off-diagonal parity matrix entries are sqrt(2)b_n/n. All these factors agree with the full Fourier convention. No blocking formula or index error was found.

The first candidate used the even outer solve through M=256, the archived inner cut N=512 and support Mi=1024, and J=4096. Its structured estimate failed. A high-precision midpoint diagnosis, explicitly not a proof, gave:

| Quantity | Midpoint diagnostic |
|---|---:|
| Smallest eigenvalue of trial K | 2.83033e-75 |
| Largest generalized eigenvalue of (V,K) | 2.88045 |
| Largest generalized eigenvalue of (U_k,K) | 5.02177 |
| Largest generalized eigenvalue of (H_J* C* C H_J,K) | 1.20930 |
| Largest generalized eigenvalue of the complete tau=1 correction against K | 62.1234 |

These diagnostics are saved in `structured_even_M256_midpoint_diagnostic.json`. The decisive failure diagnosis was then converted to an interval check: an exact dyadic vector, with denominator 2^160, has

\[
 \begin{aligned}
 x^*Kx&\in[6.46928439415864760555\ldots\times10^{-20}],\\
 x^*Vx&\in[6.81404407434054455021\ldots\times10^{-20}],\\
 x^*(K-V)x&=-3.44759680181896944662\ldots\times10^{-21}
              \quad\text{with interval radius below }4.2\times10^{-86}.
 \end{aligned}
\]

The exact numerators, 768-bit interval energies, and scope are saved in `structured_ceiling_counterwitness.json`. They use the saved Arb enclosures in `structured_even_M256_J4096_ingredients.json`. Thus the optimistic ceiling K-V is already not positive. Every further term subtracted by (2) is positive semidefinite. Consequently no choice of the Young parameter or moment order can make this *same frozen candidate with these inner inverse weights* certify positivity. Increasing J alone only adds positive terms to V and cannot fix it either. This is a rigorously falsified certificate candidate; it is **not** a negative direction for the exact Weil form or exact Schur complement.

A justified refinement changes the outer solve or improves the inner inverse, rather than increasing arithmetic precision alone. In particular, the current implementation's restriction M<=N is not required by the mathematics. The outer solve can extend through Mi or beyond, keeping the same inner h/k split. The remote requirement is J>max(M,Mi), and each moment call must use its actual support maximum. Higher M can reduce the actual outer residual before applying any inverse bound. Whether that succeeds needs a new certificate; it is not inferred from the current failure.

Finally, reviewed `structured_inverse_insert.tex`. Its enlarged lower-form domain and inverse variational argument are sound. Requested only small clarifications: call g_n the increasing diagonal lower weights (their reciprocals decrease); call the congruent remote trace a permissible choice of rho; explicitly include both Fourier signs in the finite/remote row split; and state finite support before choosing J beyond Z. No substantive analytic gap was found in the insertion.

## 8. The two justified solve expansions also fail the same ceiling test

The parent expanded the actual outer solve to M=512 and then M=1024, retaining the certified inner factors and J=4096. Both structured sign tests failed. Each failure was then checked against the stronger optimistic ceiling K-V using a separately frozen exact dyadic vector:

| Outer support M | Strict interval enclosure of x*(K-V)x | Radius less than |
|---|---:|---:|
| 256 | -3.44759680181896945e-21 | 4.2e-86 |
| 512 | -1.11469298502037761e-19 | 2.1e-84 |
| 1024 | -7.20037401977242684e-59 | 3.3e-124 |

The vectors are stored in `structured_ceiling_counterwitness.json`, `structured_ceiling_counterwitness_M512.json`, and `structured_ceiling_counterwitness_M1024.json`. Their input ingredient files have SHA-256 hashes recorded in each witness. The standalone script `check_structured_ceiling.py` checks those hashes and recomputes the Arb quadratic forms from the interval ingredients; all three checks passed at both 768 and 896 bits. No floating-point eigensolver enters its sign gates. The midpoint eigensolver was used only to suggest the frozen dyadic witnesses.

Reproduce the quadratic-form checks with:

```sh
python check_structured_ceiling.py --bits 896
```

This verifier assumes the input matrix enclosures produced by the separately archived assembly scripts. It is not an independent reimplementation of the explicit formula. All three results reject these particular certificate candidates, not the true signed Schur matrices. No further parameter expansion was attempted after the third failure.

## 9. A monotone signed refinement of the far inverse

The ceiling failures isolate an actual need: replace the crude far inverse D_g^-1 by an upper bound retaining more of U. A rigorous way to do this is available once one proves a two-sided preconditioned bound

\[
 I\preceq A=D_g^{-1/2}UD_g^{-1/2}\preceq\mathcal M I.
\]

This is a bounded operator defined first through its form; no unbounded operator products are assumed. For \(\mathcal M>1\), put
\(S=I-A/\mathcal M\) and

\[
 P_k(A)=\mathcal M^{-1}\sum_{j=0}^{k-1}S^j+S^k,
 \qquad k\ge0,
\]

where the empty sum is zero. Scalar functional calculus gives

\[
 A^{-1}\preceq P_{k+1}(A)\preceq P_k(A)\preceq I,
 \qquad
 0\preceq P_k(A)-A^{-1}
       =S^k(I-A^{-1}),
\]

and

\[
 \|P_k(A)-A^{-1}\|\le(1-1/\mathcal M)^k.
\]

The monotonicity follows from
\(P_k-P_{k+1}=\mathcal M^{-1}S^k(A-I)\succeq0\).
For \(\mathcal M=1\) the inverse is already exact. The first nontrivial upper bound is

\[
 U^{-1}\preceq D_g^{-1}
 -\mathcal M^{-1}D_g^{-1}(U-D_g)D_g^{-1},
\]

interpreted through forms when needed. Thus the correction to the old bound is a signed nonnegative subtraction, rather than another unsigned norm term. Certifying its evaluations on the actual low-head residuals remains work.

The parent proposed an explicit bound for \(\mathcal M\). Two normalization/justification points were checked:

1. The correct global bound for the separate pole diagonal is `32 h/L`, not `32 h/L^2`; its zero-mode value is exactly `32 h/L`. Consequently
   `C_R = 2 pi B_* + 32 h/L + 2 P`
   bounds the norm of `W-D_arch` from its bounded commutator and separate prime/pole diagonal.
2. The existing manuscript proved only the lower arch diagonal estimate, but the same E_L bounds its upper error. With `z=1/4+it/2` and `w=z+1`, the same Binet argument has
   `Re log(w)-log(t/2) <= 25/(8t^2)`;
   the recurrence contributions `-Re(1/(2w))-Re(1/z)` are nonpositive. The remainder bound `1/(15t)` is unchanged, and `25/8<7/2`. The existing absolute trigamma and exponential-series bounds therefore give
   `|a_n-log(|n|/L)| <= E_L(|t_n|)`.

For the shifted inner tail `U=(1-c)D_arch+R`, this proves

\[
 D_g\preceq U\preceq D_g+\Omega I
             \preceq(1+\Omega/g_{N+1})D_g,
 \quad
 \Omega=\kappa+2(1-c)E_L(t_*)+C_R.
\]

Here `0<=c<1`, the existing lower tail certificate supplies D_g, and E_L decreases. This makes the polynomial inverse prerequisite quantitatively accessible at the fixed certified window. It does not establish the low-head sign, and a fixed-window contraction factor is not a uniform-in-window estimate.

## 10. Final audit of the actual fixed-window inverse constants

Reviewed `far_inverse_insert.tex`, `certify_far_inverse.py`, and its saved 384-bit output after the 320-bit computation. No blocking mathematical or code issue was found. The bounded-form inverse identity is justified as follows: the two-sided form order `D_g<=U<=mD_g` implies equality of their square-root form domains. Since `D_g>=gamma I`, the bounded map `D_g^-1/2` sends the entire Hilbert space onto that domain. The represented preconditioned form is therefore a bounded positive operator A with `I<=A<=mI`. The variational inverse identity gives `U^-1=D_g^-1/2 A^-1 D_g^-1/2`; no illicit application of an unbounded U to arbitrary Hilbert vectors is required.

The actual remainder bound is enclosed near `C_R=34.4504616030760`. With the same positive shifted diagonal weights as the earlier tail certificate, the upper ratios are strictly below 66.76640 in the even sector n>512 and 334.71708 in the odd sector n>1536. Thus integers 67 and 335 are valid, giving geometric factors 66/67 and 334/335. The script checks positivity of each gamma and a strict interval inequality against the claimed integer; the arithmetic gates do not use midpoint comparisons.

These are estimates for the complete shifted far operators at lambda=4. The theorem's matrix-error bound and its conditional growing-window scale are correct, but the explicit integers are not asserted uniformly in lambda. The signed polynomial-power evaluations and the final low-mode Schur sign remain outstanding. No G2 sign gap was closed in this revision.
