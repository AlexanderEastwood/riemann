# Riemann project research map

_Generated from `research-map.json` — last updated 2026-09-23._
_Do not hand-edit: run `python3 tools/make_map.py`._

```mermaid
graph LR
  rh["RH"]
  g1["G1 (weak)<br/><small>thm:v14-radical</small><br/><small>&#128193; evidence/v124/g2_source_certificate</small>"]
  fixedspace["Fixed-space / Burnol Sonine route<br/><small>continuation: OPERATOR-BRIDGES</small>"]
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
  concentration["signed weighted concentration<br/><small>prop:v131-concentration</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: uniform complete signed operator floor remains unproved</b></small><br/><small>continuation: WEIL-FLOOR</small>"]
  weaken["Target weakening<br/><small>continuation: WEIL-FLOOR</small>"]
  floor["uniform finite floor suffices<br/><small>prop:v136-bounded-floor</small><br/><small>&#128193; evidence/v136</small><br/><small>continuation: WEIL-FLOOR</small>"]
  gapfree["no uniform positive gap exists<br/><small>prop:v135-growing-radical</small><br/><small>&#128193; evidence/v135</small>"]
  floortest["W_lambda >= -8 I at lambda=5,6,8<br/><small>prop:v138-three-floors</small><br/><small>&#128193; evidence/v138</small>"]
  shiftbarrier["bounded shift keeps the exp cutoff barrier<br/><small>prop:v138-shifted-floor</small><br/><small>&#128193; evidence/v138</small>"]
  metablind["Scoped information-loss obstructions<br/><small>thm:v139-probe-relaxation; thm:v139-protected-orbit</small><br/><small>&#128193; evidence/v139</small>"]
  altroutes["Alternative mechanisms: distinct missing inputs"]
  circle["circle / Toeplitz-Hankel lens<br/><small>&#128193; evidence/diag_true_symbol</small><br/><small>continuation: OPERATOR-BRIDGES</small>"]
  debranges["de Branges / Hermite-Biehler<br/><small><b>wall: screw-kernel positivity = RH; no fixed-window bridge</b></small><br/><small>continuation: OPERATOR-BRIDGES</small>"]
  f1["function field / Hodge / F_1<br/><small><b>wall: no intersection form supplied for this window (missing construction)</b></small><br/><small>continuation: OPERATOR-BRIDGES</small>"]
  nb["Nyman-Beurling-Baez-Duarte<br/><small>prop:ns53-nb-block-gain; eq:ns53-nb-rbc</small><br/><small>&#128193; evidence/ns53_nb_blocks</small><br/><small><b>wall: RBC: corrected arithmetic residual block correlations (open sufficient input)</b></small><br/><small>continuation: NB-GAIN</small>"]
  li["Direct rational Li / entire window-test identification<br/><small>&#128193; evidence/diag_routes/li</small><br/><small><b>wall: direct rational-Li / entire-window classes intersect only at zero</b></small>"]
  dbn["de Bruijn–Newman: paired transport<br/><small>prop:ns52-cluster; prop:ns52-unmatched</small><br/><small>&#128193; evidence/ns52_heat_pairs</small><br/><small><b>wall: complete signed transport with uniform support control (open)</b></small><br/><small>continuation: HEAT-TRANSPORT</small>"]
  ccmmu["W_4 >= 0  <=>  CCM mu_lambda >= 0 for all lambda <= 4"]
  simpleeven4["complete W_4: simple even ground; real-zero transform<br/><small>prop:v140-ground4; cor:v140-real-zeros</small><br/><small>&#128193; evidence/v140</small><br/><small>continuation: CCM-LIMIT</small>"]
  stepb["CCM step (b): finite-compression zeros track zeta zeros (numerical)<br/><small>&#128193; evidence/diag_ns2_semantic_lock</small><br/><small>continuation: CCM-LIMIT</small>"]
  semanticlock["CCM finite-compression semantic lock, lambda=3 N=120<br/><small>lem:v141-centering; prop:v141-ccm-lock</small><br/><small>&#128193; evidence/v141</small><br/><small>continuation: CCM-LIMIT</small>"]
  groundzero4["complete ground zero within 0.1 of gamma_1<br/><small>lem:v142-energy-projection; prop:v142-ground-zero</small><br/><small>&#128193; evidence/v142</small><br/><small>continuation: CCM-LIMIT</small>"]
  groundzero4resolution["first complete zero within 9e-33; archived resolution quantified<br/><small>prop:v143-first-zero-bound; prop:v143-resolution; prop:v143-fixed-window-meaning</small><br/><small>&#128193; evidence/v143</small><br/><small>continuation: CCM-LIMIT</small>"]
  pencilconcentration["pencil loss budget; cofinal obligation retained<br/><small>prop:v144-pencil-concentration</small><br/><small>&#128193; evidence/v144</small><br/><small>continuation: WEIL-FLOOR</small>"]
  betaexplicit["exact lattice symbol; varying envelopes<br/><small>prop:v146-beta-explicit</small><br/><small>&#128193; evidence/v146</small>"]
  minorantlevels["bounded-complexity minorants: arithmetic gap remains<br/><small>prop:v146-packet-loss; prop:v146-level-complexity</small><br/><small>&#128193; evidence/v146</small><br/><small><b>wall: ZLD + packet: conditional minorant-complexity obstruction only</b></small><br/><small>continuation: LEVEL-PACKETS</small>"]
  zeroleveldistribution["zero level distribution and packet coverage: open inputs<br/><small>prop:v147-level-separation; ass:v147-zld; prop:v147-depth-measure; prop:v147-broad-packet</small><br/><small>&#128193; evidence/v147</small><br/><small><b>wall: ZLD + packet: conditional minorant-complexity obstruction only</b></small><br/><small>continuation: LEVEL-PACKETS</small>"]
  weightedexactcost["weighted exact cost: peak bound fails at critical levels<br/><small>prop:v149-critical-density; prop:v149-weighted-cost; prop:v149-qc1-insufficient; ass:v149-qg</small><br/><small>&#128193; evidence/v149</small><br/><small><b>wall: QG + WLH packet: conditional minorant-complexity obstruction only</b></small><br/><small>continuation: LEVEL-PACKETS</small>"]
  capacityweight["positive arithmetic weight: critical capacity input<br/><small>lem:v150-weight; prop:v150-critical-energy; ass:v150-cae</small><br/><small>&#128193; evidence/v150</small><br/><small><b>wall: CAE</b></small><br/><small>continuation: WEIL-FLOOR</small>"]
  capacityslack["fixed energy loss for the Gaussian arithmetic weight<br/><small>prop:v150-capacity-slack</small><br/><small>&#128193; evidence/v150</small><br/><small><b>wall: fixed-slack shortcut: eta >= delta kappa exp(gamma lambda^2) - O(lambda log lambda)</b></small>"]
  inputcomparison["ZLD to QG; CAE is the signed-floor target<br/><small>prop:v151-input-comparison</small><br/><small>&#128193; evidence/v151</small><br/><small>continuation: WEIL-FLOOR</small>"]
  capacitychannels["Fixed/sub-endpoint channel deletion with unchanged signed terms<br/><small>prop:ns43-fixed-channel; prop:ns43-moving-channel</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: channel deletion: unbounded comparison error for the Gaussian weight</b></small>"]
  bumpstrength["Restricted bump discrepancy can carry the full zero obstruction<br/><small>prop:ns43-bump-strength</small><br/><small>&#128193; evidence/v152</small>"]
  adaptiveidentity["Unrestricted exact adaptive hierarchy = complement floor<br/><small>ns43-conc-prop-adaptive</small><br/><small>&#128193; evidence/v152</small><br/><small>continuation: WEIL-FLOOR</small>"]
  scalarsetshortcut["Scalar set bounds alone determine signed floor: general inference<br/><small>ns43-conc-prop-scalar</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: general inference false: countermodels with equal scalar set extrema and opposite signed bottoms</b></small>"]
  relativeselection["Complete relative selection and entire-transform control<br/><small>prop:ns43-ccm-rayleigh-selection; prop:ns43-ccm-residual-selection</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: complete relative selection plus entire-transform control (both open)</b></small><br/><small>continuation: CCM-LIMIT</small>"]
  absoluteselection["Absolute residual/resolvent data alone select ground: abstract inference<br/><small>prop:ns43-ccm-nonselection</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: abstract inference false: countermodel family with alternating profiles</b></small>"]
  coarseprofile["Single profile from the specified coarse rescaled liminf<br/><small>prop:ns43-ccm-coarse-profile</small><br/><small>&#128193; evidence/v152</small><br/><small><b>wall: under the explicit coarse scale the limit form is zero; finer scales open</b></small>"]
  fineradicalrank["Uniform or polynomial positive gap after o(lambda²/log lambda) removed directions<br/><small>lem:ns46-finite-arc; ns46-a2-cor-large-block; ns46-a2-cor-rank</small><br/><small>&#128193; evidence/v153</small><br/><small><b>wall: positive-gap strategy must remove rank >= lambda^2/(20000 log lambda)</b></small>"]
  kernelapi["Exact kernel exclusion: affine-potential injectivity<br/><small>prop:ns51-affine-potential; eq:ns51-api</small><br/><small>&#128193; evidence/ns51_kernel</small><br/><small><b>wall: API: actual arithmetic affine-potential injectivity (open)</b></small><br/><small>continuation: KERNEL-API</small>"]
  generic_h1["Generic H¹ bootstrap from a zero eigenvalue<br/><small>prop:ns51-no-generic-bootstrap</small><br/><small>&#128193; evidence/ns51_kernel</small><br/><small>continuation: KERNEL-API</small>"]
  localucp["Local open-set UCP for the full prime-shift operator<br/><small>prop:ns55-local-ucp-counterexample; prop:ns55-parity-ucp-counterexample</small><br/><small>&#128193; evidence/v155</small><br/><small><b>wall: local f=A_a f=0 does not force f=0; whole-window API is not refuted</b></small><br/><small>continuation: KERNEL-API</small>"]
  fullpositivecone["Ordinary-cone positivity for the full Weil semigroup<br/><small>prop:ns55-nonpositive-semigroup</small><br/><small>&#128193; evidence/v155</small><br/><small><b>wall: order-preservation shortcut fails; quadratic-form positivity is a different property</b></small><br/><small>continuation: KERNEL-API</small>"]
  finiteweightcontrols["Finite prime-weight changes: negative tests and first-zero controls<br/><small>cor:ns57-finite-weight-negative; thm:ns57-first-zero-controls; cor:ns57-fixed-direction-sensitivity</small><br/><small>&#128193; evidence/v156</small>"]
  boundedfloorstability["Bounded perturbations preserve the finite-floor objective<br/><small>lem:ns57-bounded-detection; thm:ns57-bounded-floor-stability</small><br/><small>&#128193; evidence/v156</small><br/><small>continuation: WEIL-FLOOR</small>"]
  radicalboundarytest["Translated-radical boundary test: exact kernel equivalence and forced controls<br/><small>prop:ns58-boundary-identity; prop:ns58-equivalence; prop:ns58-forced-pairing</small><br/><small>&#128193; evidence/v157</small><br/><small>continuation: KERNEL-API</small>"]
  nbdifference["NB adjacent-difference norm budget<br/><small>prop:v158-adjacent-budget; prop:v158-mellin-budget</small><br/><small>&#128193; evidence/v158</small><br/><small>continuation: NB-GAIN</small>"]
  nbrawlog["NB uniform logarithmic raw norm<br/><small>prop:v158-lindelof-budget</small><br/><small>&#128193; evidence/v158</small><br/><small><b>wall: known zeta large values contradict every fixed logarithmic N^(-2) raw norm bound</b></small>"]
  nbeulergrid["Uniform logarithmic norm after explicit Euler-grid correction<br/><small>prop:ns60-growing-euler-obstruction</small><br/><small>&#128193; evidence/v159</small><br/><small><b>wall: zeta large values exceed the allowed finite Euler-product loss</b></small>"]
  nbsmoothedbudget["Fixed smoothed NB: positive averages and N^(-2) trace<br/><small>prop:ns61-rh-equivalence; prop:ns61-average-budget</small><br/><small>&#128193; evidence/v159</small><br/><small>continuation: NB-GAIN</small>"]
  nbsmoothedcorrelation["Actual optimized smoothed residual correlations<br/><small>eq:ns61-open-correlation; eq:ns61-endpoint-correlation; prop:ns69-remainder; prop:ns71-selected-input</small><br/><small>&#128193; evidence/v160</small><br/><small><b>wall: non-summable lower contraction for the actual optimized residual (open sufficient input)</b></small><br/><small>continuation: NB-GAIN</small>"]
  nbsharpintegrated["Strong convergence of the smoothed canonical sharp Mobius sequence<br/><small>prop:ns62-smoothed-obstruction; prop:ns62-positive-cone; prop:ns64-cone-distance; prop:ns65-cesaro-obstruction</small><br/><small>&#128193; evidence/v159</small><br/><small><b>wall: a surviving weighted-Mertens witness for this coefficient rule</b></small><br/><small>continuation: NB-GROWTH</small>"]
  nbchangingnorm["Relative convergence with increasing Mellin smoothing<br/><small>prop:ns63-one-atom</small><br/><small>&#128193; evidence/v159</small><br/><small><b>wall: one-atom unconditional control refutes this convergence inference</b></small>"]
  nbcanonicalgrowth["Canonical smoothed norm: subpolynomial growth<br/><small>prop:ns66-growth-bounds; cor:ns66-growth-exponent; prop:ns67-polynomial-cutoff; prop:ns67-abel-conditioning</small><br/><small>&#128193; evidence/v160</small><br/><small><b>wall: direct subpolynomial canonical norm bound, or a bounded cofinal subsequence (open)</b></small><br/><small>continuation: NB-GROWTH</small>"]
  nbcanonicalcells["Complete canonical divisor cells and full tail<br/><small>prop:ns67-cells; lem:ns67-remainder; prop:ns67-polynomial-cutoff</small><br/><small>&#128193; evidence/v160/ns67</small><br/><small>continuation: NB-GROWTH</small>"]
  nbabelwholegain["Power gain solely between the two complete Abel vectors<br/><small>prop:ns67-abel-conditioning</small><br/><small>&#128193; evidence/v160/ns67</small><br/><small><b>wall: uniform conditioning excludes an exponent improvement in this whole-vector split</b></small><br/><small>continuation: NB-GROWTH</small>"]
  nbrenewalforcing["Positive renewal with signed arithmetic forcing<br/><small>prop:ns68-weighted-inversion; prop:ns68-scalar-criterion</small><br/><small>&#128193; evidence/v160/ns68</small><br/><small><b>wall: independent square-root-plus-epsilon bound for the signed forcing</b></small><br/><small>continuation: NB-GROWTH</small>"]
  nbcriticalrenewalenergy["Finite total critical renewal energy<br/><small>cor:ns68-critical-energy</small><br/><small>&#128193; evidence/v160/ns68</small><br/><small><b>wall: critical-line Mellin pole contradicts finite weighted L2 energy</b></small><br/><small>continuation: NB-GROWTH</small>"]
  nbrepairedbounds["Uniform comparison with the repaired elementary Gram<br/><small>prop:ns70-cusp; prop:ns70-repaired-background</small><br/><small>&#128193; evidence/v160/ns70</small><br/><small><b>wall: pointwise Mellin-density comparison forced by all-coefficient localization</b></small>"]
  nbselectedpreconditioner["Repaired-kernel selection measured with true energy<br/><small>prop:ns71-selected-input</small><br/><small>&#128193; evidence/v160/ns71</small><br/><small><b>wall: cofinal lower numerator and upper selected cost with nonsummable relative gain</b></small><br/><small>continuation: NB-GAIN</small>"]
  nblocalgeometry["Complete local energy and discrete curvature<br/><small>prop:ns72-local-energy; prop:ns72-interpolation; prop:ns72-curvature</small><br/><small>&#128193; evidence/v161/ns72</small><br/><small>continuation: NB-GAIN</small>"]
  nbcurvaturearithmetic["Cofinal arithmetic curvature and selected cost<br/><small>eq:ns72-local-directions</small><br/><small>&#128193; evidence/v161/ns72</small><br/><small><b>wall: actual curvature lower bound and selected true cost giving nonsummable relative contraction</b></small><br/><small>continuation: NB-GAIN</small>"]
  nbsamegramcontrol["Infer convergence from shared Gram geometry and finite efficiency<br/><small>prop:ns74-same-gram; cor:ns74-finite-indistinguishability</small><br/><small>&#128193; evidence/v161/ns74</small><br/><small><b>wall: explicit inserted inner-factor control; scope is this finite-statistics inference</b></small>"]
  nbdivisorfeedback["Exact divisor feedback and finite unit-step failure<br/><small>prop:ns75-divisor-cells</small><br/><small>&#128193; evidence/v162/ns75</small><br/><small>continuation: NB-GAIN</small>"]
  nbcontinuousdefect["Exact continuous inner-factor defect and strict closure separation<br/><small>prop:ns76-continuous-distance; prop:ns76-strict-closure</small><br/><small>&#128193; evidence/v162/ns76</small><br/><small>continuation: NB-CONTINUOUS</small>"]
  nbcontinuoustail["Complete continuous zero-tail budget<br/><small>prop:ns77-tail-budget</small><br/><small>&#128193; evidence/v162/ns77</small><br/><small>continuation: NB-CONTINUOUS</small>"]
  nbarithmeticsampling["Complete reciprocal-knot norm and exact divisor inversion<br/><small>prop:ns78-sampling; eq:ns78-sample-inverse</small><br/><small>&#128193; evidence/v163/ns78</small><br/><small>continuation: NB-SAMPLES</small>"]
  nbbalancedfeedback["Tail-balanced divisor feedback control<br/><small>prop:ns79-balance</small><br/><small>&#128193; evidence/v163/ns79</small><br/><small>continuation: NB-GAIN</small>"]
  nbarithmeticpreconditioner["Uniform efficiency using the full arithmetic sampling Gram<br/><small>prop:ns80-uniform-efficiency</small><br/><small>&#128193; evidence/v163/ns80</small><br/><small>continuation: NB-GAIN</small>"]
  nbfiniteconditioning["Polynomial ordinary Gram conditioning and an effective finite comparator<br/><small>prop:ns81-conditioning; prop:ns81-finite-comparator</small><br/><small>&#128193; evidence/v164/ns81</small><br/><small>continuation: NB-GAIN</small>"]
  nbcompressedtail["Finite physical comparator with an exact rank-two tail<br/><small>prop:ns82-tail-compression</small><br/><small>&#128193; evidence/v165/ns82</small><br/><small>continuation: NB-GAIN</small>"]
  nbcriticalfloor["Critical-zero logarithmic lower bound at every fixed smoothing order<br/><small>prop:ns83-log-floor</small><br/><small>&#128193; evidence/v166/ns83</small><br/><small>continuation: NB-GAIN</small>"]
  nbuniformrelativecontraction["Fixed-fraction contraction of the full error at every doubling<br/><small>eq:ns83-gain-budget</small><br/><small>&#128193; evidence/v166/ns83</small><br/><small>continuation: NB-GAIN</small>"]
  nboptimizedpotential["Optimized arithmetic potential and complete observation tails<br/><small>&#128193; evidence/ns86_optimized_arithmetic</small><br/><small>continuation: NB-GAIN</small>"]
  nbconvolutioncontrol["Divisor-convolution correction from N to N squared: finite control<br/><small>&#128193; evidence/ns86_optimized_arithmetic</small><br/><small>continuation: NB-GAIN</small>"]
  nbjointlocalization["Joint finite arithmetic observations preserve logarithmic gain scale<br/><small>&#128193; evidence/ns87_joint_tail</small><br/><small>continuation: NB-GAIN</small>"]
  nbdilationenvelope["Multiplicative normal equations and a scalar whole-error upper envelope<br/><small>&#128193; evidence/ns88_dilation_defect</small><br/><small>continuation: NB-DILATION</small>"]
  nbdilationstrongnumerator["Eventual energy/j^p dilation-defect lower bound with p<1<br/><small>&#128193; evidence/ns88_dilation_defect</small><br/><small><b>wall: The proposed stronger numerator forces error decay contradicting the critical-zero lower bound</b></small><br/><small>continuation: NB-DILATION</small>"]
  nbnormalizedupper["Constructive zero-exterior upper certificates preserve every decay rate<br/><small>&#128193; evidence/ns89_upper_normalization</small><br/><small>continuation: NB-SAMPLES</small>"]
  nbmobiusjointcancellation["Exact Mobius cancellation; fixed-size absolute-bound loss<br/><small>&#128193; evidence/ns90_mobius_gain</small><br/><small>continuation: MOBIUS-COST, MOBIUS-MARGIN</small>"]
  nbjointabelbound["Joint first-primitive finite lower bound with complete grouped tail<br/><small>&#128193; evidence/ns91_joint_abel</small><br/><small>continuation: MOBIUS-COST, MOBIUS-MARGIN</small>"]
  nbarithmeticcostbudget["Complete scalar cost budget and a feasible endpoint-only update<br/><small>&#128193; evidence/ns92_arithmetic_cost</small><br/><small>continuation: MOBIUS-COST, MOBIUS-MARGIN</small>"]
  nbaveragedabsolutecost["Averaging the fully separated absolute Mobius cost<br/><small>&#128193; evidence/ns93_averaged_cost</small><br/><small><b>wall: productwise absolute values force a linear majorant even before averaging</b></small><br/><small>continuation: MOBIUS-COST, MOBIUS-MARGIN</small>"]
  circlecountinference["Tangent-circle similarity point and count imbalance infer RH<br/><small>&#128193; evidence/ns94_circle_inversion</small><br/><small><b>wall: exact symmetric off-line control preserves the proposed geometric count and infinity features</b></small><br/><small>continuation: ZERO-GEOMETRY</small>"]
  nbsquareproductrestriction["Square-scale product restriction and complete gain split<br/><small>&#128193; evidence/ns95_square_product</small><br/><small>continuation: NB-GAIN</small>"]
  nblcmsquarecone["LCM divisor squares: complete-rule floors and signed refit equivalence<br/><small>&#128193; evidence/ns96_lcm_square</small><br/><small>continuation: NB-GAIN</small>"]

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
  nbfiniteconditioning --> nbcompressedtail
  nbsmoothedbudget --> nbcriticalfloor
  nbcriticalfloor --> nbuniformrelativecontraction
  nbarithmeticsampling --> nboptimizedpotential
  nboptimizedpotential --> nbconvolutioncontrol
  nboptimizedpotential --> nbjointlocalization
  nboptimizedpotential --> nbdilationenvelope
  nbdilationenvelope --> nbdilationstrongnumerator
  nbsmoothedbudget --> nbnormalizedupper
  nbjointlocalization --> nbmobiusjointcancellation
  nbmobiusjointcancellation --> nbjointabelbound
  nbjointabelbound --> nbarithmeticcostbudget
  nbarithmeticcostbudget --> nbaveragedabsolutecost
  altroutes --> circlecountinference
  nbjointlocalization --> nbsquareproductrestriction
  nbsquareproductrestriction --> nblcmsquarecone
  concentration -. "uniform complete signed operator floor remains unproved" .-> floor
  debranges -. "screw-kernel positivity = RH; no fixed-window bridge" .-> rh
  nb -. "RBC: corrected arithmetic residual block correlations (open sufficient input)" .-> rh
  dbn -. "complete signed transport with uniform support control (open)" .-> rh
  capacityweight -. "CAE" .-> floor
  relativeselection -. "complete relative selection plus entire-transform control (both open)" .-> g2
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
  click nbcompressedtail "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v165/ns82/" "evidence: evidence/v165/ns82" _blank
  click nbcriticalfloor "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v166/ns83/" "evidence: evidence/v166/ns83" _blank
  click nbuniformrelativecontraction "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/v166/ns83/" "evidence: evidence/v166/ns83" _blank
  click nboptimizedpotential "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns86_optimized_arithmetic/" "evidence: evidence/ns86_optimized_arithmetic" _blank
  click nbconvolutioncontrol "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns86_optimized_arithmetic/" "evidence: evidence/ns86_optimized_arithmetic" _blank
  click nbjointlocalization "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns87_joint_tail/" "evidence: evidence/ns87_joint_tail" _blank
  click nbdilationenvelope "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns88_dilation_defect/" "evidence: evidence/ns88_dilation_defect" _blank
  click nbdilationstrongnumerator "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns88_dilation_defect/" "evidence: evidence/ns88_dilation_defect" _blank
  click nbnormalizedupper "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns89_upper_normalization/" "evidence: evidence/ns89_upper_normalization" _blank
  click nbmobiusjointcancellation "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns90_mobius_gain/" "evidence: evidence/ns90_mobius_gain" _blank
  click nbjointabelbound "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns91_joint_abel/" "evidence: evidence/ns91_joint_abel" _blank
  click nbarithmeticcostbudget "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns92_arithmetic_cost/" "evidence: evidence/ns92_arithmetic_cost" _blank
  click nbaveragedabsolutecost "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns93_averaged_cost/" "evidence: evidence/ns93_averaged_cost" _blank
  click circlecountinference "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns94_circle_inversion/" "evidence: evidence/ns94_circle_inversion" _blank
  click nbsquareproductrestriction "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns95_square_product/" "evidence: evidence/ns95_square_product" _blank
  click nblcmsquarecone "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/ns96_lcm_square/" "evidence: evidence/ns96_lcm_square" _blank

  classDef proved fill:#a5d6a7,stroke:#1b5e20,stroke-width:1px,color:#000;
  class g1,windows,w3,w4e,w4o,w4,weaken,floor,gapfree,floortest,shiftbarrier,metablind,ccmmu,simpleeven4,semanticlock,groundzero4,groundzero4resolution,pencilconcentration,betaexplicit,inputcomparison,bumpstrength,adaptiveidentity,finiteweightcontrols,boundedfloorstability,radicalboundarytest,nbdifference,nbsmoothedbudget,nbcanonicalcells,nblocalgeometry,nbdivisorfeedback,nbcontinuousdefect,nbcontinuoustail,nbarithmeticsampling,nbbalancedfeedback,nbarithmeticpreconditioner,nbfiniteconditioning,nbcompressedtail,nbcriticalfloor,nboptimizedpotential,nbconvolutioncontrol,nbjointlocalization,nbdilationenvelope,nbnormalizedupper,nbmobiusjointcancellation,nbjointabelbound,nbarithmeticcostbudget,nbsquareproductrestriction,nblcmsquarecone proved;
  classDef live fill:#ffd54f,stroke:#f57f17,stroke-width:3px,color:#000;
  class stepb,kernelapi live;
  classDef closed fill:#ef9a9a,stroke:#b71c1c,stroke-width:1px,color:#000;
  class w5,primenorm,normcontr,schatten,sampling,farmaj,blockmetric,flattop,recipband,cotlar,scalarprim,li,capacityslack,capacitychannels,scalarsetshortcut,absoluteselection,coarseprofile,fineradicalrank,generic_h1,localucp,fullpositivecone,nbrawlog,nbeulergrid,nbsharpintegrated,nbchangingnorm,nbabelwholegain,nbcriticalrenewalenergy,nbrepairedbounds,nbsamegramcontrol,nbuniformrelativecontraction,nbdilationstrongnumerator,nbaveragedabsolutecost,circlecountinference closed;
  classDef blocked fill:#ce93d8,stroke:#4a148c,stroke-width:1px,color:#000;
  class concentration,minorantlevels,zeroleveldistribution,weightedexactcost,capacityweight,relativeselection,nbsmoothedcorrelation,nbcanonicalgrowth,nbrenewalforcing,nbselectedpreconditioner,nbcurvaturearithmetic blocked;
  classDef open fill:#cfd8dc,stroke:#37474f,stroke-width:1px,color:#000;
  class rh,fixedspace,g2,uniform,altroutes,circle,debranges,f1,nb,dbn open;
  subgraph Legend
    direction LR
    lg_live["current route (gold)"]:::live
    lg_closed["scoped exclusion"]:::closed
    lg_proved["proved"]:::proved
    lg_open["open"]:::open
    lg_blocked["blocked"]:::blocked
  end
```

## Status

| status | count | meaning |
|---|---:|---|
| `proved` | 48 | established result |
| `live` | 2 | current route (gold): being worked now |
| `closed` | 33 | scoped comparison, construction or inference excluded under its stated hypotheses |
| `blocked` | 11 | attempted; obstruction found |
| `open` | 10 | unresolved target or route; may have prior partial work |

## Shared continuation inputs

These tags describe unfinished continuations, **not assumptions needed for
the existing proved results**. Identical tags group an explicitly stated
objective; the relation and direction restrictions below still matter.
A shared RH consequence does not make two estimates identical. Failure of
a stronger sufficient bound does not disprove the smaller quantity it bounds.

| input | question still open | tasks / scope |
|---|---|---|
| [MOBIUS-COST](#input-mobius-cost) | Bound the actual projected cost of the fixed logarithmic Mobius direction | NS73 p1; NS90–93,98 |
| [MOBIUS-MARGIN](#input-mobius-margin) | Force a compatible signed numerator for the same fixed direction | NS90,91,93,98 |
| [NB-GAIN](#input-nb-gain) | Lower-bound actual residual gain along a cofinal sequence | NS53,59,61,69,71–73,75,79–83,86,87,95–97 |
| [NB-SAMPLES](#input-nb-samples) | Make a complete signed arithmetic upper-error sum tend to zero | NS78,89; NS85 fixed-template test |
| [NB-GROWTH](#input-nb-growth) | Control internal canonical arithmetic cancellation at fixed smoothing | NS66–68 |
| [NB-DILATION](#input-nb-dilation) | Prove growth of the cumulative actual dilation defect | NS88 |
| [NB-CONTINUOUS](#input-nb-continuous) | Bridge continuous zero-defect information to the integer problem | NS76,77 |
| [WEIL-FLOOR](#input-weil-floor) | One complete signed lower floor with a common cofinal constant | NS24,34,39,43,47,50; v1.36 |
| [KERNEL-API](#input-kernel-api) | Exclude full-window arithmetic nullvectors on the complete domain | NS51,55,58 |
| [CCM-LIMIT](#input-ccm-limit) | Obtain complete relative ground selection and transform control | NS5,14,18,19,43 |
| [LEVEL-PACKETS](#input-level-packets) | Supply arithmetic level mass and independent admissible packet coverage | NS27,29,32–33,39,54 |
| [ZERO-GEOMETRY](#input-zero-geometry) | Find zeta-specific zero rigidity beyond reflection symmetry | NS94; NS100 reassessment; NS101 bounded attempt; NS103 window-sensitivity diagnostic; NS104 interpretation audit |
| [HEAT-TRANSPORT](#input-heat-transport) | Control exterior-cluster transport and test-support costs | NS52 |
| [OPERATOR-BRIDGES](#input-operator-bridges) | Construct the route-specific operator or geometric transfer | Fixed-space; circle/Toeplitz; de Branges; function-field/Hodge |

<a id="input-mobius-cost"></a>
### MOBIUS-COST: Bound the actual projected cost of the fixed logarithmic Mobius direction

For d_n=-mu(n) log(2N/n), N<n<=2N, retain K_N=||(I-Pi_N) sum d_n a_n||². The NS93 sufficient averaged route asks for bounded means of K_(2^j) over J<=j<2J, together with MOBIUS-MARGIN on the same ranges. Pointwise bounded K_N is stronger. NS98 does not supply either bound.

**Scope / stop:** This is the same direction and exact projected cost in NS73 p1 and NS90–93/98. It is not the full NS73 three-template span or the curvature direction. NS92 gives K_N<=U_N<=kappa log(2) S_N; bounding the signed suffix energy S_N is sufficient but stronger. NS93 excludes only the fully absolute product majorant. NS98 bounds the projected diagonal but leaves its signed cross term unestimated. A new decomposition, finite table or free trace rescaling alone does not change the input.

Sources: [evidence/ns98_projected_cost/argument.tex](evidence/ns98_projected_cost/argument.tex) · [evidence/ns92_arithmetic_cost/argument.tex](evidence/ns92_arithmetic_cost/argument.tex) · [evidence/ns93_averaged_cost/argument.tex](evidence/ns93_averaged_cost/argument.tex).

<a id="input-mobius-margin"></a>
### MOBIUS-MARGIN: Force a compatible signed numerator for the same fixed direction

With ell_N=<r_N,sum d_n a_n>, obtain a lower bound for its gain relative to E_N and the same projected cost K_N. The NS91 lower bound b_N retains the joint interior allowance and complete tail. NS93 gives a sufficient averaged criterion: positive lower means of (b_(2^j)/E_(2^j))_+ on the same ranges as the bounded cost means.

**Scope / stop:** A cost upper bound alone does not prove descent. The averaged sufficient criterion is not claimed necessary; actual ell_N may admit bounds that b_N cannot detect. The N^6 grouped tail is controlled, but its interior margin remains open. The divisor-inversion quadratic rewrite under the old normal equations gives the same numerator.

Sources: [evidence/ns91_joint_abel/argument.tex](evidence/ns91_joint_abel/argument.tex) · [evidence/ns93_averaged_cost/argument.tex](evidence/ns93_averaged_cost/argument.tex).

<a id="input-nb-gain"></a>
### NB-GAIN: Lower-bound actual residual gain along a cofinal sequence

For a fixed smoothing order and actual optimized residual, prove a nonsummable sequence of relative gains. In q=2, the full block target is Delta_N/E_N, Delta_N=h_N^T H_N^(-1)h_N. NS87 localizes the actual arithmetic observations with complete tails at T=N^6; a positive lower liminf of j A_(2^j)/E_(2^j) is sufficient. This remains unproved.

**Scope / stop:** Related selected-direction bounds are sufficient routes to this objective, not the same scalar cost. NS71 needs its model-inverted numerator and true-energy ratio; NS72 needs actual curvature and selected cost; NS95/96 use a restricted N-to-N² span and complementary gain. NS53/59 use the unsmoothed analogue, so their formulas are not identified with q=2. NS80–82 guarantee a fraction of available gain, not a fraction of total error. NS83 excludes eventual fixed-fraction whole-error contraction, not all nonsummable slower gains.

Sources: [evidence/ns87_joint_tail/argument.tex](evidence/ns87_joint_tail/argument.tex) · [evidence/v160/ns71/proof.tex](evidence/v160/ns71/proof.tex) · [evidence/ns95_square_product/argument.tex](evidence/ns95_square_product/argument.tex) · [evidence/ns96_lcm_square/argument.tex](evidence/ns96_lcm_square/argument.tex).

<a id="input-nb-samples"></a>
### NB-SAMPLES: Make a complete signed arithmetic upper-error sum tend to zero

Construct integer approximants whose complete reciprocal-sample or zero-exterior error tends to zero. NS78 compares the complete sample sum with the full physical norm; NS89 preserves every decay rate under its optimal normalization. Neither result bounds the arithmetic sum cofinally.

**Scope / stop:** This is an upper-error route to the same convergence objective, not the MOBIUS-COST scalar or a new lower-gain identity. A fixed-template failure does not exclude freely chosen coefficients; coefficientwise convergence is not norm convergence.

Sources: [evidence/v163/ns78](evidence/v163/ns78) · [evidence/ns89_upper_normalization](evidence/ns89_upper_normalization).

<a id="input-nb-growth"></a>
### NB-GROWTH: Control internal canonical arithmetic cancellation at fixed smoothing

Prove subpolynomial growth of the canonical smoothed norm, or separately establish a useful bounded cofinal subsequence with its required implication. NS66 identifies the power-growth exponent; NS67 supplies complete cells and tail; NS68 transfers the forcing power through the positive renewal operator.

**Scope / stop:** Different object from the optimized projected cost. Strong full-sequence convergence is already excluded; weaker growth targets are not. Cancellation merely between the two complete centered Abel terms cannot change the exponent. Renewal positivity cannot manufacture the missing forcing estimate.

Sources: [evidence/v159](evidence/v159) · [evidence/v160/ns67](evidence/v160/ns67) · [evidence/v160/ns68](evidence/v160/ns68).

<a id="input-nb-dilation"></a>
### NB-DILATION: Prove growth of the cumulative actual dilation defect

Force divergence of the cumulative normalized absolute dilation defect appearing in NS88’s whole-error upper envelope.

**Scope / stop:** A different scalar and sufficient route to convergence; no identity with the fixed Mobius cost. The eventual energy/j^p lower bound for p<1 is excluded; p=1 remains open within the stated constant restriction. Finite sign changes do not settle cumulative growth.

Sources: [evidence/ns88_dilation_defect/argument.tex](evidence/ns88_dilation_defect/argument.tex).

<a id="input-nb-continuous"></a>
### NB-CONTINUOUS: Bridge continuous zero-defect information to the integer problem

Supply a valid additional bridge from the continuous dilation closure to integer approximation, or prove actual zero continuous defect by new arithmetic input.

**Scope / stop:** The continuous closure is strictly larger. Its small certified upper bound is not an upper bound for integer error and is not zero. This does not share the projected-cost estimate.

Sources: [evidence/v162/ns76](evidence/v162/ns76) · [evidence/v162/ns77](evidence/v162/ns77).

<a id="input-weil-floor"></a>
### WEIL-FLOOR: One complete signed lower floor with a common cofinal constant

Prove q_a[f]>=-C||f||² with a common finite C on complete admissible domains: the actual even source complement and the odd sector, with the established source transfer to the full form. All prime, pole, exterior and cross terms must remain.

**Scope / stop:** CAE, unrestricted exact adaptive concentration, critical Clifford domination and coefficient-one localization absorption are versions of this same floor under their stated domains. Their stronger fixed-slack or channel-deletion failures do not refute the floor. This is a second genuine shared-gap family, distinct from the NB selected numerator/cost. RH implications alone do not identify their estimates. NS104 clarification: a common absolute error bound can suffice without resolving each tiny positive eigenvalue. The target does not require a positive spectral gap. A pre-claim Abel-damping screen applies NS47 to the fixed positive multiplier 2 Re(xi'/xi)(1/2+epsilon+it), epsilon>1/2: uniformly bounded undamping cost is excluded for this ordinary-closable unbounded comparison. Shrinking epsilon to zero leaves the justified absolute-convergence domain; no positivity transfer or new arithmetic estimate is supplied. This overlap audit adds no theorem or closure node.

Sources: [evidence/v151](evidence/v151) · [evidence/v152](evidence/v152) · [evidence/ns47_clifford_weil/representation.tex](evidence/ns47_clifford_weil/representation.tex) · [evidence/ns50_cae_localization/localization-v2.tex](evidence/ns50_cae_localization/localization-v2.tex) · [evidence/diag_ns104_ground_mechanism/results.md](evidence/diag_ns104_ground_mechanism/results.md) · [audits/prime-archimedean-screen-2026-09-23-v1/results.md](audits/prime-archimedean-screen-2026-09-23-v1/results.md).

<a id="input-kernel-api"></a>
### KERNEL-API: Exclude full-window arithmetic nullvectors on the complete domain

Establish arithmetic affine-potential injectivity (API), respecting parity, endpoints, all prime shifts and poles. The homogeneous translated-radical boundary test is exactly the null equation, not an independent rigidity estimate.

**Scope / stop:** This is a different unresolved input. Local open-set UCP and ordinary-cone positivity are false for the actual operator; those controls are not full-window nullvectors. No generic Sobolev bootstrap or whole-space compact inverse supplies API.

Sources: [evidence/v154](evidence/v154) · [evidence/v155](evidence/v155) · [evidence/v157](evidence/v157).

<a id="input-ccm-limit"></a>
### CCM-LIMIT: Obtain complete relative ground selection and transform control

Control the complete cutoff residual relative to a complete separator (or the stated Rayleigh-excess/gap variant) cofinally, plus entire-transform evaluator/tightness bounds. Global-ground claims also require the specified odd ordering.

**Scope / stop:** Fixed-window real-zero transforms and proximity to the first zeta zero do not supply convergence to Xi. Absolute residual/resolvent data and a polynomial positive separator do not replace the named relative inputs. Distinct from the NB cost and API. NS104 evaluates the frozen finite trial only; the v1.43 complete-root radius is an energy/evaluator upper bound, not a measured displacement. Later trial zeros are not transferred to the complete ground.

Sources: [evidence/v152](evidence/v152) · [evidence/v140](evidence/v140) · [evidence/v143](evidence/v143) · [evidence/diag_ns104_ground_mechanism/results.md](evidence/diag_ns104_ground_mechanism/results.md).

<a id="input-level-packets"></a>
### LEVEL-PACKETS: Supply arithmetic level mass and independent admissible packet coverage

Verify the relevant ZLD/QG level-distribution hypothesis and separate bounded-energy source-admissible packet coverage needed for the stated minorant-complexity implication.

**Scope / stop:** These hypotheses concern an obstruction to bounded minorant complexity, not a proof of the signed Weil floor. ZLD implies only the stated QG growth clause; packet feasibility does not follow. Do not merge this gap with WEIL-FLOOR.

Sources: [evidence/v146](evidence/v146) · [evidence/v147](evidence/v147) · [evidence/v149](evidence/v149) · [evidence/v151](evidence/v151) · [audits/ns54-zero-picture-review-2026-09-22-v1.html](audits/ns54-zero-picture-review-2026-09-22-v1.html).

<a id="input-zero-geometry"></a>
### ZERO-GEOMETRY: Find zeta-specific zero rigidity beyond reflection symmetry

A geometric revival must add a property of the actual xi/theta/Euler-product object that symmetric off-line controls do not share. The NS94 power-product detector still requires an all-height vanishing proof.

**Scope / stop:** Equal inversion counts and an infinite exterior similarity point do not imply RH: the point depends on circle parameters. That inference is closed, not every geometric approach. A classical RH-equivalent radial-growth or disk-contraction criterion is not a new arithmetic estimate; any new proposed sufficient mechanism needs its own test and scope. NS100 tests a concrete stronger condition using the actual theta kernel: its p=0 slice cosine transform at frequency 40 is strictly negative, and continuity extends failure to small p>0. This closes only per-slice positivity; the full integrated kernel remains unestimated. Its classical associated-kernel criterion is not a novel mechanism. NS101 stops the proposed completion/factorization attempt without a new estimate. Its reciprocal positive-Gaussian dilation control retains a positive even differential kernel, order one and the usual zero strip but introduces off-axis zeros. It changes the single-lattice coefficients and does not claim monotonicity, log-concavity or all modular laws. The original full-sign question is not closed; reopening needs a specific additional arithmetic identity. NS103 records four finite-grid Davenport-Heilbronn detections and a heuristic bandwidth count, not minimum support sizes, a sharp height cutoff or a universal detection law. NS104 corrects the parameter conversion: manuscript lambda=4 has logarithmic half-width log4. The unchanged archived trial has near-zeros at the first64 zeta ordinates at two precisions, including beyond the heuristic crossover; no new complete-ground root transfer, null-space mechanism or cofinal estimate follows.

Sources: [evidence/ns94_circle_inversion](evidence/ns94_circle_inversion) · [evidence/ns100_reassessment/argument.tex](evidence/ns100_reassessment/argument.tex) · [evidence/ns100_reassessment/proposals.json](evidence/ns100_reassessment/proposals.json) · [evidence/ns100_reassessment/sources.json](evidence/ns100_reassessment/sources.json) · [evidence/ns101_theta_factorization/argument.tex](evidence/ns101_theta_factorization/argument.tex) · [evidence/diag_ns103_window_calibration/results.md](evidence/diag_ns103_window_calibration/results.md) · [evidence/diag_ns104_ground_mechanism/results.md](evidence/diag_ns104_ground_mechanism/results.md).

<a id="input-heat-transport"></a>
### HEAT-TRANSPORT: Control exterior-cluster transport and test-support costs

Bound the external zero-cluster interactions and support dependence that survive symmetry-paired heat transport.

**Scope / stop:** Internal inverse-gap cancellation alone is insufficient. The unmatched-real-zero obstruction is conditional and its hypothesis was not verified. This is not the NB projected-cost question.

Sources: [evidence/v154](evidence/v154).

<a id="input-operator-bridges"></a>
### OPERATOR-BRIDGES: Construct the route-specific operator or geometric transfer

These are separate unfinished constructions, grouped only to mark their independence from NS98: evaluator estimates and closed realization (fixed-space); actual structural/asymptotic transfer (circle/Toeplitz); a valid unshifted-sign/extension bridge (de Branges); number-field intersection construction and positivity transfer (Hodge/F_1).

**Scope / stop:** No equivalence between these missing inputs is asserted. The old circle/Toeplitz measurement lane is not Dad’s tangent-circle zero-count proposal. Shifted finite-window data do not determine an unshifted sign; analogy with function fields does not construct a number-field intersection theory.

Sources: [COMPARISON.md](COMPARISON.md) · [evidence/diag_true_symbol](evidence/diag_true_symbol).

## Nodes

- [ ] **RH** — via Weil positivity
  - [ ] **Alternative mechanisms: distinct missing inputs** — Logical RH equivalence does not establish equal proof difficulty or a universal route closure. NS-51–53 test explicit first lemmas.
    - [X] **Direct rational Li / entire window-test identification** — evidence: [`evidence/diag_routes/li/`](evidence/diag_routes/li/) · **wall: direct rational-Li / entire-window classes intersect only at zero** → `None` (Scoped direct-identification obstruction; no statement excluding indirect Li inequalities) · The specified rational Li-transform class has trivial intersection with the finite-window entire Paley–Wiener class. This closes direct identification only; it does not exclude indirect inequalities or all Li approaches.
    - [~] **Exact kernel exclusion: affine-potential injectivity** — `prop:ns51-affine-potential; eq:ns51-api` · `codex/ns55-arithmetic-kernel` · evidence: [`evidence/ns51_kernel/`](evidence/ns51_kernel/) · **wall: API: actual arithmetic affine-potential injectivity (open)** → `rh` (eq:ns51-api; prop:ns51-sign-continuation) · Complete form-domain reduction is exact in both parities. NS-55 rules out importing local UCP or ordinary-cone semigroup positivity; first-zero nullvectors must reach both endpoints. API remains open, with no signed arithmetic overlap estimate and no required uniform positive gap. · **Continuation [KERNEL-API](#input-kernel-api) (same nullvector input):** The complete-domain or boundary reformulation does not prove arithmetic injectivity.
      - [x] **Finite prime-weight changes: negative tests and first-zero controls** — `cor:ns57-finite-weight-negative; thm:ns57-first-zero-controls; cor:ns57-fixed-direction-sensitivity` · `codex/ns57-prime-weight-rigidity` · evidence: [`evidence/v156/`](evidence/v156/) · NS-57: every nonzero finite coefficient change gives negative compact tests in both parities and finite first-zero windows. Translation/reflection geometry, endpoint saturation and the modified affine-potential equation survive; the original arithmetic radical identity does not. Fixed-pattern lambda_* = O(sqrt(log(1/epsilon))) is an analytic upper bound, not a certified threshold. No negative original Weil direction or API closure.
      - [X] **Generic H¹ bootstrap from a zero eigenvalue** — `prop:ns51-no-generic-bootstrap` · evidence: [`evidence/ns51_kernel/`](evidence/ns51_kernel/) · Rank-one bounded perturbation of the same logarithmic principal operator has a non-H¹ nullvector. This closes only inference from generic structural hypotheses; arithmetic regularity is not refuted. · **Continuation [KERNEL-API](#input-kernel-api) (scoped failed shortcut):** This specific general mechanism is closed; full-window arithmetic injectivity remains open.
      - [X] **Local open-set UCP for the full prime-shift operator** — `prop:ns55-local-ucp-counterexample; prop:ns55-parity-ucp-counterexample` · evidence: [`evidence/v155/`](evidence/v155/) · **wall: local f=A_a f=0 does not force f=0; whole-window API is not refuted** → `None` (prop:ns55-local-ucp-counterexample) · Exact local-patch counterexamples, in each parity for a>log2 and after finitely many linear constraints. They do not solve A_a f=0 on the whole window and give no negative diagonal Weil energy. Prime-shift-free exterior-cell uniqueness remains valid under its explicit support hypothesis. · **Continuation [KERNEL-API](#input-kernel-api) (scoped failed shortcut):** This specific general mechanism is closed; full-window arithmetic injectivity remains open.
      - [X] **Ordinary-cone positivity for the full Weil semigroup** — `prop:ns55-nonpositive-semigroup` · evidence: [`evidence/v155/`](evidence/v155/) · **wall: order-preservation shortcut fails; quadratic-form positivity is a different property** → `None` (prop:ns55-nonpositive-semigroup) · Positive off-diagonal pole-minus-archimedean cross terms for disjoint nonnegative tests show that the full real-space semigroup is not positivity preserving. A bounded positive multiplication conjugation cannot repair the cone property. No separate parity-cone claim, negative q direction, or API closure. · **Continuation [KERNEL-API](#input-kernel-api) (scoped failed shortcut):** This specific general mechanism is closed; full-window arithmetic injectivity remains open.
      - [x] **Translated-radical boundary test: exact kernel equivalence and forced controls** — `prop:ns58-boundary-identity; prop:ns58-equivalence; prop:ns58-forced-pairing` · `codex/ns58-radical-boundary` · evidence: [`evidence/v157/`](evidence/v157/) · NS-58 stop condition: homogeneous vanishing is exactly the original null equation, with no independent sign estimate. Altered weights produce a necessarily nonzero forcing profile; compactness excludes only a uniform lower bound on the whole fixed-window space. API and the uniform floor remain open. · **Continuation [KERNEL-API](#input-kernel-api) (same nullvector input):** The complete-domain or boundary reformulation does not prove arithmetic injectivity.
    - [ ] **Nyman-Beurling-Baez-Duarte** — `prop:ns53-nb-block-gain; eq:ns53-nb-rbc` · evidence: [`evidence/ns53_nb_blocks/`](evidence/ns53_nb_blocks/) · **wall: RBC: corrected arithmetic residual block correlations (open sufficient input)** → `rh` (eq:ns53-nb-rbc; exact convergence criterion is prior art, and RBC is not proved or claimed equivalent to RH) · Any fixed-order NB convergence suffices. NS-61 proves an elementary smoothed difference budget but leaves the actual optimized correlation input open. NS-60/62/63 exclude scoped correction, coefficient and changing-norm shortcuts. Finite gains are not cofinal bounds. · **Continuation [NB-GAIN](#input-nb-gain) (full gain target):** The actual cofinal arithmetic decrease remains open; complete tails and a gain identity do not force it.
      - [x] **Fixed smoothed NB: positive averages and N^(-2) trace** — `prop:ns61-rh-equivalence; prop:ns61-average-budget` · evidence: [`evidence/v159/`](evidence/v159/) · One fixed Mellin integration preserves the RH criterion. Trace <= 3*kappa/(8*N^2), and scaled trace tends to that constant. Every Gram cross term and transformed numerator remains. · **Continuation [NB-GAIN](#input-nb-gain) (supporting result):** The proved finite identity, norm comparison or efficiency statement remains unconditional as stated. Using it to obtain convergence requires new actual-residual arithmetic control.
        - [!] **Actual optimized smoothed residual correlations** — `eq:ns61-open-correlation; eq:ns61-endpoint-correlation; prop:ns69-remainder; prop:ns71-selected-input` · evidence: [`evidence/v160/`](evidence/v160/) · **wall: non-summable lower contraction for the actual optimized residual (open sufficient input)** → `rh` (prop:ns61-gain; no necessity or equivalence claim for this sufficient estimate) · The complete signed endpoint remainder exceeds the leading model at N=64,128. Repaired-kernel directions recover 97.06% of full finite gain at N=256, using the actual complete energy. No cofinal numerator/cost estimate is proved. · **Continuation [NB-GAIN](#input-nb-gain) (full gain target):** The actual cofinal arithmetic decrease remains open; complete tails and a gain identity do not force it.
          - [!] **Repaired-kernel selection measured with true energy** — `prop:ns71-selected-input` · evidence: [`evidence/v160/ns71/`](evidence/v160/ns71/) · **wall: cofinal lower numerator and upper selected cost with nonsummable relative gain** → `rh` (prop:ns71-selected-input; sufficient, not asserted necessary) · Certified finite gain fractions above 97% at N=128,256 for the projected repaired direction. Exact selected numerator/cost criterion avoids the excluded uniform comparison. · **Continuation [NB-GAIN](#input-nb-gain) (different selected direction):** Numerator and true-cost estimates are missing for this direction. It is not NS73 p1 or NS98 K_N.
            - [x] **Complete local energy and discrete curvature** — `prop:ns72-local-energy; prop:ns72-interpolation; prop:ns72-curvature` · evidence: [`evidence/v161/ns72/`](evidence/v161/ns72/) · Uniform model-only curvature comparison and local direction rules. No cofinal actual arithmetic estimate. · **Continuation [NB-GAIN](#input-nb-gain) (supporting result):** The proved finite identity, norm comparison or efficiency statement remains unconditional as stated. Using it to obtain convergence requires new actual-residual arithmetic control.
              - [!] **Cofinal arithmetic curvature and selected cost** — `eq:ns72-local-directions` · evidence: [`evidence/v161/ns72/`](evidence/v161/ns72/) · **wall: actual curvature lower bound and selected true cost giving nonsummable relative contraction** → `rh` (NS-72; finite efficiency is insufficient) · Diagonal curvature retains 97.63% of finite optimal gain at N=256. The prescribed three-template span is weaker on all five blocks. · **Continuation [NB-GAIN](#input-nb-gain) (different selected direction):** Numerator and true-cost estimates are missing for this direction. It is not NS73 p1 or NS98 K_N.
                - [x] **Exact divisor feedback and finite unit-step failure** — `prop:ns75-divisor-cells` · evidence: [`evidence/v162/ns75/`](evidence/v162/ns75/) · Exact local jump cancellation is not descent: every held-old unit step tested increases full error. No asymptotic exclusion of other feedback. · **Continuation [NB-GAIN](#input-nb-gain) (supporting result):** The proved finite identity, norm comparison or efficiency statement remains unconditional as stated. Using it to obtain convergence requires new actual-residual arithmetic control.
                  - [x] **Complete reciprocal-knot norm and exact divisor inversion** — `prop:ns78-sampling; eq:ns78-sample-inverse` · evidence: [`evidence/v163/ns78/`](evidence/v163/ns78/) · S/16 <= squared norm <=21 S/16, all cells and tails retained. No cofinal vanishing sample sum. · **Continuation [NB-SAMPLES](#input-nb-samples) (upper-error route):** The complete signed sum still needs a cofinal upper bound tending to zero; the norm equivalence/normalization alone supplies none.
                    - [x] **Optimized arithmetic potential and complete observation tails** — evidence: [`evidence/ns86_optimized_arithmetic/`](evidence/ns86_optimized_arithmetic/) · NS86: exact joint-cutoff Muntz quadrature represents actual correlations; P_N(1)=E_N. Complete observation-tail bound and shared-tail cancellation are proved. Classical zero-evaluation obstruction remains; no cofinal lower bound or injectivity theorem. · **Continuation [NB-GAIN](#input-nb-gain) (supporting result):** The proved finite identity, norm comparison or efficiency statement remains unconditional as stated. Using it to obtain convergence requires new actual-residual arithmetic control.
                      - [x] **Divisor-convolution correction from N to N squared: finite control** — evidence: [`evidence/ns86_optimized_arithmetic/`](evidence/ns86_optimized_arithmetic/) · NS86: raw defect-convolution square holds through N^2, retaining signed normalization sums and omitted forcing. Unit step raises error at N=4,16 and lowers it at N=8; damped old-space-refitted direction captures 27.31% of available gain at N=16. Modified coefficients generally lose the exact defect-square identity. No eventual failure or general route closure. · **Continuation [NB-GAIN](#input-nb-gain) (restricted square-scale route):** The N-to-N² class retains a restricted span and complementary gain. NS96 positivity after refitting does not bound the actual cofinal numerator.
                      - [x] **Joint finite arithmetic observations preserve logarithmic gain scale** — evidence: [`evidence/ns87_joint_tail/`](evidence/ns87_joint_tail/) · NS87: complete coupled-tail bound and explicit safe step. NS81/83 imply T=N^(5+epsilon) preserves relative gain up to o(1/log N), with no effective onset or arithmetic lower estimate. Finite N=32 to 64, T=4096 certificate retains >95.98% of available gain. Full Gram/inverse retained; no fast solver or cofinal decay. · **Continuation [NB-GAIN](#input-nb-gain) (full gain target):** The actual cofinal arithmetic decrease remains open; complete tails and a gain identity do not force it.
                        - [x] **Exact Mobius cancellation; fixed-size absolute-bound loss** — evidence: [`evidence/ns90_mobius_gain/`](evidence/ns90_mobius_gain/) · NS90 exact identity cancels the prime main terms. Under a nonzero residual logarithmic or constant tail, the termwise absolute divisor allowance diverges as cutoff grows at fixed N; no uniform-in-N conclusion at T=N^6. At N16,256 the certified triangle lower bound is vacuous despite positive full numerators. The direction and full joint arithmetic lower-gain target remain open; inherited NS73 efficiencies are not new results. · **Continuation [MOBIUS-COST](#input-mobius-cost) (same selected cost):** The old-space endpoint correction leaves K_N unchanged. NS98 retains the same unestimated signed projected cross term. · **Continuation [MOBIUS-MARGIN](#input-mobius-margin) (companion sufficient input):** A compatible lower signed numerator is still required, even if a cost bound is obtained. No cofinal margin follows from a finite positive gain.
                          - [x] **Joint first-primitive finite lower bound with complete grouped tail** — evidence: [`evidence/ns91_joint_abel/`](evidence/ns91_joint_abel/) · NS91: exact old-space correction removes 0<t<N without changing gain or true projected cost. Complete absolute dyadic-tail bound is negligible at T=N^6; finite N256 gain >0.02821 certifies the known NS73 direction, not a new best error. No uniform interior margin/cost estimate. The NS78 divisor-inversion quadratic rewrite reduces to the same numerator under normal equations; no independent positivity or route closure. · **Continuation [MOBIUS-COST](#input-mobius-cost) (same selected cost):** The old-space endpoint correction leaves K_N unchanged. NS98 retains the same unestimated signed projected cross term. · **Continuation [MOBIUS-MARGIN](#input-mobius-margin) (companion sufficient input):** A compatible lower signed numerator is still required, even if a cost bound is obtained. No cofinal margin follows from a finite positive gain.
                            - [x] **Complete scalar cost budget and a feasible endpoint-only update** — evidence: [`evidence/ns92_arithmetic_cost/`](evidence/ns92_arithmetic_cost/) · NS92 applies the prior NS61 complete average to signed Mobius tails. A finite scalar upper bounds the full projected cost and an endpoint-only direction without a new-block inverse. At N256 a 1/16 step has complete physical gain >1.57%; the cheaper scalar budget certifies >0.0443% for step 1/512. No new best error. Seven scalar budgets through N65536 are finite checks only; uniform arithmetic cost and numerator estimates remain open. · **Continuation [MOBIUS-COST](#input-mobius-cost) (stronger sufficient budget):** Its signed suffix budget bounds K_N; failure to bound this larger budget would not refute bounded projected cost. · **Continuation [MOBIUS-MARGIN](#input-mobius-margin) (companion sufficient input):** A compatible lower signed numerator is still required, even if a cost bound is obtained. No cofinal margin follows from a finite positive gain.
                              - [X] **Averaging the fully separated absolute Mobius cost** — evidence: [`evidence/ns93_averaged_cost/`](evidence/ns93_averaged_cost/) · **wall: productwise absolute values force a linear majorant even before averaging** → `None` (evidence/ns93_averaged_cost/argument.tex; scoped to this sufficient cost bound) · NS93: signed suffix cost has diagonal <=(log 2)^2/4; its fully absolute product majorant is >=N log(4/3)^2/9216 for dyadic N>=2048. Its growing-block mean diverges. Actual signed cost, averaged numerator and full PR42 route remain open; finite means not extrapolated. · **Continuation [MOBIUS-COST](#input-mobius-cost) (excluded majorant only):** The fully absolute bound is closed. Actual projected K_N and signed suffix means remain open; this continuation does not reopen that majorant. · **Continuation [MOBIUS-MARGIN](#input-mobius-margin) (companion sufficient input):** A compatible lower signed numerator is still required, even if a cost bound is obtained. No cofinal margin follows from a finite positive gain.
                        - [x] **Square-scale product restriction and complete gain split** — evidence: [`evidence/ns95_square_product/`](evidence/ns95_square_product/) · NS95: free signed divisor-product weights force b_(mp) independent of prime p>N for mp<=N^2. Exact complementary gain retained; an invisible arithmetic vector refutes the all-residual comparison under the stated prime-pair hypothesis, not the actual-target bound. Free lift captures 99.83% of finite N16-to-256 gain versus 27.31% for NS86, with complete costs and tails. Product-pairing matrix indefinite on tested blocks. Reweighting generally loses the defect-square prescription; no cofinal lower estimate or new best error. · **Continuation [NB-GAIN](#input-nb-gain) (restricted square-scale route):** The N-to-N² class retains a restricted span and complementary gain. NS96 positivity after refitting does not bound the actual cofinal numerator.
                          - [x] **LCM divisor squares: complete-rule floors and signed refit equivalence** — evidence: [`evidence/ns96_lcm_square/`](evidence/ns96_lcm_square/) · NS96: for the entire coefficient sequence c=-q grouped from any PSD matrix, E>=3087/4096 uniformly in size; c=+q gives E>1/32. Complete real Mellin exterior retained. After unrestricted old refitting, the projected PSD cone equals the signed LCM span; a nonzero old-orthogonal residual pairing matrix is indefinite. No floor for unrestricted/refitted error, actual cofinal gain bound, or general sieve no-go. Single rank-one squares and extra trace/diagonal constraints are outside the cone equality. NS97 audit: this does not advance the earlier arithmetic lower-gain input; positive-rule qualitative failure already follows from NS78. Trace normalization leaves the same rays when step scale is free. The Mellin separator and floor function already appear in NS74 under different hypotheses. · **Continuation [NB-GAIN](#input-nb-gain) (restricted square-scale route):** The N-to-N² class retains a restricted span and complementary gain. NS96 positivity after refitting does not bound the actual cofinal numerator.
                      - [x] **Multiplicative normal equations and a scalar whole-error upper envelope** — evidence: [`evidence/ns88_dilation_defect/`](evidence/ns88_dilation_defect/) · NS88: dilation defect equals the overlap of successive orthogonal increments. Complete next-size upper certificate and E_(2^(J+1))<=K exp(-sqrt(2) S_J). Lower growth or even divergence of S_J remains unproved; finite envelope is weaker than optimized finite errors. No RH decay or necessity claim. · **Continuation [NB-DILATION](#input-nb-dilation) (different sufficient scalar):** Only the specified stronger pointwise demand is excluded; cumulative normalized absolute-defect growth is unestimated.
                        - [X] **Eventual energy/j^p dilation-defect lower bound with p<1** — evidence: [`evidence/ns88_dilation_defect/`](evidence/ns88_dilation_defect/) · **wall: The proposed stronger numerator forces error decay contradicting the critical-zero lower bound** → `None` (evidence/ns88_dilation_defect/argument.tex; scoped to the displayed dilated optimized approximant) · NS88: exact increment inequality plus NS83 excludes eventual abs(d_(2^j))/E_(2^j)>=a/j^p for a>0, 0<=p<1; at p=1 excludes a>1/sqrt(2). No pointwise upper bound on every defect; smaller p=1 constants and other constructions remain open. · **Continuation [NB-DILATION](#input-nb-dilation) (different sufficient scalar):** Only the specified stronger pointwise demand is excluded; cumulative normalized absolute-defect growth is unestimated.
                    - [x] **Tail-balanced divisor feedback control** — `prop:ns79-balance` · evidence: [`evidence/v163/ns79/`](evidence/v163/ns79/) · Preserves exterior coefficient but leaves final jump. Endpoint-augmented span captures 71.18% at N=256; no uniform raw descent. · **Continuation [NB-GAIN](#input-nb-gain) (supporting result):** The proved finite identity, norm comparison or efficiency statement remains unconditional as stated. Using it to obtain convergence requires new actual-residual arithmetic control.
                    - [x] **Uniform efficiency using the full arithmetic sampling Gram** — `prop:ns80-uniform-efficiency` · evidence: [`evidence/v163/ns80/`](evidence/v163/ns80/) · Projected condition ratio <=21, one-step capture >=21/121, twenty-step capture >97.79%. Complete comparator inverse assumed; no fast inverse or cofinal relative contraction. · **Continuation [NB-GAIN](#input-nb-gain) (supporting result):** The proved finite identity, norm comparison or efficiency statement remains unconditional as stated. Using it to obtain convergence requires new actual-residual arithmetic control.
                      - [x] **Polynomial ordinary Gram conditioning and an effective finite comparator** — `prop:ns81-conditioning; prop:ns81-finite-comparator` · evidence: [`evidence/v164/ns81/`](evidence/v164/ns81/) · Condition O(N^4 log² N); sufficient cutoff 2^16(N+1)^6 with full tail bound. Enormous comparator not assembled; no practical solver or cofinal decay. · **Continuation [NB-GAIN](#input-nb-gain) (supporting result):** The proved finite identity, norm comparison or efficiency statement remains unconditional as stated. Using it to obtain convergence requires new actual-residual arithmetic control.
                        - [x] **Finite physical comparator with an exact rank-two tail** — `prop:ns82-tail-compression` · evidence: [`evidence/v165/ns82/`](evidence/v165/ns82/) · Sufficient cutoff O(N^(7/3) log^(1/3)(2N)); projected condition <=9. Scalar constants certified; comparator not assembled; no cofinal decay. · **Continuation [NB-GAIN](#input-nb-gain) (supporting result):** The proved finite identity, norm comparison or efficiency statement remains unconditional as stated. Using it to obtain convergence requires new actual-residual arithmetic control.
              - [X] **Infer convergence from shared Gram geometry and finite efficiency** — `prop:ns74-same-gram; cor:ns74-finite-indistinguishability` · evidence: [`evidence/v161/ns74/`](evidence/v161/ns74/) · **wall: explicit inserted inner-factor control; scope is this finite-statistics inference** → `None` (cor:ns74-finite-indistinguishability) · A unitary altered family preserves every Gram entry and has arbitrarily close finite statistics but a positive floor. No original-family error floor.
                - [x] **Exact continuous inner-factor defect and strict closure separation** — `prop:ns76-continuous-distance; prop:ns76-strict-closure` · evidence: [`evidence/v162/ns76/`](evidence/v162/ns76/) · Continuous defect depends on B(1), B′(1), B″(1). Integer closure strictly smaller; target distances not proved different. · **Continuation [NB-CONTINUOUS](#input-nb-continuous) (relaxation bridge):** Continuous defect bounds cannot be promoted to integer-error upper bounds without an additional argument.
                  - [x] **Complete continuous zero-tail budget** — `prop:ns77-tail-budget` · evidence: [`evidence/v162/ns77/`](evidence/v162/ns77/) · Published finite-height information implies continuous squared distance <2.08e-32; not an integer upper bound or zero-distance proof. · **Continuation [NB-CONTINUOUS](#input-nb-continuous) (relaxation bridge):** Continuous defect bounds cannot be promoted to integer-error upper bounds without an additional argument.
          - [X] **Uniform comparison with the repaired elementary Gram** — `prop:ns70-cusp; prop:ns70-repaired-background` · evidence: [`evidence/v160/ns70/`](evidence/v160/ns70/) · **wall: pointwise Mellin-density comparison forced by all-coefficient localization** → `None` (prop:ns70-repaired-background) · Subtracting d/max repairs the adjacent n^-2 cusp to n^-3. Uniform lower and upper all-coefficient comparisons still fail, respectively by critical zeros and unbounded zeta values. Selected directions remain outside the exclusion.
        - [!] **Canonical smoothed norm: subpolynomial growth** — `prop:ns66-growth-bounds; cor:ns66-growth-exponent; prop:ns67-polynomial-cutoff; prop:ns67-abel-conditioning` · evidence: [`evidence/v160/`](evidence/v160/) · **wall: direct subpolynomial canonical norm bound, or a bounded cofinal subsequence (open)** → `rh` (cor:ns66-growth-exponent) · Fixed-order exponent equals beta_star-1/2 by local zero evaluation and conditional Bochner-Abel bounds. Exact reformulation, with no improved arithmetic estimate. A bounded cofinal subsequence is sufficient but not asserted necessary. Exact cells through N^2 retain the exponent; centered whole Abel vectors have a uniform conditioning bound, so internal arithmetic remains the target. · **Continuation [NB-GROWTH](#input-nb-growth) (canonical target):** The missing bound acts inside the actual signed canonical response or forcing, not on the optimized Mobius direction.
          - [x] **Complete canonical divisor cells and full tail** — `prop:ns67-cells; lem:ns67-remainder; prop:ns67-polynomial-cutoff` · evidence: [`evidence/v160/ns67/`](evidence/v160/ns67/) · Exact signed cells and a full Stirling remainder <=1/(6z). Tail norm beyond N^2 is O(log N), so the growing finite norm has the same RH-equivalent exponent; no subpolynomial estimate. · **Continuation [NB-GROWTH](#input-nb-growth) (support or scoped exclusion):** The stated exact cells/conditioning or excluded stronger target does not establish or refute subpolynomial canonical growth.
          - [!] **Positive renewal with signed arithmetic forcing** — `prop:ns68-weighted-inversion; prop:ns68-scalar-criterion` · evidence: [`evidence/v160/ns68/`](evidence/v160/ns68/) · **wall: independent square-root-plus-epsilon bound for the signed forcing** → `rh` (prop:ns68-scalar-criterion; equivalence is not a new estimate) · Positive weighted inverse exists with q_theta<1; it transfers the same power. The integer first-annulus square-root-plus-epsilon bound remains RH-equivalent. · **Continuation [NB-GROWTH](#input-nb-growth) (canonical target):** The missing bound acts inside the actual signed canonical response or forcing, not on the optimized Mobius direction.
            - [X] **Finite total critical renewal energy** — `cor:ns68-critical-energy` · evidence: [`evidence/v160/ns68/`](evidence/v160/ns68/) · **wall: critical-line Mellin pole contradicts finite weighted L2 energy** → `None` (cor:ns68-critical-energy; scope is these total integrals) · Both critical weighted total integrals diverge by any known critical-line zero. Logarithmic or subpolynomial growth remains possible; this does not assert divergence of D_N. · **Continuation [NB-GROWTH](#input-nb-growth) (support or scoped exclusion):** The stated exact cells/conditioning or excluded stronger target does not establish or refute subpolynomial canonical growth.
          - [X] **Power gain solely between the two complete Abel vectors** — `prop:ns67-abel-conditioning` · evidence: [`evidence/v160/ns67/`](evidence/v160/ns67/) · **wall: uniform conditioning excludes an exponent improvement in this whole-vector split** → `None` (prop:ns67-abel-conditioning; no obstruction to internal arithmetic cancellation) · After explicit centering, their triangle norm is between D_N and (1+2||sigma_1||)D_N. Cancellation inside the integral and exact cells is still unestimated. · **Continuation [NB-GROWTH](#input-nb-growth) (support or scoped exclusion):** The stated exact cells/conditioning or excluded stronger target does not establish or refute subpolynomial canonical growth.
        - [x] **Constructive zero-exterior upper certificates preserve every decay rate** — evidence: [`evidence/ns89_upper_normalization/`](evidence/ns89_upper_normalization/) · NS89: exact constrained optimum E_N^0=E_N+eta_N^2/q_N and E_N<=E_N^0<=1.144579 E_N for every N>=256. Explicit rational size-256 trial has complete squared error <0.000014144. Both errors may remain positive; no cofinal decay theorem or improved best finite bound. Remote physical tail is retained. · **Continuation [NB-SAMPLES](#input-nb-samples) (upper-error route):** The complete signed sum still needs a cofinal upper bound tending to zero; the norm equivalence/normalization alone supplies none.
        - [x] **Critical-zero logarithmic lower bound at every fixed smoothing order** — `prop:ns83-log-floor` · evidence: [`evidence/v166/ns83/`](evidence/v166/ns83/) · Burnol construction adapted with complete endpoint and tail control. Positive lower liminf; no upper bound or finite onset. · **Continuation [NB-GAIN](#input-nb-gain) (rate restriction):** Eventual fixed-fraction whole-error contraction is excluded; slower nonsummable descent and available-gain capture are not.
          - [X] **Fixed-fraction contraction of the full error at every doubling** — `eq:ns83-gain-budget` · evidence: [`evidence/v166/ns83/`](evidence/v166/ns83/) · Cumulative relative gains <=log K+O(1). Individual gains may fluctuate; capture of available block gain is not excluded. · **Continuation [NB-GAIN](#input-nb-gain) (rate restriction):** Eventual fixed-fraction whole-error contraction is excluded; slower nonsummable descent and available-gain capture are not.
        - [X] **Relative convergence with increasing Mellin smoothing** — `prop:ns63-one-atom` · evidence: [`evidence/v159/`](evidence/v159/) · **wall: one-atom unconditional control refutes this convergence inference** → `None` (prop:ns63-one-atom) · One fixed atom has relative squared error ~D0^2/(8r) unconditionally, while its absolute squared error diverges. The fixed-order criterion remains valid; changing the norm is not RH evidence.
        - [X] **Strong convergence of the smoothed canonical sharp Mobius sequence** — `prop:ns62-smoothed-obstruction; prop:ns62-positive-cone; prop:ns64-cone-distance; prop:ns65-cesaro-obstruction` · evidence: [`evidence/v159/`](evidence/v159/) · **wall: a surviving weighted-Mertens witness for this coefficient rule** → `None` (prop:ns62-smoothed-obstruction; not a general NB obstruction) · Localized Laguerre witness preserves nonconvergence for the full integer sequence even if the number of integrations varies. Selected subsequences and optimal coefficients are outside the theorem. The nonnegative difference cone fails locally at its forced sixth coefficient -1/5. An explicit dual separator certifies full-space cone distance >0.00228323, with local equality only. Fixed ordinary Cesaro iterates also fail; weaker norm-growth targets remain open. · **Continuation [NB-GROWTH](#input-nb-growth) (support or scoped exclusion):** The stated exact cells/conditioning or excluded stronger target does not establish or refute subpolynomial canonical growth.
      - [x] **NB adjacent-difference norm budget** — `prop:v158-adjacent-budget; prop:v158-mellin-budget` · evidence: [`evidence/v158/`](evidence/v158/) · Complete basis change transforms both Gram and correlations. Raw Gram norm O_epsilon(N^(-5/3+epsilon)); no lower correlation estimate. Near-N^(-2) power control of the raw all-coefficient norm is equivalent to Lindelof, not a proved estimate. · **Continuation [NB-GAIN](#input-nb-gain) (unsmoothed analogue):** Its arithmetic correlation input has the same kind of role at a different smoothing order; no equality with q=2 quantities is asserted.
      - [X] **NB uniform logarithmic raw norm** — `prop:v158-lindelof-budget` · evidence: [`evidence/v158/`](evidence/v158/) · **wall: known zeta large values contradict every fixed logarithmic N^(-2) raw norm bound** → `None` (prop:v158-lindelof-budget; closure of this all-coefficient raw comparison only) · For every fixed B, the raw difference Gram is not O((log N)^B/N^2), even on dyadic blocks. Projected Grams and the actual residual direction are outside this obstruction.
      - [X] **Uniform logarithmic norm after explicit Euler-grid correction** — `prop:ns60-growing-euler-obstruction` · evidence: [`evidence/v159/`](evidence/v159/) · **wall: zeta large values exceed the allowed finite Euler-product loss** → `None` (prop:ns60-growing-euler-obstruction) · Only this explicit all-coefficient correction with Q_N <= N^alpha, fixed alpha < 1. Complete grid defect and cross terms retained; optimal projection and actual-residual estimates remain open.
    - [X] **Tangent-circle similarity point and count imbalance infer RH** — evidence: [`evidence/ns94_circle_inversion/`](evidence/ns94_circle_inversion/) · **wall: exact symmetric off-line control preserves the proposed geometric count and infinity features** → `None` (evidence/ns94_circle_inversion/argument.tex; geometry and symmetry alone, not zeta arithmetic) · NS94: exact separate/successive inversion formulas. Similarity point depends only on circle parameters; a symmetric off-line polynomial has equal interior counts and infinite exterior similarity point. No actual zeta counterexample or general geometric closure. Nonnegative power-product defect detects displacement, but its all-height vanishing remains an RH-equivalent unproved target. · **Continuation [ZERO-GEOMETRY](#input-zero-geometry) (closed count inference; separate continuation):** Revisit geometry only with an actual zeta-specific rigidity input, not a different inversion parameter.
    - [ ] **circle / Toeplitz-Hankel lens** — `lane/circle-toeplitz` · evidence: [`evidence/diag_true_symbol/`](evidence/diag_true_symbol/) · measurement lane; closure claims withdrawn after NS-31; geometry and exact identities retained · **Continuation [OPERATOR-BRIDGES](#input-operator-bridges) (distinct route-specific construction):** Read the route-specific demand; this tag is an inventory grouping, not an equivalence between its members or with NS98.
    - [ ] **de Branges / Hermite-Biehler** — **wall: screw-kernel positivity = RH; no fixed-window bridge** → `rh` (Suzuki Thm 1.5 (arXiv 2606.09096); the shifted finite-window construction sits strictly below the spectral bottom and does not determine its sign; fixed-window determinacy equivalence not proved) · Shifted fixed-window structures do not determine the unshifted sign; arbitrary extension uniqueness is not established. NS-51 gives a complete-domain nullvector reduction; arithmetic injectivity remains open. · **Continuation [OPERATOR-BRIDGES](#input-operator-bridges) (distinct route-specific construction):** Read the route-specific demand; this tag is an inventory grouping, not an equivalence between its members or with NS98.
    - [ ] **de Bruijn–Newman: paired transport** — `prop:ns52-cluster; prop:ns52-unmatched` · evidence: [`evidence/ns52_heat_pairs/`](evidence/ns52_heat_pairs/) · **wall: complete signed transport with uniform support control (open)** → `rh` (prop:ns52-cluster; prop:ns52-unmatched gives only a conditional obstruction to one same-test comparison) · Finite-cluster singularities cancel; external interaction and support growth remain. Same-test uniform comparison fails IF an unmatched real deformed zero exists; that hypothesis is not verified here. General heat route open. · **Continuation [HEAT-TRANSPORT](#input-heat-transport) (different arithmetic input):** Pairing cancels internal singularities but leaves exterior interactions and support dependence.
    - [ ] **function field / Hodge / F_1** — **wall: no intersection form supplied for this window (missing construction)** → `None` (RESEARCH_MAP note supplied no number-field intersection form, transfer map, or impossibility proof; function-field RH is a theorem for different objects) · No number-field intersection form and quantified positivity transfer are supplied here. A missing construction is not an impossibility theorem. · **Continuation [OPERATOR-BRIDGES](#input-operator-bridges) (distinct route-specific construction):** Read the route-specific demand; this tag is an inventory grouping, not an equivalence between its members or with NS98.
  - [ ] **Fixed-space / Burnol Sonine route** — `lane/fixed-space` · needs evaluator estimates + closed-operator realization · **Continuation [OPERATOR-BRIDGES](#input-operator-bridges) (distinct route-specific construction):** Read the route-specific demand; this tag is an inventory grouping, not an equivalence between its members or with NS98.
  - [x] **G1 (weak)** — `thm:v14-radical` · `lane/g1` · evidence: [`evidence/v124/g2_source_certificate/`](evidence/v124/g2_source_certificate/) · closed for the repaired prolate source
  - [ ] **G2: cofinal -o(1)** — `prop:v121-cofinal-rh` · eps_lambda -> 0 cofinally IS RH
    - [x] **Fixed-window certificates** — `lane/window-scaling` · no finite list is cofinal
      - [x] **CCM finite-compression semantic lock, lambda=3 N=120** — `lem:v141-centering; prop:v141-ccm-lock` · evidence: [`evidence/v141/`](evidence/v141/) · Eight local root discrepancies reproduce CCM Figure 1 with 768/1024-bit interval gates. The zero benchmark cannot detect a common positive scale or identity shift. No new window, complete-ground transfer or cofinal statement. · **Continuation [CCM-LIMIT](#input-ccm-limit) (fixed-window support):** The certified finite-window statement does not establish any cofinal ground-to-Xi limit.
      - [x] **W_4 >= 0 both sectors** — `prop:v126-full-window` · evidence: [`evidence/v126/`](evidence/v126/) · largest completely certified positive window in this record; lambda=3 is also certified; restored evidence does not supply a cofinal theorem
        - [x] **W_4 >= 0  <=>  CCM mu_lambda >= 0 for all lambda <= 4** — CCM arXiv:2511.22755 Cor 3.7-3.8 write 'we cannot assert mu_lambda >= 0'; monotone in lambda; positioning statement
        - [x] **complete W_4: simple even ground; real-zero transform** — `prop:v140-ground4; cor:v140-real-zeros` · `result/ns5-ground-state` · evidence: [`evidence/v140/`](evidence/v140/) · NS-5 complete: mu0<2.454e-75, mu1>1e-73, 1024/1280-bit shifted inertia; CvS Thm6.1 applies; no Xi convergence or G2 claim · **Continuation [CCM-LIMIT](#input-ccm-limit) (fixed-window support):** The certified finite-window statement does not establish any cofinal ground-to-Xi limit.
          - [~] **CCM step (b): finite-compression zeros track zeta zeros (numerical)** — evidence: [`evidence/diag_ns2_semantic_lock/`](evidence/diag_ns2_semantic_lock/) · The 170-value CCM reproduction is a midpoint diagnostic, not a bound. Eight lambda=3, N=120 local roots are certified separately in v1.41. Original sinc-lattice inference withdrawn: missing centering phase in zeros.py. v1.42 separately encloses one complete lambda=4 zero within 0.1 of gamma_1. High-accuracy discrepancy transfer and cofinal Xi convergence remain open. v1.43 certifies a complete first-positive-zero radius 8.752082e-33 and quantifies the archived bound resolution; no complete discrepancy sign or 1e-71 magnitude. NS-43 supplies precise complete relative-selection and entire-transform criteria; none is proved cofinally. Absolute residuals and ordinary resolvent collapse alone do not select the Gaussian, as an explicitly nonarithmetic countermodel shows. · **Continuation [CCM-LIMIT](#input-ccm-limit) (same convergence continuation):** Complete relative selection and transform control are both still required.
            - [X] **Absolute residual/resolvent data alone select ground: abstract inference** — `prop:ns43-ccm-nonselection` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: abstract inference false: countermodel family with alternating profiles** → `None` (prop:ns43-ccm-nonselection) · Exact abstract family has simple even nonnegative real-zero grounds, arbitrarily fast residual decay, resolvent collapse and tight support, yet alternating profiles. It is not an arithmetic support-consistent Weil family; CCM itself remains open.
            - [!] **Complete relative selection and entire-transform control** — `prop:ns43-ccm-rayleigh-selection; prop:ns43-ccm-residual-selection` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: complete relative selection plus entire-transform control (both open)** → `g2` (prop:ns43-ccm-rayleigh-selection: missing cofinal complete separator relative to the cutoff residual) · Missing cofinal complete separator relative to the explicit cutoff residual, or Rayleigh-excess/gap plus evaluator/weighted-tightness control. Global-ground use additionally needs odd ordering. No fixed-head replacement or polynomial positive separator. · **Continuation [CCM-LIMIT](#input-ccm-limit) (same convergence continuation):** Complete relative selection and transform control are both still required.
            - [X] **Single profile from the specified coarse rescaled liminf** — `prop:ns43-ccm-coarse-profile` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: under the explicit coarse scale the limit form is zero; finer scales open** → `None` (prop:ns43-ccm-coarse-profile) · Under the explicit scale, full both-parity liminf, nonnegativity and lower-semicontinuity hypotheses, density of translated radicals forces the limit form to zero. Finer scales and other selection mechanisms remain open.
          - [x] **complete ground zero within 0.1 of gamma_1** — `lem:v142-energy-projection; prop:v142-ground-zero` · `codex/complete-ground-zero-transfer` · evidence: [`evidence/v142/`](evidence/v142/) · 1024/1280-bit complete even separator 1e-67 plus energy projection; unique simple local zero, no earlier-zero ordering, discrepancy sign or cofinal claim. · **Continuation [CCM-LIMIT](#input-ccm-limit) (fixed-window support):** The certified finite-window statement does not establish any cofinal ground-to-Xi limit.
            - [x] **first complete zero within 9e-33; archived resolution quantified** — `prop:v143-first-zero-bound; prop:v143-resolution; prop:v143-fixed-window-meaning` · `codex/complete-ground-zero-transfer` · evidence: [`evidence/v143/`](evidence/v143/) · NS-19: 1024/1280-bit evaluator bound and earlier-zero exclusion. A lower-energy transfer at 1e-71 needs rho-l about 3.2032e-153 plus a suitable trial center. No complete sign, universal resolution no-go or cofinal claim. · **Continuation [CCM-LIMIT](#input-ccm-limit) (fixed-window support):** The certified finite-window statement does not establish any cofinal ground-to-Xi limit.
      - [x] **lambda=3** — `prop:v116-window-positive` · evidence: [`evidence/v124/g2_certificate/`](evidence/v124/g2_certificate/)
      - [x] **lambda=4 even** — `prop:v125-even-complete` · `result/v125-even-complete` · evidence: [`evidence/v126/`](evidence/v126/)
      - [x] **lambda=4 odd** — `prop:v126-odd-complement` · `result/v126-odd-complement` · evidence: [`evidence/v126/`](evidence/v126/)
      - [X] **lambda=5: stipulated 10^-8 D tail comparison** — `prop:v152-tail-comparison` · evidence: [`evidence/ns44_metric_replay/`](evidence/ns44_metric_replay/) · **wall: stipulated 1e-8 D tail comparison fails: positive q/D < 7e-18 (lambda=5)** → `None` (prop:v152-tail-comparison; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · NS-44 fresh exact dyadic witnesses, Arb 320/448: positive q/D <7e-18 even and <12e-18 odd, contradicting the stipulated 1e-8 comparison. Failure of this comparison, not negative Weil directions or complete lambda=5 positivity. Historical v1.27 originals remain unarchived.
    - [x] **Target weakening** — `lane/bounded-floor` · **Continuation [WEIL-FLOOR](#input-weil-floor) (supporting implication):** The equivalence/transfer is proved as stated; existence of the common cofinal bound is not.
      - [x] **no uniform positive gap exists** — `prop:v135-growing-radical` · evidence: [`evidence/v135/`](evidence/v135/) · growing radical family prevents a uniform positive complement gap; the later density/floor argument gives a distinct sufficient criterion without such a gap
        - [X] **Uniform or polynomial positive gap after o(lambda²/log lambda) removed directions** — `lem:ns46-finite-arc; ns46-a2-cor-large-block; ns46-a2-cor-rank` · evidence: [`evidence/v153/`](evidence/v153/) · **wall: positive-gap strategy must remove rank >= lambda^2/(20000 log lambda)** → `None` (lem:ns46-finite-arc; ns46-a2-cor-rank) · NS-46: fixed-range fine translates give complete near-zero rank asymptotic to lambda²/(20000 log lambda), exact even/odd counts and residual C exp(-lambda²/2000). Ill-conditioned finite Grams are bounded explicitly. The positive gap is at most this residual, so only uniform or polynomial positive coercivity is excluded; a smaller positive gap remains possible; no signed floor, negative Weil direction, finite starting-window certificate or closure of gap-free block methods.
      - [x] **uniform finite floor suffices** — `prop:v136-bounded-floor` · evidence: [`evidence/v136/`](evidence/v136/) · decay not required; dichotomy inf spec -> -inf or RH · **Continuation [WEIL-FLOOR](#input-weil-floor) (supporting implication):** The equivalence/transfer is proved as stated; existence of the common cofinal bound is not.
        - [x] **Bounded perturbations preserve the finite-floor objective** — `lem:ns57-bounded-detection; thm:ns57-bounded-floor-stability` · evidence: [`evidence/v156/`](evidence/v156/) · NS-57: q+B+cI is nonnegative on every compact test iff RH and B+cI>=0, for a fixed bounded self-adjoint B. Under RH the perturbed ground bottom tends to inf sigma(B); otherwise to -infinity. Consequences of v1.36; no new arithmetic lower estimate. Failure of exact positivity under finite coefficient changes does not obstruct a robust bounded-floor method. · **Continuation [WEIL-FLOOR](#input-weil-floor) (supporting implication):** The equivalence/transfer is proved as stated; existence of the common cofinal bound is not.
        - [x] **W_lambda >= -8 I at lambda=5,6,8** — `prop:v138-three-floors` · `result/v138-three-floors` · evidence: [`evidence/v138/`](evidence/v138/) · both parities, full infinite tail, Z=0; margin 0.84 -> 0.10 (odd) as lambda grows; not cofinal
        - [x] **bounded shift keeps the exp cutoff barrier** — `prop:v138-shifted-floor` · evidence: [`evidence/v138/`](evidence/v138/) · N+1 > L exp(M_phi - delta); polynomial cutoff needs delta ~ M_phi
        - [!] **positive arithmetic weight: critical capacity input** — `lem:v150-weight; prop:v150-critical-energy; ass:v150-cae` · `codex/bounded-capacity-weight` · evidence: [`evidence/v150/`](evidence/v150/) · **wall: CAE** → `floor` (ass:v150-cae; CAE is the bounded-floor target in positive-weight coordinates (v1.51)) · NS-34: explicit positive Gaussian arithmetic radical with pole mass 1/sqrt(3); exact full and windowed Picone identities retain exterior edges and both parity poles. Critical Arithmetic Energy comparison (CAE) is the uniform complement-floor target in these coordinates, not an independent positivity theorem. Coefficient-one capacity error remains open. NS-43 extends the loss obstruction to any fixed prime-power channel and moving omitted channels bounded away from the endpoint, with unchanged other signed terms. Full coefficient-one or compensated estimates remain open. · **Continuation [WEIL-FLOOR](#input-weil-floor) (same floor under stated domains):** These continuations retain the complete signed floor. NS47 Clifford contraction and NS50 critical absorption share it; their coordinate change is not a new estimate.
          - [X] **Fixed/sub-endpoint channel deletion with unchanged signed terms** — `prop:ns43-fixed-channel; prop:ns43-moving-channel` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: channel deletion: unbounded comparison error for the Gaussian weight** → `None` (prop:ns43-fixed-channel; prop:ns43-moving-channel) · Exact source-admissible even and odd tests force an unbounded comparison error for the specified Gaussian weight. Covers bounded channel counts and sublinear-in-exp(2a) cutoffs. Endpoint-approaching omissions, compensation, and another weight are not closed.
          - [x] **Restricted bump discrepancy can carry the full zero obstruction** — `prop:ns43-bump-strength` · evidence: [`evidence/v152/`](evidence/v152/) · For an explicit smooth compact probe with transform zeros only on the imaginary axis, a bounded translated prime discrepancy would exclude off-line zeros. The bound is unproved; no converse or weaker-than-RH claim. For arbitrary probes, boundedness permits off-line zeros only at common transform zeros; it does not exclude that masking.
          - [x] **ZLD to QG; CAE is the signed-floor target** — `prop:v151-input-comparison` · `codex/ns38-ns39-integration` · evidence: [`evidence/v151/`](evidence/v151/) · NS-39: exact inverse corrected-zero-field formula for the potential, including finite-window pole mass. ZLD implies QG growth with kappa theta² D/(2K) on the same prescribed family; no packet input supplied. CAE equals the uniform complement floor. General measure countermodels are not arithmetic independence. All three arithmetic inputs remain open; no new positivity conclusion. · **Continuation [WEIL-FLOOR](#input-weil-floor) (supporting implication):** The equivalence/transfer is proved as stated; existence of the common cofinal bound is not.
          - [X] **fixed energy loss for the Gaussian arithmetic weight** — `prop:v150-capacity-slack` · `closed/v150-capacity-slack` · evidence: [`evidence/v150/`](evidence/v150/) · **wall: fixed-slack shortcut: eta >= delta kappa exp(gamma lambda^2) - O(lambda log lambda)** → `None` (prop:v150-capacity-slack; coefficient-one CAE and other weights not closed) · Scoped closure: for this explicit weight, discarding fixed delta>0 of transformed energy, or the prime-2 channel alone, forces eta >= delta*kappa*exp(gamma*lambda^2)-O(lambda log lambda). Exact source-admissible even and odd tests, all cross terms controlled. Does not close coefficient-one capacity, another weight, or the physical Weil form.
    - [ ] **Uniform mechanism for G2**
      - [X] **Cotlar cross terms / atomization** — `closed/cotlar-atomization` · **evidence missing** · **wall: shortcut: cross norm >= 73/(375 pi) cofinally; not all Cotlar arguments** → `None` (v1.34; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · v1.34, cross norm >= 73/(375 pi)
      - [X] **Schatten / Hilbert-Schmidt** — `prop:v132-schatten` · `closed/schatten` · **evidence missing** · **wall: scoped: remainder outside finite Schatten classes; negative-only penalty stays a constant (does not obstruct v136)** → `None` (prop:v132-schatten; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route))
      - [x] **Scoped information-loss obstructions** — `thm:v139-probe-relaxation; thm:v139-protected-orbit` · `result/v139-meta-obstruction` · evidence: [`evidence/v139/`](evidence/v139/) · Full-histogram cap/probe relaxation fails; protected finite-head spectral orientation fails. Does not subsume all ten closures.
      - [X] **basis / sampling dominance** — `prop:v121-complement-cancellation` · `closed/sampling-dominance` · evidence: [`evidence/v124/g2_schur_cancellation/`](evidence/v124/g2_schur_cancellation/) · **wall: estimate counterexample: source-complement vector with tiny q despite O(1) cancellation** → `None` (prop:v121-complement-cancellation; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route))
      - [X] **flat-top smoothing** — `prop:v132-flat-top` · `closed/flat-top` · **evidence missing** · **wall: construction class: form-exact positive smoothing = point mass; signed smoothing not covered** → `None` (prop:v132-flat-top; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route))
      - [X] **lambda=5 N=25: tested dyadic norm comparison** — `prop:v152-block-comparison` · `closed/block-metric` · evidence: [`evidence/ns45_block_replay/`](evidence/ns45_block_replay/) · **wall: fixed-partition comparison fails: Rayleigh 341/250, 2093/1500 > 1 (lambda=5, N=25)** → `None` (prop:v152-block-comparison; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · NS-45 new 320/448-bit dyadic pair certificates on the first three existing blocks give exact rational Rayleigh bounds 341/250 even and 2093/1500 odd >1. Excludes all admissible smaller block metrics and positive row weights for this partition; no full-block inertia or general signed-block no-go. Historical v1.28 originals remain unarchived.
      - [X] **norm contraction** — `prop:v120-norm-counterexample` · `closed/norm-contraction` · evidence: [`evidence/v124/g2_weighted_signed/`](evidence/v124/g2_weighted_signed/) · **wall: specific estimate: violated by a POSITIVE direction, q/D > 2.05 at lambda=4** → `None` (prop:v120-norm-counterexample; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route))
      - [X] **reciprocal-band commutation** — `closed/reciprocal-band` · **evidence missing** · **wall: generic mechanism: persistent source-compressed commutator > 9e-6; not every band choice** → `None` (v1.33; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · v1.33, commutator norm > 9e-6
      - [X] **scalar far majorant** — `prop:v125-cutoff-cost` · `closed/scalar-far-majorant` · evidence: [`evidence/v126/g2_window_resolution/`](evidence/v126/g2_window_resolution/) · **wall: cost of one estimate: N > L exp(M_phi/(1-c)); not every method** → `None` (prop:v125-cutoff-cost; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · Necessary lower barrier N+1 > L exp(M_phi/(1-c)) for the specified scalar majorant; no optimal-cutoff asymptotic
      - [X] **scalar signed primitive** — `cor:v137-scalar-no-go` · `closed/scalar-primitive` · evidence: [`evidence/v137/`](evidence/v137/) · **wall: genuine closure of the scalar route: a Delta(beta_a) -> infinity, unconditional** → `None` (cor:v137-scalar-no-go; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · a Delta(beta_a) -> infinity, unconditional
      - [!] **signed weighted concentration** — `prop:v131-concentration` · `lane/concentration` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: uniform complete signed operator floor remains unproved** → `floor` (prop:v131-concentration; QG/ZLD plus packets concern minorant complexity, not a proof of this floor) · Valid sufficient criterion; the missing positivity input is a complete joint signed operator lower bound with a uniform cofinal error. QG plus a separate admissible bounded-energy packet would obstruct bounded level count, not supply this positivity input. NS-22 grid-family losses and its invalid sampled tail charge prove no closure (NS-31/36). NS-43 proves unrestricted exact adaptive levels are equivalent to the floor target; a nonarithmetic countermodel refutes general completeness of scalar set bounds. Specific arithmetic operator estimates remain open. · **Continuation [WEIL-FLOOR](#input-weil-floor) (same floor under stated domains):** These continuations retain the complete signed floor. NS47 Clifford contraction and NS50 critical absorption share it; their coordinate change is not a new estimate.
        - [X] **Scalar set bounds alone determine signed floor: general inference** — `ns43-conc-prop-scalar` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: general inference false: countermodels with equal scalar set extrema and opposite signed bottoms** → `None` (ns43-conc-prop-scalar) · Exact commuting three-outcome countermodels share all scalar set extrema but have signed bottoms -1/5 and +1/10, also after exact source removal. General inference is false; no arithmetic realization or physical concentration impossibility claimed.
        - [x] **Unrestricted exact adaptive hierarchy = complement floor** — `ns43-conc-prop-adaptive` · evidence: [`evidence/v152/`](evidence/v152/) · Fixed-window compactness proves convergence of complete compressed lower edges. Cofinal uniform floor existence is equivalent; no effective complexity or new arithmetic bound. Growing adaptive level counts are unrestricted. · **Continuation [WEIL-FLOOR](#input-weil-floor) (same floor under stated domains):** These continuations retain the complete signed floor. NS47 Clifford contraction and NS50 critical absorption share it; their coordinate change is not a new estimate.
        - [!] **bounded-complexity minorants: arithmetic gap remains** — `prop:v146-packet-loss; prop:v146-level-complexity` · `codex/beta-lattice-identity` · evidence: [`evidence/v146/`](evidence/v146/) · **wall: ZLD + packet: conditional minorant-complexity obstruction only** → `None` (prop:v146-level-complexity inputs, named as ZLD in v1.47; no implication to the signed floor is established) · NS-27: eta >= [(b+B)c-B]+ and, conditionally, eta >= [cD/(2K)-Q]+. D->infinity is unconditional; uniform level mass, bounded packet energy and trough multiplicity are not established. Source and odd-sector scopes explicit; no proved closure. NS-29 makes the missing value-distribution statement ZLD explicit; cumulative size and arbitrary positive-fraction spread are insufficient. · **Continuation [LEVEL-PACKETS](#input-level-packets) (complexity input only):** Do not label this missing level/packet estimate as the signed positivity input.
          - [!] **zero level distribution and packet coverage: open inputs** — `prop:v147-level-separation; ass:v147-zld; prop:v147-depth-measure; prop:v147-broad-packet` · `codex/level-density-zero-statement` · evidence: [`evidence/v147/`](evidence/v147/) · **wall: ZLD + packet: conditional minorant-complexity obstruction only** → `None` (ass:v147-zld; packet coverage eq:v147-packet-coverage; no implication to the signed floor is established) · NS-29: conditional reduction requires lower measures for every level band and source-admissible bounded-energy packet coverage of those bands. Zero theorems assessed do not provide the input. D->infinity gives no uniform band measure; broad pulses cost log X. No closure or RH-equivalence claim. · **Continuation [LEVEL-PACKETS](#input-level-packets) (complexity input only):** Do not label this missing level/packet estimate as the signed positivity input.
            - [!] **weighted exact cost: peak bound fails at critical levels** — `prop:v149-critical-density; prop:v149-weighted-cost; prop:v149-qc1-insufficient; ass:v149-qg` · `codex/weighted-level-review` · evidence: [`evidence/v149/`](evidence/v149/) · **wall: QG + WLH packet: conditional minorant-complexity obstruction only** → `None` (ass:v149-qg; no implication to the signed floor is established) · NS-32/33: PR14 withdrawn after major findings. Exact density is unbounded at negative critical values; histogram peaks are not caps. The conditional QC_K loss implication survives. QG and source-admissible bounded-energy all-Borel WLH remain open inputs for a bounded-level obstruction, not for a positivity proof. NS-31/36 repair finite-bin interpretations; no closed physical route or G2/RH claim. · **Continuation [LEVEL-PACKETS](#input-level-packets) (complexity input only):** Do not label this missing level/packet estimate as the signed positivity input.
        - [x] **exact lattice symbol; varying envelopes** — `prop:v146-beta-explicit` · `codex/beta-lattice-identity` · evidence: [`evidence/v146/`](evidence/v146/) · Unconditional Perron identity with strict endpoint, trivial zeros and remainder. NS-26: 40 low plus 14 deep/centroid samples; numerical illustration only. Classical explicit formula restated, not new positivity content.
        - [x] **pencil loss budget; cofinal obligation retained** — `prop:v144-pencil-concentration` · `codex/complete-ground-zero-transfer` · evidence: [`evidence/v144/`](evidence/v144/) · NS-24 exact translation: relative loss <= nu_k + eta_a ||v_k||^2/q+. Source constraint and mixture cross terms retained. Diagnostic thresholds not certified; fixed-head tests do not replace cofinal full-complement control. No new concentration bound. · **Continuation [WEIL-FLOOR](#input-weil-floor) (supporting implication):** The equivalence/transfer is proved as stated; existence of the common cofinal bound is not.
      - [X] **unsigned prime-norm domination** — `prop:v119-prime-essential` · `closed/prime-norm` · evidence: [`evidence/v124/g2_growing_sign/`](evidence/v124/g2_growing_sign/) · **wall: cost: prime norm ~ lambda survives finite removal; exponential cutoff (estimate, not route)** → `None` (prop:v119-prime-essential; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · norm ~ lambda, survives any finite removal

## Reading it

Each node is an idea. A node with children is a branch point: the
children are the sub-ideas tried from it. A `closed` node excludes only
its stated comparison, construction or inference under its hypotheses.
It does not close every neighboring route. `live` records current activity,
not an exclusive recommendation. A proved tool may have an open continuation.

Continuation tags group missing inputs without changing theorem statuses.
Read each relation: same selected cost, stronger sufficient budget, broader
gain target and distinct criterion are not interchangeable. NS99 audits these
dependencies; NS100 separately screens possible new tests. Neither audit is
a new theorem node or an RH advance.

Nodes marked with a folder icon are clickable in the diagram and link
to their evidence directory, which may contain proofs, certificates or
explicitly labeled diagnostics; the same
links appear in the list above.

