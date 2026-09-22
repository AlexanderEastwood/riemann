# v1.53 — NS-46: fine translated-radical blocks

Classification: analytic proofs and an explicit open input. This is not a
numerical illustration or a certified computation. No new window or tail metric.

## Result and scope

The construction changes the v1.35 block: centers remain in [-1,1] while their
spacing shrinks, and a finite interpolation estimate explicitly pays the Gram
conditioning cost. For a=log(lambda) sufficiently large, set
J=floor(lambda²/(40000a)), m=2J+1. The complete cutoff block has rank m,
exact even/odd ranks J+1 and J, and complete operator residual at most
C exp(-lambda²/2000). Thus m is asymptotic to lambda²/(20000 log lambda).

Removing o(lambda²/log lambda) directions cannot leave a uniform positive gap
or a positive gap bounded below by a fixed power of lambda^(-1). Smaller
positive gaps are not excluded. This is an obstruction to that positive
coercivity objective; it does not exhibit a negative Weil direction or bound
the remaining complement. The actual even source removes at most one even
block dimension. Full prime and pole terms, and all block mixtures, are retained.

The complete, signed, uniform complementary lower floor remains an open input.
Its transfer to the full form was already proved in v1.18/v1.36. No new transfer
lemma is claimed. Neither G2 nor RH is proved. The constants and eventual
starting threshold are analytic; no finite numerical threshold is certified.

## Files and verification

- `new_section.tex`: authoritative new manuscript section, embedded verbatim.
- `ns46-fine-block-2026-09-22-v1.html`: versioned user-facing report.
- `build_report.json`: actual integrated build, 269 pages and zero undefined
  references, duplicate references, or overfull boxes.
- `review_record.md`: independent review scope and resolved summary finding.
- `provenance.json`: SHA256/size inventory of the original author and review files.
- `../ns46_radical_block/`: pinned source proofs, independent reviews, and Astra-2's
  separately labeled fixed-spacing companion. The companion and its literature
  input are not used in the v1.53 theorem or integrated into the manuscript.

Replay the actual build with `./manuscript/build.sh`; validate this incremental
archive with `python3 tools/verify_manifest.py v153`. Check the external
inventory by comparing each path, byte length and SHA256 in `provenance.json`.
This integrity check does not replace analytic review.

Local draft based on commit 24f4ab5 (PR #21), with standalone task claim
0355edb. No v1.53 publication, merge or tag is asserted. Main advanced to
b0baadf while work was isolated; the PR #21 dependency is retained explicitly.
