# NS-4b — coverage of the ten closed routes by the two v1.39 meta-obstructions

Analysis (coverage table); not a certificate. 2026-09-21.

Manuscript: `manuscript/fixed_space_prime_action_v1.tex`, v1.40, at commit `b185969`
(all line numbers below refer to that file at that commit). Evidence read:
`evidence/v139/{research_report.md, adversarial_review.md, new_section.tex,
check_exact_models.py, exact_model_results.json}`.

**Result in one line.** `thm:v139-probe-relaxation` covers **1** of the ten closures
(scalar signed primitive); `thm:v139-protected-orbit` covers **0** of the ten cleanly
(it covers the pointwise-minimum estimator, which is not one of the ten nodes, and has a
thematic but non-logical parallel with prime-norm domination); **9** are **neither**;
the live mechanism `prop:v131-concentration` lies **outside both** classes, violating
hypothesis (A2) of the first theorem and the orientation-universality requirement (B3)
of the second. The manuscript's own scoping sentence (lines 10616–10623) is confirmed
and sharpened: the "pointwise and primitive closures" are in the displayed classes, but
the primitive is in the *first* class only, not the second.

Nothing here is a claim about G2 or RH.

---

## 0. The two theorems, reduced to checkable hypotheses

### (A) `thm:v139-probe-relaxation` (lines 10418–10465)

An estimate is an instance of (A) iff it can be written as a scalar budget
`B_a >= 0` with

- **(A1) class.** There is a set `R_a` of even nonnegative probability densities on
  frequency space containing every physical density
  `p_f(xi) = (|F_a f(xi)|^2 + |F_a f(-xi)|^2)/2`, `||f|| = 1`, from **the full space
  `L^2(I_a)` or the complete rank-one source complement `Q_a L^2(I_a)`, both parities**
  (lines 10394–10398, 10420–10423).
- **(A2) probe.** For all large `a`, `R_a` also contains the symmetrized cutoff probe
  `p*_a` of `eq:v139-probe-density` (lines 10424–10428), built from `lem:v137-probe`
  (lines 10181–10226) centred at a critical-zero ordinate `gamma_0`.
- **(A3) soundness.** `int beta_a p >= -B_a` for every `p in R_a`
  (`eq:v139-relaxed-error`, lines 10432–10434), with `beta_a` the exact symbol
  `eq:v130-beta` (line 8822) / `eq:v135-full-symbol` (line 9674).

Conclusion: `B_a -> +infinity`; no uniform finite floor along any cofinal family.
Mechanism: bounded cofinal `B` + (A1) => bounded floor => RH
(`prop:v136-bounded-floor`, lines 10036–10084, or `cor:v136-complement-floor`,
lines 10086–10110) => probe pairing `int beta_a p*_a = (a/pi) J_a <= -a/(6 pi^2)`
(`prop:v137-conditional-mass`, lines 10228–10320) => contradiction.

The explicit eligible relaxation is `R_a = {even p in W^{1,1}: p>=0, int p = 1,
||p||_inf <= a/pi, TV(p) <= 2a}` (`eq:v139-density-constraints`, lines 10407–10411).
The strongest mass-and-height-only bound is the bathtub value `ell_a^cap`
(`eq:v139-bathtub`, lines 10483–10488), which the theorem drives to `-infinity`
(`eq:v139-cap-divergence`, line 10502).

Quantifier warning quoted from the text (lines 10467–10470): "The quantifier over both
parities is essential to this proof. For separate parity errors it proves unconditional
divergence of their maximum, not unconditional divergence of each merely from one
sector's boundedness."

### (B) `thm:v139-protected-orbit` (lines 10517–10572)

Setting: `M` = multiplication by the exact `beta_a` on **all of `L^2(R)`** (not on the
Paley–Wiener range); `S` a finite-dimensional frequency subspace; `U_S` = unitaries
fixing `S` pointwise, with `U - I` of finite rank, preserving `D(M)` (lines 10519–10523).
Statement `eq:v139-orbit-edge` (lines 10524–10530):

    inf_{U in U_S}  inf_{f in C_c^inf(I_a), ||f||=1, F_a f perp S}  <U* M U F_a f, F_a f>  =  ess inf beta_a.

With `S ⊇ F_a E + M F_a E` for any finite physical head `E`, every allowed `U` preserves
the complete action on the protected columns (`eq:v139-protected-columns`,
lines 10535–10537).

An estimate is an instance of (B) iff

- **(B1) object.** It is a lower bound for the compression of the multiplier `M` to the
  physical Fourier image (a Rayleigh-value bound on `Ran F_a` or its complement).
- **(B2) inputs.** Its inputs are spectral data of `M` (unitary invariants of `beta_a`,
  e.g. `ess inf`, the value distribution) plus **finitely many** protected graph columns
  `F_a e, M F_a e`.
- **(B3) orientation universality.** Its claimed lower number "must remain valid after
  every unitary conjugation `U* M U`" in `U_S` (lines 10538–10541: "a sound universal
  compression bound insensitive to all the allowed orientations, even after retaining
  these exact columns, cannot exceed `ess inf beta_a`").

Conclusion: the bound is `<= ess inf beta_a -> -infinity` (by `cor:v137-scalar-no-go`,
lines 10322–10350, invoked at line 10571).

Scope sentence quoted from the text (lines 10587–10592): "`U*MU` generally is *not* a
multiplication operator. The theorem rules out bounds required to be valid on that larger
operator class. It does not construct a rearranged prime sequence, a negative arithmetic
Weil test, or a no-go for methods retaining the multiplier's physical support geometry."
And (lines 10581–10582): "This does not preserve the action on an infinite physical
block."

### Ambiguities in the hypotheses (quoted, not resolved)

1. **(B3) is a property of a proof, not of a number.** The theorem defines a double
   infimum; whether a given closure "is required to be valid for every `U`" depends on
   which inputs its proof uses. The adversarial review (`adversarial_review.md` §6) makes
   the same point for prime-norm domination: "Covered only for an implementation proved
   to be orientation-blind with the stated protected data". I treat an estimate as in (B)
   only when its proof visibly uses nothing but (B2) inputs.
2. **(A1) requires the full space or the rank-one complement.** Five of the ten closures
   are stated on a finite-codimension Fourier tail `Q_N L^2(0,L)` (prime norm, norm
   contraction, v120 Schatten, far majorant, block metrics). The text does not say
   whether (A) extends to such tails. It would need `||W P_N|| -> 0` for the removed
   head (`prop:v118-gap-free`, lines 6011–6030), which is false for a general Fourier
   head, so I count these as outside (A1) as stated.
3. **"Instance" could mean "proof is a special case" or "conclusion is a corollary".**
   I record both readings where they differ.
4. **Parity.** (A) needs both parities in `R_a`; `prop:v131-concentration` is stated in
   the even sector (line 9002) and extended to both parities only in
   `prop:v135-both-parities` (lines 9671–9701). This matters for (d) below only in that
   the even-sector version is, if anything, *further* from (A1).

---

## 1. Coverage table

| # | Route (map node) | Proposition(s), lines | (a) class closed and mechanism | (b) in (A)? | (b) in (B)? | (c) true cause if neither |
|---|---|---|---|---|---|---|
| 1 | unsigned prime-norm domination | `prop:v119-prime-essential` 6181–6234; `prop:v119-prime-scale` 6236–6292; target `prop:v115-sharp-tail` 4304–4326; `eq:v119-unsigned-cutoff` 6298–6301 | Closed: any tail bound of the form `QW(f,f) >= {arch diagonal − M_λ − Schur errors}‖f‖²` on `Q_N L²(0,L)`, where the *signed* prime term is replaced by `−‖T_pr‖‖f‖²` with `T_pr` the **positive-coefficient** truncated-translation sum. Mechanism: simultaneous recurrence of the finitely many phases `e^{2πik log m/L}` gives modulations `M_k` with `M_k* T_pr M_k → T_pr` in norm and `M_k f ⇀ 0`, so `‖Q T_pr Q‖ = ‖T_pr‖` for every finite-rank `P` and `‖Q(T_pr − C)Q‖ ≥ ‖T_pr‖` for every compact `C` (essential norm = norm); PNT gives `‖T_pr‖ = (1+o(1))λ`. Consequence: exponential Fourier cutoff `log((N+1)/L) > (1+o(1))λ`. | **No.** (A1) fails: the estimate lives on a finite-codimension tail, not the full space or rank-one complement. Even a full-space version ("`β_a ≥ arch(ξ) − sup|𝔯_a|` pointwise") *would* be an (A)-type pointwise-minorant budget, but it diverges for the elementary unconditional reason `sup|𝔯_a| ~ λ` (PNT), not for (A)'s reason (RH-conditional probe pairing). Coverage in that sense would be vacuous and misattribute the cause. | **No, with a thematic parallel.** Parallel: both say "finite-rank protection does not move an essential quantity". Not an instance: (i) (B1) fails — the object is the *unsigned* operator `T_pr` and its norm (top of spectrum of |prime symbol|), not the compression edge of the signed `M`; (ii) (B3) fails — the v115 estimate uses the archimedean matrix entries `a_n`, `(b_n−b_m)/(n−m)` in the physical Fourier basis and their Schur row bounds, which are position data and change under `U*MU`; (iii) the v119 witnesses `M_k f` are *physical* vectors inside `L²(0,L)`, whereas (B) rotates a physical vector *out* of the Paley–Wiener range through a non-multiplier conjugate — v119 is stronger in kind for a different quantity. | Essential-norm rigidity of the unsigned prime operator under finite-rank removal (phase recurrence), plus PNT growth `‖T_pr‖ ~ λ` versus logarithmic archimedean growth → exponential cutoff cost. Unconditional, elementary; no RH input. |
| 2 | norm contraction | `prop:v120-norm-counterexample` 6538–6559; context `prop:v120-weighted-error` 6341–6362 | Closed: the **two-sided** weighted contraction `‖D^{-1/2} Q_16 (W_4 − D) Q_16 D^{-1/2}‖ ≤ 1` at `λ = 4` with the exact archimedean diagonal `D`. Mechanism: an exact dyadic even vector `v` on `17 ≤ |n| ≤ 256` with certified `QW_4(v,v)/⟨Dv,v⟩ ∈ (2.0525, 2.0526)`, i.e. the weighted remainder has Rayleigh value `> 1`. "This is a positive direction, not a negative Weil direction" (line 6558). | **No.** (A3) is a *lower* floor; the closed estimate is a two-sided norm condition that fails on the *upper* side (a harmless positive direction). No density class, fixed window `λ = 4`, Fourier-tail coordinates (A1 fails too). | **No.** (B1) fails: a two-sided weighted norm is not a compression lower bound; the orbit class preserves only `M ⪰ mI`. Fixed window, not cofinal. | The two-sided condition is strictly stronger than the one-sided target `B ⪰ −I` and is violated by a positive direction; separately `prop:v120-weighted-error` shows a dimensionless weighted error `η_λ → 0` does not convert to an ordinary error `o(1)` when the scale `C_λ ~ λ` grows (scale-conversion loss). No information-loss principle involved. |
| 3 | Schatten / Hilbert–Schmidt | `prop:v120-not-schatten` 6368–6407; `prop:v132-schatten` 9151–9226; `eq:v132-interlace` 9230–9235 | Two closures. **v120:** `D^{-1/2} T_pr D^{-1/2}` (and the full weighted remainder `𝓑`) is in no Schatten class `S_p`; mechanism: the prime diagonal `τ_n` is a finite trigonometric polynomial with positive coefficients, so `|τ_n|` has positive lower density and `Σ|τ_n/a_n|^p = ∞` since `a_n ~ log n`; Jensen on the spectral measure. Closes any global squared-entry budget. **v132:** the negative-only Schatten refinement `η_a^{(2)} = ∫_0^{D_a} min{1, tr A_E, ‖A_E‖_HS} dt` (a rigorous upper bound on the negative error via `‖A_E‖ ≤ ‖A_E‖_HS`) is not forced to vanish: in the Dirichlet model `q^mod = a²‖f'‖² − (π²/4)‖f‖²` on `H_0^1(−a,a)`, nonnegative with exact null source `u^mod`, unitary dilation makes all `A_{E(t)}` `a`-independent and the coefficient is a positive constant. Interlacing: rank-one compression cannot remove the second channel. | **No.** v132's estimate is not a density functional: `‖A_E‖_HS² = ∬_{E×E} |⟨k_ξ,k_ζ⟩|² dξdζ` (`eq:v132-hs-kernel`, line 9167) uses the sinc kernel of the Paley–Wiener projection — position data that no density constraint reproduces; it is not "sound on `R_a`" in the sense of (A3) because for a non-physical `p` there is no operator. (Only the cruder *trace* specialization `∫ min{1, tr C_E(t)} dt ≈ ∫ min{1, a|E(t)|/π} dt` is a mass-and-height bound of (A)-type; that is the v131 layer-cake diagnostic, not the recorded v132 closure.) v120: a non-membership statement, no lower floor at all. Also the v132 closure's conclusion ("does not vanish structurally, even for a nonnegative model") is not a divergence statement. | **No.** (B3) fails: `A_E = P_a F_a* 1_E F_a P_a` depends on the spectral projections `1_E` of `M` *and* the infinite-dimensional position of `Ran F_a`; under `U ∈ U_S`, `1_E → U* 1_E U` and `‖A_E‖_HS` changes. The research report says exactly this: "Concentration Schatten quantities retain frequency geometry; they are not merely multiplier spectral data." | **v132:** coupling loss — the negative-only layer-cake discards every favorable superlevel set, so even a nonnegative model with exact null source keeps an `a`-independent budget; the second concentration channel survives rank-one compression. **v120:** the prime diagonal is almost-periodic (non-decaying) and the weight `1/log n` cannot make it `ℓ^p`. |
| 4 | basis / sampling dominance | `prop:v121-complement-cancellation` 6098–6162 | Closed: the heuristic that archimedean+pole dominance `q_np` off the source makes positivity readable from basis-vector or random-vector energies. Mechanism: certified even unit `v ∈ E_64` at `λ = 3`, exactly `⊥ p_3`, with `0 < QW_3(v,v) < 3·10^{-31}` yet `q_np(v) > 0.4`, `q_pr(v) < −0.4`: coherent prime/non-prime cancellation to 31 digits inside the exact source complement. | **No.** Not a scalar budget on a density class; an existence certificate of a coherent near-null direction at a fixed window (`λ = 3`), refuting a *dominance* heuristic. The value is positive, and no cofinal object appears. | **No.** (B) protects finitely many columns and rotates the rest; this closure exhibits one specific *physical* direction with cancellation, and its point is the size of the off-diagonal correlations, not the spectral edge. The review: "sampled correlations and graph defects are additional geometric inputs." | Coupling loss: discarding off-diagonal prime/archimedean correlations (basis or sampled diagonal dominance) misses `O(1)` coherent cancellation. Fixed-window, certified. |
| 5 | scalar far majorant | `prop:v125-cutoff-cost` 8286–8313; `prop:v127-rank-barrier` 7882–7906 | Closed: the scalar diagonal far majorant with weights `g_{N+1} = (1−c){log((N+1)/L) − E_L} − κ_{λ,N}`, `κ ≥ M_φ ≥ ‖T_pr‖`: positivity forces `N+1 > L exp(M_φ/(1−c))` with `M_φ/λ → 1` (via `prop:v119-prime-scale`); polynomial-rank corrections cannot repair it (v127). Mechanism: elementary — the minorant crosses zero only where `log(n/L)` exceeds the unsigned prime constant `~ λ`. Text (lines 8305–8306): "a cost of this particular scalar diagonal majorant, not a lower bound on the cutoff required by every possible argument." | **No.** The closure is a *cutoff threshold* for a **positive** remote certificate that works at every window at exponential cost; (A)'s conclusion is that a *full-space* budget diverges and says nothing about `N`. (A1) fails (tail), and the arithmetic constant is the *unsigned* `‖T_pr‖`, so even a full-space relative would diverge for the elementary reason in row 1. The review: "Its exponential-cutoff obstruction is not implied by a no-go for cofinal floors." | **No.** The weights `g_n` are the diagonal of `M` in the physical Fourier basis (position data); (B3) fails. | Exponential cost: signed prime term replaced by its unsigned norm `(1+o(1))λ` against only logarithmic archimedean growth, so the crossover is at `n ~ L e^λ`. Zhu (arXiv:2608.24827) has the same doubly-exponential shape for a different object (see `COMPARISON.md`). |
| 6 | block metrics (v1.28) | `prop:v127-block-metric` 7916–7950; `lem:v128-comparison-obstruction` 7983–8014; `prop:v128-dyadic-fails` 8016–8071 | Closed: the infinite signed block-metric criterion (dyadic frequency blocks `I_j`, metrics `0 ≺ M_j ⪯ T_jj`, `β_jk = ‖M_j^{-1/2} T_jk M_k^{-1/2}‖`, `sup_j Σ_{k≠j} β_jk ≤ ρ < 1 ⇒ T ⪰ (1−ρ)⊕M_j`) at `λ = 5`, `N = 25`, four blocks: certified lower bounds on the pair-norm matrix give `λ_max(H_±) ≥ 1.5396, 1.6014 > 1`, so the row-sum criterion fails for **all** admissible metrics and all positive scalar row reweightings (the lemma). Mechanism: the pair-norm comparison discards joint signs and directions (exact example `T = ¼I + ¾𝟙𝟙ᵗ`, lines 8081–8089). Text (8077–8079): "concerns this fixed cutoff and partition; it does not exclude another polynomial cutoff or a family that starts at a larger window." | **No.** Operator inequality in Fourier-block coordinates on a tail with a specific partition; no density class; fixed window and partition, not cofinal. | **No.** The blocks `T_jk = Q_j W Q_k` are the matrix of `M` in a chosen physical partition; under `U ∈ U_S` they change, so (B3) fails. The information loss here (phases between blocks) is relative to a *fixed physical partition*, not to spectral data: "block norms retain a chosen physical partition" (review §6). | Coupling loss: a row-sum-of-norms (Schur/Cotlar-type) comparison is strictly lossy — a positive operator can fail it. Certified at one window and partition only. |
| 7 | flat-top smoothing | `prop:v132-flat-top` 9245–9266 | Closed: smoothing `β_a` by a **positive** probability kernel `κ` whose characteristic function `χ = 1` on an open interval containing `[−2a, 2a]` (form-exact on functions supported in `(−a,a)`). Mechanism: `χ(t) = 1` near `0` forces `κ = δ_0` (`∫(1 − cos tξ)dκ = 0` for all small `t` ⇒ `κ` concentrated at `0`). Any nontrivial form-exact flat-top kernel must change sign. | **No.** Not an estimate: a rigidity theorem for probability measures. No budget, no class. | **No.** No compression bound, no orientation class. Review: "a rigidity theorem about characteristic functions, not a lower-floor estimator." | Fourier-analytic rigidity (uniqueness of characteristic functions): convex averaging cannot preserve the form, so positivity by smoothing is a new sign problem, not a regularization. |
| 8 | reciprocal-band commutation (v1.33) | `prop:v133-leakage` 9311–9354; `prop:v133-noncommute` 9363–9432 | Closed: the hope that source-compressed concentration operators `A_E, A_F` of nested reciprocal-scale bands `E_a = [−1/(10a), 1/(10a)]`, `F_a = [−1/(5a), 1/(5a)]` asymptotically commute. Mechanism: exact Toeplitz–leakage identities `[A_E, A_F] = L_F* L_E − L_E* L_F`; after unitary dilation to `(−1,1)` the commutator converges in norm to the fixed `[C_{1/10}, C_{1/5}]`, whose norm exceeds `9·10^{-6}` by explicit Taylor expansion of the sinc kernel; the source correction is `o(1)` because `z_a ⇀ 0` after dilation and `C_c` is compact. Cofinal (`liminf`). | **No.** The closed object is an operator commutator, not a scalar budget on densities. | **No.** The commutator's value is determined by the Paley–Wiener leakage `H_E = (I − Π) 1_E J` — precisely the position of `Ran F_a` relative to the spectral projections; under `U ∈ U_S` it changes. (B3) fails; also (B1): not a compression lower bound. | Geometric: Paley–Wiener leakage (Hankel-type) does not vanish under reciprocal scaling; the leakage identities are exact. |
| 9 | Cotlar cross terms / atomization (v1.34) | `prop:v134-disjoint` 9481–9541 | Closed: Cotlar–Stein/row-sum estimates that discard cross terms between disjoint reciprocal channels, and channel atomization (`J` copies of weight `w/J`). Mechanism: `liminf ‖1_{E_a} Π_{a,u} 1_{F_a}‖ ≥ 73/(375π) > 0.0619` (explicit sinc pairing on normalized indicators; source correction `o(1)`); exact identity `Z_a* Z_a = P_a F_a* m_a F_a P_a` shows regrouping does not change the operator to be bounded. | **No.** An operator-product / cross-channel statement, not a density budget. | **No.** `Π_{a,u}` *is* the (source-compressed) projection onto `Ran F_a`, exactly the object the orbit rotates; (B3) fails. Review: "persistent cross channels and exact regrouping address operator products rather than a blind scalar floor." | Coupling loss: cross terms between disjoint channels are `O(1)` cofinally; atomization is a relabeling (the joint Gram is invariant). |
| 10 | scalar signed primitive | `prop:v134-primitive` 9558–9636; `cor:v137-scalar-no-go` 10322–10350; inputs `lem:v137-probe` 10181–10226, `prop:v137-conditional-mass` 10228–10320 | Closed: the optimal scalar decomposition `β = b + W'`, `b ≥ 0`, `‖W‖_∞ = Δ(β)/2` (drawdown `eq:v134-drawdown`), giving `∫β|F|² ≥ −aΔ(β)‖f‖²` through Bernstein `‖F'‖_2 = ‖xf‖_2 ≤ a‖f‖`, on the whole physical space (both parities). Needed `aΔ(β_a) → 0` (v1.34) or bounded (v1.36). `cor:v137` proves `aΔ(β_a) → +∞` and `inf β_a → −∞` unconditionally. Mechanism: conditional (RH) probe pairing `J_a ≤ −1/(6π)` beside a critical zero via the explicit formula, then `prop:v136-bounded-floor` turns any bounded cofinal budget into RH → contradiction. | **YES.** Verified hypothesis by hypothesis, as the manuscript itself states (lines 10509–10515). (A1): every physical `p_f` has `TV(p_f) ≤ 2a` (line 10415), so `R_a = {even p ≥ 0, ∫p = 1, TV(p) ≤ 2a}` contains all physical densities, both parities. (A2): `TV(p*_a) ≤ 2a/π ≤ 2a` (line 10447). (A3): integration by parts `∫βp = ∫bp − ∫W p' ≥ −‖W‖_∞ TV(p) = −aΔ(β)`, valid for every `p` in `R_a`, so `B_a = aΔ(β_a)` is sound. Conclusion `aΔ(β_a) → ∞` is the first limit of `eq:v137-scalar-divergence`. Under *both* readings of "instance": the v139 proof (lines 10445–10465) is the v137 proof (lines 10336–10350) with the class enlarged, and the conclusion is a corollary. Caveat quoted (10513–10515): "`Δ(b)` itself is not rearrangement invariant. Calling it distribution-only would be incorrect." | **No.** (B3) fails: the primitive bound uses `‖F'‖_2 ≤ a‖F‖_2` for `F ∈ Ran F_a`. After a rotation `U F_a f = v` with `v` a normalized indicator of a piece of a narrow deep well `{β_a < r}`, `⟨U*MU h, h⟩ = ∫β|v|² < r ≈ ess inf`, while `−aΔ` can lie strictly above `ess inf` (for a well of width `ε` and depth `D`, `Δ ≈ Dε`, so `−aΔ = −aDε ≫ −D` when `ε ≪ 1/a`). So the primitive bound is *not* sound on the orbit and is not an orientation-universal bound. | — (covered by (A)). |

**Not among the ten but worth recording.** The pointwise-minimum estimator
`β_a ≥ −η_a` (`eq:v130-pointwise`, line 8836; closed by the second limit of
`cor:v137-scalar-no-go`) is in **both** classes: in (A) with `R_a` = all even unit
densities and `B_a = −inf β_a`; in (B) because `M ⪰ (ess inf β_a) I` is invariant under
every conjugation, and (B) says this is the *best* orientation-universal bound. The
adversarial review §6 notes it is "not an additional member of the table's ten-node
inventory". So the honest tally is: (A) ∩ (B) = {pointwise minimum} (outside the ten);
(A) \ (B) = {scalar signed primitive} (row 10); (B) \ (A) = ∅ among recorded closures;
neither = rows 1–9.

---

## 2. Why the "neither" rows cluster into three causes

- **Exponential cost from the unsigned prime norm** (rows 1, 5): the arithmetic term is
  bounded by `‖T_pr‖ ~ λ` (PNT), elementary and unconditional; the closure is a cutoff
  threshold, not a divergence of a full-space budget. (A) and (B) both need the *signed*
  `β_a` and the RH-conditional probe (`prop:v137-conditional-mass`); these closures never
  touch either.
- **Coupling loss in a fixed physical coordinate system** (rows 3-v132, 4, 6, 9): the
  estimate discards correlations between blocks/channels/levels that are defined by a
  *physical* partition or by the Paley–Wiener kernel. That is an information loss, but
  not the one either theorem quantifies: (A) relaxes the *density class*, (B) relaxes the
  *orientation of the whole Paley–Wiener subspace* while keeping finitely many columns.
  Neither theorem models "keep the Paley–Wiener geometry but drop cross terms".
- **Fixed-window counterexamples and rigidity** (rows 2, 3-v120, 7, 8): a certified
  counterexample at one window (`λ = 4, 5`), a non-membership statement, a rigidity
  theorem, or an exact nonvanishing commutator. None is a cofinal scalar floor.

---

## 3. (d) The live mechanism `prop:v131-concentration` is outside both classes

Definition (lines 9006–9011): on `H_a^ev = L²_ev(−a,a)`, `P_a = I − |u_a⟩⟨u_a|`, and

    C_{a,u}(E) = P_a F_a* 1_E F_a P_a ,

a positive contraction with **no Fourier truncation**. The live criterion
`eq:v131-weighted-concentration` (lines 9051–9054): with a step minorant
`−D_a + Σ_j w_{a,j} 1_{G_{a,j}} ≤ β_a` (`eq:v131-step-minorant`),

    −D_a P_a + Σ_j w_{a,j} C_{a,u}(G_{a,j})  ⪰  −η_a P_a ,

which gives `q[f] ≥ −η_a ‖f‖²` on `P_a H_a^ev`; the both-parity form is
`prop:v135-both-parities` (lines 9671–9701); the bounded-floor target is
`cor:v136-complement-floor` (lines 10086–10110). Its exact channel form is
`eq:v133-joint-channel` (lines 9449–9453) with `Z_a* Z_a = P_a F_a* m_a F_a P_a`
(line 9505).

### Against (A): hypothesis (A2) is violated (probe inclusion)

The estimate's *output* has the shape of (A3) — a scalar floor `−η_a` on physical
vectors. But (A) requires the floor to be sound on a class `R_a` that **also contains the
probe** `p*_a`. The concentration estimate is sound exactly on the physical densities
`{p_f : f ∈ P_a L²(I_a)}` and on nothing larger: for a unit physical `f`,
`Σ_j w_j ⟨C_{a,u}(G_j) f, f⟩ = Σ_j w_j p_f(G_j)`, and the operator inequality asserts
that **every physical density puts weighted mass at least `D_a − η_a` on the good sets**.
That assertion is a statement about the operators `C_{a,u}(G_j)` — i.e. about the joint
time–frequency constraint that `|F_a f|²` is the squared modulus of an entire function of
exponential type `a`. The probe `p*_a` is compactly supported (support of width `π/a`
around `±γ_0`) and is therefore **not** a physical density: "a nonzero compactly supported
frequency density cannot be such a squared transform: the entire transform of a compact
physical function cannot vanish on a real open interval" (lines 10472–10475). For the
probe, `Σ_j w_j p*_a(G_j)` can be zero (all mass on the bad set beside a zero), so the
scalar inequality `−D_a + Σ w_j p*(G_j) ≥ −η_a` is false while the operator inequality
may still hold. Hence no `R_a` satisfying (A2) exists on which the concentration budget
`η_a` is sound: **(A2) fails**, and with it (A3) on any probe-containing class.

Put differently: (A) quantifies the loss from replacing the physical class by a larger
density class characterized by scalar constraints (mass, height, variation, histogram).
The concentration route replaces nothing — it keeps the exact physical class, encoded as
operator inequalities. This is what the manuscript means by "retains information excluded
by both relaxations" (lines 10621–10622) and what the research report §5 calls "not
merely multiplier spectral data".

### Against (B): requirement (B3) is violated (orientation universality); also (B2)

`C_{a,u}(G) = P_a F_a* 1_G F_a P_a` is built from the spectral projections `1_G` of `M`
**and** the full isometry `F_a` (an infinite-dimensional object). Under `M → U* M U`,
`U ∈ U_S`, the spectral projections become `U* 1_G U` and the operators become
`P_a F_a* U* 1_G U F_a P_a`, whose lower bounds on `P_a H` are different. Explicitly,
take the adversary's rotation from the proof (lines 10548–10560): a physical unit
`h = F_a f ⊥ S` is carried to a unit `v` supported in the sublevel set `{β_a < r}`.
Choosing `r < −D_a + min_j w_j` puts `v` off every good set `G_j = {β_a ≥ …}`, so
`Σ_j w_j ‖1_{G_j} v‖² = 0`, whereas the concentration inequality demands
`Σ_j w_j ‖1_{G_j} h‖² ≥ D_a − η_a` for the *unrotated* `h`. After conjugation the
inequality is false. So the concentration estimate is **not** valid for every `U ∈ U_S`:
it is not an orientation-universal bound, and (B)'s conclusion (`≤ ess inf β_a`) does not
apply to it. In the theorem's own words (lines 10581–10582, 10588–10592): the orbit
"does not preserve the action on an infinite physical block", and the theorem gives "no
no-go for methods retaining the multiplier's physical support geometry". (B2) fails for
the same reason: the estimate's input is the infinite physical block `Ran F_a P_a`, not
finitely many protected columns.

### What would go wrong if a theorem accidentally covered it

- **If (A) covered it** (i.e. if `p*_a` were a physical density), then under RH Weil
  positivity would give `∫β_a p*_a ≥ 0`, contradicting the RH-conditional
  `∫β_a p*_a ≤ −a/(6π²)` of `prop:v137-conditional-mass`. So "(A) covers the
  concentration route" would be a disproof of RH by a soft information argument; the
  manuscript flags exactly this (lines 10352–10355: "Such an assertion would contradict
  the RH positivity used in the conditional part of the argument"). More generally,
  `eq:v133-joint-channel` shows that for a hierarchy fine enough the concentration
  criterion is *algebraically equivalent* to the complete complement floor on
  `P_a L²(I_a)`; (A) covering it would therefore prove `inf σ(W_{e^a}) → −∞`
  unconditionally, whereas under RH every window form is nonnegative
  (`prop:v121-cofinal-rh`, `COMPARISON.md` CCM `μ_λ` paragraph).
- **If (B) covered it**, its conclusion would put the physical compression's lower edge at
  `ess inf β_a`. That contradicts a **certified** fact: at `λ = 4` the complete form is
  nonnegative with simple ground `0 < μ_0 < 2.454·10^{-75}` (`prop:v126-full-window`,
  `prop:v140-ground4`), while `β_4` takes the value `≈ −3.419` at the deepest located well
  (line 9119; non-rigorous point value, but `inf β_a < 0` is unconditional there since
  `D_a = ‖(β_a)_-‖_∞ > 0`). So `inf σ(W_4) = μ_0 > 0 > ess inf β_4`: the Paley–Wiener
  position carries positivity strictly beyond the pointwise minimum, and any class that
  contained the physical estimate would have a false conclusion at a certified window.
  The same gap (`0.95, 2.76, 3.68` Rayleigh values against point values
  `−2.38, −3.42, −5.02` at `λ = 3, 4, 5`, lines 9114–9124, diagnostics only) is the entire
  reason the route is live.

Conclusion for (d): the concentration route is outside (A) by (A2) and outside (B) by
(B3)/(B2); its remaining obligation is unchanged — the cofinal signed inequality
`eq:v131-weighted-concentration` with one uniform finite constant, both parities, all
couplings controlled (`cor:v136-complement-floor`). Nothing here makes it more likely to
succeed; it only confirms the two theorems do not touch it.

---

## 4. (e) The positive counterexample `prop:v139-location-counterexample`

Statement (lines 10594–10609): for `D_a > 0` and **any** measurable `E_a` with
`|E_a| = π/(2a(D_a+1))`, put `b_a = 1 − (D_a+1) 1_{E_a}`. Then for every physical `f`,
`∫ b_a |F_a f|² ≥ ½‖f‖²`, independently of the location or shape of `E_a`, even though
`ess inf b_a = −D_a → −∞`. Proof: the elementary height bound
`|F_a f|² ≤ (a/π)‖f‖²`. Checked exactly in `check_exact_models.py`
(`location_blind_positive_models`: floor `1/2` at `D = 1, 100, 10^{12}`).

**What it shows.**

1. A **location-blind, rearrangement-invariant, mass-and-height** estimate can supply a
   *positive uniform* floor for a symbol family with divergent negative depth. In bathtub
   terms, `ell_a^cap(b_a) = (a/π)[|E_a|(−D_a) + (π/a − |E_a|)] = ½` exactly: the right
   invariant is the mass-cap value, not `ess inf`.
2. The class of the counterexample **contains the probe** (`p*_a` has mass 1 and height
   `≤ a/π`), and the budget is still bounded (`B_a = −½ < 0`, i.e. no negative floor at
   all). So (A)'s conclusion is **false** for `b_a`. Therefore (A) is not a statement
   about class structure alone; its arithmetic input — the RH-conditional negative probe
   pairing of `prop:v137-conditional-mass`, converted to an unconditional divergence
   through `prop:v136-bounded-floor` — is essential. The review §5 states this: "this
   model does not have the negative arithmetic probe pairing from v1.37 needed for that
   argument."
3. The two theorems' notions of "location-independent" are **genuinely different**. For
   `b_a`, the mass-cap estimate (an (A)-type density budget) succeeds, while (B)'s
   orientation-universal edge is `ess inf b_a = −D_a → −∞` and fails. The height bound
   `a/π` is a Paley–Wiener-position property that the orbit destroys. So
   (A)-membership does not imply (B)-membership — which is exactly the situation of row 10
   (primitive: in (A), not in (B)).

**What it rules out.**

- The unrestricted slogan "every estimate insensitive to the arithmetic location of
  negative mass fails" (research report §4: "the unrestricted wording rejected").
- The inference "`ess inf β_a → −∞` ⇒ every location-blind bound fails" — negative depth
  alone proves nothing; the divergence of the *total negative mass on a window of measure
  `π/a` beside a zero* (depth `~ a` over width `~ 1/a`, i.e. `ell_a^cap(β_a) → −∞`) is
  what (A) actually uses.
- Any attempt to kill the concentration route by a "depth" or "histogram" argument alone:
  the counterexample is a symbol for which a strictly weaker (mass-cap) estimate already
  gives a floor, so a fortiori the concentration estimate (which retains the full
  Paley–Wiener geometry) cannot be excluded by such arguments.

**What it does not do.** It is not the arithmetic symbol (line 10611: "This example is not
the arithmetic symbol"); it does not weaken (A) or (B) for `β_a`; it supplies no positive
mechanism for `β_a`.

---

## 5. Consistency with the manuscript's own scoping claims

- Line 10616–10617, "The proved scalar pointwise and primitive closures fall within the
  displayed classes": confirmed, with the sharpening that the primitive is in (A) only
  and the pointwise minimum in both.
- Lines 10617–10620, "The Schatten, signed block-norm, noncommuting band, Cotlar, and
  flat-top results have additional geometric or structural hypotheses; their recorded
  closures are not corollaries of a single insensitivity assertion": confirmed (rows 3,
  6, 7, 8, 9), with the specific hypothesis each violates recorded above.
- Status paragraph, lines 199–209, "The evidence report audits the ten historical
  closures and does not claim that all are subsumed": confirmed; the count is 1 of 10 for
  (A), 0 of 10 for (B).
- `adversarial_review.md` §6 ten-row table: consistent. Differences are only in
  precision: the review leaves prime-norm domination conditionally covered by (B) "for an
  implementation proved to be orientation-blind"; I record it as **neither**, because the
  recorded v115/v119 estimate visibly uses Fourier-basis matrix entries of the archimedean
  part (position data) and concerns the unsigned operator, so no recorded implementation
  is orientation-blind.
- `NEXT_STEPS.md` NS-15 says "NS-4b's table and concentration exclusion already exist in
  v139/adversarial_review.md sections 6–7". That table gives one-line verdicts without
  hypothesis checks or line references; this document supplies the hypothesis-by-
  hypothesis check requested by NS-4b and reaches the same verdicts.

## 6. Files

- `coverage.md` — this analysis.
- `coverage_insert.tex` — LaTeX draft of the table and a short paragraph, with the
  suggested insertion anchor marked. Test-compiled against a scratch copy of the v1.40
  manuscript; `manuscript/*.tex` is unchanged.
- `README.md` — scope statement.
