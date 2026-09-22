# Internal scope and algebra review — NS-34 / v1.50

This is an internal analytic check, not a numerical certificate or the
separate independent NS-37 review. No new numerical gate is involved.

1. The work was claimed at 38324b5 on an isolated worktree based on 70eb2bb.
   NS-31, NS-35, NS-36 and NS-37 are separately owned and coordinated.
2. h is the explicit unnormalized E(H)(exp x), not an inferred ground or
   the actual finite-window source. Normalizing h on I_a is harmless by
   homogeneity, but all displayed constants use the unnormalized h.
3. Poisson evenness is inherited from the Fourier-invariant H with H(0)=0
   and integral H=0. Each summand is positive for x>=0; reflection covers
   x<0. On finite closed intervals h and 1/h are smooth and bounded.
4. The n=1 lower bound and all-integer Gaussian upper bound give A_-/A_+
   = (2*pi-3)/(4*pi). Taking x-log(2) over x yields prefactor 2^(-9/2)
   and exponent (3*pi/4)*exp(2x). With w_2=log(2)/sqrt(2), kappa is
   (2*pi-3)*log(2)/(128*pi), with no missing edge factor two.
5. Mellin(H)(z)=z(z-1)*pi^(-z/2)*Gamma(z/2)/sqrt(3). Multiplication by
   zeta(z) follows first for Re z>1; analytic continuation is justified by
   the proved two-sided decay. At z=1 the value is 1/sqrt(3). No zero
   location, RH or numerical zeta value is used.
6. Radicality is the existing unconditional arithmetic radical identity,
   not a positivity assertion. Its compact-test distributional consequence
   yields H_infinity h=-2 I_h cosh(x/2); all pointwise prime and continuous
   expressions converge locally. No global positive Weil operator is assumed.
7. Picone is applied with finite prime partial sums before convergence.
   The transformed positive edges and weighted potential sums converge for
   compact f; no divergent unweighted prime diagonal is subtracted in the
   limit. The proof does not extend the formula to arbitrary noncompact
   ratios f/h with infinite separate terms.
8. Full pole = 2|<f,c>|^2 - 2|<f,s>|^2. With nu=ch/I_h, the first pole
   and negative potential produce -(2/3) Var_nu. The negative sinh square
   survives in odd parity; evenness alone removes it only in the even sector.
9. Exterior T_a has positive contributions from both orientations of every
   excluded prime edge and the continuous kernel. E_global=E_interior+
   integral(T_a/h)|f|^2. Since n>=exp(2a) has both shifted endpoints outside
   for interior x when appropriate to that orientation, the identity matches
   the original strict-cutoff form. Endpoint equalities have zero measure.
10. Closing on each fixed-window core is valid because c/h and h,1/h are
    bounded there. The positive exterior energy is controlled by the global
    transformed energy, so (r_a)+ and (r_a)- terms are finite on the domain.
11. The actual source constraint is integral h*g*conj(u_a)=0, not a nu-mean
    condition. Two complex dimensions in the even test space suffice to
    impose this one complex linear condition. Odd vectors are orthogonal
    to every even source. No approximate projection calculation is used.
12. The bump band halfwidth b=log(2)/16 keeps it disjoint from its prime-2
    translates. For t=a-2log(2), the selected inward edges stay in I_a.
    Each nonzero endpoint has zero opposite endpoint, so its edge energy
    equals a positive weighted |f(x)|^2 with no unknown cross term.
13. The original-form upper bound covers all unit mixtures: the Fourier
    parity multiplier is at most sqrt(2), Cauchy-Schwarz sums the two fixed
    bump transforms, |C_a|<=2P, Lambda(n)<=log n, and the full even pole
    is <=2a+exp(a). The negative odd pole only improves this upper bound.
14. The sufficient capacity form is exactly q - (r_a)+ - delta E_interior.
    Its negative direction does not identify a negative direction of q.
    eta>=0 is explicit before taking the positive part of the bound.
15. The theorem forbids a fixed delta>0 and deleting prime-2 for this h.
    It does not forbid delta=0, retaining every edge, a different weight,
    or the original concentration/capacity criterion. No blanket no-go.
16. CAE is named openly as the existing bounded-floor requirement in new
    coordinates, with both parities and the source residual. The conditional
    RH implication is inherited from v1.36, not asserted achieved here.
17. Only elementary symbolic estimates enter the new proof; no floating
    value, interval gate or two-precision experiment is being represented.
    The constants A and a_0 are defined analytically, not fitted.
18. The broad ground-state method and Gaussian zeta kernel are classical.
    The archive establishes the particular scoped comparison obstruction;
    worldwide novelty and publication readiness are not claimed.

19. NS-37 independent review found no MAJOR. M1's rescaling wording is now
    explicit: h->k h entails g->g/k and I_h->k I_h; 2 I_h^2 Var_nu(g)
    is invariant, whereas the displayed 2/3 is tied to the frozen scale.
    M2's eta>=0 hypothesis was added before the final reviewed wording.
20. Fixed-window closure is spelled out through J_h=q_a+V_a with V_a a
    bounded ordinary L2 form. The shifted form norms agree up to constants
    depending on a, which suffices for domain identification, not uniform
    cofinal estimates. The squared-edge map gives the nonnegative integral
    on this closure. No global closed positive Weil realization is assumed.
