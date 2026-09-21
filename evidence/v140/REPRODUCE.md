# NS-5: complete lambda=4 spectral ordering and the ground transform

This is a certified computation using previously archived complete
certificates, not a finite-compression diagnostic. No RH hypothesis or
zero list is used. The new gates take a few seconds because the old
infinite-tail residual enclosures are reused.

Requirements: Python 3, python-flint 0.9.0 (Arb); the complete repository
checkout including evidence/v126/. No NumPy, midpoint solve or numerical
eigensolver is required by the verifier.

From the repository root:

```sh
python3 evidence/v140/certify_ground4.py --bits 1024
python3 evidence/v140/certify_ground4.py --bits 1280
python3 evidence/v140/check_independent.py
python3 tools/verify_manifest.py v140
./manuscript/build.sh
```

Both reports must say `PASS_COMPLETE_SIMPLE_EVEN_GROUND`. At the exact
threshold 1e-73 the 17-dimensional even lower Schur form must have one
negative and 16 positive pivots; the 16-dimensional odd lower form must
have 16 positive pivots. Every pivot excludes zero. The exact finite even
trial in zero-based column16 has complete Rayleigh quotient <2.454e-75.

## Fixed parameters and changes from v1.17

- Window lambda=4; L=2log4; outer head ends at16; normalized parity bases.
- Existing complete tail floor delta=1.7940e-8; no lambda=3 tail constant.
- Existing finite trials supported through4096; no new solve, CG depth,
  preconditioner, support or normalization is introduced.
- Complete relative Schur constants: even62629/100000; odd428/1000.
- Threshold sigma=1e-73; ordinary head/tail Grams computed from exact
  frozen dyadic columns, retaining the head congruence.
- Archived complete ingredients include rows through65536 and the
  order64 infinite remote majorant. These cutoff values belong to the
  existing lambda4 certificates; the new calculation introduces no
  additional tail truncation.
- v1.17 recomputed shifted residuals and inverse weights. Here the exact
  resolvent identity bounds the complete shift directly. Merely subtracting
  sigma times the identity from an unshifted lower matrix would be wrong.

## Inherited inputs and replay scope

`certify_ground4.py` records the SHA256 of the exact inputs used in each
run. They remain in their original evidence/v126/ locations rather than
being duplicated here. The new verifier reconstructs both exact frozen
trial matrices, checks their heads against saved enclosures, and computes
the ordinary Grams afresh. It replays the even relative-margin gate, the
odd K-orthogonal complement gate, the exact rational shared-head check,
and the odd repaired-direction scalar gate. It independently reevaluates
the elementary archimedean tail-floor constant.

The full residual assemblies themselves are inherited theorem inputs:
even at768/896bits; odd complement ingredients at768bits; odd repaired
direction at1024/1280bits. The two new working precisions do not turn the
old768bit odd enclosure into a fresh higher-precision assembly. Full
original assembly scripts and witnesses are in g2_simultaneous/,
g2_odd_complement/ and g2_weighted_signed/ under evidence/v126/.

## Conclusions and limits

The complete selfadjoint W4 has 0<mu0<2.454e-75 and mu1>1e-73, so its
ground is simple, even and isolated with gap>9.7546e-74. The hypotheses
of Connes–van Suijlekom Theorem6.1 are checked in new_section.tex,
including their real distribution on[0,L] and essential selfadjointness
on the trigonometric core. Consequently the entire Fourier transform of
the complete ground has only real zeros.

This is a fixed-window application of an existing external theorem.
It does not assert simple transform zeros, equality or convergence to
Riemann Xi, a cofinal estimate, G2 or RH. No PDF is delivered.
