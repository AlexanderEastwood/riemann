# v1.60 evidence: complete cancellation and selected directions

This directory contains only new NS-67–71 evidence. RH and G2 remain open.
No independent review is claimed. The complete q=2 Gram implementation is
inherited, unchanged, from `../v159/ns61/certify_smoothed.py`; its SHA-256
is recorded in each dependent certificate.

- `ns67/`: exact signed physical cells, full tails, complete mixed terms,
  polynomial-cutoff growth equivalence, and centered Abel conditioning.
- `ns68/`: complete first-annulus forcing, positive weighted renewal,
  RH-equivalent scalar growth target, and critical total-energy divergence.
- `ns69/`: actual optimized endpoint remainder, factor-18 improved absolute
  allowance, and full projected one/two-direction finite gain comparisons.
- `ns70/`: elementary Gram cusp correction and the precise all-coefficient
  comparison exclusions. The actual Gram stays positive.
- `ns71/`: repaired-kernel selection measured with the complete actual Gram;
  97.06% of the optimal finite block gain at N=256, with its open cofinal
  numerator/cost input stated explicitly.
- `proof.tex`: concatenated proof fragments, included verbatim once in the
  live manuscript. `validation.json` pins source hashes and check scope.
- `research-update-2026-09-23-v1.html`: readable report.
- `integration-review-2026-09-23-v1.html`: local self-review, not an
  independent audit or a publication-readiness claim.

## Classification and limits

The proofs contain exact identities and proved implications with stated
hypotheses. The JSON files certify only the displayed finite computations,
constants and full tails. The canonical growth and optimized correlation
estimates remain open. Finite efficiency is not evidence of a cofinal bound.

Floating-point scans are outside this directory, under
`../diag_ns67_canonical_cells/`; they are not certificates.

## Replay from repository root

Certified dependencies are pinned in `requirements-replay.txt`. Optional
illustration dependencies are separate. `runtime-provenance.json` records
the tested Python/Arb/Maxima/TeX versions.

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v160/ns67/verify_replays.py
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v160/verify_replays.py
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v160/ns71/verify_replays.py
```

For fresh computations, invoke each `certify_*.py --help`. Canonical cells
use N=8,16,64,512,4096 and cutoff 1024N, with a 2048N replay at N=16,512.
Independent complete Gram checks use N=8,16,64. Renewal checks use
N=16,64,512,4096,65536,1048576. Optimized endpoint checks use
N=16,32,64,128, with a doubled series cutoff at N=128. Background checks
use n=256,1024,4096, with all three replayed at doubled cutoff.
Preconditioner checks use N=16,32,64,128,256, with doubled cutoff at N=256.
Every primary finite computation is repeated at 256 and 384 bits.

The Gram-series cutoff is 128, doubled to 256 for independent tail replay;
Bernoulli order is 24. The complete remainder is retained at either cutoff.
This changes an enclosure's sharpness, not the mathematical finite problem.
All solves retain Arb balls. No midpoint solve enters a certificate.

Run each `ns*/exact-checks.mac` with Maxima; all 137 exact checks must pass.
Maxima exit status alone is insufficient: require each saved PASS count and
no error. The NS-69 file explicitly disables scalar-matrix simplification;
NS-70 supplies its mathematical positivity assumption to symbolic limits.

```sh
./manuscript/build.sh
python3 tools/verify_manifest.py v160
```
