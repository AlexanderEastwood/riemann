# Adversarial review: scoped meta-obstructions (v1.39)

**Status:** independent proof review, 2026-09-21. No G2 or RH sign gap is closed. This review does not certify publication readiness or worldwide novelty.

## 1. The original informal assertion needs two distinct definitions

“Insensitive to the arithmetic location of negative mass” is not a mathematical hypothesis. In particular, the following are different:

1. invariance under domain-preserving unitary rotations of the ambient spectral operator, while fixing finitely many physical observations;
2. replacing realizable physical Fourier densities by a larger class of nonnegative densities that contains the explicit v1.37 forbidden probe;
3. invariance under measure-preserving rearrangements of the frequency variable;
4. using ordinary operator norms, Schatten quantities, primitive drawdowns, or concentration operators.

The proposed arguments prove (1) and (2). They do not automatically prove (3), and they do not identify all instances of (4) with either proved class. This restriction is essential, not cosmetic.

## 2. Protected finite-head orientation theorem: proof check

Let `M=M_b` be multiplication by a real, even symbol on the ambient frequency Hilbert space, bounded below by its finite essential infimum `m`. Work either on the full space or within one parity sector. Let `J=F_a` be the zero-extension Fourier isometry from the physical interval `(-a,a)`, in the unitary normalization. Require a dense infinite-dimensional physical smooth core whose transforms belong to `D(M)`; the manuscript's logarithmic-growth symbol has this property.

Let `S` be an arbitrary finite-dimensional ambient subspace. Choose an ordinary-unit smooth physical vector `f` such that `h=Jf` is orthogonal to `S` and to every required finite-dimensional physical source constraint. This is possible because finitely many linear constraints cannot annihilate the infinite-dimensional smooth core.

For any `r>m`, there is a finite bounded spectral band lying below `r` whose spectral subspace is infinite-dimensional: a positive-measure sublevel set for a Lebesgue multiplication operator has this property, and it can be intersected with a bounded spectral band without losing all its measure. Choose an ordinary-unit vector `v` in that band orthogonal to `S`. Both `h` and `v` lie in `D(M)`.

There is a unitary `U` which sends `h` to `v`, is the identity off `span{h,v}`, and fixes `S` pointwise. This is an ordinary two-dimensional unitary extension; no positivity assumption is used. Consequently

`<U* M U Jf,Jf> = <Mv,v> < r`.

The lower bound `M >= m I` holds under every such conjugation. Therefore the infimum of the ordinary Rayleigh quotient over these orientations and admissible physical test vectors is exactly `m`.

**Domain check.** Since the range of `U-I` is contained in the finite-dimensional subspace `span{h,v} ⊂ D(M)`, both `U` and `U*` preserve `D(M)`. Moreover `U* M U-M` extends to a bounded finite-rank selfadjoint operator: the terms involving `M(U-I)` are finite-rank bounded, and `(U*-I)M` has a bounded extension by selfadjointness and the membership of the finite range vectors in `D(M)`. The form domain is likewise preserved. Thus this counterorientation does not rely on changing the physical form core or admitting an undefined test.

**Finite observations.** If a finite-dimensional physical head `E` satisfies `JE ⊂ D(M)`, take `S` to contain `JE+MJE`. Then for every `e∈E`,

`U* M U Je = MJe`.

The complete ambient action on the head is unchanged, not merely its compressed quadratic matrix. This includes the actual source and its complete residual when they belong to `E`. Further finitely many graph observations can be included in `S` whenever their domain membership is justified.

**Parity check.** Because `b` is even, carry out the construction inside the even or odd ambient sector and extend by the identity on the other sector. If the protected data mix parity, first enlarge `S` by reflection; it remains finite-dimensional. The corresponding spectral subspace below `r` remains infinite-dimensional in either parity.

**Scope limitation.** In general `U* M_b U` is not a multiplication operator and does not arise from a rearranged prime configuration. The theorem concerns estimates that are sound for the whole explicitly defined orientation class. It cannot be advertised as a theorem about all rearrangement-invariant estimates for multiplication symbols.

For the actual symbol, `cor:v137-scalar-no-go` gives `ess inf beta_a → -∞` (continuity equates infimum and essential infimum). Thus a lower certificate valid for every protected orientation cannot provide a uniform finite floor, including on any cofinal family. This last statement uses the existing unconditional divergence theorem, not an assumption of RH.

## 3. Probe-saturated density relaxation: proof check

Let `w` be exactly the nonnegative smooth v1.37 probe, with integral `2π`, supremum at most one, and total variation two. Fix one positive nontrivial zero ordinate `gamma_0`, and define

`p_a(xi) = (a/pi) w(2a(xi-gamma_0))`,

`p_a^ev(xi) = (p_a(xi)+p_a(-xi))/2`.

The symmetrization is necessary for a density relaxation intended to reflect individual parity sectors. Since `beta_a` is even, it does not change the pairing with the symbol. Direct change of variables gives

* integral `p_a^ev = 1`;
* `0 <= p_a^ev <= a/pi`;
* total variation at most `2a/pi`, hence at most `2a`;
* smooth compact support, so all symbol integrals here are finite.

Every ordinary-unit physical vector in either parity has an even Fourier density satisfying the same mass and supremum constraints and the weaker variation bound `TV(|F_a f|²) <= 2a`. Indeed the support length gives the supremum bound by Cauchy-Schwarz, and Plancherel gives `||F'_a f||_2=||xf||_2<=a`, followed by the product derivative estimate. No source-to-physical norm transfer occurs.

Consequently the explicit class

`R_a = {p even, p>=0, integral p=1, ||p||_infinity<=a/pi, TV(p)<=2a}`

(with finite symbol integral) contains the actual normalized parity densities and the symmetrized forbidden probe. The same conclusion holds after removing the actual source, provided the relaxation still contains all the remaining physical densities; orthogonality to that source is not encoded by these three scalar constraints.

Suppose a nonnegative budget `B_a` is sound on all of `R_a`, i.e. `integral beta_a p >= -B_a` for every such density. A bounded cofinal subsequence of `B_a` would give the complete finite physical lower floor and hence RH by `prop:v136-bounded-floor`. If the physical class is the complete rank-one complement instead, use `cor:v136-complement-floor`, retaining both parities and the already established vanishing source residual.

Under RH, the exact v1.37 probe estimate gives eventually

`integral beta_a p_a^ev <= -a/(6 pi²)`.

Thus the hypothetical bounded cofinal subsequence is impossible. Since `B_a>=0`, absence of a bounded cofinal subsequence is exactly `B_a→+∞`.

**Parity quantifier warning.** With separate sector budgets the argument gives unconditional divergence of `max(B_a^even,B_a^odd)`, unless an independent theorem says one sector alone implies RH. Under RH each sector's probe-saturated budget separately has the displayed linear lower bound. Do not silently turn that conditional assertion into unconditional divergence for each isolated sector.

**Regularity warning.** The probe passes precisely the mass, supremum and total-variation constraints above. It does not pass all possible physical differential constraints. For example, an actual physical density has the pointwise derivative bound `||(|F_a f|²)'||_infinity <= 2a²/(sqrt(3) pi)`, whereas the narrowly mollified probe generally violates such a sharp pointwise derivative bound. An estimate using more physical information is outside this tested relaxation unless probe inclusion is separately verified.

## 4. Full-histogram relaxation and its limitation

For a fixed lower-bounded coercive symbol, the bathtub principle gives the exact mass-cap optimization

`inf_{p>=0, integral p=1, p<=a/pi} integral beta_a p`

`= (a/pi) integral_0^(pi/a) beta_a^uparrow(s) ds`,

where the increasing rearrangement is with respect to Lebesgue measure. A partial filling of a level set handles atoms in the distribution of symbol values. Evenness causes no loss because the symbol is even and symmetrization preserves admissibility and energy. This formula applies to the supremum-cap class, without asserting an identical formula after adding total variation.

This is a genuinely strong histogram-only benchmark: it retains the full value distribution rather than just the depth or total mass. It is nevertheless probe-saturated, so its nonnegative negative-floor budget diverges by the previous argument for the actual arithmetic family. This does not assert that every frequency-rearrangement-invariant estimate must equal the mass-cap optimization; an estimate might retain further realizability information.

## 5. Counterexample to an overbroad claim

Take arbitrary `D_a→∞` and any measurable symmetric set with

`|E_a| = pi/[2a(D_a+1)]`.

Set `b_a = 1-(D_a+1)1_{E_a}`. For every ordinary physical test supported in `[-a,a]`, irrespective of the location or shape of `E_a`,

`integral b_a |F_a f|² >= [1-(D_a+1)(a/pi)|E_a|] ||f||² = (1/2)||f||²`.

This is a scalar, location-insensitive positive lower bound even though `ess inf b_a=-D_a→-∞`. It refutes a generic claim based on negative depth divergence alone. It does not refute the actual-symbol result: this model does not have the negative arithmetic probe pairing from v1.37 needed for that argument.

## 6. Coverage of the ten recorded closures

| Recorded route | Consequence of these meta-obstructions? |
|---|---|
| Scalar signed primitive | Its sound budget is reproduced on the mass/variation relaxation; direct continuation of v1.37, not a wholly new closure. |
| Unsigned prime-norm domination | Covered only for an implementation proved to be orientation-blind with the stated protected data; the existing arithmetic prime essential-norm theorem is a different statement. |
| Norm contraction | Not automatically covered; its existing counterexample concerns a different scalar estimate. |
| Negative-only Schatten/Hilbert-Schmidt | Not automatically covered: source-compressed concentration Schatten values retain locations through Fourier kernels. |
| Basis/sampling dominance | Not automatically covered; sampled correlations and graph defects are additional geometric inputs. |
| Scalar far majorant | Its exponential-cutoff obstruction is not implied by a no-go for cofinal floors; the cutoff-cost theorem remains separate. |
| Dyadic block metrics | Not automatically covered; block norms retain a chosen physical partition, and the existing result is a particular certified failed criterion. |
| Positive flat-top smoothing | Not covered: this is a rigidity theorem about characteristic functions, not a lower-floor estimator. |
| Reciprocal-band commutation | Not covered: a nonvanishing commutator is a geometric product obstruction. |
| Cotlar/atomization | Not covered: persistent cross channels and exact regrouping address operator products rather than a blind scalar floor. |

The pointwise minimum and the stronger full-histogram mass-cap estimator are directly ruled out, but the pointwise estimator is not an additional member of the table's ten-node inventory. A claim that the theorem explains all ten closures would overstate its logical coverage.

## 7. Review conclusion

Both scoped theorems survive the domain, parity, finite-source, and bounded-floor checks above. The useful new conclusion is precise: finite protected head information does not rescue an orientation-universal estimate, and the actual arithmetic symbol defeats every density relaxation that still admits the explicit forbidden probes, including the complete-histogram mass-cap optimization and the mass/supremum/variation relaxation. Neither theorem supplies a sign mechanism or identifies the physical low-concentration subspace with the entire source complement. The signed concentration operator remains outside these blindness hypotheses and remains open.

## 8. Review of the exact integrated proof text

Reviewed file: `evidence/v139/new_section.tex`.

Reviewed SHA-256: `77616f0f82cbdeb26cb28a383da9438b8c2ed41d5dbb7faef5950e7bf2f669ce`.

**Verdict: passes this adversarial mathematical review as a pair of scoped obstructions.** No correction to the reviewed proof text is requested. This verdict does not establish worldwide novelty, publication readiness, G2, or RH. It is tied to the file hash above.

Checks against the exact text:

* The logarithmic physical form domain is correct for the fixed-window asymptotic `beta_a(xi)=log(2+|xi|)+O_a(1)`. The orientation construction preserves both the operator domain and the form domain, rather than silently changing admissible physical tests.
* For a real, lower-bounded measurable symbol with finite-measure sublevel sets, the bathtub threshold exists: the sublevel measures increase to infinity because the symbol is finite almost everywhere on the infinite Lebesgue space. The closed threshold level has finite measure, as it is contained in a slightly higher strict sublevel. Partial filling of that level supplies the required mass. No continuity or strict monotonicity of the distribution is required.
* The protected-orientation infimum has the quantifiers in the correct order. The same finite protected subspace is held fixed, while the adversarial orientation and smooth physical witness may vary. The theorem does not claim one orientation works for every physical witness.
* Finite-rank conjugation preserves the whole protected action when both `JE` and `MJE` are fixed. Its general conjugate is explicitly allowed to leave the multiplier class. Therefore no rearranged-prime interpretation is being smuggled into the conclusion.
* The symmetrized probe has exactly unit mass and gives `(a/pi)J_a`. The conditional constant `a/(6 pi²)` is therefore correct. The unconditional argument uses a bounded cofinal subsequence to obtain RH, not an assumed RH rate.
* The complete physical space, or its complete source complement with both parities and the established vanishing residual, is explicitly required. The text correctly refuses to infer an unconditional obstruction from a single parity alone.
* In the comparison model, the absent ingredient is the negative arithmetic probe pairing, not probe inclusion in the relaxation. The exact proof now makes this distinction correctly.
* The scope statement does not claim that all ten existing closures follow from one insensitivity property. The surviving geometric concentration estimate is explicitly excluded from the proved no-go classes.
