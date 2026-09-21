"""Certified real-matrix remote Gram majorants for the actual Weil commutator.

Conditional inputs: exact matrices are enclosed by G and b; B bounds |b_n|
for all n; optional annulus weights bound the inverse tail diagonal. This
routine computes interval enclosures of PROVED PSD majorants, not a proof of
those input hypotheses. See directional_tail_derivation.md.
"""
from flint import arb, arb_mat, fmpq


def remote_gram_majorant(G, b, M, J, order, B, tau, eta=1,
                         annular_cuts=None, annular_weights=None,
                         remainder="weighted"):
    """Return U with (Q_J W G)^* weight (Q_J W G) <= U.

    G is real arb_mat in full normalized Fourier coordinates -M,...,M.
    b has 2*M+1 entries. B,tau,eta are rigorous real scalar enclosures of
    positive constants. The true B must dominate sup |b_n|. annular_cuts
    starts with J; annular_weights has the same length, final annulus goes
    to infinity. Each weight must be a proved positive upper inverse weight.
    With no annuli, the weight is one. Complex data need Hermitian products,
    not the real transpose used by this implementation.
    """
    assert M >= 1 and J > M and order >= 1
    assert G.nrows() == 2*M+1 and len(b) == 2*M+1
    B, tau, eta = arb(B), arb(tau), arb(eta)
    assert B > 0 and tau > 0 and eta > 0
    cuts = [J] if annular_cuts is None else list(annular_cuts)
    weights = [arb(1)] if annular_weights is None else [arb(x) for x in annular_weights]
    assert cuts[0] == J and len(cuts) == len(weights)
    assert all(cuts[k] < cuts[k+1] for k in range(len(cuts)-1))
    assert all(x > 0 for x in weights)
    d = G.ncols()
    b = [arb(x) for x in b]
    V = arb_mat(order, 2*M+1)
    ratios = [arb(fmpq(m,M)) for m in range(-M,M+1)]
    for i, ratio in enumerate(ratios):
        power = arb(1)
        for j in range(order):
            V[j,i] = power
            power *= ratio
    bG = arb_mat([[b[i]*G[i,k] for k in range(d)] for i in range(2*M+1)])
    S, T = V*G, V*bG

    def weighted_zeta(s, denominator_correction=False):
        out = arb(0)
        for k, cut in enumerate(cuts):
            z = arb(s).zeta(arb(cut+1))
            if k+1 < len(cuts):
                z -= arb(s).zeta(arb(cuts[k+1]+1))
            factor = weights[k]
            if denominator_correction:
                factor /= (1-arb(fmpq(M,cut+1)))**2
            out += factor*z
        return out

    # Only r distinct even exponents are needed; all odd-parity entries are 0.
    moments = {s: arb(M)**(s-2)*2*weighted_zeta(s)
               for s in range(2, 2*order+1, 2)}
    H = arb_mat([[moments[j+k+2] if (j+k)%2 == 0 else arb(0)
                  for k in range(order)] for j in range(order)])
    U0 = (1+eta)*B**2*(S.transpose()*H*S) + (1+1/eta)*(T.transpose()*H*T)
    kappa = 8*B**2*arb(M)**(2*order)*weighted_zeta(2*order+2, True)
    powers = [ratio**order for ratio in ratios]
    cMr = sum((power**2 for power in powers), arb(0))
    if remainder == "weighted":
        weightedG = arb_mat([[powers[i]*G[i,k] for k in range(d)]
                            for i in range(2*M+1)])
        D = kappa*(2*M)*(weightedG.transpose()*weightedG)
    elif remainder == "count":
        D = kappa*cMr*(G.transpose()*G)
    else:
        raise ValueError("remainder must be 'weighted' or 'count'")
    U = (1+tau)*U0 + (1+1/tau)*D
    return {"upper": U, "leading": U0, "remainder": D,
            "moments_S": S, "moments_T": T, "H": H,
            "kappa": kappa, "cMr": cMr}
