# Actual Weil eigenfunctions have zero physical boundary trace

Proof integrated in complete manuscript v1.18 after independent internal adversarial review, 2026-09-21. This treats the actual complete semilocal Weil operator, not its finite Fourier compressions. All constants below are fixed-window constants; no useful uniform-in-window source comparison is asserted. Reviews are saved alongside this derivation; they are not external referee reports.

## 1. Exact physical decomposition

Let Ω=(0,L), L=2log λ, and extend physical functions by zero outside Ω. Use the Fourier transform with multiplier variable t (exponent exp(−itx)). Let A=(1/2)L_Δ^Dir be the restricted, exterior-Dirichlet logarithmic Laplacian, whose full-line symbol is log|t|. In dimension one, on compactly supported smooth tests,

    A f(x)=∫_0^∞ [2 f(x)1_(y<1)−f(x+y)−f(x−y)]/(2y) dy −γ_E f(x).

This follows from Chen–Weth, Theorem1.1: c_1=1 and ρ_1=−2γ_E. This is the RESTRICTED logarithmic Laplacian, not the logarithm of the Dirichlet Laplacian.

Write ρ(y)=e^(y/2)/(2sinh y) and k(y)=ρ(y)−1/(2y). Then k extends continuously to zero with k(0)=1/4 and is integrable on every finite interval. The exact negative-archimedean operator of the manuscript is

    A_arch f(x)=∫_0^∞ ρ(y)[2e^(−y/2)f(x)−f(x+y)−f(x−y)]dy
               −[log(4π)+γ_E]f(x).

As a normalization check, its Fourier-basis diagonal is exactly −A_n in eq:v114-arch-diagonal: the omitted y>L diagonal integral equals −log tanh(L/2), with its sign retained.

Subtracting A gives the exact identity

    A_arch=A−log(2π)I−K_k,
    (K_kf)(x)=∫_Ω k(|x−y|)f(y)dy.

Indeed the remaining scalar integral is

    ∫_0^∞ [1/sinh y−1_(y<1)/y]dy=log2,

by integrating csch y as log tanh(y/2) and taking the lower cutoff to zero. Thus the scalar is log2−log4π=−log2π. No diagonal constant was dropped.

Put a_m=log m and w_m=Λ(m)/sqrt(m). The complete physical Weil operator is therefore

    W=A+K,

    (Kf)(x)=−log(2π)f(x)−∫_Ω k(|x−y|)f(y)dy
       −Σ_(1<m<λ²) w_m[1_(x+a_m<L)f(x+a_m)+1_(x>a_m)f(x−a_m)]
       +2∫_Ω cosh((x−y)/2)f(y)dy.

The strict prime upper cut only removes a zero full-length translation. The last term is the actual pole term: in centered coordinates its form is 2|<f,cosh(x/2)>|²−2|<f,sinh(x/2)>|². Its kernel is 2cosh((x−y)/2), so both signs are retained.

For every 1≤p≤∞ the operator K is bounded on Lp(Ω), with common bound

    ||K||_(p→p) ≤ C_λ
      :=log(2π)+2∫_0^L|k(y)|dy+2P_λ+4sinh(L/2),
    P_λ=Σ_(1<m≤λ²) w_m.

The integral-kernel row/column bounds prove the k and pole estimates, with
sup_x∫_Ω2cosh((x−y)/2)dy=4sinh(L/2). Each truncated translation has Lp norm≤1. In particular the L∞ and L2 versions are the same bounded operator on their common domain. K is real and self-adjoint on L2.

### Closed-form identification

The displayed equality first holds on C_c^∞(Ω), by the exact physical Weil formula. This is a form core for the Dirichlet logarithmic Laplacian (Chen–Weth Theorem3.1). It is also a form core for the manuscript's W: finite periodic Fourier sums are a form core by prop:v114-weil-core; multiply a smooth periodic sum by cutoffs removing endpoint strips of width ε. For any fixed 0<s<1/2, the discarded function has periodic H^s norm O(ε^(1/2−s)) and therefore tends to zero in the logarithmic form norm. The bound follows directly from the fractional difference quotient, or interpolation of its L2 norm O(sqrt ε) and H1 norm O(ε^(−1/2)). The interpolation bound is O(ε^(1/2−s)); both endpoints are treated as one periodic neighborhood. Smooth compact support is obtained. Thus both lower-bounded closed forms agree on a common form core, and W=A+K as self-adjoint operators. In particular D(W)=D(A) and their form domains agree; this is a bounded-perturbation conclusion, not an assumed endpoint condition.

## 2. A boundedness bootstrap that requires no Sobolev gain

Let Wu=μu, u∈D(W)⊂L2(Ω), μ real. Choose 0<ε<min(1,L), and define the nonnegative killed small-jump generator

    A_ε f(x)=∫_(0<y<ε) [2f(x)−f(x+y)−f(x−y)]/(2y)dy,

with exterior zero values, in its closed Dirichlet-form realization. Define

    J_ε f(x)=∫_(y∈Ω, |x−y|≥ε) f(y)/(2|x−y|)dy.

Then exactly, as closed operators,

    A=A_ε+[log(1/ε)−γ_E]I−J_ε.

The small-jump form is Markovian, including the nonnegative killing term from the exterior. Its semigroup is sub-Markovian and its resolvent obeys

    ||(A_ε+aI)^−1||_(p→p)≤1/a, a>0, p=2,∞.

This standard contraction can alternatively be proved for finite-activity cutoff kernels ε'>0 and passed to the increasing closed forms; each finite-activity generator is a killed symmetric jump generator. In particular the L2 and L∞ resolvents are consistent.

The large-jump kernel is square integrable in each row:

    ||J_ε||_(2→∞)≤(1/(2ε))^(1/2).

Indeed ∫_(|z|≥ε)1/(4z²)dz=1/(2ε), and restriction to Ω only decreases it.

Set a=log(1/ε)−γ_E−μ. Choose ε so a>C_λ; this is always possible at fixed λ,μ. The eigen equation becomes

    (A_ε+aI+K)u=J_εu.

The inverse of A_ε+aI+K exists simultaneously on L2 and L∞ by the Neumann series

    [I+(A_ε+aI)^−1K]^−1(A_ε+aI)^−1.

The series has norm≤1/(a−C_λ). Since J_εu belongs to L∞∩L2, the two inverse constructions agree, by their common Neumann partial sums and convergence in L2 (Ω has finite measure). Uniqueness in L2 identifies the bounded solution with u. Therefore

    ||u||∞ ≤ ||u||2 / [(a−C_λ)sqrt(2ε)].

For a completely explicit choice take

    ε=min{1/2,L/2, exp[−(|μ|+γ_E+C_λ+1)]}.

Then a−C_λ≥1. This bound may be extremely poor as λ grows; only fixed-window boundedness is claimed. It does not assume that the log-order resolvent gains a positive Sobolev order.

## 3. Boundary regularity of the actual eigenfunction

The zero extension of u belongs to the logarithmic Dirichlet form space H(Ω), by Section1. The eigen equation is now

    L_Δ u = 2(μu−Ku)=:f in Ω,  u=0 outside Ω,

and f∈L∞(Ω), by Section2 and K's L∞ bound. Theorem1.1 of Hernández-Santamaría–López Ríos–Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” arXiv:2401.18033, therefore applies: Ω is a bounded interval satisfying an exterior uniform sphere condition, u∈H(Ω)∩L∞, and the RHS is bounded. For complex u apply the real theorem to its real and imaginary parts. It yields a continuous representative of the zero extension and

    |u(x)|≤C_(λ,μ,u) /sqrt(|log(min{dist(x,∂Ω),0.1})|),
         0<x<L.

Consequently EVERY eigenfunction of the complete W has

    u(0)=u(L)=0.

In particular this holds for the simple even ground certified at λ=3. No eigenvalue positivity, RH, source assumption, or ground-state ordering is used in this regularity result.

This is stronger than the elementary conditional obstruction “any globally bounded eigenfunction admitting a finite nonzero endpoint trace is impossible”; the bootstrap and boundary theorem establish the continuous zero trace itself.

## 4. What this does and does not say about the Fourier endpoint

The theorem establishes the actual physical trace. For an eigenfunction with absolutely summable Fourier coefficients, it also forces

    L^(−1/2) Σ_(n∈Z) u_hat(n)=0.

In even normalized parity coordinates this is

    L^(−1/2)[v_0+sqrt2 Σ_(n≥1)v_n]=0.

Continuity alone does not prove absolute Fourier convergence or convergence of the sharp partial sums at the endpoint. No such assertion is made here. Fejér sums and Poisson/Abel means DO converge to the physical endpoint0, by continuity.

For a scale-correct quantitative statement define, N≥4,

    σ_(N−1)u(0)=L^(−1/2) Σ_(|n|<N)(1−|n|/N) u_hat(n).

Its positive convolution kernel is F_N(2πx/L)/L, where
F_N(θ)=N^(−1)[sin(Nθ/2)/sin(θ/2)]², with total mass1. Put h=L/sqrt N and d(x)=min(x,L−x). The boundary bound gives |u(x)|≤C sqrt(ℓ(h)) for d(x)<h, where ℓ(t)=1/|log(min(t,0.1))| is increasing. For d(x)≥h, the inequality sin(πx/L)≥2d(x)/L gives

    F_N(2πx/L)/L ≤ L/[4N d(x)²],
    ∫_(d≥h) F_N(2πx/L)dx/L ≤ L/(2Nh)=1/(2sqrt N).

Consequently, retaining all physical Fourier scale factors,

    |σ_(N−1)u(0)| ≤ C sqrt(ℓ(L/sqrt N)) + ||u||∞/(2sqrt N)
                 = O_(λ,μ,u)((log N)^(−1/2)).

The same expression holds at x=L. This is a positive-kernel filtered endpoint estimate, not a claim about sharp Fourier cuts or absolute convergence.

Since the exact repaired G1 source has nonzero physical endpoint B_λ, any proposed NONZERO physical endpoint comparison to the actual complete ground is false: for any scalar multiple c u,

    |p_λ(0)−c u(0)|/|B_λ|=1.

This does not contradict ordinary-norm overlap or exponentially small absolute residuals. It also does NOT rule out an endpoint claim for finite-compression eigenvectors evaluated on a joint growing-window/cutoff diagonal; the fixed-window limiting statement and that two-parameter limit are different. A finite-cut endpoint theorem requires its own rate and normalization and cannot identify a nonzero continuum ground trace.

## Primary sources verified

1. Chen–Weth, “The Dirichlet Problem for the Logarithmic Laplacian,” arXiv:1710.03416v6, Theorem1.1 (integral normalization), Theorem3.1 (form density), Theorem1.11 (earlier boundary decay for every exponent<1/2): https://arxiv.org/pdf/1710.03416.
2. Hernández-Santamaría, López Ríos, Saldaña, “Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian,” arXiv:2401.18033, Theorem1.1 (bounded weak solution + bounded RHS yields continuity of zero extension and sharp log^(−1/2) boundary estimate): https://arxiv.org/pdf/2401.18033.

The boundedness bootstrap in Section2 is supplied here rather than attributed to results on unperturbed eigenfunctions. The actual prime/pole perturbations are present throughout.
