# Absolute operator residual for the repaired source and its literal finite projection

Status: analytic proof internally reviewed by adversarial_g2 with no blocking error found, September 21, 2026. This is internal review, not external referee approval. This closes ordinary-norm Rayleigh/residual prerequisites if accepted. It does not identify a ground state, establish G2, or control endpoint-normalized graph defects.

## Claimed result and exact normalization

Use precisely the repaired fixed-order n=0,4 source, physical Hilbert norm L2(du/u), first-slot-linear convention, and canonical semilocal Weil operator W_lambda of manuscript v1.14. Put

    c=2*pi*lambda^2,  L=2 log(lambda),
    N=ceil(lambda^8(1+L)),  k_lambda=P_N p_lambda.

There are fixed positive C,c0 and a sufficiently-large-lambda threshold such that

    c0 <= ||p_lambda||, ||k_lambda|| <= C,
    ||W_lambda p_lambda|| + ||W_lambda k_lambda||
       <= C lambda^6 exp(-c/3).

In particular, the finite compressed matrix obeys

    ||W_{lambda,N} k_lambda|| <= C lambda^6 exp(-c/3).

After ordinary unit normalization u_lambda=p_lambda/||p_lambda||, and likewise for k_lambda, both

    alpha_lambda=<W_lambda u_lambda,u_lambda> ->0,
    ||(W_lambda-alpha_lambda)u_lambda|| ->0,

with the same exponential estimate up to a constant. The bound concerns the full unweighted output norm. No division by the exponentially small physical endpoint is made.

## Inputs from the existing manuscript

1. Exact compact-source radicality and the pole/prime/archimedean estimates yield the uniform Sobolev inequality (Proposition g1-sobolev):

       |<W_lambda p_lambda,v>| <= C |B_lambda| r(lambda)
          [||v||+||D_log v||+|v(-a)|+|v(a)|]

   for every periodic H1 test v. The constant is independent of v and lambda. This already includes the full zero moment, the zero-value repair, the exterior co-Poisson tail, and inversion averaging. It is the only place where the global radical identity is used below.
2. Endpoint size: |B_lambda| <= C lambda^(11/2) exp(-c), and r(lambda) is bounded for sufficiently large lambda.
3. The actual closed operator is D_d+[M_b,H], with commutator norm <=C lambda; d_n satisfies

       |d_n| <= C[lambda+1+log(2+|n|/L)].

   Its off-diagonal entries satisfy |W_nm|<=C lambda/|n-m|. Every BV proxy is in its operator domain, and finite Fourier sums form an operator core.
4. The v1.14 polynomial-endpoint theorem also supplies the uniformly quantified coefficient tail

       |hat p_lambda(n)| <= C |B_lambda| lambda sqrt(L)/|n|,
       |n|>N=ceil(lambda^8(1+L)).

   The same exact vector and matrix are used throughout.

No independent sign, spectral gap, positivity, ground overlap, or RH assumption is added.

## 1. An explicit nonzero limiting source

The only external input needed for the norm lower bound is the uniform fixed-mode Hermite approximation in Connes--Consani--Moscovici, Zeta Spectral Triples, Lemma 7.2:
https://arxiv.org/html/2511.22755v1#S7
It gives suitably normalized n=0,4 modes q_{n,lambda} with sup_{|u|<=lambda}|q_{n,lambda}(u)-H_n(u)|=O(lambda^-2). The following normalization and co-Poisson estimates are derived here.

The fixed Hermite functions are normalized in L2(R). To replace the suitable normalization by the manuscript's exact unit norm, expand the squared norm:

    ||q_n||^2 - 1 = -integral_{|u|>lambda}|H_n|^2
       +2 Re integral_{-lambda}^lambda H_n conjugate(q_n-H_n)
       +integral_{-lambda}^lambda |q_n-H_n|^2 = O(lambda^-2).

The cross term uses the fixed L1 norm of H_n, and the last term is O(lambda^-3). Consequently division by ||q_n|| preserves the uniform O(lambda^-2) rate, rather than merely the weaker O(lambda^-3/2) estimate obtained by a triangle inequality.

Since the two Fourier eigenvalues chi_n tend to one exponentially fast, the actual coefficients converge at rate O(lambda^-2) to

    a_0^infinity = -H_4(0) = -sqrt(3)/(2*2^(1/4)),
    a_4^infinity = H_0(0) = 2^(1/4).

Thus the raw physical source and, after its exponentially small fixed repair, the exact source satisfy

    sup_{|u|<=lambda}|tilde h_lambda(u)-h_infinity(u)|<=C lambda^-2,
    h_infinity(u)=(4*pi/sqrt(3))*u^2*(2*pi*u^2-3)*exp(-pi*u^2).

The displayed scalar is important: h_infinity is 8/sqrt(3) times the h in CCM equation (7.1). It follows directly by using

    H_0=2^(1/4) exp(-pi*u^2),
    H_4=(16*pi^2*u^4-24*pi*u^2+3)/(2*2^(1/4)*sqrt(3))*exp(-pi*u^2).

The limiting source has h_infinity(0)=0, integral zero, and Fourier eigenvalue +1, being a combination of Hermite modes 0 and 4.

Define f_infinity=E(h_infinity). Poisson summation with both zero moments gives J f_infinity=f_infinity. Gaussian decay and this inversion identity imply f_infinity belongs to L2(du/u).

## 2. Global ordinary-norm convergence and a lower bound

For lambda^-1<=u<=lambda, there are at most lambda/u compact-source summands. The source approximation therefore gives

    |sqrt(u) sum_{n*u<=lambda} [tilde h_lambda(nu)-h_infinity(nu)]|
       <= C lambda^-1 u^-1/2.

Squaring and integrating du/u yields an O(lambda^-1) squared norm, because

    lambda^-2 integral_{lambda^-1}^{lambda} u^-2 du <= C lambda^-1.

The omitted Gaussian terms with nu>lambda have L2 norm bounded by a polynomial in lambda times exp(-pi*lambda^2). To see this uniformly in u, bound the decreasing Gaussian-polynomial tail by its first term plus u^-1 times its integral; multiply by sqrt(u), then integrate on the window. The Gaussian tail outside the window for f_infinity is bounded in the same way, with inversion handling u<lambda^-1.

Inversion averaging is an L2 contraction, and f_infinity is inversion-even. Therefore, after extension by zero outside I_lambda,

    ||p_lambda-f_infinity||_{L2(R_+,du/u)} <= C lambda^-1/2.

This provides both an ordinary-norm upper bound and an explicit positive eventual lower bound. For u>=1, every summand h_infinity(nu) is positive, hence

    ||f_infinity||^2 >= integral_1^2 h_infinity(u)^2 du >0.

One may take

    c0=(1/4)*(integral_1^2 h_infinity(u)^2 du)^(1/2)

for all sufficiently large lambda. An even more elementary explicit positive lower bound is

    c0 >= [pi/sqrt(30)]*(2*pi-3)*exp(-121*pi/100),

obtained on u in [1,11/10]. This lower bound is asymptotic in lambda; no numerical threshold is claimed.

## 3. The polynomial input tail is tiny in operator graph norm

Write e=(I-P_N)p_lambda, with N as above. The coefficient tail gives

    ||e|| <= C |B_lambda| lambda sqrt(L/N).

The diagonal bound and the elementary integral comparison

    sum_{n>N} [1+log(2+n/L)]^2/n^2
      <= C [1+log(2+N/L)]^2/N

give

    ||D_d e|| <= C |B_lambda| lambda sqrt(L/N)
                     [lambda+1+log(2+N/L)].

The commutator norm is O(lambda), so

    ||W_lambda e|| <= C |B_lambda| lambda sqrt(L/N)
                     [lambda+1+log(2+N/L)]
                  <= C |B_lambda| lambda^-2.

Here N>=lambda^8(1+L), L grows only logarithmically, and log(N/L)=O(log lambda). In particular k_lambda has the same positive norm lower bound for a common sufficiently large lambda threshold, and ||k_lambda|| is bounded. This is a uniform graph approximation result for this specific sequence, stronger than the previous fixed-window operator-core statement.

## 4. Low-output control from the exact radical estimate

Use an auxiliary output cutoff M, distinct from the actual finite source cutoff N. For v=P_M v with ||v||=1,

    ||D_log v|| <= 2*pi*M/L,
    |v(-a)|+|v(a)| <= 2 sqrt((2M+1)/L).

The Sobolev radical estimate thus implies

    ||P_M W_lambda p_lambda||
      <= C |B_lambda| r(lambda)
          [1+M/L+sqrt(M/L)].

This estimate may be used for exponentially large M because the existing Sobolev statement has a constant independent of the test; this is not an unjustified extension of a fixed-band constant C_T. No derivative is placed on the nonsmooth source.

## 5. High-output control from the actual matrix

Assume M>2N. The diagonal has no contribution to Q_M W_lambda P_N. The exact off-diagonal bound gives the Hilbert--Schmidt estimate

    ||Q_M W_lambda P_N||^2
      <= C lambda^2 sum_{|m|<=N} sum_{|n|>M} 1/(n-m)^2
      <= C lambda^2 N/M.

Since ||p_lambda|| is bounded,

    ||Q_M W_lambda p_lambda||
      <= C lambda sqrt(N/M) + ||W_lambda e||
      <= C lambda^5 sqrt(1+L) M^-1/2
             +C |B_lambda| lambda^-2.

All prime, pole and archimedean pieces are present: the cross estimate uses the actual complete matrix, and its diagonal is treated through the graph-tail estimate. No separately divergent pole or prime sum is estimated absolutely.

## 6. Optimize the auxiliary split and normalize

Take M=ceil(exp(2c/3)). It is greater than 2N for large lambda. Then

    |B_lambda| r(lambda) M/L
       <= C lambda^(11/2) exp(-c/3),
    lambda^5 sqrt(1+L) M^-1/2
       <= C lambda^6 exp(-c/3).

The remaining terms are smaller. Combining the low and high estimates proves

    ||W_lambda p_lambda|| <= C lambda^6 exp(-c/3).

The graph-tail estimate gives the same bound for W_lambda k_lambda, and compression contractivity gives it for W_{lambda,N} k_lambda. Ordinary unit normalization is safe because of Section 2. For a unit candidate u,

    |alpha|=|<Wu,u>|<=||Wu||,
    ||(W-alpha)u||<=2||Wu||.

Consequently the Rayleigh value and full centered residual both tend to zero, without claiming that their associated spectral point is the bottom of the spectrum.

## Exact limitations and failed stronger inference

1. The auxiliary M is not a new finite matrix used for the source or endpoint. The actual candidate remains P_N p_lambda with N polynomial. M appears only in a proof splitting the output of the canonical infinite operator.
2. The absolute estimate does not vanish after endpoint normalization. Dividing the displayed bound by |B_lambda| produces an exponentially large upper bound of order exp(2c/3) times a polynomial. This is insufficient for the G2 source/graph pairing.
3. Even arbitrarily small residual and Rayleigh value say nothing about lowest-state overlap: diag(-1,epsilon) with candidate e_2 has residual epsilon at zero and exact Rayleigh epsilon, but overlap with the lowest eigenspace is zero. This obstruction persists for epsilon->0.
4. The inequality lambda_min<=alpha->0 is only an upper bound; it does not exclude a fixed negative eigenvalue. The separate large-support overlap/complement sign remains open.
5. This proof does not establish a uniformly small unbounded D_log W_lambda p_lambda norm. For finite compression, multiplying the residual by N/L gives an absolute bound but still does not repair endpoint normalization.
6. It would be invalid to estimate the infinite exterior prime and pole couplings separately by absolute L2 translation norms: those naive norm sums diverge. The proof instead retains the already-proved centered pole-prime cancellation through the Sobolev estimate and uses the bounded actual finite-window matrix for the high-output step.
