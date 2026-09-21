# Adversarial review of the ordinary residual and sharp Fourier tail

21 September 2026. Reviewed against complete manuscript v1.14 and the candidate files `operator_residual_derivation.md` and `sharp_arch_tail.md`. No main-manuscript edits were made.

## Outcome

Both proposed arguments passed internal analytic review. The first closes the ordinary-norm source/Rayleigh/residual prerequisites for the actual repaired two-mode source and its unchanged literal Fourier projection. The second gives a positive entire omitted Fourier complement at lambda=3 already beyond index 256. Neither supplies a signed head/complement Schur bound, a ground-state overlap lower bound, an endpoint-normalized graph estimate, or G2.

## 1. Actual unweighted residual: accepted with its stated scope

The conclusion checked is

\[
c_0\le\|p_\lambda\|,\|P_{N_\lambda}p_\lambda\|\le C,
\qquad
\|\mathsf W_\lambda p_\lambda\|+
\|\mathsf W_\lambda P_{N_\lambda}p_\lambda\|
\le C\lambda^6e^{-c/3},
\]

where c=2 pi lambda^2, L=2 log lambda, and N_lambda=ceil(lambda^8(1+L)). Constants and the eventual threshold are asymptotic, not numerically certified. The finite compression inherits the estimate by orthogonal projection.

The decisive point is that the manuscript's Sobolev estimate explicitly holds for **every** periodic H1 test with one constant independent of the test and lambda. Taking its dual supremum over unit vectors in E_M gives a factor O(1+M/L+sqrt(M/L)). Summing separate per-mode estimates would introduce an unnecessary sqrt(M) and would not yield the claimed exponent at the chosen split. The submitted proof uses the correct supremum.

The following details were checked:

- The physical unit-norm Hermite approximation retains the uniform O(lambda^-2) error. In the squared-norm expansion, its cross term is bounded using the fixed Hermite L1 norm, and its squared error contributes O(lambda^-3). No unjustified unit-normalization precision is assumed.
- The limiting source is exactly

  \[
  h_\infty(u)=\frac{4\pi}{\sqrt3}u^2(2\pi u^2-3)e^{-\pi u^2}.
  \]

  Its two moments vanish, its Fourier eigenvalue is +1, and its co-Poisson output is inversion even. On the window the summand error is at most C lambda^-1 u^-1/2. Squaring and integrating du/u gives O(lambda^-1); Gaussian tails and inversion complete the claimed global L2 convergence O(lambda^-1/2).
- The displayed positive norm lower bound follows from positive summands for u>=1. The explicit estimate using u in [1,11/10] has the correct factor 2 pi/sqrt(30) and exponent -121 pi/100. It is an eventual lower bound, not a certified finite-lambda threshold.
- For e=(I-P_N)p, the accepted v1.14 coefficient tail and the actual logarithmic diagonal give

  \[
  \|\mathsf W_\lambda e\|
  \le C|B_\lambda|\lambda\sqrt{L/N}
    [\lambda+1+\log(2+N/L)]
  \le C|B_\lambda|\lambda^{-2}.
  \]

  The bounded commutator has norm O(lambda), by the already established Chebyshev prime-mass estimate. The coefficient and graph bounds concern the complete operator, including its distinct logarithmic diagonal.
- For M>2N, the off-diagonal Hilbert–Schmidt estimate is exactly O(lambda sqrt(N/M)); no extra L factor or physical endpoint factor belongs in this estimate. The diagonal contributes zero between those disjoint sections.
- Choosing the auxiliary **output** split M=ceil(exp(2c/3)) makes the low-output and high-output estimates at most C lambda^6 exp(-c/3). This does not enlarge the actual candidate's cutoff N and does not replace the finite object.
- The first-slot-linear identity used for dual testing and the canonical operator/core domain are consistent. The argument uses the already proved radical/pole-prime cancellation through the uniform Sobolev estimate; it never separates the actual infinite prolate exterior prime and pole contributions into divergent absolute norm sums.

For either ordinary unit-normalized candidate, this establishes alpha=<Wu,u>->0 and ||(W-alpha)u||->0. It does not identify which eigenvalue is approximated.

## 2. Sharp full-tail and even-tail lower bounds: accepted

All constants in `sharp_arch_tail.md` were checked. In particular:

- The sine-series comparison first uses the decreasing majorant t/(a_k^2+t^2); the exponential correction is at most R_L/t. This gives |S_n-(pi/4)sgn n|<=C_L/|t_n|.
- Binet's digamma formula after shifting z to z+1 has denominator imaginary part 5t/4. With integral u/(exp(2 pi u)-1) du=1/24, its remainder is at most 1/(15t). The reciprocal terms contribute 7/(2t^2). The trigamma and finite-L series yield exactly the remaining terms in E_L(t). The logarithmic diagonal constant is log(|n|/L), with no missing 2 pi.
- The prime degree function counts actual truncated translations and their adjoints. Its six interval values for lambda=3 are correct. The full-length m=9 translation is zero in L2 and is excluded correctly.
- The negative pole vector is sinh(x/2). Its squared Fourier coefficients and the doubled two-sided tail give the stated 4 h_L L/(pi^2 N) loss.
- The parity refinement is valid. In the original translated Fourier basis the even compression of the limiting commutator has entries 1/[2(n+m)], a positive Gram kernel. In the centered basis the alternating phases conjugate this matrix by diag((-1)^n), preserving positivity. The odd compression has the opposite sign, and the negative pole term vanishes only on even tests.

The scalar Arb evaluation was rerun at 256 bits using the existing runtime dependency. It passed all strict inequalities:

\[
\Gamma_{3,256}^{\rm sharp}>0.0148,
\quad \Gamma_{3,256}^{\rm even}>1.5867,
\quad \Gamma_{3,512}^{\rm sharp}>0.7085.
\]

The enclosed values begin 0.0148329203130568, 1.5867887543730771, and 0.7085077224770671, respectively. This rerun uses the same Arb implementation, not independent software verification. It certifies the scalar analytic constants; it is not a certification of the head matrix, its inverse action, or the signed Schur correction.

## 3. The remaining overlap requirement is substantial

Let u_lambda be the normalized actual source, phi_lambda a normalized lowest eigenvector, kappa_lambda=|<u_lambda,phi_lambda>|, and epsilon_lambda=C lambda^6 exp(-c/3). The spectral equation gives the exact inequality

\[
|\lambda_0(\lambda)|\,\kappa_\lambda
\le\|\mathsf W_\lambda u_\lambda\|
\le\epsilon_\lambda.
\]

Thus an **independent** estimate kappa_lambda/epsilon_lambda->infinity would imply lambda_0(lambda)->0. Together with domain-inclusion monotonicity, this would force nonnegative lowest values on every fixed window. Conversely, if lambda_0(lambda)<=-delta for a fixed delta>0, then kappa_lambda<=epsilon_lambda/delta. A negative ground direction can therefore be exponentially close to orthogonal to the constructed source without contradicting the new residual theorem.

No such independent lower overlap bound is established here. The elementary model diag(-1,epsilon_lambda), with the candidate equal to the second coordinate vector, satisfies arbitrarily small ordinary residual and Rayleigh value while its lowest-state overlap is zero. It is a logical warning, not a counterexample to the arithmetic operator. The overlap/signed-Schur problem remains the sign problem; it is not a negligible normalization detail.

Dividing the accepted residual estimate by the physical endpoint instead gives an exponentially growing upper bound proportional to exp(2c/3) times a polynomial. No endpoint-normalized compatibility estimate follows.

## 4. Backup route considered and not pursued

A separate route used the physical PSWF operator H_lambda=H_0+lambda^-2 V, with H_0=-d^2+4 pi^2 u^2 and V=(u^2 d/du)'. Harmonic ladder algebra gives V=(a^4+(a*)^4-2N^2-2N-3)/4. Its first corrections are w_0=-sqrt(6)H_4/(32 pi) and w_4=sqrt(6)H_0/(32 pi)-sqrt(105)H_8/(16 pi). Finite Gaussian quasimodes would then provide exact radical comparison sources with absolutely summable exterior couplings.

That backup was not promoted to a theorem or completed: the submitted output-splitting proof is stronger, shorter, and already uses established manuscript inputs. No additional quasimode or spectral-gap claim is needed for the accepted result. The direct exterior-tail approach for the actual prolate source remains unsuitable for separate unsigned prime/pole estimates, whose naive norms diverge.

## Next concrete sign test

At lambda=3, use the now positive full complement beyond N=256 in the exact signed Schur matrix F-B* T^(-1) B, with certified inverse-action residuals and both parity sectors. Positivity of a smaller finite section or the source residual must not replace this correction. A successful fixed-window certificate would still need a separate argument for growing windows before contributing a G2 conclusion.
