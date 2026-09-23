# NS-86: optimized arithmetic potential and a convolution correction

Exact identities, a proved complete observation-tail estimate, and certified
finite computations. The aggregate asymptotic gain remains an open input.

`argument.tex` gives the complete integral-minus-sum form of the optimized
normal equations, including the joint cutoff required by the logarithmic
tail. It proves a bound on the discarded observation tail and an exact
cancellation of its shared log-moment. This uses the classical Müntz
operator; it is not a new RH criterion or an arithmetic lower bound.

The tested coefficient rule is `q = 2c + 1*c*c`, truncated at `N^2`, with
Dirichlet convolution and the actual optimized old coefficients. Its divisor
defect equals the convolution square of the old defect through `N^2`.
This is not pointwise squaring or an energy contraction. Complete unit-step
errors at N=4,8,16 are respectively about 39.60, 0.478, and 29.55 times the
old error. The optimally damped direction, after refitting all old
coefficients, captures 84.94%, 84.94%, and 27.31% of available gain.
Damping and refitting generally change the exact convolution-square identity.

The original and NS74 altered families are distinguished explicitly. The
coefficient identity is common algebra, but the original physical divisor
identity is not claimed for altered atoms. No asymptotic failure of the
original family or of all nonlinear correction rules is proved.

## Replay

Run from the repository root with the pinned `python-flint==0.9.0` environment.
Use fresh output paths if preserving an earlier run; the commands below
generate the named current artifacts for an isolated replay checkout.

```sh
.venv/bin/python evidence/ns86_optimized_arithmetic/certify_newton.py --bits 256 --sizes 4 8 16 --output evidence/ns86_optimized_arithmetic/newton-256bits.json
.venv/bin/python evidence/ns86_optimized_arithmetic/certify_newton.py --bits 384 --sizes 4 8 16 --output evidence/ns86_optimized_arithmetic/newton-384bits.json
.venv/bin/python evidence/ns86_optimized_arithmetic/certify_newton.py --bits 384 --sizes 16 --cutoff 256 --output evidence/ns86_optimized_arithmetic/newton-cutoff-384bits.json
.venv/bin/python evidence/ns86_optimized_arithmetic/certify_physical.py --bits 256 --input evidence/ns86_optimized_arithmetic/newton-256bits.json --output evidence/ns86_optimized_arithmetic/physical-256bits.json
.venv/bin/python evidence/ns86_optimized_arithmetic/certify_physical.py --bits 384 --input evidence/ns86_optimized_arithmetic/newton-384bits.json --output evidence/ns86_optimized_arithmetic/physical-384bits.json
.venv/bin/python evidence/ns86_optimized_arithmetic/certify_physical.py --bits 384 --input evidence/ns86_optimized_arithmetic/newton-cutoff-384bits.json --cell-stop 131072 --output evidence/ns86_optimized_arithmetic/physical-cutoff-384bits.json
maxima --very-quiet -b evidence/ns86_optimized_arithmetic/exact-checks.mac > evidence/ns86_optimized_arithmetic/exact-checks-output.txt
.venv/bin/python evidence/ns86_optimized_arithmetic/verify_replays.py
pyright evidence/ns86_optimized_arithmetic
```

Validation covers 156 scalar, 728 coefficient and 144 potential comparisons
between precisions; 58 same-problem comparisons after cutoff changes;
14 physical/Gram norm comparisons; 56 potential/Gram pairing comparisons;
and 82 exact Maxima checks. Decimal serialization may widen displayed balls
beyond their separately recorded analytic tail radii.

Review is local author review with independent numerical representations,
not an independent human proof audit. No new manuscript version or version
tag is created. Both original missing-evidence groups remain open.
