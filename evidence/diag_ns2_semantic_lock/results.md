# Diagnostic (semantic lock); not a certificate.

NS-2: reproduce one of Connes–Consani–Moscovici's own §6 numerical values
(arXiv:2511.22755v1, *Zeta spectral triples*, 27 Nov 2025) from this
repository's assembly of the semilocal Weil form
(`evidence/v124/g2_schur_cancellation/assembly_general.py`).

Script: `reproduce_ccm.py` (this directory).  Run from the repository root
with the project venv.  Eigensolves are mpmath midpoint solves; matrix
entries are Arb balls.  Nothing here is a bound.

## 1. What CCM actually print in §6 (quoted)

CCM ship no code or ancillary files.  The numbers in §6 are **not**
eigenvalues of the Weil form; they are distances between zeta zeros and the
spectrum of their perturbed scaling operator.  Verbatim (p. 25–27):

> "One computes using the above formulas the matrix of the Weil quadratic
> form and the spectrum of the operator D_log^{(λ,N)}.  These computations
> require high precision but are easily preformed using 200 digits accuracy
> due to the fast convergence of the special functions involved.  The first
> case is λ = 3 and one takes N = 120."

Figure 1 caption: "This shows the differences between the first twenty zeros
of ζ(1/2 + is) and the eigenvalues of the operator D_log^{(λ,N)} for λ = 3 and
N = 120."  The plotted values (read from the figure's text layer) are

    ρ1 1.6e-34   ρ2 2.1e-31   ρ3 1.5e-29   ρ4 8.3e-27   ρ5 1.3e-25
    ρ6 1.2e-23   ρ7 7.5e-22   ρ8 6.6e-21   ρ9 1.2e-18   ρ10 8.8e-18
    ρ11 7.3e-17  ρ12 2.2e-15  ρ13 9.7e-14  ρ14 2.7e-13  ρ15 6.3e-12
    ρ16 5.6e-11  ρ17 2.9e-10  ρ18 1.2e-9   ρ19 5.6e-8   ρ20 2.4e-7

> "We then consider the first fifty zeros of zeta, use still N = 120 and the
> values of λ given by λ = √12 ∼ 3.4641, λ = √13 ∼ 3.60555, λ = √14 ∼ 3.74166.
> We get the following table giving an upper bound on the absolute value of
> the difference between the nontrivial zeros of the Riemann zeta function
> ζ(1/2 + is) and the eigenvalues of the operator D_log^{(λ,N)}."

Table (first rows; the full 50-row table is transcribed in
`reproduce_ccm.py`, `CCM_TABLE`):

    k    λ=√12         λ=√13         λ=√14
    1    3.41e-50      2.44e-55      1.07e-60
    2    5.89e-47      4.5e-52       2.08e-57
    3    5.18e-45      4.16e-50      2.e-55
    ...
    50   9.02e-2       2.04e-3       4.78e-6

The abstract's headline "2.5 × 10^{-55} for the first zero" is the λ=√13,
k=1 entry (2.44e-55); the "10^{-1235}" is a heuristic probability, not a
computed quantity, and is not reproducible.

The only place CCM show the lowest eigenvalue ε_λ itself is Figure 4, a plot
of log(ε_λ) against μ = λ² with no printed values; from the plot,
ln ε_λ ≈ −90 at μ = 9 and ≈ −150 at μ = 14 (read to ±5).

**Definition of the quantity** (§5.1, §5.6, Thm 5.10).  τ_{n,m} =
QW_λ(V_n, V_m), |n|,|m| ≤ N, V_n = κ(U_n), U_n(x) = L^{-1/2} e^{2πinx/L} on
[0, L], L = 2 log λ.  ε_N = smallest eigenvalue of τ (assumed simple, even
eigenvector ξ).  Theorem 5.10 (iii): the spectrum of D_log^{(λ,N)} is the
real zero set of

    ξ̂(z) = 2 L^{-1/2} sin(zL/2) Σ_{|j|≤N} ξ_j / (z − 2πj/L).       (CCM 5.25)

So the §6 numbers are |γ_k − z_k| with z_k the zero of ξ̂ nearest γ_k.

## 2. Convention dictionary (CCM → this repository)

CCM's matrix (Lemma 5.1): τ_{i,i} = a_i, τ_{i,j} = (b_i − b_j)/(i − j),
a_{−j} = a_j, b_{−j} = −b_j, with
b_n = −(1/π) ∫_0^L sin(2πny/L) D(y) dy, a_n = 2 ∫_0^L (1 − y/L) cos(2πny/L) D(y) dy,
D = log_*(Ψ♯), Ψ♯ = W♯_{0,2} − W♯_R − Σ_p W♯_p (CCM 3.13).

| item | CCM (arXiv:2511.22755) | `assembly_general.py` / manuscript | status |
|---|---|---|---|
| window | [λ^{-1}, λ], L = 2 log λ, λ > 1 real | `L=2*arb(lam).log()`, λ integer only (`pairs(lam)`, `arb(lam)`) | same; non-integer λ needs the transcription `sequences_M` (λ² = M integer) |
| basis | V_n = κ(U_n), orthonormal in L²([λ^{-1},λ], d*u), n ∈ Z, |n| ≤ N | same U_n = L^{-1/2}e^{2πinx/L} ("normalized logarithmic Fourier basis", eq. v114-weil-decomposition) | same |
| parity reduction | none (full 2N+1 matrix) | even block on e_0, (e_m+e_{−m})/√2; odd block on (e_m−e_{−m})/√2; zero-mode entries √2·b_m/m | exact unitary reduction of the same matrix |
| Hermitian convention | antilinear in the first slot (CCM §2.1) | linear in the first slot | irrelevant here: τ is real symmetric |
| pole term W_{0,2} | 32L sinh²(L/4)(L² − 16π²mn)/((L²+16π²m²)(L²+16π²n²)) (Lemma 4.1) | b_n ∋ 32Lh n/(L²+16π²n²), d_n ∋ 32Lh(L²−16π²n²)/(L²+16π²n²)², h = sinh²(L/4) | identical: (b_n−b_m)/(n−m) reproduces Lemma 4.1 exactly |
| prime term | −Σ_{1<k≤e^L} Λ(k)k^{-1/2} q(U_n,U_m)(log k) (4.3) | b_n ∋ +(1/π)Σ Λ(m)m^{-1/2} sin(t_n log m), d_n ∋ −2Σ Λ(m)m^{-1/2}(1−log m/L)cos(t_n log m), over prime powers m < λ² | identical; the endpoint k = λ² (present in CCM, absent in `pairs`) contributes exactly 0 since q(·)(L) = 0 |
| archimedean off-diagonal | −W_R(V_n,V_m) = (α_L(n) − α_L(m))/(n − m), α_L(n) = (1/π)∫_0^L sin(2πnx/L)ρ(x)dx (Prop. 4.3) | b_n ∋ (1/π)∫_0^L ρ(y) sin(t_n y) dy, evaluated as −½ Im ψ(¼ − it_n/2) − Σ_k λ^{−(4k+1)} t_n/((2k+½)²+t_n²) | identical (closed form checked by hand: ρ = Σ_k e^{−(2k+½)y}, tail ∫_L^∞ uses t_nL = 2πn) |
| archimedean diagonal | −W_R(V_n,V_n) = −2γ_L(n) + 2β_L(n) with (4.4): W_R(V_n,V_n) = 2w(L) + 2∫_0^L(cos(t_nx) − e^{−x/2})ρ dx − (2/L)∫_0^L x cos(t_nx)ρ dx, w(L) = ½(γ+log 4π) − ½ log((e^L+1)/(e^L−1)) | a_n = Re ψ(¼ − it_n/2) − log π + Re ψ′(¼ − it_n/2)/(2L) − (2/L)Σ_k λ^{−(4k+1)}(c_k²−t_n²)/(c_k²+t_n²)² | identical after regularization: the divergent Σ c_k/(c_k²+t²) and Σ 1/(2k+1) combine to Re ψ + γ + 2 log 2, and −2w(L) cancels the artanh(λ^{-2}) remainder, leaving −log π (derivation in §5 below) |
| sign of the whole form | QW = W_{0,2} − W_R − Σ W_p | same signs on b_n and d_n (checked term by term above) | same |
| overall scale | τ as above | τ as above | **not tested by §6**: the zero set of ξ̂ is invariant under τ → cτ + sI |
| truncation | E_N = span{V_n : |n| ≤ N}, N = 120 | J = 120 (n = 0..120 in each parity block) | same |
| archimedean series cutoff | "200 digits accuracy" via 2F1/Φ series in e^{−2L} | K = 96 terms of ρ = Σ e^{−(2k+½)y} with a rigorous tail radius λ^{−(4K+1)} (≈ 1e-184 at λ=3) | different evaluation, same function; balls carry the tail |

Where CCM's text is ambiguous: (4.14) defines γ_L(n) with (cos − e^{−x/2})
under the integral *and* adds c(L), whereas (4.11) says ∫(cos − e^{−x/2})ρ =
∫(cos − 1)ρ + c(L); the two readings differ by 2c(L) on the diagonal.  Only
the reading γ_L(n) = ∫(cos − 1)ρ + c(L) + w(L) is consistent with (4.4), and
that reading equals the repository's a_n.  If CCM had coded the other reading
their diagonal would be shifted by the constant 2c(L)·(−1) — an identity
shift, invisible in §6.  So this ambiguity cannot be resolved by §6 either.

## 3. Adaptation for λ = √12, √13, √14

`sequences(lam, J, bits)` takes integer λ (`range(2, lam*lam)`, `arb(lam)`,
`lam**4`).  `reproduce_ccm.sequences_M(M, J, bits, K)` is a line-by-line
transcription with λ² = M:

    2 log λ → log M,   λ^{−(4k+1)} → M^{−2k}/√M,   λ^{−4} → M^{−2},
    pairs(λ) → prime powers 1 < m ≤ M  (CCM's range; endpoint term is 0).

Cross-check at λ = 3 (M = 9), J = 120, 1024 bits: the transcription and the
original agree entry by entry within the ball radii (`transcription_xcheck`
in `runs/run_M9_*.json`: max |mid diff| 5.0e-187, max radius 6.7e-187 at both
1024 and 1536 bits — the radius is set by the K = 96 archimedean tail
λ^{−(4K+1)}, not by the working precision — `overlap_all: true`).

## 4. Results

All runs: N = 120 (matrix 241x241, reduced to the even 121x121 and odd 120x120 blocks), K = 96,
zeta zeros from `mpmath.zetazero` at >= 220 digits.  Two precisions per case: assembly
1024 bits / eigensolve-roots 220 digits, and 1536 bits / 300 digits.

### 4.1 Ground of the truncated form (midpoint eigensolves; not bounds)

| lambda | bits/dps | eps_N (lowest, even) | second even | lowest odd | even-simple | Arb Rayleigh quotient of the midpoint vector | max entry radius | ln eps_N | Fig. 4 (by eye) |
|---|---|---|---|---|---|---|---|---|---|
| 3 | 1024/220 | 2.9540580925e-38 | 2.1461011279e-31 | 1.1275632641e-34 | True | [2.9540580925585e-38 +/- 1.24e-78] | 1.4e-186 | -86.4 | ~ -90 |
| 3 | 1536/300 | 2.9540580925e-38 | 2.1461011279e-31 | 1.1275632641e-34 | True | [2.9540580925585e-38 +/- 1.24e-78] | 1.4e-186 | -86.4 | ~ -90 |
| sqrt(12) | 1024/220 | 5.1220197336e-54 | 1.6932114544e-46 | 4.0388151226e-50 | True | [5.1220197336635e-54 +/- 4.22e-94] | 4.0e-211 | -122.7 | ~ -128 |
| sqrt(12) | 1536/300 | 5.1220197336e-54 | 1.6932114544e-46 | 4.0388151226e-50 | True | [5.1220197336635e-54 +/- 4.22e-94] | 4.0e-211 | -122.7 | ~ -128 |
| sqrt(13) | 1024/220 | 3.4839881993e-59 | 1.3118542845e-51 | 3.0559133975e-55 | True | [3.4839881993312e-59 +/- 4.12e-99] | 8.2e-218 | -134.6 | ~ -140 |
| sqrt(13) | 1536/300 | 3.4839881993e-59 | 1.3118542845e-51 | 3.0559133975e-55 | True | [3.4839881993312e-59 +/- 4.12e-99] | 8.2e-218 | -134.6 | ~ -140 |
| sqrt(14) | 1024/220 | 1.4598129516e-64 | 9.3843336472e-57 | 1.6680022583e-60 | True | [1.4598129516305e-64 +/- 2.89e-104] | 5.2e-224 | -147.0 | ~ -153 |
| sqrt(14) | 1536/300 | 1.4598129516e-64 | 9.3843336472e-57 | 1.6680022583e-60 | True | [1.4598129516305e-64 +/- 2.89e-104] | 5.2e-224 | -147.0 | ~ -153 |

Precision stability: the two precisions agree to every digit shown (the JSON files carry 40 digits of eps_N and of each z_k; they are identical between the two runs for every case).

### 4.2 |gamma_k - z_k| here versus CCM's printed values

**lambda = 3** (CCM: Figure 1; sign changes of xi_hat on [0, gamma_20+1]: 20 = number of zeros used, so no extra real zeros below gamma_20).

| k | gamma_k | here (1024/220) | here (1536/300) | CCM | ratio here/CCM |
|---|---|---|---|---|---|
| 1 | 14.13472514173 | 1.5823297e-34 | 1.5823297e-34 | 1.6e-34 | 0.989 |
| 2 | 21.02203963877 | 2.0605503e-31 | 2.0605503e-31 | 2.1e-31 | 0.981 |
| 3 | 25.01085758014 | 1.4609049e-29 | 1.4609049e-29 | 1.5e-29 | 0.974 |
| 4 | 30.42487612585 | 8.2936869e-27 | 8.2936869e-27 | 8.3e-27 | 0.999 |
| 5 | 32.93506158773 | 1.279456e-25 | 1.279456e-25 | 1.3e-25 | 0.984 |
| 6 | 37.58617815882 | 1.1743895e-23 | 1.1743895e-23 | 1.2e-23 | 0.979 |
| 7 | 40.91871901214 | 7.5284866e-22 | 7.5284866e-22 | 7.5e-22 | 1.004 |
| 8 | 43.32707328091 | 6.5658743e-21 | 6.5658743e-21 | 6.6e-21 | 0.995 |
| 9 | 48.00515088116 | 1.1879477e-18 | 1.1879477e-18 | 1.2e-18 | 0.990 |
| 10 | 49.77383247767 | 8.7872346e-18 | 8.7872346e-18 | 8.8e-18 | 0.999 |
| 11 | 52.97032147771 | 7.2845222e-17 | 7.2845222e-17 | 7.3e-17 | 0.998 |
| 12 | 56.44624769706 | 2.2126179e-15 | 2.2126179e-15 | 2.2e-15 | 1.006 |
| 13 | 59.34704400260 | 9.7491479e-14 | 9.7491479e-14 | 9.7e-14 | 1.005 |
| 14 | 60.83177852460 | 2.6960644e-13 | 2.6960644e-13 | 2.7e-13 | 0.999 |
| 15 | 65.11254404808 | 6.3407719e-12 | 6.3407719e-12 | 6.3e-12 | 1.006 |
| 16 | 67.07981052949 | 5.6332421e-11 | 5.6332421e-11 | 5.6e-11 | 1.006 |
| 17 | 69.54640171117 | 2.9303579e-10 | 2.9303579e-10 | 2.9e-10 | 1.010 |
| 18 | 72.06715767448 | 1.2163706e-9 | 1.2163706e-9 | 1.2e-09 | 1.014 |
| 19 | 75.70469069908 | 5.5763241e-8 | 5.5763241e-8 | 5.6e-08 | 0.996 |
| 20 | 77.14484006887 | 2.4157751e-7 | 2.4157751e-7 | 2.4e-07 | 1.007 |

ratio range: 0.974 .. 1.014; max |ratio - 1| = 0.026

**lambda = sqrt(12)** (CCM: table p. 26-27; sign changes of xi_hat on [0, gamma_50+1]: 50 = number of zeros used, so no extra real zeros below gamma_50).

| k | gamma_k | here (1024/220) | here (1536/300) | CCM | ratio here/CCM |
|---|---|---|---|---|---|
| 1 | 14.13472514173 | 3.4076325e-50 | 3.4076325e-50 | 3.41e-50 | 0.999 |
| 2 | 21.02203963877 | 5.8926606e-47 | 5.8926606e-47 | 5.89e-47 | 1.000 |
| 3 | 25.01085758014 | 5.1849946e-45 | 5.1849946e-45 | 5.18e-45 | 1.001 |
| 4 | 30.42487612585 | 4.2015205e-42 | 4.2015205e-42 | 4.2e-42 | 1.000 |
| 5 | 32.93506158773 | 7.8384069e-41 | 7.8384069e-41 | 7.84e-41 | 1.000 |
| 6 | 37.58617815882 | 1.0684157e-38 | 1.0684157e-38 | 1.07e-38 | 0.999 |
| 7 | 40.91871901214 | 9.421047e-37 | 9.421047e-37 | 9.42e-37 | 1.000 |
| 8 | 43.32707328091 | 1.0544074e-35 | 1.0544074e-35 | 1.05e-35 | 1.004 |
| 9 | 48.00515088116 | 3.2465345e-33 | 3.2465345e-33 | 3.25e-33 | 0.999 |
| 10 | 49.77383247767 | 2.9857429e-32 | 2.9857429e-32 | 2.99e-32 | 0.999 |
| 11 | 52.97032147771 | 3.7587848e-31 | 3.7587848e-31 | 3.76e-31 | 1.000 |
| 12 | 56.44624769706 | 1.865544e-29 | 1.865544e-29 | 1.87e-29 | 0.998 |
| 13 | 59.34704400260 | 1.2768366e-27 | 1.2768366e-27 | 1.28e-27 | 0.998 |
| 14 | 60.83177852460 | 4.4737435e-27 | 4.4737435e-27 | 4.47e-27 | 1.001 |
| 15 | 65.11254404808 | 2.1766186e-25 | 2.1766186e-25 | 2.18e-25 | 0.998 |
| 16 | 67.07981052949 | 2.7643884e-24 | 2.7643884e-24 | 2.76e-24 | 1.002 |
| 17 | 69.54640171117 | 2.3008189e-23 | 2.3008189e-23 | 2.3e-23 | 1.000 |
| 18 | 72.06715767448 | 1.585413e-22 | 1.585413e-22 | 1.59e-22 | 0.997 |
| 19 | 75.70469069908 | 1.5885439e-20 | 1.5885439e-20 | 1.59e-20 | 0.999 |
| 20 | 77.14484006887 | 9.5453162e-20 | 9.5453162e-20 | 9.55e-20 | 1.000 |
| 21 | 79.33737502024 | 2.3643515e-19 | 2.3643515e-19 | 2.36e-19 | 1.002 |
| 22 | 82.91038085408 | 6.6985426e-18 | 6.6985426e-18 | 6.7e-18 | 1.000 |
| 23 | 84.73549298051 | 5.2370192e-17 | 5.2370192e-17 | 5.24e-17 | 0.999 |
| 24 | 87.42527461312 | 8.4022403e-16 | 8.4022403e-16 | 8.4e-16 | 1.000 |
| 25 | 88.80911120763 | 1.942801e-15 | 1.942801e-15 | 1.94e-15 | 1.001 |
| 26 | 92.49189927055 | 2.4150988e-14 | 2.4150988e-14 | 2.42e-14 | 0.998 |
| 27 | 94.65134404051 | 6.0546935e-13 | 6.0546935e-13 | 6.05e-13 | 1.001 |
| 28 | 95.87063422824 | 1.2578234e-12 | 1.2578234e-12 | 1.26e-12 | 0.998 |
| 29 | 98.83119421819 | 3.1499664e-12 | 3.1499664e-12 | 3.15e-12 | 1.000 |
| 30 | 101.3178510057 | 2.7192902e-11 | 2.7192902e-11 | 2.72e-11 | 1.000 |
| 31 | 103.7255380404 | 3.5704443e-10 | 3.5704443e-10 | 3.57e-10 | 1.000 |
| 32 | 105.4466230523 | 1.7033639e-9 | 1.7033639e-9 | 1.7e-09 | 1.002 |
| 33 | 107.1686111842 | 2.3322714e-9 | 2.3322714e-9 | 2.33e-09 | 1.001 |
| 34 | 111.0295355431 | 1.2007174e-7 | 1.2007174e-7 | 1.2e-07 | 1.001 |
| 35 | 111.8746591769 | 2.893454e-7 | 2.893454e-7 | 2.89e-07 | 1.001 |
| 36 | 114.3202209154 | 4.0994324e-7 | 4.0994324e-7 | 4.1e-07 | 1.000 |
| 37 | 116.2266803208 | 9.107062e-7 | 9.107062e-7 | 9.11e-07 | 1.000 |
| 38 | 118.7907828659 | 2.7783175e-6 | 2.7783175e-6 | 2.78e-06 | 0.999 |
| 39 | 121.3701250024 | 3.5326388e-5 | 3.5326388e-5 | 3.53e-05 | 1.001 |
| 40 | 122.9468292935 | 0.00018277411 | 0.00018277411 | 0.000183 | 0.999 |
| 41 | 124.2568185543 | 0.00016674764 | 0.00016674764 | 0.000167 | 0.998 |
| 42 | 127.5166838795 | 0.00029742428 | 0.00029742428 | 0.000297 | 1.001 |
| 43 | 129.5787041999 | 0.0021920876 | 0.0021920876 | 0.00219 | 1.001 |
| 44 | 131.0876885309 | 0.0043471623 | 0.0043471623 | 0.00435 | 0.999 |
| 45 | 133.4977372029 | 0.011856357 | 0.011856357 | 0.0119 | 0.996 |
| 46 | 134.7565097533 | 0.012709091 | 0.012709091 | 0.0127 | 1.001 |
| 47 | 138.1160420545 | 0.028677879 | 0.028677879 | 0.0287 | 0.999 |
| 48 | 139.7362089521 | 0.14285885 | 0.14285885 | 0.143 | 0.999 |
| 49 | 141.1237074040 | 0.19808928 | 0.19808928 | 0.198 | 1.000 |
| 50 | 143.1118458076 | 0.090239496 | 0.090239496 | 0.0902 | 1.000 |

ratio range: 0.996 .. 1.004; max |ratio - 1| = 0.004

**lambda = sqrt(13)** (CCM: table p. 26-27; sign changes of xi_hat on [0, gamma_50+1]: 50 = number of zeros used, so no extra real zeros below gamma_50).

| k | gamma_k | here (1024/220) | here (1536/300) | CCM | ratio here/CCM |
|---|---|---|---|---|---|
| 1 | 14.13472514173 | 2.4362928e-55 | 2.4362928e-55 | 2.44e-55 | 0.998 |
| 2 | 21.02203963877 | 4.4957241e-52 | 4.4957241e-52 | 4.5e-52 | 0.999 |
| 3 | 25.01085758014 | 4.1559229e-50 | 4.1559229e-50 | 4.16e-50 | 0.999 |
| 4 | 30.42487612585 | 3.6519787e-47 | 3.6519787e-47 | 3.65e-47 | 1.001 |
| 5 | 32.93506158773 | 7.1137465e-46 | 7.1137465e-46 | 7.11e-46 | 1.001 |
| 6 | 37.58617815882 | 1.0604534e-43 | 1.0604534e-43 | 1.06e-43 | 1.000 |
| 7 | 40.91871901214 | 1.0047891e-41 | 1.0047891e-41 | 1e-41 | 1.005 |
| 8 | 43.32707328091 | 1.1894118e-40 | 1.1894118e-40 | 1.19e-40 | 1.000 |
| 9 | 48.00515088116 | 4.1248157e-38 | 4.1248157e-38 | 4.12e-38 | 1.001 |
| 10 | 49.77383247767 | 3.981989e-37 | 3.981989e-37 | 3.98e-37 | 1.000 |
| 11 | 52.97032147771 | 5.499748e-36 | 5.499748e-36 | 5.5e-36 | 1.000 |
| 12 | 56.44624769706 | 3.0417546e-34 | 3.0417546e-34 | 3.04e-34 | 1.001 |
| 13 | 59.34704400260 | 2.2927899e-32 | 2.2927899e-32 | 2.29e-32 | 1.001 |
| 14 | 60.83177852460 | 8.4588665e-32 | 8.4588665e-32 | 8.46e-32 | 1.000 |
| 15 | 65.11254404808 | 4.8170993e-30 | 4.8170993e-30 | 4.82e-30 | 0.999 |
| 16 | 67.07981052949 | 6.6059057e-29 | 6.6059057e-29 | 6.61e-29 | 0.999 |
| 17 | 69.54640171117 | 6.0780141e-28 | 6.0780141e-28 | 6.08e-28 | 1.000 |
| 18 | 72.06715767448 | 4.662261e-27 | 4.662261e-27 | 4.66e-27 | 1.000 |
| 19 | 75.70469069908 | 5.5015655e-25 | 5.5015655e-25 | 5.5e-25 | 1.000 |
| 20 | 77.14484006887 | 3.537443e-24 | 3.537443e-24 | 3.54e-24 | 0.999 |
| 21 | 79.33737502024 | 9.7463018e-24 | 9.7463018e-24 | 9.75e-24 | 1.000 |
| 22 | 82.91038085408 | 3.3138069e-22 | 3.3138069e-22 | 3.31e-22 | 1.001 |
| 23 | 84.73549298051 | 2.856447e-21 | 2.856447e-21 | 2.86e-21 | 0.999 |
| 24 | 87.42527461312 | 5.3223137e-20 | 5.3223137e-20 | 5.32e-20 | 1.000 |
| 25 | 88.80911120763 | 1.3327463e-19 | 1.3327463e-19 | 1.33e-19 | 1.002 |
| 26 | 92.49189927055 | 2.0677681e-18 | 2.0677681e-18 | 2.07e-18 | 0.999 |
| 27 | 94.65134404051 | 5.9431741e-17 | 5.9431741e-17 | 5.94e-17 | 1.001 |
| 28 | 95.87063422824 | 1.3367878e-16 | 1.3367878e-16 | 1.34e-16 | 0.998 |
| 29 | 98.83119421819 | 4.089794e-16 | 4.089794e-16 | 4.09e-16 | 1.000 |
| 30 | 101.3178510057 | 4.2121372e-15 | 4.2121372e-15 | 4.21e-15 | 1.001 |
| 31 | 103.7255380404 | 6.6120595e-14 | 6.6120595e-14 | 6.61e-14 | 1.000 |
| 32 | 105.4466230523 | 3.6016941e-13 | 3.6016941e-13 | 3.6e-13 | 1.000 |
| 33 | 107.1686111842 | 5.6555354e-13 | 5.6555354e-13 | 5.66e-13 | 0.999 |
| 34 | 111.0295355431 | 4.0260127e-11 | 4.0260127e-11 | 4.03e-11 | 0.999 |
| 35 | 111.8746591769 | 1.0449754e-10 | 1.0449754e-10 | 1.04e-10 | 1.005 |
| 36 | 114.3202209154 | 1.8489598e-10 | 1.8489598e-10 | 1.85e-10 | 0.999 |
| 37 | 116.2266803208 | 4.9239192e-10 | 4.9239192e-10 | 4.92e-10 | 1.001 |
| 38 | 118.7907828659 | 1.9403969e-9 | 1.9403969e-9 | 1.94e-09 | 1.000 |
| 39 | 121.3701250024 | 3.2423133e-8 | 3.2423133e-8 | 3.24e-08 | 1.001 |
| 40 | 122.9468292935 | 1.9993745e-7 | 1.9993745e-7 | 2e-07 | 1.000 |
| 41 | 124.2568185543 | 2.1217055e-7 | 2.1217055e-7 | 2.12e-07 | 1.001 |
| 42 | 127.5166838795 | 5.6572562e-7 | 5.6572562e-7 | 5.66e-07 | 1.000 |
| 43 | 129.5787041999 | 5.4933678e-6 | 5.4933678e-6 | 5.49e-06 | 1.001 |
| 44 | 131.0876885309 | 1.3455247e-5 | 1.3455247e-5 | 1.35e-05 | 0.997 |
| 45 | 133.4977372029 | 5.3000868e-5 | 5.3000868e-5 | 5.3e-05 | 1.000 |
| 46 | 134.7565097533 | 6.8754568e-5 | 6.8754568e-5 | 6.88e-05 | 0.999 |
| 47 | 138.1160420545 | 0.00030113121 | 0.00030113121 | 0.000301 | 1.000 |
| 48 | 139.7362089521 | 0.002002484 | 0.002002484 | 0.002 | 1.001 |
| 49 | 141.1237074040 | 0.0030069091 | 0.0030069091 | 0.00301 | 0.999 |
| 50 | 143.1118458076 | 0.0020444488 | 0.0020444488 | 0.00204 | 1.002 |

ratio range: 0.997 .. 1.005; max |ratio - 1| = 0.005

**lambda = sqrt(14)** (CCM: table p. 26-27; sign changes of xi_hat on [0, gamma_50+1]: 50 = number of zeros used, so no extra real zeros below gamma_50).

| k | gamma_k | here (1024/220) | here (1536/300) | CCM | ratio here/CCM |
|---|---|---|---|---|---|
| 1 | 14.13472514173 | 1.0651528e-60 | 1.0651528e-60 | 1.07e-60 | 0.995 |
| 2 | 21.02203963877 | 2.0774128e-57 | 2.0774128e-57 | 2.08e-57 | 0.999 |
| 3 | 25.01085758014 | 2.0028185e-55 | 2.0028185e-55 | 2e-55 | 1.001 |
| 4 | 30.42487612585 | 1.885638e-52 | 1.885638e-52 | 1.89e-52 | 0.998 |
| 5 | 32.93506158773 | 3.8104041e-51 | 3.8104041e-51 | 3.81e-51 | 1.000 |
| 6 | 37.58617815882 | 6.1291256e-49 | 6.1291256e-49 | 6.13e-49 | 1.000 |
| 7 | 40.91871901214 | 6.1728305e-47 | 6.1728305e-47 | 6.17e-47 | 1.000 |
| 8 | 43.32707328091 | 7.6628599e-46 | 7.6628599e-46 | 7.66e-46 | 1.000 |
| 9 | 48.00515088116 | 2.9391814e-43 | 2.9391814e-43 | 2.94e-43 | 1.000 |
| 10 | 49.77383247767 | 2.9562788e-42 | 2.9562788e-42 | 2.96e-42 | 0.999 |
| 11 | 52.97032147771 | 4.4158391e-41 | 4.4158391e-41 | 4.42e-41 | 0.999 |
| 12 | 56.44624769706 | 2.6760436e-39 | 2.6760436e-39 | 2.68e-39 | 0.999 |
| 13 | 59.34704400260 | 2.1880863e-37 | 2.1880863e-37 | 2.19e-37 | 0.999 |
| 14 | 60.83177852460 | 8.4311392e-37 | 8.4311392e-37 | 8.43e-37 | 1.000 |
| 15 | 65.11254404808 | 5.4807654e-35 | 5.4807654e-35 | 5.48e-35 | 1.000 |
| 16 | 67.07981052949 | 8.0161157e-34 | 8.0161157e-34 | 8.02e-34 | 1.000 |
| 17 | 69.54640171117 | 8.0222148e-33 | 8.0222148e-33 | 8.02e-33 | 1.000 |
| 18 | 72.06715767448 | 6.7313966e-32 | 6.7313966e-32 | 6.73e-32 | 1.000 |
| 19 | 75.70469069908 | 9.1055781e-30 | 9.1055781e-30 | 9.11e-30 | 1.000 |
| 20 | 77.14484006887 | 6.1947287e-29 | 6.1947287e-29 | 6.19e-29 | 1.001 |
| 21 | 79.33737502024 | 1.8648384e-28 | 1.8648384e-28 | 1.86e-28 | 1.003 |
| 22 | 82.91038085408 | 7.3770098e-27 | 7.3770098e-27 | 7.38e-27 | 1.000 |
| 23 | 84.73549298051 | 6.8940861e-26 | 6.8940861e-26 | 6.89e-26 | 1.001 |
| 24 | 87.42527461312 | 1.453466e-24 | 1.453466e-24 | 1.45e-24 | 1.002 |
| 25 | 88.80911120763 | 3.8866486e-24 | 3.8866486e-24 | 3.89e-24 | 0.999 |
| 26 | 92.49189927055 | 7.2343161e-23 | 7.2343161e-23 | 7.23e-23 | 1.001 |
| 27 | 94.65134404051 | 2.3253672e-21 | 2.3253672e-21 | 2.33e-21 | 0.998 |
| 28 | 95.87063422824 | 5.5810327e-21 | 5.5810327e-21 | 5.58e-21 | 1.000 |
| 29 | 98.83119421819 | 2.0096067e-20 | 2.0096067e-20 | 2.01e-20 | 1.000 |
| 30 | 101.3178510057 | 2.3878242e-19 | 2.3878242e-19 | 2.39e-19 | 0.999 |
| 31 | 103.7255380404 | 4.3289535e-18 | 4.3289535e-18 | 4.33e-18 | 1.000 |
| 32 | 105.4466230523 | 2.6229587e-17 | 2.6229587e-17 | 2.62e-17 | 1.001 |
| 33 | 107.1686111842 | 4.5956664e-17 | 4.5956664e-17 | 4.6e-17 | 0.999 |
| 34 | 111.0295355431 | 4.2319813e-15 | 4.2319813e-15 | 4.23e-15 | 1.000 |
| 35 | 111.8746591769 | 1.164748e-14 | 1.164748e-14 | 1.16e-14 | 1.004 |
| 36 | 114.3202209154 | 2.4537789e-14 | 2.4537789e-14 | 2.45e-14 | 1.002 |
| 37 | 116.2266803208 | 7.5262186e-14 | 7.5262186e-14 | 7.53e-14 | 0.999 |
| 38 | 118.7907828659 | 3.6144141e-13 | 3.6144141e-13 | 3.61e-13 | 1.001 |
| 39 | 121.3701250024 | 7.4397698e-12 | 7.4397698e-12 | 7.44e-12 | 1.000 |
| 40 | 122.9468292935 | 5.2379638e-11 | 5.2379638e-11 | 5.24e-11 | 1.000 |
| 41 | 124.2568185543 | 6.2249313e-11 | 6.2249313e-11 | 6.22e-11 | 1.001 |
| 42 | 127.5166838795 | 2.2294557e-10 | 2.2294557e-10 | 2.23e-10 | 1.000 |
| 43 | 129.5787041999 | 2.6370806e-9 | 2.6370806e-9 | 2.64e-09 | 0.999 |
| 44 | 131.0876885309 | 7.5057748e-9 | 7.5057748e-9 | 7.51e-09 | 0.999 |
| 45 | 133.4977372029 | 3.8003242e-8 | 3.8003242e-8 | 3.8e-08 | 1.000 |
| 46 | 134.7565097533 | 5.6541871e-8 | 5.6541871e-8 | 5.65e-08 | 1.001 |
| 47 | 138.1160420545 | 3.6581221e-7 | 3.6581221e-7 | 3.66e-07 | 0.999 |
| 48 | 139.7362089521 | 2.9755767e-6 | 2.9755767e-6 | 2.98e-06 | 0.999 |
| 49 | 141.1237074040 | 5.3403248e-6 | 5.3403248e-6 | 5.34e-06 | 1.000 |
| 50 | 143.1118458076 | 4.7848764e-6 | 4.7848764e-6 | 4.78e-06 | 1.001 |

ratio range: 0.995 .. 1.004; max |ratio - 1| = 0.005

### 4.3 Verdict

Reproduced.  Every one of CCM's 170 printed differences (20 at λ = 3, 150 in
the √12/√13/√14 table) is matched to the two or three significant figures
CCM print, with ratio here/CCM in [0.974, 1.014] at λ = 3 (CCM print two
figures there, so the residual is rounding) and within 0.5 % for the
three-figure table, including the headline 2.44e-55 (here 2.43629e-55) and
1.07e-60 (here 1.06515e-60).  The two precisions agree to all 40 stored
digits, so the values are precision-stable at fixed problem size.  ε_N is
even-simple in every case (lowest odd eigenvalue 3–4 orders above the even
ground; second even eigenvalue 7–8 orders above), which is the hypothesis of
CCM Theorem 5.10, and ξ̂ has no extra real zeros below the last zeta zero
used.  ln ε_N (−86.4, −122.7, −134.6, −147.0) sits within the ±5 reading
error of CCM's Figure 4 (≈ −90, −128, −140, −153), a coarse check on the
overall scale that §6 itself cannot provide.

No discrepancy in anything the test can see; the remaining unlocked degree
of freedom is the common scale / identity shift of QW_λ (see §2, §7).


## 5. Derivation used for the archimedean diagonal (hand check)

With ρ(x) = e^{x/2}/(e^x − e^{−x}) = Σ_{k≥0} e^{−c_k x}, c_k = 2k + ½, and
t = t_n = 2πn/L (so sin(tL) = 0, cos(tL) = 1):

    ∫_0^L cos(tx) e^{−cx} dx = c(1 − e^{−cL})/(c² + t²)
    ∫_0^L x cos(tx) e^{−cx} dx = (c² − t²)/(c² + t²)² − e^{−cL}[Lc/(c²+t²) + (c²−t²)/(c²+t²)²]
    ∫_0^L e^{−x/2} e^{−cx} dx = (1 − e^{−(c+½)L})/(c + ½)

so −W_R(V_n,V_n) = −2w(L) − 2∫(cos − e^{−x/2})ρ + (2/L)∫ x cos ρ becomes

    −2Σ_k [c_k/(c_k²+t²) − 1/(2k+1)]           = Re ψ(¼ − it/2) + γ + 2 log 2
    −2 Σ_k e^{−(2k+1)L}/(2k+1) − 2w(L)          = −γ − log 4π          (artanh cancels)
    (2/L) Σ_k (c_k²−t²)/(c_k²+t²)²              = Re ψ′(¼ − it/2)/(2L)
    remaining tails                             = −(2/L)Σ_k e^{−c_kL}(c_k²−t²)/(c_k²+t²)²

(the e^{−c_kL} Lc/(c²+t²) tails from the two cos integrals cancel each
other).  Sum: Re ψ − log π + Re ψ′/(2L) − tail, which is `a` in
`sequences`.  Exact identity; checked also by the numerics of §4.

## 6. Sensitivity of the test (what a "pass" locks)

At N = 30, λ = 3 (512 bits / 80 digits; `sensitivity.py`, committed here),
the first five |γ_k − z_k| are 2.2e-33, 2.9e-30, 2.1e-28,
1.3e-25, 2.0e-24.  Deliberate perturbations of the assembly give

| perturbation | ε_N | first-zero difference | extra real zeros below γ_5 |
|---|---|---|---|
| none | 4.02e-37 | 2.2e-33 | 0 |
| zero-mode factor √2 → 1 | 1.2e-30 | 8.4e-29 | 0 |
| prime term × (1 + 1e-8) | −1.8e-8 | 1.1e-7 | 5 |
| prime term × (1 + 1e-20) | −9.9e-21 | 5.1e-21 | 2 |
| prime term × (1 + 1e-40) | 4.02e-37 | 2.2e-33 | 0 |
| archimedean diagonal sign flipped | −4.07 | 2.5 | 7 |
| pole term dropped | −4.83 | (no bracketed root) | 6 |

So reproducing CCM's figures pins the *relative* weights of the pole,
prime and archimedean pieces and the basis geometry to roughly the size of
ε_N (about 1e-30 relative), but says nothing about a common scalar factor
or an identity shift.

## 7. Claim labels

- exact: the term-by-term identity of the repository's b_n, a_n with CCM
  Lemma 4.1, (4.3), Prop. 4.3/(4.4) (§2, §5 above), including the
  regularized archimedean diagonal.
- numerical: every number in §4 and §6 (midpoint eigensolves; Arb balls only
  for the matrix entries).
- open: the overall scale and any identity shift of QW_λ are not tested by
  CCM's §6 and cannot be, since they do not move the zeros of ξ̂; CCM print
  no eigenvalue with digits.  The only scale information is Figure 4 read by
  eye (§4).
- Nothing here concerns G2 or RH.
