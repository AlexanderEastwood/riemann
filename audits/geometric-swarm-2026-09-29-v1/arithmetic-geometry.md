# Arithmetic geometry construction lane — 2026-09-29, v1

Internal construction/admission note. Parent reviewed current main `b5bd5fa`, all 104 conclusion records and 14 continuation demands. This lane read the refreshed AGENTS, relevant register entries, controls, NS94/100/101 accounts and PR68 geometry caveat. This is not a historical proof revalidation. No theorem, numerical screen, research row, thaw or novelty claim is made.

**Wall check: Same open gap.** Closest input: OPERATOR-BRIDGES, function-field/Hodge component; destination: WEIL-FLOOR. What changes: two explicit possible source objects and their first construction tests are specified. Their arithmetic-to-Weil transfer remains absent. NS94 excludes its symmetry/count inference, not these constructions. PR68 explicitly leaves arithmetic geometry as an independent construction program.

| Candidate | Existing object and dimension | Speculative addition | First decision-changing prerequisite |
|---|---|---|---|
| A. Labeled adelic correspondence surface | Scaling site and its complex lift; toy `E_p × E_q`, complex dimension 2, real dimension 4 | Global correspondence pairing retaining orbit labels and the infinite place | Can its local trace retain primitive prime periods without introducing mixed-prime trace support? |
| B. Adelic dilation-energy surface | `Y = P¹_Q × P¹_Q`, complex dimension 2; integral model has Krull dimension 3 | An explicit map from complete Weil tests to integrable adelic metrics with a uniform transfer remainder | Does the explicit metric family retain independent local valuation information after intersection? |

## A. Labeled adelic correspondence surface

**Established starting point.** Connes–Consani construct the scaling site and prove a Riemann–Roch theorem on individual prime periodic orbits, with real-valued dimensions. Their later paper constructs an adelic complex lift using elliptic curves with triangular structures and isogenies. Neither cited theorem is a global positivity transfer to the repository's Weil forms. Sources: [Geometry of the scaling site](https://arxiv.org/abs/1603.03191); [Complex lift](https://arxiv.org/html/1805.10501v1).

**Concrete toy.** For a prime p, set `E_p = C*/p^Z = C/(2πi Z + log(p) Z)`. For distinct p,q, `S_pq = E_p × E_q` is a genuine complex surface, hence a real four-dimensional manifold. This ordinary product is our toy, not an identification with Connes–Consani's full adelic object. Extra products increase real dimension by two per elliptic factor; dimension alone supplies no arithmetic rigidity.

An essential distinction: multiplication `z ↦ p^k z` becomes the identity on `E_p`. Its ordinary graph cannot represent distinct prime powers. The endomorphism `[n]: z ↦ z^n` instead has degree n² and is not a substitute for a p^k return. A simultaneous positive-real scaling flow on both factors also has no common positive period: `log p/log q` is irrational. We therefore propose retaining separate prime correspondences and *labeled arrows before forgetting the covering*: a return carries the deck label k and elapsed time `k log p`, even when its underlying map is the identity. A groupoid or suspension-level correspondence must retain these data. Its global intersection theory is not constructed here.

**Arithmetic requirement.** For a finite prime set S and smooth compactly supported h on positive time, the desired local orbit distribution is

`L_S(h) = Σ_(p∈S) Σ_(k≥1) (log p) h(k log p)`.

This is the prime-power distribution of `−ζ'/ζ`, before changing to centered Weil normalization. On that convention, an `e^(−t/2)` factor appears in the prime contribution; its location must be fixed in the transfer, not silently absorbed. A global trace needs the exact infinite-place, pole and endpoint contributions too. In particular, support at `log(pq)` is forbidden in this *logarithmic-derivative trace* for distinct primes. Mixed terms in a convolution or intersection pairing can be legitimate; these are different assertions.

The original input is the integral multiplicative/adelic structure giving prime valuations, primitive periods and the exact archimedean factor. Generic reflection symmetry does not give it. Assigning `log p` by hand only recreates an explicit formula; it is not a positivity estimate.

**Hoped-for mechanism.** Build a primitive correspondence class `D_(a,f)` and real intersection form I with `I(D,D)≤0`, together with the common transfer specification below. Neither primitive reduction, the required global I, nor compatibility of its completion with source restrictions is supplied by local tropical Riemann–Roch. These are explicit missing construction steps, followed by the separate uniform remainder estimate.

**First test: labeled two-prime trace compatibility.** Specify the arrow composition, trace and descent for p=2, q=3 at the symbolic level. Determine whether repeated identity maps remain distinct returns, and whether forming the surface introduces a nonzero trace contribution at `log 6`. A successful construction must derive the required primitive-support distinction from its trace operation; a direct sum of separately prescribed prime distributions would not test gluing. Failure rejects that quotient/trace construction. Success justifies studying global compatibility and the infinite place; it proves neither Hodge positivity nor RH. This is a proposed construction audit, not an executed test or a new sufficient inequality.

## B. Adelic dilation-energy surface

**Explicit existing object.** Let `Y=P¹_Q×P¹_Q`, with projections π₁,π₂, and use its regular integral model over Z. An arithmetic surface such as `P¹_Z` has Krull dimension 2 and complex fiber dimension 1; it is not a real 4-manifold. Our product's complex fiber has real dimension 4, while its integral model has Krull dimension 3.

Take `φ_n([x₀:x₁])=[n x₀:x₁]` for positive integers n, and the standard adelically metrized `L=O(1)`: model/max metric at finite places and Fubini–Study metric at infinity. Define

`A_n = φ_n* L̄ − L̄`,   `M_n = π₁* A_n − π₂* A_n`.

These are differences of nef adelic line bundles; their underlying line bundles are trivial. Fix `|p|_p=p^(−1)` and standard Q place weights. On the chart `x₁≠0`, define the metric potential by `u_(n,v)=−log(||x₁||_(φ_n*L)/||x₁||_L)`. At finite place v it is

`u_(n,v)(x)=log[max(|n x₀|_v,|x₁|_v)/max(|x₀|_v,|x₁|_v)]`.

This gives explicit local dependence on `v_p(n)`, not fitted zeta-zero data. At infinity use the corresponding square-root Euclidean norms. On Y the potential is `u_(n,v)(x)−u_(n,v)(y)`. Set `H̄=π₁*L̄+π₂*L̄` and form finite real linear combinations of the M_n, using the continuous extension of quadratic intersection from rational coefficients.

**Established sign and its limit.** Yuan–Zhang's arithmetic Hodge index theorem applies to an integrable adelic M, nef H with big underlying H, and `M·H=0`: it gives `M̄²·H̄≤0`. Here underlying triviality supplies that orthogonality. This is a usable source of positive energy `−M̄²·H̄`, not a theorem about the zeta function. [Theorem 1.3](https://arxiv.org/html/1304.3538v1). Ordinary divisor classes alone erase this family's information; the metrics carry it.

**Speculative adaptation.** Seek a fixed, arithmetic prescription assigning complete real Weil tests f to limits of `Σ c_n(a,f) M_n`. The coefficients must be prescribed independently of the desired sign. Valuation/divisor identities, potentially the exact Möbius extraction `Λ(n)=Σ_(d|n) μ(d)log(n/d)`, would enter a derivation of the transfer, not merely be labels on a generic positive Gram matrix. No coefficient prescription or such identity is supplied here. Integrability and convergence of the assigned metrics remain required.

**First test: local-information survival.** Derive the symbolic local pairings of the specified M₂,M₃,M₆, retaining the 2-adic, 3-adic and archimedean terms separately. Check whether valuation structure survives **after intersection and quotient by constant/base-pullback metric classes**, or whether the proposed assignment reduces to a generic metric depending only on a single real dilation parameter. Merely observing that the displayed local potentials are nonzero does not pass this test. Success would retain this metric family for a transfer-formula investigation; collapse would reject it as a source of independent arithmetic information. This is an information/admissibility test, not a finite sign screen, and no calculation has been performed.

## Complete conditional edge and matched controls

For either candidate the exact required edge is: for every window a, every real f in the **complete actual even source complement or odd sector**, construct the specified class Jₐf, prove its sign theorem and

`qₐ[f] = −I(Jₐf,Jₐf) + Rₐ[f]`,   `|Rₐ[f]| ≤ C ||f||²`,

with one finite C independent of a and f. Include all prime, pole, exterior and cross terms, establish completion/density and the repository's source transfer; then `qₐ[f]≥−C||f||²` supplies WEIL-FLOOR and its established v1.36 RH implication. No positive spectral gap is requested. An exact identity is the C=0 case. The transfer and remainder are absent, and asking for them alone would merely rename the same open input. The independent first tests above concern whether the *specific source objects* retain the data such a transfer would require.

**NS47 implementation stop:** if `−I(Jf,Jf)` is the squared norm of one global ordinary-L² closable map J, the displayed bounded-remainder representation is excluded by NS47. A viable adaptation must instead retain window-dependent factors that do not glue to that map, or a completion/transfer nonclosable in ordinary L², while still proving the common ordinary-norm remainder bound. Moving to an arithmetic metric does not automatically escape this result. The present window-indexed construction specification does not assert the excluded global closability.

Davenport–Heilbronn does not share the proposed exact Q-adelic/one-lattice and gamma data; NS101 changes the original coefficients. Thus neither refutes the complete proposed arithmetic implication on its stated premises. Both remain mandatory stress tests of any later *generic* transfer argument. NS100 rules out its per-slice theta positivity shortcut, which is not used here. No control is claimed passed. A finite prime-weight perturbation (NS57) must change the proposed exact arithmetic identity; otherwise an asserted **exact nonnegativity** transfer is suspect. NS57 does not exclude a robust bounded-floor transfer. Source-local positivity alone, extra dimensions, and a valid pairing on an unrelated space supply no RH conclusion.

**Final wall: Same open gap — OPERATOR-BRIDGES/WEIL-FLOOR.** Two construction specifications and bounded admissibility questions are ready; no missing global arithmetic estimate is resolved.

## Cross-review of spectral-geometry.md

Scope: adversarial review of the displayed oscillator, response, elementary sign diagnostic and Suzuki overlap; no numerical replay or full upstream audit. **No MAJOR finding** in the requested implications.

- The response orientation agrees with [Suzuki, equation (1.7)](https://arxiv.org/html/1204.1827v2): lower shift divided by upper shift. For a denominator zero ρ, `z=i(ρ−1/2−a)` has imaginary part `Re ρ−1/2−a`; its numerator is `ξ(ρ−2a)`. Choosing a sufficiently small positive shift avoids other zeros by discreteness. The all-positive-shift criterion is sufficient and is Suzuki's stated family; arbitrarily small shifts suffice for this contradiction, whereas one safe fixed shift does not.
- At `z=iy`, `y>1/2+a`, the local exponents are `σ±=1/2±a+y>1`. Thus `1−p^(−σ+) > 1−p^(−σ−)>0`, giving the stated local response greater than one. This rejects the exact independently passive port, not completed global coupling.
- The two oscillator modes have four real classical phase coordinates and an infinite-dimensional quantum Hilbert space. Vacuum-subtracted energies, the weighted domain and the finite-prime trace domain are correct. The all-prime construction is rigorously defined by `log n` on ℓ²(N), avoiding an unrenormalized infinite vacuum-energy sum. Its trace is ζ only for `Re s>1`; spectral zeros do not follow.
- Suzuki's explicit construction is indeed stated for `a>1`. Innerness/Hermite–Biehler inequalities are already known unconditionally for `a≥1/2` (paper §1.2); this does not supply the explicit extension through all small positive shifts. The draft correctly disclaims novelty.
- **MINOR convention clarification:** Suzuki writes `Y′=zJH Y` for `J=[[0,−1],[1,0]]`, whereas the draft writes `JY′=zHY` with that J. These differ by a sign. Either convention can be used, but an exact response realization must explicitly transform the B-component/response or orientation; aligning the displayed differential equation with Suzuki would avoid ambiguity. This does not invalidate the independent pole or prime-port calculation.

Arithmetic-lane peer review from geometry_symplectic found no MAJOR; its two MINOR requests (fixed local metric sign/normalization and post-intersection information test) are incorporated above. The simultaneous-product-flow qualification is also incorporated. These agent reviews are not external specialist validation.
