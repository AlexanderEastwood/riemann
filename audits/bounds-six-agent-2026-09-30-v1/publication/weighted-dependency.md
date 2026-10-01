# Forward dependency note — existing coefficient corollary

This reproduces the already checked dependency of gain01 from public NS78; it is not a new attempt or bound. It avoids making unpublished local working files a prerequisite for the public audit. The preserved notes retain their original provenance references.

For finite real c and real alpha, let R=alpha tau-sum c_n a_n in the fixed q=2 complete space. NS78 (`evidence/v163/ns78/proof.tex`) supplies samples z_m, eta, h_m=log(1+1/m), D_0=0, D_m=(z_(m+1)-z_m+eta)/h_m and delta_m=D_m-D_(m-1), with

    S_total=eta²+sum_(m>=1)(z_m²+z_(m+1)²)/(m(m+1)) <=16||R||²,
    c+alpha mu=mu*delta.

Since 1/h_m<=2m, 1/m²<=2/[m(m+1)] and zeta(2)<2,

    sum_m D_m²/m⁴ <=24 S_total,
    sum_m delta_m²/m⁴ <=4 sum_m D_m²/m⁴ <=96 S_total.

On l²(n^-4), dilation of an index by d has norm d^-2. The Dirichlet convolution by mu is therefore bounded by sum_d |mu(d)|/d²<=zeta(2); its operator series converges absolutely. Hence

    sum_n |c_n+alpha mu(n)|²/n⁴
       <=1536 zeta(2)² ||R||².

For alpha=0 and the exact residualized synthesis coefficients (-G^-1 C v,v), this is exactly gain01's L<=B S. Every physical cell and tail in NS78 is retained. The argument uses the original divisor identity but no signed Mobius cancellation. It gives coefficient control from energy, not actual residual decay; gain01/03 record the inverse-order and certificate-scale limitations. The publication introduces no new cofinal assertion.
