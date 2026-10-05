# Review 5 — complex domain, actual poles and source hypotheses

**Verdict: PASS, with a recommended boundary-domain clarification.**

Reviewed baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208` (PR75).
Read the current review brief and derivation, repository instructions,
the PR75 boundary derivation, the PR74 arXiv-method review, and the missing
original-evidence ledger. The coordinator records the register-wide
conclusions/dependency review; this reviewer did not replay every historical
proof or certificate. Both original-recovery groups remain OPEN.

This is an independent paper check of the assigned complex-domain question,
not a numerical or symbolic scan. It does not assess an exhaustive literature
search. Only this review file is owned by this reviewer.

**Wall check: Same open gap.** Closest: NS100/101 and PR74/75.
The changed representation repairs ordinary real-axis transforms; it supplies
no original-theta all-height signed estimate. Complex poles specifically
prevent treating the new transform as an entire-function substitute.

## 1. Real Schwartz regularity and the ordinary complex integral

PASS on derivation (1), (5), and Section 3 (lines 177–191 in the reviewed
snapshot). Keep the distinctions explicit:

- Smoothness at zero comes from the original complete expression
  `f(u)=2*cosh(u/2)-h(u)`, not from declaring an arbitrary half-line series
  to have a smooth reflection.
- At either real end, every derivative is bounded by a derivative-dependent
  constant times `exp(-abs(u)/2)`. Consequently `f` belongs to the Schwartz
  class on the real line. Its ordinary Fourier transform `Y` is also
  Schwartz on the real line.
- Schwartz regularity implies neither an entire Fourier transform nor
  arbitrarily wide complex strips. The exponential tail, not the real-axis
  differentiability or polynomial decay of `Y`, determines this domain.

For `r=x+i*y`, absolute convergence follows from

```text
abs(f(u)*exp(i*r*u)) <= exp(-abs(u)/2-y*u).
```

For each compact subset of `abs(y)<1/2`, the same integrable domination
holds after multiplying by every `abs(u)^j`. This proves holomorphy of the
integral and complex differentiation under it in that open strip. It also
justifies the integrations by parts giving

```text
(r^2+1/4)*Y(r)=4*X(r),  abs(Im r)<1/2.
```

The original `X`, coming from the complete double-exponentially decaying
`phi`, is entire. The domain limitation belongs to the new primitive's
ordinary transform, not to `X`.

## 2. The two poles are genuine; the whole boundary is not singular

At `r=i/2`, `1/2+i*r=0`; at `r=-i/2`, it equals 1. With the project's
normalization,

```text
X(i/2)=X(-i/2)=1/4,
p'(i/2)=i, p'(-i/2)=-i.
```

Thus analytic continuation by (5) has exactly the two possible denominator
singularities, and neither is removable:

```text
Res_(r=i/2) Y(r)=-i,
Res_(r=-i/2) Y(r)= i.
```

These are actual simple poles. In particular `Y` is not entire.

The boundary-integral wording benefits from separating two facts. At every
point of either boundary line `Im r=+/-1/2`, the ordinary two-sided integral
fails: the leading tail at one end is `exp(i*x*u)` with nonzero unit
amplitude. At `x=0` its integral diverges linearly; at `x!=0` its primitive
oscillates without a limit. The double-exponentially decaying remainder
cannot cancel that leading nonconvergence. Outside the closed strip the
same end has exponentially growing amplitude.

Nevertheless analytic continuation is regular at every point of those
boundary lines except `+/-i/2`. Failure of the original integral is not a
natural boundary or a line of poles. An Abel continuation or another
regularized boundary prescription would be a different operation from
ordinary integration and must be named if used.

Recommended replacement for the draft's phrase “prevent convergence at the
strip endpoints”:

> The ordinary integral converges absolutely exactly in the open strip
> `abs(Im r)<1/2` and fails on its boundary lines. Its meromorphic
> continuation has simple poles only at `r=+/-i/2`; all other points of
> those lines are regular after continuation.

This is a precision improvement, not a correction to any displayed identity.

## 3. Csordas's admissible class does not contain this primitive

Directly checked [Csordas, arXiv:1309.0055v2](https://arxiv.org/html/1309.0055v2),
Definition 1.2, formula (1.4), and Section 2. The admissible-kernel definition
requires smoothness, strict positivity, evenness, strict decrease on the
positive half-line, and a super-Gaussian bound on every derivative for a
fixed positive exponent increment. The required decay fails here already
for the zeroth derivative:

```text
f(u)/exp(-u/2) -> 1,
f(u)/exp(-u^(2+epsilon)) -> infinity, every epsilon>0.
```

There is no need to decide strict decrease to exclude membership. An
admissible-kernel theorem from that source cannot be applied to `f` by
retaining only positivity, evenness and smooth rapid real decay. The
entire-function Laguerre-Pólya criteria likewise cannot be applied directly
to meromorphic `Y`. The source distinguishes first-Laguerre positivity from
the all-order criterion; no implication from the former to RH is licensed.

None of this invalidates real-variable product differentiation in (9) or
the corrected first-Laguerre target (10). Nor does it exclude a different
theorem with genuinely matched hypotheses. No such theorem is imported by
this audit.

## 4. Scope of the finding and stop

The domain analysis is compatible with the paper's boundary repair:
separate transforms of the new `A_j` are legitimate on the real axis. It
prevents only an unsupported entire-transform substitution for `Y`.
Equation (10) is still an equivalent obligation, not an independent
estimate. No control pass or original nonlinear-IVP inequality follows
from membership in a smooth or Schwartz class.

No manuscript change, row, thaw, computation, commit, push or outreach was
performed. RH, G2 and the original all-height signed estimate remain open.

**Final wall check: Same open gap — NS100/101, PR74/75.**
