# v1.37 — an arithmetic no-go for bounded scalar primitive budgets

**Status:** proved obstruction to a previously proposed route. No G2 sign gap was closed. RH is not proved. Delivery is LaTeX only.

## Question tested

The v1.36 reduction made a uniform finite ordinary-norm lower floor sufficient. That relaxed the earlier o(1) target and required retesting the v1.34 primitive mechanism rather than simply retaining its old rejection.

For the complete physical symbol beta_a, define

    Delta_a = sup_{x<y} (−integral_x^y beta_a(xi) dxi)_+.

The previous proved estimate is q_a[f] >= −a Delta_a ||f||². Could a Delta_a stay bounded along a cofinal family?

**Answer: no. The new proof establishes a Delta_a -> infinity unconditionally for the actual arithmetic symbol.** It also establishes inf_xi beta_a(xi) -> −infinity. A linear rate is only proved conditionally on RH.

## Exact setting and scope

- a=log(lambda), T=2a, I_a=(-a,a), ordinary norm in L2(I_a,dx), first-slot-linear convention.
- Complete canonical closed physical Weil form, domain integral log(2+|xi|) |F(xi)|² dxi < infinity, where F is the unitary Fourier transform of zero extension.
- No finite Fourier cutoff is introduced. All prime powers with log n<T appear with weight Lambda(n)/sqrt(n), with the strict endpoint convention.
- beta_a is exactly Re psi(5/4+i xi/2) − log pi − r_a(xi), including the continuum term of v1.30 and the full both-parity identity of v1.35. It is not the raw prime-comb symbol.
- The result concerns scalar sufficient bounds on the full physical space. It neither identifies C_a^low with the source complement nor supplies a bound on either complement. Both parity blocks and all required couplings remain obligations.

## Proof mechanism

Choose delta=1/100 and a fixed even positive smooth mollifier kappa supported in (−delta,delta), with integral1. Set

    w = 1_[pi,3pi] * kappa,
    H(t) = integral w(s) exp(−its) ds,
    K(u) = integral_[−1,1] H(t) exp(iut) dt.

Then w>=0, integral w=2pi, ||w'||_1=2, H(±1)=0, K(u)=O((1+u²)^−1), and K(0)<−1/(3pi). The sign follows analytically from

    integral_pi^(3pi) sin(s)/s ds
      = −pi integral_0^pi sin(u)/[(pi+u)(2pi+u)] du <= −1/(3pi),

plus the 1/2 Lipschitz bound for sinc and the mollification error pi/100. All constants are fixed before the window grows.

Assume RH temporarily and fix a zero ordinate gamma0 of multiplicity m0. The explicit formula gives the exact identity

    J_a = integral beta_a(xi) w(T(xi−gamma0)) dxi
        = sum_gamma m_gamma K(T(gamma−gamma0)) + E_T,

    |E_T| <= 8pi exp(−5T/2) / [5T(1−exp(−2T))].

There is no omitted 2pi or T factor. The inverse-transform kernel outside |t|<=T is precisely −exp(−5|t|/2)/(1−exp(−2|t|)), from the 5/4 reference multiplier. The transform of the probe is T^−1 exp(−i gamma0 t) H(t/T). Inside the cutoff, the complete geometric distribution and both pole signs are retained.

The endpoint zeros make the truncated test continuous and piecewise smooth, with its second derivative a finite measure. Mollification extends the smooth explicit formula to this test with a uniform O((1+|gamma|)^−2) zero-sum majorant at fixed T. If exp(T) is a prime power, its endpoint atom pairs with zero. Isolation of gamma0 and N(Y)=O(Y log Y) give

    J_a = m0 K(0) + O_gamma0,w(T^−2) + E_T <= −1/(6pi)

eventually. The last inequality is RH-conditional.

The optimal scalar primitive decomposition beta_a=b_a+U_a', b_a>=0, ||U_a||∞=Delta_a/2 gives J_a>=−Delta_a, because the probe has variation2. Its mass is pi/a. Thus, under RH,

    Delta_a >= 1/(6pi),
    inf beta_a <= −a/(6pi²)

eventually. The threshold is not claimed effective here.

Now suppose a Delta_a were bounded on any cofinal sequence. The old primitive inequality would give a complete ordinary uniform lower floor; v1.36 would imply RH. The preceding RH-conditional estimate would then contradict that same bounded sequence. This proves a Delta_a -> infinity unconditionally. The identical contradiction, using the full symbol identity, excludes any cofinal pointwise lower bound beta_a>=−C and proves inf beta_a -> −infinity.

This is not circular: RH is first a consequence of the hypothesized scalar certificate, and is then used to disprove that certificate. We do not assume RH to obtain an unconditional sign for the physical form.

## Adversarial checks and limits

An independent reviewer checked the explicit-formula extension, all Fourier factors, the reference multiplier's exterior tail, the strict prime cutoff at resonance, multiplicity and the cofinal contradiction. See adversarial_review.md.

The nonnegative frequency probe is **not** asserted to equal |F|² for a physical Paley–Wiener transform supported in I_a. Under RH its negative pairing therefore does not contradict Weil positivity. This is precisely why a scalar frequency comparison can fail while a support-constrained operator comparison survives.

The script check_probe.py checks the rational gate 6*(22/7)²<100 and gives independent binary64 quadrature diagnostics of the probe and a single spectral atom at T=2,7,19,100. These T values are abstract scaling tests, not new arithmetic windows. The approximate K(0) is −0.35434715073059375. Numerical quadrature is not an interval certificate and is not used as the proof of the theorem. No lambda=8 calculation was attempted. An initial attempt to use mpmath found that package unavailable; the diagnostic was rewritten using the standard library. The analytic proof is independent of that implementation choice.

No unconditional linear rate for Delta_a or inf beta_a is asserted. The unconditional conclusions are the two divergent limits. The theorem does not rule out all matrix-valued metrics, signed concentration estimates, or symbol modifications with a separately proved physical error bound.

## Candidate register and novelty audit

**ID:** G2.6-PT-01b, retest of PT-01 under the v1.36 finite-floor reduction.

**Precise proposed sufficient estimate:** sup_j a_j Delta(beta_a_j)<infinity, a_j->infinity. **Status: rigorously ruled out.** The related scalar pointwise estimate inf_j,xi beta_a_j(xi)>−infinity is also ruled out.

**Nearest prior proposal:** v1.34 optimal signed-primitive/Bernstein estimate, previously rejected as an o(1) mechanism using a Dirichlet model and finite diagnostics. Those tests did not settle the relaxed O(1) objective. The new ingredient is an endpoint-vanishing positive probe and the absolutely convergent actual zero-sum identity; it proves divergence for the arithmetic symbol rather than fitting a few windows or changing a constant.

**Other prior routes:** this is not a renamed Schur or structured inverse, scalar prime norm, finite-rank metric repair, source-only small-residual argument, dyadic pair norm, common-Gram off-block factorization, Picone transform, or a new concentration criterion. It closes a scalar simplification of the surviving signed concentration route. It does not revive the negative-only Schatten, commuting-channel, Cotlar, point-value repair, or raw-transfer shortcuts.

**Primary-literature screen (September 21, 2026):**

- [Burnol, Sur les Formules Explicites I: analyse invariante (2000), Theorem2.1](https://arxiv.org/abs/math/0101068): classical explicit-formula foundation and normalization; our limited-regularity extension is supplied by the mollification argument.
- [Suzuki, Weil's quadratic form via the screw function, v2](https://arxiv.org/html/2606.09096v2): nearby finite-window operator setting, not a source of this scalar divergence claim.
- [Zhu, Weil positivity in compact windows, v2, September2,2026](https://arxiv.org/html/2608.24827v2), Sections3 and14: a nearby envelope/cutoff barrier bounds the raw prime comb by its total mass. Our calculation uses the continuum-cancelled beta_a and a negative truncated spectral-atom mass to exclude bounded optimal primitive errors. We do not use its numerical certificates or assert a new priority over general cutoff oscillation theory.

The obstruction is new within the inspected project log. The ingredients are classical; worldwide novelty remains unresolved. It is registered as a proved no-go, not as a new live positive mechanism.

## Remaining target

Retain the signed source-compressed concentration estimate

    −D_a P_a + sum_j w_a,j C_a,u(G_a,j) >= −C_* P_a,

with one finite C_* along a cofinal family, plus the full odd block and any physical blocks/couplings not subordinate to this projection. Here P_a=I−|u_a><u_a| is the actual ordinary source-complement projection and C_a,u is the physical concentration operator. The new theorem says that the primitive budget and the minimum of the scalar symbol cannot supply C_*; favorable and unfavorable frequency levels must be controlled jointly on the physical transform image.

The next concrete lemma is a uniform signed estimate for that joint operator, retaining off-diagonal concentration interactions rather than replacing it by a scalar drawdown or pointwise envelope. No arithmetic proof of this lemma is supplied here. **No G2 gap was closed; RH remains open.**
