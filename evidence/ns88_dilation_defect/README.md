# NS88: multiplicative normal equations and whole-error upper bounds

**Classification:** exact identities, proved upper envelopes and a scoped
numerator obstruction, plus certified finite checks. No cofinal arithmetic
lower estimate, logarithmic whole-error upper rate, G2 or RH is proved.
Manuscript remains v1.66.

`argument.tex` identifies the dilation defect as an overlap of successive
orthogonal increments. It gives a next-size upper-error certificate and a
cumulative whole-error envelope. A lower growth estimate for its scalar sum
would imply a logarithmic upper rate; this arithmetic input remains open.
The generic envelope can be much weaker than directly optimized finite bounds.

The first cell gives an exact short formula for P_N(2). `physical.py`
independently integrates both the complete potential and autocorrelation,
retaining explicit Stirling remainders and every cross term. It shares the
certified coefficients with the Gram calculation; this is an independent
representation, not an independent human or agent proof audit.

Reproduce from the repository root with Python 3.14.6 / python-flint 0.9.0:

```sh
.venv/bin/python evidence/ns88_dilation_defect/certify.py --bits 256 --output evidence/ns88_dilation_defect/check-256bits.json
.venv/bin/python evidence/ns88_dilation_defect/certify.py --bits 384 --output evidence/ns88_dilation_defect/check-384bits.json
.venv/bin/python evidence/ns88_dilation_defect/certify.py --bits 384 --sizes 64 --cutoff 256 --output evidence/ns88_dilation_defect/check-cutoff-384bits.json
.venv/bin/python evidence/ns88_dilation_defect/physical.py --bits 256 --input evidence/ns88_dilation_defect/check-256bits.json --output evidence/ns88_dilation_defect/physical-256bits.json
.venv/bin/python evidence/ns88_dilation_defect/physical.py --bits 384 --input evidence/ns88_dilation_defect/check-384bits.json --output evidence/ns88_dilation_defect/physical-384bits.json
.venv/bin/python evidence/ns88_dilation_defect/physical.py --bits 384 --input evidence/ns88_dilation_defect/check-cutoff-384bits.json --stop 131072 --output evidence/ns88_dilation_defect/physical-cutoff-384bits.json
maxima --very-quiet -b evidence/ns88_dilation_defect/exact-checks.mac > evidence/ns88_dilation_defect/exact-checks-output.txt
.venv/bin/python evidence/ns88_dilation_defect/verify_replays.py
pyright evidence/ns88_dilation_defect/certify.py evidence/ns88_dilation_defect/physical.py evidence/ns88_dilation_defect/verify_replays.py
```

The Maxima worksheet checks 13 scalar algebra/integration identities. It
does not machine-prove the infinite-dimensional theorem or the asymptotic
implication. Inherited analytic inputs are the complete kernel in v159,
physical cells/Stirling remainder in v163 (from NS67/78), and the critical-zero
lower bound in v166. Both historical original-evidence gaps remain open.
All 94 prior registered conclusions were reviewed at main 99640fe.
