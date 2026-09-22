# Arithmetic content of the pencil surplus (NS-20) -- DIAGNOSTIC

> **Correction notice (2026-09-22, after the adversarial audit `audits/circle-symbol-lane-2026-09-22-v2.html` (NS-31, PR #16); originals retained below).**
> Withdrawn: "only the prime powers with log m < 1.7 enter the net value at all", "which primes carry the surplus", and "a three-to-five-term balance summing to 1e-38…1e-92". The small primes dominate the net prime sum to a few percent or an absolute 1e-4; they do not determine the surplus, which is 1e-38…1e-92 — e.g. at λ=3 the m=8 term is 1.7e-25, twelve orders above the surplus, and at λ=6 the m=32 term is 7.8e-69 against 1e-92. Deleting small terms changes the quantity. The super-exponential-in-lag decay is an observed finite list, not an asymptotic. Also: the three "sum of primes" level rows have the net sum in the "pos" column and the positive level in the "neg" column; the correct pairs are (−0.546, +0.491) at λ=3 v₀, (−0.664, +0.598) at λ=4, (−1.089, +1.000) at λ=6, with the same shift for v₁, v₂. What stands: the exact term-by-term decomposition and its cross-checks; the qualitative statement that the O(1) budget is carried by digamma, continuum and m=2, and the level energies by the prime powers near the cutoff.

**Status: diagnostic, not a certificate.** Midpoint (mpmath, 120 digits) values of exact
closed-form quadratic forms, plus float grid quadrature for the level split. Nothing here is
a bound; nothing here bears on G2 or RH.

Board row NS-20. Follow-up to `evidence/diag_true_symbol/results.md` section 7 (the level
pencil): the first three pencil vectors `v_k` of `W v = nu (W + W^-) v` on the even head cancel
positive- and negative-level energies of size 0.09-0.30 down to `nu_k q+ ~ 1e-38 ... 1e-92`.
Question asked here: written out in the explicit terms of the symbol, is that surplus an
explicit arithmetic quantity (one prime power, a small set, a closed-form-looking relation,
a pattern stable in lambda), or a many-term cancellation only a certificate can see?

## 0. The identity being tabulated

The validated symbol (`eq:v130-beta`; `a = log lambda`, `L = 2a`) is

    beta_a(xi) = [Re psi(5/4 + i xi/2) - log pi]  -  2 sum_{1<m<lambda^2} Lambda(m)/sqrt(m) cos(xi log m)
                 + 2 int_0^L e^{t/2} cos(xi t) dt,

and `q[v] = int_R beta_a |F v|^2 dxi` (unitary F of the zero extension of the head function
`f_v(x) = sum_n v_n c_n cos(2 pi n x/L)` on `[0, L]`, `||v||_2 = 1` = Plancherel mass).  Since
`int cos(xi y) |F f|^2 dxi = A_f(y)`, the autocorrelation `A_f(y) = int f(x) f(x+y) dx`, each
term is a time-domain functional of the direction:

    q[v] = Psi_v  +  sum_m P_m(v)  +  C(v),
    Psi_v  = int (Re psi(5/4 + i xi/2) - log pi) |F v|^2 dxi          (digamma / archimedean term)
    P_m(v) = -2 Lambda(m)/sqrt(m) A_v(log m)                          (one per prime power m < lambda^2)
    C(v)   = +2 int_0^L e^{t/2} A_v(t) dt                              (continuum term)

so the prime sum minus the continuum is the weighted Chebyshev remainder
`-2 int_1^{lambda^2} A_v(log u) u^{-1/2} d(psi(u) - u)` sampled by the direction's autocorrelation.

## 1. Method and checks (`decomp.py` -> `decomp_output.txt`)

- Pencil exactly as `pencil.py`: `W = block()` (Arb, 1024 bits at lambda = 3, 4; 2048 at 6),
  `W^- = int beta_a^- |Fe|^2` by float grid quadrature to xi = 4000, pencil solved in mpmath at
  120 digits; even head N = 48; `v_k` normalised to `||v||_2 = 1`.
- **Every term is assembled exactly.** `block()` is linear in its sequences `(b, d)`, and
  `sequences()` is a sum of one contribution per symbol term, so the head matrix of each term
  is `block()` of the split sequences (checked: split sums reproduce `sequences()` to 1e-187
  and the split blocks sum to `block()` to 1e-114).  One subtlety: `sequences()` is written
  with `psi(1/4 - i xi/2)` and folds the pole term
  `1/(1/4 + xi^2) = Re[1/(1/4 + i xi/2)]` (from `psi(5/4 + z) = psi(1/4 + z) + 1/(1/4 + z)`)
  into its `32 L sinh^2(L/4)` continuum piece, whose time-domain kernel is therefore
  `e^{t/2} + e^{-t/2}` on `[0, L]`, not `e^{t/2}`.  The symbol's own split above is recovered
  by moving the Lorentzian `int |Fv|^2/(1/4 + xi^2) = 2 int_0^L e^{-t/2} A_v(t) dt`, which
  has the closed form `expcorr_matrix(s = -1/2)` in the script; the `e^{t/2}` kernel
  (`s = +1/2`) gives the continuum term directly, and the two together reproduce the
  sequences' continuum block to 5e-16 (independent check of the split).  The prime blocks
  equal `-Lambda(m)/sqrt(m) * S(log m)`, `S` the closed-form correlation matrix, to 1e-14.
- **Cross-check by grid quadrature** of each symbol term against `|F v_k|^2` (with the
  analytic `log(xi/2) - log pi` tail beyond xi = 4000 for the digamma term): every term whose
  size exceeds 1e-6 agrees with the exact value to 1e-15 relative or better (column
  `rel.diff` in the output).  Terms below 1e-7 are pure quadrature noise in the float
  column; only the exact column is meaningful there.
- **The sum reaches `nu_k q+` itself.**  `sum of terms - v^T W v` is 1e-115 (working
  precision), and `v^T W v = nu_k q+[v_k]` to the quoted digits (4.242e-38, ..., 2.959e-79):
  the float error in `W^-` enters the pencil vector as `nu (dW^-) v`, i.e. scaled by `nu`, so
  the surplus is resolved to the *relative* accuracy of `W^-` however small it is (as
  `pencil.py` states).  The exact eigenvectors `u_k` of `W` are decomposed as well (section 5).
- **Positive-/negative-level parts** of each term are `int_{beta_a > 0}` and
  `int_{beta_a < 0}` by the same grid quadrature; they have no closed form and carry the
  quadrature's ~1e-6 absolute accuracy (plus the `W^-` tail beyond the grid, <= 3e-4 relative
  at lambda >= 4, `wminus_tail.py`).  `A_v(log m)` in the tables is `P_m /(-2 Lambda(m)/sqrt(m))`.

## 2. Net decomposition of `q[v_k]` (exact)

Each column sums, term by term, to the `total` row.  `nu_k q+` is the pencil's own value of the
same number; `q+` is the positive-level energy the direction has to cancel.

### lambda = 3: net terms (exact), ||v_k|| = 1

| term | v_0 | v_1 | v_2 |   | A_v0(log m) | A_v1(log m) | A_v2(log m) |
|---|--:|--:|--:|---|--:|--:|--:|
| digamma | -0.7742 | -0.0870 | 0.0462 |  |  |  |  |
| m=2 (2) | -0.0548 | -0.3181 | -0.0441 |  | 0.0559 | 0.3245 | 0.0450 |
| m=3 (3) | -3.74e-04 | -0.0909 | -0.4740 |  | 2.95e-04 | 0.0716 | 0.3737 |
| m=4 (2^2) | -3.21e-07 | -5.76e-04 | -0.0733 |  | 4.64e-07 | 8.32e-04 | 0.1057 |
| m=5 (5) | -3.44e-10 | -2.88e-06 | -0.0025 |  | 2.39e-10 | 2.00e-06 | 0.0017 |
| m=7 (7) | -9.36e-19 | -1.14e-13 | -1.99e-09 |  | 6.36e-19 | 7.73e-14 | 1.35e-09 |
| m=8 (2^3) | -1.66e-25 | -8.57e-20 | -7.34e-15 |  | 3.38e-25 | 1.75e-19 | 1.50e-14 |
| continuum | 0.8294 | 0.4966 | 0.5478 |  |  |  |  |
| **sum of primes** | -0.0552 | -0.4095 | -0.5940 | | | | |
| **total = q[v_k]** | 4.242e-38 | 3.138e-31 | 6.420e-25 | | | | |
| nu_k q+[v_k] | 4.242e-38 | 3.138e-31 | 6.42e-25 | | | | |
| q+[v_k] (quadrature) | 0.0898 | 0.0896 | 0.1368 | | | | |

### lambda = 4: net terms (exact), ||v_k|| = 1

| term | v_0 | v_1 | v_2 |   | A_v0(log m) | A_v1(log m) | A_v2(log m) |
|---|--:|--:|--:|---|--:|--:|--:|
| digamma | -0.7900 | -0.1622 | -0.0153 |  |  |  |  |
| m=2 (2) | -0.0656 | -0.3243 | -0.0568 |  | 0.0669 | 0.3308 | 0.0580 |
| m=3 (3) | -7.36e-04 | -0.1223 | -0.4361 |  | 5.80e-04 | 0.0964 | 0.3437 |
| m=4 (2^2) | -1.59e-06 | -0.0015 | -0.1070 |  | 2.29e-06 | 0.0022 | 0.1543 |
| m=5 (5) | -7.72e-09 | -2.62e-05 | -0.0092 |  | 5.36e-09 | 1.82e-05 | 0.0064 |
| m=7 (7) | -1.22e-14 | -2.55e-10 | -7.60e-07 |  | 8.27e-15 | 1.73e-10 | 5.16e-07 |
| m=8 (2^3) | -2.68e-18 | -1.16e-13 | -7.73e-10 |  | 5.48e-18 | 2.36e-13 | 1.58e-09 |
| m=9 (3^2) | -1.66e-21 | -1.36e-16 | -1.86e-12 |  | 2.27e-21 | 1.86e-16 | 2.54e-12 |
| m=11 (11) | -9.45e-29 | -2.45e-23 | -1.16e-18 |  | 6.54e-29 | 1.70e-23 | 8.05e-19 |
| m=13 (13) | -6.55e-38 | -5.03e-32 | -7.51e-27 |  | 4.60e-38 | 3.53e-32 | 5.28e-27 |
| continuum | 0.8563 | 0.6105 | 0.6244 |  |  |  |  |
| **sum of primes** | -0.0663 | -0.4482 | -0.6091 | | | | |
| **total = q[v_k]** | 6.639e-66 | 7.112e-59 | 1.543e-52 | | | | |
| nu_k q+[v_k] | 6.639e-66 | 7.112e-59 | 1.543e-52 | | | | |
| q+[v_k] (quadrature) | 0.2256 | 0.2616 | 0.2977 | | | | |

### lambda = 6: net terms (exact), ||v_k|| = 1

| term | v_0 | v_1 | v_2 |   | A_v0(log m) | A_v1(log m) | A_v2(log m) |
|---|--:|--:|--:|---|--:|--:|--:|
| digamma | -0.8183 | -0.1864 | -0.0516 |  |  |  |  |
| m=2 (2) | -0.0875 | -0.2572 | -0.0937 |  | 0.0892 | 0.2624 | 0.0956 |
| m=3 (3) | -0.0020 | -0.1853 | -0.3078 |  | 0.0015 | 0.1461 | 0.2427 |
| m=4 (2^2) | -1.23e-05 | -0.0054 | -0.1672 |  | 1.77e-05 | 0.0079 | 0.2412 |
| m=5 (5) | -2.51e-07 | -3.15e-04 | -0.0392 |  | 1.75e-07 | 2.19e-04 | 0.0273 |
| m=7 (7) | -2.26e-11 | -1.15e-07 | -7.81e-05 |  | 1.53e-11 | 7.83e-08 | 5.31e-05 |
| m=8 (2^3) | -7.08e-14 | -6.08e-10 | -7.47e-07 |  | 1.44e-13 | 1.24e-09 | 1.52e-06 |
| m=9 (3^2) | -1.01e-15 | -1.36e-11 | -2.75e-08 |  | 1.38e-15 | 1.85e-11 | 3.76e-08 |
| m=11 (11) | -1.91e-19 | -5.39e-15 | -2.46e-11 |  | 1.32e-19 | 3.73e-15 | 1.70e-11 |
| m=13 (13) | -1.87e-23 | -9.65e-19 | -8.46e-15 |  | 1.32e-23 | 6.78e-19 | 5.95e-15 |
| m=16 (2^4) | -4.35e-30 | -4.75e-25 | -9.27e-21 |  | 1.26e-29 | 1.37e-24 | 2.68e-20 |
| m=17 (17) | -1.63e-31 | -2.22e-26 | -5.49e-22 |  | 1.19e-31 | 1.62e-26 | 3.99e-22 |
| m=19 (19) | -1.27e-35 | -2.63e-30 | -1.01e-25 |  | 9.44e-36 | 1.95e-30 | 7.45e-26 |
| m=23 (23) | -3.57e-44 | -1.56e-38 | -1.32e-33 |  | 2.73e-44 | 1.20e-38 | 1.01e-33 |
| m=25 (5^2) | -5.01e-49 | -3.13e-43 | -3.85e-38 |  | 7.79e-49 | 4.86e-43 | 5.98e-38 |
| m=27 (3^3) | -4.80e-54 | -4.26e-48 | -7.63e-43 |  | 1.13e-53 | 1.01e-47 | 1.80e-42 |
| m=29 (29) | -7.73e-59 | -9.85e-53 | -2.59e-47 |  | 6.18e-59 | 7.87e-53 | 2.07e-47 |
| m=31 (31) | -8.90e-65 | -1.66e-58 | -6.62e-53 |  | 7.22e-65 | 1.35e-58 | 5.36e-53 |
| m=32 (2^5) | -7.76e-69 | -1.78e-62 | -8.89e-57 |  | 3.17e-68 | 7.27e-62 | 3.63e-56 |
| continuum | 0.9078 | 0.6347 | 0.6596 |  |  |  |  |
| **sum of primes** | -0.0894 | -0.4483 | -0.6081 | | | | |
| **total = q[v_k]** | 1.054e-92 | 1.062e-85 | 2.959e-79 | | | | |
| nu_k q+[v_k] | 1.054e-92 | 1.062e-85 | 2.959e-79 | | | | |
| q+[v_k] (quadrature) | 0.1669 | 0.1915 | 0.2242 | | | | |

## 3. Positive-level and negative-level parts of each term

Columns `pos` = `int_{beta_a > 0} term * |F v_k|^2`, `neg` = `int_{beta_a < 0}`; `pos + neg` is the
net value of section 2, and the `total` row is `(q+[v_k], q-[v_k])`.

### lambda = 3: positive-level / negative-level parts (quadrature over {beta_a > 0} / {beta_a < 0})

| term | v_0 pos | v_0 neg | v_1 pos | v_1 neg | v_2 pos | v_2 neg |
|---|--:|--:|--:|--:|--:|--:|
| digamma | -0.3898 | -0.3844 | -0.0472 | -0.0399 | +0.0117 | +0.0345 |
| m=2 (2) | -0.0277 | -0.0271 | -0.1593 | -0.1588 | -0.0400 | -0.0041 |
| m=3 (3) | -0.0009 | +0.0006 | -0.0786 | -0.0122 | -0.3707 | -0.1034 |
| m=4 (2^2) | -0.0046 | +0.0046 | -0.0737 | +0.0731 | -0.0032 | -0.0701 |
| m=5 (5) | -0.0603 | +0.0603 | -0.0562 | +0.0562 | +0.0178 | -0.0203 |
| m=7 (7) | -0.3123 | +0.3123 | +0.0890 | -0.0890 | +0.0734 | -0.0734 |
| m=8 (2^3) | -0.1401 | +0.1401 | -0.0675 | +0.0675 | -0.0299 | +0.0299 |
| continuum | +1.0256 | -0.1962 | +0.4830 | +0.0136 | +0.4777 | +0.0700 |
| **sum of primes** | -0.0552 | -0.5460 | -0.4095 | -0.3462 | -0.5940 | -0.3526 |
| **total (q+, q-)** | +0.0898 | -0.0898 | +0.0896 | -0.0896 | +0.1368 | -0.1368 |

### lambda = 4: positive-level / negative-level parts (quadrature over {beta_a > 0} / {beta_a < 0})

| term | v_0 pos | v_0 neg | v_1 pos | v_1 neg | v_2 pos | v_2 neg |
|---|--:|--:|--:|--:|--:|--:|
| digamma | -0.3954 | -0.3946 | -0.0821 | -0.0802 | -0.0129 | -0.0024 |
| m=2 (2) | -0.0325 | -0.0330 | -0.1619 | -0.1624 | -0.0281 | -0.0288 |
| m=3 (3) | -0.0003 | -0.0004 | -0.0612 | -0.0612 | -0.2179 | -0.2181 |
| m=4 (2^2) | -0.0001 | +0.0001 | -0.0014 | -0.0002 | -0.0914 | -0.0156 |
| m=5 (5) | -0.0003 | +0.0003 | -0.0232 | +0.0232 | -0.1923 | +0.1831 |
| m=7 (7) | -0.0091 | +0.0091 | -0.1907 | +0.1907 | +0.1109 | -0.1109 |
| m=8 (2^3) | -0.0104 | +0.0104 | -0.0518 | +0.0518 | -0.0068 | +0.0068 |
| m=9 (3^2) | -0.0373 | +0.0373 | -0.0041 | +0.0041 | -0.0480 | +0.0480 |
| m=11 (11) | -0.2151 | +0.2151 | +0.1637 | -0.1637 | +0.0980 | -0.0980 |
| m=13 (13) | -0.3592 | +0.3592 | -0.1063 | +0.1063 | -0.0341 | +0.0341 |
| continuum | +1.2854 | -0.4291 | +0.7806 | -0.1701 | +0.7203 | -0.0959 |
| **sum of primes** | -0.0663 | -0.6645 | -0.4482 | -0.4369 | -0.6091 | -0.4097 |
| **total (q+, q-)** | +0.2256 | -0.2256 | +0.2616 | -0.2616 | +0.2977 | -0.2977 |

### lambda = 6: positive-level / negative-level parts (quadrature over {beta_a > 0} / {beta_a < 0})

| term | v_0 pos | v_0 neg | v_1 pos | v_1 neg | v_2 pos | v_2 neg |
|---|--:|--:|--:|--:|--:|--:|
| digamma | -0.4094 | -0.4090 | -0.0934 | -0.0929 | -0.0264 | -0.0252 |
| m=2 (2) | -0.0439 | -0.0435 | -0.1287 | -0.1285 | -0.0471 | -0.0466 |
| m=3 (3) | -0.0013 | -0.0007 | -0.0927 | -0.0926 | -0.1546 | -0.1532 |
| m=4 (2^2) | -0.0002 | +0.0001 | -0.0028 | -0.0026 | -0.0837 | -0.0835 |
| m=5 (5) | -0.0002 | +0.0002 | -0.0006 | +0.0002 | -0.0199 | -0.0193 |
| m=7 (7) | +0.0000 | -0.0000 | -0.0001 | +0.0001 | -0.0070 | +0.0069 |
| m=8 (2^3) | +0.0000 | -0.0000 | -0.0001 | +0.0001 | -0.0091 | +0.0091 |
| m=9 (3^2) | -0.0001 | +0.0001 | -0.0011 | +0.0011 | -0.0404 | +0.0404 |
| m=11 (11) | -0.0006 | +0.0006 | -0.0236 | +0.0236 | -0.1832 | +0.1832 |
| m=13 (13) | -0.0019 | +0.0019 | -0.0835 | +0.0835 | -0.0742 | +0.0742 |
| m=16 (2^4) | -0.0029 | +0.0029 | -0.0433 | +0.0433 | +0.0263 | -0.0263 |
| m=17 (17) | -0.0190 | +0.0190 | -0.1719 | +0.1719 | +0.0821 | -0.0821 |
| m=19 (19) | -0.0427 | +0.0427 | -0.1061 | +0.1061 | -0.0270 | +0.0270 |
| m=23 (23) | -0.1269 | +0.1269 | +0.1103 | -0.1103 | -0.0452 | +0.0452 |
| m=25 (5^2) | -0.0905 | +0.0905 | +0.0738 | -0.0738 | +0.0240 | -0.0240 |
| m=27 (3^3) | -0.0785 | +0.0785 | +0.0354 | -0.0354 | +0.0333 | -0.0333 |
| m=29 (29) | -0.2856 | +0.2856 | +0.0041 | -0.0041 | +0.0626 | -0.0626 |
| m=31 (31) | -0.3264 | +0.3264 | -0.1248 | +0.1248 | -0.0498 | +0.0498 |
| m=32 (2^5) | -0.0685 | +0.0685 | -0.0376 | +0.0376 | -0.0238 | +0.0238 |
| continuum | +1.6654 | -0.7576 | +0.8783 | -0.2436 | +0.7874 | -0.1278 |
| **sum of primes** | -0.0894 | -1.0891 | -0.4483 | -0.5934 | -0.6081 | -0.5368 |
| **total (q+, q-)** | +0.1669 | -0.1669 | +0.1915 | -0.1915 | +0.2242 | -0.2242 |

## 4. Running remainder: how far out in the prime sum the identity is still moving

`psi_v + sum_{m' <= m} P_m'(v) + C(<= log m)`, with `C(<= T) = 2 int_0^T e^{t/2} A_v(t) dt`; the last column is the full sum with `T = 2a` and all m < lambda^2.


| lambda | k | m=2 | m=3 | m=4 | m=5 | m=7 | m=8 | full (= q[v_k]) |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 3 | 0 | -0.015374 | -0.000054 | -0.000000 | -0.000000 | +0.000000 | +0.000000 | 4.24e-38 |
| 3 | 1 | -0.275066 | -0.019578 | -0.000144 | -0.000000 | -0.000000 | +0.000000 | 3.14e-31 |
| 3 | 2 | +0.231796 | -0.290530 | -0.026063 | -0.000281 | -0.000000 | -0.000000 | 6.42e-25 |
| 4 | 0 | -0.019613 | -0.000120 | -0.000000 | -0.000000 | -0.000000 | -0.000000 | 6.64e-66 |
| 4 | 1 | -0.285406 | -0.029496 | -0.000447 | -0.000003 | -0.000000 | -0.000000 | 7.11e-59 |
| 4 | 2 | +0.188235 | -0.299547 | -0.042270 | -0.001380 | -0.000000 | -0.000000 | 1.54e-52 |
| 6 | 0 | -0.028905 | -0.000379 | -0.000004 | -0.000000 | -0.000000 | -0.000000 | 1.05e-92 |
| 6 | 1 | -0.268327 | -0.052800 | -0.001869 | -0.000050 | -0.000000 | -0.000000 | 1.06e-85 |
| 6 | 2 | +0.126553 | -0.281047 | -0.071782 | -0.008257 | -0.000010 | -0.000000 | 2.96e-79 |

## 5. Exact eigenvectors of W beside the pencil vectors

`u_k` = eigenvector of `W` for `e_k` (exact from Arb, 120-digit eigensolve); same decomposition, same normalisation.


| lambda | k | vector | digamma | m=2 | m=3 | m=4 | continuum | total | q+ |
|--:|--:|---|--:|--:|--:|--:|--:|--:|--:|
| 3 | 0 | v_0 (pencil) | -0.7742 | -0.0548 | -3.74e-04 | -3.21e-07 | 0.8294 | 4.242e-38 | 0.0898 |
| 3 | 0 | u_0 (eig W) | -0.7742 | -0.0548 | -3.74e-04 | -3.21e-07 | 0.8294 | 4.242e-38 | 0.0898 |
| 3 | 1 | v_1 (pencil) | -0.0870 | -0.3181 | -0.0909 | -5.76e-04 | 0.4966 | 3.138e-31 | 0.0896 |
| 3 | 1 | u_1 (eig W) | -0.0987 | -0.3258 | -0.0911 | -5.77e-04 | 0.5162 | 3.139e-31 | 0.0896 |
| 3 | 2 | v_2 (pencil) | 0.0462 | -0.0441 | -0.4740 | -0.0733 | 0.5478 | 6.420e-25 | 0.1368 |
| 3 | 2 | u_2 (eig W) | 0.1356 | -0.1185 | -0.3963 | -0.0725 | 0.4542 | 6.516e-25 | 0.1402 |
| 4 | 0 | v_0 (pencil) | -0.7900 | -0.0656 | -7.36e-04 | -1.59e-06 | 0.8563 | 6.639e-66 | 0.2256 |
| 4 | 0 | u_0 (eig W) | -0.7900 | -0.0656 | -7.36e-04 | -1.59e-06 | 0.8563 | 6.639e-66 | 0.2256 |
| 4 | 1 | v_1 (pencil) | -0.1622 | -0.3243 | -0.1223 | -0.0015 | 0.6105 | 7.112e-59 | 0.2616 |
| 4 | 1 | u_1 (eig W) | -0.1152 | -0.2929 | -0.1214 | -0.0015 | 0.5311 | 7.134e-59 | 0.2631 |
| 4 | 2 | v_2 (pencil) | -0.0153 | -0.0568 | -0.4361 | -0.1070 | 0.6244 | 1.543e-52 | 0.2977 |
| 4 | 2 | u_2 (eig W) | 0.1055 | -0.1410 | -0.3243 | -0.1046 | 0.4736 | 1.579e-52 | 0.3109 |
| 6 | 0 | v_0 (pencil) | -0.8183 | -0.0875 | -0.0020 | -1.23e-05 | 0.9078 | 1.054e-92 | 0.1669 |
| 6 | 0 | u_0 (eig W) | -0.8183 | -0.0875 | -0.0020 | -1.23e-05 | 0.9078 | 1.054e-92 | 0.1669 |
| 6 | 1 | v_1 (pencil) | -0.1864 | -0.2572 | -0.1853 | -0.0054 | 0.6347 | 1.062e-85 | 0.1915 |
| 6 | 1 | u_1 (eig W) | -0.1462 | -0.2253 | -0.1834 | -0.0054 | 0.5606 | 1.065e-85 | 0.1924 |
| 6 | 2 | v_2 (pencil) | -0.0516 | -0.0937 | -0.3078 | -0.1672 | 0.6596 | 2.959e-79 | 0.2242 |
| 6 | 2 | u_2 (eig W) | 0.0658 | -0.1914 | -0.1798 | -0.1597 | 0.5041 | 3.026e-79 | 0.2337 |

## 6. Reading

1. **Only the first few prime powers enter the net value.**  The autocorrelation of a deep
   direction decays super-exponentially in the lag: for `v_0`, `A(log 2), A(log 3), A(log 4),
   A(log 5)` are `6e-2, 3e-4, 5e-7, 2e-10` at lambda = 3 and `9e-2, 2e-3, 2e-5, 2e-7` at
   lambda = 6, and it keeps falling by 4-6 decades per prime power to `1e-25` (m = 8,
   lambda = 3) and `1e-68` (m = 32, lambda = 6).  So the *net* prime sum is `P_2` alone to
   better than 97% for `v_0` at all three windows (`-0.055, -0.066, -0.089`), `P_2 + P_3`
   (with `P_4` at 1e-3) for `v_1`, and `P_3 + P_4 + P_2 + P_5` for `v_2`.  The k-th pencil
   direction reaches one lag further out; nothing with `log m > 1.7` (m >= 7) ever
   contributes above 1e-4.  The running remainder (section 4) is within 1e-6 of its final
   value (1e-38 ... 1e-79) once the prime sum is cut at m = 8 and the continuum integral at
   `T = log 8 = 2.08`, for all nine directions and whatever the window: the identity is local
   in the lag, and the window enters only through the direction itself.
2. **The net cancellation is a three-to-five-term balance of O(1) quantities.**  For the
   ground direction: digamma `-0.77, -0.79, -0.82`; continuum `+0.83, +0.86, +0.91`;
   `P_2 = -0.055, -0.066, -0.089` (lambda = 3, 4, 6), summing to `4e-38, 7e-66, 1e-92`.  The
   three numbers drift slowly and monotonically with the window; no term is small, none
   vanishes, and no closed-form relation among them is visible (their ratios,
   `P_2 / C = 0.066, 0.077, 0.096`, `Psi / C = -0.93, -0.92, -0.90`, are not recognisable
   constants).  Each is a transcendental functional of the eigenvector -- the archimedean
   term is a spectral integral against `Re psi`, the others are lag-domain integrals of
   `A_v` -- and it is the eigenvalue problem that tunes the direction until they balance.
3. **The level split is carried by the *other* end of the prime sum.**  The prime powers with
   `log m` near `L = 2a` (m = 7, 8 at lambda = 3; 11, 13 at lambda = 4; 23-32 at lambda = 6)
   contribute `1e-18 ... 1e-68` net but `+-0.1 ... +-0.36` to each level separately:
   `cos(xi log m)` with `log m ~ L` is in phase with the symbol's own comb of period `2 pi/L`
   (section 5 of `diag_true_symbol`), so on `{beta_a > 0}` and `{beta_a < 0}` these terms
   are large and opposite.  At lambda = 6 the prime sum splits as `-1.09 / +1.00` for `v_0`
   while netting `-0.089`; the continuum term splits `+1.67 / -0.76` netting `+0.91`; the
   digamma term, smooth on the comb scale, splits evenly (`-0.41 / -0.41`).  So the two
   questions -- which primes carry `q+` and `q-` (the 0.09-0.30 the direction must cancel) and
   which primes carry `q` (its net) -- have disjoint answers: the top of the prime sum for
   the former, `m = 2, 3` (and 4, 5) for the latter.
4. **The pattern is stable in lambda.**  Same ordering of terms, same lags active, same
   level-split mechanism, magnitudes drifting by tens of percent from lambda = 3 to 6; the
   surplus shrinks from 1e-38 to 1e-92 with no visible change in the O(1) terms.  Nothing
   in the tables distinguishes lambda = 6 from lambda = 3 except the size of the comb-phase
   prime powers in the level split (they grow with the number of prime powers near `L`).
5. **Pencil vectors vs eigenvectors of W** (section 5): `v_0 = u_0` to all printed digits;
   `v_1`, `v_2` differ from `u_1`, `u_2` by tens of percent in the leading terms and up to a
   factor 3 in the smaller ones (the two orderings agree only for the ground), with the same
   qualitative decomposition, so the reading does not depend on which family is used.

**Verdict.**  Written in the symbol's own terms, the per-direction surplus is an explicit but
not a closed-form arithmetic quantity.  It is exactly `Psi_v - 2 sum_m Lambda(m)/sqrt(m)
A_v(log m) + 2 int_0^{2a} e^{t/2} A_v(t) dt`, and because the autocorrelation `A_v` of a deep
pencil direction decays super-exponentially in the lag (4-6 decades per prime power), only
the prime powers with `log m < 1.7` enter the net value at all: `m = 2` alone carries the
ground's prime content to better than 97% at lambda = 3, 4 and 6 (`P_2 = -0.055, -0.066,
-0.089`), `m = 2, 3` carry `v_1`'s, and `m = 2, 3, 4, 5` carry `v_2`'s, while everything from
m = 7 to lambda^2 contributes below 1e-4 net.  The cancellation is therefore a three-to-five-term
balance -- for the ground, digamma `~ -0.8`, continuum `~ +0.85`, `P_2 ~ -0.06` -- of O(1)
transcendental functionals of the eigenvector (one spectral integral against `Re psi`, the rest
lag-domain integrals of `A_v`), stable in form across the three windows with slowly drifting
magnitudes; no term is small, none vanishes, and no closed-form relation among them is visible,
so the balance itself is only visible to the computation.  Separately, the positive-/negative-level
split of the same direction (`q+ = -q- = 0.09 ... 0.30`) is carried by the opposite end of the
prime sum, the prime powers with `log m` near `2a` whose `cos(xi log m)` is in phase with the
symbol's comb: those contribute `+-0.1 ... +-0.36` to each level and `1e-18 ... 1e-68` net.  "Which
primes carry the level energies" and "which primes carry the surplus" have disjoint answers,
and neither singles out an arithmetic identity that would make the surplus a priori
nonnegative.  Nothing here is a bound.

## 7. Reproduction

From the repo root (run time ~1 min per case plus ~50 s for each new Arb sequence cache;
the caches `evidence/v124/g2_schur_cancellation/sequences_v3_l*_J56_b*_k96.json` are
regenerated on first run and are not committed):

    .venv/bin/python evidence/diag_pencil_arithmetic/decomp.py 3,48,1024 4,48,1024 6,48,2048 > evidence/diag_pencil_arithmetic/decomp_output.txt

The tables above are the exact/quadrature columns of that file; the smaller-magnitude entries
of the level split are quoted to 4 decimals.
