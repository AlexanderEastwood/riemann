# v1.66 incremental evidence: fixed-order critical-zero lower bound

NS83 applies Burnol's established dual-vector argument with explicit extra
Hardy operators. This is a logarithmic asymptotic LOWER bound for squared
error, not the missing upper bound or a proof of convergence. It gives no
finite-size onset and no asymptotic equality. Its order q is fixed.

The certified script evaluates ten positive critical-zero enclosures and
both-conjugate weights for q=1,2,3, with weight one per zero. Omitted terms
are nonnegative; this subset is not asserted to approximate the full sum.
It also checks exact rational Hilbert inverse corners for multiplicities
1..8; the all-multiplicity identity is analytic, not inferred from this list.

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v166/ns83/certify_constants.py --bits 256
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v166/ns83/certify_constants.py --bits 384
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v166/verify_replays.py
maxima --very-quiet -b evidence/v166/ns83/exact-checks.mac
pyright evidence/v166
./manuscript/build.sh
python3 tools/verify_manifest.py v166
```

There are 43 precision enclosure matches and 33 exact Maxima checks.
No numerical onset N0 is claimed. This theorem does not imply a pointwise
bound on each block gain, and does not restrict the earlier uniform capture
of available gain. Original cofinal arithmetic decay, Weil floor, G2 and RH
remain open. Local self-review only, with literature inputs explicit.
