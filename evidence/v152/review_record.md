# NS-43/44/45 coordinated review record

Classification: adversarial mathematical and provenance review, with the
separately identified independent interval replays. This record is not itself
a numerical certificate. All scope limitations in the author proofs remain.

## Analytic proofs

- **Capacity channels — Astra RH1, read-only review:** no MAJOR/MINOR in
  `prime_channel_obstruction.tex`, SHA256
  `69adde550e66edf804ebe3b0ac215f60a255fdb5228b675cdd0a67bcc8c6d66a`.
  Checked inward-edge geometry for fixed and moving channels, use of evenness
  when an endpoint crosses zero, exact source kernel, unit-mixture cross terms,
  original-form upper budget, and precisely scoped truncation conclusions.
- **Bump input strength — Astra RH2, read-only review:** no MAJOR/MINOR in
  `bump_input_strength.tex`, SHA256
  `a333c4fbcd7098e4b789215834232e44224a9d57df465f708d886f6f272345e2`.
  Checked the plus sign on the zeta logarithmic derivative, finite endpoint
  correction, cancellation at s=1/2, residue at an off-line zero, and the
  infinite uniform-convolution probe with only imaginary transform zeros.
  Boundedness remains unproved; no converse is asserted. The arbitrary-pair
  statement permits masking only at common transform zeros, rather than
  excluding such masking.
- **Concentration — coordinator and assisting-agent integration review:**
  compactness, rather than generic strong-resolvent convergence, proves lower-edge
  convergence. Review added the explicit nonzero form-domain test assumption
  for the generalized theorem; it holds for the actual logarithmic-growth
  symbol. Use `concentration_operator_collapse-v2.tex`, SHA256
  `6320c6f77d81f98a3496bb6043af71f036c1e49be728a519ed91cfce1955031a`.
  The original fragment is preserved. The three-outcome scalar countermodel
  is explicitly nonarithmetic.
- **CCM — independent concentration-agent review:** one MINOR scope issue was
  corrected by explicitly resetting the coarse-profile proposition to the full
  both-parity form. The final complete-ground statement likewise includes both
  parities. The direct cross-term floor is stated explicitly; no relative rate
  is needed for that floor, while selection does require relative control.
  Use `selection_note-v2.tex`, SHA256
  `3c4135cdea011f07184a68afd54c45e389cb53f982ebb11cd33b0de08ebd9286`.
  The original proof/report is preserved. Final review has no outstanding
  MAJOR/MINOR/NOTE; see `concentration/ccm_review.md`.

## Certified comparisons

- **NS-44:** the independent review reran the frozen verifier into temporary
  output and checked a separate direct four-sign sum without calling the
  author's parity block or signed-pairing function. Both 320/448-bit gates pass.
  Coefficient remainder bounds and the actual archimedean D were checked.
  Final hardening adds explicit rejection of optimized Python with disabled
  assertions in both entry points. All numerical quantities and witnesses are
  unchanged. Final source SHA256
  `8d49106455b72127d8ff8c617cc12f4f0419580896e49e2b3117115892a89fa2`;
  certificate SHA256
  `a32b8d9dac79037392f6dfc124152bf04dcac826864af16dafeb88dcc468781b`.
  Final review pins and final replay are in `concentration/ns44_review.md`.
- **NS-45:** the independent CCM-agent review reran the complete verifier with
  temporary output. Both precisions passed, producing a byte-identical
  certificate, SHA256
  `ee9b6a526ec79a6501f426957e847940d7052f0da39bb8c86690b7237aa19114`.
  Checked exact dyadics, both signed-index embeddings, squared cross gates,
  positive-metric dichotomy, rational Rayleigh arithmetic and infinite-extension
  implication. No full-block inertia certificate is assumed. See
  `ccm/ns45_review.md` and its replay transcript.
- **Integrated certified propositions — Astra RH1, read-only review:** no
  MAJOR mathematical finding in `comparison_replays.tex`, SHA256
  `5c7b2c69a05aa7f7002bc4fd8a7ee8d486aac03e027fe750a997f544d085d181`.
  Its MINOR provenance finding caught the transient NS-44 review-pin mismatch
  during the guard hardening; the final independent review now pins the hardened
  source and regenerated certificate above. The mathematical values were never
  changed. It confirmed the universal Q16 comparison needs no source projection,
  and that the exact Rayleigh obstruction closes only the tested partition.

## Integration

The v1.52 fragment preserves the final concentration proof and final CCM v2.
CCM's printed literal labels are changed to live references and its user-facing
node recommendations are omitted from the manuscript. The primary Dirichlet
identity link is added to the bump proof. Those presentation changes do not
alter the propositions. The final integration review also corrects the map's
common-transform-zero wording. See `concentration/integration_review.md` for
the final pinned integration and map checks.

The final provenance index pins every new author file and review. Existing
PRs #18–20 were coordinated without modifying their branches. The v1.52 work
is local, based on PR #20; no merge, tag or new publication is asserted.
