# Fixed-Space Prime Compatibility

Alexander Eastwood's complete working manuscript, **v1.64**.

**G2 and the Riemann Hypothesis remain open.** Nothing in this repository
claims otherwise.

## Navigating this repository

- **[RESEARCH_MAP.md](RESEARCH_MAP.md)** — the whole project as one diagram:
  every idea, which sub-ideas were tried, and which passed or failed.
- **[COMPARISON.md](COMPARISON.md)** — where the certified `lambda = 4`
  window sits relative to published work, with the parameter translation.
- **[REPO_LAYOUT.md](REPO_LAYOUT.md)** — directory layout, branch and tag
  conventions, and how to add a new version.
- **[evidence/MISSING.md](evidence/MISSING.md)** — artifacts the manuscript
  cites that this repository does not yet contain. Read this before relying
  on any computer-assisted claim.
- **[AGENTS.md](AGENTS.md)** — instructions for AI agents contributing here.

```sh
./manuscript/build.sh                     # build the PDF (source validation is not a build)
python3 tools/verify_manifest.py v126     # check a version's artifacts, or --all
python3 tools/make_map.py                 # regenerate RESEARCH_MAP.md
```

## Status at a glance

| | |
|---|---|
| Only positivity result | `W_4 >= 0`, both parity sectors — evidence restored and verified |
| Complete ground at lambda=4 | Simple and even; `0<mu0<2.454e-75`, `mu1>1e-73`; its entire Fourier transform has only real zeros ([certificate](evidence/v140/)) |
| Complete-ground first zero | First positive zero simple and within 8.752082e-33 of gamma_1, at 1024/1280 bits ([v1.43](evidence/v143/)); no discrepancy sign |
| CCM finite benchmark | Eight local lambda=3, N=120 root discrepancies certified at 768/1024 bits; broader reproduction remains diagnostic ([v1.41](evidence/v141/)) |
| Finite floors | `W_λ >= -8·I` at λ = 5, 6, 8, both parities, full infinite tail (`prop:v138-three-floors`) |
| Certified window | half-width `a = log 4 = 1.386`; 1.73× the published Zhu window, 4× the classical range |
| Current mechanisms | Complete kernel exclusion (API); CCM complete-ground selection; paired heat transport and arithmetic approximation inputs remain open |
| Scoped obstructions | See the map for the precise comparison classes; alternative routes are not collectively proved closed |
| Evidence gaps | Both remaining groups explicitly not archived; disclosure complete, recovery open — see the ledger |
| G2 | open |
| RH | open, and not claimed |

## v1.64: ordinary conditioning and an effective finite comparator (NS-81)

Exact coefficient recovery from a finite reciprocal-sample prefix gives an
unconditional ordinary Gram condition bound **O(N^4 log²(2N))**. This rules
out exponential growth of the spectral condition number in these physical
atom coordinates; it says nothing about the size of the approximation error
or a signed Weil spectral floor.

The full arithmetic comparator now has an explicitly sufficient finite
cutoff, **M = 2^16 (N+1)^6**, with a complete tail bound and projected
condition ratio at most 42. For an old-size-256 block, use total atom count
512: the sufficient cutoff exceeds **10^21 cells**. That enormous comparator
was not assembled. The result establishes effectiveness, not a fast solver
or a necessary lower bound on computational cost.

Small-prefix inverse certificates and scalar tail bounds pass at 256/384
bits. The missing cofinal signed arithmetic decay, G2 and RH remain open.

[Readable update](evidence/v164/research-update-2026-09-23-v1.html) ·
[Proof and finite checks](evidence/v164/).

## v1.63: complete arithmetic sampling and a uniform block guarantee (NS-78–80)

The complete squared residual norm is bounded above and below by fixed
multiples of an explicit weighted sum over **all reciprocal-integer samples**.
Exact inversion exposes the remaining signed divisor constraints. Independent
physical-cell integration, including the infinite tail, confirms the Gram
norm at N=16,64,256.

Preserving the exterior tail does not repair the tested divisor rule:
at N=256 its best three-direction span captures **59.97%** of full gain;
adding the endpoint atom reaches **71.18%**, versus curvature's **97.63%**.
Thirteen of fifteen raw unit steps increase error; two decrease it at N=128.

The full arithmetic sampling Gram supplies an unconditional, size-independent
comparison: an ideal preconditioned step captures at least **21/121** of
available block gain, and twenty capture **more than 97.79%**. This retains
the entire infinite arithmetic comparator; no fast inverse is supplied.
A uniform fraction of available gain is not a cofinal lower bound relative
to the full residual error. That arithmetic input, G2 and RH remain open.

[Readable update](evidence/v163/research-update-2026-09-23-v1.html) ·
[Proofs and complete finite replays](evidence/v163/).
No new Weil window, uniform Weil floor, or RH proof.

## v1.62: divisor feedback and the continuous relaxation (NS-75–77)

Cancelling the actual residual's next derivative jumps is exact locally,
but its held-old unit step increases the full error on all five checked
blocks. At N=256 its optimized three-direction span captures **56.02%** of
full gain, versus **97.63%** for curvature. This is a finite control, not
an asymptotic exclusion of all arithmetic feedback.

The continuous-dilation relaxation has an exact distance formula in terms
of the classical unknown inner factor. Its closure is strictly larger than
the integer closure; a certified explicit witness separates the two.
A complete positive zero-tail budget, combined with published finite-height
zero verification, gives continuous squared distance **below 2.08e-32**.
This is not an upper bound for integer error, a new zero verification, or a
proof of zero distance. The original cofinal arithmetic input remains open.

[Readable update](evidence/v162/research-update-2026-09-23-v1.html) ·
[Proofs and complete finite replays](evidence/v162/).
No new Weil window, uniform floor, G2 or RH proof.

## v1.61: local geometry and an arithmetic control (NS-72–74)

The repaired model has an explicit positive differential energy. Its
numerator is uniformly comparable to a discrete curvature energy, yielding
an O(N) coefficient rule once the actual residual correlations are known.
At N=256 the diagonal curvature rule captures **97.63% of the full block
gain**, an **8.13% reduction of squared error**, versus the optimum's 8.33%.
The best combination of three prescribed Mobius/log-taper templates captures
83.66%; these finite comparisons do not exclude other arithmetic formulas.

An explicit unitary altered family has identical complete Gram matrices
and arbitrarily close finite efficiency statistics, but an unconditional
positive approximation floor. This is a control on the inference from
finite geometry, not an off-line zeta zero or a floor for the original
family. The original cofinal arithmetic numerator/cost estimate remains open.

[Readable update](evidence/v161/research-update-2026-09-23-v1.html) ·
[Proofs and complete finite replays](evidence/v161/).
No new Weil window, uniform floor, G2 or RH proof.

## v1.60: keep arithmetic in the chosen direction (NS-67–71)

The repaired elementary kernel selects a direction capturing **97.06% of
full optimal block improvement at N=256**, versus **38.41%** for the
unmodified correlation direction. That is an **8.08% reduction in squared
residual error**, versus the full optimum's **8.33%**. These are certified
finite results at 256/384 bits, with a doubled-cutoff replay; they do not
supply the required cofinal lower contraction.

Exact cell energies retain the weaker canonical growth target. Centering
the two complete Abel terms proves that cancellation between those whole
vectors cannot change their power exponent; internal arithmetic remains
open. The positive renewal operator transfers a forcing bound without
improving its exponent, and its critical weighted total energy diverges.
The actual optimized endpoint remainder exceeds the leading model at
N=64 and N=128. An explicit cusp correction fixes the elementary Gram's
adjacent scaling, but uniform all-coefficient comparison is still false.
Using that repaired kernel only to choose coefficients avoids assuming
such a comparison: all gains are measured with the complete actual Gram.

[Readable research update](evidence/v160/research-update-2026-09-23-v1.html) ·
[Proofs, Maxima checks, finite certificates and validation](evidence/v160/).
No new Weil window, uniform floor, G2 or RH proof. The next input is an
arithmetic lower bound for the selected numerator together with a bound
for its true-energy cost along a cofinal sequence.

## v1.59: a fixed smoothing gives an elementary block bound (NS-60–66)

One extra Mellin integration keeps convergence equivalent to RH and gives
an unconditional complete difference-block trace bound `3*kappa/(8*N^2)`.
The missing input is a lower estimate for the actual optimized residual
correlations; their endpoint expansion now states its entire remainder.
Arb checks at 256/384 bits retain the infinite Gram tail and all projection
terms. On N=16 and N=32, the trace lower bound is below 1/50 of the true gain.

Explicit Euler-grid corrections have a scoped uniform-norm obstruction.
The canonical sharp Mobius interpolant still fails along the full integer
sequence after smoothing; optimized coefficients and selected subsequences
are not excluded. A positive coefficient cone already fails on a finite
interval; an explicit dual separator certifies a full-space distance
lower bound greater than 0.00228323. Signed approximation is not excluded. Increasing the smoothing order is also not an RH test: one fixed
atom then has relative squared error tending to zero while absolute squared
error grows. Keep the norm fixed while increasing N.

A fixed number of ordinary Cesaro averages also fails to give canonical
convergence. A weaker target remains: the fixed-order canonical norm
has growth exponent exactly `beta_star - 1/2`. Subpolynomial growth is
equivalent to RH, and even a bounded cofinal subsequence would suffice.
These growth bounds remain unproved; the exact reformulation supplies
no new zero-free region.

[Readable report](evidence/v159/research-update-2026-09-22-v2.html) ·
[Proofs, exact Maxima checks and finite certificates](evidence/v159/).
Published through PR #32. RH, G2 and the original Weil floor remain open.

## v1.58: an arithmetic limit on uniform NB block bounds (NS-59)

Adjacent dilation differences give an unconditional complete Gram bound
`||D_N|| = O_epsilon(N^(-5/3+epsilon))`. The proof uses an exact Mellin
identity and the classical Weyl estimate, with every cross term retained.
A near-`N^(-2)` power bound for the raw Gram is equivalent to Lindelof;
every fixed logarithmic factor at that scale is ruled out by known large
values of zeta. This does not rule out a better bound for the projected
Gram or the actual residual direction.

Arb checks at 256 and 384 bits show that the old raw-trace bound retains
less than 1/400 of the true gain at N=128 and N=256. Changing the basis
shrinks the correlations too, and its trace bound is worse at N=256.
The missing ingredient remains an asymptotic lower correlation estimate.

[Proof, report, finite certificates and validation](evidence/v158/).
No NB convergence, uniform Weil floor, G2 or RH proof is claimed.

## v1.57: the exact boundary test reaches its stop condition (NS-58)

The full exterior pairing against every translated arithmetic radical is
exactly equivalent to the original nullvector equation. Its derivation is
valid on the complete form domain, with both poles and all exterior prime
rows retained. It supplies no independent sign or uniqueness estimate.

Finite prime-weight changes add an explicit forcing term. That forcing is
nonzero for every nonzero test, but its map is compact and has no uniform
positive lower bound on the entire fixed-window unit sphere. This does not
exclude a bound restricted to a particular altered operator's finite kernel.

[Proof, report, exact algebra checks and validation](evidence/v157/).
NS-58 stops as specified; API, the uniform finite floor, G2 and RH remain open.

## v1.56: finite prime-weight controls (NS-57)

Every nonzero finite change to the prime-shift coefficients creates negative
compact smooth tests in both parity sectors, however small the change. The
altered complete family has a finite first-zero window, including endpoint
support saturation and its modified affine-potential equation. It does **not**
retain the original arithmetic radical identity. No negative direction for the
unchanged Weil form is claimed.

For a fixed perturbation pattern of size epsilon, the first-zero parameter
has an analytic upper bound `lambda_* = O(sqrt(log(1/epsilon)))`; constants
are pattern-dependent and no numerical threshold is certified. Fixed bounded
perturbations preserve the cofinal finite-floor objective. The exact scalar
compensation criterion and conditional spectral limit follow from v1.36.

[Proof, report, exact Maxima checks and validation](evidence/v156/).
These are analytic controls and target-stability results, not a new signed
arithmetic estimate. API, the original uniform floor, G2 and RH remain open.

## v1.55: local uniqueness shortcuts tested

The actual prime-shift operator admits nonzero functions with both f and A_a f
zero on an open patch. The construction works in each parity for a > log 2 and
after finitely many linear constraints, including source orthogonality. These
are **not full-window nullvectors** and supply no negative Weil direction.
The complete semigroup also fails ordinary pointwise positivity preservation;
that property is distinct from nonnegativity of the quadratic form.

A prime-shift-free exterior observation cell does give uniqueness, but a
hypothetical first-zero nullvector must reach both window endpoints. An exact
inward-dilation identity retains all signed prime overlaps and pole changes;
no new arithmetic sign estimate is proved. API remains open.

[Report and proof](evidence/v155/) · 285 pages, 0 undefined/duplicate references.
No new window, tail metric, uniform floor, G2 or RH claim.

## v1.54: three different first lemmas

The complete nullvector equation is now an affine screw-potential condition,
with no unproved square-integrable derivative assumption. A rank-one
countermodel shows why that generic regularity shortcut fails. Paired heat
transport cancels inverse-gap singularities while retaining external-zero
interactions. Nyman–Beurling approximation has an exact residualized block
update and unconditional gain lower bound. The arithmetic injectivity,
transport and asymptotic correlation estimates remain open.

[Version report and validation](evidence/v154/) ·
[kernel report](evidence/ns51_kernel/kernel-route-2026-09-22-v1.html) ·
[heat report](evidence/ns52_heat_pairs/heat-pairs-2026-09-22-v1.html) ·
[approximation report](evidence/ns53_nb_blocks/nb-blocks-2026-09-22-v1.html)

## Research map

Every idea, which sub-ideas were tried from it, and which passed or failed.
Green = proved · gold = current route · red = closed · purple = blocked · grey = open.
Nodes with a folder icon link to the `evidence/` directory holding their
certificates; the full version with a node-by-node list is
[RESEARCH_MAP.md](RESEARCH_MAP.md).

<!-- research-map:start -->
```mermaid
graph LR
  rh["RH"]
  g1["G1 (weak)<br/><small>thm:v14-radical</small><br/><small>&#128193; evidence/v124/g2_source_certificate</small>"]
  fixedspace["Fixed-space / Burnol Sonine route"]
  g2["G2: cofinal -o(1)<br/><small>prop:v121-cofinal-rh</small>"]
  windows["Fixed-window certificates"]
  w3["lambda=3<br/><small>prop:v116-window-positive</small><br/><small>&#128193; evidence/v124/g2_certificate</small>"]
  w4e["lambda=4 even<br/><small>prop:v125-even-complete</small><br/><small>&#128193; evidence/v126</small>"]
  w4o["lambda=4 odd<br/><small>prop:v126-odd-complement</small><br/><small>&#128193; evidence/v126</small>"]
  w4["W_4 >= 0 both sectors<br/><small>prop:v126-full-window</small><br/><small>&#128193; evidence/v126</small>"]
  w5["lambda=5: stipulated 10^-8 D tail comparison<br/><small>prop:v152-tail-comparison</small><br/><small>&#128193; evidence/ns44_metric_replay</small><br/><small><b>wall: stipulated 1e-8 D tail comparison fails: positive q/D < 7e-18 (lambda=5)</b></small>"]
  uniform["Uniform mechanism for G2"]
  primenorm["unsigned prime-norm domination<br/><small>prop:v119-prime-essential</small><br/><small>&#128193; evidence/v124/g2_growing_sign</small><br/><small><b>wall: cost: prime norm ~ lambda survives finite removal; exponential cutoff (estimate, not route)</b></small>"]
  normcontr["norm contraction<br/><small>prop:v120-norm-counterexample</small><br/><small>&#128193; evidence/v124/g2_weighted_signed</small><br/><small><b>wall: specific estimate: violated by a POSITIVE direction, q/D > 2.05 at lambda=4</b></small>"]
  schatten["Schatten / Hilbert-Schmidt<br/><small>prop:v132-schatten</small><br/><small>EVIDENCE MISSING</small><br/><small><b>wall: scoped: remainder outside finite Schatten classes; negative-only penalty stays a constant (does not obstruct v136)</b></small>"]
  sampling["basis / sampling dominance<br/><small>prop:v121-complement-cancellation</small><br/><small>&#128193; evidence/v124/g2_schur_cancellation</small><br/><small><b>wall: estimate counterexample: source-complement vector with tiny q despite O(1) cancellation</b></small>"]
  farmaj["scalar far majorant<br/><small>prop:v125-cutoff-cost</small><br/><small>&#128193; evidence/v126/g2_window_resolution</small><br/><small><b>wall: cost of one estimate: N > L exp(M_phi/(1-c)); not every method</b></small>"]
  blockmetric["lambda=5 N=25: tested dyadic norm comparison<br/><small>prop:v152-block-comparison</small><br/><small>&#128193; evidence/ns45_block_replay</small><br/><small><b>wall: fixed-partition comparison fails: Rayleigh 341/250, 2093/1500 > 1 (lambda=5, N=25)</b></small>"]
  flattop["flat-top smoothing<br/><small>prop:v132-flat-top</small><br/><small>EVIDENCE MISSING</small><br/><small><b>wall: construction class: form-exact positive smoothing = point mass; signed smoothing not covered</b></small>"]
  recipband["reciprocal-band commutation<br/><small>EVIDENCE MISSING</small><br/><small><b>wall: generic mechanism: persistent source-compressed commutator > 9e-6; not every band choice</b></small>"]
  cotlar["Cotlar cross terms / atomization<br/><small>EVIDENCE MISSING</small><br/><small><b>wall: shortcut: cross norm >= 73/(375 pi) cofinally; not all Cotlar arguments</b></small>"]
  scalarprim["scalar signed primitive<br/><small>cor:v137-scalar-no-go</small><br/><small>&#128193; evidence/v137</small><br/><small><b>wall: genuine closure of the scalar route: a Delta(beta_a) -> infinity, unconditional</b></small>"]
  concentration["signed weighted concentration<br/><small>prop:v131-concentration</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: QG + WLH packet</b></small>"]
  weaken["Target weakening"]
  floor["uniform finite floor suffices<br/><small>prop:v136-bounded-floor</small><br/><small>&#128193; evidence/v136</small>"]
  gapfree["no uniform positive gap exists<br/><small>prop:v135-growing-radical</small><br/><small>&#128193; evidence/v135</small>"]
  floortest["W_lambda >= -8 I at lambda=5,6,8<br/><small>prop:v138-three-floors</small><br/><small>&#128193; evidence/v138</small>"]
  shiftbarrier["bounded shift keeps the exp cutoff barrier<br/><small>prop:v138-shifted-floor</small><br/><small>&#128193; evidence/v138</small>"]
  metablind["Scoped information-loss obstructions<br/><small>thm:v139-probe-relaxation; thm:v139-protected-orbit</small><br/><small>&#128193; evidence/v139</small>"]
  altroutes["Alternative mechanisms: distinct missing inputs"]
  circle["circle / Toeplitz-Hankel lens<br/><small>&#128193; evidence/diag_true_symbol</small>"]
  debranges["de Branges / Hermite-Biehler<br/><small><b>wall: screw-kernel positivity = RH; no fixed-window bridge</b></small>"]
  f1["function field / Hodge / F_1<br/><small><b>wall: no intersection form supplied for this window (missing construction)</b></small>"]
  nb["Nyman-Beurling-Baez-Duarte<br/><small>prop:ns53-nb-block-gain; eq:ns53-nb-rbc</small><br/><small>&#128193; evidence/ns53_nb_blocks</small><br/><small><b>wall: RBC: corrected arithmetic residual block correlations (open sufficient input)</b></small>"]
  li["Direct rational Li / entire window-test identification<br/><small>&#128193; evidence/diag_routes/li</small><br/><small><b>wall: direct rational-Li / entire-window classes intersect only at zero</b></small>"]
  dbn["de Bruijn–Newman: paired transport<br/><small>prop:ns52-cluster; prop:ns52-unmatched</small><br/><small>&#128193; evidence/ns52_heat_pairs</small><br/><small><b>wall: complete signed transport with uniform support control (open)</b></small>"]
  ccmmu["W_4 >= 0  <=>  CCM mu_lambda >= 0 for all lambda <= 4"]
  simpleeven4["complete W_4: simple even ground; real-zero transform<br/><small>prop:v140-ground4; cor:v140-real-zeros</small><br/><small>&#128193; evidence/v140</small>"]
  stepb["CCM step (b): finite-compression zeros track zeta zeros (numerical)<br/><small>&#128193; evidence/diag_ns2_semantic_lock</small>"]
  semanticlock["CCM finite-compression semantic lock, lambda=3 N=120<br/><small>lem:v141-centering; prop:v141-ccm-lock</small><br/><small>&#128193; evidence/v141</small>"]
  groundzero4["complete ground zero within 0.1 of gamma_1<br/><small>lem:v142-energy-projection; prop:v142-ground-zero</small><br/><small>&#128193; evidence/v142</small>"]
  groundzero4resolution["first complete zero within 9e-33; archived resolution quantified<br/><small>prop:v143-first-zero-bound; prop:v143-resolution; prop:v143-fixed-window-meaning</small><br/><small>&#128193; evidence/v143</small>"]
  pencilconcentration["pencil loss budget; cofinal obligation retained<br/><small>prop:v144-pencil-concentration</small><br/><small>&#128193; evidence/v144</small>"]
  betaexplicit["exact lattice symbol; varying envelopes<br/><small>prop:v146-beta-explicit</small><br/><small>&#128193; evidence/v146</small>"]
  minorantlevels["bounded-complexity minorants: arithmetic gap remains<br/><small>prop:v146-packet-loss; prop:v146-level-complexity</small><br/><small>&#128193; evidence/v146</small><br/><small><b>wall: ZLD + packet</b></small>"]
  zeroleveldistribution["zero level distribution and packet coverage: open inputs<br/><small>prop:v147-level-separation; ass:v147-zld; prop:v147-depth-measure; prop:v147-broad-packet</small><br/><small>&#128193; evidence/v147</small><br/><small><b>wall: ZLD + packet</b></small>"]
  weightedexactcost["weighted exact cost: peak bound fails at critical levels<br/><small>prop:v149-critical-density; prop:v149-weighted-cost; prop:v149-qc1-insufficient; ass:v149-qg</small><br/><small>&#128193; evidence/v149</small><br/><small><b>wall: QG + WLH packet</b></small>"]
  capacityweight["positive arithmetic weight: critical capacity input<br/><small>lem:v150-weight; prop:v150-critical-energy; ass:v150-cae</small><br/><small>&#128193; evidence/v150</small><br/><small><b>wall: CAE</b></small>"]
  capacityslack["fixed energy loss for the Gaussian arithmetic weight<br/><small>prop:v150-capacity-slack</small><br/><small>&#128193; evidence/v150</small><br/><small><b>wall: fixed-slack shortcut: eta >= delta kappa exp(gamma lambda^2) - O(lambda log lambda)</b></small>"]
  inputcomparison["ZLD to QG; CAE is the signed-floor target<br/><small>prop:v151-input-comparison</small><br/><small>&#128193; evidence/v151</small>"]
  capacitychannels["Fixed/sub-endpoint channel deletion with unchanged signed terms<br/><small>prop:ns43-fixed-channel; prop:ns43-moving-channel</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: channel deletion: unbounded comparison error for the Gaussian weight</b></small>"]
  bumpstrength["Restricted bump discrepancy can carry the full zero obstruction<br/><small>prop:ns43-bump-strength</small><br/><small>&#128193; evidence/v152</small>"]
  adaptiveidentity["Unrestricted exact adaptive hierarchy = complement floor<br/><small>ns43-conc-prop-adaptive</small><br/><small>&#128193; evidence/v152</small>"]
  scalarsetshortcut["Scalar set bounds alone determine signed floor: general inference<br/><small>ns43-conc-prop-scalar</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: general inference false: countermodels with equal scalar set extrema and opposite signed bottoms</b></small>"]
  relativeselection["Complete relative selection and entire-transform control<br/><small>prop:ns43-ccm-rayleigh-selection; prop:ns43-ccm-residual-selection</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: cofinal separator</b></small>"]
  absoluteselection["Absolute residual/resolvent data alone select ground: abstract inference<br/><small>prop:ns43-ccm-nonselection</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: abstract inference false: countermodel family with alternating profiles</b></small>"]
  coarseprofile["Single profile from the specified coarse rescaled liminf<br/><small>prop:ns43-ccm-coarse-profile</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: under the explicit coarse scale the limit form is zero; finer scales open</b></small>"]
  fineradicalrank["Uniform or polynomial positive gap after o(lambda²/log lambda) removed directions<br/><small>lem:ns46-finite-arc; ns46-a2-cor-large-block; ns46-a2-cor-rank</small><br/><small>&#128193; evidence/v153</small><br/><small><b>wall: positive-gap strategy must remove rank >= lambda^2/(20000 log lambda)</b></small>"]
  kernelapi["Exact kernel exclusion: affine-potential injectivity<br/><small>prop:ns51-affine-potential; eq:ns51-api</small><br/><small>&#128193; evidence/ns51_kernel</small><br/><small><b>wall: API: actual arithmetic affine-potential injectivity (open)</b></small>"]
  generic_h1["Generic H¹ bootstrap from a zero eigenvalue<br/><small>prop:ns51-no-generic-bootstrap</small><br/><small>&#128193; evidence/ns51_kernel</small>"]
  localucp["Local open-set UCP for the full prime-shift operator<br/><small>prop:ns55-local-ucp-counterexample; prop:ns55-parity-ucp-counterexample</small><br/><small>&#128193; evidence/v155</small><br/><small><b>wall: local f=A_a f=0 does not force f=0; whole-window API is not refuted</b></small>"]
  fullpositivecone["Ordinary-cone positivity for the full Weil semigroup<br/><small>prop:ns55-nonpositive-semigroup</small><br/><small>&#128193; evidence/v155</small><br/><small><b>wall: order-preservation shortcut fails; quadratic-form positivity is a different property</b></small>"]
  finiteweightcontrols["Finite prime-weight changes: negative tests and first-zero controls<br/><small>cor:ns57-finite-weight-negative; thm:ns57-first-zero-controls; cor:ns57-fixed-direction-sensitivity</small><br/><small>&#128193; evidence/v156</small>"]
  boundedfloorstability["Bounded perturbations preserve the finite-floor objective<br/><small>lem:ns57-bounded-detection; thm:ns57-bounded-floor-stability</small><br/><small>&#128193; evidence/v156</small>"]
  radicalboundarytest["Translated-radical boundary test: exact kernel equivalence and forced controls<br/><small>prop:ns58-boundary-identity; prop:ns58-equivalence; prop:ns58-forced-pairing</small><br/><small>&#128193; evidence/v157</small>"]
  nbdifference["NB adjacent-difference norm budget<br/><small>prop:v158-adjacent-budget; prop:v158-mellin-budget</small><br/><small>&#128193; evidence/v158</small>"]
  nbrawlog["NB uniform logarithmic raw norm<br/><small>prop:v158-lindelof-budget</small><br/><small>&#128193; evidence/v158</small><br/><small><b>wall: known zeta large values contradict every fixed logarithmic N^(-2) raw norm bound</b></small>"]
  nbeulergrid["Uniform logarithmic norm after explicit Euler-grid correction<br/><small>prop:ns60-growing-euler-obstruction</small><br/><small>&#128193; evidence/v159</small><br/><small><b>wall: zeta large values exceed the allowed finite Euler-product loss</b></small>"]
  nbsmoothedbudget["Fixed smoothed NB: positive averages and N^(-2) trace<br/><small>prop:ns61-rh-equivalence; prop:ns61-average-budget</small><br/><small>&#128193; evidence/v159</small>"]
  nbsmoothedcorrelation["Actual optimized smoothed residual correlations<br/><small>eq:ns61-open-correlation; eq:ns61-endpoint-correlation; prop:ns69-remainder; prop:ns71-selected-input</small><br/><small>&#128193; evidence/v160</small><br/><small><b>wall: non-summable lower contraction for the actual optimized residual (open sufficient input)</b></small>"]
  nbsharpintegrated["Strong convergence of the smoothed canonical sharp Mobius sequence<br/><small>prop:ns62-smoothed-obstruction; prop:ns62-positive-cone; prop:ns64-cone-distance; prop:ns65-cesaro-obstruction</small><br/><small>&#128193; evidence/v159</small><br/><small><b>wall: a surviving weighted-Mertens witness for this coefficient rule</b></small>"]
  nbchangingnorm["Relative convergence with increasing Mellin smoothing<br/><small>prop:ns63-one-atom</small><br/><small>&#128193; evidence/v159</small><br/><small><b>wall: one-atom unconditional control refutes this convergence inference</b></small>"]
  nbcanonicalgrowth["Canonical smoothed norm: subpolynomial growth<br/><small>prop:ns66-growth-bounds; cor:ns66-growth-exponent; prop:ns67-polynomial-cutoff; prop:ns67-abel-conditioning</small><br/><small>&#128193; evidence/v160</small><br/><small><b>wall: direct subpolynomial canonical norm bound, or a bounded cofinal subsequence (open)</b></small>"]
  nbcanonicalcells["Complete canonical divisor cells and full tail<br/><small>prop:ns67-cells; lem:ns67-remainder; prop:ns67-polynomial-cutoff</small><br/><small>&#128193; evidence/v160/ns67</small>"]
  nbabelwholegain["Power gain solely between the two complete Abel vectors<br/><small>prop:ns67-abel-conditioning</small><br/><small>&#128193; evidence/v160/ns67</small><br/><small><b>wall: uniform conditioning excludes an exponent improvement in this whole-vector split</b></small>"]
  nbrenewalforcing["Positive renewal with signed arithmetic forcing<br/><small>prop:ns68-weighted-inversion; prop:ns68-scalar-criterion</small><br/><small>&#128193; evidence/v160/ns68</small><br/><small><b>wall: independent square-root-plus-epsilon bound for the signed forcing</b></small>"]
  nbcriticalrenewalenergy["Finite total critical renewal energy<br/><small>cor:ns68-critical-energy</small><br/><small>&#128193; evidence/v160/ns68</small><br/><small><b>wall: critical-line Mellin pole contradicts finite weighted L2 energy</b></small>"]
  nbrepairedbounds["Uniform comparison with the repaired elementary Gram<br/><small>prop:ns70-cusp; prop:ns70-repaired-background</small><br/><small>&#128193; evidence/v160/ns70</small><br/><small><b>wall: pointwise Mellin-density comparison forced by all-coefficient localization</b></small>"]
  nbselectedpreconditioner["Repaired-kernel selection measured with true energy<br/><small>prop:ns71-selected-input</small><br/><small>&#128193; evidence/v160/ns71</small><br/><small><b>wall: cofinal lower numerator and upper selected cost with nonsummable relative gain</b></small>"]
  nblocalgeometry["Complete local energy and discrete curvature<br/><small>prop:ns72-local-energy; prop:ns72-interpolation; prop:ns72-curvature</small><br/><small>&#128193; evidence/v161/ns72</small>"]
  nbcurvaturearithmetic["Cofinal arithmetic curvature and selected cost<br/><small>eq:ns72-local-directions</small><br/><small>&#128193; evidence/v161/ns72</small><br/><small><b>wall: actual curvature lower bound and selected true cost giving nonsummable relative contraction</b></small>"]
  nbsamegramcontrol["Infer convergence from shared Gram geometry and finite efficiency<br/><small>prop:ns74-same-gram; cor:ns74-finite-indistinguishability</small><br/><small>&#128193; evidence/v161/ns74</small><br/><small><b>wall: explicit inserted inner-factor control; scope is this finite-statistics inference</b></small>"]
  nbdivisorfeedback["Exact divisor feedback and finite unit-step failure<br/><small>prop:ns75-divisor-cells</small><br/><small>&#128193; evidence/v162/ns75</small>"]
  nbcontinuousdefect["Exact continuous inner-factor defect and strict closure separation<br/><small>prop:ns76-continuous-distance; prop:ns76-strict-closure</small><br/><small>&#128193; evidence/v162/ns76</small>"]
  nbcontinuoustail["Complete continuous zero-tail budget<br/><small>prop:ns77-tail-budget</small><br/><small>&#128193; evidence/v162/ns77</small>"]
  nbarithmeticsampling["Complete reciprocal-knot norm and exact divisor inversion<br/><small>prop:ns78-sampling; eq:ns78-sample-inverse</small><br/><small>&#128193; evidence/v163/ns78</small>"]
  nbbalancedfeedback["Tail-balanced divisor feedback control<br/><small>prop:ns79-balance</small><br/><small>&#128193; evidence/v163/ns79</small>"]
  nbarithmeticpreconditioner["Uniform efficiency using the full arithmetic sampling Gram<br/><small>prop:ns80-uniform-efficiency</small><br/><small>&#128193; evidence/v163/ns80</small>"]
  nbfiniteconditioning["Polynomial ordinary Gram conditioning and an effective finite comparator<br/><small>prop:ns81-conditioning; prop:ns81-finite-comparator</small><br/><small>&#128193; evidence/v164/ns81</small>"]

  rh --> g1
  rh --> fixedspace
  rh --> g2
  g2 --> windows
  windows --> w3
  windows --> w4e
  windows --> w4o
  windows --> w4
  windows --> w5
  g2 --> uniform
  uniform --> primenorm
  uniform --> normcontr
  uniform --> schatten
  uniform --> sampling
  uniform --> farmaj
  uniform --> blockmetric
  uniform --> flattop
  uniform --> recipband
  uniform --> cotlar
  uniform --> scalarprim
  uniform --> concentration
  g2 --> weaken
  weaken --> floor
  weaken --> gapfree
  floor --> floortest
  floor --> shiftbarrier
  uniform --> metablind
  rh --> altroutes
  altroutes --> circle
  altroutes --> debranges
  altroutes --> f1
  altroutes --> nb
  altroutes --> li
  altroutes --> dbn
  w4 --> ccmmu
  w4 --> simpleeven4
  simpleeven4 --> stepb
  windows --> semanticlock
  simpleeven4 --> groundzero4
  groundzero4 --> groundzero4resolution
  concentration --> pencilconcentration
  concentration --> betaexplicit
  concentration --> minorantlevels
  minorantlevels --> zeroleveldistribution
  zeroleveldistribution --> weightedexactcost
  floor --> capacityweight
  capacityweight --> capacityslack
  capacityweight --> inputcomparison
  capacityweight --> capacitychannels
  capacityweight --> bumpstrength
  concentration --> adaptiveidentity
  concentration --> scalarsetshortcut
  stepb --> relativeselection
  stepb --> absoluteselection
  stepb --> coarseprofile
  gapfree --> fineradicalrank
  altroutes --> kernelapi
  kernelapi --> generic_h1
  kernelapi --> localucp
  kernelapi --> fullpositivecone
  kernelapi --> finiteweightcontrols
  floor --> boundedfloorstability
  kernelapi --> radicalboundarytest
  nb --> nbdifference
  nb --> nbrawlog
  nb --> nbeulergrid
  nb --> nbsmoothedbudget
  nbsmoothedbudget --> nbsmoothedcorrelation
  nbsmoothedbudget --> nbsharpintegrated
  nbsmoothedbudget --> nbchangingnorm
  nbsmoothedbudget --> nbcanonicalgrowth
  nbcanonicalgrowth --> nbcanonicalcells
  nbcanonicalgrowth --> nbabelwholegain
  nbcanonicalgrowth --> nbrenewalforcing
  nbrenewalforcing --> nbcriticalrenewalenergy
  nbsmoothedcorrelation --> nbrepairedbounds
  nbsmoothedcorrelation --> nbselectedpreconditioner
  nbselectedpreconditioner --> nblocalgeometry
  nblocalgeometry --> nbcurvaturearithmetic
  nblocalgeometry --> nbsamegramcontrol
  nbcurvaturearithmetic --> nbdivisorfeedback
  nbsamegramcontrol --> nbcontinuousdefect
  nbcontinuousdefect --> nbcontinuoustail
  nbdivisorfeedback --> nbarithmeticsampling
  nbarithmeticsampling --> nbbalancedfeedback
  nbarithmeticsampling --> nbarithmeticpreconditioner
  nbarithmeticpreconditioner --> nbfiniteconditioning
  concentration -. "QG + WLH packet" .-> floor
  debranges -. "screw-kernel positivity = RH; no fixed-window bridge" .-> rh
  nb -. "RBC: corrected arithmetic residual block correlations (open sufficient input)" .-> rh
  dbn -. "complete signed transport with uniform support control (open)" .-> rh
  minorantlevels -. "ZLD + packet" .-> floor
  zeroleveldistribution -. "ZLD + packet" .-> floor
  weightedexactcost -. "QG + WLH packet" .-> floor
  capacityweight -. "CAE" .-> floor
  relativeselection -. "cofinal separator" .-> g2
  kernelapi -. "API: actual arithmetic affine-potential injectivity (open)" .-> rh
  nbsmoothedcorrelation -. "non-summable lower contraction for the actual optimized residual (open sufficient input)" .-> rh
  nbcanonicalgrowth -. "direct subpolynomial canonical norm bound, or a bounded cofinal subsequence (open)" .-> rh
  nbrenewalforcing -. "independent square-root-plus-epsilon bound for the signed forcing" .-> rh
  nbselectedpreconditioner -. "cofinal lower numerator and upper selected cost with nonsummable relative gain" .-> rh
  nbcurvaturearithmetic -. "actual curvature lower bound and selected true cost giving nonsummable relative contraction" .-> rh

  click g1 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_source_certificate/" "evidence: evidence/v124/g2_source_certificate" _blank
  click w3 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_certificate/" "evidence: evidence/v124/g2_certificate" _blank
  click w4e "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v126/" "evidence: evidence/v126" _blank
  click w4o "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v126/" "evidence: evidence/v126" _blank
  click w4 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v126/" "evidence: evidence/v126" _blank
  click w5 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns44_metric_replay/" "evidence: evidence/ns44_metric_replay" _blank
  click primenorm "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_growing_sign/" "evidence: evidence/v124/g2_growing_sign" _blank
  click normcontr "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_weighted_signed/" "evidence: evidence/v124/g2_weighted_signed" _blank
  click sampling "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v124/g2_schur_cancellation/" "evidence: evidence/v124/g2_schur_cancellation" _blank
  click farmaj "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v126/g2_window_resolution/" "evidence: evidence/v126/g2_window_resolution" _blank
  click blockmetric "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns45_block_replay/" "evidence: evidence/ns45_block_replay" _blank
  click scalarprim "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v137/" "evidence: evidence/v137" _blank
  click concentration "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click floor "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v136/" "evidence: evidence/v136" _blank
  click gapfree "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v135/" "evidence: evidence/v135" _blank
  click floortest "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v138/" "evidence: evidence/v138" _blank
  click shiftbarrier "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v138/" "evidence: evidence/v138" _blank
  click metablind "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v139/" "evidence: evidence/v139" _blank
  click circle "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_true_symbol/" "evidence: evidence/diag_true_symbol" _blank
  click nb "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns53_nb_blocks/" "evidence: evidence/ns53_nb_blocks" _blank
  click li "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_routes/li/" "evidence: evidence/diag_routes/li" _blank
  click dbn "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns52_heat_pairs/" "evidence: evidence/ns52_heat_pairs" _blank
  click simpleeven4 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v140/" "evidence: evidence/v140" _blank
  click stepb "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_ns2_semantic_lock/" "evidence: evidence/diag_ns2_semantic_lock" _blank
  click semanticlock "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v141/" "evidence: evidence/v141" _blank
  click groundzero4 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v142/" "evidence: evidence/v142" _blank
  click groundzero4resolution "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v143/" "evidence: evidence/v143" _blank
  click pencilconcentration "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v144/" "evidence: evidence/v144" _blank
  click betaexplicit "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v146/" "evidence: evidence/v146" _blank
  click minorantlevels "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v146/" "evidence: evidence/v146" _blank
  click zeroleveldistribution "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v147/" "evidence: evidence/v147" _blank
  click weightedexactcost "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v149/" "evidence: evidence/v149" _blank
  click capacityweight "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v150/" "evidence: evidence/v150" _blank
  click capacityslack "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v150/" "evidence: evidence/v150" _blank
  click inputcomparison "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v151/" "evidence: evidence/v151" _blank
  click capacitychannels "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click bumpstrength "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click adaptiveidentity "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click scalarsetshortcut "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click relativeselection "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click absoluteselection "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click coarseprofile "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v152/" "evidence: evidence/v152" _blank
  click fineradicalrank "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v153/" "evidence: evidence/v153" _blank
  click kernelapi "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns51_kernel/" "evidence: evidence/ns51_kernel" _blank
  click generic_h1 "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns51_kernel/" "evidence: evidence/ns51_kernel" _blank
  click localucp "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v155/" "evidence: evidence/v155" _blank
  click fullpositivecone "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v155/" "evidence: evidence/v155" _blank
  click finiteweightcontrols "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v156/" "evidence: evidence/v156" _blank
  click boundedfloorstability "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v156/" "evidence: evidence/v156" _blank
  click radicalboundarytest "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v157/" "evidence: evidence/v157" _blank
  click nbdifference "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v158/" "evidence: evidence/v158" _blank
  click nbrawlog "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v158/" "evidence: evidence/v158" _blank
  click nbeulergrid "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v159/" "evidence: evidence/v159" _blank
  click nbsmoothedbudget "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v159/" "evidence: evidence/v159" _blank
  click nbsmoothedcorrelation "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v160/" "evidence: evidence/v160" _blank
  click nbsharpintegrated "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v159/" "evidence: evidence/v159" _blank
  click nbchangingnorm "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v159/" "evidence: evidence/v159" _blank
  click nbcanonicalgrowth "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v160/" "evidence: evidence/v160" _blank
  click nbcanonicalcells "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v160/ns67/" "evidence: evidence/v160/ns67" _blank
  click nbabelwholegain "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v160/ns67/" "evidence: evidence/v160/ns67" _blank
  click nbrenewalforcing "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v160/ns68/" "evidence: evidence/v160/ns68" _blank
  click nbcriticalrenewalenergy "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v160/ns68/" "evidence: evidence/v160/ns68" _blank
  click nbrepairedbounds "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v160/ns70/" "evidence: evidence/v160/ns70" _blank
  click nbselectedpreconditioner "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v160/ns71/" "evidence: evidence/v160/ns71" _blank
  click nblocalgeometry "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v161/ns72/" "evidence: evidence/v161/ns72" _blank
  click nbcurvaturearithmetic "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v161/ns72/" "evidence: evidence/v161/ns72" _blank
  click nbsamegramcontrol "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v161/ns74/" "evidence: evidence/v161/ns74" _blank
  click nbdivisorfeedback "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v162/ns75/" "evidence: evidence/v162/ns75" _blank
  click nbcontinuousdefect "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v162/ns76/" "evidence: evidence/v162/ns76" _blank
  click nbcontinuoustail "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v162/ns77/" "evidence: evidence/v162/ns77" _blank
  click nbarithmeticsampling "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v163/ns78/" "evidence: evidence/v163/ns78" _blank
  click nbbalancedfeedback "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v163/ns79/" "evidence: evidence/v163/ns79" _blank
  click nbarithmeticpreconditioner "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v163/ns80/" "evidence: evidence/v163/ns80" _blank
  click nbfiniteconditioning "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v164/ns81/" "evidence: evidence/v164/ns81" _blank

  classDef proved fill:#a5d6a7,stroke:#1b5e20,stroke-width:1px,color:#000;
  class g1,windows,w3,w4e,w4o,w4,weaken,floor,gapfree,floortest,shiftbarrier,metablind,ccmmu,simpleeven4,semanticlock,groundzero4,groundzero4resolution,pencilconcentration,betaexplicit,inputcomparison,bumpstrength,adaptiveidentity,finiteweightcontrols,boundedfloorstability,radicalboundarytest,nbdifference,nbsmoothedbudget,nbcanonicalcells,nblocalgeometry,nbdivisorfeedback,nbcontinuousdefect,nbcontinuoustail,nbarithmeticsampling,nbbalancedfeedback,nbarithmeticpreconditioner,nbfiniteconditioning proved;
  classDef live fill:#ffd54f,stroke:#f57f17,stroke-width:3px,color:#000;
  class stepb,kernelapi live;
  classDef closed fill:#ef9a9a,stroke:#b71c1c,stroke-width:1px,color:#000;
  class w5,primenorm,normcontr,schatten,sampling,farmaj,blockmetric,flattop,recipband,cotlar,scalarprim,li,capacityslack,capacitychannels,scalarsetshortcut,absoluteselection,coarseprofile,fineradicalrank,generic_h1,localucp,fullpositivecone,nbrawlog,nbeulergrid,nbsharpintegrated,nbchangingnorm,nbabelwholegain,nbcriticalrenewalenergy,nbrepairedbounds,nbsamegramcontrol closed;
  classDef blocked fill:#ce93d8,stroke:#4a148c,stroke-width:1px,color:#000;
  class concentration,minorantlevels,zeroleveldistribution,weightedexactcost,capacityweight,relativeselection,nbsmoothedcorrelation,nbcanonicalgrowth,nbrenewalforcing,nbselectedpreconditioner,nbcurvaturearithmetic blocked;
  classDef open fill:#cfd8dc,stroke:#37474f,stroke-width:1px,color:#000;
  class rh,fixedspace,g2,uniform,altroutes,circle,debranges,f1,nb,dbn open;
  subgraph Legend
    direction LR
    lg_live["current route (gold)"]:::live
    lg_closed["closed route"]:::closed
    lg_proved["proved"]:::proved
    lg_open["open"]:::open
    lg_blocked["blocked"]:::blocked
  end
```
<!-- research-map:end -->

## Current manuscript

- [Complete LaTeX](manuscript/fixed_space_prime_action_v1.tex)
- [Research log and candidate register](log/RH_G1_G2_research_log.md)
- [Revision notes](log/v1_revision_notes.md)
- [Checksums and provenance for the local draft](manifest/v1.59_manifest.json)

One live manuscript; delivery is **LaTeX only** at the author's request.
Prior versions are reachable by tag (`v1.24`, `v1.34` … `v1.38`).

## New in v1.53

[NS-46, jointly with Astra-2](evidence/v153/), proves a larger complete near-zero
block: dimension asymptotic to **lambda²/(20000 log lambda)** and full operator
residual at most **C exp(-lambda²/2000)**. The construction changes from widely
spaced translates to increasingly close translates inside a fixed interval.
A finite-arc interpolation proof explicitly pays for the deteriorating Gram.

The block has exact even/odd dimensions. Removing o(lambda²/log lambda)
directions cannot leave a positive uniform or polynomial gap. This is a stronger
rank obstruction, **not a complementary lower floor**. It determines no energy
sign and gives no certified finite starting window. The gap-free uniform-floor
route remains open. No new numerical window, tail metric, G2 or RH claim.

[Assessment, proof and review scope](evidence/v153/ns46-fine-block-2026-09-22-v1.html).
The joint result is reviewed in [PR #24](https://github.com/AlexanderEastwood/riemann/pull/24)
and builds on the merged v1.52. Archived reports retain their prepublication checkpoint status.

## New in v1.52 (PR #21)

[NS-43/44/45](evidence/v152/) add two fresh, narrowly scoped comparison
certificates and complete analytic proofs for route selection. At the existing
lambda=5 window, both parity witnesses have positive Weil energy but violate
`10^-8 D`. The existing N=25 dyadic norm comparison has rational Rayleigh
bounds **1.364** and **2093/1500**, both above one. These replace missing proof
inputs for those comparisons; they do not recover historical artifacts or
establish a negative Weil direction.

The capacity proof extends the fixed-loss obstruction to all fixed prime-power
channels and omitted channels uniformly below the endpoint. Exact adaptive
concentration is an equivalent floor target; scalar set bounds can miss signed
operator information. CCM needs a complete relative selection estimate and
entire-transform control. Abstract residual/resolvent and coarse-profile
shortcuts close only under their stated hypotheses. CCM step (b) stays the sole
gold node; the circle lane remains open. No G2 or RH result.

[Route assessment and scope](evidence/v152/ns43-route-assessment-2026-09-22-v1.html).
The v1.52 change is reviewed in PR #21 and builds on the merged v1.51 work in PR #20. Archived reports retain their prepublication checkpoint status.

## New in v1.51

[NS-39](evidence/v151/) gives one proposition comparing the three open inputs:
ZLD implies QG's growth clause on the same prescribed family, with lower cost
`κ θ² D / (2K)`; packet feasibility remains separate. The complete corrected
zero field gives the positive-weight potential exactly. CAE is precisely the
uniform complement-floor target in those coordinates. No new signed estimate,
arithmetic independence, G2 or RH result follows.

[NS-38](evidence/ns38_archival_disclosure/ns38-archival-disclosure-2026-09-22-v3.html)
uses explicit disclosure for both missing evidence groups; no originals were
recovered. The five v1.35 scientific files are present and match legacy hashes.
The two new measurement records are separate diagnostics:
[NS-41 odd feasible states](evidence/diag_ns41_odd_feasibility/) and
[NS-42 transformed energies](evidence/diag_ns42_energy_budget/).
Neither is cited as a bound. NS-40's QG literature assessment is coordinated
separately in [PR #19](https://github.com/AlexanderEastwood/riemann/pull/19).

## New in v1.50

NS-34 chooses the explicit positive Gaussian arithmetic radical as the
weight in the physical prime-shift/Picone identity. Its exact pole mass is
1/sqrt(3); the complete energy identity retains the odd pole and exterior
edges. For this weight, a fixed fractional loss of transformed energy,
or omission of the prime-2 channel alone, forces a capacity error growing
like exp(gamma*lambda^2), up to O(lambda log lambda). The source constraint
is imposed exactly in a two-dimensional even test space; odd parity is
covered separately.

The closed result concerns those weakened lower comparisons. The full
coefficient-one comparison remains the named open input CAE, equivalent
to the existing uniform complement-floor target in these coordinates.
A different weight is not excluded. No numerical experiment, new window
or tail metric; G2 and RH remain open. See [v1.50](evidence/v150/).

## New in v1.49

PR #14's v1.48 candidate is held for major review findings. The valid
weighted bound eta >= [c' QC_K - Q]+ is restated self-contained. Negative
critical values make the exact continuous level-density peak infinite;
the finite histogram peak is a different quantity. QC_1 growth alone is
also insufficient: a full-support countermodel has QC_1~D/2 but QC_2->0.
The corrected cofinal input is Exact Level Quantization Growth (QG), plus
admissible bounded-energy weighted packets; a QC_1/K law needs a separate
shape hypothesis. Both inputs remain open. No new computation, window or
tail metric. G2 and RH remain open. See [v1.49](evidence/v149/) and the
[PR #14 review](audits/2026-09-21-v1.48-pr14-v3.html).

## New in v1.47

NS-29 separates the measure of every interval of symbol levels from the
Fourier coverage and original energy of a physical packet. Cumulative
sublevel bounds do not imply the required density. The exact zero expansion
provides a precise named open input, ZLD, with endpoint and trivial terms
retained. The zero theorems assessed do not supply that value distribution.
Depth growth yields only local widths with window-dependent constants;
broad Fourier pulses have energy log X + O(1). Both uniform level measure
and bounded-energy packet coverage remain open. The route stays blocked,
not closed; G2 and RH remain open. See [v1.47](evidence/v147/).

## New in v1.46

The exact lattice-symbol identity retains the strict prime-power endpoint,
trivial zeros and Perron remainder. Its envelopes vary; the comb is an
explicit-formula representation, not a new positivity mechanism. The
numerical illustration checks 40 low samples and 14 deep-trough/centroid
locations with explicit summation and zero-count conventions.

The minorant analysis proves local packet bounds and a conditional linear
level-count inequality. Positive spill and original packet energy must be
retained. Uniform arithmetic level distribution and bounded packet energy
remain unproved, so the route stays **blocked, not closed**. The concentration
criterion remains valid; G2 and RH remain open. See [v1.46](evidence/v146/).

## New in v1.45

Audit MINOR M1/M2 wording corrections: inherited 320/768/896-bit inputs are
separated from the new 1024/1280-bit gates, and the direct-bound limitation
is paired with the separate frozen-trial transfer floor, about 6.65e-38.
No enclosure changed. See [v1.45](evidence/v145/).

## New in v1.44

NS-24 translates the weighted concentration inequality to exact pencil
directions: the relative minorant loss must be at most
`nu_k + eta_a ||v_k||^2/q+[v_k]`, with source admissibility and all mixture
cross terms retained. This is a fixed-window head condition. The complete
criterion still needs cofinal uniform control; uniformly bounded errors
already suffice under v1.36's hypotheses. The twelve small lambda=4 N=48
values are cited only as diagnostics. No new computation or concentration
bound is claimed, and the v1.43 enclosure is unchanged. G2 and RH stay open.

## New in v1.43

NS-19 closes with a two-sided enclosure of the complete first positive
lambda=4 zero and a precise resolution statement. The radius is
`sqrt(C_ell*rho)/0.0016 < 8.752082e-33 < 9e-33`. The missing lower-energy
transfer would require a Rayleigh gap about `3.2032e-153` (relative
`1.3055e-78`), plus a suitably centered trial for a gamma-centered result.
The finite N=120 discrepancy of about `+2.92504e-71` is separately
certified and does not transfer to the complete ground. This is a limit
of the displayed archived bounds, not a failure of the object or a
universal no-go theorem. No new window or tail metric; G2 and RH stay open.

## New in v1.42

One local zero of the **complete** lambda=4 ground transform is now
certified within 0.1 of the first zeta ordinate. It is unique and simple
in that interval. The complete even-sector separator 1e-67 makes an
energy-projection bound small enough to transfer endpoint and derivative
signs. The old global separator is too coarse for the same test.

All 4097 trial coefficients and the archived infinite-tail bounds are
retained. Both 1024/1280-bit replays and a second implementation pass.
No new window is computed. This does not determine the discrepancy's sign,
order earlier zeros, or establish cofinal convergence. G2 and RH remain
open. [Proof and replay](evidence/v142/).

## New in v1.41

The existing lambda=3, N=120 compression reproduces the first eight local
zero discrepancies in CCM §6 Figure 1, with interval eigenpair/root gates
replayed at 768 and 1024 bits. The first discrepancy is approximately
1.582329697193127e-34, matching their rounded 1.6e-34.

This identifies the missing `(-1)^n` centering phase in the prior NS-14
script. Its sinc-lattice conclusion is withdrawn; the old run is preserved
with a correction. The new result is finite-dimensional and supplies no
complete-ground zero locations or cofinal convergence. G2 and RH remain open.
The literature comparison is integrated and both missing evidence groups
remain OPEN. [Proof and replay](evidence/v141/).

## New in v1.39

Two precise meta-obstructions delimit information-losing estimates. The
optimal full-histogram mass-cap bound, and a mass/height/variation
relaxation, cannot supply a cofinal finite floor for the actual symbol.
A separate spectral-rotation theorem preserves any finite head and its
complete operator action while exposing the divergent negative multiplier
edge. Its conjugates need not remain multiplication operators.

The unrestricted slogan “every location-insensitive estimate fails” is
false; an exact positive counterexample and a ten-route coverage audit
are included. These results do not close G2 or prove RH.

[Proof, exact checks and scope audit](evidence/v139/).

## New in v1.38

v1.36 reduced G2 to a **uniform finite floor**: one constant `C_*` with
`W_λ >= -C_*·I` along a cofinal family suffices, with no decay required.
v1.38 tests that reduction directly instead of seeking another positivity
certificate.

With a common shift `δ = 8`, head cutoff `N = 256`, remote cutoff
`J = 4096`, moment order 16, and **no tail-metric prerequisite** (`Z = 0`),
both complete parity forms are certified at λ = 5, 6, 8:

    -8  <=  inf σ(W_λ^±)  <  1e-16

The lower bound retains the complete infinite Fourier tail; the upper
bound is a certified finite-support trial quotient. By support
consistency the floor holds for every `1 < λ <= 8`. The same exact dyadic
witnesses pass at 160 and 256 bits.

The shift is what makes it affordable: the remote cutoff needs
`N+1 > L·exp(M_φ − δ)`, so `δ = 8` buys a factor `e^8`. But
`prop:v138-shifted-floor` proves any *bounded* shift keeps the exponential
barrier of `prop:v125-cutoff-cost`; escaping it in this comparison would
need `δ` to grow like `M_φ ~ λ`, which is uninformative. The certificate's
generalized margin falls from 0.84 to 0.10 (odd) across the three windows.
**That decrease measures enclosure headroom, not the sign of the physical
edge** — no cofinal lower estimate is asserted, and no G2 gap is closed.

- [certificates, 160 and 256 bits](evidence/v138/)

## New in v1.37

v1.36 showed that one uniform finite ordinary lower floor on the complete
small-residual complement would suffice. v1.37 tests whether the older
scalar primitive estimate could meet this weaker target.

It cannot: for the exact arithmetic symbol, its optimal scalar error
`a Delta(beta_a)` tends to infinity. The pointwise infimum of `beta_a`
also tends to minus infinity. Both conclusions are unconditional.

The proof uses a nonnegative frequency probe whose Fourier transform
vanishes at the two physical cutoff endpoints. Under RH its pairing with
the exact symbol retains a negative cutoff side lobe around a zero.
Any bounded cofinal scalar certificate would itself imply RH via v1.36,
then contradict that pairing. The linear rates are RH-conditional; no
unconditional linear rate is asserted.

The probe is not a physical squared Paley–Wiener transform, so these scalar
obstructions do not refute positivity of the physical form. The signed
concentration estimate, retaining favorable and unfavorable levels jointly,
remains open in both parities. No G2 sign gap was closed.

- [Proof and novelty report](evidence/v137/research_report.md)
- [Proof excerpt](evidence/v137/new_section.tex)
- [Independent adversarial review](evidence/v137/adversarial_review.md)
- [Probe checks](evidence/v137/check_probe.py) · [results](evidence/v137/probe_results.json)

The ingredients are classical; worldwide novelty is not claimed. Numerical
quadrature is diagnostic and not a proof.

## The `lambda = 4` evidence

The original v1.26 reproduction bundle has been recovered and committed
under [`evidence/v126/`](evidence/v126/): 468 files, byte-identical to the
archived ZIP (SHA-256 `ccdb8eaa…82d8f`, independently re-verified). It
includes both final certificate directories:

- [complete even sector — `g2_simultaneous`](evidence/v126/g2_simultaneous/)
- [complete odd sector — `g2_odd_complement`](evidence/v126/g2_odd_complement/)

Final proof gates using the saved ingredients, witness bindings and the
exact shared-head equality were replayed successfully. This did not
regenerate witnesses or rerun every residual assembly; RESTORED in the
ledger records availability, not a fresh independent audit of every
computation. Provenance and per-file checksums:
[`manifest/README_v126_evidence_recovery.md`](manifest/README_v126_evidence_recovery.md).

## License

Apache-2.0 — see [LICENSE](LICENSE).
