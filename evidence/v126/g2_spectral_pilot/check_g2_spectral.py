#!/usr/bin/env python3
"""Actual finite Weil matrix / repaired prolate source pilot.

Numerical evidence only: quadrature and Galerkin comparisons are not rigorous
error enclosures. No zeta zeros, RH assumptions, or fitted source coefficients.
Dependencies: numpy, scipy, mpmath. Run this file to write g2_spectral_checks.json.
"""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.special import roots_legendre
from scipy.linalg import eigh, null_space
from numpy.polynomial.legendre import legval


def prime_powers(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p*p::p] = False
    powers, weights = [], []
    for p in np.flatnonzero(sieve):
        k = int(p)
        while k <= limit:
            powers.append(k)
            weights.append(np.log(p) / np.sqrt(k))
            k *= int(p)
    order = np.argsort(powers)
    return np.log(np.asarray(powers)[order]), np.asarray(weights)[order]


def weil_matrix(length, nmax, extra_nodes=0):
    """Original [0,L] Fourier basis, separate correct logarithmic diagonal."""
    npos = np.arange(nmax + 1)
    tpos = 2*np.pi*npos / length
    nodes, weights = roots_legendre(2*nmax + 300 + extra_nodes)
    y = (nodes + 1)*length/2
    w = weights*length/2
    rho = np.exp(y/2) / (2*np.sinh(y))
    sin = np.sin(tpos[:, None]*y)
    cos = np.cos(tpos[:, None]*y)
    # A prime power at the support endpoint has zero diagonal weight and
    # sin(2*pi*n)=0; rounding exp(L) across it does not change the exact form.
    jumps, prime_w = prime_powers(int(np.floor(np.exp(length)+1e-10)))
    phase = tpos[:, None]*jumps
    point_b = 32*length*np.sinh(length/4)**2*npos / (length**2 + 16*np.pi**2*npos**2)
    bpos = point_b + (sin @ (w*rho) + np.sin(phase) @ prime_w)/np.pi
    pole_diag = (32*length*np.sinh(length/4)**2
        * (length**2-16*np.pi**2*npos**2)
        / (length**2+16*np.pi**2*npos**2)**2)
    prime_diag = 2*np.cos(phase) @ ((1-jumps/length)*prime_w)
    arch_diag = ((2*(1-y/length)*cos - 2*np.exp(-y/2)) @ (w*rho)
        + np.log(4*np.pi) + float(mp.euler) + np.log(np.tanh(length/2)))
    diagpos = pole_diag-prime_diag-arch_diag
    b = np.concatenate((-bpos[:0:-1], bpos))
    diag = np.concatenate((diagpos[:0:-1], diagpos))
    n = np.arange(-nmax, nmax+1)
    distance = n[:, None]-n[None, :]
    matrix = np.divide(b[:, None]-b[None, :], distance,
        out=np.zeros(distance.shape), where=distance != 0)
    np.fill_diagonal(matrix, diag)
    return matrix


def repaired_source(lam_string, size=55, digits=85, return_mp=False, return_coefficients=False):
    mp.mp.dps = digits
    lam = mp.mpf(lam_string)
    c = 2*mp.pi*lam**2
    aa = lambda j: (j+1)/mp.sqrt((2*j+1)*(2*j+3)) if j >= 0 else mp.mpf(0)
    mat = mp.matrix(size)
    for k in range(size):
        ell = 2*k
        mat[k,k] = ell*(ell+1)+c*c*(aa(ell)**2+aa(ell-1)**2)
        if k+1 < size:
            mat[k,k+1] = mat[k+1,k] = c*c*aa(ell)*aa(ell+1)
    values, vectors = mp.eigsy(mat)
    modes = []
    for col in (0,2):
        coeff = [vectors[k,col]*mp.sqrt(mp.mpf(4*k+1)/2)/mp.sqrt(lam)
                 for k in range(size)]
        center = mp.fsum(coeff[k]*(-1)**k*mp.binomial(2*k,k)/4**k
                         for k in range(size))
        sign = mp.sign(center)
        coeff = [sign*x for x in coeff]
        modes.append((coeff, abs(center), 2*lam*coeff[0]))
    # Integral h_n = chi_n h_n(0). These are precisely manuscript a_0,a_4.
    a0, a4 = -modes[1][2], modes[0][2]
    hc = [a0*modes[0][0][k]+a4*modes[1][0][k] for k in range(size)]
    hzero = mp.fsum(hc[k]*(-1)**k*mp.binomial(2*k,k)/4**k for k in range(size))
    radius = mp.mpf(3)/4
    def phi(x):
        return mp.exp(1-1/(1-(x/radius)**2)) if abs(x)<radius else mp.mpf(0)
    i0 = mp.quad(phi, [0,radius/2,radius])
    i2 = mp.quad(lambda x: x*x*phi(x), [0,radius/2,radius])
    moment_ratio = i0/i2
    def hmp(x):
        # Three-term recurrence avoids repeated independent polynomial calls.
        xx=x/lam; previous=mp.mpf(1); current=xx; raw=hc[0]
        for degree in range(2,2*size-1):
            following=((2*degree-1)*xx*current-(degree-1)*previous)/degree
            if degree%2==0:
                raw += hc[degree//2]*following
            previous,current=current,following
        return raw-hzero*phi(x)*(1-moment_ratio*x*x)
    bplus = mp.sqrt(lam)*mp.fsum(hc)
    # Interior lower trace: n=lambda^2 is excluded when lambda^2 is integral.
    count = int(mp.ceil(lam**2))-1
    lower = mp.fsum(hmp(mp.mpf(n)/lam) for n in range(1,count+1))/mp.sqrt(lam)
    endpoint = (bplus+lower)/2
    coeff64 = np.zeros(2*size-1)
    coeff64[::2] = [float(x) for x in hc]
    z64, ratio64, l64 = float(hzero),float(moment_ratio),float(lam)
    def h(x):
        x = np.asarray(x)
        bump = np.zeros_like(x)
        inside = np.abs(x)<.75
        bump[inside] = np.exp(1-1/(1-(x[inside]/.75)**2))*(1-ratio64*x[inside]**2)
        return legval(x/l64,coeff64)-z64*bump
    metadata = dict(lambda_=l64,c=float(c),legendre_even_dimension=size,digits=digits,
        h_at_zero_before_repair=mp.nstr(hzero,30),B_plus=mp.nstr(bplus,30),
        B_physical=mp.nstr(endpoint,30),B_over_B_plus=mp.nstr(endpoint/bplus,25),
        bump_radius=.75,bump_moment_ratio=mp.nstr(moment_ratio,30),
        raw_integral_check=mp.nstr(2*lam*hc[0],10))
    if return_coefficients:
        return h,hmp,metadata,hc
    return (h,hmp,metadata) if return_mp else (h,metadata)


def source_coefficients(lam, nmax, h, quad_order=180):
    length = 2*np.log(lam)
    a = length/2
    # Every arithmetic endpoint jump is an integration breakpoint.
    points = [-a,a]
    for n in range(1,int(np.ceil(lam*lam))+1):
        for v in (lam/n,.75/n):
            if 1/lam < v < lam:
                points.append(np.log(v))
    points = sorted(set(points))
    nodes, weights = roots_legendre(quad_order)
    coeff = np.zeros(nmax+1)
    for left,right in zip(points,points[1:]):
        x = (left+right)/2+(right-left)/2*nodes
        u = np.exp(x)
        k = np.zeros_like(u)
        for n in range(1,int(np.floor(lam/np.exp((left+right)/2)))+1):
            k += h(n*u)
        k *= np.sqrt(u)
        coeff += np.cos(2*np.pi*np.arange(nmax+1)[:,None]*x/length) @ (weights*k)*(right-left)/2
    coeff /= np.sqrt(length)
    coeff *= np.where(np.arange(nmax+1)%2==0,1,-1) # centered -> [0,L]
    return np.concatenate((coeff[:0:-1],coeff))


def diagnostics(w,coeff,length,endpoint):
    norm = np.linalg.norm(coeff)
    u = coeff/norm
    alpha = float(u @ w @ u)
    residual = w@u-alpha*u
    epsilon = float(np.linalg.norm(residual))
    basis = null_space(u[None,:])
    beta = float(eigh(basis.T@w@basis,subset_by_index=[0,0],eigvals_only=True)[0])
    gamma = beta-alpha
    ev,evec = eigh(w,subset_by_index=[0,min(3,w.shape[0]-1)])
    overlap = float(abs(u@evec[:,0]))
    sine = float(np.sqrt(max(0,1-overlap**2)))
    nmax = (w.shape[0]-1)//2
    qe = np.zeros((2*nmax+1,nmax+1)); qe[nmax,0]=1
    qo = np.zeros((2*nmax+1,nmax))
    for n in range(1,nmax+1):
        qe[nmax-n,n] = qe[nmax+n,n] = 1/np.sqrt(2)
        qo[nmax-n,n-1] = 1/np.sqrt(2); qo[nmax+n,n-1]=-1/np.sqrt(2)
    even_low = eigh(qe.T@w@qe,subset_by_index=[0,min(2,nmax)],eigvals_only=True)
    odd_low = eigh(qo.T@w@qo,subset_by_index=[0,min(2,nmax-1)],eigvals_only=True)
    return dict(N=nmax,dimension=w.shape[0],source_norm=float(norm),alpha=alpha,
        residual=epsilon,complement_bottom=beta,gamma=gamma,
        residual_over_gamma=epsilon/gamma if gamma>0 else None,
        ground_eigenvalue=float(ev[0]),ground_gap=float(ev[1]-ev[0]),
        lowest_eigenvalues=ev.tolist(),even_lowest=even_low.tolist(),odd_lowest=odd_low.tolist(),
        source_ground_overlap=overlap,source_ground_angle_sine=sine,
        projected_source_endpoint=float(np.sum(coeff)/np.sqrt(length)),
        relative_endpoint_error=float(abs(np.sum(coeff)/np.sqrt(length)-endpoint)/abs(endpoint)),
        symmetry_error=float(np.max(np.abs(w-w.T))),
        reflection_error=float(np.max(np.abs(w-w[::-1,::-1]))),
        even_source_error=float(np.max(np.abs(u-u[::-1]))))


def main():
    rows=[]; checks=[]
    for lam_str in ('1.5','2','2.5','3'):
        h,meta = repaired_source(lam_str)
        lam = float(lam_str); length=2*np.log(lam)
        full = source_coefficients(lam,64,h)
        row = dict(source=meta,finite=[])
        for nmax in (8,16,32,64):
            coeff = full[64-nmax:64+nmax+1]
            w = weil_matrix(length,nmax)
            d = diagnostics(w,coeff,length,float(meta['B_physical']))
            row['finite'].append(d)
            print(json.dumps(dict(lambda_=lam,**d)),flush=True)
        coeff_refined = source_coefficients(lam,64,h,320)
        w0=weil_matrix(length,64); w1=weil_matrix(length,64,300)
        checks.append(dict(lambda_=lam,
            observed_matrix_quadrature_difference_norm=float(np.linalg.norm(w1-w0,2)),
            observed_source_quadrature_difference_norm=float(np.linalg.norm(coeff_refined-full)),
            refined_diagnostics=diagnostics(w1,coeff_refined,length,float(meta['B_physical']))))
        rows.append(row)
    out=dict(status='NON-CERTIFIED NUMERICAL PILOT; no truncation or interval enclosure.',
        source='Manuscript normalized n=0,4 angular PSWF source with fixed exact scalar repair; finite Legendre approximation.',
        finite_object='P_N p_lambda and actual (2N+1)-dimensional Weil matrix in [0,L] basis; diagnostic N only, not asymptotic cutoff.',
        repair='phi=exp(1-1/(1-(t/(3/4))^2)) on |t|<3/4, psi=phi*(1-C*t^2), C=integral(phi)/integral(t^2*phi).',
        rows=rows,convergence_checks=checks)
    Path(__file__).with_name('g2_spectral_checks.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':
    main()
