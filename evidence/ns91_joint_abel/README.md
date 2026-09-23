# NS91: joint first-primitive grouping

Classification: exact identities, proved complete-tail inequalities, and certified finite computations. The cofinal arithmetic lower-gain input remains open.

This integrates the separately preserved September 23 standalone draft after the approval-service failure resolved. NS91 was claimed in commit cc8528d before repository edits. The manuscript remains v1.66.

The first primitive combines the signed compensator before taking absolute values. Removing the old-space term Ns a_N makes it vanish on 0<t<N without changing the gain numerator or true projected cost. Fixed dyadic grouping then gives a positive lower numerator at N16,64,256, including the sum of absolute values of all omitted dyadic integrals. The N256 lower relative gain exceeds 0.02821 (0.02822 at the doubled cutoff). This is a certificate for an already known NS73 direction, not a new best finite error.

The complete grouped tail is negligible at T=N^6. The new continuation check also shows exactly why the proposed quadratic rewrite does not prove a sign: NS78 inversion plus the normal equations leaves beta squared times the original numerator. This is a limit of that inference, not a closure of the arithmetic approach.

No uniform finite interior margin or projected-cost estimate is proved. Both historical original-evidence gaps remain open.

## Reproduction

From this directory, use Python with python-flint==0.9.0. Repository inputs are located relative to the script; optional --repo selects another checkout with the same archives.

```sh
python check_grouping.py --bits 256 --output check-256bits.json
python check_grouping.py --bits 384 --output check-384bits.json
python check_grouping.py --bits 384 --stop 524288 --cutoff-replay --output check-cutoff-384bits.json
python check_grouping.py --bits 256 --endpoint-normalize --output endpoint-256bits.json
python check_grouping.py --bits 384 --endpoint-normalize --output endpoint-384bits.json
python check_grouping.py --bits 384 --stop 524288 --cutoff-replay --endpoint-normalize --output endpoint-cutoff-384bits.json
maxima --very-quiet -b exact-checks.mac > exact-checks-output.txt
python verify.py
```

The script uses original NS89 optimized interval coefficients and NS73's full projected costs. Its old numerator is used only for validation after calculating the new bound. No original Gram solve was rerun. Two precisions and doubled physical/inherited Gram cutoffs were replayed in this branch. The full proof is author work; 32 Maxima checks cover finite algebra and antiderivatives only. No independent human or agent review is claimed.

See argument.tex, validation.json, dependency-validation.json, self-review.json, turn-review.json, and ../../audits/joint-abel-research-2026-09-23-v2.html. All archived new files and the report are bound by inventory.json.
