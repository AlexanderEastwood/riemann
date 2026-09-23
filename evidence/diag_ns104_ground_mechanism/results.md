Diagnostic of the frozen finite trial, not a new complete-ground certificate.

# NS104: what the archived ground check does and does not explain

The stated prediction is **supported for the archived finite trial**: its
transform is tiny at all 64 tested zeta ordinates, with opposite signs at
each pair of endpoints gamma_j +/- 0.01. This does not identify the cause of
the small Rayleigh quotient, establish the pattern for the complete ground,
or turn a proximity bound into a measured displacement.

Pre-registration: draft [PR57](https://github.com/AlexanderEastwood/riemann/pull/57),
commit `0513e84`, preceded the NS104 claim at `605bbe7` and the scan.
The unchanged proposal is in `PROPOSAL.md`. No new version or theorem node.

## Object and replay

We evaluate the normalized exact column 16 of the even 4097-row trial in
`evidence/v126/g2_simultaneous/simultaneous_even_M4096_s16_normalized_witness.json.gz`.
This is the same f used in v1.42/1.43. It is **not** a saved infinite
eigenfunction. Every cosine coefficient (modes 0 through 4096) is included.
The complete ground xi_4 is accessed in the earlier certificates through
its projection h=P_(xi_4)f and energy estimates.

Arb evaluations at 1024 and 1280 bits agree; serialized intervals overlap
for every paired numerical field. The Rayleigh enclosure is inherited from
the saved complete residual ingredients at 768 and 896 bits, respectively;
those assemblies are not recomputed. There is no new cutoff, eigensolve or
omitted finite-coefficient remainder. Dependency hashes are in both reports.

```
.venv/bin/python evidence/diag_ns104_ground_mechanism/evaluate_trial.py --bits 1024 --output /tmp/ns104-fresh-1024.json
.venv/bin/python evidence/diag_ns104_ground_mechanism/evaluate_trial.py --bits 1280 --output /tmp/ns104-fresh-1280.json
.venv/bin/python evidence/diag_ns104_ground_mechanism/validate_results.py
```

Use fresh output paths. The diagnostic stops at 64 ordinates as registered.

## Observations

Write F=widehat(f) and rho=q_W[f], with
rho = 2.45361754930714...e-75. The complete eigenvalue satisfies
0 < mu_0 <= rho; **rho is not a measured value of mu_0**.
The table shows display approximations, not additional root enclosures.

| j | gamma_j | abs(F(gamma_j)) | F'(gamma_j) | linearized shift -F/F' |
|---|---:|---:|---:|---:|
| 1 | 14.13472514 | 1.06412e-40 | 3.10869e-3 | -3.42306e-38 |
| 2 | 21.02203964 | 1.64476e-40 | -5.42615e-5 | -3.03117e-36 |
| 3 | 25.01085758 | 2.50187e-41 | 4.88381e-6 | 5.12277e-36 |
| 10 | 49.77383248 | 3.32304e-44 | -6.40098e-13 | 5.19146e-32 |
| 29 | 98.83119422 | 1.38694e-42 | 1.31914e-24 | 1.05140e-18 |
| 32 | 105.44662305 | 6.66414e-42 | -2.65060e-26 | 2.51420e-16 |
| 48 | 139.73620895 | 5.64238e-41 | -8.91357e-33 | 6.33010e-9 |
| 64 | 169.91197648 | 9.17068e-41 | -7.00686e-37 | 1.30881e-4 |

All 64 endpoint pairs have opposite signs. This gives nearby trial roots
by continuity, but no uniqueness or sharper root-displacement certificate
is supplied. One Newton step is also evaluated; it is not a root enclosure.
Tiny values alone do not imply uniformly tiny root displacements: the
slopes decrease sharply. The largest linearized displacement is about
1.77081e-4 at j=63.

The largest abs(F(gamma_j))/sqrt(rho) is 0.00332047 (rounded upward), at j=2.
The formal two-sided partial sample sum 2 sum_(j<=64) F(gamma_j)^2 / rho is
0.0001018608892.... It is **not claimed to be an energy fraction**: no
complete zero-side representation with a nonnegative omitted remainder is
established here. In particular, this number does not prove that the rest
of the energy comes only from zeros above a crossover.

At j=1, sqrt(rho)/abs(F') is 1.59340587e-35, about 465.49 times the
linearized displacement 3.42306343e-38. Thus the suggested scale is not an
observed equality for this trial. Since mu_0 itself is not determined, this
comparison neither proves nor refutes a proposed asymptotic law for the
complete ground. The earlier finite N=120 discrepancy is a different object.

## Three corrections to the proposed interpretation

### Window convention and the proposed crossover

The manuscript's lambda=4 is multiplicative: support is
[-log 4, log 4], and L=2 log 4. NS103 uses the same letter for the
**logarithmic half-width**, support [-lambda,lambda]. On converting its
heuristic 2 pi exp(2a) to a=log 4, the value is 32 pi = 100.5309649...,
between gamma_29 and gamma_30, not 2 pi exp(8). The trial pattern continues
past that value through gamma_64; a hard cutoff reading is not supported.

NS103's four detection windows are first detected points on its chosen
finite basis/grid and threshold. They are not proved minimum support
sizes or a universal detection law. Compact support in physical space does
not give compact support of the entire Fourier transform in frequency.
An effective bandwidth count is not the dimension of the full
Paley-Wiener space, which is infinite dimensional. Counting finite zero
constraints alone does not identify a minimizer or bound the residual tail.
No sharp zero-height interpretation of fixed-window positivity is proved.
The relation of the explicit-formula conventions must be checked on the
same tests before transferring a numerical threshold; calling one object
"semilocal" does not by itself settle that comparison.

The fixed-window results establish positivity, spectral structure and
ground-transform zeros. They do not verify a new height of zeta zeros or
establish cofinal convergence. The cutoff-cost theorem is for its specified
scalar majorant, not a universal lower bound on every possible method.

### The 9e-33 bound is already an energy/evaluator bound

v1.43 proves abs(ell(v))^2 <= C_ell q_W[v] using the complete Schur
comparison, with C_ell = 79920.06156776.... For h=P_(xi_4)f and the
certified derivative lower bound d=0.0016, it obtains

    abs(z_1(4)-gamma_1) <= sqrt(C_ell rho)/d = 8.75208157...e-33.

Thus the connection between the energy upper budget and the proximity
upper budget was already part of the certificate. The radius is not an
observed displacement; its interval includes zero. Replacing C_ell by 1
requires an additional argument. Dropping the rest of a zero sum is not
justified without its nonnegativity: off-line pairs contribute signed cross
products. Global nonnegativity of the W4 form does not make each zero
contribution nonnegative. No RH assumption is used in the Schur argument.

The existing coarse transfer bound is norm(f-h) <= sqrt(rho/1e-67), about
1.5664e-4. Its transform and derivative allowances are about 2.60823e-4 and
2.08757e-4. The latter already exceeds abs(F'(gamma_2))=5.42615e-5.
Consequently those displayed bounds do not transfer this scan's later
trial roots to the complete ground. This is a limitation of the available
bounds, not proof that the complete pattern fails or cannot be certified.

No Davenport-Heilbronn complete ground, matched Rayleigh bound or projection
certificate is present. Its proposed analogous proximity remains untested.
The unchanged `example_screen.py` run in `control-sanity.json` checks the
control implementation, not this ground prediction. The actual prediction
is marked not-applicable to that unmatched archive; no positivity implication
is being admitted through this exception. NS100/101 have the same mismatch.

### A uniform negative floor need not resolve tiny positive energies

v1.36 asks for q_a[f] >= -C norm(f)^2 with one finite C on the complete
admissible domains cofinally. It does not ask for an error smaller than
each positive eigenvalue. A uniform absolute remainder bound can suffice
even when it exceeds a tiny positive energy. Resolving that energy's sign
is a stronger task. No finite list of numerical windows proves a cofinal
bound, but that is different from saying the floor must numerically resolve
all near-null directions. NS46's obstruction to a positive spectral gap
does not obstruct this weaker negative-floor target. The full parity,
source, prime, pole, exterior and cross-term obligations remain in place.

## Review and disposition

Reviewed main `d92264127a6bf40cbfb85899e1db676576457546`, including all
104 conclusion nodes, the 14 continuation groups, current checkpoints,
board, evidence ledger and changed NS103 claims. Node objects are unchanged
from the prior reviewed main `a47d8a1`; the affected continuation summary is
corrected forward. This is a conclusions/dependency and interpretation
review, not a replay of all historical proofs. Both missing-original groups
remain OPEN. Local author review only; no independent reviewer is claimed.

**Wall check: Distinct test** of the stated finite-trial prediction;
**Same open gap** for CCM-LIMIT and WEIL-FLOOR. Closest: NS43/46,
v1.40–1.43, NS103. The observation supports a near-zero pattern but does not
prove a null-space mechanism, convergence, an energy-tail law or a new
arithmetic estimate. No frozen family is thawed. Stop at the registered
diagnostic; any complete-ground extension needs its own explicit transfer
estimate and control assessment before another row is claimed.
