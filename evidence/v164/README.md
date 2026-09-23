# v1.64 evidence: ordinary conditioning and a finite arithmetic comparator

Incremental NS81 evidence only. The huge sufficient comparator is not assembled.
The proved ordinary positive-Gram bound is not a signed Weil spectral floor,
not a bound on approximation error, and not RH/G2. Local self-review only.

The certified script assembles only prefix cells 1..N with the final sample
at N+1, for N=16,64,256. Positive definiteness follows from exact coefficient
inversion. A complete Arb inverse gives tr(P_N^-1)<C_N at these sizes,
confirming the analytic ordinary prefix floor without midpoint solves.
The all-size theorem does not require that stronger finite trace test to
succeed at every larger size. The remaining outputs evaluate a complete
analytic discarded-tail bound at the large sufficient cutoff; they do not
sum the enormous comparator or substitute a finite zero prefix.

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v164/ns81/certify_conditioning.py --bits 256 --sizes 16 64 256
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v164/ns81/certify_conditioning.py --bits 384 --sizes 16 64 256
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/v164/verify_replays.py
pyright evidence/v164
./manuscript/build.sh
python3 tools/verify_manifest.py v164
```

The Maxima file must report 18 exact checks. There is no numerical tail cutoff
in the small prefix calculation: every specified term is evaluated, while the
full discarded infinite tail is handled by the proved scalar operator bound.
The NS80 efficiency argument then applies with condition ratio 42. This
removes the unspecified infinite inverse in principle, but the cutoff is
impractical and no cofinal gain or decay estimate follows.
