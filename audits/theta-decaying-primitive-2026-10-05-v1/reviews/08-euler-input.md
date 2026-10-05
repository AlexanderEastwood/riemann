# Review 08 — logarithmic Euler input and its domain

**Disposition: PASS for the domain/identity audit; OPEN for the estimate.**

**Wall check: Same open gap.** Closest: NS100/101, PR74/75 and the
September 23 Abel-damping audit. What changes: the missing first-Laguerre
sign can be written with the original logarithmic Euler derivative, but
no new prime-sum estimate or transfer through the critical strip is given.
The fixed-damping NS47 obstruction has a narrower, different hypothesis
set and does not close this pointwise second-derivative question.

Reviewed baseline: `d93aaf6b8dbe1fcbebf6fff4f6d1f71d993f4208` (PR75).
I read AGENTS, this audit's brief and derivation, the WEIL-FLOOR continuation
scope, the board's Abel-damping entry, and that audit's proposal, results
and validation. The parent performed the full 104-node/14-group turn
review; this review does not claim to repeat every historical proof or
certificate. No numerical/symbolic scan or candidate proof was performed.

## 1. Exact expression, including the completion

Use `s=1/2+i*r`, `p=r^2+1/4`, and define the completed zeta factor without
the polynomial by

```text
Zc(s) = pi^(-s/2)*Gamma(s/2)*zeta(s),
xi(s) = s*(s-1)*Zc(s)/2.
```

Since `s*(s-1)=-p`, the draft's equation (5) gives, on the real r axis,

```text
X(r) = -p*Zc(s)/4,
Y(r) = -Zc(s).
```

Thus wherever `zeta(s) != 0`, ordinary logarithmic differentiation gives

```text
L1[Y](r)/Y(r)^2
  = Re[(zeta'/zeta)'(s) + psi1(s/2)/4],                 (E1)
```

where the prime on `zeta'/zeta` is differentiation with respect to s,
and `psi1` is the trigamma function. The sign follows from
`d/dr=i*d/ds`, so `-d_r^2 log Y=d_s^2 log Zc`. No choice of a global
logarithm is required: this is a local quotient identity away from zeros.
The expression inside `Re` is real on this zero-free portion of the
critical line, by the completed functional symmetry.

Consequently equation (10), away from those zeros, is exactly

```text
Re[(zeta'/zeta)'(1/2+i*r) + psi1(1/4+i*r/2)/4]
  >= 2*(1/4-r^2)/(r^2+1/4)^2.                         (E2)
```

Equivalently the full completed expression is

```text
L1[X](r)/X(r)^2
 = Re[-1/s^2 - 1/(s-1)^2
      + psi1(s/2)/4 + (zeta'/zeta)'(s)] >= 0.         (E3)
```

The two rational terms equal `2*(r^2-1/4)/p^2` on the critical line.
They are exactly the correction in draft equation (9); deleting them
would change the target, particularly for `abs(r)<1/2`. The factor
`pi^(-s/2)` contributes no second logarithmic derivative, but the gamma
and polynomial completion cannot be discarded.

At a real zero of X or Y, (E1)--(E3) are undefined. The draft's undivided
equations (9)--(10) remain valid there: `L1[X]=X'^2>=0`, including zero
for a multiple zero. Therefore an argument using (E2) needs every real
nonzero point, plus the undivided handling of zeros; it must not assert
a globally bounded logarithmic quotient. No simplicity assumption is
needed. This is a reformulation of the first-Laguerre target, not an
RH-equivalent conclusion or a new bound.

## 2. What the actual Euler product does and does not supply

The original prime-power coefficients give

```text
-zeta'/zeta(s) = sum_(n>=2) Lambda(n)*n^(-s),
(zeta'/zeta)'(s) = sum_(n>=2) Lambda(n)*log(n)*n^(-s),
Re(s)>1.                                               (E4)
```

These series and their indicated differentiation are absolutely and
locally uniformly convergent in this half-plane. Thus the real arithmetic
part there is

```text
sum_(n>=2) Lambda(n)*log(n)*n^(-sigma)*cos(r*log(n)).
```

Nonnegative coefficients do not give a nonnegative cosine sum. The
elementary absolute bound by `sum Lambda(n)*log(n)*n^(-sigma)` is a bound
in `sigma>1`; it does not supply (E2) on `sigma=1/2`.

Applying Abel damping `n^(-epsilon)` to the critical-line series makes
(E4) justified only for `epsilon>1/2`. Sending epsilon to zero crosses
the convergence boundary before reaching the requested line. Meromorphic
continuation of `(zeta'/zeta)'` exists, but this alone supplies neither
the termwise prime-series limit nor its one-sided lower bound. Its double
poles at zeros and the zeta pole must be respected in any contour or
transport argument. Any regularized prime representation must display
its correction/residue terms and estimate their complete signed sum;
no such estimate is present here.

The arXiv source already used by the older audit,
[Sondow--Dumitrescu, arXiv:1005.1104](https://arxiv.org/abs/1005.1104),
states horizontal monotonicity of the modulus in a zero-free half-plane.
Its stated conclusion concerns the first logarithmic derivative. It
does not, just by differentiation, establish the sign of the second
logarithmic derivative required in (E3), and the critical line is not a
zero-free right half-plane available unconditionally. I checked this
source's stated scope, not a new proof of its theorem.

## 3. Precise comparison with the recorded damping obstruction

`audits/prime-archimedean-screen-2026-09-23-v1/results.md` considers the
complete Weil comparison with fixed `epsilon>1/2` and multiplier

```text
m_epsilon(r) = 2*Re[xi'/xi(1/2+epsilon+i*r)].
```

Its rejected premise is an all-test, support-independent estimate
`q_epsilon[g]-q[g] <= C*||g||^2`. The positive multiplier grows like
`log(2+abs(r))`, and NS47 excludes domination by its ordinary-closable
unbounded square with that bounded error. This is the existing fixed-
damping wall, not a new result from this review.

(E2) is instead a pointwise second-logarithmic-derivative inequality.
It has not been shown to imply that forbidden all-test comparison, so
NS47 must not be cited as excluding (E2) or all Euler-based approaches
to it. What does transfer from the old audit is the explicit domain
failure of an unjustified shrinking-damping Euler-series argument.
A shrinking schedule does not by itself provide the missing estimate.

## 4. Matched-control status and stop decision

- NS101 shares the generic quotient/product and primitive identities,
  but its multiplicative frequency factor changes the original zeta
  data. It supplies no identical `Lambda(n)` Euler series or original
  nonlinear Jacobi IVP. Therefore it rejects the primitive-only
  inference in the draft, not the original arithmetic assertion (E2).
- Davenport--Heilbronn has different coefficients, conductor and gamma
  completion and lacks this original Euler product. It is not a matched
  control for the literal (E2)/(E4) package. This mismatch is not a pass.
- If the original arithmetic is reduced to generic smoothness,
  positivity or completed symmetry, the applicable existing controls
  again apply. Merely displaying `Lambda(n)` before discarding its
  relations does not discriminate the original object.

No actual original-arithmetic estimate is available from this bounded
review. A candidate would need an independent all-height lower estimate
for the complete left side of (E2), with its justified prime-side
representation, all zero neighborhoods and gamma correction retained.
Naming that desired estimate is not a method and does not meet the thaw
condition. Do not start a prime-prefix scan, an undamping scan or a new
row on the strength of (E1)--(E4).

**Final: OPEN; Same open gap.** The review sharpens where Euler data would
have to enter and prevents a convergence-domain substitution. It does
not provide the required estimate or rule out the original theta route.
