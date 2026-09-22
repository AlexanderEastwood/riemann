# Riemann project research map

_Generated from `research-map.json` — last updated 2026-09-22._
_Do not hand-edit: run `python3 tools/make_map.py`._

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
  altroutes["Alternative criteria (classical RH equivalents; no finite bridge proved)"]
  circle["circle / Toeplitz-Hankel lens<br/><small>&#128193; evidence/diag_true_symbol</small>"]
  debranges["de Branges / Hermite-Biehler<br/><small><b>wall: screw-kernel positivity = RH; no fixed-window bridge</b></small>"]
  f1["function field / Hodge / F_1<br/><small><b>wall: no intersection form supplied for this window (missing construction)</b></small>"]
  nb["Nyman-Beurling-Baez-Duarte<br/><small>&#128193; evidence/diag_routes/nb</small><br/><small><b>wall: d_N -> 0 = RH; no finite bridge from W_4 to d_N</b></small>"]
  li["Li / Keiper coefficients<br/><small>&#128193; evidence/diag_routes/li</small><br/><small><b>wall: all Li coefficients >= 0 = RH; windowed coefficients are different objects</b></small>"]
  dbn["de Bruijn-Newman (Lambda = 0 iff RH)<br/><small>&#128193; evidence/diag_routes/dbn</small><br/><small><b>wall: Lambda <= 0 = RH; positive-time barrier reproduced, no-bridge not proved</b></small>"]
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
  concentration -. "QG + WLH packet" .-> floor
  debranges -. "screw-kernel positivity = RH; no fixed-window bridge" .-> rh
  nb -. "d_N -> 0 = RH; no finite bridge from W_4 to d_N" .-> rh
  li -. "all Li coefficients >= 0 = RH; windowed coefficients are different objects" .-> rh
  dbn -. "Lambda <= 0 = RH; positive-time barrier reproduced, no-bridge not proved" .-> rh
  minorantlevels -. "ZLD + packet" .-> floor
  zeroleveldistribution -. "ZLD + packet" .-> floor
  weightedexactcost -. "QG + WLH packet" .-> floor
  capacityweight -. "CAE" .-> floor
  relativeselection -. "cofinal separator" .-> g2

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
  click nb "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_routes/nb/" "evidence: evidence/diag_routes/nb" _blank
  click li "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_routes/li/" "evidence: evidence/diag_routes/li" _blank
  click dbn "https://github.com/AlexanderEastwood/riemann/tree/main/evidence/diag_routes/dbn/" "evidence: evidence/diag_routes/dbn" _blank
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

  classDef proved fill:#a5d6a7,stroke:#1b5e20,stroke-width:1px,color:#000;
  class g1,windows,w3,w4e,w4o,w4,weaken,floor,gapfree,floortest,shiftbarrier,metablind,ccmmu,simpleeven4,semanticlock,groundzero4,groundzero4resolution,pencilconcentration,betaexplicit,inputcomparison,bumpstrength,adaptiveidentity proved;
  classDef live fill:#ffd54f,stroke:#f57f17,stroke-width:3px,color:#000;
  class stepb live;
  classDef closed fill:#ef9a9a,stroke:#b71c1c,stroke-width:1px,color:#000;
  class w5,primenorm,normcontr,schatten,sampling,farmaj,blockmetric,flattop,recipband,cotlar,scalarprim,capacityslack,capacitychannels,scalarsetshortcut,absoluteselection,coarseprofile,fineradicalrank closed;
  classDef blocked fill:#ce93d8,stroke:#4a148c,stroke-width:1px,color:#000;
  class concentration,debranges,f1,nb,li,dbn,minorantlevels,zeroleveldistribution,weightedexactcost,capacityweight,relativeselection blocked;
  classDef open fill:#cfd8dc,stroke:#37474f,stroke-width:1px,color:#000;
  class rh,fixedspace,g2,uniform,altroutes,circle open;
  subgraph Legend
    direction LR
    lg_live["current route (gold)"]:::live
    lg_closed["closed route"]:::closed
    lg_proved["proved"]:::proved
    lg_open["open"]:::open
    lg_blocked["blocked"]:::blocked
  end
```

## Status

| status | count | meaning |
|---|---:|---|
| `proved` | 22 | established result |
| `live` | 1 | current route (gold): being worked now |
| `closed` | 17 | closed route (red): proved insufficient or impossible; kept deliberately |
| `blocked` | 11 | attempted; obstruction found |
| `open` | 6 | target, not yet attacked |
| `wall` | 0 | wall tag: on a blocked node, the named open input it terminates on (dashed edge to the node that input reduces to); on a closed node, the closing mechanism and its scope (estimate/construction/route), no edge |

## Nodes

- [ ] **RH** — via Weil positivity
  - [ ] **Alternative criteria (classical RH equivalents; no finite bridge proved)** — Each child is a classical RH criterion. The record proved structural obstructions to specific bridges, not that every bridge fails; 'all equivalent; same wall' withdrawn per audit PR #22.
    - [!] **Li / Keiper coefficients** — evidence: [`evidence/diag_routes/li/`](evidence/diag_routes/li/) · **wall: all Li coefficients >= 0 = RH; windowed coefficients are different objects** → `rh` (Li class ∩ finite-window Paley-Wiener class = {0} blocks direct identification; that every transfer reduces to prop:v121 is argued, not proved) · audit PR #22 (2026-09-22-conclusions-review.md §4): classical RH criterion; no finite bridge to window positivity proved in either direction; 'closed' withdrawn. What is proved: the canonical rational Li-transform class meets the fixed-window entire class trivially.
    - [!] **Nyman-Beurling-Baez-Duarte** — evidence: [`evidence/diag_routes/nb/`](evidence/diag_routes/nb/) · **wall: d_N -> 0 = RH; no finite bridge from W_4 to d_N** → `rh` (Burnol's zero-evaluator/co-Poisson dictionary is structural, not a bound for a specified d_N; the report's sharp-rate necessity claim is false (audit A3)) · audit PR #22 (2026-09-22-conclusions-review.md §4): classical RH criterion; no finite bridge to window positivity proved in either direction; 'closed' withdrawn. The earlier 'a proof must attain the sharp C/log N rate' sentence is withdrawn (audit A3).
    - [ ] **circle / Toeplitz-Hankel lens** — `lane/circle-toeplitz` · evidence: [`evidence/diag_true_symbol/`](evidence/diag_true_symbol/) · measurement lane; closure claims withdrawn after NS-31; geometry and exact identities retained
    - [!] **de Branges / Hermite-Biehler** — **wall: screw-kernel positivity = RH; no fixed-window bridge** → `rh` (Suzuki Thm 1.5 (arXiv 2606.09096); the shifted finite-window construction sits strictly below the spectral bottom and does not determine its sign; fixed-window determinacy equivalence not proved) · audit PR #22 (2026-09-22-conclusions-review.md §4): classical RH criterion; no finite bridge to window positivity proved in either direction; 'closed' withdrawn. Structural statement only: existence of the shifted de Branges structure does not decide the unshifted sign.
    - [!] **de Bruijn-Newman (Lambda = 0 iff RH)** — evidence: [`evidence/diag_routes/dbn/`](evidence/diag_routes/dbn/) · **wall: Lambda <= 0 = RH; positive-time barrier reproduced, no-bridge not proved** → `rh` (Rodgers-Tao Lambda >= 0; the record reproduced a specified positive-time barrier, not a theorem excluding all transfer arguments (audit A4); v1.46 exact zero expansion postdates the route report) · audit PR #22 (2026-09-22-conclusions-review.md §4): classical RH criterion; no finite bridge to window positivity proved in either direction; 'closed' withdrawn. Blanket 'no bridge' withdrawn (audit A4); the route was closed before the v1.46 exact zero expansion existed.
    - [!] **function field / Hodge / F_1** — **wall: no intersection form supplied for this window (missing construction)** → `None` (RESEARCH_MAP note supplied no number-field intersection form, transfer map, or impossibility proof; function-field RH is a theorem for different objects) · audit PR #22 (2026-09-22-conclusions-review.md §4): classical RH criterion; no finite bridge to window positivity proved in either direction; 'closed' withdrawn. Not an RH-equivalent criterion here: a missing construction, so no dashed edge.
  - [ ] **Fixed-space / Burnol Sonine route** — `lane/fixed-space` · needs evaluator estimates + closed-operator realization
  - [x] **G1 (weak)** — `thm:v14-radical` · `lane/g1` · evidence: [`evidence/v124/g2_source_certificate/`](evidence/v124/g2_source_certificate/) · closed for the repaired prolate source
  - [ ] **G2: cofinal -o(1)** — `prop:v121-cofinal-rh` · eps_lambda -> 0 cofinally IS RH
    - [x] **Fixed-window certificates** — `lane/window-scaling` · no finite list is cofinal
      - [x] **CCM finite-compression semantic lock, lambda=3 N=120** — `lem:v141-centering; prop:v141-ccm-lock` · evidence: [`evidence/v141/`](evidence/v141/) · Eight local root discrepancies reproduce CCM Figure 1 with 768/1024-bit interval gates. The zero benchmark cannot detect a common positive scale or identity shift. No new window, complete-ground transfer or cofinal statement.
      - [x] **W_4 >= 0 both sectors** — `prop:v126-full-window` · evidence: [`evidence/v126/`](evidence/v126/) · only positive result; evidence restored and verified
        - [x] **W_4 >= 0  <=>  CCM mu_lambda >= 0 for all lambda <= 4** — CCM arXiv:2511.22755 Cor 3.7-3.8 write 'we cannot assert mu_lambda >= 0'; monotone in lambda; positioning statement
        - [x] **complete W_4: simple even ground; real-zero transform** — `prop:v140-ground4; cor:v140-real-zeros` · `result/ns5-ground-state` · evidence: [`evidence/v140/`](evidence/v140/) · NS-5 complete: mu0<2.454e-75, mu1>1e-73, 1024/1280-bit shifted inertia; CvS Thm6.1 applies; no Xi convergence or G2 claim
          - [~] **CCM step (b): finite-compression zeros track zeta zeros (numerical)** — evidence: [`evidence/diag_ns2_semantic_lock/`](evidence/diag_ns2_semantic_lock/) · The 170-value CCM reproduction is a midpoint diagnostic, not a bound. Eight lambda=3, N=120 local roots are certified separately in v1.41. Original sinc-lattice inference withdrawn: missing centering phase in zeros.py. v1.42 separately encloses one complete lambda=4 zero within 0.1 of gamma_1. High-accuracy discrepancy transfer and cofinal Xi convergence remain open. v1.43 certifies a complete first-positive-zero radius 8.752082e-33 and quantifies the archived bound resolution; no complete discrepancy sign or 1e-71 magnitude. NS-43 supplies precise complete relative-selection and entire-transform criteria; none is proved cofinally. Absolute residuals and ordinary resolvent collapse alone do not select the Gaussian, as an explicitly nonarithmetic countermodel shows.
            - [X] **Absolute residual/resolvent data alone select ground: abstract inference** — `prop:ns43-ccm-nonselection` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: abstract inference false: countermodel family with alternating profiles** → `None` (prop:ns43-ccm-nonselection) · Exact abstract family has simple even nonnegative real-zero grounds, arbitrarily fast residual decay, resolvent collapse and tight support, yet alternating profiles. It is not an arithmetic support-consistent Weil family; CCM itself remains open.
            - [!] **Complete relative selection and entire-transform control** — `prop:ns43-ccm-rayleigh-selection; prop:ns43-ccm-residual-selection` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: cofinal separator** → `g2` (prop:ns43-ccm-rayleigh-selection: missing cofinal complete separator relative to the cutoff residual) · Missing cofinal complete separator relative to the explicit cutoff residual, or Rayleigh-excess/gap plus evaluator/weighted-tightness control. Global-ground use additionally needs odd ordering. No fixed-head replacement or polynomial positive separator.
            - [X] **Single profile from the specified coarse rescaled liminf** — `prop:ns43-ccm-coarse-profile` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: under the explicit coarse scale the limit form is zero; finer scales open** → `None` (prop:ns43-ccm-coarse-profile) · Under the explicit scale, full both-parity liminf, nonnegativity and lower-semicontinuity hypotheses, density of translated radicals forces the limit form to zero. Finer scales and other selection mechanisms remain open.
          - [x] **complete ground zero within 0.1 of gamma_1** — `lem:v142-energy-projection; prop:v142-ground-zero` · `codex/complete-ground-zero-transfer` · evidence: [`evidence/v142/`](evidence/v142/) · 1024/1280-bit complete even separator 1e-67 plus energy projection; unique simple local zero, no earlier-zero ordering, discrepancy sign or cofinal claim.
            - [x] **first complete zero within 9e-33; archived resolution quantified** — `prop:v143-first-zero-bound; prop:v143-resolution; prop:v143-fixed-window-meaning` · `codex/complete-ground-zero-transfer` · evidence: [`evidence/v143/`](evidence/v143/) · NS-19: 1024/1280-bit evaluator bound and earlier-zero exclusion. A lower-energy transfer at 1e-71 needs rho-l about 3.2032e-153 plus a suitable trial center. No complete sign, universal resolution no-go or cofinal claim.
      - [x] **lambda=3** — `prop:v116-window-positive` · evidence: [`evidence/v124/g2_certificate/`](evidence/v124/g2_certificate/)
      - [x] **lambda=4 even** — `prop:v125-even-complete` · `result/v125-even-complete` · evidence: [`evidence/v126/`](evidence/v126/)
      - [x] **lambda=4 odd** — `prop:v126-odd-complement` · `result/v126-odd-complement` · evidence: [`evidence/v126/`](evidence/v126/)
      - [X] **lambda=5: stipulated 10^-8 D tail comparison** — `prop:v152-tail-comparison` · evidence: [`evidence/ns44_metric_replay/`](evidence/ns44_metric_replay/) · **wall: stipulated 1e-8 D tail comparison fails: positive q/D < 7e-18 (lambda=5)** → `None` (prop:v152-tail-comparison; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · NS-44 fresh exact dyadic witnesses, Arb 320/448: positive q/D <7e-18 even and <12e-18 odd, contradicting the stipulated 1e-8 comparison. Failure of this comparison, not negative Weil directions or complete lambda=5 positivity. Historical v1.27 originals remain unarchived.
    - [x] **Target weakening** — `lane/bounded-floor`
      - [x] **no uniform positive gap exists** — `prop:v135-growing-radical` · evidence: [`evidence/v135/`](evidence/v135/) · dense radical family; same fact as the floor reduction
        - [X] **Uniform or polynomial positive gap after o(lambda²/log lambda) removed directions** — `lem:ns46-finite-arc; ns46-a2-cor-large-block; ns46-a2-cor-rank` · evidence: [`evidence/v153/`](evidence/v153/) · **wall: positive-gap strategy must remove rank >= lambda^2/(20000 log lambda)** → `None` (lem:ns46-finite-arc; ns46-a2-cor-rank) · NS-46: fixed-range fine translates give complete near-zero rank asymptotic to lambda²/(20000 log lambda), exact even/odd counts and residual C exp(-lambda²/2000). Ill-conditioned finite Grams are bounded explicitly. The positive gap is at most this residual, so only uniform or polynomial positive coercivity is excluded; a smaller positive gap remains possible; no signed floor, negative Weil direction, finite starting-window certificate or closure of gap-free block methods.
      - [x] **uniform finite floor suffices** — `prop:v136-bounded-floor` · evidence: [`evidence/v136/`](evidence/v136/) · decay not required; dichotomy inf spec -> -inf or RH
        - [x] **W_lambda >= -8 I at lambda=5,6,8** — `prop:v138-three-floors` · `result/v138-three-floors` · evidence: [`evidence/v138/`](evidence/v138/) · both parities, full infinite tail, Z=0; margin 0.84 -> 0.10 (odd) as lambda grows; not cofinal
        - [x] **bounded shift keeps the exp cutoff barrier** — `prop:v138-shifted-floor` · evidence: [`evidence/v138/`](evidence/v138/) · N+1 > L exp(M_phi - delta); polynomial cutoff needs delta ~ M_phi
        - [!] **positive arithmetic weight: critical capacity input** — `lem:v150-weight; prop:v150-critical-energy; ass:v150-cae` · `codex/bounded-capacity-weight` · evidence: [`evidence/v150/`](evidence/v150/) · **wall: CAE** → `floor` (ass:v150-cae; CAE is the bounded-floor target in positive-weight coordinates (v1.51)) · NS-34: explicit positive Gaussian arithmetic radical with pole mass 1/sqrt(3); exact full and windowed Picone identities retain exterior edges and both parity poles. Critical Arithmetic Energy comparison (CAE) is the uniform complement-floor target in these coordinates, not an independent positivity theorem. Coefficient-one capacity error remains open. NS-43 extends the loss obstruction to any fixed prime-power channel and moving omitted channels bounded away from the endpoint, with unchanged other signed terms. Full coefficient-one or compensated estimates remain open.
          - [X] **Fixed/sub-endpoint channel deletion with unchanged signed terms** — `prop:ns43-fixed-channel; prop:ns43-moving-channel` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: channel deletion: unbounded comparison error for the Gaussian weight** → `None` (prop:ns43-fixed-channel; prop:ns43-moving-channel) · Exact source-admissible even and odd tests force an unbounded comparison error for the specified Gaussian weight. Covers bounded channel counts and sublinear-in-exp(2a) cutoffs. Endpoint-approaching omissions, compensation, and another weight are not closed.
          - [x] **Restricted bump discrepancy can carry the full zero obstruction** — `prop:ns43-bump-strength` · evidence: [`evidence/v152/`](evidence/v152/) · For an explicit smooth compact probe with transform zeros only on the imaginary axis, a bounded translated prime discrepancy would exclude off-line zeros. The bound is unproved; no converse or weaker-than-RH claim. For arbitrary probes, boundedness permits off-line zeros only at common transform zeros; it does not exclude that masking.
          - [x] **ZLD to QG; CAE is the signed-floor target** — `prop:v151-input-comparison` · `codex/ns38-ns39-integration` · evidence: [`evidence/v151/`](evidence/v151/) · NS-39: exact inverse corrected-zero-field formula for the potential, including finite-window pole mass. ZLD implies QG growth with kappa theta² D/(2K) on the same prescribed family; no packet input supplied. CAE equals the uniform complement floor. General measure countermodels are not arithmetic independence. All three arithmetic inputs remain open; no new positivity conclusion.
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
      - [X] **scalar far majorant** — `prop:v125-cutoff-cost` · `closed/scalar-far-majorant` · evidence: [`evidence/v126/g2_window_resolution/`](evidence/v126/g2_window_resolution/) · **wall: cost of one estimate: N > L exp(M_phi/(1-c)); not every method** → `None` (prop:v125-cutoff-cost; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · N ~ L exp(M_phi): exponential cutoff cost
      - [X] **scalar signed primitive** — `cor:v137-scalar-no-go` · `closed/scalar-primitive` · evidence: [`evidence/v137/`](evidence/v137/) · **wall: genuine closure of the scalar route: a Delta(beta_a) -> infinity, unconditional** → `None` (cor:v137-scalar-no-go; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · a Delta(beta_a) -> infinity, unconditional
      - [!] **signed weighted concentration** — `prop:v131-concentration` · `lane/concentration` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: QG + WLH packet** → `floor` (ass:v149-qg; ZLD implies the QC_K bound at a fixed window (prop:v151-input-comparison ii); CAE = target) · Valid sufficient criterion; the missing positivity input is a complete joint signed operator lower bound with a uniform cofinal error. QG plus a separate admissible bounded-energy packet would obstruct bounded level count, not supply this positivity input. NS-22 grid-family losses and its invalid sampled tail charge prove no closure (NS-31/36). NS-43 proves unrestricted exact adaptive levels are equivalent to the floor target; a nonarithmetic countermodel refutes general completeness of scalar set bounds. Specific arithmetic operator estimates remain open.
        - [X] **Scalar set bounds alone determine signed floor: general inference** — `ns43-conc-prop-scalar` · evidence: [`evidence/v152/`](evidence/v152/) · **wall: general inference false: countermodels with equal scalar set extrema and opposite signed bottoms** → `None` (ns43-conc-prop-scalar) · Exact commuting three-outcome countermodels share all scalar set extrema but have signed bottoms -1/5 and +1/10, also after exact source removal. General inference is false; no arithmetic realization or physical concentration impossibility claimed.
        - [x] **Unrestricted exact adaptive hierarchy = complement floor** — `ns43-conc-prop-adaptive` · evidence: [`evidence/v152/`](evidence/v152/) · Fixed-window compactness proves convergence of complete compressed lower edges. Cofinal uniform floor existence is equivalent; no effective complexity or new arithmetic bound. Growing adaptive level counts are unrestricted.
        - [!] **bounded-complexity minorants: arithmetic gap remains** — `prop:v146-packet-loss; prop:v146-level-complexity` · `codex/beta-lattice-identity` · evidence: [`evidence/v146/`](evidence/v146/) · **wall: ZLD + packet** → `floor` (prop:v146-level-complexity inputs, named as ZLD in v1.47) · NS-27: eta >= [(b+B)c-B]+ and, conditionally, eta >= [cD/(2K)-Q]+. D->infinity is unconditional; uniform level mass, bounded packet energy and trough multiplicity are not established. Source and odd-sector scopes explicit; no proved closure. NS-29 makes the missing value-distribution statement ZLD explicit; cumulative size and arbitrary positive-fraction spread are insufficient.
          - [!] **zero level distribution and packet coverage: open inputs** — `prop:v147-level-separation; ass:v147-zld; prop:v147-depth-measure; prop:v147-broad-packet` · `codex/level-density-zero-statement` · evidence: [`evidence/v147/`](evidence/v147/) · **wall: ZLD + packet** → `floor` (ass:v147-zld; packet coverage eq:v147-packet-coverage) · NS-29: conditional reduction requires lower measures for every level band and source-admissible bounded-energy packet coverage of those bands. Zero theorems assessed do not provide the input. D->infinity gives no uniform band measure; broad pulses cost log X. No closure or RH-equivalence claim.
            - [!] **weighted exact cost: peak bound fails at critical levels** — `prop:v149-critical-density; prop:v149-weighted-cost; prop:v149-qc1-insufficient; ass:v149-qg` · `codex/weighted-level-review` · evidence: [`evidence/v149/`](evidence/v149/) · **wall: QG + WLH packet** → `floor` (ass:v149-qg) · NS-32/33: PR14 withdrawn after major findings. Exact density is unbounded at negative critical values; histogram peaks are not caps. The conditional QC_K loss implication survives. QG and source-admissible bounded-energy all-Borel WLH remain open inputs for a bounded-level obstruction, not for a positivity proof. NS-31/36 repair finite-bin interpretations; no closed physical route or G2/RH claim.
        - [x] **exact lattice symbol; varying envelopes** — `prop:v146-beta-explicit` · `codex/beta-lattice-identity` · evidence: [`evidence/v146/`](evidence/v146/) · Unconditional Perron identity with strict endpoint, trivial zeros and remainder. NS-26: 40 low plus 14 deep/centroid samples; numerical illustration only. Classical explicit formula restated, not new positivity content.
        - [x] **pencil loss budget; cofinal obligation retained** — `prop:v144-pencil-concentration` · `codex/complete-ground-zero-transfer` · evidence: [`evidence/v144/`](evidence/v144/) · NS-24 exact translation: relative loss <= nu_k + eta_a ||v_k||^2/q+. Source constraint and mixture cross terms retained. Diagnostic thresholds not certified; fixed-head tests do not replace cofinal full-complement control. No new concentration bound.
      - [X] **unsigned prime-norm domination** — `prop:v119-prime-essential` · `closed/prime-norm` · evidence: [`evidence/v124/g2_growing_sign/`](evidence/v124/g2_growing_sign/) · **wall: cost: prime norm ~ lambda survives finite removal; exponential cutoff (estimate, not route)** → `None` (prop:v119-prime-essential; scope per audit PR #22 §2 (closure of the named estimate/construction, not of the surrounding route)) · norm ~ lambda, survives any finite removal

## Reading it

Each node is an idea. A node with children is a branch point: the
children are the sub-ideas tried from it. `closed` children are proved
dead ends and are kept deliberately — they are the project's main
output. `live` is the only node currently worth spending on.

Nodes marked with a folder icon are clickable in the diagram and link
to the `evidence/vNNN/` directory holding their certificates; the same
links appear in the list above.

