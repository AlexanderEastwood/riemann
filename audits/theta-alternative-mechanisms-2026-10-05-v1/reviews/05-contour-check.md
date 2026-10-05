# Independent review 05 — contour obstruction and its admission scope

**Decision:** the conditional pole obstruction is sound. Any nonremovable pole of the complete original quotient `k=C/M` inside `abs(Im z)<pi/4` excludes positive definiteness of k. No original pole has been located or certified. This would reject one sufficient certificate, not the complete first-Laguerre inequality J. A finite-box falsification is a useful audit target with a complete dependency edge, independently of the missing positivity estimator; it is not ready to run without an actual box and quantitative enclosures.

Reviewed baseline: `221ceec9da825bdc787111447badad961860760a` (PR78), scope commit `b5147e82803cccdb641bcb611b3c90c3c76cf51e`. Read AGENTS, this brief, proposer 03, and PR78's nonlocal construction and independent algebra review. I inherit the coordinator's complete conclusion-register review and did not replay historical certificates. Both missing-original recovery groups remain OPEN. Paper review only: no source theorem imported, computation, scan, certification, row, thaw, version, outreach, spawn or commit.

**Wall check: Same open gap — NS100/101, PR76–78.** The contour analysis changes the sufficient-certificate rejection criterion, not the original missing signed estimate. A future instantiated pole test would have a distinct falsification question; none is instantiated here.

## 1. Original analytic domain and axis nonvanishing

For `abs(Im z)<pi/4`, `Re(exp(2z))>0`; the complete theta series and its derivatives converge normally on compact subsets. The principal square root is `exp(z)`, so Jacobi inversion gives `h(-z)=h(z)` and hence even phi without crossing a branch cut. Conjugation preserves the original real coefficients. This establishes the asserted connected strip for the displayed series, not a maximal analytic-continuation domain.

For real u>=0 every original phi summand is positive because `2*pi*n^2*exp(2u)-3>0`; evenness covers negative u. Thus M(x)>0. For real y strictly within the strip,

```text
M(iy)=int_R abs(phi(s+iy))^2 ds>0,
C(iy)=int_R s^2*abs(phi(s+iy))^2 ds>0.
```

Strictness follows from analytic nontriviality: vanishing of either integral would force phi to vanish along a line, hence identically. These are complete integrals, not complex pointwise positivity claims. Off-axis zeros remain possible.

## 2. Uniform tails and saddle extension

The stated qualitative bounds can be justified explicitly. Fix `a<pi/4`, put `q=cos(2a)>0`, and define finite positive constants

```text
S_j(a)=sum_(n>=1) n^j*exp(-pi*q*(n^2-1)), j=2,4.
```

For w>=0 and |v|<=a, the original series gives

```text
abs(phi(w+i*v)) <= [2*pi^2*S_4(a)*exp(9w/2)
                     +3*pi*S_2(a)*exp(5w/2)]*exp(-pi*q*exp(2w)).
```

Reflection covers w<0. Absorbing the polynomial exponential factors yields an explicitly boundable K_a with

```text
abs(phi(w+i*v)) <= K_a*exp(-d_a*exp(2*abs(w))), d_a=pi*q/2.
```

Differentiated series yield corresponding derivative bounds. These establish local uniform convergence and differentiation of M/C throughout the strip. They also provide complete tails for an eventual certificate. For real-s truncation |s|<=R and z in a closed substrip, let `D=d_a*exp(2R)`. Since `max(abs(s+x),abs(s-x))=abs(s)+abs(x)`, valid absolute discarded-tail bounds are

```text
M tail <= K_a^2*exp(-D)/D,
C tail <= K_a^2*exp(-D)*(R^2/D+R/D^2+1/(2D^3)).
```

These follow from `exp(2(R+t))>=exp(2R)*(1+2t)` and retain both ends. They are loose uniform bounds, not evaluated certificates.

For x=Re z large, the central region |s|<=x/2 has both reflected kernel arguments with real parts >=x/2. Factoring out n=1 produces a relative remainder bounded uniformly by `O(exp(-c_a*exp(x)))`. The n=1 polynomial factors are uniformly separated from zero there. The exterior has absolute bound polynomial times `exp(-c'_a*exp(3x))`, including its s^2 weight.

For `A=2*pi*exp(2z)`, its argument stays in a closed sector inside `(-pi/2,pi/2)`. Expanding around s=0 and integrating the complex Gaussian gives the same coefficients as the real saddle; the errors are uniform since `Re A>=q*abs(A)`. The absolute Gaussian integral divided by the magnitude of its complex value is bounded by a constant depending on a. Consequently neither the lattice error nor exterior bound loses relative control through oscillatory cancellation. This validates

```text
M(z)=2*pi^4*exp(9z-A)*sqrt(2*pi/A)*(1+O(A^-1)),
k(z)=1/(4A)-1/(8A^2)+O(A^-3).
```

Evenness handles the other end. Thus M is zero-free at both sufficiently distant ends of each closed substrip. The remaining zeros lie in a compact subset of a larger open strip and are finite. This also justifies an unspecified small zero-free strip around the real axis. No finite threshold or explicit onset is established by the O notation.

## 3. Residues really force a sign change

Horizontal lines avoiding the finite pole set have integrable exponential end tails for k. The same uniform bounds make the contour's vertical sides vanish. For xi>=0, the upper shift therefore gives exactly

```text
K(xi)=exp(-eta*xi)*int_R k(x+i*eta)*exp(i*xi*x)dx
      +2*pi*i*sum Res[k(z)*exp(i*xi*z)].
```

Cancelled M zeros are removable; poles and all their Laurent coefficients must be retained. A simple upper pair `a+i*b, -a+i*b`, with residues `R,-conj(R)`, contributes `-4*pi*exp(-b*xi)*Im(R*exp(i*a*xi))`. The sign and factor check.

If a pole exists, finite zero counts supply a lowest positive pole height b. Select eta above b and below the next height. Among poles at b, select maximal order m. Distinct real parts supply distinct frequencies, so the leading residue polynomial cannot cancel identically. Imaginary-axis nonvanishing excludes zero frequency. Consequently

```text
K(xi)=exp(-b*xi)*xi^(m-1)*(T(xi)+O(1/xi))+O(exp(-eta*xi)),
```

where T is a nonzero real trigonometric polynomial of mean zero. For m=1 the lower-degree polynomial term is absent. To avoid an unnecessary almost-periodicity theorem: if `B=sup abs(T)` and S is the positive Cesaro mean of T^2, then `T^2<=B*abs(T)` and mean(T)=0 imply liminf averages of each positive/negative part are at least S/(2B). Each part therefore exceeds S/(4B) at arbitrarily large arguments. The lower errors cannot remove both signs. Positive definiteness of an integrable k requires K>=0, so the contradiction is valid for poles of any order.

The independently checked transform factors are `Fourier(M)(xi)=X(xi/2)^2/2`, `Fourier(C)(xi)=L1[X](xi/2)/4` and

```text
L1[X](r)=(1/pi)*int_R X(r-xi/2)^2*K(xi) dxi.
```

Negative K somewhere does not force this convolution negative. The obstruction stops at k-PD.

## 4. Matched controls and bounded certification prerequisites

An analytic pole control is `k_0(t)=1/(cosh(8t)+cosh(d))`, d>0. It is real-even, positive on both axes in the stated strip, exponentially decaying horizontally, and has poles `t=+/-d/8+i*pi/8`. The contour formula yields the sign-changing transform

```text
K_0(xi)=pi*sin(d*xi/8)/(4*sinh(d)*sinh(pi*xi/8)).
```

This checks the analytic implication and residue scaling, not original theta arithmetic. Conversely `k_1(t)=exp(-t^2)*(1+t^2)` is entire and positive on both real and imaginary axes within |Im t|<pi/4, yet its transform is `sqrt(pi)*exp(-xi^2/4)*(3/2-xi^2/4)`. Absence of poles and axis positivity do not suffice; this generic control does not match the original coefficients or tail asymptotic.

NS101 shares the quotient construction and contour calculus, but changes the lattice and IVP; its negative-Laguerre examples force failure of k-PD without locating a pole. NS100 does not exclude this complete-pair approach. DH does not instantiate the original completion, so its strip/quotient need separate verification before use. NS74/83 concern different NB hypotheses and quantifiers. None is a claimed successful arithmetic screen.

A one-box original falsification needs: a specified compact rectangle strictly off both axes and inside the strip; rigorous complete M, M' and C enclosures; explicit lattice/integration tails; a zero-free M boundary and positive certified argument-principle count; and C nonvanishing throughout the rectangle. Count >0 suffices without simplicity, because no enclosed M zero can then cancel. The contour winding must be enclosed rigorously, not inferred from sampled phase. Arb interval arithmetic, adaptive subdivisions and two-precision replay are prerequisites. A diagnostic point value would not establish any of them.

This is admissible in principle as a useful route-validation audit: a pole closes the specific quotient-PD certificate. No pole in one box only excludes that box; an inconclusive enclosure decides nothing. No original rectangle is supplied, and computing one by an unbounded or automatic search is not part of this admission. **No positivity estimator admitted; no instantiated box; zero scan budget.** J and RH remain open.
