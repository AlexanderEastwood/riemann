# Adversarial review: the bounded scalar primitive route fails for the actual symbol

September 21, 2026. Reviewed against the complete v1.36 manuscript, in particular the exact continuum symbol, v1.34 primitive bound, full-parity extension, and v1.36 uniform-semiboundedness criterion. This report does not claim G2 or RH.

## Verdict

The proposed argument survives adversarial review after making the compact-test extension of the explicit formula explicit. It proves, for the actual arithmetic symbol,

    a Delta(beta_a) -> +infinity as a -> infinity.

This conclusion is unconditional. The stronger quantitative statement

    Delta(beta_a) >= 1/(6 pi),
    a Delta(beta_a) >= a/(6 pi)

for all sufficiently large a is proved **under RH only**. The unconditional conclusion uses a contradiction: a bounded cofinal subsequence would give RH through v1.34 plus v1.36, and the conditional estimate would then contradict that subsequence.

Thus replacing v1.34's previously requested vanishing primitive error by a merely bounded error does not revive that scalar route. This is a cofinal no-go for the actual arithmetic symbol, not only a countermodel. It does not disprove the signed physical concentration criterion.

## 1. Fixed probe and exact constants

Let delta=1/100. Choose any even nonnegative smooth mollifier kappa supported in [-delta,delta] with integral one; for example the normalized usual compact exponential bump. Define

    w(s) = (1_[pi,3pi] * kappa)(s).

Then w is nonnegative, smooth and compactly supported, its integral is 2 pi, and

    w'(s)=kappa(s-pi)-kappa(s-3pi),
    ||w'||_1=2.

The last equality is exact because the two endpoint supports are disjoint. Use the nonunitary Fourier convention

    H(t)=integral_R w(s) exp(-i t s) ds.

It gives

    H(t)=2 exp(-2 pi i t) sin(pi t)/t * kappa-hat(t),
    H(1)=H(-1)=0,
    |H(t)|<=2 pi.

Set

    K(x)=integral_-1^1 H(t) exp(i x t) dt.

Fubini gives the exact formula

    K(0)=2 integral_R sinc(s) w(s) ds,
    sinc(s)=sin(s)/s.

For the unmollified interval,

    C0=integral_pi^(3pi) sinc(s) ds
      =-pi integral_0^pi sin(u)/((pi+u)(2pi+u)) du
      <=-1/(3 pi).

Also sinc'(s)=-integral_0^1 t sin(ts) dt, hence |sinc'|<=1/2. Therefore mollification changes C0 by at most pi delta, and

    integral sinc(s)w(s) ds <=-1/(3 pi)+pi/100 < -1/(6 pi),
    K(0)<-1/(3 pi).

All these inequalities are analytic. They require no fitted numerical sine-integral values. The sign is compatible with w>=0 because the transform is truncated to [-1,1]; K is not a positive kernel.

Two integrations by parts, using H(+-1)=0, give K(x)=O((1+|x|)^(-2)). The implicit constant is fixed by this one probe and is independent of a and of the chosen zero.

## 2. Exact Fourier accounting and the reference archimedean tail

Let T=2a. Denote the original archimedean convolution distribution by D_ar, with multiplier

    Re psi(1/4+i xi/2)-log pi.

Away from the origin its kernel is

    -rho(t),   rho(t)=exp(|t|/2)/(2 sinh |t|).

The global explicit-formula distribution is

    D_global=D_ar - sum_m Lambda(m)/sqrt(m) (delta_log(m)+delta_-log(m))
                  +2 cosh(t/2).

Under RH this distribution equals sum_gamma exp(i gamma t), where every real ordinate is counted with multiplicity. Its Fourier multiplier is consequently 2 pi sum_gamma delta_gamma.

The v1.30 beta_a uses the **5/4** reference, not the 1/4 reference. The digamma recurrence adds the convolution kernel exp(-|t|/2). Thus its inverse multiplier distribution D_beta agrees with D_global on |t|<T. On |t|>T, it has only the kernel

    -rho_ref(t),
    rho_ref(t)=exp(-5|t|/2)/(1-exp(-2|t|)).

The exponent 5/2 matters. Reusing the original 1/4 archimedean tail without accounting for the added kernel would not give the stated exact decomposition.

Fix a real critical ordinate gamma0, of multiplicity m>=1. The probe in frequency is w_T(xi)=w(T(xi-gamma0)); its unnormalized inverse testing transform is

    V_T(t)=T^(-1) exp(-i gamma0 t) H(t/T).

In particular V_T(+-T)=0. Direct pairing with D_beta and the explicit formula yields

    J_T := integral_R beta_a(xi) w(T(xi-gamma0)) dxi
         = sum_gamma K(T(gamma-gamma0)) + E_T,

    E_T = -T^(-1) integral_|t|>T rho_ref(t)
                         exp(-i gamma0 t)H(t/T) dt.

There is **no missing factor 2 pi** in this formula. The factor appears in the full multiplier 2 pi sum delta_gamma and is already incorporated by the identity integral_R H(t)exp(ixt)dt=2 pi w(x). Truncating the t integral replaces that full transform by K. The factor T^(-1) in V_T is canceled by t=T s in the compact part.

Since |H|<=2 pi, the error obeys

    |E_T| <= 8 pi exp(-5T/2)/(5T(1-exp(-2T))).

This is exactly the proposed tail constant.

## 3. Eligibility of the compact test

The compact test is

    V_T(t) 1_|t|<=T.

It is continuous and piecewise smooth, because H(+-1)=0, but its first derivative generally has jumps at the endpoints. It must not be called a smooth test without explanation.

A rigorous extension is available. This compact test has a second distributional derivative which is a finite measure. Convolving with smooth compact approximate identities gives smooth tests with uniformly bounded second-derivative total variation and a common compact support. Their Fourier transforms have a uniform O_T((1+|gamma|)^(-2)) bound. Under RH, N(U)=O(U log U) makes the zero series absolutely summable with this majorant, permitting passage to the limit. On the geometric side, only finitely many prime atoms occur in the common support; near zero the test is smooth and the archimedean finite-part pairing converges. This proves the displayed exact identity for the piecewise-smooth test.

If T happens to equal log(m), the prime atom at the endpoint contributes zero because V_T(+-T)=0. Therefore the manuscript's strict prime cutoff is preserved and no half-weight convention is needed.

## 4. Isolating one critical zero under RH

For fixed gamma0, all other zero ordinates are separated from gamma0, and

    sum_(gamma != gamma0) 1/|gamma-gamma0|² < infinity.

This follows from discreteness near gamma0 and the usual zero-counting estimate at infinity. The K decay therefore gives

    sum_gamma K(T(gamma-gamma0))
      =m K(0)+O_gamma0(T^(-2)).

Consequently

    J_T -> m K(0) < -m/(3 pi),

and, for all sufficiently large T,

    J_T <= -1/(6 pi).

The eventual threshold depends on the fixed zero and probe and is not made effective here. The proof does not require simplicity or numerical isolation of gamma0. The realness of all other ordinates in this estimate is an RH assumption; using the same O(T^(-2)) estimate unconditionally would be an error.

## 5. Primitive comparison

For each fixed a, beta_a is smooth, bounded below, and tends to plus infinity as |xi| grows. Proposition v1.34 therefore gives a decomposition

    beta_a=b_a+W_a',   b_a>=0,   ||W_a||_infinity=Delta(beta_a)/2,

with the equality in the optimal-norm sense used in that proposition. Integrating against the nonnegative compact smooth w_T gives

    J_T >= -(Delta(beta_a)/2)||w_T'||_1
         = -Delta(beta_a).

The derivative norm is scale invariant: ||w_T'||_1=||w'||_1=2. There is no missing T factor. Combining this with the preceding bound proves, under RH,

    Delta(beta_a)>=1/(6 pi)

eventually. Multiplication by a supplies the claimed conditional linear divergence.

## 6. Unconditional cofinal conclusion

Suppose, toward a contradiction, a_j tends to infinity and a_j Delta(beta_(a_j))<=C for a fixed finite C. The v1.34 primitive estimate, now valid for both parities by the full-parity symbol identity, gives

    W_(a_j) >= -C I

on every complete physical form domain in this cofinal family. The v1.36 semiboundedness criterion therefore implies RH. The RH-conditional conclusion of Section 5 then gives

    a_j Delta(beta_(a_j)) >= a_j/(6 pi),

a contradiction. Since the existence of a bounded cofinal subsequence is exactly the negation of divergence to plus infinity for a nonnegative function, this proves unconditionally

    a Delta(beta_a) -> +infinity.

The proof does not assert an unconditional linear rate. It is logically valid to use RH after deriving it from the hypothesis being contradicted.

## 7. Pointwise scalar baseline also fails

The same probe has integral 2 pi/T=pi/a. Hence under RH,

    inf_xi beta_a(xi) <= J_T/(pi/a) <= -a/(6 pi²)

eventually. If a fixed finite scalar pointwise lower floor existed along a cofinal family, integration against squared physical Fourier transforms would give the v1.36 uniform lower bound, imply RH, and contradict this estimate. Thus inf beta_a tends to minus infinity unconditionally, again without the conditional linear rate being made unconditional.

This concerns unrestricted pointwise symbol comparison. It does not assert that the actual support-constrained physical Weil form has negative vectors. Under RH that form is nonnegative while these scalar-symbol troughs persist.

## 8. Scope and novelty

This result is a continuation and decisive falsification of the v1.34 scalar primitive proposal after v1.36 weakened the required error from o(1) to O(1). Its new ingredient is a nonnegative frequency probe with exact Fourier endpoint zeros and a negative truncated transform at the origin, combined with the full explicit formula. The old finite-window scans and the positive Dirichlet countermodel did not establish this actual-arithmetic cofinal obstruction.

The ingredients—explicit-formula localization, Fourier endpoint cancellation, integration by parts, and zero-counting summability—are classical. Worldwide novelty is unresolved and should not be asserted. This is not a new live positivity mechanism, and it does not rule out the signed concentration hierarchy, source-sensitive physical inequalities, or all matrix-valued metrics.

No G2 gap was closed. The uniform signed lower bound on the required physical complement remains open.
