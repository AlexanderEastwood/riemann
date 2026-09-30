# Independent mathematical review

Reviewed base: `ccebc6524cf8adf5e83143ad00daa55b190737bd` (PR #63 merged).
Reviewer: delegated mathematical-review agent, 2026-09-29.

Scope: read the current agent rules, conclusion register and continuation
inputs, current README/board, missing-evidence ledger, PR #63 audit, and this
attempt's admission, script and saved 50/80-digit outputs. Checked the
relevant NS51/55/58 statements and the bounded operator/packet algebra.
This is not a replay of historical proofs, a new numerical run, or an
interval certificate. No external literature claim is needed for the
elementary checks below.

## Outcome

The diagnostic is correctly set up and does not support either proposed
one-sided boundary ordering. I found no material sign, normalization or
parity error. Its information about the RH problem is limited: it tests
generic compression algebra at Euler parameters and supplies no new
arithmetic estimate or bridge to the complete signed Weil form.

**Wall check: Same open gap** for KERNEL-API, closest NS51/55/58 and PR #63.
The literal mixed-boundary ordering is a distinct auxiliary statement from
PR #63's bounds-only implication, but it is not a distinct arithmetic input
addressing API. The present floating outputs diagnose its failure. Do not
call this a newly proved wall or extend the failure to exact Euler methods.

## Mathematical checks

Write `Q=I-P`, `a=log(p)`, and `r=p^(-1/2)`. The normalization is

`D_p=(1+r^2)I-r(T_a+T_-a)` and `C_p=(1-r^2)D_p^(-1)`.

Thus D is the inverse **denominator**, not literally the inverse of the
normalized Poisson chain without its scalar factor. The admission uses
the former wording correctly. The D operators are bounded, strictly
positive, self-adjoint and mutually commuting on the whole line.

On `range(P)`, direct insertion of `P+Q=I` gives

`(PD_pP D_qP+PD_qP D_pP)/2 = PD_pD_qP-K_pq`.

The proposed sign direction is therefore correct. Also
`<f,K_pq f>=Re <QD_p f,QD_q f>`; positivity of the individual D operators
does not fix this mixed exterior inner product's sign. The script computes
exactly its packet matrix, not a substitute for the full Weil energy.

The four indicator packets have unit individual norm and disjoint supports
inside the window. With `x=3/2`, `y=x+log(3/2)`, the relevant positive exterior
coincidence is `y+log(2)=x+log(3)`. Its reflected negative coincidence is the
other nonzero path. The same relation creates an interior coincidence that
Q correctly removes. The displayed matrix has two identical off-diagonal
blocks with entry `1/(2 sqrt(6))`, consistent with the saved values.
The four chosen sign vectors have squared norm four. Reflection exchanges
the first and third packets, and the second and fourth; the even and odd
labels are correct. Within each parity, equal and opposite packet signs
give the two diagnostic signs.

No compressed-product indefiniteness follows from an indefinite K. Nor is
this a negative Weil test, a first-window nullvector, or an API
counterexample. Although indicators belong to the logarithmic form domain,
the calculation is only of bounded D operators and imposes neither the
full null equation nor source constraints. That limitation is correctly
disclosed. A smooth common bump could replace the indicators if needed;
doing so would not add an arithmetic mechanism.

## Why this should have been a cheaper screen

The identity `QD_pP=-r Q(T_a+T_-a)P` removes the scalar diagonal completely.
The remaining mixed form is a positive scalar times a translation-overlap
form. The same packet pattern works for an open range of ordinary positive
shifts and weights. The special relation `r=exp(-a/2)`, primality and the
global compatibility of all Euler coefficients are not used to obtain the
sign behavior. Retaining their literal values is therefore insufficient
evidence that this proposed estimate exploits arithmetic.

A full certified replay or new theorem node is not worthwhile. An elementary
exact support-overlap proof could close this narrow ordering if desired,
but it would only formalize the cheap rejection. The current diagnostic,
with its stated limits, is sufficient to stop pursuing this ordering.

## Recommended admission questions

Before another numerical screen, require all three:

1. **Proof-use test:** identify the precise step that fails when the Euler
   coefficients or prime shifts are replaced by generic admissible values.
   Merely inserting `log p` and `p^(-1/2)` does not pass.
2. **Implication test:** write a conditional derivation from the proposed
   estimate to one named open input, retaining every signed term and domain.
   If success still leaves a wholly unspecified bridge, reduce its priority.
3. **Small-model test:** simplify the operator algebra and check a
   two-packet or two-dimensional model before using high precision. Here
   the mixed exterior inner product already predicts indefiniteness.

These are triage tools, not a claim that generic operator methods cannot
solve an arithmetic problem. A successful generic lemma can be useful when
its verified arithmetic hypotheses and complete transfer are specified.
Here neither transfer was supplied. The best next action is to select a
single missing arithmetic estimate and study the assumptions of applicable
unconditional theorems against it, rather than generate another positive
representation and search afterward for its connection to API.
