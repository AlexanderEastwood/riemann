# Adversarial certificate review — 2026-09-30

**Major finding first:** no major defect found in either fixed-parameter derivation or replay. The fresh numerical premise succeeds. This resolves evidence for one existing conditional full-line multiplier claim, not any physical-window or cofinal estimate.

**Wall check: Same open gap.** Closest result: NS38 / `prop:v132-global-index`. What changes is replacement evidence for the existing fixed value beta_(log4)(1), not its mathematical definition or a new RH route. The full-line finite-negative-index shortcut is excluded under its stated hypotheses once this numerical premise is accepted. The physical signed floor, G2, RH and NB arithmetic gain remain open.

## Reviewed source and boundaries

Coordinator refreshed the isolated public source at 769359298fada57711b6895c4bde3fabe2cc5168. Reviewed AGENTS, the 104-node conclusion register and continuation scopes, README/current NEXT_STEPS context, MISSING/NS38 disclosure and the directly affected manuscript statements. This is a conclusions/dependency review and a fresh replay of only the specified scalar claim, not revalidation of all historical proofs. Source files and the original manuscript/register were not changed.

The exact source is `manuscript/fixed_space_prime_action_v1.tex`, equations `eq:v130-r-symbol`, `eq:v130-beta`, proposition `prop:v132-global-index`, and the appendix disclosure around the absent `certify_beta4_negative.py`. At a=log(4), xi=1, the signs are:

    Re psi(5/4+i/2) - log(pi)
    - 2 sum_{1<m<16} Lambda(m) cos(log m)/sqrt(m)
    + 2 integral_0^log(16) exp(t/2) cos(t) dt.

Exactly 2,3,4,5,7,8,9,11,13 contribute. The weight is log of the underlying prime, not log of the prime power. Sixteen is a prime power but is excluded by the strict endpoint. This was checked from the source and both independently enumerated lists. No endpoint perturbation, parameter search, extra frequency or new window was used.

## Direct path

The direct verifier uses exact rational complex input 5/4+i/2, `acb.digamma`, and outward Arb elementary operations at 192 and 320 bits. The continuum antiderivative is correct: after the factor two it equals `(16 cos(log16)+32 sin(log16)-4)/5`. The separate complex-exponential formula overlaps it. Exact directed dyadic endpoints are exported, then rounded outward to rationals with denominator 10^45, using floor at the lower end and ceiling at the upper end. The strict comparisons against those rational endpoints are checked with balls; no midpoint or binary floating-point conversion enters the certificate.

Both direct precisions certify the same strict 45-place interval:

    -0.640027118160897146421661394744768547319369747
       < beta_(log4)(1) <
    -0.640027118160897146421661394744768547319369746.

## Independent series path

The independent implementation uses no library digamma, gamma or Euler constant. Its decomposition

    f(x)=1/(x+1)-(x+5/4)/((x+5/4)^2+1/4)
        =(1/4)/((x+1)(x+5/4))
          +(1/4)/((x+5/4)((x+5/4)^2+1/4))

is algebraically correct and positive decreasing for x>=0. The residual after k=0,...,K-1 lies between I_K and I_K+f(K), with `I_K=.5 log((K+5/4)^2+1/4)-log(K+1)`. There is no omitted k=K term or tail-sign inversion.

Its Euler-constant interval `H_M-log M-1/M < gamma < H_M-log M` follows by telescoping the elementary integral comparison. The width is an analytic truncation allowance; increasing working precision need not shrink it.

The continuum Taylor expansion integrates `Re exp((1/2+i)t)` term by term. After K=40 terms, the first omitted absolute majorant is `L(|c|L)^40/41!`; successive ratios are at most `|c|L/42<1`. The script's factorial and ratio indices match this argument. The resulting symmetric remainder is outward and is below 4.04e-30.

Both 128/256-bit series runs certify the broader rational bounds

    -0.640150 < beta_(log4)(1) < -0.639904 < -3/5.

These enclosures contain both direct balls, not merely their displayed midpoints. Independence is of analytic evaluation paths; both implementations share python-flint/Arb as the interval backend. This is not a second backend or recovery of the historical all-rational implementation.

## Replay and integrity

`replay.py` imports both sealed scripts without running their default output-writing entrypoints on import. It redirects only their output-directory globals into this reviewer's `direct-replay/` and `series-replay/` folders, then executes both complete mains in this review's Python subprocess. No other reviewer's files are written.

All **37 checks pass** in `replay.json`: every sealed file hash before and after; byte-identical fresh outputs for both complete programs; the strict cutoff/list; both broader series rational gates; both continuum remainder gates; printed series balls containing the fresh series balls; all four series/direct cross-containments; and both direct strict rational endpoint gates. Source hashes and exact rational output are retained. CLI pyright on the owned annotated verifier reports zero errors, warnings and informations.

## Downstream scope audit

1. The finite sum and digamma expression make beta continuous and real even on the real frequency axis. A strictly negative value at xi=1 therefore gives a nonempty negative interval about 1 and its reflection about -1; no numerical interval width is claimed here.
2. Inside these intervals, arbitrarily many smooth nonzero Fourier bumps can have pairwise disjoint symmetric supports. Choose each bump even. Multiplication by beta is strictly negative on their span because every nonzero vector has mass only where beta<0, and disjoint supports remove mixed terms.
3. For any fixed m homogeneous linear constraints, choose a span of dimension d>m. Their common kernel has dimension at least d-m. Thus arbitrarily large negative subspaces remain in the even full-line sector. No continuity of the finite functionals is needed beyond their being defined on these Schwartz tests. This is a negative-index statement; it does not address arbitrary affine prescribed constraints.
4. The inverse Fourier transforms are Schwartz, but nonzero compact-frequency smooth tests cannot also be supported in a bounded physical interval. They are not admissible compactly supported physical tests on (-log4,log4). Therefore full-line negative index cannot be transferred to the physical lambda=4 form. It is consistent with that form's certified nonnegativity in both parity sectors. The symbol identity quoted here is the even-sector physical identity; no unreviewed odd physical implication is asserted.
5. Success supplies fresh evidence for the existing proposition's numerical premise. It does not recover `certify_beta4_negative.py`, the old output, original witness packages, or either missing-original evidence group. Both original-recovery groups remain **OPEN**. No manuscript/register change, theorem row, public page, scan, or publication was performed.

**Final classification: Same open gap; fixed existing-claim validation passed.** No remaining major finding within this bounded scalar and scope audit.
