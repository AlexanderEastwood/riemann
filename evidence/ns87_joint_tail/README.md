# NS87: joint arithmetic observation tails and complete block gain

**Classification:** exact identities, proved localization consequences of NS81/83,
and certified finite examples. No new arithmetic lower bound or RH proof.
The manuscript remains v1.66.

`argument.tex` derives finite-potential quadrature, the joint tail metric, a safe
correction and polynomial localization at the logarithmic gain scale. The
unconditional polynomial localization does not prove a positive gain at that
scale. Its asymptotic onset is not effective here; its large sufficient cutoff
is not asserted necessary or computationally practical.

The full arithmetic Gram is retained. This is not a fast replacement for its
inverse. The finite physical cutoff is distinct from the analytic Gram cutoff.
Changing the former changes the localized observation problem; changing the
latter replays the same full Gram with a different enclosure.

Replay from the repository root, using Python 3.14.6 and python-flint 0.9.0:

```sh
.venv/bin/python evidence/ns87_joint_tail/certify.py --bits 256 --output evidence/ns87_joint_tail/check-256bits.json
.venv/bin/python evidence/ns87_joint_tail/certify.py --bits 384 --output evidence/ns87_joint_tail/check-384bits.json
.venv/bin/python evidence/ns87_joint_tail/certify.py --bits 384 --sizes 32 --kernel-cutoff 256 --output evidence/ns87_joint_tail/check-cutoff-384bits.json
maxima --very-quiet -b evidence/ns87_joint_tail/exact-checks.mac > evidence/ns87_joint_tail/exact-checks-output.txt
.venv/bin/python evidence/ns87_joint_tail/verify_replays.py
pyright evidence/ns87_joint_tail/certify.py evidence/ns87_joint_tail/verify_replays.py
```

The 14 Maxima checks verify elementary algebra and integration primitives,
not the infinite-dimensional operator theorem. The two potential/physical
representations share the certified coefficients and Gram; they are independent
representations, not an independent human review. Inherited dependencies are
`evidence/v159/ns61`, `evidence/v163/ns78`, `evidence/v164/ns81` and
`evidence/v166/ns83`; current manifests are checked. Known historical missing
originals remain open.

The turn review covers all 93 prior registered conclusions at main 4890f3a.
The self-review records proof scope and computation checks separately.
