# Adversarial Schur assessment and a stronger certified tail

21 September 2026. Fixed window lambda=3, actual unshifted orthonormal Fourier basis, both parity sectors. The final analytic and interval audit below accepts the complete fixed-window Schur certificate. No main-manuscript edits, uniform-window result, or G2 claim are made here.

## A useful improvement: positive weighting of the prime shifts

Let A be the sum of the actual truncated prime translations and their adjoints on [0,L], with nonnegative coefficients. This does not assert that A is positive semidefinite. The Weil prime term is -A. For any bounded strictly positive function phi, weighted Cauchy–Schwarz gives

\[
|\langle Af,f\rangle|
\le\int_0^L\frac{(A\phi)(x)}{\phi(x)}|f(x)|^2\,dx,
\qquad
\|A\|\le\mathop{\rm ess\,sup}_{x}\frac{(A\phi)(x)}{\phi(x)}.
\]

Indeed each edge x to x+s uses

\[
2|f(x+s)f(x)|\le
\frac{\phi(x)}{\phi(x+s)}|f(x+s)|^2+
\frac{\phi(x+s)}{\phi(x)}|f(x)|^2.
\]

Choose phi(x)=cosh(x-log 3) and L=2 log 3. On every interval with a fixed collection of active shifts, the ratio is A_0+B_0 tanh(x-log 3), so it is monotone or constant. Its essential supremum is therefore obtained as a one-sided value at a shift breakpoint.

Write u=exp(x), with 1<=u<=9, and w_m=Lambda(m)/sqrt(m). A forward shift has the exact ratio (m u^2+9/m)/(u^2+9); a backward shift has (u^2/m+9m)/(u^2+9). All breakpoints are rational u=m or 9/m, together with 1 and 9. Thus every endpoint ratio is a rational linear combination of the six actual weights w_2,w_3,w_4,w_5,w_7,w_8.

The maximum is approached from u>7, or equivalently from u<9/7, and equals

\[
M_\phi=
\frac{85}{116}w_2+\frac{65}{87}w_3+
\frac{193}{232}w_4+\frac{137}{145}w_5+
\frac{35}{29}w_7
=2.68905577193190117962112657598\ldots.
\]

The m=8 shift is not discarded: it occurs in the endpoint comparisons for every interval where it is active, but not in the maximizing interval. The full-length m=9 shift is zero as an L2 operator, as in v1.15.

`certify_weighted_prime_tail.py` checks every endpoint comparison at 256-bit Arb precision using exact rational coefficients before interval evaluation. It passed, and its full output is `weighted_prime_tail_certificate.json`. Substituting M_phi for the previous flat degree bound in the proved sharp-tail formula yields

\[
\Gamma^{\rm all}_{3,256}>0.4970,
\qquad \Gamma^{\rm even}_{3,256}>2.0690,
\qquad \Gamma^{\rm all}_{3,512}>1.1907.
\]

The complete all-parity tail is already positive beyond N=156, although the margin there is only 0.00107689; N=160 gives 0.0264381. These smaller cuts are optional. At the requested unchanged N=256 the reciprocal-gap loss falls by more than a factor of 33 relative to 0.0148. This is a certified tail improvement, not evidence that the signed head/complement correction is positive. It is a fixed-lambda calculation; the chosen weight is not asserted to give a useful uniform large-window estimate.

## Retain the growing diagonal in the inverse bound

The same proof gives more than a scalar gap. Put t_n=2 pi |n|/L, t_*=2 pi(N+1)/L and use the already proved E_L(t). On the full tail define

\[
\kappa=M_\phi+\pi/2+2C_L/t_*+4h_LL/(\pi^2N),
\qquad g_n=\log(|n|/L)-E_L(t_n)-\kappa.
\]

For the even sector omit pi/2 and the negative-pole term from kappa. The exact tail operator satisfies T>=diag(g_n), and g_n is positive and increasing for N=256. The positive inverse order is therefore

\[
T^{-1}\preceq\operatorname{diag}(g_n^{-1}).
\]

In the verified-solve identity with residual rows R_n, the final correction obeys

\[
R^*T^{-1}R\preceq\sum_{|n|>N}R_n^*R_n/g_n.
\]

This keeps cancellation inside each residual row and rewards distant frequencies. It is stronger than replacing every denominator by the smallest scalar gap. Annular lower bounds for g_n allow implementation using differences of remote Gram tails: no special-function sum with logarithmic weights is necessary. The upper bound must be a matrix/Gram bound on all head directions, not separate uncorrelated entrywise error claims.

## Further even-sector option: a legitimate finite-rank Hilbert correction

In the even basis the limiting archimedean commutator is the positive matrix K_nm=1/[2(n+m)]. Write

\[
(Vx)(t)=2^{-1/2}\sum_{n>N}x_n t^{n-1/2},\qquad K=V^*V.
\]

For any finite orthogonal projection P_J in L2(0,1), K_J=V^*P_JV satisfies 0<=K_J<=K exactly. Thus T_even>=diag(g_even)+K_J, and the finite-rank Woodbury formula produces a sharper inverse upper bound than the diagonal alone. Shifted Legendre test functions give explicit rational-function moments in n. The original/centered Fourier phase change only conjugates these positive matrices by diag((-1)^n).

An arbitrary positive quadrature rule does **not** automatically give K_J<=K on the entire infinite tail. That unsupported replacement would invalidate a signed certificate. The orthogonal-projection construction avoids it. This refinement is proposed, not computed or certified here.

## What must survive the tiny eigenspaces

1. An ordinary matrix-norm error bound times the identity can swamp a head eigenvalue of order 10^-38. Preserve residual moments as Gram matrices, or use an exact congruence/preconditioner with its metric retained. Near-null source cancellation belongs in the residual rows before taking absolute values.
2. A negative truncated-output certificate rejects that sufficient error budget, not the underlying Weil form. A positive certificate omitting remote rows proves nothing about the whole complement until those rows have a rigorous upper Gram bound.
3. A float64 approximate lowest vector cannot diagnose a 10^-38 Rayleigh value accurately: a 10^-16 admixture in an O(1)-energy direction contributes order 10^-32. Interval LDL, sufficiently precise vectors, or verified congruence is required.
4. Solving the intermediate block exactly in interval arithmetic is legitimate because its positivity is inherited from the already proved tail bound. If a frozen rational approximate solve is used instead, its nonzero intermediate residual must remain in the Gram budget.
5. Positive definiteness of F alone never establishes F-B* T^(-1)B>=0. The new prime weight and inverse comparison only reduce the certified subtraction; they do not authorize dropping it.

The initial recommendation was to retain the growing diagonal and every directional Gram. The completed certificates below show that moderate explicit cutoffs suffice at this fixed window. The inverse-Hilbert refinement was not needed and remains an unimplemented option.


## Final proof and code audit: complete positivity at one window

The parent implemented `certify_infinite_schur.py` using `assembly.py`. I reviewed the actual proof, coefficient assembly, frozen-witness reconstruction, parity moments, matrix error budget, and interval LDL procedure. No blocking issue was found.

The exact remote expansion is

\[
(WG)_n=\sum_{j<r}M^j n^{-j-1}(b_nS_j-T_j)+E_n,
\quad |n|>J>M.
\]

The two-sign Gram is H_jk=M^(j+k)(1+(-1)^(j+k)) zeta(j+k+2,J+1). The factor 8 in the geometric remainder includes both remote tails; c_Mr is the full sum over signed support indices. The script uses normalized parity inputs, hence the sqrt(2) moment factor on positive modes, and embeds them isometrically into the full signed-index space. There is no missing or duplicated opposite-sign output tail. The remote bound is the complete matrix majorant, including its leading moments and the Young-inequality factor; the tiny scalar geometric remainder alone is not substituted for it.

Every finite residual row N<n<=J is retained, including the residual caused by freezing the midpoint solve. The diagonal inverse weights are formed as g(n)=gamma+log(n/(N+1))+E(t_*)-E(t_n), exactly the proved increasing diagonal lower function. The final subtraction is R* diag(1/g) R plus the complete remote Gram divided by g(J+1). This is a form-order consequence of T^(-1)<=D_g^(-1), not an unsupported bound based on a distant subblock alone.

The coefficient assembly retains every shorter prime-power shift and the separate logarithmic diagonal. The full-length m=9 shift is exactly zero in the physical L2 space; including it only in B_* conservatively enlarges the remote absolute bound. Archimedean digamma/trigamma evaluation retains 128 exponentially weighted correction terms and adds the stated uniform sine and diagonal tail radii. All scalar functions and linear algebra use outward Arb ball enclosures.

The publication insert's completion-of-the-square proof is valid on the closed form domain. A positive finite Schur matrix and T>=gamma I>0 give coercivity of the full operator through the bounded invertible map (x,y) -> (x,y+T^(-1)Bx). Positive real symmetric matrices also control complex vectors. The two normalized parity sectors span the complete physical window.

### Same-witness replays at higher precision

Both original 768-bit certificates were replayed at 896 bits using the exact same frozen dyadic witness. The uncompressed witness hashes agree exactly between original and replay. This is an independent replay and analytic/code review, not an independent arithmetic library implementation or external referee review.

| Sector | N | M | J | r | Positive pivots | Smallest pivot enclosure |
|---|---:|---:|---:|---:|---:|---|
| Even | 256 | 512 | 4096 | 80 | 257 | (9.17498,9.17499) x 10^-9 |
| Odd | 512 | 1024 | 4096 | 100 | 512 | (9.68026,9.68027) x 10^-8 |

Even witness SHA256: `993c5b325c1cc7dce64c1dbdab9384dd54dea6a480cce8739cf623e9e8bce43c`.

Odd witness SHA256: `4054507110d6a806c3dfa926c716c1692de4c9b7dc7801263d50b92cbd8dfdea`.

The smallest tail lower values exceed 2.0690 (even) and 1.1907 (odd). The geometric remainder squares are below 1.656 x 10^-148 and 3.288 x 10^-124 respectively. All pivot enclosures and witness identities are recorded in the corresponding `infinite_schur_*_b896_diagonal.json` files. The minimum LDL pivot is not a lower bound for the smallest operator eigenvalue; no numerical coercivity constant is inferred from it.

### Accepted conclusion and limits

There exists epsilon_3>0 such that the complete canonical closed Weil form at the single physical window [1/3,3] satisfies QW_3(f,f)>=epsilon_3 ||f||_2^2 on its full form domain. This includes the entire infinite Fourier complement and both parity sectors. No zero-location assumption is used.

This closes the signed head/complement obligation at lambda=3 only. It supplies neither an estimate along unbounded windows nor a lower bound for the true lowest-eigenvector overlap with the repaired source. It does not settle endpoint stability of that eigenvector, G2, the remaining full-strip transfer obligations, or RH. The existing graph defect remains in every downstream transfer formula.

The earlier N=256, M=512, J=1024, r=128 attempt failed at a negative pivot of its conservative lower majorant. That was a failure of the sufficient error budget, not evidence of a negative Weil form. The certified growing-diagonal inverse bound and larger remote cutoff resolved that budget at this one window. No further experiments were run after the successful higher-precision replays.
