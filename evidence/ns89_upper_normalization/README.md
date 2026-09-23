# NS89: constructive complete upper certificates

**Classification:** exact optimal-normalization identities and a proved
upper-rate comparison, with certified finite rational witnesses. The
candidate `E_N <= C/log N` remains unproved. No new lower-bound result.
Manuscript stays v1.66.

The user redirected this turn away from another fixed-seed obstruction
test and back to upper bounds. That proposed test was stopped before
publication. The final result is an exact way to require zero exterior
on `x>1` while preserving every possible upper decay rate. The remote tail
near `x=0`, or reciprocal `t=infinity`, is retained in full.

If `E_N^0` is the optimal squared error with `sum c_n/n=0`, then
`E_N^0 = E_N + eta_N^2/q_N`, where `q_N=v^T G_N^-1 v` and `v_n=1/n`.
Projection gives `E_N <= E_N^0 <= E_N/q_N`. Since `q_N` is nondecreasing,
the finite certificate at 256 proves **`E_N^0 <= 1.144579 E_N` for every
N>=256**. This compares two unknown errors; it does not prove decay.

Explicit rational coefficients at N=16,64,256 are in the `check-*.json`
files. They have exactly zero exterior. Their full energies are certified
after rounding; no midpoint inverse enters a proof. At N=256 the rational
trial has squared error about `0.00001414366610575`, and an independent
physical calculation with the complete remote tail proves error
**below `0.000014144`**. This is slightly above the existing unrestricted
optimum, not a new best finite bound. The normalization adds about 0.0088342%
of that optimum.

`argument.tex` gives the projection proof and explicit finite signed
divisor-cell upper certificate. The remaining task is an independent
uniform arithmetic upper estimate for that complete certificate along a
specified coefficient family. Finite fits do not establish it.

Reproduce from the repository root (Python 3.14.6, python-flint 0.9.0):

```sh
.venv/bin/python evidence/ns89_upper_normalization/certify.py --bits 256 --output evidence/ns89_upper_normalization/check-256bits.json
.venv/bin/python evidence/ns89_upper_normalization/certify.py --bits 384 --output evidence/ns89_upper_normalization/check-384bits.json
.venv/bin/python evidence/ns89_upper_normalization/certify.py --bits 384 --cutoff 256 --sizes 256 --output evidence/ns89_upper_normalization/check-cutoff-384bits.json
.venv/bin/python evidence/ns89_upper_normalization/physical.py --bits 256 --input evidence/ns89_upper_normalization/check-256bits.json --output evidence/ns89_upper_normalization/physical-256bits.json
.venv/bin/python evidence/ns89_upper_normalization/physical.py --bits 384 --input evidence/ns89_upper_normalization/check-384bits.json --output evidence/ns89_upper_normalization/physical-384bits.json
.venv/bin/python evidence/ns89_upper_normalization/physical.py --bits 384 --input evidence/ns89_upper_normalization/check-cutoff-384bits.json --stop 524288 --output evidence/ns89_upper_normalization/physical-cutoff-384bits.json
maxima --very-quiet -b evidence/ns89_upper_normalization/exact-checks.mac > evidence/ns89_upper_normalization/exact-checks-output.txt
.venv/bin/python evidence/ns89_upper_normalization/verify_replays.py
pyright evidence/ns89_upper_normalization/*.py
```

The two physical runs share exact rational trial vectors but use an
independent complete physical representation of their error. This is not
independent human or agent review. Twelve Maxima checks verify finite
algebra and antiderivatives, not the missing cofinal estimate. All 96 prior
conclusions were reviewed for scope and dependencies at main `ba02640`;
both historical original-evidence gaps remain open.
