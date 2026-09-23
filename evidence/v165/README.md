# v1.65 incremental evidence: retaining the analytic physical tail

Exact theorem and certified scalar constants only. No large comparator
matrix or preconditioned iteration was assembled or executed. This uses a
different physical-cell comparator from NS81, preserving the exact
logarithmic main tail as a rank-two form. The full remainder and cross terms
are retained. The theorem does not imply cofinal decay, G2 or RH.

Replay:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v165/ns82/certify_tail.py --bits 256
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v165/ns82/certify_tail.py --bits 384
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v165/verify_replays.py
maxima --very-quiet -b evidence/v165/ns82/exact-checks.mac
pyright evidence/v165
./manuscript/build.sh
python3 tools/verify_manifest.py v165
```

Twenty scalar enclosures match across precisions. Four exact rational
cube-root cutoffs are independently rechecked. The Maxima file must report
12 exact checks. No numerical tail cutoff is silently substituted: the
complete discarded Bernoulli remainder is handled analytically. Local
self-review only; no independent review or practical solver claim.
