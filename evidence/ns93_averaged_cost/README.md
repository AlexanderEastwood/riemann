# NS93: averaged cost attempt

Classification: exact finite identities, proved scoped majorant obstruction,
certified finite computations, and two open averaged arithmetic inputs.
No cofinal gain, new best error, or RH claim.

See `argument.tex` and `../../audits/averaged-arithmetic-cost-2026-09-23-v1.html`.
The diagonal of S is uniformly bounded; signed off-diagonal cancellation is
still unestimated. The absolute-product majorant grows at least linearly,
so averaging cannot prove bounded cost by that particular separation.

Replay from the repository root:

```sh
python evidence/ns93_averaged_cost/check_cost.py --bits 256 --output evidence/ns93_averaged_cost/cost-256bits.json
python evidence/ns93_averaged_cost/check_cost.py --bits 384 --output evidence/ns93_averaged_cost/cost-384bits.json
python evidence/ns93_averaged_cost/check_cost.py --bits 384 --sieve-multiplier 2 --output evidence/ns93_averaged_cost/cost-sieve-replay.json
maxima --no-init --very-quiet --quit-on-error --batch=evidence/ns93_averaged_cost/checks.mac > evidence/ns93_averaged_cost/checks-output.txt
maxima --no-init --very-quiet --quit-on-error --batch=evidence/ns94_circle_inversion/checks.mac > evidence/ns94_circle_inversion/checks-output.txt
python evidence/ns93_averaged_cost/verify.py
```

There is no physical cutoff: these are exact finite scalar sums. Independent
quadratic expansions check N16/32/64; the doubled sieve checks table limits.
Original Mobius implementation is bound by hash. The author reviewed the
analytic squarefree count and constants; Maxima checks finite algebra only.
The sufficient averaged criterion is prior descent plus Cauchy-Schwarz,
not new arithmetic content. Both historical evidence gaps remain open.
