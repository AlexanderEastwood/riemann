NUMERICAL ILLUSTRATION ONLY — not a certificate, window computation, or Weil-tail estimate.

# NS-26: exact symbol identity and the finite zero-sum comparison

The exact proposition and proof are `prop:v146-beta-explicit` and
`eq:v146-lattice` in the manuscript; their incremental source is
`evidence/v146/beta_lattice_identity.tex`. RH and G2 remain open.

## What had to change

1. The archived cutoffs x = lambda² are 9, 16, 36, 64, all integers.
   The defining sum is strict. Perron inversion supplies a half-weight
   at a prime-power endpoint, which must be removed. In beta the resulting
   term is +Lambda(x)/sqrt(x) cos(xi log x). It vanishes at 36, but not
   at 9, 16, or 64. The separate noninteger identity has zero endpoint term.
2. The diagnostic's equal crests and exact quarter-point zeros are not
   exact properties. The identity has a frequency-dependent cosine
   envelope and an additional sine envelope. The table already shows this.
3. `selfsim_output.txt` has only three decimal places. A literal 1e-6
   comparison to its rounded numbers is impossible. We reproduced all
   forty underlying sample locations with the unchanged `make_beta_true`
   and compared an independently assembled zero-side formula; all saved
   three-decimal roundings also agree. No ground or head was recomputed.
4. `4 sum sin(gamma L)/gamma` is a zero-frequency amplitude contribution,
   not a crest-minus-trough. Applying it to every zero would use RH.
   We use only a finite located zero list in the illustration, count all
   zeros up to 680, and retain the omitted sum in the exact identity.

## Exact formula used for the numerical illustration

Set s=1/2-i xi and K_e(w)=exp(Lw+e²w²/2)/w. Gaussian Perron inversion gives

    S_e(s) = sum_n Lambda(n)n^(-s) Phi(log(x/n)/e)
           = x^(1-s) exp(e²(1-s)²/2)/(1-s) - zeta'/zeta(s)
             - sum_rho K_e(rho-s) - sum_{n=1}^9 K_e(-2n-s) + I_e(s),

where Phi is the standard normal distribution function and

    I_e(s) = (1/(2 pi i)) integral_{Re w=-20}
             [-zeta'/zeta(s+w)] K_e(w) dw.

Only the first nine trivial zeros lie between this line and the initial
right line. Do NOT sum Gaussian-weighted trivial residues to infinity:
that would diverge along the negative real axis. The left contour stays
in the identity. The nontrivial-zero sum converges absolutely and includes
zeros anywhere in the critical strip, without RH.

Define the exact desmoothing correction

    D_e(s) = sum_n Lambda(n)n^(-s)
             [1_{n<x} - Phi(log(x/n)/e)].

This correction returns to the original sharp cutoff, not a new window.
At n=x its coefficient is -1/2. The functional equation and digamma
recurrence cancel the complete archimedean/log-derivative/lower-limit block.
Consequently the exact identity is

    beta = 2 Re sum_rho K_e(rho-s)
         + 2 Re sum_{n=1}^9 K_e(-2n-s)
         - 2 Re [x^(1-s) expm1(e²(1-s)²/2)/(1-s)]
         - 2 Re D_e(s) - 2 Re I_e(s).

The script evaluates the endpoint part of -2 Re D_e separately. This is
not a residual defined by subtracting the answer: every term is assembled
from zeros, trivial residues, the pole, and a convergent Gaussian Perron
correction. The original finite prime formula is used only for comparison.

The left contour is tiny on these inputs. For |xi|<=12, the functional
equation on z=-19.5+i(t-xi), the digamma series at 20.5, and the absolutely
convergent log-derivative series at Re(1-z)=20.5 give

    |zeta'/zeta(z)| <= 8 + 0.1 |t|.

For example |cot(pi z/2)|=1 on this line, psi(20.5)<log(20.5), and
|psi(20.5+iy)-psi(20.5)| <= |y| (1/20.5+1/20.5²).
It follows directly that

    2 |I_e| <= x^(-20) exp(200e²)/(20 pi)
               [8 sqrt(2 pi)/e + 0.2/e²] < 4e-18

for x>=9 and .025<=e<=.03. The script omits this bounded contour term.
It evaluates 400 positive zeros and their conjugates; Arb's finite zero
count N(680)=400 agrees with this list at both input precisions. No
assumption about the real parts of higher zeros is made. Gaussian damping
and the unconditional O(T log T) zero count ensure convergence; this run
is a floating-point illustration, not an interval certificate for its
omitted zero tail. The prime correction is summed through 256; the tail
is dominated by the Gaussian in log(n/64), using Lambda(n)<=log n.
The exact infinite tails remain part of the formula. Neither omitted tail
is replaced by an asserted RH estimate.

## Replay and observed agreement

From the repository root:

    .venv/bin/python evidence/diag_beta_lattice_identity/verify_identity.py

Environment: python-flint 0.9.0 and mpmath 1.4.1. The original beta function
and its prime-power assembly are imported unchanged. The zero-side prime
powers are generated independently. `check_b192.json` uses 192-bit zero
inputs, 45 decimal digits, epsilon=.025; `check_b256.json` uses 256-bit
zero inputs, 65 decimal digits, epsilon=.03. All results here are numerical
illustrations. The maximum observed absolute discrepancies are respectively
3.073e-21 and 3.257e-21, below 1e-6. Each JSON records every component,
the source hash, the saved rounding and the error from the legacy floating
sample abscissa. Pyright: 0 errors, 0 warnings.

The full zero contribution quoted below is reconstructed through the
Gaussian formula with exact desmoothing, rather than identified with a
400-zero raw or Cesaro sum. The residual in a truncated *sharp* zero sum
is then its difference from the reconstructed value; no bound on that
sharp-sum residual is claimed.

| lambda | 0.25 | 0.5 | 0.75 | 1 | 1.25 | 1.5 | 2 | 2.5 | 3 | 4 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | -0.001049620 | -0.285170440 | +0.004813623 | +0.283528080 | -0.011627613 | -0.279198149 | +0.271550179 | -0.259112589 | +0.238487065 | +0.119430410 |
| 4 | -0.000136061 | -0.686696623 | +0.000587379 | +0.694629609 | -0.001325758 | -0.708227383 | +0.728494661 | -0.757157288 | +0.797086684 | +0.935066074 |
| 6 | -0.009625892 | -0.509465665 | +0.029106199 | +0.511568482 | -0.049274218 | -0.515132406 | +0.520278251 | -0.527201212 | +0.536192519 | +0.562320938 |
| 8 | +0.000335780 | -0.130577913 | -0.001066304 | +0.131917033 | +0.001979857 | -0.134212830 | +0.137571506 | -0.142157995 | +0.148213318 | +0.166265590 |

## Which terms explain the naive mismatch

At lambda=3, C_x(0)=0.285219144687, decomposed as

    full zero amplitude       -0.077669995516
    trivial-zero amplitude    -0.003314956020
    strict endpoint           +0.366204096223

The 400-zero index-Cesaro candidate is -0.077720711653; height-Cesaro
(weight 1-gamma/680) gives -0.076414263832. Neither is a crest-minus-trough.
For the actual difference at u=1 minus u=1/2:

    full shifted zero term    -0.159765789563
    trivial-zero term         -0.003943883015
    strict endpoint           +0.732408192445
    TOTAL                     +0.568698519867

The height-Cesaro shifted zero term is -0.157163432709, with remaining
correction -0.002602356854. The raw 400-zero term is -0.164351811782,
with remaining correction +0.004586022219. The full shifted zero difference
is also not exactly twice its zero-frequency amplitude: the denominator
shifts contribute a further -0.004425798532 relative to that approximation.
Thus the sign reversal is mainly the endpoint term and the amplitude/difference
normalization, not a hidden archimedean constant (that block cancels exactly).

The exact amplitude at zero is the weighted arithmetic expression

    psi(5/4)-log(pi) - 2 sum_{n<x} Lambda(n)/sqrt(n) + 4(sqrt(x)-1).

Its four values are 0.285219144687, 0.684047784634, 0.508768457193,
0.130137500274. The archimedean constant is -1.372183419226, not the
-2.11 printed in the original diagnostic prose.

## Finding and scope

This is the classical explicit formula with the actual weighting, phase,
cutoff convention and remainder restored. It does not add a new arithmetic
lens, uniform positivity estimate, or energy budget determined by one scalar.
The energy still uses the full Fourier distribution of the state. The
failure here is of the constant-amplitude and truncated-zero surrogates,
not of the symbol or the concentration criterion. No new window, head,
Weil-tail metric or complete-ground enclosure was computed. G2 and RH remain open.
