#!/usr/bin/env python3
"""N=64 refinement; both parity sectors retained. Not a certificate."""
import json
from pathlib import Path
import mpmath as mp
from check_g2_spectral import repaired_source
from check_g2_spectral_mp import matrix, coefficients


def run(lamstr='3',size=70,digits=105,order=320,nmax=64):
    _,h,meta=repaired_source(lamstr,size,digits,return_mp=True)
    lam=mp.mpf(lamstr); length=2*mp.log(lam)
    nodes,weights=mp.gauss_quadrature(order,'legendre')
    co=coefficients(lam,nmax,h,nodes,weights)
    w=matrix(lam,nmax,nodes,weights)
    norm=mp.norm(co); u=co/norm
    qe=mp.matrix(2*nmax+1,nmax+1); qo=mp.matrix(2*nmax+1,nmax)
    qe[nmax,0]=1
    for n in range(1,nmax+1):
        qe[nmax-n,n]=qe[nmax+n,n]=1/mp.sqrt(2)
        qo[nmax-n,n-1]=1/mp.sqrt(2); qo[nmax+n,n-1]=-1/mp.sqrt(2)
    we=qe.T*w*qe; wo=qo.T*w*qo; ue=qe.T*u
    alpha=(ue.T*we*ue)[0]; r=we*ue-alpha*ue
    v=ue.copy(); v[0]-=1
    house=mp.eye(nmax+1)-2*v*v.T/(v.T*v)[0]
    basis=house[:,1:]; c=basis.T*we*basis
    ce=mp.eigsy(c,eigvals_only=True)
    ee,ev=mp.eigsy(we); oe=mp.eigsy(wo,eigvals_only=True)
    beta=min(ce[0],oe[0]); gamma=beta-alpha
    combined=sorted(list(ee)+list(oe))
    overlap=abs((ue.T*ev[:,0])[0]) if ee[0]<oe[0] else mp.mpf(0)
    info=dict(alpha=alpha,residual=mp.norm(r),complement_bottom=beta,gamma=gamma,
        ground_eigenvalue=combined[0],ground_gap=combined[1]-combined[0],
        ground_angle_sine=mp.sqrt(abs(1-overlap**2)),ground_is_even=bool(ee[0]<oe[0]),
        even_complement_bottom=ce[0],odd_bottom=oe[0],source_norm=norm,
        projected_endpoint=mp.fsum(co)/mp.sqrt(length),
        relative_endpoint_error=abs(mp.fsum(co)/mp.sqrt(length)-mp.mpf(meta['B_physical']))/abs(mp.mpf(meta['B_physical'])))
    if gamma>0:
        z=mp.lu_solve(c-alpha*mp.eye(nmax),basis.T*r)
        q=mp.norm(z); energy=((basis.T*r).T*z)[0]
        info.update(residual_over_gamma=mp.norm(r)/gamma,schur_tangent_bound=q,
            schur_sine_bound=q/mp.sqrt(1+q*q),schur_energy_bound=energy,
            lower_ground_bound=alpha-energy,
            normalized_inverse_residual=mp.norm((c-alpha*mp.eye(nmax))*z-basis.T*r)/mp.norm(r))
    row=dict(source=meta,N=nmax,dimension=2*nmax+1,quadrature_order=order,
        status='Non-certified high-precision finite calculation; both parity sectors.',
        diagnostics={k:mp.nstr(v,35) if isinstance(v,mp.mpf) else v for k,v in info.items()},
        even_lowest=[mp.nstr(x,35) for x in ee[:4]],odd_lowest=[mp.nstr(x,35) for x in oe[:4]])
    print(json.dumps(row),flush=True)
    Path(__file__).with_name('g2_spectral_wide_checks.json').write_text(json.dumps(row,indent=2)+'\n')


if __name__=='__main__':
    run()
