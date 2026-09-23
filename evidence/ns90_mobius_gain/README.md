# NS90: direct attempt at the PR42 arithmetic lower gain

**Classification:** exact identity and a proved fixed-size implication,
with certified finite tests. **No cofinal lower gain obtained.**

The selected Mobius/logarithmic direction is inherited from NS73. This
attempt tests whether its numerator can be lower-bounded analytically;
it does not repeat its known finite efficiency as new progress.

Using old-space orthogonality cancels the two prime main terms exactly.
The numerator equals `(log 2) E_N` minus a **joint signed compensator**:
exterior normalization, a finite divisor sum, and a complete pairing tail.
All three are retained in [argument.tex](argument.tex).

At N=16 and 256 the full numerator is positive and overlaps the archived
full-Gram calculation. The tested termwise absolute-value lower bound is
negative. At N=256 it is below `-186 E_N` at T=262144 and below `-226 E_N`
at T=524288. The individual finite summands depend on T and must not be
compared as cutoff invariants. These are not the asymptotic cutoffs N^6.
Dropping the finite divisor forcing even gives the wrong sign at these
sizes. Neither observation excludes the signed direction.

The proof explains a more general fixed-size issue: if the residual's
logarithmic or constant tail is nonzero, the absolute divisor allowance
diverges as T grows, although the signed expression converges. The actual
tail slopes are certified nonzero at the two tested sizes. This does not
supply constants uniform in N or exclude a different bound at T=N^6.

The main route remains NS87/PR42: prove a cofinal lower estimate for the
**full joint signed arithmetic observation energy**. This selected scalar
attempt has not done so. Its true projected cost is inherited from NS73;
no smaller model or unprojected cost is substituted. RH/G2 remain open.
Manuscript remains v1.66; there is no new version tag.

## Reproduce

From the repository root, with Python 3.14.6 and python-flint 0.9.0:

```sh
.venv/bin/python evidence/ns90_mobius_gain/certify.py --bits 256 --input evidence/ns89_upper_normalization/check-256bits.json --reference evidence/v161/ns73/mobius-256bits.json --output evidence/ns90_mobius_gain/check-256bits.json
.venv/bin/python evidence/ns90_mobius_gain/certify.py --bits 384 --input evidence/ns89_upper_normalization/check-384bits.json --reference evidence/v161/ns73/mobius-384bits.json --output evidence/ns90_mobius_gain/check-384bits.json
.venv/bin/python evidence/ns90_mobius_gain/certify.py --bits 384 --stop 524288 --sizes 256 --input evidence/ns89_upper_normalization/check-cutoff-384bits.json --reference evidence/v161/ns73/mobius-cutoff-replay-384bits.json --output evidence/ns90_mobius_gain/check-cutoff-384bits.json
maxima --very-quiet -b evidence/ns90_mobius_gain/exact-checks.mac > evidence/ns90_mobius_gain/exact-checks-output.txt
.venv/bin/python evidence/ns90_mobius_gain/verify_replays.py
pyright evidence/ns90_mobius_gain/*.py
```

Verification: 38 precision scalar overlaps, 8 complete cutoff overlaps,
5 archived numerator overlaps, and 15 exact Maxima sanity checks. All
five finite runs give a positive complete numerator, negative elementary
lower bound, and wrong sign when the finite divisor sum is omitted.
Source hashes bind every inherited coefficient/cost file and fresh script.
The NS161 manifest (32 entries) and NS89 inventory (21 entries) passed;
original Gram solves were not rerun. Review was by the author only.
The 358-page unchanged manuscript builds with zero undefined/duplicate
references. All 97 prior conclusions were reviewed at main 0a11971 for
scope and dependencies; both historical missing-original groups stay open.
