# Direct replacement certificate — sealed independent result

**Wall check: Same open gap.** Closest result: NS38 / `prop:v132-global-index`.
What changes: replayable evidence for the single existing numerical premise
`beta_(log4)(1)<-3/5`. No new arithmetic input or cofinal estimate is attempted.
This is a conclusions/dependency review plus a fresh numerical certificate,
not a replay of all historical proofs and not recovery of an original file.

## Reviewed source and independence

Read-only source: `/private/tmp/riemann-prime-folding-review-20260930`, commit
`769359298fada57711b6895c4bde3fabe2cc5168`, refreshed by the coordinating agent.
Reviewed current AGENTS, all research-map node status/title/notes and the
continuation-input scopes, current README status and dependent summaries,
NEXT_STEPS relevant rows, the full missing-evidence ledger and NS38 claim
changes. Read manuscript `eq:v130-r-symbol`, `eq:v130-beta`,
`prop:v132-global-index`, their surrounding proofs and the appendix disclosure
of absent `certify_beta4_negative.py`. Exact source hashes are in outputs.json.

The source formula was checked before computation. No independent agent's
implementation or result was read before sealing this result. Only the
coordinator's fixed-claim brief was used to select the task; its reported
numerical interval was a claim to verify, not an input to evaluating beta.

## Exact reduction

Put L=2 log4=log16. The current manuscript defines

    beta = Re psi(5/4+i/2) - log(pi)
           - 2 sum_(1<m<16) Lambda(m) m^(-1/2) cos(log m)
           + 2 integral_0^L exp(t/2) cos(t) dt.

The strict integer endpoint excludes 16 even though 16 is a prime power.
Exact integer factorization gives the included prime powers
`2,3,4,5,7,8,9,11,13`; Lambda(p^k)=log(p), not log(p^k).

An antiderivative of exp(t/2)cos(t) is

    F(t) = (4/5) exp(t/2) ((1/2)cos(t)+sin(t)).

Differentiation gives F'(t)=exp(t/2)cos(t): the sine cross terms cancel,
and (1/4+1)/(5/4)=1. Since exp(L/2)=4 and F(0)=2/5,

    2(F(L)-F(0)) = (16 cos(L)+32 sin(L)-4)/5.

This retains the continuum term's positive sign in beta and its lower
endpoint contribution -4/5. A second complex-exponential evaluation of the
same integral overlaps at each precision; the elementary antiderivative is
the analytic justification, not overlap alone.

## Ball certificate and exact outward bounds

`verify_beta.py` evaluates the formula directly with `python-flint 0.9.0`:
`acb.digamma()` at the exact rational argument 5/4+i/2, and Arb pi/log/sqrt/
cos/sin for the other terms. No floating midpoint is used in a proof gate.
It recomputes at 192 and 320 bits, exports each term's directed dyadic
endpoints exactly as rational numerator/denominator pairs, then rounds the
beta interval outward to denominator 10^45. Strict ball comparisons confirm
both decimal-rational endpoint inequalities at both precisions:

    -0.640027118160897146421661394744768547319369747
      < beta_(log4)(1) <
    -0.640027118160897146421661394744768547319369746.

In particular the manuscript's historical broad interval

    -0.64784909 < beta_(log4)(1) < -0.6321938 < -3/5

is verified. This is fresh replacement evidence, not an assertion that the
unavailable historical computation used these methods or returned these
precise values. Arb/acb's certified-function implementations are the
numerical library trust dependency of this direct-method certificate.

Approximate decomposition for orientation only (exact balls are in JSON):
archimedean -1.2251461931; signed prime sum -2.0613235404;
continuum -1.4762044655; beta -0.6400271182. The signed prime sum is
SUBTRACTED. Its negative value therefore contributes positively to beta.

## Scope of the consequence

Continuity and evenness of the finite-sum symbol provide symmetric open
frequency intervals on which it is negative. Arbitrarily many disjoint
smooth symmetric frequency supports there yield arbitrarily many mutually
orthogonal negative directions for the full-line multiplier; any fixed
finite number of linear constraints reduces this dimension by at most
that finite number. These inverse Fourier transforms are Schwartz, but
they are not supported inside (-log4,log4). Thus this supplies the numerical
premise of the existing full-line negative-index implication, not a negative
physical-window Weil direction. Certified physical W4 positivity is intact.

Both historical original-evidence groups remain recovery OPEN. No source
manuscript, registry, primary configuration, research state, gallery or
publication file was changed. RH, G2 and the full cofinal signed-arithmetic
floor remain open. No candidate scan, new theorem row or thaw occurred.

## Replay

From the repo root:

    .venv/bin/python audits/bounds-six-agent-2026-09-30-v1/certificate/01-direct/verify_beta.py
    pyright --project audits/bounds-six-agent-2026-09-30-v1/certificate/01-direct/pyrightconfig.json

Replay passes both precision gates and exact outward comparisons.
Scoped CLI Pyright diagnostics: zero errors, zero warnings (no LSP tool
available in this session). Every Python function has type annotations.
The owned configuration selects the existing project virtual environment;
no working import, dependency or global configuration was changed.
