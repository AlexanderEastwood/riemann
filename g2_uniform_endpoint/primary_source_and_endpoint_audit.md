# Large windows and the actual continuum endpoint: primary-source audit

Starting point: complete manuscript v1.17. This report separates cited theorems from deductions checked here. No finite experiment is used to justify an asymptotic assertion.

## Main findings

1. A lower bound for the actual lowest semilocal eigenvalue of the form mu_lambda >= -epsilon(lambda), epsilon(lambda)->0 along any unbounded sequence, is already equivalent to RH. It is not a weaker analytic condition whose proof can be inferred from bounded-window certificates.
2. Every eigenfunction of the canonical fixed-window Weil operator has a continuous representative that is zero at both physical endpoints. The boundedness gate needed for the available logarithmic-Laplacian boundary theorem can be proved by the small-jump resolvent argument supplied by the endpoint agent and independently audited below.
3. The latter conclusion concerns actual continuum eigenfunctions. It does not contradict nonzero finite ground-vector endpoints, nor the repaired source's nonzero endpoint. It prevents using the actual continuum ground value as a nonzero boundary normalizer.

## Precise primary sources and what they establish

- [Connes–Consani–Moscovici, *Zeta Spectral Triples*, Section 3](https://arxiv.org/html/2511.22755v1#S3): formula (3.19) gives the canonical form and its archimedean Fourier symbol; Theorem 3.6 establishes discrete semibounded spectrum. Formula (3.27) records monotonicity of the bottom under enlarging support; Corollary 3.8 states that a zero limiting bottom implies RH. Section 5's finite boundary evaluation and ground construction do not assert a nonzero pointwise endpoint for the actual continuum eigenfunction.
- [Suzuki, *Weil's quadratic form via the screw function*, Theorem 1.1 and Corollary 1.2](https://arxiv.org/html/2606.09096v2#S1.SS2): the canonical operator is the Friedrichs realization, and its spectral bottom is the infimum over compactly supported smooth tests. Theorem 1.3 proves continuity in window size. Theorem 1.4 gives simple even ground states for sufficiently small windows, not a large-window lower bound. The positive metric in (1.9) uses a shift already known to lie below the actual bottom.
- [Burnol, *Sur les Formules Explicites I: analyse invariante*, Theorems 3.3 and 3.7, pp. 5–6](https://arxiv.org/pdf/math/0101068): the conductor-operator identity explains the local explicit-formula terms; Theorem 3.7 proves positivity for some sufficiently short compact multiplicative support. It supplies neither positivity for arbitrary support nor the needed large-window estimate. Essential self-adjointness of a local conductor operator is not positivity of the global semilocal Weil form.
- [Chen–Weth, *The Dirichlet Problem for the Logarithmic Laplacian*, Theorem 1.1](https://arxiv.org/pdf/1710.03416): the Fourier symbol of L_Delta is 2 log|t| and its singular-integral constants in one dimension are c_1=1 and rho_1=-2 gamma. Their Theorem 1.11 already gives vanishing boundary values for bounded weak solutions with bounded right-hand side, with every logarithmic exponent below 1/2.
- [Hernández-Santamaría–López Ríos–Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*, Theorem 1.1, p. 2](https://arxiv.org/pdf/2401.18033): on a bounded domain satisfying an exterior uniform sphere condition, a bounded weak zero-exterior solution with bounded right-hand side is continuous on the whole space and satisfies |u(x)|<=C ell(dist(x,boundary))^(1/2), where ell(r)=1/|log(min(r,0.1))|. Their Hopf lower bound, Theorem 1.4, additionally requires a nonnegative supersolution; that hypothesis is not asserted for a Weil eigenfunction.

## Deduction A: the eventual lower-bound target is RH-equivalent

Let q be the fixed global Weil form in centered logarithmic coordinates. Let Omega_a=(-a,a), a=log(lambda), and define

    m(a)=inf{q[f]/||f||_2^2 : 0 != f in C_c^infinity(Omega_a)}.

The primary form-core result identifies this infimum with the lowest eigenvalue of the canonical operator. Since the test spaces are nested,

    a<b  =>  m(a)>=m(b).

Suppose a_j->infinity and m(a_j)>=-epsilon_j with epsilon_j>=0 and epsilon_j->0. Fix any compactly supported smooth f. For every sufficiently large j its support is inside Omega_{a_j}, so

    q[f]>=-epsilon_j ||f||_2^2.

Letting j increase proves q[f]>=0. Weil's positivity criterion gives RH. Equivalently, for each fixed a, nesting directly gives m(a)>=m(a_j)>=-epsilon_j, hence m(a)>=0.

Conversely, RH implies positivity of q on every compactly supported smooth test, so m(a)>=0 for every a and the proposed bound holds with epsilon_j=0. Thus these are equivalent:

- RH;
- m(a)>=0 for every a>0;
- there exists any cofinal sequence of windows with m(a_j)>=-o(1);
- liminf_{a->infinity}m(a)>=0.

The manuscript's already proved trial vectors with Rayleigh quotient tending to zero give the additional upper bound m(a)<=o(1). Combined with the preceding equivalent conditions this yields m(a)->0, but the upper bound alone supplies no positivity.

The precise contrapositive is useful: if RH fails, one fixed compact smooth test has q[f]/||f||^2=-delta<0. Every window containing its support then has m(a)<=-delta. Increasing the window cannot wash out that fixed negative witness.

The lambda=3 certificate propagates positivity to all smaller windows by nesting. For larger windows it supplies an upper bound on the bottom, not a lower bound. This explains exactly why more isolated positive computations do not prove the eventual lower-bound target.

## Deduction B: the exact physical operator is a bounded perturbation of half the Dirichlet logarithmic Laplacian

Fix a>0 and Omega=(-a,a); all functions are extended by zero outside Omega. Use the unitary Fourier convention with multiplier 1/(2 pi) in Parseval. The archimedean symbol of the Weil operator is

    m_infinity(t)=Re psi(1/4+it/2)-log(pi).

Put

    r(t)=Re psi(1/4+it/2)-log(|t|/2),
    k(x)=(1/(2 pi)) integral_R r(t) exp(itx) dt.

The digamma asymptotic gives r(t)=O(t^-2) at infinity. Near zero it is -log|t|+O(1), which is integrable. Thus r belongs to L1(R), and k is bounded and continuous. Consequently the exact canonical operator is

    W_Omega = (1/2)L_Delta,Omega + K_Omega,

where

    K_Omega = -log(2 pi) I + P_Omega(k*)P_Omega + Pi_Omega - P_arith.

Here Pi_Omega has integral kernel 2 cosh((x-y)/2), and

    (P_arith u)(x)
       = sum_{1<m<exp(2a)} Lambda(m)/sqrt(m)
            [u(x+log m)+u(x-log m)].

The full-length endpoint shift may be included or omitted: it is zero almost everywhere. All shifts use zero extension. The sum is finite at each fixed a.

Every term in K_Omega is bounded on both L2(Omega) and L-infinity(Omega). For example, the convolution remainder has norm at most |Omega| ||k||_infinity on either space; the arithmetic shift norm is at most twice the finite sum of its weights. The pole kernel is bounded on the compact square. These constants need not be uniform in a.

The identity first holds on compact smooth tests and then for the closed forms by their common form core. Bounded self-adjoint perturbation gives the canonical operator identity and equality of operator domains. In particular, this is the restricted, zero-exterior logarithmic Laplacian, not the spectral logarithm of a periodic or Dirichlet differential Laplacian.

## Deduction C: independent audit of the missing boundedness gate

The following is the endpoint agent's small-jump argument, checked here with the physical constants and domains.

For 0<epsilon<1 define the nonnegative killed-jump operator A_epsilon by the closed Dirichlet form

    e_epsilon[u]
       =(1/4) integral_R integral_{|x-y|<epsilon}
                      |u(x)-u(y)|^2/|x-y| dy dx,

with zero exterior values. Its formal action inside Omega is

    A_epsilon u(x)
       =(1/2) integral_{|h|<epsilon}[u(x)-u(x+h)]/|h| dh.

Define the bounded integral operator

    J_epsilon u(x)
       =(1/2) integral_{y in Omega, |x-y|>=epsilon}
                         u(y)/|x-y| dy.

The exact one-dimensional identity is

    (1/2)L_Delta,Omega
       =A_epsilon+[log(1/epsilon)-gamma]I-J_epsilon.

The coefficient is -gamma because rho_1=-2 gamma before dividing by two. Both J_epsilon and the scalar term are bounded on L2, so this identity also fixes the operator domain. Moreover,

    ||J_epsilon u||_infinity
       <=sqrt(|Omega|)/(2 epsilon) ||u||_2.

For b>0 the resolvent R_b=(A_epsilon+bI)^(-1) has L2 norm at most 1/b. It is positive and has L-infinity norm at most 1/b. One can prove the latter without citing a semigroup theorem: for real bounded f, test the weak resolvent equation with (u-||f||_infinity/b)_+ and its negative counterpart. The Markov truncation inequality makes the jump contribution nonnegative, forcing both excesses to vanish. Positivity then gives the complex-valued estimate as well. Thus the L2 and L-infinity realizations agree on their intersection.

Let W_Omega u=mu u. Choose epsilon so small that

    b=log(1/epsilon)-gamma-mu
       >max(||K_Omega||_{2->2}, ||K_Omega||_{infinity->infinity}).

The eigen-equation becomes

    (A_epsilon+bI+K_Omega)u=J_epsilon u,

or

    (I+R_b K_Omega)u=R_b J_epsilon u.

The right-hand side belongs to L2 intersect L-infinity. The same Neumann series for (I+R_b K_Omega)^(-1) converges in both norms. Its L-infinity limit and L2 limit agree, and uniqueness of the L2 solution identifies that limit with the original eigenfunction u. Therefore every eigenfunction is bounded. No positivity, simplicity, parity, or sign of mu was used.

A crude quantitative bound is

    ||u||_infinity
       <=sqrt(|Omega|)/(2 epsilon [b-||K_Omega||_{infinity->infinity}]) ||u||_2.

It is adequate to prove boundedness at each fixed window; it is not advertised as a useful growing-window estimate.

## Deduction D: genuine continuum eigenfunctions have zero physical endpoint

The preceding boundedness gives a bounded right-hand side in

    L_Delta,Omega u=2(mu u-K_Omega u).

The canonical form domain is the zero-exterior logarithmic-Laplacian energy space. An interval has the exterior uniform sphere property. All hypotheses of the cited optimal boundary theorem now hold. Thus every eigenfunction has a continuous representative on R, with

    |u(x)|<=C_{Omega,u}/sqrt(|log(min(dist(x,boundary Omega),0.1))|),
    u(-a)=u(a)=0.

For complex eigenfunctions, apply the real theorem to the real and imaginary parts. Passing back through x=log(u_physical) preserves the zero value at u_physical=lambda and lambda^-1. Translating to the manuscript's [0,L] coordinate preserves it as well; there is no phase or scale that turns zero into a nonzero endpoint.

This closes a qualitative endpoint-regularity question but changes the target: the repaired source has its separately proved nonzero B_lambda, whereas the actual continuum ground has ordinary trace zero. Multiplying that continuum ground by any finite nonzero scalar cannot produce the source's nonzero ordinary endpoint. A comparison requiring their nonzero endpoint values to agree is therefore false in this literal continuum form.

The theorem does not say that every finite Ritz ground endpoint is zero. Its exact noncancellation argument proves the opposite at each finite cut under the specified finite hypotheses. Neither ordinary norm nor the canonical graph norm controls endpoint evaluation, so the two statements are compatible.

No Hopf lower bound is used. The full Weil operator contains arithmetic and pole terms with signs; the nonnegative supersolution hypothesis in the logarithmic-Laplacian Hopf theorem must not be inserted silently. Nor does the upper boundary estimate prove that sqrt(log(1/d))u has a nonzero limit. A renormalized boundary functional would require a new definition and proof and cannot replace the manuscript's physical endpoint automatically.

## Additional elementary diagnostic: endpoint evaluation is graph-unbounded

In the normalized translated Fourier basis, choose the even shell I_N={n:N<=|n|<=2N}, of size M_N=2(N+1), and put

    f_N=(sqrt(L)/M_N) sum_{n in I_N} V_n.

Then the physical endpoint is exactly one, but ||f_N||_2^2=L/M_N. Since W=diag(d)+bounded and d_n=log|n|+O_L(1),

    ||W f_N||_2 <= C_L log(2N) sqrt(L/M_N) ->0.

Hence f_N tends to zero even in the canonical operator graph norm while its endpoint stays one. This explicitly rules out any generic estimate of endpoint error by ordinary norm or this graph norm alone. It preserves, rather than removes, the need to track the sampler's physical endpoint and explicit graph defect.

## Next concrete work

The global spectral lower-bound obligation remains RH-equivalent and unproved. The endpoint result is a proved correction of an incompatible normalization target. A viable next step is to keep the finite physical endpoint and its cutoff dependence explicit, or to define a different continuum boundary datum and independently establish its relation to the finite endpoint. Either choice must retain the common finite object, graph defect, and full-strip normalization. None follows solely from the new fixed-window ground-state angle.
