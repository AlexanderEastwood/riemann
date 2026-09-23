# NS95: square-scale product grouping

Exact restrictions and finite certificates; **no cofinal arithmetic lower bound**.
The free signed divisor-product space generalizes the prescribed NS86 correction,
but generally loses its defect-square prescription. Its new coefficients at mp
are independent of primes p>N whenever mp<=N^2. Full and restricted gains are
not identified. The arbitrary-residual comparison obstruction is not a failure
of the actual-target estimate.

`argument.tex` gives the product-space definitions, coefficient restriction,
exact complete gain split, constraint-loss lower bound and stopping condition.
The complete Gram and infinite tail are inherited from NS61; independent
physical integration reuses NS86's exact cells and complete Stirling tail.
No midpoint solves. `check-*.json` includes enclosures of the exact free fit;
the printed ball coefficients are not rounded rational trial coefficients.

At N=16 to M=256 the free lift has rank 96 (full block 240), captures more
than 99.827% of available gain, and reduces old error by more than 55.636%.
The earlier one-direction projected optimum captures about 27.31%. These are
finite comparisons, not a new best error or an asymptotic claim.

Replay from the repository root with Python 3.14, python-flint 0.9.0 and Maxima
5.50.0 (versions used, not a claim that other versions fail):

```sh
python evidence/ns95_square_product/certify.py --bits 256 --sizes 4 8 16 --output evidence/ns95_square_product/check-256bits.json
python evidence/ns95_square_product/certify.py --bits 384 --sizes 4 8 16 --output evidence/ns95_square_product/check-384bits.json
python evidence/ns95_square_product/certify.py --bits 384 --cutoff 256 --sizes 16 --output evidence/ns95_square_product/check-cutoff-384bits.json
python evidence/ns95_square_product/physical.py --bits 256 --input evidence/ns95_square_product/check-256bits.json --sizes 4 8 16 --stop 65536 --output evidence/ns95_square_product/physical-256bits.json
python evidence/ns95_square_product/physical.py --bits 384 --input evidence/ns95_square_product/check-384bits.json --sizes 4 8 16 --stop 65536 --output evidence/ns95_square_product/physical-384bits.json
python evidence/ns95_square_product/physical.py --bits 384 --input evidence/ns95_square_product/check-cutoff-384bits.json --sizes 16 --stop 131072 --output evidence/ns95_square_product/physical-cutoff-384bits.json
maxima --very-quiet -b evidence/ns95_square_product/checks.mac > evidence/ns95_square_product/checks-output.txt
python evidence/ns95_square_product/verify.py
```

Runtime-dependent JSON timing fields need not be byte-identical. The verifier
checks ball overlaps, exact ranks and coefficient constraints, complete physical
norm agreement, dependency bindings, and 12 prior NS86 scalar overlaps.
The doubled Gram cutoff and doubled physical cutoff are distinct checks.
Both numerical runs and the exact rank elimination are fresh.

`turn-review.json` records the required full register review at c679b08.
`dependency-validation.json` checks inherited inventories and selected hashes;
it does not replay every historical calculation. `self-review.json` is an
author review, not an independent review. No new manuscript version or tag.
Both missing historical original-evidence groups remain OPEN.
