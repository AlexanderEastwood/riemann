# v1.62 evidence: divisor feedback and continuous relaxation

Incremental NS-75–77 evidence only. RH/G2 remain open. Local self-review only.
The classical factorization and published zero verification are external inputs.

- `ns75/`: exact divisor-log cells and full jump measure; actual coefficient
  feedback, three-direction span, and held-old unit-step control. Every finite
  quantity uses the full arithmetic Gram, tails, projection and cross terms.
- `ns76/`: complete tail unitary, exact continuous q=2 distance, invisible
  residual component, and strict closure separation with a certified witness.
- `ns77/`: positive complete zero-tail bound and scalar calibration. The
  Platt–Trudgian zero verification is cited, not re-executed or archived here.
- `proof.tex` is integrated verbatim in the live manuscript.
- Dated HTML files give the readable update and local self-review.

## Reproduce

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v162/verify_replays.py
pyright evidence/v162
./manuscript/build.sh
python3 tools/verify_manifest.py v162
```

For fresh NS75 runs use `certify_divisor.py --bits 256 --sizes 16 32 64 128 256
--output <new-path>` and replay at 384 bits. The cutoff replay adds
`--cutoff 256 --sizes 256`. The default cutoff 128 and Bernoulli order 24
retain the complete Hurwitz/Bernoulli tail; increasing cutoff tightens the
same problem. Inherited kernel/projection/curvature hashes are recorded.
NS76 `certify_local_gap.py --bits 256` and NS77 `certify_tail.py --bits 256`
print JSON; repeat at 384 bits. Their complete elementary expressions have
no numerical cutoff. NS77 handles the full zero tail analytically.
Run the three Maxima files; require PASS counts 11, 29 and 18.

No midpoint solve is used. Source hashes, replay enclosures, manuscript
intervals, overlap with the published curvature calculation, and claim
scope are checked. The local separator is a lower bound for sigma_(3/2),
not tau. The tiny continuous bound is not an integer error upper bound.
