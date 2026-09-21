# Independent audit of the polynomial endpoint theorem

Reviewed against the complete v1.13 source and `endpoint_derivation.md`, September 20, 2026.

**Verdict:** no fatal gap found in the asymptotic estimate for the exact fixed two-mode source. The argument appears to prove relative endpoint recovery O(lambda^(-1)) at N=ceil(lambda^8(1+2 log lambda)), with unspecified absolute constants and sufficiently-large threshold. This is not a certified usable cutoff at lambda=3, and it is not a growing-window spectral or G2 theorem.

## Normalization and existing inputs

The manuscript has h°(u)=lambda^(-1/2)g(u/lambda), integral h°=0, and E(h°)(u)=sqrt(u) sum_m h°(mu). Therefore, at u=v/lambda,

    f°(v/lambda)=sqrt(v)/lambda sum_{mv<lambda²} g(mv/lambda²).

The proposed formula for G is exact away from thresholds. Its equality-threshold convention does not affect L² bounds and its right endpoint jet uses the correct strict interior trace. The measure norm of each g is O(lambda) from the finite-Fourier eigenvalue of size chi/lambda; summing M=O(lambda²) terms gives total variation O(lambda³), and the maximum frequency is 2 pi M=O(c).

The earlier manuscript proposition immediately preceding `lem:pswf-away-energy` gives |psi_n,c(x)|≤C|psi_n,c(1)|/x for all x≥1. The proved two-mode endpoint noncancellation therefore supplies the required |g(x)|≤C|Bplus| for x≥1. No lower bound for g on the exterior is assumed. The repaired lower-tail norm is actually O(|Bplus| lambda^(-1)(1+log lambda)), stronger than the relaxed lambda^(-1/2) input used here. The raw source differs by a co-Poisson bump whose coefficient is exponentially smaller than Bplus, so replacing repaired by raw source in this exterior estimate is legitimate.

## Growing-order derivative constants

For j≤ceil(c), degree D=ceil(Ac), and fixed interval radius d, the differentiated exponential remainder has the exact upper bound

    ||nu|| Omega^j exp(Omega d) (Omega d)^(D+1-j)/(D+1-j)!.

For Omega≤A0c the factorial exponent is at most

    [A0 d +(A−1) log(e A0 d/(A−1))]c + O(log c),

uniformly over that derivative range. Choosing A sufficiently large produces exp(−Kc)(Cc)^j with C independent of j and c. This supplies the derivative uniformity actually used; no fixed-order asymptotic has been differentiated.

Degree-O(c) Markov bounds cost (Cc²)^j. The L²-to-sup factor costs one extra c=O(lambda²). Applied to G's exterior norm O(Bplus lambda²), this gives Bplus lambda⁴(C lambda⁴)^j. For individual g the exterior sup avoids this extra degree factor. These estimates remain valid at the endpoint because the angular extension is entire.

The conversion (v d/dv)^j=ΣS(j,k)v^k d^k/dv^k does not add a hidden factorial: S(j,k)≤binom(j,k)j^(j−k), so the sum against A^k is at most (A+j)^j. Since j=O(lambda²) and A=O(lambda⁴), one fixed enlargement of the exponential base suffices. The square-root prefactor is controlled by the same argument, bounding its k-th derivative by k!C^k≤(Cj)^k.

## Thresholds, endpoint traces and Fourier tails

For each fixed lambda, the compact sum has finitely many thresholds. At the lower endpoint the right trace is G minus a fixed collection of exterior terms, even when lambda² is an integer. A threshold arbitrarily close to the endpoint can make the analytic neighborhood of the *actual piecewise function* very small, but that is not used. The analytic continuation of each fixed branch remains available for the Cauchy estimate, and the thresholds are accounted for by explicit jumps.

The logarithmic derivative jump of order j at an interior threshold is m^(-1/2) times a fixed endpoint jet of g, with reflection and square-root factors. Summing m<lambda² costs O(lambda). The boundary jet bound O(Bplus lambda³(C lambda⁴)^j) is therefore a safe common upper bound. Inversion symmetry exactly cancels the zeroth periodic boundary jump.

The j=0 jump train agrees with the manuscript's exact sine-sum Fourier formula. Excluding the largest integer below lambda² costs at most C|Bplus|/lambda because that jump has weight O(1/lambda). Every other near-upper-endpoint integer has lambda²−m≥1, so the harmonic estimate is uniform even when lambda² is arbitrarily close to an integer. The remaining weighted cosecant sum is O(lambda L(1+log lambda)). There is no unproved arithmetic nonresonance assumption.

For j≥1, the two physical Fourier normalization factors combine to 1/L. Summation gives

    Σ_{|n|>N} J_j/(L|2 pi n/L|^(j+1))
      ≤ C J_j (L/(2 pi N))^j/j.

At N=ceil(lambda⁸(1+L)), the ratio C lambda⁴ L/N is O(lambda^(-4)), so the complete higher-jump contribution is O(Bplus/lambda).

The branchwise analytic remainder has derivative bound O(L lambda³ r! rho^(-r) exp(Ac)), with no factor equal to the number of intervals: their lengths sum to L. Summing the Fourier tail and dividing by Bplus introduces exp(c) but leaves a factor (CL/N)^(r−1). With r=ceil(c), its logarithm is −6c log lambda+O(c)+O(log lambda), which tends to minus infinity faster than every fixed logarithmic power. This part is uniform in the arithmetic threshold locations.

## Repair and necessary wording

The arbitrary fixed C-infinity repair must stay out of the growing-order analytic differentiation. Treating it by the Dirichlet projection Lebesgue norm O(log(N+2)) is correct. Its sup norm is at most the stated C lambda^(3/2)|h°(0)| (in fact a sharper direct bound is available), and |h°(0)|/|Bplus| is a polynomial times exp(−c). Hence its endpoint projection error is negligible on this polynomial diagonal.

Three small presentation requirements should be retained in the final proof:

1. Invoke Dirichlet–Jordan convergence at the common continuous periodic endpoint to identify the infinite Fourier sum with the one-sided physical endpoint. Piecewise analyticity/BV supplies this.
2. State whether the signed j=0 formula denotes P_N−I or I−P_N. Its sign is immaterial to the absolute estimate but must be consistent in an identity.
3. State explicitly that all O constants may depend on the fixed two-mode orders and the chosen fixed bump, but not on lambda, derivative order j≤ceil(c), or the distance of lambda² to the nearest integer.

No claim should be made for a growing family of PSWF orders. The finite Fourier measure and radial bounds used here are for orders 0 and 4. No proof is supplied for the small spectral complement at this diagonal; all sampler graph defects and the additional form/graph work remain.
