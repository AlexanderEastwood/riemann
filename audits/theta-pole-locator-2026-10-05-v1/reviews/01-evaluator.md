# Agent 01 — original completed-theta diagnostic evaluator

Reviewed main `bc3ff0c962c485ac8104ce8cd832c119c260c871`, current AGENTS,
this audit's brief, and PR79 reviews 03, 05 and 06. The coordinator owns
the full-register refresh; this is not a replay of historical certificates.
Both missing-original recovery groups remain OPEN.

**Wall check: Distinct test.** Closest PR78/79, NS100/101. An original
uncancelled denominator zero would reject the general quotient-PD
sufficient construction. This implementation supplies a bounded locator's
values, not a signed estimate or zero certificate. The original complete
Laguerre target, RH and G2 remain open.

## Fixed protocol and output

`evidence/diag_theta_pole_locator/theta_eval.py` implements
`evaluate(z,bits=128,replay=False)`. It returns `m=B*M`, `c=B*C`, and
`dm=(B*M)'`, with

```text
B(z)=exp(2*pi*exp(2*z)-9*z)/(4*pi^4).
```

B is entire and nowhere zero. Thus it changes no denominator-zero or
cancellation question. Its logarithmic derivative is
`B'/B=4*pi*exp(2*z)-9`, which is included in `dm`; omitting it would
change Newton steps. Lattice and real-integration errors are multiplied
by `abs(B)`, and derivative errors additionally include `abs(B'/B)`
times the M error. The evaluator rejects points with `abs(Re z)>2`
or `abs(Im z)>5/8`; the locator separately retains the exact search box.

The preregistered initial calculation uses 128-bit ordinary mpmath,
lattice `n<=24`, and 48-point Gauss-Legendre quadrature on each segment
of `[0,1/8,1/4,1/2,1,2,4]`. The replay uses 256 bits, lattice `n<=32`,
96 points per segment, and appends endpoint `9/2`. Evenness in the real
integration variable supplies the negative half-line by multiplication
by two. No adaptive extra lattice, grid, precision or domain is hidden.

**There is no rigorous quadrature or roundoff enclosure.** These are
ordinary floating evaluations, including the evaluated analytic majorants.
The metadata says so explicitly. Replaying precision, cutoffs and
quadrature does not turn a diagnostic value into an interval certificate.

## Exact derivative and original arithmetic

For `Re u>=0`, write `t=pi*exp(2*u)` and
`S_j=sum_(n>=1) n^j*exp(-t*n^2)`. The complete original kernel satisfies

```text
phi(u)=exp(u/2)*(2*t^2*S_4-3*t*S_2),
phi'(u)=exp(u/2)*(-4*t^3*S_6+15*t^2*S_4-(15/2)*t*S_2).
```

These are the full original theta coefficients, truncated only with the
explicit majorants below. The recurrence for each finite lattice term
is `q^(n^2)` with `q=exp(-t)`, and successive ratio `q^(2*n+1)`;
this avoids repeated complex exponentials without changing coefficients.
For negative real part the implementation uses `phi(u)=phi(-u)` and
`phi'(u)=-phi'(-u)`. The finite truncations on the two sides need not
agree exactly at the switch; their discrepancy is within the lattice
error, and no derivative of a numerical switch is introduced.

The differentiated complete product is

```text
M'(z)=int_R [phi'(s+z)*phi(s-z)-phi(s+z)*phi'(s-z)] ds.
```

This integrand is also even in s. Analytic differentiation is used;
finite-difference derivatives and midpoint solves are not used.

## Explicit lattice and complete real-tail majorants

Set `a=abs(Im z)`, `b=pi*cos(2*a)>0`, `d=b/2`. For power `j` and
cutoff N, define

```text
n0=N+1,
r_j=((n0+1)/n0)^j*exp(-b*(2*n0+1)),
T_j=n0^j*exp(-b*n0^2)/(1-r_j).
```

The successive positive-term ratios decrease, so `T_j` majorizes the
entire omitted Gaussian lattice whenever `r_j<1`. Since
`b*(N+1)^2>=13/4`, each omitted `t^alpha*exp(-b*n^2*t)` decreases
on real `t>=1` for all exponents needed here. Uniformly in `Re u`,
reflection then gives

```text
E0=2*pi^2*T_4+3*pi*T_2,
E1=4*pi^3*T_6+15*pi^2*T_4+(15/2)*pi*T_2.
```

These bound the omitted phi and phi' lattice respectively. For the full
kernel envelopes, set

```text
S_j=sum_(n>=1) n^j*exp(-b*(n^2-1)),
F(alpha)=max_(t>=1) t^alpha*exp(-d*t),
K0=2*pi^2*S_4*F(9/4)+3*pi*S_2*F(5/4),
K1=4*pi^3*S_6*F(13/4)+15*pi^2*S_4*F(9/4)
   +(15/2)*pi*S_2*F(5/4).
```

The maximum is evaluated at `max(1,alpha/d)`. Each S is a finite
32-term sum plus the same geometric tail multiplied by `exp(b)`.
Thus `abs(phi^(j)(w+iv))<=Kj*exp(-d*exp(2*abs(w)))`, j=0,1,
throughout the applicable closed substrip. Let `Lj=Kj*exp(-d)`.
The unnormalized lattice-integral errors on `[-R,R]` are at most

```text
P=2*L0*E0+E0^2,
P1=2*(L0*E1+L1*E0+E0*E1),
M: 2*R*P,     C: (2*R^3/3)*P,     M': 2*R*P1.
```

For the complete discarded real tails, put `D=d*exp(2*R)`. PR79's
uniform estimate and the analogous derivative estimate give

```text
M: K0^2*exp(-D)/D,
C: K0^2*exp(-D)*(R^2/D+R/D^2+1/(2*D^3)),
M': 2*K0*K1*exp(-D)/D.
```

The derivative bound retains both product derivatives. All six majorants
are separately reported after the normalization and its derivative are
charged. Their floating evaluations are useful truncation diagnostics;
none bounds quadrature or arithmetic roundoff.

## Implementation checks before the original locator

No original M/C evaluation was performed by this agent before admission.
Synthetic checks used the cached quadrature rule alone on `x^20` and
`exp(-x^2)` over `[-1,1]`, compared with `2/21` and
`sqrt(pi)*erf(1)`. Absolute discrepancies were respectively
`7.3468397e-40`, `5.8774718e-39` at 128 bits/48 nodes, and
`1.7380289e-76`, `1.7272337e-76` at 256 bits/96 nodes. They check rule
assembly, not theta quadrature accuracy. The matched pole/removable-pole
controls belong to the locator agent.

Pyright on the touched evaluator: **0 errors, 0 warnings**. Runtime:
existing project Python with mpmath 1.3.0. No package installed. No git
operation, manuscript version, row claim, thaw or external outreach.
