DIAGNOSTIC, NOT A CERTIFICATE.

# NS-42 transformed energy budgets

First three generalized pencil directions k=0,1,2 at each existing λ=3,4; N=48 gives 49 even modes and 48 odd modes. All vectors have ordinary L² norm one. The even vectors are raw and are not asserted to be orthogonal to the actual source. Odd vectors have odd parity and hence no even-source constraint.

Set a=log λ. The physical coordinates are e₀(x)=1/√(2a), eₙ(x)=(-1)ⁿ cos(nπx/a)/√a in the even sector, and eₙ(x)=(-1)ⁿ sin(nπx/a)/√a in the odd sector, on (-a,a), extended by zero. The (-1)ⁿ factors are retained from the block() matrix convention. These are the first three eigenvectors of Wv=ν(W+W⁻)v, rather than the first three ordinary eigenvectors of W.

Use the unnormalized Gaussian weight h of eq:v150-weight, g=f/h inside the window and g=0 outside, c=cosh(x/2), s=sinh(x/2), Iₕ=1/√3 and dν=c h dx/Iₕ. J denotes the full squared-edge energy of eq:v150-global-energy; Jₐ denotes the same energy restricted to edges whose two endpoints are inside the window. E=∫(Tₐ/h)|f|² is the exterior edge contribution, so J=Jₐ+E. V=(2/3)Varν(g). The signed potential entry is R=∫rₐ|f|², with rₐ=(Tₐ−2Iₕc)/h. It is not ∫(rₐ)₋|f|². Π=2|∫cf|²−2|∫sf|²; S=2|∫sf|² is the nonnegative odd negative-pole magnitude. The identities are q=J−V−S and q=Jₐ+R+Π.

The pencil uses the original float W⁻ grid (0.001≤ξ<4000 with steps 0.002 and 0.01) and 1024-bit Arb W converted to midpoint mpmath arithmetic at 150 decimal digits. That defines the frozen diagnostic vectors; it is not an accuracy certificate for the pencil. Each vector is saved with 130 significant digits. Matrix q and pencil residuals are computed internally before decimal export; their printed residuals are not claims about exact arithmetic on the exported decimals.

Jₐ is measured directly from nonnegative squared-edge integrands, with continuous and prime parts saved separately. E and ∫c|f|²/h are independently integrated; the two pole moments are evaluated by analytic Fourier-basis formulas. Gauss–Legendre orders 96 and 144 use float64 nodes and weights with mpmath integrands at 70 and 90 decimal digits respectively. The Gaussian sum is numerically truncated at n=8, exterior prime sums at n=16λ, and exterior continuous integration at y=log(16λ); no truncation enclosure is claimed. The report displays the order-144 run. Both raw runs, all per-prime contributions, norms and residuals are archived.

| λ/parity/k | J global | V=2/3 Var | S odd pole | J local | R potential | Pi pole | q midpoint W |
|---|---:|---:|---:|---:|---:|---:|---:|
| 3/e/0 | 8.618567797e-03 | 8.618567797e-03 | 0.000000000e+00 | 8.618567443e-03 | -1.495836743e+00 | 1.487218176e+00 | 4.241907386e-38 |
| 3/e/1 | 6.575646232e+00 | 6.575646232e+00 | 0.000000000e+00 | 6.575646230e+00 | -7.381340285e+00 | 8.056940556e-01 | 3.138280287e-31 |
| 3/e/2 | 9.776229492e+01 | 9.776229492e+01 | 0.000000000e+00 | 9.776229491e+01 | -9.859688817e+01 | 8.345932584e-01 | 6.420031763e-25 |
| 3/o/0 | 2.950092119e+00 | 2.916897821e+00 | 3.319429848e-02 | 2.950092119e+00 | -2.916897820e+00 | -3.319429848e-02 | 1.511071171e-34 |
| 3/o/1 | 2.440443495e+01 | 2.434636001e+01 | 5.807493803e-02 | 2.440443494e+01 | -2.434636000e+01 | -5.807493803e-02 | 5.097930173e-28 |
| 3/o/2 | 3.773761463e+02 | 3.772739093e+02 | 1.022370059e-01 | 3.773761462e+02 | -3.772739092e+02 | -1.022370059e-01 | 4.110278768e-22 |
| 4/e/0 | 1.718285954e-03 | 1.718285954e-03 | 0.000000000e+00 | 1.718285954e-03 | -1.532519607e+00 | 1.530801321e+00 | 6.638601939e-66 |
| 4/e/1 | 7.803024725e+00 | 7.803024725e+00 | 0.000000000e+00 | 7.803024725e+00 | -8.788985977e+00 | 9.859612517e-01 | 7.111804775e-59 |
| 4/e/2 | 1.449350738e+02 | 1.449350738e+02 | 0.000000000e+00 | 1.449350738e+02 | -1.458816262e+02 | 9.465524764e-01 | 1.542746605e-52 |
| 4/o/0 | 3.196887695e+00 | 3.160870947e+00 | 3.601674738e-02 | 3.196887695e+00 | -3.160870947e+00 | -3.601674738e-02 | 2.959227654e-62 |
| 4/o/1 | 3.223600919e+01 | 3.216484214e+01 | 7.116704953e-02 | 3.223600919e+01 | -3.216484214e+01 | -7.116704953e-02 | 1.167085244e-55 |
| 4/o/2 | 7.285951227e+02 | 7.284923785e+02 | 1.027441569e-01 | 7.285951227e+02 | -7.284923785e+02 | -1.027441569e-01 | 1.707699543e-49 |

The largest order-144 absolute residual in J−V−S−q is 1.372400e-12; the largest quadrature norm error is 1.266663e-14. The largest change from order 96 to 144, divided by 1+the magnitude of the order-144 value, is 1.136848e-15 across J, Jₐ, V and R. These are diagnostic comparisons, not error bounds. The independent integrations do not resolve the tiny matrix q values. JSON fields named identity_reconstructed add q to the separately measured subtractive terms and are expressly not independent measurements of J.

## Replay

```sh
.venv/bin/python evidence/diag_ns42_energy_budget/freeze.py
.venv/bin/python evidence/diag_ns42_energy_budget/measure.py 3 even --order 96 --dps 70
.venv/bin/python evidence/diag_ns42_energy_budget/measure.py 3 even --order 144 --dps 90
# Repeat the two measure calls for 3 odd, 4 even, 4 odd.
.venv/bin/python evidence/diag_ns42_energy_budget/report.py
```

The original assembly may regenerate its sequence caches; they are not a separate certificate. The frozen vectors and all eight measurement outputs are archived here. Ordinary norm checks, per-prime terms and internal matrix residuals are saved. The HTML report is the delivered document.

Validation: actual base-v1.50 build 246 pages, zero undefined/duplicate references; Python diagnostics zero errors/warnings. No manuscript or map edits. Nothing in this diagnostic is cited as a bound.
