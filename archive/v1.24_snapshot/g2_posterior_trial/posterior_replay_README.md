# Complete directional certificate replay

Use the cumulative bundle with its original directory layout. The files below are in g2_posterior_trial; prior exact inputs remain in g2_low_schur and g2_weighted_signed.

Runtime used: Python with python-flint 0.9.0 (Arb ball arithmetic). The scripts regenerate coefficient caches when absent; caches are reproducible and are not included in this compact addition.

From the bundle root run:

```sh
python g2_posterior_trial/posterior_trial.py --mode verify --M 4096 --steps 16 --bits 768
python g2_posterior_trial/posterior_trial.py --mode verify --M 4096 --steps 16 --bits 896
```

The --mode verify switch uses the archived frozen dyadic trial; it does not regenerate the numerical proposal. The proof gate must report PASS_COMPLETE_DIRECTION and includes all rows beyond J=65536. The four-step supplementary trial can be checked by replacing `--steps 16` with `--steps 4`.

A pass concerns the one specified even head vector. It is not a positive-matrix certificate, growing-window estimate, or RH proof.
