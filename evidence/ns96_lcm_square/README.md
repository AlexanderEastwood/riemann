# NS96: divisor squares before and after refitting

**Scoped analytic results; no lower gain for the unrestricted actual error.**

The complete coefficient rule `c = -q`, where `q` groups any PSD matrix
by least common multiple, has squared error at least **3087/4096** at every
size. The opposite complete rule `c = q` has squared error at least
`1-log(2)-log(2)^2/2-log(2)^4/8 > 1/32`.

These floors cease to apply after arbitrary old-coefficient refitting.
In fact the projected PSD cone equals the full signed span of the new LCM
atoms. A single pair of rank-one squares generates both signs of each
projected atom. Every nonzero LCM pairing matrix of an old-orthogonal
residual is indefinite. This is not a no-go for the refitted approximation
class, a single constrained square, or Selberg sieve methods generally.

`argument.tex` proves the complete Mellin identity including the exterior,
both floors, projected-cone equality, and the necessary signed real-moment
balance after refitting. The LCM/divisor-square algebra is classical;
the cited primary lecture notes supply context, not an unproved input.

Replay from the repository root:

```sh
python evidence/ns96_lcm_square/certify.py --bits 256 --output evidence/ns96_lcm_square/check-256bits.json
python evidence/ns96_lcm_square/certify.py --bits 384 --output evidence/ns96_lcm_square/check-384bits.json
maxima --very-quiet -b evidence/ns96_lcm_square/checks.mac > evidence/ns96_lcm_square/checks-output.txt
python evidence/ns96_lcm_square/verify.py
```

Used Python 3.14.6, python-flint 0.9.0, Maxima 5.50.0 and pyright 1.1.411.
The Python dependency is pinned in `requirements-replay.txt`; no new
dependency was installed. The two-precision runs enclose scalar
constants and check finite exact algebra at N=3,4,8,12; they do not prove
the general theorems by sampling. Those are analytic proofs. No physical
cutoff or optimized Gram computation enters this result, so a numerical
tail-cutoff replay is inapplicable. The 17 Maxima checks supplement author
review; no independent review is claimed.

`dependencies.json` binds unchanged normalization and scope sources to
the reviewed base. `turn-review.json` records the review of all 103 prior
conclusions and the post-handoff check. `inventory.json` hashes this
incremental evidence and the [versioned report](../../audits/lcm-square-obstruction-2026-09-23-v1.html).
The manuscript stays v1.66; both historical missing-original groups,
the actual cofinal lower gain, G2 and RH remain open.
