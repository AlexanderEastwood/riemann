# NS-21 lobe-mass test against the level surplus -- DIAGNOSTIC, NOT A CERTIFICATE

**Status: diagnostic, not a certificate. Float quadrature, N=48 finite section,
midpoint pencil. No bound is claimed. The candidate lemma tested here is killed
by a counterexample (section 5); the replacement statement in section 6 is a
PROPOSAL, not a result.** Plain-ASCII math throughout.

Board row: NS-21. Scripts: `lobe_mass.py` (this directory). Output:
`lobe_mass_output.txt` (all four windows, every lobe), `lobe_mass_l{3,4,6,8}.json`.
Run from the repo root with `.venv/bin/python evidence/diag_lobe_mass/lobe_mass.py`
(cases as `lam,N,bits,dps`; `--pool` re-prints from the JSON files).

## 1. Question

Section 6 of `evidence/diag_true_symbol/results.md` found that the negative lobe of
the symbol beta_a nearest the first zeta ordinate gamma_1 = 14.1347 deepens with the
window while the ground's Fourier mass there falls. Section 7 gave the level pencil
W v = nu (W + W^-) v on the even head, whose vectors v_k order the head by the
surviving positive-level surplus nu_k = q[v_k]/q+[v_k] (1e-105 .. 1e-2). The
candidate inequality to test:

    (A)  mass_k(lobe) <= C * nu_k,          mass_k(I) = 2 int_I |F v_k|^2 dxi,  ||v_k||_2 = 1
    (B)  mass_k(lobe) <= C * sqrt(nu_k)
    (C)  max over negative lobes I of mass_k(I) <= C * nu_k

for k = 0..5, lambda = 3, 4, 6, 8, even head N = 48 (bits 1024/1024/2048/2048), with
"lobe" = (a) the negative interval of beta_a nearest gamma_1 (the rule of
`nearzero.py`: the interval containing the grid point nearest gamma_1, else the nearer
flanking one) and (b) every negative lobe of beta_a in xi < 60. Also computed: the
negative-level energy E_k(I) = 2 int_I beta_a |F v_k|^2 in each lobe.

Method. The pencil is rebuilt exactly as in `pencil.py` (W from Arb `block()`, W^- from
float quadrature of beta_a^- on the grid to xi = 4000, Cholesky pencil in mpmath at
dps = 120 / 120 / 180 / 180). Pencil vectors are v_k = C^{-T} u_k, normalised to
||v_k||_2 = 1 so that int |F v_k|^2 = 1 (the zero-extended even modes are orthonormal
and F is unitary), moved to the transform with the (-1)^n of `pencil.py` / `nearzero.py`
(`sgn`). Lobes are found on a grid of step 0.001 on (0, 60); masses and energies are
trapezoid sums on that grid. Everything is in double precision after the pencil; entries
below about 1e-30 (high lobes at lambda = 8) are at the floating-point floor of the
transform sum and carry no information.

Checks. nu_0..nu_5 reproduce `pencil_output.txt` (dps 120) at every lambda, including
nu_0 = 6.31e-92 (lambda 6) and 1.47e-105 (lambda 8) at dps 180, so the pencil is
precision-stable at these sizes. At lambda = 3, 4 the ground's gamma_1-lobe mass and
energy reproduce `nearzero_output.txt` (N = 120): 1.544e-4 / -5.57e-5 and 9.63e-7 /
-3.29e-7 against 1.54e-4 / -5.56e-5 and 1.10e-6 / -3.74e-7. At lambda = 6, 8 the N = 48
head is not converged (section 7 of `diag_true_symbol`): 2.36e-7 and 7.84e-8 here
against 5.52e-7 and 3.46e-7 at N = 120. A factor 2-4 in a quantity that is off by
1e85-1e98 from the candidate bound does not affect anything below. The sanity
assertion that v_k^T W v_k / v_k^T W+ v_k equals nu_k passed in every run. The
Plancherel mass on [0, 60) is 1.000000 for all 24 directions (nothing of these deep
directions lives beyond xi = 60).

## 2. The lobe nearest gamma_1, k = 0..5

Lobe geometry (identical to `nearzero.py`, as it must be):

| lambda | L | cell 2pi/L | u(gamma_1) | lobe | centre | depth | width | width/cell |
|--:|--:|--:|--:|:--|--:|--:|--:|--:|
| 3 | 2.197 | 2.860 | 4.94 | [11.552, 12.810] | 12.290 | -0.668 | 1.258 | 0.440 |
| 4 | 2.773 | 2.266 | 6.24 | [15.242, 16.230] | 15.613 | -0.550 | 0.988 | 0.436 |
| 6 | 3.584 | 1.753 | 8.06 | [14.953, 15.755] | 15.293 | -1.442 | 0.802 | 0.457 |
| 8 | 4.159 | 1.511 | 9.36 | [14.901, 15.666] | 15.242 | -2.130 | 0.765 | 0.506 |

log10 of surplus, mass and energy side by side (E_k is negative; its magnitude is
tabulated):

| lambda | k | log10 nu_k | log10 mass_k | log10 \|E_k\| | log10(mass/nu) | log10(mass/sqrt nu) |
|--:|--:|--:|--:|--:|--:|--:|
| 3 | 0 | -36.33 | -3.81 | -4.25 | 32.5 | 14.4 |
| 3 | 1 | -29.46 | -1.93 | -2.35 | 27.5 | 12.8 |
| 3 | 2 | -23.33 | -1.05 | -1.45 | 22.3 | 10.6 |
| 3 | 3 | -18.21 | -2.82 | -3.47 | 15.4 | 6.3 |
| 3 | 4 | -13.21 | -1.04 | -1.41 | 12.2 | 5.6 |
| 3 | 5 | -8.95 | -1.34 | -1.75 | 7.6 | 3.1 |
| 4 | 0 | -64.53 | -6.02 | -6.48 | 58.5 | 26.2 |
| 4 | 1 | -57.57 | -3.59 | -4.06 | 54.0 | 25.2 |
| 4 | 2 | -51.29 | -1.98 | -2.47 | 49.3 | 23.7 |
| 4 | 3 | -45.27 | -1.06 | -1.56 | 44.2 | 21.6 |
| 4 | 4 | -40.01 | -1.38 | -1.92 | 38.6 | 18.6 |
| 4 | 5 | -34.89 | -1.03 | -1.52 | 33.9 | 16.4 |
| 6 | 0 | -91.20 | -6.63 | -6.66 | 84.6 | 39.0 |
| 6 | 1 | -84.26 | -4.16 | -4.20 | 80.1 | 38.0 |
| 6 | 2 | -77.88 | -2.53 | -2.57 | 75.4 | 36.4 |
| 6 | 3 | -72.01 | -1.47 | -1.53 | 70.5 | 34.5 |
| 6 | 4 | -66.73 | -1.52 | -1.59 | 65.2 | 31.9 |
| 6 | 5 | -61.65 | -1.83 | -1.85 | 59.8 | 29.0 |
| 8 | 0 | -104.83 | -7.11 | -6.97 | 97.7 | 45.3 |
| 8 | 1 | -98.00 | -4.58 | -4.44 | 93.4 | 44.4 |
| 8 | 2 | -91.81 | -2.94 | -2.81 | 88.9 | 43.0 |
| 8 | 3 | -86.01 | -1.91 | -1.79 | 84.1 | 41.1 |
| 8 | 4 | -80.80 | -2.18 | -2.08 | 78.6 | 38.2 |
| 8 | 5 | -75.53 | -2.13 | -1.99 | 73.4 | 35.6 |

Power-law fits log10 mass = p * log10 nu + c over k = 0..5:

| lambda | p | c | rms residual (decades) | span of log10 nu | span of log10 mass |
|--:|--:|--:|--:|--:|--:|
| 3 | 0.073 | -0.43 | 0.76 | 27.4 | 2.8 |
| 4 | 0.161 | +5.38 | 0.75 | 29.6 | 5.0 |
| 6 | 0.165 | +9.45 | 0.82 | 29.6 | 5.2 |
| 8 | 0.167 | +11.44 | 0.82 | 29.3 | 5.2 |
| pooled (24 pts) | 0.037 | -0.60 | 1.43 | 95.9 | 6.1 |

Reading of the fits. There is no power law. Within one window the mass rises from
the ground by 3-5 decades over k = 0..3 while nu rises 18-19 decades, then saturates at
1e-2 .. 1e-1 for k >= 3 and is **non-monotone** (dips at k = 3 for lambda 3, at k = 4
for lambda 4, 6, 8) while nu keeps rising 5-7 decades per step. The per-window
exponent p ~ 0.16 is an artefact of that rise-then-plateau shape, and the intercept
c moves by 12 decades across lambda, so the fitted "law" is different at every window.
Pooled, p = 0.04 with 1.4 decades of scatter: mass ~ nu^0, i.e. the lobe mass does not
track the surplus at all.

## 3. Every negative lobe in xi < 60 (variant C and the profile)

Full tables (mass_k and E_k for every lobe, all four windows) are in
`lobe_mass_output.txt`. Summary of variant (C), the largest single-lobe mass of each
direction:

| lambda | k | log10 nu_k | max lobe mass | at centre (u) | width/cell | log10(max mass / nu) |
|--:|--:|--:|--:|--:|--:|--:|
| 3 | 0 | -36.3 | 0.305 | 1.43 (0.50) | 0.498 | 35.8 |
| 3 | 5 | -9.0 | 0.152 | 27.55 (9.63) | 0.640 | 8.1 |
| 4 | 0 | -64.5 | 0.257 | 1.13 (0.50) | 0.500 | 63.9 |
| 4 | 5 | -34.9 | 0.093 | 15.61 (6.89) | 0.436 | 33.9 |
| 6 | 0 | -91.2 | 0.211 | 0.87 (0.49) | 0.494 | 90.5 |
| 6 | 5 | -61.7 | 0.078 | 18.39 (10.49) | 0.410 | 60.5 |
| 8 | 0 | -104.8 | 0.194 | 0.76 (0.50) | 0.501 | 104.1 |
| 8 | 5 | -75.5 | 0.080 | 3.79 (2.51) | 0.502 | 74.4 |

For all 24 directions the maximum single-lobe mass lies in [0.078, 0.305] and the fit
log10 maxmass = p log10 nu + c gives p = -0.010 .. -0.012 (rms 0.06): the largest lobe
mass is a constant of order 0.1-0.3 across 96 decades of nu. Variant (C) is dead on
the first lobe alone: the u = 1/2 lobe [0, 2 pi/2L] carries 0.19-0.30 of the ground's
mass at every window.

The per-lobe profile of the ground (k = 0), mass in the lobe at cell index u:

| lambda | u=0.5 | 1.5 | 2.5 | 3.5 | 4.5 | 5.5 | 6.5 | 7.5 | 8.5 | 9.5 | 10.5 |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | 0.305 | 0.154 | 0.037 | 4.0e-3 | 1.5e-4 (g1) | 2.3e-6 | 1.4e-7 | 4.8e-10 | -- | 1.0e-11 | -- |
| 4 | 0.257 | 0.163 | 0.064 | 0.015 | 1.7e-3 | 5.7e-5 | 9.6e-7 (g1) | 3.9e-7 | 2.4e-8 | -- | 1.3e-10 |
| 6 | 0.211 | 0.157 | 0.086 | 0.034 | 9.6e-3 | 1.8e-3 | 1.8e-4 | 6.9e-6 | 2.4e-7 (g1) | 1.0e-7 | 1.3e-8 |
| 8 | 0.194 | 0.152 | 0.092 | 0.043 | 0.015 | 3.8e-3 | 6.5e-4 | 6.5e-5 | 2.3e-6 | 7.8e-8 (g1) | 3.3e-8 |

(-- : no lobe centred in that cell; the prime terms shift some lobes off the
half-integer train above u ~ 8.) The ground's lobe mass is monotone decreasing in u
with an accelerating decay (successive ratios at lambda = 8: 0.78, 0.61, 0.47, 0.35,
0.25, 0.17, 0.10, 0.036, 0.033), and the profile widens in cell units as lambda grows
(section 5 of `diag_true_symbol`). For k >= 1 the profile is peaked at a cell index
that grows roughly with k (the "max at" column above) and then decays similarly. The
gamma_1 lobe sits at u = 4.9, 6.2, 8.1, 9.4, further out in cells at each window, which
is why the ground's mass there falls with lambda even as the profile widens.

Negative-set mass and level energies on [0, 60) for every direction:

| lambda | mass on {beta_a < 0}, k = 0..5 | E^- = -E^+ on [0,60), k = 0..5 |
|--:|:--|:--|
| 3 | 0.500, 0.500, 0.504, 0.501, 0.522, 0.537 | 0.090, 0.090, 0.137, 0.184, 0.190, 0.241 |
| 4 | 0.500, 0.500, 0.504, 0.531, 0.518, 0.566 | 0.226, 0.262, 0.298, 0.252, 0.244, 0.360 |
| 6 | 0.500, 0.500, 0.500, 0.502, 0.501, 0.505 | 0.167, 0.192, 0.224, 0.244, 0.208, 0.304 |
| 8 | 0.500, 0.500, 0.500, 0.501, 0.500, 0.502 | 0.044, 0.059, 0.078, 0.110, 0.121, 0.126 |

(E^- + E^+ on [0,60) is at the 1e-6 float level in every case, consistent with
nu_k q+ <= 1e-9.) The gamma_1 lobe's share of the negative-level energy,
E_k(lobe) / E^-_k, runs from 6e-4 (lambda 3, k 0) and 2e-6 (lambda 8, k 0) up to
0.26 (lambda 3, k 2) and 0.15 (lambda 8, k 3): again not a function of nu_k.

## 4. Negative-level energy in the gamma_1 lobe

E_k(lobe) / mass_k(lobe) is an effective depth. For the ground it is -0.36, -0.34,
-0.93, -1.38 at lambda = 3, 4, 6, 8 against lobe depths -0.67, -0.55, -1.44, -2.13:
between 0.54 and 0.65 of the depth, i.e. the ground's mass in the lobe sits roughly
where a half-sine profile would put it (mean of -sin over a half period = 0.64). The
same ratio holds for k = 1..5 (0.55-0.68 of the depth). So E_k(lobe) carries no
information beyond mass_k(lobe) and the lobe depth; it inherits the nu-blindness of
the mass.

## 5. Counterexample (kills every variant)

At lambda = 8, N = 48 (2048 bits, dps 180), the ground pencil direction v_0 has
nu_0 = 1.47e-105 and Fourier mass 7.8e-8 (3.5e-7 at N = 120, `nearzero.py`) in the
negative lobe [14.90, 15.67] of beta_a nearest gamma_1, so mass/nu = 1e97.7 and
mass/sqrt(nu) = 1e45.3. The first negative lobe of beta_a, [0, pi/L] = [0, 0.755]
(cell index u = 1/2), carries 0.194 of v_0's unit mass, so maxmass/nu = 1e104.1. At
lambda = 3 the same three ratios for v_0 are 1e32.5, 1e14.4, 1e35.8, and at lambda = 4,
6 they are 1e58.5 / 1e26.2 / 1e63.9 and 1e84.6 / 1e39.0 / 1e90.5. Hence:

- (A) mass_k(gamma_1 lobe) <= C nu_k needs C >= 1e97.7; (B) needs C >= 1e45.3;
  (C) needs C >= 1e104.1 -- and the required C is not uniform in lambda: it grows
  as 1/nu_0(lambda) times a slowly varying factor (1e-4 .. 1e-7 for (A)), i.e.
  the mass behaves like nu^0 while the bound is asked to behave like nu^1.
- Nor is any positive power p in mass <= C nu^p uniform across k at a fixed
  window: at every lambda the mass is non-monotone in k while nu_k is strictly
  increasing, so mass/nu^p is not monotone for any p > 0, and for
  p <= 1/10 the spread of mass/nu^p over k = 0..5 is still 1.9 (lambda 3) to
  3.3 (lambda 8) decades.
- At a fixed lambda and a fixed finite set of directions the inequality is
  vacuous (any finite positive quantity is <= C times any positive quantity for
  some C); the only possible content was uniformity in lambda and in k, and both
  fail.

Because the ground itself is the counterexample, restricting the hypothesis to the
ground, to the deep block (nu_k < 1e-8), to the half-cell lobes only (all lobes
tabulated have width 0.31-0.65 cells), or to the even sector does not rescue any
variant. The failure is a failure of the *object*: the surplus nu_k is a global
ratio q/q+ of two order-0.1 cancelling energies, whereas the lobe mass is a local
Fourier-localisation quantity set by where the direction's spectral support ends
in cell units; the two are unrelated in the deep block, where every direction has
1 - nu_k = E^-/E^+ = 1 to at least eight digits.

## 6. PROPOSAL (replacement statement the numbers do support; not a result)

**PROPOSAL, not a lemma.** Hypotheses as tested: even sector, head N = 48 (converged
at lambda = 3, 4; a lower section at lambda = 6, 8), lambda in {3, 4, 6, 8}, the six
smallest pencil directions v_k (all with nu_k < 1e-8), lobes of beta_a on xi < 60.

    (P1)  For every deep pencil direction, the Fourier mass on the negative set
          {beta_a < 0} is 1/2 + delta with |delta| <= 0.07 (|delta| <= 0.006 at
          lambda = 6, 8): the 50/50 level split of the ground (diag_true_symbol
          sections 3-4) holds direction by direction across the deep block, and the
          direction's negative-level energy E^-_k = (1 - nu_k) E^+_k lies in
          [0.04, 0.36], neither of them a function of nu_k.

    (P2)  The mass of a deep direction in any single negative lobe is at most 0.31,
          attained at the u = 1/2 lobe for the ground and at a lobe with cell index
          <= 10.5 for k = 1..5; the lobe-mass profile u -> mass_k(lobe at u) of the
          ground is monotone decreasing with accelerating decay (ratios 0.78 -> 0.03
          over u = 0.5 .. 9.5 at lambda = 8) and widens in cell units with lambda.

    (P3)  Consequently any lemma that bounds mass_k(gamma_1 lobe) must bound it by a
          spectral-extent quantity of v_k (e.g. its mass beyond a cell index tied to
          gamma_1 L / 2 pi), not by the surplus nu_k, which carries no local
          information in the deep block. The correct local object for the race of
          diag_true_symbol section 6 is the profile (P2) against the lobe depth
          -- and (P2) is a finite-window observation with no claimed uniformity in
          lambda (the profile widens), so it does not by itself feed the cofinal
          target of prop:v121-cofinal-rh or the bounded floor of
          prop:v136-bounded-floor.

Nothing in (P1)-(P3) is a bound; (P1) and (P2) are 24-direction, four-window
observations at one head size; (P3) is a reading. G2 and RH are not addressed.

## 7. What failed / caveats

- The N = 48 head is a lower section at lambda = 6, 8 (ground gamma_1-lobe mass
  differs from N = 120 by factors 2.3 and 4.4). Irrelevant to the verdict, relevant
  to the profile numbers in section 3 at those windows.
- Masses below ~1e-30 (lobes beyond xi ~ 45 at lambda = 8, beyond 55 at lambda = 6)
  are at the double-precision floor of the transform sum; they are printed in
  `lobe_mass_output.txt` for completeness and mean nothing.
- W^- is float quadrature (~1e-6 relative on the denominator, as in `pencil.py`), so
  nu_k carries ~6 relative digits; the log10 nu_k used here are exact to far better
  than the 0.01 quoted.
- Nothing was substituted for the requested experiment; the pencil, the head size,
  the bit counts and the lobe rule are those specified in NS-21.
