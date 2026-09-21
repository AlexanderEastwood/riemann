# First far-inverse polynomial: sharper prefix bounds and failure tests

Assume throughout the proved closed-form sandwich

\[
 D\preceq U\preceq mD,\qquad D\succeq\gamma I>0,
 \quad m>1.
\]

Let A be the bounded operator represented by the preconditioned form, put H=A-I and h=m-1, and let J_1=I-H/m. Thus

\[
 0\preceq H\preceq hI,\qquad
 U^{-1}\preceq D^{-1/2}J_1D^{-1/2}.
\]

All formulas below are statements about bounded H and J_1. They require no application of the unbounded U to an arbitrary Hilbert vector. The two-sided form order identifies D(U^(1/2)) with D(D^(1/2)), so the inverse identity and bounded preconditioned operator are legitimate. In the actual Fourier calculation, D is diagonal and the prefix projection is orthogonal.

## 1. Scalar prefix estimates

For a right-hand side k set y=D^(-1/2)k, p=P_J y, q=(I-P_J)y. Write

\[
 v=\|p\|^2,\qquad a=\langle Hp,p\rangle,
 \qquad \|q\|\le e.
\]

The proposed estimate is valid:

\[
 \langle Hy,y\rangle\ge
 \max\{0,a-2h\sqrt v\,e\}.
\]

It bounds the cross term with the operator norm of H and discards the nonnegative tail diagonal. Positivity yields the stronger triangle estimate

\[
 \langle Hy,y\rangle\ge
 [\sqrt a-\sqrt h\,e]_+^2,
 \tag{1}
\]

where [t]_+=max(t,0). Indeed the reverse triangle inequality applies to H^(1/2)p and H^(1/2)q.

The known orthogonality p perpendicular q improves this further. For v>0,

\[
 \boxed{
 \langle Hy,y\rangle\ge
 \ell(a,v,e):=[\sqrt a-\sqrt{h-a/v}\,e]_+^2.}
 \tag{2}
\]

The radicand is nonnegative because a<=hv. To prove (2), write z=|<Hp,q>|. Since H^2<=hH and p is orthogonal to q,

\[
 z^2\le\bigl(\|Hp\|^2-a^2/v\bigr)e^2
       \le(ha-a^2/v)e^2.
\]

For a>0, positive-semidefinite Cauchy gives <Hq,q>>=z^2/a. Consequently

\[
 \langle Hy,y\rangle\ge a-2z+z^2/a.
\]

Minimizing over 0<=z<=sqrt(ha-a^2/v)e proves (2). If a=0, positivity forces Hp=0 and the claimed lower bound is zero. If v=0, the prefix contains no information and zero is a valid lower bound.

This is the sharp lower bound using only the scalar data a,v,e,h and prefix/tail orthogonality. For the positive branch take p=(sqrt(v),0), q=(0,e) and the rank-one matrix

\[
 H=\begin{pmatrix}
 a/v&-\sqrt{(a/v)(h-a/v)}\\
 -\sqrt{(a/v)(h-a/v)}&h-a/v
 \end{pmatrix}.
\]

It has spectrum {0,h} and attains (2). On the zero branch, take the lower-right entry a/e^2 and off-diagonal entry -a/(sqrt(v)e); the resulting rank-one matrix has norm a/v+a/e^2<=h and annihilates p+q. Degenerate cases follow directly.

The resulting certified first-polynomial upper bound is

\[
 \boxed{
 \langle U^{-1}k,k\rangle
 \le\langle J_1y,y\rangle
 \le v+e^2-\ell(a,v,e)/m.}
 \tag{3}
\]

Outward interval evaluation must respect the known nonnegative radicands. For example a lower enclosure for a and an upper enclosure for v give a conservative value in (2), since the bracket increases with a and decreases with v; e and h are upper bounds. A negative lower ball endpoint for a may be replaced by zero using the independently proved a>=0.

## 2. Matrix-head version and a noncommutativity trap

Let Y be a matrix of head columns in place of y, and write Y_P=P_JY and Y_Q=(I-P_J)Y. Define finite matrices

\[
 V=Y_P^*Y_P,\qquad A_P=Y_P^*H Y_P,
 \qquad Y_Q^*Y_Q\preceq E.
\]

The scalar bounds (1) and (2) apply to every head vector x, with
v=x^*Vx, a=x^*A_Px and e^2=x^*Ex. Their pointwise positive-part expressions are generally not quadratic forms. One must not substitute matrix square roots and positive parts without a separate operator proof.

A safe directly computable matrix lower bound is, for every fixed 0<theta<=1,

\[
 \boxed{
 Y^*HY\succeq
 (1-\theta)A_P-(\theta^{-1}-1)hE.}
 \tag{4}
\]

It follows from the Hilbert-space Young inequality applied to H^(1/2)Y_Px and H^(1/2)Y_Qx. Therefore

\[
 Y^*J_1Y\preceq V+E-
 \{(1-\theta)A_P-(\theta^{-1}-1)hE\}/m.
 \tag{5}
\]

No factor equal to the number of head columns is introduced. If one can instead certify hE<=r^2 A_P with 0<=r<1, then the sharper relative matrix bound

\[
 Y^*HY\succeq(1-r)^2A_P
\]

follows directly from (1) on every head vector.

Do not replace the right side of (4) by its positive part merely because Y*HY is positive. In general F>=0 and F>=L do not imply F>=L_+. A counterexample is

\[
 F=\begin{pmatrix}2&\sqrt2\\\sqrt2&1\end{pmatrix},
 \qquad L=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Both F and F-L are positive semidefinite, but F-L_+ is indefinite.

## 3. Certifying failure of the first polynomial itself

An upper bound on <Hy,y> gives a lower bound on the first-polynomial correction. For example,

\[
 \langle Hy,y\rangle\le(\sqrt a+\sqrt h\,e)^2
 \quad\Longrightarrow\quad
 \langle J_1y,y\rangle\ge
 v-(\sqrt a+\sqrt h\,e)^2/m.
 \tag{6}
\]

If this lower bound already exceeds the permitted trial energy in a tested direction, the first polynomial cannot certify that direction; better numerical evaluation or a tighter upper enclosure cannot change that fact. A useful stronger failure gate does not require any bound on the remote norm.

Scalar functional calculus on 0<=H<=m-1 gives

\[
 J_1^{-1}=(I-H/m)^{-1}\preceq I+H.
\]

For t in [0,m-1], this is simply m/(m-t)<=1+t. Cauchy in the positive J_1 metric and p perpendicular q imply

\[
 v^2=|\langle p,y\rangle|^2
 \le\langle J_1^{-1}p,p\rangle\langle J_1y,y\rangle
 \le(v+a)\langle J_1y,y\rangle.
\]

Hence

\[
 \boxed{\langle J_1y,y\rangle\ge v^2/(v+a)}
 \tag{7}
\]

for v>0. This is often more informative than the trivial lower bound v/m.

There is an exact matrix version:

\[
 \boxed{Y^*J_1Y\succeq V(V+A_P)^\dagger V.}
 \tag{8}
\]

Indeed the Gram block of J_1^(-1/2)Y_P and J_1^(1/2)Y is positive, with cross block Y_P*Y=V. Its first diagonal block is at most V+A_P. Enlarging that block and taking its form Schur complement proves (8). The generalized inverse is legitimate: 0<=A_P<=hV implies ker(V+A_P)=ker V, so the required range condition holds. If V is positive definite, the generalized inverse is the ordinary inverse.

A strictly positive excess of (7) or (8) over the available budget proves a failure of the first-polynomial certificate, not a failure of the true inverse bound or of Weil positivity. Later inverse polynomials decrease toward the true correction and can in principle succeed after the first fails.

## Scope

These are analytic bounds for the actual bounded preconditioned far operator under its already proved two-sided sandwich. They neither compute the new prefix energies nor prove a signed low-head inequality. The fixed-window constants m=67 or 335 may be inserted only in their certified parity sectors. All residual/source and finite-to-complete distinctions remain unchanged.

## 4. A sharper sector upper bound for the actual far operator

The earlier two-sided sandwich used a global absolute remainder norm. The actual parity signs give a smaller upper bound at lambda=4. In the notation of the existing sharp-tail proof, the limiting archimedean off-diagonal is the positive Hilbert matrix `1/[2(n+m)]` on the even sector and its negative on the odd sector. Its norm is at most pi/2. The remaining arch commutator has norm at most `2 C_L/t_*`; here C_L=1. The signed prime term is bounded above in either sector by the already certified weighted prime norm `p_m`.

The centered pole form is `2|<f,cosh(x/2)>|^2-2|<f,sinh(x/2)>|^2`. Only its positive term remains in the even sector, and only its nonpositive term in the odd sector. With L=2log4 and h=sinh^2(L/4), the complex Fourier coefficient of the cosh vector has absolute value

\[
 |c_n|=\frac{\sinh(L/4)}{\sqrt L\,(t_n^2+1/4)}.
\]

Consequently the even positive-pole tail norm is bounded by

\[
 2\sum_{|n|>N}|c_n|^2
 =4\sum_{n>N}|c_n|^2
 \le\frac{hL^3}{4\pi^4}\sum_{n>N}n^{-4}
 \le\frac{hL^3}{12\pi^4N^3}.
\]

This accounts for the pole factor 2 and for both Fourier signs; no additional parity factor is needed. The phase (-1)^n from centered coordinates is unitary and has no effect on this trace bound or the sign.

Thus the remainder upper bounds for the shifted operator W-cD_arch are

\[
 C_+^{\rm even}=\pi/2+2/t_*+p_m+
               hL^3/(12\pi^4N^3),\qquad
 C_+^{\rm odd}=2/t_*+p_m.
\]

The exact arch diagonal alone is multiplied by 1-c; none of these off-diagonal, prime, or pole terms is multiplied by 1-c. If the existing lower diagonal is
`g_n=(1-c)(log(n/L)-E_L(t_n))-kappa`, with gamma=g_(N+1)>0, then

\[
 D_g\preceq U\preceq
 D_g+\{\kappa+2(1-c)E_L(t_*)+C_+\}I.
\]

Accordingly any integer m strictly above

\[
 1+\{\kappa+2(1-c)E_L(t_*)+C_+\}/\gamma
\]

is valid. The proposed integer targets 20 even and 90 odd require the corresponding interval gate; the analytic comparison itself is justified. This improves the fixed-window inverse approximation prerequisite only and does not by itself sign the low Schur correction.

## 5. Reusing the structured certificate consistently

In the inner block factorization, let R=B-UZ and let the already certified finite lower matrix satisfy
`L_lower <= K_Z-R*D_g^-1 R`, with `C L_lower C* >= mu I`.
If an improved positive upper inverse Q satisfies

\[
 U^{-1}\preceq Q\preceq D_g^{-1},
\]

then the same finite certificate is still admissible, since
`K_Z-R*Q R >= K_Z-R*D_g^-1 R >= L_lower`.
The resulting complete structured inverse upper bound is

\[
 \langle T^{-1}(h,k),(h,k)\rangle
 \le\langle Qk,k\rangle+
 \mu^{-1}\|C(h-Z^*k-R^*Qk)\|^2.
\]

For the polynomial inverses, Q is comparable in form to D_g^-1, so the associated lower form Q^-1 has the required common domain and the same closed-form proof applies. Both occurrences of D_g^-1 must be replaced consistently. Improving the far energy term alone while leaving the old mixed term frozen is not generally a valid bound. For a failure gate, the far term alone is sufficient if it already exceeds the complete allowed budget, since the remaining mixed square is nonnegative.

## 6. Audit of the finite-prefix convolution implementation

Reviewed `refine_inverse.py`, its imported scalar remote-moment routine, and the saved J=16384 output. The finite-prefix energy is correctly computed as

\[
 a_P=k_J^*D_J^{-1}(U_J-D_J)D_J^{-1}k_J,
\]

where U is the shifted far operator W-cD_arch, D is the positive lower diagonal with its original fixed cut N=512, and the outer residual k comes from the unshifted complete trial. The code uses the correct shift in `action`, and forms the prefix norm V=k_J*D_J^-1 k_J separately.

The polynomial action indices are exact. For a prefix of size s, coefficient s-1+i of the product with coefficients `1/k`, indexed by k=1-s,...,s-1 and with zero at k=0, gives `sum_{j!=i} z_j/(i-j)`. Combining the z and bz convolutions therefore gives `sum_{j!=i}(b_i-b_j)z_j/(i-j)`. Coefficient s-1+i of the reversed-vector/Hankel product gives `sum_j z_j/(2 start+i+j)`, producing the correct parity contribution `+/- (b_i+b_j)/(n_i+n_j)`, including the opposite-sign diagonal entry. The same-sign diagonal remains d_n-c a_n. The 25-row dense comparison is consistent with this analytic indexing check.

The scalar remote-moment majorant uses the full parity coefficients: the zero mode contributes S_0 only, nonzero even pairs have the sqrt(2) normalization, and the moment Gram already counts both Fourier signs. Dividing its scalar bound by g_N(J+1) correctly bounds the complete omitted weighted norm. The full infinite weighted operator is never assigned a Hilbert--Schmidt norm.

The smaller remote H bound is also valid. Keep kappa_N fixed in D_g and use the upper remainder at J:

\[
 Q_JHQ_J\preceq\nu_J I,\qquad
 \nu_J=
 \frac{\kappa_N+2(1-c)E_L(t_{J+1})+C_+(J)}{g_N(J+1)}.
\]

This follows because the diagonal commutes with Q_J and the already proved parity upper bound applies to the physical Fourier tail beyond J. Using kappa_J instead in the numerator would change the target lower diagonal and would not justify this statement. The implementation correctly keeps kappa_N.

Since H is positive,
`||H^(1/2)Q_Jy||^2 <= nu_J ||Q_Jy||^2`.
Thus its complete correction satisfies

\[
 \langle Hy,y\rangle\ge
 [\sqrt{a_P}-\sqrt{\nu_J U_k}]_+^2,
\]

and the code's `V+U_k-correction/20` is a rigorous scalar upper bound for the first-polynomial far contribution, assuming the separately verified even m=20 sandwich. This is a scalar calculation, so its positive-part operation has none of the matrix-clipping defect discussed above.

At J=16384, the saved complete far upper bound is approximately 7.93789e-20, above the trial budget K approximately 6.46928e-20. This does not certify that the first polynomial itself fails: the unconditional lower bound is only approximately 1.01433e-20, below K. The finite-prefix value alone is approximately 4.90460e-20 and cannot substitute for the complete quantity. Refining the remote enclosure is therefore logically justified at this stage.

No blocking formula, index, parity, or shift error was found. No conclusion about the complete structured mixed term or the whole head matrix is supplied by this one-direction probe.

## 7. Final manuscript-insertion review

Reviewed `inverse_refinement_insert.tex`, including its general Q_* replacement proposition. No blocking defect was found. The new constant gates match the saved 384-bit output: the even ratio is less than 19.215607 and the odd ratio is less than 89.840960, giving valid integer bounds 20 and 90. The scalar and matrix prefix proofs retain the correct sign of the Young coefficient and do not introduce a matrix positive-part operation.

For the general refined inverse, the domain argument is valid in full: from `D_g<=U<=mD_g` and `U^-1<=Q_*<=D_g^-1` one gets `m^-1 D_g^-1<=Q_*<=D_g^-1`. Thus Q_* is injective with dense range, and its self-adjoint inverse form satisfies `D_g<=Q_*^-1<=mD_g`, with the same square-root form domain. In particular `Q_*Rx` belongs to the operator domain of `Q_*^-1` for each finite head vector. The old lower certificate is retained because `K_Z-R*Q_*R>=K_Z-R*D_g^-1R`. The proof consistently updates both the far quadratic term and the mixed head vector.

A minor statement clarification is to require nu>=0 explicitly in the general prefix proposition; its actual norm-bound values are already positive. No other correction was requested.

The reported J=65536 calculation gives a complete first-polynomial far upper bound about 5.75789e-20, below the one-direction trial energy about 6.46928e-20. This is a meaningful scalar bound including the infinite remote tail, subject to its saved interval gates. It does not evaluate the remaining mixed square or establish the full head-matrix Schur sign. The 896-bit same-witness replay was still in progress when this final insertion review was written.
