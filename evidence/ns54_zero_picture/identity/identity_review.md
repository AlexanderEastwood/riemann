# NS-54 — identity and sign review of Claude's zero-picture essay

Internal review note. Scope: exact identities and their interpretation; no new numerical experiment, no Selberg literature assessment, no heat-flow assessment. Pinned repository: `ccd722bf2b0e6fd6f0133f5b9220fed130b2c325`. All manuscript line numbers below refer to `manuscript/fixed_space_prime_action_v1.tex` at that revision. Reviewed against the exact recorded identities, not diagnostic surrogates. The findings below concern the supplied essay, not defects in the cited exact formulas.

## MAJOR 1 — the unconditional field is not a gamma-only sinc sum

**Essay claim:** v1.46 writes the symbol as a sum of `sin(L(gamma-xi))/(gamma-xi)` kernels without RH.

**Finding:** false. Put `a=log(lambda)`, `L=2a`, `x=exp(L)`, `s=1/2-i xi`. The exact identity is

```
beta_a(xi) = 2 Re lim_{T→∞} sum_{|Im rho|<T} x^(rho-s)/(rho-s)
             - 2 Re sum_{n≥1} x^(-2n-s)/(2n+s)
             + e_x cos(L xi),
e_x = Lambda(x)/sqrt(x) if x is an integer, and 0 otherwise.
```

The zero sum includes multiplicities and uses the prescribed symmetric-height Perron limit. At a finite height it additionally has `-2 Re R_{x,T}(s)`; smooth weighting of a finite list does not authorize deleting this term. References: manuscript:10087–10110, 10121–10126, 10679–10714.

For `rho=1/2+eta+i gamma`, set `y=gamma+xi`. Its individual real summand is

```
2 exp(L eta) [eta cos(L y) + y sin(L y)]/(eta²+y²).
```

It becomes `2 sin(L y)/y` only when `eta=0`, with continuous value `2L` at `y=0`. A conjugate pair on the line contributes

```
2 [ sin(L(gamma+xi))/(gamma+xi) + sin(L(gamma-xi))/(gamma-xi) ].
```

Replacing **all** zeros by such pairs assumes RH. The manuscript states exactly this restriction at 10189–10201. Off-line displacement enters both an exponential weight and the kernel denominator; an ordinate-counting measure cannot encode it. The correct unconditional object is the corrected complex-zero field, not the counting measure of ordinates convolved with a real sinc.

## MAJOR 2 — the symbol is not centered by subtracting expected zero density

**Essay claim:** the symbol equals sinc-smoothed zero density minus its smooth expected density; positivity/negativity says whether the local count is above/below expectation.

**Finding:** the claimed subtraction is absent. In the first line of v1.46 the functional equation and digamma recurrence give the exact cancellation

```
A(xi) + 2 Re (zeta'/zeta)(s) - 2 Re [1/(1-s)] = 0,
A(xi) = Re psi(5/4+i xi/2) - log(pi).
```

Thus the full field itself, with endpoint and trivial-zero correction, is `beta_a`. There is no remaining subtraction of a smooth mean: manuscript:10099–10105 and 10147–10155. A smoothed counting-field interpretation under RH would retain its nonzero expected-density contribution; a separately centered field would be a different object.

**Direct fixed-window check:** from the prime expression at manuscript:9614–9620,

```
beta_a(xi) = A(xi) - 2 sum_{1<n<x} Lambda(n)/sqrt(n) cos(xi log n)
             + 2 Re [(exp((1/2+i xi)L)-1)/(1/2+i xi)].
```

For fixed `a`, the finite prime sum is bounded, the last term is `O_a(1/|xi|)`, and `A(xi)=log(|xi|/(2pi))+o(1)`. Consequently `beta_a(xi)=log|xi|+O_a(1)→+∞`. The same asymptotic is explicitly recorded at manuscript:13042. Treating this as the centered fluctuation field would remove a term that the actual symbol retains.

**Independent sign obstruction:** the real sinc kernel is not a nonnegative averaging kernel. With `k_L(y)=sin(Ly)/y`,

```
k_L(0)=L,                  k_L(3pi/(2L))=-2L/(3pi).
```

Increasing a positive zero mass at the latter separation decreases the field. Its sign therefore cannot be read as an excess/deficit of a local unsigned count. This is an exact kernel calculation, not a newly simulated zero configuration or a counterexample to an arithmetic theorem.

The true form identity does stand, in both parities: `q_a[f]=integral beta_a |F(f~)|²`, manuscript:12321–12329. Its sign is decided by the **whole** weighted positive-minus-negative energy. No assertion that Fourier mass concentrated in a vaguely “locally dense” region has positive energy follows from the zero picture.

## MAJOR 3 — density smoothing is a derivative of argument smoothing

**Essay claim:** the symbol's value distribution is that of a smoothed `S` at scale `1/L`; its growing negative depth is the same phenomenon as unbounded `S(t)` fluctuations.

**Finding:** the identification does not follow even after provisionally imposing RH and performing the missing centering. Let `N` be the ordinate counting function and `M` its smooth part, so the argument fluctuation is the primitive `S=N-M` (with the usual constant/conventions fixed). The density discrepancy is the Stieltjes distribution `dS`, not `S(t) dt`.

For a finite interval `[A,B]`, the relevant integration by parts is

```
integral_[A,B] k_L(t-xi) dS(t)
 = [k_L(t-xi) S(t)]_A^B - integral_A^B k_L'(t-xi) S(t) dt.
```

After any admissible common regularization, the centered density convolution is the **frequency derivative** of the convolution with `S`, with boundary/remainder terms retained. A value-distribution theorem for a smoothing of `S` does not automatically give a theorem for this derivative. The uncentered arithmetic field also retains the mean and, without RH, the real-part factors from MAJOR 1. This is an object mismatch before the separate literature/scaling questions are reached.

The record's actual depth proof has a different mechanism. Under RH an isolated zero produces a surviving negative cutoff side lobe: manuscript:12878–12898 proves eventually `inf beta_a ≤ -a/(6pi²)` using the probe at 12831–12875. The unconditional `inf beta_a→-∞` is then obtained by the bounded-floor contradiction at 12986–12999; **no unconditional linear rate** is claimed. This proof requires neither a large argument fluctuation nor a high-frequency largest-local-deficit statement. Attributing this recorded obstruction to Selberg's omega phenomenon is unsupported.

## MINOR 1 — the zero endpoint at lambda=6 does not make the value a pure zero sum

The arithmetic statement `Lambda(36)=0` is correct: `36=2²·3²` is not a prime power, so `e_36=0`. But the trivial-zero term remains. At `xi=0`,

```
C_a(0) = -2 sum_{n≥1} 36^(-2n-1/2)/(2n+1/2),
          -2/19425 ≤ C_a(0) < -1/9720 < 0.
```

The first summand is exactly `-1/9720`; bounding every denominator below by `5/2` gives the geometric bound `2/19425`. Thus the difference from the full zero sum is about `-1.03·10^-4`, even at the simplest point. A finite zero list also retains its Perron remainder. Calling lambda=6 “endpoint-free” is correct; calling it an exact “clean zero-sum value” is not. References: manuscript:10204–10206 and 10683–10696.

## NOTE 1 — the comb language is valid only with varying envelopes

The exact lattice identity is

```
beta_a(2pi u/L)=C_x(2pi u/L) cos(2pi u)+S_x(2pi u/L) sin(2pi u),
C_x(xi)=e_x+2 Re H_x(xi),       S_x(xi)=-2 Im H_x(xi),
H_x(xi)=sum_rho x^(rho-1/2)/(rho-1/2+i xi)
        -sum_{n≥1} x^(-2n-1/2)/(2n+1/2-i xi).
```

The shifted denominators vary with frequency; the trivial term is part of `H_x`. Neither constant crests nor zero quarter points is an identity. References: manuscript:10161–10185. The archived lambda=6 values at `u=1/4` and `u=3/4` are `-0.009625892` and `+0.029106199`; its integer crests at `u=1` and `u=4` are `0.511568482` and `0.562320938`: `evidence/diag_beta_lattice_identity/results.md:118`. These are existing diagnostic values, not bounds. The essay may call the oscillatory appearance a cutoff side-lobe picture, but cannot replace the actual field by one periodic sinc comb or a single amplitude.

The zero-frequency amplitude is specifically

```
beta_a(0)=psi(5/4)-log(pi)-2 sum_{n<x} Lambda(n)/sqrt(n)+4(sqrt(x)-1),
```

with archimedean constant about `-1.372183419`, not an unweighted `psi(x)-x` remainder. At lambda=3 the recorded crest-minus-trough decomposition is `-0.159765789563` from all zeros, `-0.003943883015` from trivial zeros, and `+0.732408192445` from the endpoint, totaling `+0.568698519867`: manuscript:10208–10223. The correction terms can determine the observed sign.

## NOTE 2 — pole cancellation and code-piece bookkeeping must remain explicit

The original shifted symbol absorbs the Lorentzian `(xi²+1/4)^(-1)` into `Re psi(5/4+i xi/2)`. The older coefficient assembler uses `psi(1/4-i xi/2)` and includes that Lorentzian in its continuum piece, whose kernel is `exp(t/2)+exp(-t/2)`, instead of the symbol's `exp(t/2)` alone. This is documented in `evidence/diag_pencil_arithmetic/results.md:45`–53 and algebraically in manuscript:9655–9663. It does not introduce a new freely subtractable expected-density or pole term. The explicit-formula cancellation above uses the complete expression, not separately named code pieces.

**Verdict within this assigned scope:** the exact complete-form identity and the endpoint-free fact at 36 stand. The unconditional gamma-only sinc picture, mean-subtracted field, local-count sign interpretation, and identification with the value distribution of smoothed `S` fall. A correct replacement must retain complex-zero locations, the uncentered signed field, all endpoint/trivial/Perron terms, and the full Fourier weighting of the state. This note supplies no signed floor, QG proof, G2 or RH claim.
