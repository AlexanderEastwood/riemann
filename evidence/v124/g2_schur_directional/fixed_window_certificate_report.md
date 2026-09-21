# Complete fixed-window Weil positivity certificate at lambda=3

## Established result and scope

The interval computations below certify strict positivity of the complete canonical semilocal Weil operator at the exact window lambda=3, in both reflection sectors, using the proved operator/core, matrix, and tail identities in the working manuscript. All Fourier modes are included: the infinite complement is bounded analytically rather than discarded.

This is a computer-assisted **fixed-window** result. It does not establish G2 uniformly as the window grows, ground-state parity or simplicity, the required endpoint/graph-normalized asymptotics, or RH. The interval arithmetic is a proof enclosure, whereas the earlier floating-point spectral plots were numerical evidence only.

## Exact certificate parameters

Here N is the head cutoff, M the finite support cutoff of the lifted columns, J the last explicitly computed output row, and r the number of terms in the remote geometric expansion. Both runs use 768-bit Arb arithmetic, 128 terms in the special-function assembly series, exact lambda=3, and tau=1/1000000 in the remote Young inequality.

| Reflection sector | N | M | J | r | Head dimension | Positive LDL pivots |
|---|---:|---:|---:|---:|---:|---:|
| Even | 256 | 512 | 4096 | 80 | 257 | 257 |
| Odd | 512 | 1024 | 4096 | 100 | 512 | 512 |

Both use diagonal inverse weights, not a common inverse coercivity constant. The minimum tail constants are respectively greater than 2.0690317004 and 1.1907506685. The geometric remainder coefficients delta^2 are enclosed near 1.6557866048e-148 and 3.2874200718e-124.

The reported minimum LDL pivots are approximately 9.1749869395e-9 and 9.6802634105e-8. These are **not lower eigenvalue bounds**. Positivity follows because every pivot is strictly positive; the magnitude of a pivot does not by itself quantify the spectral gap.

## Proof chain

1. **Canonical operator and domain.** On the trigonometric basis the exact off-diagonal entries are W_nm=(b_n-b_m)/(n-m), with bounded real odd b, and the separately defined physical diagonal satisfies d_n=log(|n|/L)+O(1). Thus W=diag(d)+[M_b,H], where the discrete Hilbert transform H is bounded. The operator is self-adjoint on the log-squared weighted sequence domain, finite sequences are an operator core, and its quadratic-form domain has one logarithmic weight. Agreement on the established trigonometric form core identifies this operator with the canonical closed Weil form. Reflection yields an orthogonal even/odd decomposition.

2. **Exact matrix assembly.** `assembly.py` uses the physical logarithmic diagonal, the pole term, every nonzero prime-power shift at lambda=3, and certified digamma/trigamma formulas with explicit geometric tail radii. The shift at m=9 is identically zero. All 8,321 even/odd matrix entries through cutoff 64 overlap the independent integration certificate; see `assembly_independent_overlap.json`. No prolate-source or ground-state identification is assumed in this sign certificate.

3. **Positive diagonal lower bound on the entire tail.** The cosh-weighted prime Schur estimate, archimedean Hilbert-commutator estimate, and pole estimate prove T=Q_N W Q_N >= D=diag(g(n))>0 for every omitted Fourier index. With the notation of the sharp-tail proof,

       g(n)=Gamma_N+log(n/(N+1))+E(t_{N+1})-E(t_n).

   The common commutator and pole losses are retained at cutoff N. Hence g is increasing, and inverse order gives T^{-1}<=D^{-1}. This is the step that makes the final bounds substantially sharper than the old scalar Gamma_N^{-1} budget.

4. **Exact finite lift and residual.** The numerical intermediate inverse solve is used only to choose a finite lift Z, then frozen to exact dyadic midpoints. The code computes

       K_Z=F-B^*Z-Z^*B+Z^*TZ,
       R=B-TZ,

   with every finite intermediate residual retained. The exact Schur complement obeys

       F-B^*T^{-1}B = K_Z-R^*T^{-1}R
                     >= K_Z-R^*D^{-1}R.

5. **All infinite residual rows are included.** Rows N<n<=J are evaluated directly with the correct diagonal. For |n|>J, the identity (n-m)^{-1}=sum_{j<r}m^j n^{-j-1}+(m/n)^r/(n-m) gives exact moment rows. Their Gram is bounded by the Hurwitz-zeta moment matrix plus an explicit geometric-remainder Gram. The full signed-index parity factors, including sqrt(2) and the two tails, are retained. The monotonicity of g bounds the weighted remote contribution by U_remote/g(J+1).

6. **Finite interval sign check and closed-form conclusion.** Arb interval LDL verifies strict positivity of

       L_cert=K_Z-R_near^*D_near^{-1}R_near
                    -U_remote/g(J+1).

   Therefore the exact Schur complement is positive. The tail is already positive. A bounded invertible block-triangular congruence then proves strict positivity of the full operator in that reflection sector. Applying this in both sectors covers the whole canonical fixed-window form. The congruence argument gives a positive operator lower bound in principle; no numerical value for that lower bound is asserted here.

## Reproduction and integrity

Run `certify_infinite_schur.py` with:

```text
--N 256 --M 512 --J 4096 --r 80 --bits 768 --parity even --diagonal
--N 512 --M 1024 --J 4096 --r 100 --bits 768 --parity odd --diagonal
```

Report SHA-256 values at this checkpoint:

```text
infinite_schur_N256_M512_J4096_r80_even_b768_diagonal.json
7bfbda6db0664eb4667b2567cb05f69098e3d9031dce876ad2c550c6dc868e8a

infinite_schur_N512_M1024_J4096_r100_odd_b768_diagonal.json
a52654a03664dd7dee81ce9857f34ed042dc08305b6781f63ab1b31be3ad70d5
```

The exact finite-lift witnesses are saved as compressed JSON. Their **uncompressed** SHA-256 values are:

```text
schur_witness_N256_M512_even_b768.json.gz
993c5b325c1cc7dce64c1dbdab9384dd54dea6a480cce8739cf623e9e8bce43c

schur_witness_N512_M1024_odd_b768.json.gz
4054507110d6a806c3dfa926c716c1692de4c9b7dc7801263d50b92cbd8dfdea
```

The sequence caches preserve interval radii. Arbitrary recomputation may produce different enclosing intervals while proving the same inequalities; the hashes identify these particular checkpoint reports and witnesses. Independent higher-precision replay is recorded separately when completed.

## Meaning of the earlier failures

The odd scalar-Gamma budget at N=256 failed even before the remote tail was added. The full odd scalar-Gamma budget at N=512/M=1024/J=2048 also failed, and the smaller-head odd diagonal budget N=256/M=512/J=4096 failed. Those were negative directions of conservative **lower bounds**, not negative directions of the actual Weil operator. Their records remain in the bundle. They explain why directional moments, diagonal inverse weights, and the larger odd lift were needed; none is evidence against the established final positivity statement.

## Next concrete obligation

At this fixed window, run shifted certificates for W-aI, for example with a=1e-36. Positivity of the odd shifted sector together with a lower even Schur matrix having exactly one negative direction, and the already certified even trial Rayleigh quotient below 5.32e-38, would prove the whole-window ground state is simple and even with a quantitative separation. Such a shift requires subtracting a consistently from every physical diagonal and tail lower bound and verifying the complete indefinite LDL inertia, not stopping at the first negative pivot.

After that fixed-window ordering check, the unresolved G2 task remains obtaining estimates that hold along the required growing-window family and interact with the physical endpoint, graph defect, and required normalization. No finite list of positive window certificates replaces that uniform proof.
