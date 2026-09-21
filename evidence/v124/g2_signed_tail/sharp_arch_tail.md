# Sharp archimedean and complete high-Fourier tail at lambda = 3

Research proof candidate, September 21, 2026. All operators, Fourier phases and physical scale factors are those of manuscript v1.14. The result concerns the omitted Fourier complement; positivity of the whole window still requires the signed head/complement Schur estimate.

## Main bound

Put L=2 log(lambda), t_n=2 pi n/L, h_L=sinh²(L/4),

    R_L = exp(−L/2)/(1−exp(−2L)),
    C_L = max(1, 1/4+R_L),
    E_L(t) = 1/(15t)+7/(2t²)+pi/(2Lt)+(2+2R_L)/(Lt²).

Let M_lambda be the essential supremum, for 0≤x≤L, of

    sum_{log m≤x} Lambda(m)/sqrt(m)
      + sum_{log m≤L−x} Lambda(m)/sqrt(m),

with only 1<m<lambda² included. The full-length shift, if lambda² is an integer prime power, is zero on L² and contributes nothing.

For N≥1, set t_*=2 pi(N+1)/L and

\[
 \Gamma_{\lambda,N}^{\rm sharp}
 =\log\frac{N+1}{L}-M_\lambda-\frac\pi2
 -\frac{2C_L}{t_*}-E_L(t_*)
 -\frac{4h_LL}{\pi^2N}.
\]

Then the actual semilocal Weil form obeys

\[
 QW_\lambda(f,f)\ge
 \Gamma_{\lambda,N}^{\rm sharp}\|f\|_2^2,
 \qquad \widehat f(n)=0\quad(|n|\le N).
\]

At lambda=3, M_3=log2/sqrt2+log3/sqrt3+log2/2+log5/sqrt5+log7/sqrt7+log2/sqrt8. Also h_L=1/3, R_L=27/80, C_L=1. Interval evaluation of this exact expression proves

    Gamma_(3,256)^sharp > 0.0148,
    Gamma_(3,512)^sharp > 0.7085.

Thus a strictly positive whole omitted complement is already available beyond Fourier index 256, without extending the finite Weil certificate to that index or using any zeta-zero data. This is a substantial improvement over the earlier crude tail constant; it still does not determine the sign of the finite Schur complement.

## 1. Archimedean sine sequence

Let a_k=2k+1/2. The exact Fourier-grid identity is

\[
 S_n=\int_0^L\rho(y)\sin(t_ny)dy
 =\sum_{k\ge0}\frac{(1-e^{-a_kL})t_n}{a_k^2+t_n^2}.
\]

For t>0, x↦t/(x²+t²) is decreasing. Comparing its sum on x=1/2+2k with its integral gives

\[
 \frac\pi4-\frac1{4t}
 \le\sum_{k\ge0}\frac{t}{a_k^2+t^2}
 \le\frac\pi4+\frac1t.
\]

Indeed the lower integral is one half of the integral from 1/2 to infinity, namely pi/4−arctan(1/(2t))/2; the upper sum adds at most its initial summand to that integral. The omitted exponential sum is nonnegative and at most R_L/t. Hence

\[
 |S_n-\tfrac\pi4\operatorname{sgn}n|
 \le\frac{C_L}{|t_n|},\qquad n\ne0.
\]

No derivative estimate for rho is needed. The Fourier-grid condition t_nL=2 pi n is essential in the positive exponential-series identity.

The off-diagonal archimedean operator is [M_b,H], b_n=S_n/pi and H_nm=1/(n−m) for n≠m, H_nn=0. On the tail |n|>N write b_n=sgn(n)/4+e_n. Since ||H||=pi,

\[
 \|[M_b,H]_{\rm tail}\|
 \le\frac\pi2+\frac{2C_L}{t_*}.
\]

Compression causes no extra term: both multipliers preserve the tail, so its matrix is the commutator with the compressed Hilbert transform.

## 2. Complete archimedean diagonal

Use the already derived exact series identity, with z=1/4+it/2 (complex conjugation does not affect the real parts),

\[
 -A_n=\Re\psi(z)-\log\pi
 +\frac{\Re\psi_1(z)}{2L}
 -\frac2L\sum_{k\ge0}e^{-a_kL}
       \frac{a_k^2-t^2}{(a_k^2+t^2)^2},
 \qquad t=|t_n|>0.
\]

All logarithmic constants are retained. In particular this is the complete diagonal, not a divided-difference diagonal continuation.

For the digamma term use Binet's exact representation [DLMF 5.9.15](https://dlmf.nist.gov/5.9.E15), valid in Re z>0, and the recurrence psi(z)=psi(z+1)−1/z. At w=5/4+it/2,

    |u²+w²| ≥ |Im(w²)| = 5t/4,
    integral_0^infinity u/(exp(2 pi u)−1) du = 1/24.

Thus the Binet integral remainder has modulus ≤1/(15t). Moreover Re log w≥log(t/2), Re(1/(2w))≤5/(2t²), and Re(1/z)≤1/t². Therefore, for every t>0,

\[
 \Re\psi(1/4+it/2)
 \ge\log(t/2)-\frac1{15t}-\frac7{2t^2}.
\]

The absolutely convergent trigamma series gives

\[
 |\psi_1(1/4+it/2)|
 \le\sum_{k\ge0}\frac1{(k+1/4)^2+t^2/4}
 \le\frac4{t^2}+\frac\pi t.
\]

The last comparison separates the first term and bounds the decreasing remaining sum by an integral. The exponential diagonal correction has modulus at most 2R_L/(Lt²). Consequently

\[
 -A_n\ge\log\frac{|n|}{L}-E_L(|t_n|).
\]

Every error term decreases with t. This is therefore a uniform tail lower bound by substituting n=N+1.

## 3. Weighted prime degree

Let a_m=log m and w_m=Lambda(m)/sqrt m. In physical coordinates the prime operator is minus the sum of weighted truncated translations and their adjoints. Its quadratic form is bounded below using 2 Re(z conjugate(w))≤|z|²+|w|²:

\[
 -2\sum_m w_m\Re\int_0^{L-a_m}
            f(x+a_m)\overline{f(x)}\,dx
 \ge-\int_0^L d(x)|f(x)|^2dx
 \ge-M_\lambda\|f\|_2^2.
\]

This estimate applies to arbitrary complex functions and does not depend on a Fourier cutoff. It improves the total-mass estimate because a physical point does not see every shift in both directions.

For lambda=3, use symmetry about x=L/2 and write u=exp(x) in [1,3]. The step breakpoints are

    1 < 9/8 < 9/7 < 9/5 < 2 < 9/4 < 3.

The degree values on the six open intervals are respectively

    P,
    P−w8,
    P−w8−w7,
    w2+w3+w4,
    2w2+w3+w4,
    2w2+w3,

where P=w2+w3+w4+w5+w7+w8. All are ≤P: for the only potentially larger fifth value, w5>w2 because log x/sqrt x increases for 2≤x≤5<e². Values at isolated step boundaries do not affect the essential supremum. Since the first interval has positive length, M_3=P exactly.

## 4. The negative pole term on the Fourier tail

On centered physical coordinates x∈[−L/2,L/2], the pole form is

    2|<f,cosh(x/2)>|² − 2|<f,sinh(x/2)>|².

For the normalized Fourier basis, direct integration gives

\[
 |\widehat{\sinh(x/2)}(n)|^2
 =\frac{4h_Lt_n^2}{L(t_n^2+1/4)^2}
 \le\frac{4h_L}{Lt_n^2}.
\]

The centered basis differs from the uncentered one by (−1)^n, which leaves these norms unchanged. Hence for N≥1,

\[
 2\|Q_N\sinh(x/2)\|_2^2
 \le\frac{4h_LL}{\pi^2}\sum_{n>N}\frac1{n^2}
 \le\frac{4h_LL}{\pi^2N}.
\]

This retains the physical scale and improves the global negative rank-one bound by a factor O(1/N).

Combining Sections 1–4 proves the main lower bound on finite tail sequences. The v1.14 form-core/domain result extends it to the full tail form domain.

## 5. Even-sector refinement

The limiting archimedean commutator [M_sgn/4,H] has only cross-sign entries. Identifying the even tail with positive indices, its matrix is

    K_nm = 1/(2(n+m)), n,m>N,

which is positive semidefinite because 1/(n+m)=integral_0^1 x^(n+m−1) dx. In the odd sector its sign is negative. Thus on the even tail the pi/2 loss may be dropped. The negative pole term vanishes there as well. The improved even-sector constant is

\[
 \Gamma_{\lambda,N}^{\rm even}
 =\log\frac{N+1}{L}-M_\lambda
 -\frac{2C_L}{t_*}-E_L(t_*).
\]

At lambda=3,N=256 this exceeds 1.5867; it may be useful in a parity-separated verified Schur solve. The odd/full bound above remains the conservative bound for the whole tail.

## Scope and checks

The scalar interval evaluation is reproduced by `check_sharp_tail_constants.py`; it does not verify an entire head matrix or Schur complement. The only special-function identity used for the new inequalities is Binet's exact digamma formula and the convergent trigamma series. The archimedean finite-L series is already part of the manuscript's independently certified assembly.

No positivity of a finite Fourier section has been used to infer continuum positivity. This result supplies the positive tail T needed for the signed correction F−B*T^(-1)B; that correction still needs certification, and uniform large-window control remains open.
