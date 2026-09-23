# NS-85: complete finite logarithmic taper test

Certified finite errors, not a convergence or asymptotic-rate theorem.
The prescribed coefficients are `-mu(n) log(N/n)/log(N)` for every n<=N.
The two controls adjust only c1: either to cancel exterior energy exactly,
or to minimize the complete norm in that one direction. They do not fit all
N coefficients and do not repeat NS-73's projected next-block experiment.

`argument.tex` derives the exact prime-sum interior identity and specifies
the full physical tail. NS-78 supplies the proved cell/tail formulas;
NS-61 supplies complete Gram entries for the one-atom controls. The
Bettin–Conrey–Farmer logarithmic taper is prior art: their Theorem 1 assumes
RH and an inverse-zeta-derivative moment bound. Neither is used here.

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/ns85_taper_test/certify_taper.py --bits 256 --sizes 16 64 256 1024 --cell-stop 65536 --output /tmp/taper-256bits.json
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/ns85_taper_test/certify_taper.py --bits 384 --sizes 16 64 256 1024 --cell-stop 65536 --output /tmp/taper-384bits.json
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/ns85_taper_test/certify_taper.py --bits 384 --sizes 1024 --cell-stop 131072 --kernel-cutoff 256 --output /tmp/taper-cutoff-384bits.json
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python evidence/ns85_taper_test/verify_replays.py
maxima --very-quiet -b evidence/ns85_taper_test/exact-checks.mac
pyright evidence/ns85_taper_test
```

The archived replay checks 64 enclosure pairs, six same-problem quantities
with both cutoffs doubled, and six independent complete-Gram comparisons
at N=16. All 135 exact Maxima checks pass. Printed balls may be wider than
the analytic tail radius because decimal serialization rounds outward.
No finite list of decreasing errors is used to infer a cofinal rate.
Manuscript remains v1.66: this is a continuation record, not a new theorem
version. Original Weil floor, arithmetic approximation convergence, G2 and
RH remain open. Author self-review only.
