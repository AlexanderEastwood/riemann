# v1.63 evidence: full arithmetic sampling and finite-block efficiency

Incremental NS-78–80 evidence only. RH/G2 remain open. Local self-review only.

- `ns78/`: uniform complete norm comparison, exact sample/divisor inversion,
  physical-cell integration, and analytic physical and sample tails.
- `ns79/`: tail-balanced feedback and endpoint-augmented span. Complete true
  energies and old projections; the last jump is deliberately not cancelled.
- `ns80/`: full arithmetic Gram comparison, Schur transfer and uniform ideal
  block efficiency. Analytic theorem and exact rational Maxima checks; no
  numerical implementation or finite-prefix substitute for its inverse.
- `proof.tex` is integrated verbatim into the live manuscript.
- Dated HTML files give the readable update and local self-review.

## Reproduce

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v163/verify_replays.py
pyright evidence/v163
./manuscript/build.sh
python3 tools/verify_manifest.py v163
```

NS78: `certify_cells.py --bits 256 --sizes 16 64 256 --output <new-path>`;
repeat at 384 bits. Replay N=256 with `--cell-stop 131072 --kernel-cutoff
256`. The default cell stop is 65536; all cells beyond it are bounded, not
omitted. The initial kernel series cutoff is 128 with full order-24 tail.
The accurate finite norm, main tail and analytic radius are archived
separately; printed combined balls can be wider due to decimal rounding.

NS79: `certify_balanced.py --bits 256 --sizes 16 32 64 128 256 --output
<new-path>`; repeat at 384 bits. Replay N=256 with `--cutoff 256`.
Every inherited scientific dependency is hash-checked. All solves retain
Arb balls; no midpoint solve is used.

Run the three Maxima files and require PASS counts 30, 16 and 10.
NS80 uses exact rational constants, so no floating-point replay is needed.
A uniform fraction of available block gain does not prove zero limiting
error. No new Weil window, original uniform floor, G2 or RH proof.
