# v1.61 evidence: local geometry and arithmetic controls

Only new NS-72–74 evidence is included. RH and G2 remain open. No independent
review is claimed. The complete Gram/tail kernel is inherited unchanged
from v159/ns61, and projection helpers from v160/ns71; hashes are recorded.

- `ns72/`: causal factor, whole-line differential energy, interpolation and
  size-independent model-curvature comparison; complete finite gains.
- `ns73/`: prescribed physical Mobius/log-taper directions and their complete
  optimized three-dimensional span. This is not an asymptotic exclusion.
- `ns74/`: unitary altered family with unchanged complete Grams and an explicit
  positive floor. This is not a zero or floor for the original zeta family.
- `proof.tex`: proof fragments concatenated verbatim in the live manuscript.
- `validation.json`: actual build, replay, source-hash and review scope.
- The two dated HTML files give the readable update and local self-review.

All finite numerical evidence is ball arithmetic; no midpoint solve is used.
The finite kernel cutoff 128 retains the full Bernoulli/Hurwitz remainder,
with order 24. Cutoff 256 tightens the same complete problem at N=256.
All five sizes N=16,32,64,128,256 run at 256 and 384 bits. Every run has a
source hash and inherited-dependency hashes. NS74 offsets are exactly 1/10^6
and 1/10^10 above 1/2. The altered problem has the same target norm 2.

## Reproduce from the repository root

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v161/ns72/verify_replays.py
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v161/verify_replays.py
pyright evidence/v161
./manuscript/build.sh
python3 tools/verify_manifest.py v161
```

Fresh calculations: invoke each `certify_*.py --help`, using the sizes and
precisions above. Use `--cutoff 256 --sizes 256` for the cutoff replay.
Run all three `exact-checks.mac` files with Maxima and require saved PASS
counts 41, 10 and 16, not just a successful process status.

The local energy proof uses the additive positive derivative functional
on each piece and identifies it with the L0 norm only after joining the
whole-line extension. No finite-piece integration boundary is dropped.
The O(N) rule counts scalar operations after the actual correlations are
known; neither finding those correlations nor bit complexity is claimed linear.
The minimum-accuracy summaries for NS73 additionally check all serialized
fit coefficients, beyond the gain/energy metrics recorded by its generator.

No finite table supplies the cofinal curvature/numerator or true-cost bound.
