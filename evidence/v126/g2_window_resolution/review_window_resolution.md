# Adversarial review: finite window resolution at lambda=8

Reviewed the current v1.25 research log, `assembly_general.py`, `replay_finite_margin.py`, the saved 4096-bit metric/bracket, and the new `window_resolution_probe.py`. No main manuscript or parent script was edited.

## 1. The v1.25 finite bracket survives replay

The saved result concerns the fixed physical window lambda=8, even head modes 0..64, and the two finite Fourier cuts 256 and 384. Let K=S_256 and S=S_384 be their finite head Schur forms. Its generalized margin is

\[
 m=\inf_{x\ne0}\frac{x^*Sx}{x^*Kx}.
\]

The replay proves K>0 and S-delta K>0 for the saved delta. Its proposed congruence is exactly upper triangular with positive diagonal, hence invertible; interval LDL is applied to the actual congruent interval matrix, not to the midpoint alone. The separate nonzero frozen probe has a strictly positive K denominator and a rigorously bounded Rayleigh quotient. Consequently

\[
 5.697\,10^{-101}<m<5.755\,10^{-101}
\]

is justified. The corrected auxiliary trace bound uses the rigorous norm upper `1+65*10^(-20)` and no floating selection of a row maximum.

The saved trace and probe bounds already give a sharper bracket without another expensive run:

\[
 5.75469\,10^{-101}<m<5.75470\,10^{-101}.
\]

Indeed, with normalized matrices K_n,S_n, the certified trace quantity is

\[
 \ell=\{k_{\max}\operatorname{tr}(S_n^{-1})\}^{-1}
 =5.75469018716023\ldots\,10^{-101},
\]

and the frozen Rayleigh upper is `5.75469270288356...e-101`. Positivity and `K_n<=k_max I` give the asserted generalized lower bound. The coarser published bracket remains valid.

Thus the loss is neither binary64 subtraction to zero nor a mere change of coordinates. The generalized quantity is invariant under the verified invertible congruence. The replay validates the stored normalized matrices; the assembly audit below checks their intended mathematical inputs. The use of the same interval library is not an independently implemented numerical kernel.

## 2. Independent check of the assembly and remainders

Put L=2 log(lambda), t_n=2 pi n/L, h=sinh(L/4)^2, and a_j=2j+1/2. For the positive Fourier indices the assembly uses the full signed matrix with off-diagonal `(b_n-b_m)/(n-m)`, then performs normalized even/odd compression.

**Prime terms.** A direct integral of the two zero-extended translations by y=log(m) gives diagonal

`-2 w_m (1-y/L) cos(t_n y)`

and off-diagonal

`w_m [sin(t_n y)-sin(t_m y)]/[pi(n-m)]`.

These agree with the code's d and b contributions. Only prime powers with m<lambda^2 enter. The full-length translation at m=lambda^2 is zero almost everywhere, so its omission is correct. No arithmetic tail beyond this physical cutoff belongs to this finite-window prime operator.

**Pole terms.** Integrating the kernel `2 cosh((x-y)/2)` on [0,L] gives diagonal

\[
 \frac{32Lh(L^2-16\pi^2n^2)}{(L^2+16\pi^2n^2)^2},
\]

and the corresponding divided difference of

`b_n^(pole)=32 L h n/(L^2+16 pi^2 n^2)`.

In particular the squared denominator in the current diagonal is necessary and correct.

**Archimedean terms.** With `rho(y)=sum_(j>=0) exp(-a_j y)`, evaluation at `t_n L=2 pi n` gives

\[
 \int_0^L\rho(y)\sin(t_ny)\,dy
 =-\tfrac12\Im\psi(\tfrac14-it_n/2)
  -\sum_{j\ge0}e^{-a_jL}\frac{t_n}{a_j^2+t_n^2}.
\]

The finite-window correction to the infinite archimedean diagonal is

\[
 \frac2L\sum_{j\ge0}(1-e^{-a_jL})
        \frac{a_j^2-t_n^2}{(a_j^2+t_n^2)^2}.
\]

The nonexponential part is `Re trigamma(1/4-it_n/2)/(2L)`, yielding precisely the code's digamma/trigamma expression. In deriving this correction, the boundary terms in the integral of `y exp(-a_j y) cos(t_n y)` cancel the separate integral from L to infinity; neither is silently omitted.

For truncation after j=K-1, let e_K=lambda^(-4K-1). The uniform omitted bounds are

\[
 |R_s|\le\frac{e_K}{2a_K(1-\lambda^{-4})},\qquad
 |R_a|\le\frac{2e_K}{L a_K^2(1-\lambda^{-4})}.
\]

They follow from `|t|/(a^2+t^2)<=1/(2a)` and
`|a^2-t^2|/(a^2+t^2)^2<=1/a^2`. The code includes both as interval radii. Increasing arithmetic precision alone would not justify dropping this analytic remainder; the present implementation does not drop it.

**Parity and zero mode.** For n,m>0 the even/odd entry is the same-sign entry plus/minus `(b_n+b_m)/(n+m)`, including the opposite-sign diagonal. The even zero-mode coupling is `sqrt(2)b_n/n`; the zero diagonal is d_0. These are the correct normalized parity factors. The code's integer-lambda scope matches the current grid.

No missing sign, factor, logarithmic diagonal, or analytic series tail was found in this independent calculation.

## 3. What near-null arithmetic can and cannot explain

Ordinary head energies and the normalizing congruence are severely conditioned. Interval LU and serialized elimination may therefore fail through enclosure width even when the exact matrix is positive. Such a failure is not a negative result. Verified congruence and preconditioned interval solves are valid remedies because the final positive gates are still applied to the true enclosures.

For the saved lambda=8 pair, both sides of the generalized bracket pass with all analytic remainder terms retained. Hence ordinary roundoff or uncertain normalization is not an explanation for its tiny certified margin. A *finite-cutoff effect* remains entirely possible: the mathematical objects S_256 and S_384 are different minimization problems. This distinction is crucial. The result is not evidence that the complete Weil form is negative, and it is not an asymptotic assertion from one pair of cuts.

The trace/probe data also isolate one dominant finite inverse direction. For A=K_n^(-1/2) S_n K_n^(-1/2), let 0<d_1<=d_2<=... . Then

\[
 \operatorname{tr}(A^{-1})\le k_{\max}\operatorname{tr}(S_n^{-1})=:T,
 \quad d_1\le q
 \quad\Longrightarrow\quad
 d_2\ge\frac1{T-1/q}.
\]

Taking conservative saved decimals `ell=5.75469018e-101` and `q=5.75469271e-101` gives

\[
 d_2\ge\frac{\ell q}{q-\ell}>10^{-94},\qquad
 d_2/d_1\ge\ell/(q-\ell)>2\,10^6.
\]

This is a finite generalized gap and shows that the smallest relative direction is isolated. It does not say the other relative directions are all numerically well separated from zero, and it is unrelated to an ordinary complete-Weil spectral gap.

## 4. Exact identities for a cutoff sweep

Fix the physical window and a head H. For positive finite matrices through the largest tested cut, define S_M^H by minimizing the quadratic form over modes in E_M minus H. Then

\[
 0\prec S_{M_2}^H\preceq S_{M_1}^H\quad(M_2>M_1),
 \qquad m_H(M_1,M_2)=\sup\{a:S_{M_2}^H\succeq aS_{M_1}^H\}\in(0,1].
\]

Partition the larger finite matrix into head, old tail, and newly added rows:

\[
 \begin{pmatrix}F&B^*&C^*\\B&T&D^*\\C&D&U\end{pmatrix}.
\]

After eliminating the old tail, put

\[
 R=C-DT^{-1}B,\qquad A=U-DT^{-1}D^*\succ0.
\]

The exact improvement is

\[
 S_{M_1}^H-S_{M_2}^H=R^*A^{-1}R.
\]

The inverse belongs to the **omitted Schur block A**, not to its uncorrected block U. This measures relative improvement of positive finite trial energies, not an absolute negative error.

For three nested cuts at the same head and window,

\[
 m_{12}m_{23}\le m_{13}\le\min(m_{12},m_{23}).
\]

The lower inequality follows by chaining the two positive matrix inequalities. The upper inequalities follow from monotonicity of the numerator and denominator forms. Thus a healthy 384-to-512 ratio would be compatible with the already tiny 256-to-384 ratio, but would not erase that earlier loss.

For fixed test cut, increasing the retained cut automatically improves the relative margin. Bringing the cuts close together can make a finite comparison favorable without controlling the untested tail. No finite sweep provides that omitted-tail estimate.

## 5. Changing head size has a built-in monotonicity

For nested heads H_small contained in H_big contained in E_(M1), Schur associativity and order-preserving homogeneous shorting imply

\[
 m_{H_{\rm small}}(M_1,M_2)
 \ge m_{H_{\rm big}}(M_1,M_2).
\]

Indeed, short the inequality for the larger head onto the smaller one and take the maximal allowed scalar. This requires the same window, the same cuts, and positivity of the common finite matrices. It cannot compare operators at different lambda.

An improved small-head margin can transfer the difficulty into its eliminated tail. For A=I_2 and B=diag(1,epsilon), the full-head margin is epsilon. Shorting the second coordinate leaves margin one, while that eliminated block has coercivity epsilon. Therefore head-size comparisons should also record tail inverse scale or conditioning; a recovered head margin alone does not show that the full certificate is easier.

## 6. Audit of the new sweep implementation and useful outputs

`window_resolution_probe.py` verifies both finite tail positivity and the finite head Schur sign, retains the same physical operator across its cuts, and proves each reported generalized bracket by a verified congruence lower gate plus a frozen-vector Rayleigh upper. The 256-term archimedean remainder is retained. No positivity or convergence of a complete outer tail is inferred.

For tracking whether the same fragile direction persists across cuts, save the actual physical head vector Vz, or the frozen V, as well as the normalized probe z. Separately normalized probe coordinates cannot be directly compared for overlap. This is not needed for the margin certificate itself.

A useful next interpretation would be: does the relative loss persist at 384/512 with the same 65-dimensional head, and how much of any change is forced by reducing the head to 37 dimensions? The exact inequalities above give internal consistency checks. They do not replace a complete signed inverse bound, a normalized growing-family estimate, or the ordinary-error conversion required for G2.

## 7. Completed finite sweep and the physical constant head

The subsequent saved 4096-bit, 256-term runs passed all indicated finite tail and head gates. Their enclosures give:

| Head modes | Cuts | Certified finite margin |
|---|---|---|
| 0..64 | 256 to 384 | between 5.6971e-101 and 5.7547e-101 |
| 0..64 | 384 to 512 | between 1.34904e-44 and 1.36267e-44 |
| 0..36 | 256 to 384 | between 1.15556e-93 and 1.16724e-93 |

The smaller head improves the margin as shorting monotonicity requires, but does not produce a healthy finite margin. The second cutoff step likewise retains a substantial relative loss. Neither observation proves an infinite-cutoff limit or an asymptotic law.

`head_reduction_audit.py` was also reviewed. For a positive finite Schur matrix S_M, retaining only the normalized physical constant Fourier mode gives the exact scalar Schur energy

\[
 s_M^{\{0\}}=\frac1{(S_M^{-1})_{00}}.
\]

This follows by ordinary block inversion or by minimizing the positive form over all other head coordinates. The code certifies S_M>0, solves its first inverse column with interval arithmetic, certifies its positive zero component, and forms the reciprocal. The scalar margin is `s_right/s_left`. It is not the Rayleigh quotient of S_M at a vector with all other head coordinates artificially fixed to zero.

The saved constant-head ratios are

\[
 m_{\{0\}}(256,384)=9.52632675579521\ldots\,10^{-42},
 \qquad
 m_{\{0\}}(384,512)=1.45353061226547\ldots\,10^{-14}.
\]

The independent reductions through heads 0..36 and 0..64 give matching enclosed scalar energies at the shared cuts, as Schur associativity requires. The scalar head congruence has condition one. Therefore these finite relative losses cannot be explained solely by multidimensional head-coordinate conditioning. They remain compatible with extreme conditioning of the eliminated positive blocks and with a finite-cutoff resolution effect. Their positivity is retained; they are not negative Weil tests.

No blocker was found in the completed finite sweep or the constant-head shorting audit. These are research checkpoints for the specified finite objects, not a new complete-window sign, a uniform G2 estimate, or an RH conclusion.
