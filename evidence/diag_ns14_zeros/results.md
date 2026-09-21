# NS-14: real zeros of the windowed ground transform vs zeta ordinates — DIAGNOSTIC

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
