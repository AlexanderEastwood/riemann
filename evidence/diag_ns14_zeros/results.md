# NS-14: real zeros of the windowed ground transform vs zeta ordinates — DIAGNOSTIC

> **RETRACTED CONCLUSION (see the end).** The zeros DO track the zeta ordinates —
> to 1.6e-34 at λ=3 — as Connes–Consani–Moscovici report and as this
> repository's own assembly reproduces (`evidence/diag_ns2_semantic_lock/`).
> The "sinc lattice" result below is an eigenvector-accuracy artifact.

**Status: diagnostic, not a certificate.** Ground vectors of the N=256 even
compression at λ=3,4 by inverse iteration (768-bit assembly, 120 digits;
Rayleigh quotients 2.73e-38 and 2.83e-75, consistent with the certified
bounds). Transform `ξ̂_λ(z) = ∫ ξ_λ(x) e^{-izx} dx` over the window, in the
orthonormal basis `e_0 = 1/√L`, `e_n = √(2/L) cos(2πnx/L)`; real zeros on
`(0,120]` by sign scan (Δz = 0.01) and bisection.

## Result: the zeros are the sinc lattice, not zeta zeros

| λ | L | zeros of ξ̂_λ in (0,120] | zeta ordinates < 120 | mean spacing of ξ̂ zeros | 2π/L | mean zeta spacing |
|--:|--:|--:|--:|--:|--:|--:|
| 3 | 2.197 | 41 | 38 | 2.889 | 2.860 | 2.829 |
| 4 | 2.773 | 52 | 38 | 2.285 | 2.266 | 2.829 |

The zeros are equally spaced at the **lattice period 2π/L**. At λ=3 that
period happens to be close to the mean zeta spacing below 120, producing
accidental near-coincidences (14.300 vs 14.135; 25.736 vs 25.011); at λ=4
the spacing is 2.27 against zeta's 2.83, and there are 52 zeros against 38.
Nothing tracks.

## Why — an exact factorization

For any window function in this basis,

    ξ̂(z) = sin(zL/2) · R(z),
    R(z) = 2v_0/(√L z) − √(2/L) Σ_{n≥1} (−1)^n v_n · 2z/(ω_n² − z²),   ω_n = 2πn/L.

`sin(zL/2)` vanishes at every lattice point `ω_k`; `R` has a pole at `ω_n`
exactly when `v_n ≠ 0`, which cancels the zero there. So ξ̂ vanishes at every
lattice point where the ground vector has negligible weight. Since the ground
state has 90% of its mass at `n ≤ 2` and 100% at `n ≤ 8` (energy-budget
diagnostic), the zeros for `n ≳ 5` sit on the lattice to 3–4 digits
(λ=3: 14.300 vs ω_5 = 14.298; 17.165 vs ω_6 = 17.157; 20.018 vs ω_7 = 20.017),
and only the first four are displaced by the low modes (1.68, 5.01, 8.25,
11.35 vs 2.86, 5.72, 8.58, 11.44).

## Consequence for CCM step (b)

Convergence of the zeros of ξ̂_λ to zeta zeros (CCM arXiv:2511.22755 §8, the
second missing step) requires `R` to acquire zeros away from the lattice,
i.e. the ground state to spread over many Fourier modes as λ grows. Measured
`n90` (mode index holding 90% of the mass): 2, 2, 3, 3 at λ = 3, 4, 6, 8.
It is barely moving. At the windows where step (a) is certified (NS-5), there
is no sign of step (b) beginning. This is a finding about *where the
difficulty sits*, not a negative result about CCM's conjecture, which is an
asymptotic statement.

Caveat: the compression ground is used in place of the certified complete
ground; they agree on μ0 to within the bound and share the same low-mode
structure, and the zero positions depend only on the converged low-mode
ratios `v_n/v_0`.

---

## RETRACTION (later the same day)

The conclusion above is wrong. With a proper eigensolve (N=120, 1024-bit
assembly, 220-digit eigensolve — `evidence/diag_ns2_semantic_lock/reproduce_ccm.py`,
re-run independently), the first zeros of `ξ̂_3` sit on the zeta ordinates:

    k   γ_k          |γ_k − z_k|      CCM Fig. 1
    1   14.134725    1.58e-34         1.6e-34
    2   21.022040    2.06e-31         2.1e-31
    3   25.010858    1.46e-29         1.5e-29
    4   30.424876    8.29e-27         8.3e-27
    5   32.935062    1.28e-25         1.3e-25
    6   37.586178    1.17e-23         1.2e-23

The ground vector used above came from four steps of inverse iteration at 120
digits — accurate to ~1e-14 relative. The zero positions of `ξ̂` are sensitive
at the 1e-8 level (`sensitivity.py`: a 1e-8 prime-weight change moves the first
difference from 1e-33 to 1e-7 and creates spurious zeros), so the noise floor of
that vector erased the tail that places the zeros, and the sin(zL/2) lattice
came through instead. The exact factorization `ξ̂ = sin(zL/2)·R(z)` stands; its
correct reading is the opposite of the one given: the *tiny* high-index tail of
the ground vector is exactly what moves the zeros of `R` off the lattice onto
the zeta ordinates, to dozens of digits. "n90 = 2" was the wrong metric.

Corrected consequence for CCM step (b): it is numerically *happening* at every
window tested (λ = 3, √12, √13, √14 in `diag_ns2_semantic_lock`, and the
certified simple-even ground at λ=4 is the same object). What is unproved is
the convergence theorem, not the phenomenon.
