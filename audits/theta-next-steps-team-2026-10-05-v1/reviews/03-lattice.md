# Reviewer 03 — original two-shift lattice: no estimating mechanism admitted

Reviewed remote baseline: `18d324703969b5bcc9aa94043cfd90a6e8211f34` (PR76),
as refreshed by the coordinating agent. Shared worktree HEAD during this
review: `32f599ced1abb2bf2376a715042e6e4101591639`. Read AGENTS section 0
and the proposal gate, the 104-node conclusion register and 14 continuation
inputs, current README/NEXT_STEPS, evidence/MISSING, NS100/101 arguments,
and PR73/75/76 audits. This is a dependency/method-feasibility review, not a
historical proof replay. Both original-evidence recovery groups stay OPEN.

**Wall check: Same open gap — ZERO-GEOMETRY, NS100/101, PR73/75/76.**
What changes: no arithmetic hypothesis or estimating input has been supplied.
The original integer-square coefficients distinguish the object from NS101;
the reindexing, positivity of the Gaussian quadratic form and primitive
boundary repair do not estimate its signed transform. No sign computation,
scan, new row, thaw, manuscript version or external outreach is recommended.

## Decision

Do not open a lattice/residue-class calculation task from the current
representations. I found no specific signed lattice inequality or summation
method beyond the existing unestimated target. The strongest immediate
action is a stop on that task family until an explicit infinite regrouping
and its estimating inequality are supplied. A request to find such a
regrouping is not itself an admitted next step.

The exact target remains, for every real r including its zeros,

```text
p = r^2 + 1/4,
J(r) = p^2*(Y'^2-Y*Y'') + 2*(r^2-1/4)*Y^2
     = 16*(X'^2-X*X'') >= 0.
```

This is first-Laguerre positivity only. No implication from this single
inequality to RH, G2 or the complete cofinal Weil floor is established.

## An exact ledger for the missing cancellation

This ledger explains the stop; it is not proposed as a new estimating input.
On u>=0 use the original summands

```text
q_n(u) = (2*pi^2*n^4*exp(9*u/2)-3*pi*n^2*exp(5*u/2))
         *exp(-pi*n^2*exp(2*u)),             n>=1,
a_n(r) = 2*integral_0^infinity q_n(u)*cos(r*u) du.
```

The original coefficients are exactly one for every n. Each q_n is positive
on this half-line; the factor two from the original +/-n points is already
in q_n. The complete theta kernel is the even extension of the complete
sum, not the claim that each summand has smooth even extension. Gaussian
summability of the first three weighted moments justifies X=sum a_n and
its first two r derivatives, uniformly on the real r axis, and the complete
double sum

```text
B_nm(r) = a_n'*a_m' - (a_n*a_m''+a_m*a_n'')/2,
J(r)/16 = sum_(n,m>=1) B_nm(r).

B_nm(r) = integral_(u,v>=0) q_n(u)*q_m(v) *
          [(u+v)^2*cos(r*(u-v))+(u-v)^2*cos(r*(u+v))] du dv.
```

Both phases and every mixed n,m term are required. The coefficients in this
double sum are all one; arbitrary positive reweightings are not the original
problem. A theorem that the matrix B(r) is positive semidefinite for every
r would be much stronger and is already incompatible with the known finite
prefix test below. No such all-coefficient inference is being proposed.

In PR75's full-plane coordinates, k=n+m and l=n-m impose k=l modulo 2.
Both parity cosets and the coupling
`2*sinh(2t)*k*l` must be retained. Real diagonalization transports the lattice;
it does not turn it into independent integer coordinates. The half-line
formula above is just an absolutely convergent way to retain the same full
problem after reflection. It does not justify deleting either cosine or
either parity class.

## Why the immediate summation shortcuts stop

1. **Per-slice positivity is a known wall in its stated scope.** NS100's
   complete original slice has a certified negative cosine transform at
   frequency 40, and continuity extends this to nearby slices. Any proof
   requiring all such slices nonnegative is excluded. The full integral
   remains open.

2. **Unfolding before completing the lattice repeats NS101.** For the
   unreflected full-line summands, the absolute transform integral is a
   positive constant times n^(-x-1/2), where x is the real Laplace parameter.
   Summation is absolutely justified only for x>1/2, not at x=0 needed here.
   At x=1/2 NS101 even records the exact failure: each summand's transform
   is zero while the transform of the full sum is 1/4. PR76 repairs the
   complete primitive's boundaries; it does not license this different
   interchange.

3. **Finite square prefixes cannot be the nonnegative blocks.** Set
   H_M=sum_(n<=M) a_n and delta_M=sum_(n<=M) q_n'(0)>0. PR73 gives

   ```text
   L1[H_M](r) = -8*delta_M^2/r^6 + O_M(r^-8), r->infinity.
   ```

   Thus sum_(n,m<=M) B_nm is eventually negative for every fixed M.
   Its omitted terms, including mixed terms, cancel this leading negative
   asymptotic. Neither a small real-space tail nor diagonal-block positivity
   replaces that cancellation. Finite boundary repairs with a later nonzero
   odd jet have the corresponding PR73 obstruction. This is not a no-go for
   genuinely smooth infinite resummation or height-dependent approximants.

4. **Primitive structure is a known failed inference, not a lattice
   estimate.** The NS101 reciprocal mixture retains PR76's positive smooth
   primitive, envelope, unit tail and transform identities, yet J is negative
   in PR74's stated beta range. It changes the integer-square coefficients
   and original Jacobi IVP. That mismatch leaves an arithmetic method open;
   it does not count as a control pass for the present representation.

For example, writing X=H_M+T_M makes the required compensation explicit:

```text
2*H_M'*T_M' - H_M*T_M'' - T_M*H_M'' + L1[T_M]
    >= -L1[H_M],                    every real r.
```

This is exactly the missing target, not an independent tail estimate. The
mixed terms cannot be replaced by L1[T_M] alone. No lower bound for this
quantity follows from the representations reviewed here.

## Bounded prior-art applicability check

Rechecked only arXiv sources already closest to this proposed mechanism.
[Kharchev–Zabrodin I](https://arxiv.org/html/1502.04603v2), sections 3–4,
uses common moduli in its ordinary addition identities; the variables s+t
and s-t in this problem change moduli, not elliptic arguments.
[Kharchev–Zabrodin II](https://arxiv.org/html/1510.02699v1), Proposition 3.1,
does allow n1*tau and n2*tau with positive integers n1,n2 and retains the
full residue-class sum modulo n1+n2. Its imaginary-part hypothesis is
positive definiteness. The original scalar moduli match this restricted
form when exp(4t)=n1/n2. The proposition is an identity; it supplies neither
a signed lower bound nor transverse t-derivative estimates for PR75's
operator. Density of rational ratios does not provide those estimates.
No further theta-positivity theorem is imported or claimed absent globally.

## Conditional next paper check — not scheduled research

There is no unconditional additional 1–2 hour task to run from these results.
**Only if someone supplies an actual infinite Poisson/parity regrouping and
an independent signed estimating mechanism**, budget at most **2 hours**
for a completeness/admission check:

- Write its exact blocks, original coefficient weights, both parity classes,
  and equality to the complete double sum above. Verify all integration and
  differentiation exchanges, including every boundary and mixed term.
- Identify its separately proved arithmetic lower bound, valid for every
  real r; prove any error comparison uniformly through zeros and large r.
  Cancellation of finitely many reflection jets is insufficient. A putative
  margin must be independently estimated, not defined to equal J.
- Check the first step that fails for the explicit NS101 mixture, and check
  that no per-slice premise contradicts NS100. Davenport–Heilbronn does not
  have the original integer-square coefficients/completion, so it is not a
  matched test of a literal original-lattice hypothesis; generic algebra
  alone still supplies no distinction.

**Success** of that check would admit one sharply stated estimating lemma
for further work; success of the lemma plus its complete error transfer
would prove J>=0 and only the first-Laguerre target. **Failure** would stop
that supplied regrouping. Neither outcome closes the original lattice
method in general. If no regrouping and independent bound are supplied,
the completeness check has no input and should not be started.

**Final classification: Same open gap.** No viable signed lattice estimate
is admitted. RH, G2 and the cofinal signed-arithmetic lower bound remain open.
