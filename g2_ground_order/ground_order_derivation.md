# Shifted Schur inertia: adversarial proof audit

21 September 2026. The new shifted computations have passed at the unequal parity thresholds specified in the final section, with exact-witness replays at higher precision. The abstract common-threshold argument is retained below to make the inertia logic explicit. The existing v1.16 result already supplies strict positivity of the complete fixed-window form at lambda=3.

## Exact shift bookkeeping

Let W denote the canonical self-adjoint Weil operator at lambda=3, with its established logarithmic operator/form domains and compact resolvent. It commutes with reflection and splits into its even and odd sectors. Fix an exact rational threshold a>0. In a chosen sector decompose

\[
 W-aI=\begin{pmatrix}F-aI&B^*\\B&T-aI\end{pmatrix},\qquad T_a=T-aI.
\]

The off-diagonal sequence b_n is unchanged. Every actual diagonal d_n and every inverse-majorizing weight g_n must be replaced by d_n-a and g_n-a respectively. In particular the common-cut loss constants are retained; shifting does not authorize a new distant-cut denominator for the whole inverse.

For the same exact frozen finite-support witness Z,

\[
 K_{Z,a}=K_{Z,0}-a(I+Z^*Z),\qquad
 R_a=B-T_aZ=R_0+aZ.
\]

The second identity changes all intermediate residual rows where Z is supported. Outside that support the residual is unchanged. The remote moment matrix, including its complete leading Gram and geometric remainder, is unchanged because G=I-Z and all remote rows see only unchanged off-diagonal entries. The new finite lower matrix is

\[
 L_a=K_{Z,a}-\sum_{N<n\le J}\frac{R_{a,n}^*R_{a,n}}{g_n-a}
                   -\frac{U_J}{g_{J+1}-a}.
\]

Here n runs over normalized positive-index parity rows, and U_J is evaluated in the full signed-index embedding. If g_{N+1}>a, the existing inverse-order proof gives the exact form-order inequality

\[
 S_a:=F-aI-B^*T_a^{-1}B\succeq L_a.
\]

Subtracting aI only from the final unshifted lower matrix would be invalid: it misses the aZ residual and the change of inverse weights.

## Inertia implication, including exclusion of a threshold eigenvalue

Assume the even lower matrix L_a has one strictly negative eigenvalue and all its other eigenvalues strictly positive; assume the odd lower matrix is positive definite. A complete interval LDL factorization whose every pivot excludes zero and whose sign count is exactly one negative certifies the stated even inertia. Pivot sizes do not certify eigenvalue sizes. A routine that stops after the first negative pivot is not an inertia certificate.

For the even matrix, finite-dimensional min--max and S_a>=L_a show that its second eigenvalue is strictly positive. Thus S_a has at most one nonpositive eigenvalue. This stronger conclusion is needed: merely bounding the number of strictly negative eigenvalues would not by itself exclude a zero eigenvalue at a.

Let u be the existing finite-supported, normalized, even rational candidate, embedded in the complete space. Its certified Rayleigh value is

\[
 \alpha=\langle Wu,u\rangle<r:=5.32\,10^{-38}.
\]

The finite compression evaluates this full quadratic form exactly because u has no omitted input coefficients. There is no finite-to-infinite approximation in this Rayleigh statement. If r<a, then the even shifted form is negative on u. Since T_a is positive, the square-completion identity

\[
 q_a[x+y]=\langle S_ax,x\rangle+
       \|T_a^{1/2}(y+T_a^{-1}Bx)\|^2
\]

forces S_a to have a strictly negative direction. Therefore its first eigenvalue is strictly negative and its second is strictly positive. In particular S_a is invertible, has precisely one negative eigenvalue, and has no zero eigenvalue. The odd Schur matrix is positive definite by its lower matrix.

The square-completion map is boundedly invertible on the Hilbert direct sum and preserves the form domain, since T_a^{-1}B maps the finite head into the operator domain of T_a. It identifies the negative index of q_a with that of S_a. Also

\[
 \ker(W-aI)\cong\ker S_a,
 \qquad x\longmapsto x-T_a^{-1}Bx.
\]

Consequently the complete even operator has exactly one eigenvalue below a, counted with multiplicity, and no eigenvalue at a; the odd operator has none at or below a. Compact resolvent excludes continuous spectrum or finite accumulation at the threshold. Writing the complete eigenvalues in increasing order as mu_0<=mu_1<=..., the conclusion is

\[
 0<\mu_0<r<a<\mu_1.
\]

The initial strict positivity is the previously proved v1.16 result. The new shifted argument supplies simplicity and evenness of the actual complete ground state and a gap mu_1-mu_0>a-r. For a=10^-36 this gives a gap greater than 9.468 x 10^-37; for a=10^-34 it gives a gap greater than 9.99468 x 10^-35. These numerical statements remain conditional until the corresponding shifted inertia certificates pass.

The same argument can alternatively avoid invoking compact resolvent for the gap: the positive part of the finite Schur matrix and the positive entire tail have a positive common lower bound; the bounded square-completion map transports this to a positive bound on a closed codimension-one subspace. Min--max then gives a strictly positive second shifted spectral value. Compact resolvent is already established here and is the simpler formulation.

## Actual ground overlap after the gap is proved

The two parity thresholds need not be equal. It is enough that the even lower Schur matrix has one negative pivot at a_even, the odd lower matrix is positive at a_odd, and both thresholds exceed the even Rayleigh upper bound r. Then the ground is simple and even; the full second eigenvalue exceeds min(a_even,a_odd). For an exactly even trial vector, every overlap estimate below may nevertheless use a_even: its spectral expansion has no odd component. This preserves the stronger even-sector angle bound when the odd certificate requires a smaller threshold.

Let xi_0 be a unit complete ground eigenvector and P_0 its rank-one orthogonal projection. Prior positivity and the new bound mu_1>a yield, for every unit vector v in the form domain with Rayleigh value beta,

\[
 \beta\ge a\|(I-P_0)v\|^2.
\]

For the exact rational source candidate u this gives

\[
 \sin\angle(u,\xi_0)<\sqrt{r/a}.
\]

Thus the overlap conclusion concerns the actual infinite-dimensional ground state, not merely its finite compression. The bounds are sin(angle)<0.230652 at a=10^-36, or <0.0230652 at a=10^-34. Without the previous nonnegativity, the formula would require an independent lower spectral bound ell and become sin^2(angle)<(alpha-ell)/(a-ell); a possibly negative unknown ground would not permit the displayed r/a bound.

There is a modest improvement from the already certified finite inverse solve. In the N=64 compression let

\[
 A=C-\alpha I,\quad z=A^{-1}r_{\rm fin},\quad q=\|z\|,
 \quad E=\langle z,r_{\rm fin}\rangle.
\]

The vector v=(u-z)/sqrt(1+q^2) is finite-supported and has the exact full-form Rayleigh value

\[
 \beta=\alpha-\frac{E}{1+q^2}.
\]

This follows from z perpendicular to u, <Wu,z>=E, and <Wz,z>=E+alpha q^2. Existing enclosures give alpha<5.312382 x 10^-38, E>1.668982 x 10^-38, and q<0.000216. Elementary rational arithmetic therefore gives beta<3.644 x 10^-38. Also ||P_u-P_v||=q/sqrt(1+q^2)<0.000216. The triangle inequality for rank-one orthogonal projections gives

\[
 \sin\angle(u,\xi_0)
 <0.000216+\sqrt{3.644\,10^{-38}/a}.
\]

Conservative decimal bounds are 0.19112 at a=10^-36 and 0.01931 at a=10^-34. This does not assume that the finite ground is the complete ground, nor that either is the exact PSWF source.

`certify_ground_overlap_constants.py` checks these scalar inequalities against the existing interval certificate. At 256 bits it certifies the conservative trial Rayleigh upper value 3.643400077868021 x 10^-38 < 3.644 x 10^-38 and the two sine upper values 0.191108639983841 and 0.019305263998385. The scalar output is `ground_overlap_scalar_certificate.json`. It does not supply the separate shifted inertia hypotheses.

For another normalized vector v_true with a rigorously bounded projector distance ||P_true-P_u||<=delta, add delta to either actual-ground angle bound. The existing certified approximation of the exact N=64 source projection may be used this way if its normalization error is retained. The full unprojected source additionally needs its omitted ordinary-norm tail. Point evaluation is unbounded in ordinary L2, so none of these angle bounds establishes endpoint recovery or endpoint relative error.

A genuine full-operator residual bound epsilon=||(W-beta)v|| supplies the additional standard estimate sin(angle(v,xi_0))<=epsilon/(a-beta), provided beta<a. Only the residual of the complete operator is admissible; a truncated residual cannot replace it. This optional estimate has not been evaluated here.

## Scope and implementation gates

1. All shifted LDL pivots must be enclosed and must exclude zero. Indefinite elimination needs signed pivots; replacing them by magnitudes changes inertia and invalidates the certificate.
2. Freeze the same exact Z, retain shifted intermediate residuals, use shifted diagonal weights, and leave only remote off-diagonal formulas unchanged.
3. A lower matrix with two negative pivots is inconclusive about whether the exact complete form has two eigenvalues below a. It does not disprove a simple ground or the chosen spectral gap.
4. A one-negative lower matrix alone is insufficient to assert any negative exact eigenvalue: the separate Rayleigh witness supplies that direction.
5. No LDL pivot is converted into an operator eigenvalue bound. The threshold a is certified by inertia; the upper bound r comes from the exact finite-supported Rayleigh witness.
6. This would establish fixed-window parity, simplicity, a spectral threshold, and ordinary Hilbert overlap. It does not establish a uniform family of such bounds, ground-state endpoint control, G2, or RH. The sampler graph defect is unchanged.

## Initial shifted computations: scope correction

The parent's 768-bit run at a=10^-34 certified exactly one negative even lower-matrix pivot (index 24), but the odd lower matrix also had one negative pivot (index 85). The latter does not pass the needed odd positivity gate. It is not a proof of an actual odd eigenvalue below 10^-34. The same exact even witness passed its 896-bit replay with the identical sign count and witness hash. The proposed resolution is to retain the strong even threshold and use a smaller odd threshold above the trial Rayleigh value; the overlap observation above then retains its strong even threshold.


## Completed shifted certificate and accepted conclusion

The same exact frozen witnesses were replayed successfully at 896 bits:

| Sector | Threshold | Dimension | Negative pivots | Positive pivots |
|---|---:|---:|---:|---:|
| Even | 10^-34 | 257 | 1 (index 24) | 256 |
| Odd | 10^-36 | 512 | 0 | 512 |

Every pivot excludes zero. The 768-bit and 896-bit witness hashes match exactly in each sector:

- Even: `993c5b325c1cc7dce64c1dbdab9384dd54dea6a480cce8739cf623e9e8bce43c`.
- Odd: `4054507110d6a806c3dfa926c716c1692de4c9b7dc7801263d50b92cbd8dfdea`.

The shifted script updates the true diagonal before every block or residual-row construction, subtracts the exact rational shift from the full diagonal lower function, retains all frozen-solve residuals, and correctly continues interval LDL through negative pivots. The remote moment bound is unchanged for the justified disjoint-support reason. No blocking issue was found in the proof or implementation. The replay shares the same Arb arithmetic and code; it is not a separate software implementation or external review.

Combining the accepted inertia counts, previous complete positivity, and the new finite-supported trial proves that the complete lambda=3 ground is simple and even, with

\[
0<\mu_0<3.644\,10^{-38},\qquad \mu_1>10^{-36}.
\]

Thus its full spectral gap exceeds 9.6356 x 10^-37. Within the even sector all non-ground eigenvalues exceed 10^-34. The exact rational candidate and the previously certified normalized exact N=64 source projection each have sine angle less than 0.01931 to this complete ground direction.

These conclusions are confined to lambda=3. No ground-state endpoint estimate, unprojected-source comparison, uniform growing-window result, G2 closure, or RH proof is inferred. The earlier odd test at 10^-34 remains an unsuccessful sufficient lower-bound test and is not evidence of a negative or unusually low odd eigenvalue. No further sign experiments were run after the successful replay.
