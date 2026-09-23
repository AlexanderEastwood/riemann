# NS92: direct arithmetic cost budget and endpoint-only step

Classification: exact coefficient identity, proved complete cost upper bounds, certified finite steps, and explicitly open uniform inputs. No cofinal lower-gain theorem.

This applies NS61's full-space average to NS73's signed Mobius/log-taper suffixes. The resulting scalar budget U_N upper-bounds the true projected cost and the norm of a feasible direction that corrects only the old coefficient at N. No new-block inverse is required. The actual starting optimized old coefficients remain inherited inputs.

At N256 the scalar budget is below 0.001063 and guarantees more than 0.0443% relative error decrease for the fixed step 1/512. Independent complete physical integration supplies a sharper norm and certifies more than 1.57% decrease for the step 1/16. These are weaker than full refitting; no new best error or cofinal percentage is claimed.

Seven scalar budgets through N65536 lie between 0.00098 and 0.00220. This is a finite screen, not an eventual bound. Partial summation shows that the elementary bound supplies only O(N) growth; the compatible uniform cost and signed numerator estimates remain open. Both historical evidence gaps remain open. Manuscript v1.66 is unchanged.

## Reproduction

From this directory with python-flint==0.9.0:

```sh
python certify_cost.py --bits 256 --output cost-256bits.json
python certify_cost.py --bits 384 --output cost-384bits.json
python certify_cost.py --bits 384 --sizes 256 --cutoff-replay --output cost-cutoff-384bits.json
python physical_step.py --bits 256 --output physical-256bits.json
python physical_step.py --bits 384 --output physical-384bits.json
python physical_step.py --bits 384 --stop 524288 --cutoff-replay --output physical-cutoff-384bits.json
maxima --very-quiet -b exact-checks.mac > exact-checks-output.txt
python verify.py
```

Scalar sums have no truncation tail. Physical calculations retain every unit cell, the old residual exterior, and the entire remote tail with mixed terms. The inherited Gram cutoff replay changes the old coefficient enclosures, not the finite scalar cost problem. No new Gram solve was performed. The inherited true cost and numerator are used only to validate inequalities/overlaps. All input and script hashes are checked.

The 16 Maxima checks cover finite algebra only. Mathematical review is local author review, not independent review. The complete derivation is argument.tex; validation.json records the replays. See ../../audits/arithmetic-cost-step-2026-09-23-v1.html for the readable report.
