# Read-only symbolic and scalar-transfer review

Reviewed 2026-09-30. Files inspected: `check.mac`, `check-output.txt`, `transfer-audit.md`, and `construction-review.md`. The requested worksheet is named `check.mac`, not `parentcheck.mac`. This review independently checks the displayed mathematics against the source and recorded output. **The worksheet was not rerun.** The log records 25 passes and a total of 25; it also records loading a user initialization file before `kill(all)`. No effect on these identities was identified, but this is not described as an independent clean-initialization replay.

**Wall check: Same open gap.** Closest: PR69 and the two-prime construction audit. This validates the specified local geometry and the scope of one scalar realization; it supplies no complete arithmetic trace or positivity transfer. No MAJOR mathematical defect was found within this review's scope.

## 1. Contact identities and signs

Write `A=(1−by)/v`, `k=−v′A−b′y`, `α=A dt+y dx`, and `R=v∂t+b∂x+k∂y`. Direct expansion gives

    dα = A_x dx∧dt + A_y dy∧dt + dy∧dx,

    ι_R dα = (bA_x+kA_y)dt
               +(−vA_x+k)dx +(−vA_y−b)dy,

    α∧dα = (A−yA_y)dt∧dy∧dx
           = (1/v)dt∧dy∧dx.

These match the worksheet's three contractions and volume check. In the ordering `dt∧dx∧dy` the volume coefficient would instead be `−1/v`; the reported positive sign is correct for the stated ordering. The separate `α(R)=1` identity also matches. On the energy graph, `τ=A`, so `Rτ=bA_x+kA_y=0`; conservation of τ is genuinely one of the checked identities.

The checks establish algebraic equalities wherever their denominators are defined. They do not themselves prove `v>0` or regularity. The analytic specification supplies these: `a,c>0`, `v∈[min(a,c),max(a,c)]`, and `x²−x+1≥3/4`. Thus the denominators are harmless on the intended real domain and the volume never vanishes.

## 2. Transverse return and formal coupling checks

At `(x,y)=(j,0)`, j=0,1, the checked transverse infinitesimal matrix is

    L_j = [[β,0], [−v″(j)/v(j),−β]],  β=b′(j)=±1.

Its characteristic polynomial is `z²−1`, as recorded. Because `v′(j)=0`, the first variation of angular return time vanishes, so the analytic return-map discussion can use `exp(T_j L_j)`. The worksheet does not itself compute that exponential or prove the return time. Its separate arbitrary-shear identity

    det(I−[[r,0],[h,r^(−1)]]) = 2−r−r^(−1)

is correct, and equals the alternating exterior numerator. For r>1 this determinant is negative; that inequality uses the intended multiplier domain, rather than a Maxima sign certificate. A chosen half-density or scalar damping supplies the extra repetition weight. The symbolic passes alone do not construct its global bundle or a spectral trace.

The matrix `M=[[X,UX],[VY,Y]]` has determinant `det(I−M)=(1−X)(1−Y)−UVXY`. Both triangular specializations and the mixed logarithmic derivative at X=Y=0 correctly give the previously audited first mixed coefficient UV. These are formal scalar identities. Their extension to a particular contact return system, or to graded cancellations, remains a different question.

## 3. Challenge to the full scalar three-channel argument

The scalar transfer audit withstands the following checks. On each interval cut out by 0 and 1,

    u=log|x/(1−x)|−x,   u′=1/b,
    θ=t−F_I(x),          F_I′=v/b.

The worksheet checks the derivative on the interior corridor. The absolute-value expression gives the same derivative on both exterior intervals. Endpoint limits show each u map is onto R: it increases on `(0,1)` and decreases on both exterior components. Thus this is not merely a local straightening. Recovering x from u, then t from θ, and y from τ proves the coordinate map's global invertibility on each open strip.

Substitution gives the stronger exact identity `α=du+τdθ`, hence `R=∂u`. The signed Jacobian product used in the worksheet is −1 before coordinate-order accounting; its absolute value is one. The resulting positive measure is exactly `dθ dτ du`.

The invariant planes x=0,1 have zero contact-volume measure. Their deletion therefore loses no part of the scalar L² space. They are invariant, so this deletion also respects the flow. The resulting direct sum of three translation representations describes the **full scalar space**, rather than only a convenient invariant subspace. No boundary matching is missing at their strip ends: those ends occur at infinite u.

For `U_s f(u)=f(u−s)=exp(−isD)f`, the sign `D=−i∂u` is correct. Fourier transformation produces multiplication by ξ on the stated vector-valued Sobolev domain. This verifies the all-real, purely absolutely continuous spectrum and absence of scalar L² eigenvalues. The periodic circles cannot produce eigenvectors supported on measure-zero sets. Infinite measure is compatible with this spectral measure; it is ordinary trace-classness that fails. A nonzero bounded time-smearing still has the unchanged infinite transverse multiplicity and cannot be an ordinary trace-class replacement.

## 4. Limits of this validation

The 25 identities do **not** establish completeness, exhaust all closed orbits, determine recurrence/trapping, or prove the full scalar spectral decomposition. Those require the separate bounded-coefficient, monotonicity, coordinate-range, measure and functional-analysis arguments. Their presentation is consistent with the algebra inspected here.

The construction review also supplies a smooth weighted horizontal-form transport using an assigned scalar cocycle. This does not contradict the transfer audit's missing *intrinsic unstable-line/closed-realization* claim: the assigned cocycle, a global unstable bundle, and the scalar contact-volume operator are different objects. Its cutoff distributional flat trace is not the nonexistent ordinary scalar trace. No closed weighted domain, full prime assembly, archimedean completion, Weil parity/source identification or uniform signed estimate is certified by this review.

**Final wall: Same open gap.** The scoped construction and scalar-spectrum conclusions survive this read-only review. RH, G2 and the registered global arithmetic transfers remain open.

## Provenance clarification resolved

After the initial review, the parent preserved `check-output.txt` and reran the unchanged worksheet with `--no-init --quit-on-error --very-quiet`. I inspected the resulting `check-clean-output.txt` without rerunning it. It contains the same 25 named passes and `TOTAL_PASSED 25`, with no startup-initialization line. This resolves the initialization provenance qualification for the authoritative parent replay. My contribution remains read-only source/output inspection and independent checking of the displayed arguments; it is not a separate execution of the worksheet. No mathematical conclusion or tested identity changed.
