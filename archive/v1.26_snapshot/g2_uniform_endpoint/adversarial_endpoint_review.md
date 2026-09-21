# Adversarial review: zero physical trace of complete Weil eigenfunctions

21 September 2026. Reviewed `actual_ground_endpoint_derivation.md` against the complete v1.17 physical form and the two cited primary papers. No blocking mathematical issue was found. This is an internal analytic review, not external peer review.

## Exact normalization and bounded perturbation

The one-dimensional logarithmic Laplacian has c_1=1 and rho_1=-2 gamma, so half its exterior-Dirichlet realization has the displayed kernel 1/(2|x-y|) and scalar -gamma. This is the restricted operator, not the spectral logarithm of a local Dirichlet Laplacian.

I independently recomputed the archimedean subtraction. With rho(y)=e^(y/2)/(2 sinh y), one has rho(y)=1/(2y)+1/4+O(y). The scalar difference is

\[
\int_0^\infty\left(\frac1{\sinh y}-\frac{1_{y<1}}y\right)dy
-\log(4\pi)=\log2-\log(4\pi)=-\log(2\pi).
\]

It agrees with the high-frequency symbol Re psi(1/4+it/2)-log pi=log|t|-log(2pi)+o(1). The remaining convolution kernel k=rho-1/(2y) is bounded near zero and integrable on each fixed physical interval. It consequently defines a bounded operator on both L2 and L-infinity there.

The prime terms are the complete finite collection of truncated translations with their adjoints. The pole kernel is 2 cosh((x-y)/2), not a positive-semidefinite form: its centered decomposition retains the positive cosh square and negative sinh square. Its maximum row and column integral is exactly 4 sinh(L/2), since the row integral is 4[sinh(x/2)+sinh((L-x)/2)] and its maximum occurs at an endpoint. Thus the stated common K bound is valid. The full-length prime translation is zero almost everywhere; its optional inclusion in the norm bound is conservative.

## Common core and operator identification

Chen--Weth's Theorem 3.1 does state density of smooth compact support in the Dirichlet logarithmic form space on bounded Lipschitz domains. The added argument proving the same core for the manuscript's canonical form is valid: cut a smooth periodic Fourier sum off on endpoint strips of width eta. The discarded periodic function has L2 norm O(sqrt(eta)) and H1 norm O(eta^(-1/2)). Interpolation gives H^s norm O(eta^(1/2-s)) for fixed 0<s<1/2, hence convergence in the weaker logarithmic form norm. Its endpoint values agree across the periodic join. This supplies a common form core rather than imposing a boundary condition by definition. Bounded form perturbation then gives the self-adjoint operator identity W=A+K and D(W)=D(A).

Source checked: [Chen--Weth, The Dirichlet Problem for the Logarithmic Laplacian, arXiv:1710.03416v6](https://arxiv.org/pdf/1710.03416), Theorems 1.1 and 3.1.

## The L-infinity bootstrap survives the main adversarial objection

An arbitrary bounded L2 perturbation would not suffice. Here K is additionally bounded on L-infinity, which is essential and has been established above.

The exact split is

\[
A=A_\varepsilon+(\log(1/\varepsilon)-\gamma)I-J_\varepsilon.
\]

The small-jump exterior-zero form is nonnegative and Markovian, including its exterior killing part. Its positive-shift resolvent contracts both L2 and L-infinity with norm at most 1/a. A direct justification is to truncate the jump kernel below eta>0: the finite-activity generator is mI-T with a positive kernel T whose row and column integrals are at most m=log(epsilon/eta). The geometric resolvent series gives the same 1/a bound. Passing to the increasing closed forms retains that bound and consistency on the two spaces.

The remote kernel has squared row norm at most 1/(2epsilon), so J_epsilon maps L2 into L-infinity. For an eigenvalue mu choose epsilon so a=log(1/epsilon)-gamma-mu exceeds both K norms. The common Neumann series then produces a bounded solution to (A_epsilon+a+K)v=J_epsilon u. Its L2 version coincides with the original eigenfunction by uniqueness. No positive Sobolev gain is claimed or required. The explicit epsilon choice in the draft does ensure a-C_lambda>=1, for either sign of mu.

## The external regularity theorem applies with all hypotheses present

The zero extension lies in the Dirichlet energy space; the bootstrap makes it bounded; and 2(mu u-Ku) is bounded. The domain is an interval and satisfies the exterior uniform sphere condition. Theorem 1.1 of the cited paper therefore yields continuity of the zero extension and the inverse-square-root logarithmic boundary bound. For complex eigenfunctions the theorem applies to real and imaginary parts separately.

Source checked: [Hernandez-Santamaria--Lopez Rios--Saldana, Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian, arXiv:2401.18033v2](https://arxiv.org/pdf/2401.18033), Theorem 1.1. Its bounded-solution hypothesis is not automatic from that theorem; the preceding new bootstrap is what supplies it.

Thus every eigenfunction of the complete fixed-window operator has zero physical endpoint trace, independently of RH, positivity, parity or simplicity. A smooth nonvanishing coordinate-change factor between logarithmic and original physical coordinates preserves this zero trace.

## Scope that must remain explicit

1. The endpoint is the continuous representative's physical trace. Continuity with logarithmic modulus does not prove absolute Fourier summability or convergence of sharp Fourier partial sums at that point.
2. The Fejer estimate in the draft has the correct L scales, both boundary intervals, kernel mass and 1/(2 sqrt(N)) tail term. It is a positive-filter estimate at a fixed window.
3. The nonzero G1 source endpoint cannot agree relatively with the actual continuum ground endpoint: the latter is exactly zero. Ordinary norm overlap and a small ordinary operator residual are compatible with this mismatch.
4. A finite-compression eigenvector or a joint growing-window/Fourier-cut sequence is a different object. The fixed-window physical trace theorem does not exclude a separately proved nonzero normalized finite-cut endpoint along such a sequence.
5. No useful growing-window regularity constant has been proved. The boundedness constant may be extremely poor. G2 and the signed growing-window lower bound remain open.

## Publication extractions and graph-trace proposition

The concise `eigen_endpoint_insert.tex` faithfully retains the audited argument and all of the preceding scope limits. The Fejer factor is L^(-1/2) in the coefficient sum and L^(-1) in the physical convolution kernel, as required.

The parent's `graph_trace_insert.tex` also passes. Its symmetric shell has exactly 2N terms, endpoint one, and squared ordinary norm L/(2N). The separately retained logarithmic diagonal and the bounded commutator give graph norm O_lambda(log(N)/sqrt(N)). The same sequence works after a fixed scalar operator shift. Since it converges to zero in graph norm while its scalar endpoint is always one, evaluation on the polynomial core is not closable in that norm. Lower boundedness also implies convergence in the closed-form norm.

This observation is consistent with zero endpoint trace for actual eigenfunctions: the latter follows from their exact eigen equation and its regularity, whereas the polynomial-core evaluation is not a continuous graph-norm functional. Neither graph convergence of Fourier approximants nor ordinary spectral overlap alone identifies physical traces.
