# Spectral geometry lane: an arithmetic oscillator feeding a canonical system

Internal proposal/admission assessment, 2026-09-29. Reviewed base: `b5bd5fa` (parent refreshed main and reviewed all 104 conclusions and 14 continuation groups). This lane read current AGENTS, OPERATOR-BRIDGES/CCM-LIMIT, NS47, NS43's complete selection note, the NS57 dependency audit, and control instructions. This is not a new research row, thaw, sufficient-inequality proof, numerical screen, or revalidation of historical certificates.

**Wall check: Same open gap.** Closest targets: OPERATOR-BRIDGES' de Branges extension and CCM-LIMIT; closest closures: NS47 and NS57. The proposal supplies an explicit arithmetic state space and a sharply specified scattering interface. It does not supply the missing positive realization or complete transfer. The immediate decision is which construction deserves specification work, not whether RH has advanced.

## 1. Actual smaller object: a four-dimensional arithmetic oscillator

Take two classical oscillator modes with phase coordinates `(q₂,p₂,q₃,p₃)` and symplectic form `dq₂∧dp₂+dq₃∧dp₃`. Set

`H_cl = log(2)(q₂²+p₂²)/2 + log(3)(q₃²+p₃²)/2`.

Quantize using the usual number operators with vacuum energy subtracted. On `ℓ²(N₀²)`, define

`H₂₃ e_(m,n) = (m log 2+n log 3)e_(m,n)`.

Its self-adjoint domain is the weighted square-summability domain `Σ(m log2+n log3)²|c_mn|²<∞`. Finite sequences form a core. This is a constructed elementary toy, not an unspecified geometric space. For `Re s>0`,

`Tr exp(−sH₂₃) = [(1−2^(−s))(1−3^(−s))]^(−1)`.

The independent excitations record the powers of 2 and 3; these four real phase coordinates carry arithmetic information. Adding flat coordinates without new prime actions would instead add spectator dimensions.

Taking all prime modes gives the incomplete tensor product with vacuum reference, canonically identified with `ℓ²(N)` by unique factorization. The Hamiltonian is `He_n=log(n)e_n`, with domain `Σ(log n)²|c_n|²<∞`; its partition trace equals `ζ(s)` only for `Re s>1`. Each prime-power coefficient in `−ζ′/ζ = Σ_(p,k≥1) log(p)p^(−ks)` is retained there. The infinite system is not a finite-dimensional smooth manifold, and its quantum Hilbert dimension should not be confused with classical phase dimension.

**What this does not give:** zeros of a partition function at complex inverse temperature are not eigenvalues of this self-adjoint Hamiltonian. Its eigenvalues are logarithms of integers. Analytic continuation of the trace does not become a spectral determinant automatically. The gamma factor and the factors `s(s−1)/2` are absent from this toy. Consequently “the arithmetic Hamiltonian is self-adjoint, therefore RH” has no transfer theorem.

## 2. Proposed object: couple the arithmetic modes to a completed scattering system

Use the oscillator only as an arithmetic source for an auxiliary boundary system. Require the boundary response, for every shift `a>0`, to be exactly

`Θ_a(z)=ξ(1/2−a−iz)/ξ(1/2+a−iz)`,

where `ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2`.

The intended output is a conservative or passive realization whose response is analytic and contractive throughout `Im z>0`, with unit-modulus real boundary values. A canonical-system realization would use a locally integrable positive semidefinite matrix `H_a(t)` and the relation `Y′=zJH_aY`, with `J=[[0,−1],[1,0]]`, on its weighted Hilbert space, using Suzuki's orientation. A construction must specify the interval, endpoint conditions, degeneracies of `H_a`, and the self-adjoint operator or relation; writing the differential expression is insufficient. A four-component enlargement or prime-mode coupling must give the same scalar response after eliminating auxiliary channels, not a different completed function.

This target is an existing program: Suzuki's [canonical-system paper](https://arxiv.org/abs/1204.1827) relates innerness of this precise family to zero-free half-planes and constructs explicit canonical systems for `a>1`. Its critical extension to all `a>0` remains the relevant demand. We propose investigating an oscillator-to-boundary implementation of that demand, not claiming the criterion as new.

**Exact conditional edge.** If a construction from the original arithmetic data realizes these exact responses as analytic contractions for every `a>0`, it supplies OPERATOR-BRIDGES' extension and implies RH. For an off-line zero `ρ` with `Re ρ>1/2`, choose `0<a<Re ρ−1/2` avoiding the discrete numerator cancellations `ξ(ρ−2a)=0`. The denominator then creates a pole at `z=i(ρ−1/2−a)` in the upper half-plane, contradicting the response property. Functional symmetry excludes the other half of the strip. The all-shift quantifier matters; one safe shift does not suffice.

This is a direct whole-function route, not a substitute for the existing source-restricted Weil inequalities. It has no even-only conclusion: the full completed function is required. If an implementation instead invokes semilocal Weil compression, it must restore the original complete form domains, both parity sectors, pole/source constraints, and a cofinal ordinary-norm floor or the complete CCM selection/evaluator estimates. An even finite matrix and a nearby root do not provide these.

## 3. A small prerequisite that can fail—and the naive version does

A tempting architecture assigns each prime an independently passive port and cascades the ports. The required local Euler response is

`θ_(a,p)(z)=(1−p^(−(1/2+a−iz)))/(1−p^(−(1/2−a−iz)))`.

At `z=iy`, `y>1/2+a`, both exponents lie in the absolute-convergence region and `θ_(a,p)(iy)>1`: its numerator exceeds its positive denominator. Thus this exact port fails the necessary contractivity condition. This is a direct identity/sign audit of the specified port, not a numerical experiment or a new global no-go theorem. The same issue already appears with the 2/3 toy.

**Decision:** stop the independent-passive-port architecture. A coupled construction must make the archimedean gamma and polynomial completion participate in the energy balance. It cannot simply attach primes to a positive operator and invoke positivity. The first bounded task is to specify such a coupled boundary map, then verify its response identity and domain before testing a sufficient inequality. No parameter scan is justified while that map is missing. Success would establish a viable local interface; failure would reject that interface, not RH or geometric approaches generally.

## 4. Missing steps and matched controls

The proposed global object has not been constructed. Missing obligations are: explicit arithmetic coupling; complete gamma/pole realization; closed domains and boundary conditions; a justified trace/response identity beyond absolute convergence; analytic contractivity for arbitrarily small positive shifts; and control of every completion/cutoff limit. A regularization must be fixed arithmetically, with its effect proved; it cannot be chosen to delete unwanted poles.

NS47 rules out one global ordinary-L² closable square factor plus bounded remainder for the original Weil form. This proposal does not assert that factorization. If its coupling reduces to it, that implementation stops. NS57 separates bounded floors from exact positivity: finite coefficient perturbations can destroy exact positivity while retaining a bounded-floor objective. A single negative perturbed test does not refute a bounded-floor method.

Davenport–Heilbronn shares completed functional symmetry but lacks this positive degree-one Euler product and the original gamma data; it is not a matched control for an Euler-specific realization. It is matched against a proposed generic rule deriving passivity from symmetry alone, which must fail at an uncancelled shifted off-line zero. NS57 finite-weight and NS101 reciprocal-dilation controls alter the specified Euler/theta data. Any later claimed arithmetic mechanism must state precisely which identities they lose. No numerical control pass is claimed here; a future sufficient inequality requires an actual candidate screen first.

## 5. Relation to modern spectral work

[Connes–Consani–Moscovici, Zeta Spectral Triples](https://arxiv.org/abs/2511.22755), proposes self-adjoint finite-scale constructions and identifies convergence of normalized determinants toward Xi as a missing proof. Their [semilocal prolate work](https://arxiv.org/abs/2310.18423) supplies arithmetic operator structures and stability of Sonin spaces under enlarging the places. These are substantive precedents, not our missing uniform estimate. [Connes' adelic trace-formula paper](https://arxiv.org/abs/math/9811068) also explicitly distinguishes critical zeros as absorption spectrum from possible noncritical resonances. A self-adjoint visible spectrum does not eliminate an unaccounted resonance sector.

**Recommendation:** retain the explicit four-dimensional oscillator as a transparent arithmetic building block and the coupled scattering realization as a specification task. Reject the independent passive prime cascade. Do not rename either the existing Suzuki criterion or the unchanged CCM convergence obligation as a new RH route.

**Final wall check: Same open gap**, OPERATOR-BRIDGES/CCM-LIMIT. One concrete local architecture is rejected; the coupled arithmetic realization and RH remain open.

## Bounded cross-review record

The symplectic-lane agent independently checked the finite/infinite oscillator domains and trace half-planes, shifted response, pole location and cancellation avoidance, and the exact Euler-port modulus rejection. It also checked the cited Suzuki and CCM abstracts; no major or minor correction was identified. This validates the displayed local calculations and proposal scope, not the unconstructed coupling or historical proofs. This lane reciprocally checked the symplectic draft's local Reeb identities, return-map signs, repetition weights and six-dimensional grading shift; no defect was found in that bounded check.

The arithmetic-lane review found a minor sign-convention mismatch with Suzuki's canonical-system display; the displayed equation was corrected to his `Y′=zJHY` convention. That review found no major issue in the other stated calculations. The known innerness range `a≥1/2` is broader than the cited explicit construction range `a>1`; neither supplies the required small-shift extension.
