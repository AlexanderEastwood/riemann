# A moment-preserving PSD enclosure of the infinite remote Weil residual

Status: analytic derivation for adversarial review. The basic implementation requires only Hurwitz zeta and finite matrix arithmetic; no infinite sum over computed Weil rows is needed. All Fourier coefficients below are in the actual normalized basis, and the physical diagonal remains separate.

## 1. Exact expansion

Let W have the actual off-diagonal entries

    W_nm=(b_n-b_m)/(n-m),  n!=m,

with real odd bounded b, and let B_* be a proved bound for sup_n |b_n|. Let G:C^d->E_M be any finite coefficient matrix, in the full index set -M,...,M, with M>=1. Assume J>M and choose an integer r>=1. Write G_m for row m. For 0<=j<r define the row moments

    S_j=sum_{m=-M}^M (m/M)^j G_m,
    T_j=sum_{m=-M}^M (m/M)^j b_m G_m.

At j=0 use 0^0=1. For |n|>J, the diagonal never occurs, and

    (WG)_n=A_n+E_n,
    A_n=sum_{j=0}^{r-1} M^j n^(-j-1)(b_n S_j-T_j),
    E_n=sum_m (m/n)^r (b_n-b_m)G_m/(n-m).

This is an exact finite geometric expansion of (n-m)^(-1), with all factors retained. It applies equally to shifted W-aI, since the remote diagonal times G is zero.

## 2. Cheap exact moment Gram and PSD majorant

Define the real symmetric r-by-r matrix

    H_jk=M^(j+k) [1+(-1)^(j+k)] zeta(j+k+2,J+1).

Here zeta(s,a) is Hurwitz zeta. This is EXACTLY

    H_jk=sum_{|n|>J} (M^j/n^(j+1))(M^k/n^(k+1)),

hence H is positive semidefinite. Odd j+k gives zero, not a small numerical value. The matrix has no n=J term: the Hurwitz argument is J+1.

Let S,T be the r-by-d matrices with those rows. For any eta>0,

    A^*A <= U0(eta)
          :=(1+eta) B_*^2 S^* H S +(1+eta^(-1)) T^* H T.

Proof: for each direction x, write a_n=sum M^j n^(-j-1) S_j x and t_n similarly. Then A_nx=b_n a_n-t_n, and scalar Young gives |A_nx|^2<=(1+eta)B_*^2|a_n|^2+(1+eta^-1)|t_n|^2; summing produces the asserted quadratic-form inequality. Eta=1 gives the simple 2 B_*^2 S^*HS+2 T^*HT.

This estimate retains all cancellations WITHIN each exact moment and across moments in H. It discards only the cross cancellation between b_n a_n and t_n. It is a PSD congruence, not an entrywise absolute-value bound. Never replace it by its norm times the identity in the certificate's source direction.

## 3. Two rigorous remainder Grams

Put q=M/(J+1)<1, w_m=(|m|/M)^(2r), and

    kappa = 8 B_*^2 M^(2r) zeta(2r+2,J+1)/(1-q)^2,
    c_{M,r}=sum_{m=-M}^M w_m.

Then each of the following matrices bounds E^*E in Loewner order:

    D1 = kappa c_{M,r} G^*G,
    D2 = kappa (2M) G^* diag(w_m) G.

The factor 2M in D2 can be replaced by 2M+1 harmlessly. It is 2M because m=0 contributes zero when r>=1. A convex combination of D1,D2 is also a valid bound. An entrywise or spectral minimum is NOT justified in general.

Proof of D1: Cauchy--Schwarz in m gives

    |E_n x|^2 <= 4 B_*^2 (M/|n|)^(2r)
                       c_{M,r} ||Gx||^2/(|n|-M)^2.

For |n|>=J+1, replace (|n|-M)^(-2) by |n|^(-2)(1-q)^(-2), and sum both signs of n. The factors are 4 from |b_n-b_m|^2<=(2B_*)^2 and 2 from the two tails. For D2, instead use Cauchy--Schwarz with the weight w_m in the G rows and bound the number of contributing m by 2M.

An optional sharper nonuniform version uses known |b_m| rather than 2B_*. If B_R>=sup_{|n|>J}|b_n|, replace the weights by w_m(B_R+|b_m|)^2 and replace the leading 8 B_*^2 by 2. This can also be applied to D1. Absolute-value enclosures of b_m must be rigorous.

For any tau>0, the complete remote Gram is therefore bounded by

    (Q_J WG)^*(Q_J WG)
       <= U_remote=(1+tau) U0(eta)+(1+tau^(-1)) D,

where D is any valid remainder bound above. This is another scalar Young inequality applied to A+E, before summing. It is important to retain the full D matrix, especially after preconditioning or changing source coordinates.

At M=512,J=1024,r=128, the geometric squared remainder has the scale 2^(-256), up to explicit benign constants. The count c_{M,r} is about 5, versus 1025 in the coarsest row-count bound. Tau=10^-6 is a plausible choice when the target energy is around 10^-38; actual interval comparisons, not this scale estimate, decide the certificate.

## 4. Exact parity bookkeeping

Because b is odd and W commutes with Fourier reflection, remote outputs preserve parity. In a pure even column, S_j=0 for odd j and T_j=0 for even j. In a pure odd column, S_j=0 for even j and T_j=0 for odd j. These zeros should be imposed exactly from the construction, not inferred by subtracting interval approximations.

The normalized parity basis convention is:

- even: G_0=v_0, G_m=G_{-m}=v_m/sqrt(2) for m>0;
- odd: G_0=0, G_m=v_m/sqrt(2), G_{-m}=-v_m/sqrt(2).

The physical Fourier endpoint of an even vector is L^(-1/2)[v_0+sqrt(2)sum_{m>0}v_m]. It is not the unweighted sum of parity coordinates.

For a matrix with columns of both parities, the exact remote Gram has zero even/odd cross blocks. H has odd j+k entries exactly zero, so the cheap majorant and both remainder Grams respect the same block decomposition. Retaining those zeros saves arithmetic and prevents spurious cancellation radii.

An even-only paired expansion can halve the number of nonzero moment rows. For n>J,

    (WG)_n=b_n G_0/n
       +sum_{m=1}^M 2(n b_n-m b_m)G_m/(n^2-m^2).

For an odd column the corresponding pair is

    sum_{m=1}^M 2(m b_n-n b_m)G_m/(n^2-m^2).

Expanding (1-m^2/n^2)^(-1) has ratio (M/n)^2. This is algebraically the same as using the nonzero parity rows of the full r-moment construction. If q paired terms are used, the full expansion order is r=2q; the remainder exponent is then 4q in its squared bound, not 2q. The full-coordinate formula is safest for a first implementation.

## 5. Application to a signed Schur residual

Let P be the actual head projection, Q=I-P, and write

    F=PWP, B=QWP, T=QWQ >= Gamma I>0.

Let Z map head coordinates into the tail, with finite support at |m|<=M, and let I_head embed the head basis into E_M. Set

    G=I_head-Z.

Then the full residual R=B-TZ is EXACTLY QWG. In particular its remote rows |n|>J are Q_J WG. On the finite set of intervening rows, define

    R_near=(P_J-P)WG.

The complete diagonal d_n must be used when n=m in this finite calculation; never replace it by a divided-difference limit. Since the near and remote output spaces are orthogonal,

    R^*R <= R_near^* R_near + U_remote.

Consequently the exact Schur identity yields the directional finite certificate

    K=F-B^*T^(-1)B
      >= F-B^*Z-Z^*B+Z^*TZ
          -Gamma^(-1)[R_near^*R_near+U_remote].

All displayed matrices are in head coordinates. No scalar norm of R is substituted. If a source-adapted coordinate matrix C is useful, replace G by GC and congruence-transform every finite term by C^*(.)C. This preserves the mathematical inequality and can make an extremely small source direction numerically resolvable. Exact rational/interval coordinates and all Gram matrices must be retained; a nonorthonormal coordinate change does not permit silently replacing C^*C by I.

Since Z has finite support, the terms involving B^*Z and Z^*TZ require only the actual finite matrix through M. The genuinely infinite part is precisely the residual Gram above.

## 6. Exact b-weighted refinement if the cheap majorant is insufficient

The leading Gram can be retained without discarding b_nS/T cross cancellation. Define, for each integer ell>=2,

    Z_ell=sum_{|n|>J} n^(-ell),
    B_ell=sum_{|n|>J} b_n n^(-ell),
    C_ell=sum_{|n|>J} b_n^2 n^(-ell).

These are absolutely convergent. Their parity identities are

    Z_ell=C_ell=0 for ell odd; B_ell=0 for ell even.

Then the EXACT leading Gram is

    A^*A=sum_{j,k=0}^{r-1} M^(j+k)
       [ C_(j+k+2) S_j^*S_k
        -B_(j+k+2)(S_j^*T_k+T_j^*S_k)
        +Z_(j+k+2) T_j^*T_k ].

The ordinary Z_ell are explicit Hurwitz zeta values. For a finite trigonometric approximation to b_n, all B_ell and C_ell reduce to exponential power sums

    sum_{n>J} exp(i theta n)/n^ell
       =exp(i theta(J+1)) Phi(exp(i theta),ell,J+1),

where Phi is Lerch's transcendent; the defining series is absolutely convergent since ell>=2. Products of prime sine terms reduce by product-to-sum identities. At exact theta=0 use Hurwitz zeta, avoiding a nearly singular branch representation. See the primary definition https://dlmf.nist.gov/25.14.E1.

The actual b_n also has its pole rational term and archimedean sine-integral term. Neither may be discarded or replaced solely by its limiting constant. The cheap bound in Sections 2-3 includes both exactly through B_* and the finite b_m. An exact b-weighted improvement needs either rigorous infinite special-function evaluation or a proved remainder for an explicit approximation b_n=b_n^(0)+epsilon_n. Such a remainder should be charged to the S-moment Gram, since its leading row error is epsilon_n sum_j M^j n^(-j-1)S_j, rather than to the identity on head space. This refinement remains an optional next step, not a completed new enclosure of the actual B_ell,C_ell.

## Implementation notes

Python-FLINT's real Arb interface evaluates Hurwitz zeta as arb(s).zeta(arb(a)); verified against the installed 0.9.0 documentation. The proof needs an interval enclosure, not an approximate float call. Primary API: https://python-flint.readthedocs.io/en/stable/arb.html.

Compute H via only the r distinct even powers; set odd entries exactly zero. Build S,T after any exact source-adapted congruence, using arbitrary precision. Form U_remote by certified matrix products. Increasing precision is preferable to replacing interval radii by a scalar error times I, which would erase the tiny direction this construction is meant to preserve.

No infinite positivity or G2 claim follows before the final directional finite lower bound passes its own certified comparison.

## 7. Directional inverse weighting and annular Hurwitz sums

If an independent tail proof gives

    T >= D_g=diag(g_n),  g_n>0 for all tail indices,

in closed-form order, then T^(-1)<=D_g^(-1). This follows directly from the variational formula for inverse quadratic forms. Consequently the sharper Schur deduction is

    K >= F-B^*Z-Z^*B+Z^*TZ -R^*D_g^(-1)R.

The near residual can be weighted exactly row by row:

    V_near=sum_{head<|n|<=J} R_n^*R_n/g_n.

Assume g depends only on |n|, as in the proposed explicit tail bound. Choose annular cuts J_0=J<J_1<...<J_K and positive upper weights omega_k such that

    1/g_n <= omega_k for J_k<|n|<=J_{k+1},
    1/g_n <= omega_K for |n|>J_K.

For a proved monotone lower g_n, omega_k=1/g_{J_k+1} is valid. For ell>=2 put

    Z_ell^(omega)=sum_{k=0}^{K-1} omega_k
       [zeta(ell,J_k+1)-zeta(ell,J_{k+1}+1)]
       +omega_K zeta(ell,J_K+1).

Replace H_jk by

    H_jk^(omega)=M^(j+k)[1+(-1)^(j+k)]Z_(j+k+2)^(omega).

This remains an exact PSD Gram for a positive, piecewise constant majorizing weight. The leading bound U0 is unchanged in shape. The following stronger weighted remainder factor may be used:

    kappa_omega=8 B_*^2 M^(2r) {
       sum_{k=0}^{K-1} omega_k/(1-M/(J_k+1))^2
         [zeta(2r+2,J_k+1)-zeta(2r+2,J_{k+1}+1)]
       +omega_K/(1-M/(J_K+1))^2 zeta(2r+2,J_K+1) }.

Then D1,D2 use kappa_omega in place of kappa, and

    R^*D_g^(-1)R <= V_near +(1+tau)U0^(omega)+(1+tau^(-1))D^(omega).

There is no additional Gamma^(-1) prefactor. This is the implementation-ready synthesis with the sharpened arithmetic tail bound. If a single annulus is enough, take K=0 and omega_0=1/g_{J+1}; every remote contribution is then simply scaled by that weight. A few doubling annuli retain the logarithmic improvement farther out without computing extra Weil rows.

Independent proof of g_n>0 and the monotonicity or annular infimum bounds remains mandatory. Neither a numerical sample of g_n nor a lower bound at only one tail index suffices without monotonicity.
