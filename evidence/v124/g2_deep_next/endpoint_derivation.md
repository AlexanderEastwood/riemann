# Polynomial endpoint recovery for the literal repaired prolate projection

Status: new proof submitted to adversarial review, 2026-09-20. This is an asymptotic endpoint result, not G2, not a uniform spectral theorem, and not a practical certified cutoff constant. No sampler, finite matrix, Fourier normalization, or endpoint is changed.

## Proposed theorem

Let p_lambda be precisely the inversion-even, exactly repaired, fixed two-mode co-Poisson source of manuscript v1.13. Let L=2 log lambda, let B_lambda be its actual common one-sided physical endpoint, and use the original orthonormal Fourier projection P_N. Then for

    N_lambda = ceil(lambda^8 (1+L)),

one has

    |(P_{N_lambda}p_lambda)(0) - B_lambda| / |B_lambda| = O(1/lambda).

The exponent 8 is conservative. The result also holds with exponent 9 if extra slack is desired. Constants and the sufficiently-large-lambda threshold are not yet numerical. The endpoint 0 is the translated logarithmic endpoint, so evaluation has its indispensable L^{-1/2} normalization.

This would replace the existing nonquantitative/raw-BV endpoint selection by a polynomial cutoff for this exact source. It does not establish a positive complement at this cutoff, nor G2, nor graph convergence.

## Inputs already proved in the manuscript

Put c=2*pi*lambda^2 and

    g(x) = sqrt(lambda) h_lambda^circ(lambda*x)
         = a_0 psi_{0,c}(x) + a_4 psi_{4,c}(x),
    Bplus = g(1).

Extend each angular PSWF by its finite Fourier eigenrelation. The following inputs are needed, all for the fixed orders 0 and 4:

1. The coefficients a_j are O(1); concentration eigenvalues tend to 1. The Fourier eigenrelation gives an entire representation

       g(z) = integral_{-c}^c exp(i z t) dmu(t),   ||mu|| <= C lambda.

   This follows directly by changing variables in the finite Fourier eigenrelation, whose eigenvalue magnitude is asymptotic to sqrt(2*pi/c). No concentration tail asymptotic is differentiated.
2. Endpoint noncancellation and the radial bounds give

       |g(x)| <= C |Bplus|,    x >= 1.

3. |Bplus| is comparable to c^(11/4) exp(-c), and |B_lambda| is comparable to |Bplus|.
4. For the repaired source f=E(tilde h),

       || f(lambda^{-1} exp(-s)) ||_{L2(s>=0)} <= C |Bplus| lambda^{-1/2}.

5. If a=h_lambda^circ(0), then

       |a|/|Bplus| = O(c^(7/4) exp(-c)).

   The fixed compact repair is a*psi with ||psi||_infty bounded independently of lambda. The compact co-Poisson sum on the window therefore has sup norm at most C lambda^(3/2) |a|.

Primary reference for the exact entire finite-Fourier representation: NIST DLMF 30.15.5, https://dlmf.nist.gov/30.15.E5. The normalization used here is derived explicitly in manuscript Lemma v12-endpoint-energy rather than copied from DLMF's different normalization.

## Elementary approximation lemma with growing derivative order

Fix intervals I with positive length and bounded diameter, and constants A0,A1. Suppose

    F(z)=integral_{-Omega}^{Omega} exp(i z t) dnu(t),
    Omega <= A0*c,  ||nu|| <= c^A1.

For any chosen K>0 there is A=A(K,A0,A1,I), independent of c, such that the Taylor polynomial T of degree D=ceil(A*c), about the midpoint of I, satisfies simultaneously for 0<=j<=ceil(c):

    sup_I |(F-T)^(j)| <= exp(-K*c) (C*c)^j.

Proof: write the Taylor polynomial under the finite measure. If d is the interval radius, the jth differentiated exponential remainder is bounded by

    ||nu|| Omega^j exp(Omega*d) (Omega*d)^(D+1-j)/(D+1-j)!.

Since D+1-j >= (A-2)c for large c, Stirling's elementary factorial lower bound makes the right-hand side at most the displayed quantity by choosing A large. The constant C is independent of j,c. The polynomial factor ||nu|| is absorbed by slightly increasing A. This proof establishes growing-order control; it is not an unjustified differentiation of an asymptotic expansion.

Two polynomial inequalities on a fixed interval suffice:

    ||T||_infty <= C (D+1) ||T||_2,
    ||T^(j)||_infty <= (C D^2)^j ||T||_infty.

The first follows by expanding in normalized Legendre polynomials and using |P_k|<=1 and sum_{k=0}^D(2k+1)=(D+1)^2. The second is Markov's inequality iterated on successively lower-degree derivatives. The same conclusions apply to complex polynomials by taking the real part after rotating the scalar phase at a maximizing derivative value (or apply the real inequality to each real and imaginary part).

## Endpoint jets from an exterior norm, without cancellation assumptions

Set M=ceil(2 lambda^2) and define the entire finite sum

    G(v)=sum_{m=1}^M g(m*v/lambda^2).

Its Fourier measure has support in [-2*pi*M,2*pi*M], and total variation O(lambda^3). Thus the approximation lemma applies with bandwidth O(c), including derivatives through r=ceil(c).

For v in [1/2,1], apart from irrelevant threshold values,

    G(v) = lambda*v^(-1/2)*f^circ(v/lambda) + E(v),
    E(v) = sum_{m*v >= lambda^2, m<=M} g(m*v/lambda^2),

where f^circ=E(h_lambda^circ). Each term of E has argument >=1, so input 2 bounds |E(v)| by C |Bplus| lambda^2. The lower-tail bound and the negligible compact repair bound input 4 imply

    ||G||_{L2([1/2,1])} <= C |Bplus| lambda^2.

The conversion du/u=dv/v has only constant weights here. More explicitly, f^circ differs from f by a E(psi), bounded on this interval by C |a| lambda^(3/2); this is exponentially smaller than |Bplus| for large lambda.

Approximate G by a degree-D polynomial, D=O(c), with K sufficiently large (e.g. any K>2 suffices after polynomial prefactors). Since |Bplus| is polynomial in c times exp(-c), the approximation error and all its derivatives are absorbed in the following bound:

    |G^(j)(1)| <= C |Bplus| lambda^4 (C lambda^4)^j,
    0<=j<=r.

Here one lambda^2 factor is the exterior norm, the other is the degree factor in the L2-to-sup inequality. Markov supplies D^(2j)=O(lambda^(4j)).

Likewise apply the same approximation lemma to g on [1,3]. Input 2 already gives a sup bound C|Bplus|, so no L2 degree factor is needed:

    sup_{1<=x<=3} |g^(j)(x)| <= C |Bplus| (C lambda^4)^j,
    0<=j<=r.

At the strict interior trace v=1+, the compact co-Poisson sum equals G minus the fixed finite collection of exterior terms with m>=lambda^2 (including equality if lambda^2 is an integer). Every such argument at v=1 lies in [1,3]. Each derivative introduces (m/lambda^2)^j<=3^j, and there are O(lambda^2) terms. Multiplication by sqrt(v)/lambda gives

    |(v*d/dv)^j f^circ(v/lambda)|_{v=1+}
       <= C |Bplus| lambda^3 (C lambda^4)^j,
    0<=j<=r.

The conversion between ordinary derivatives and logarithmic derivatives does not cost j!: use

    (v*d/dv)^j = sum_{k=0}^j S(j,k) v^k d^k/dv^k,
    S(j,k) <= binom(j,k) j^(j-k),
    sum S(j,k) A^k <= (A+j)^j.

As j<=r=O(lambda^2) and A=C lambda^4, this is absorbed by a fixed enlargement of C. The derivatives of sqrt(v) similarly cost at most j!2^j and are absorbed by A^j.

The upper trace u=lambda- involves only the first source summand. It is g(exp(-s))*exp(-s/2), so its logarithmic jets satisfy the same bound without lambda^3. The periodic derivative jumps of the inversion-even p^circ at the identified endpoint therefore satisfy the preceding lambda^3 bound. Its zeroth-order boundary jump is exactly zero, by inversion symmetry.

Interior jumps of the jth derivative are explicitly the source endpoint logarithmic jth jet times m^(-1/2), with signs and reflection factors. Summing m<lambda^2 costs O(lambda). Consequently, if J_j is the sum of absolute jumps of the ordinary logarithmic jth derivative of p^circ, including the periodic boundary jump, then

    J_j <= C |Bplus| lambda^3 (C lambda^4)^j,
    1<=j<=r-1.

This is the main improvement over treating the entire continuous derivative variation by a global norm/Bplus.

## The function-jump contribution and near-integer resonance

The exact jump train from the manuscript yields

    endpoint Fourier tail = -(Bplus/pi) sum_{1<m<lambda^2} m^(-1/2)
                              sum_{n>N} sin(2*pi*n*log(m)/L)/n,

up to the harmless choice of which sign denotes P_N-I. The standard Dirichlet estimate, including the bounded sawtooth limit, is

    |sum_{n>N} sin(n*theta)/n|
       <= C min(1, 1/[N*|sin(theta/2)|]).

Remove the single largest integer m0<lambda^2. Its contribution is O(|Bplus|/lambda), uniformly even when lambda^2 approaches an integer arbitrarily closely. For all other m, the distance lambda^2-m is at least 1. Splitting m at lambda and lambda^2/2 gives

    sum_{1<m<lambda^2, m!=m0} m^(-1/2) / |sin(pi*log(m)/L)|
       <= C lambda*L*(1+log(lambda)).

Indeed near the upper endpoint use sin(pi log(m)/L) >= C (lambda^2-m)/(lambda^2 L), then sum the harmonic denominator after excluding m0; away from it use log(m)>=log(2). Hence the normalized function-jump endpoint tail is

    O(1/lambda + lambda*L*(1+log(lambda))/N).

This explicitly handles arbitrarily near arithmetic thresholds and does not assume a uniform distance from lambda^2 to the integers. A bound claiming uniform O(1/N) without treating this nearest jump would be false.

## Higher jets and the analytic remainder

Use piecewise integration by parts r times. For each n!=0,

    hat p^circ(n) = (1/sqrt(L)) sum_{j=0}^{r-1}
       (i*t_n)^(-j-1) sum_x [p^circ^(j)]_x exp(-i*t_n*x)
       + R_n,

with the sign convention for jumps fixed as right minus left, and

    |R_n| <= ||(p^circ)^(r)_ac||_1 / (sqrt(L)*|t_n|^r).

Signs are immaterial to estimates but must be fixed if the expansion is printed as an identity. Repeated integration of the distributional derivative with [p]_x=right-minus-left gives the displayed plus sign for the jump terms.

The j=0 contribution is exactly the jump train just estimated. For 1<=j<r, sum the absolute Fourier endpoint tails. The factor L^(-1/2) in physical endpoint evaluation combines with the Fourier coefficient factor L^(-1/2), giving

    sum_{|n|>N} J_j/[L |t_n|^(j+1)]
      <= C J_j (L/(2*pi*N))^j / j.

Thus, when q=C lambda^4 L/N<1/2, their total divided by |Bplus| is at most

    C lambda^3 sum_{j=1}^{r-1} q^j <= C lambda^7 L/N.

For the smooth-piece remainder use the entire Fourier representation directly. On a fixed small complex logarithmic disk |z-y|<=rho (e.g. rho=1/10), every active real argument x<=1 becomes x exp(z-y), whose imaginary part is at most e^rho sin(rho). There are at most O(lambda^2) summands and the physical square-root prefactor is at most a fixed constant. Cauchy's estimate therefore gives, with constants A,C independent of r and lambda,

    ||(p^circ)^(r)_ac||_1 <= C L lambda^3 r! rho^(-r) exp(A*c).

The branch chosen on each smooth interval is analytically extended with its fixed collection of summands; crossing a threshold in that auxiliary continuation causes no difficulty. Jump contributions were already extracted separately.

Summing |R_n| at the endpoint and dividing by |Bplus| gives at most

    C poly(lambda,L) exp((A+1)c) r! (C L/N)^(r-1).

For r=ceil(c) and N=ceil(lambda^8(1+L)), r!<=(C lambda^2)^r. Thus this remainder is O(lambda^{-A2}) for every fixed A2; the dominating exponent is -6c log(lambda)+O(c). This is an actual choice of growing integration order supported by the exact entire representation.

Combining the three parts gives

    |(P_N p^circ)(0)-p^circ(0)| / |Bplus|
      <= C [lambda^{-1} + lambda L(1+log(lambda))/N + lambda^7 L/N]
         + O_A2(lambda^{-A2})
      = O(lambda^{-1}).

## Restore the exact compact repair without taking high derivatives of it

The repair is only C-infinity and must not be included in the growing-order analytic argument. Instead, if e=p_lambda-p^circ, then

    ||e||_infty <= C lambda^(3/2)|h_lambda^circ(0)|.

The ordinary Fourier projection has Lebesgue norm O(log(N+2)), so

    |(P_N-I)e(0)|/|B_lambda|
      <= C lambda^(3/2) log(N+2) |h_lambda^circ(0)|/|B_lambda|
      = O_A(lambda^{-A})

for every fixed A along this polynomial N. This controls the exact repair's physical endpoint as well as its Fourier contribution. Finally use Bplus comparable to B_lambda.

## Scope, adversarial checks, and what is still open

- This changes no finite vector: it is exactly P_N p_lambda, with the physical endpoint and original Fourier cut.
- It does not suppress the true distributional derivative's arithmetic jumps or any sampler graph defect.
- It uses an asymptotic cutoff of order lambda^8 log(lambda), not the natural Slepian scale lambda^2 and not a numerical constant valid at lambda=3.
- Positive definiteness at one finite (lambda,N) does not extend to this diagonal.
- It does not by itself transfer the full growing-band G1 bound: although it supplies new high-frequency coefficient estimates, those must be inserted separately into the weighted matrix bounds with the exact repair treated in the appropriate form norm.
- It does not prove an endpoint estimate for an arbitrary member of a growing PSWF block. Fixed orders 0 and 4 and their proved source estimates are essential.
- Most dangerous steps to audit: normalization of G(v), use of repaired lower-tail bound for the unrepaired h^circ, derivative-order uniformity of Taylor approximation, periodic derivative jumps, and the nearest arithmetic threshold. Each has been explicitly addressed above.

## Addendum: a uniform high-frequency coefficient consequence (also for review)

The same proof gives, along N_lambda=ceil(lambda^8(1+L)),

    |hat p_lambda(n)| <= C |B_lambda| lambda sqrt(L)/|n|,
    all |n|>N_lambda,

with a constant independent of lambda and n. This is stronger than an endpoint statement and can be inserted into the existing weighted matrix estimate; it does not bound the whole source variation by B times a polynomial.

Indeed, the function-jump total variation is O(Bplus*lambda). The higher-jump terms give, uniformly for |t|>=2C lambda^4,

    |hat p^circ(n)| <= C |Bplus|/sqrt(L)
      [lambda/|t| + lambda^7/|t|^2] + |R_n|.

At |t_n|>=2*pi*N_lambda/L, the second term is absorbed by the first. The analytic remainder ratio to Bplus*lambda/(sqrt(L)*|t_n|) is largest at the first omitted frequency, where it is bounded by

    poly(lambda,L) exp((A+1)c) r! (C*L/N_lambda)^(r-1),

and thus tends to zero faster than every fixed power. Since the ratio decreases thereafter, the result holds uniformly in n.

For the exact repair, do not use an n-independent sup bound. Its periodic variation is polynomially bounded directly. For a fixed compact bump psi supported in [-b,b],

    integral_{1/lambda}^lambda |D_log E(psi)(u)| du/u
      <= sum_{m<=b*lambda} m^(-1/2)
           integral_0^b x^(-1/2)[|psi(x)|/2+x|psi'(x)|] dx
      <= C sqrt(lambda).

There are no source endpoint jumps since psi vanishes smoothly at b. Inversion averaging does not increase this bound, and the periodic zeroth-order boundary jump is zero. Therefore the exact repair e satisfies

    |hat e(n)| <= C |h_lambda^circ(0)| sqrt(lambda*L)/|n|,

which is exponentially smaller than the target coefficient bound.

Consequently the proof of the existing weighted transfer estimate can use the single coefficient bound above in place of the raw total variation. For any fixed R>3, x in the finite E_K with K>=N_lambda (and the same weighted norm as manuscript Section 21), the resulting estimate has the same shape as the arithmetic jump-only part:

    |QW_lambda((P_N-I)p_lambda,D_log x)|/|B_lambda|
       <= C_R ||x||_{H_R,L} lambda^2
          [L/N + (L/N)^(R-1)(1+log(2N))],

subject to exactly the same matrix-domain/convergence conditions as that existing proof. For N=N_lambda this tends to zero, and the endpoint theorem has beta=O(1/lambda). Thus the existing continuum weak-G1 estimate transfers to the literal projection along an explicit polynomial diagonal, without adding an endpoint shell. The weighted bound and its applicability should be checked independently before inclusion: it is a consequence of the established coefficient estimate plus an existing matrix convolution argument, not a new positivity assertion.

Crucially this does not yield ||D W k|| small without the weighted test restriction, does not identify k with a lowest eigenvector on growing windows, and does not alter or erase any corrected-sampler graph defect.
