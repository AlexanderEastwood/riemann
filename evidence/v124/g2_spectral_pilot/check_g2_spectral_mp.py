#!/usr/bin/env python3
"""High-precision continuation of the actual Weil/source experiment.

All estimates are numerical, not interval certified. Requires the companion
check_g2_spectral.py. Run to write g2_spectral_mp_checks.json incrementally.
"""
import json
from pathlib import Path
import mpmath as mp
from check_g2_spectral import repaired_source


def prime_data(limit):
    out=[]
    for p in range(2,limit+1):
        if all(p%j for j in range(2,int(p**.5)+1)):
            k=p
            while k<=limit:
                out.append((mp.log(k),mp.log(p)/mp.sqrt(k)))
                k*=p
    return sorted(out)


def matrix(lam,nmax,nodes,weights):
    length=2*mp.log(lam)
    ts=[2*mp.pi*n/length for n in range(nmax+1)]
    ys=[(x+1)*length/2 for x in nodes]
    ws=[w*length/2 for w in weights]
    rhos=[mp.exp(y/2)/(2*mp.sinh(y)) for y in ys]
    primes=prime_data(int(mp.floor(lam**2)))
    bs=[]; ds=[]
    for n,t in enumerate(ts):
        denom=length**2+16*mp.pi**2*n*n
        point_b=32*length*mp.sinh(length/4)**2*n/denom
        bs.append(point_b+(mp.fsum(mp.sin(t*y)*w*rho for y,w,rho in zip(ys,ws,rhos))
            +mp.fsum(mp.sin(t*y)*v for y,v in primes))/mp.pi)
        pole=32*length*mp.sinh(length/4)**2*(length**2-16*mp.pi**2*n*n)/denom**2
        prime=2*mp.fsum(mp.cos(t*y)*(1-y/length)*v for y,v in primes)
        arch=mp.fsum((2*(1-y/length)*mp.cos(t*y)-2*mp.exp(-y/2))*w*rho
            for y,w,rho in zip(ys,ws,rhos))+mp.log(4*mp.pi)+mp.euler+mp.log(mp.tanh(length/2))
        ds.append(pole-prime-arch)
    w=mp.matrix(2*nmax+1)
    b=lambda n: mp.sign(n)*bs[abs(n)]
    for i,n in enumerate(range(-nmax,nmax+1)):
        for j,m in enumerate(range(-nmax,nmax+1)):
            w[i,j]=ds[abs(n)] if n==m else (b(n)-b(m))/(n-m)
    return w


def coefficients(lam,nmax,h,nodes,weights):
    length=2*mp.log(lam); a=length/2; radius=mp.mpf(3)/4
    points=[-a,a]
    for n in range(1,int(mp.ceil(lam**2))+1):
        for v in (lam/n,radius/n):
            if 1/lam<v<lam: points.append(mp.log(v))
    points=sorted(set(points))
    co=[mp.mpf(0)]*(nmax+1)
    for left,right in zip(points,points[1:]):
        count=int(mp.floor(lam/mp.exp((left+right)/2)))
        for node,weight in zip(nodes,weights):
            x=(left+right)/2+(right-left)*node/2
            u=mp.exp(x)
            k=mp.sqrt(u)*mp.fsum(h(n*u) for n in range(1,count+1))
            amp=k*weight*(right-left)/2/mp.sqrt(length)
            for n in range(nmax+1):
                co[n]+=amp*mp.cos(2*mp.pi*n*x/length)*(-1)**n
    return mp.matrix([co[abs(n)] for n in range(-nmax,nmax+1)])


def diagnostic(w,co,length,endpoint):
    dim=w.rows; nmax=(dim-1)//2
    norm=mp.norm(co); u=co/norm; alpha=(u.T*w*u)[0]
    r=w*u-alpha*u; eps=mp.norm(r)
    v=u.copy(); v[0]-=1
    house=mp.eye(dim)-2*v*v.T/(v.T*v)[0]
    basis=house[:,1:]
    c=basis.T*w*basis
    ce=mp.eigsy(c,eigvals_only=True)
    gamma=ce[0]-alpha
    ev,vec=mp.eigsy(w)
    overlap=abs((u.T*vec[:,0])[0]); sine=mp.sqrt(abs(1-overlap**2))
    out=dict(N=nmax,dimension=dim,alpha=alpha,residual=eps,complement_bottom=ce[0],
        gamma=gamma,source_norm=norm,ground_eigenvalue=ev[0],ground_gap=ev[1]-ev[0],
        ground_angle_sine=sine,ground_overlap=overlap,
        ground_odd_part_norm=mp.norm(mp.matrix([(vec[i,0]-vec[dim-1-i,0])/2 for i in range(dim)])),
        projected_endpoint=mp.fsum(co)/mp.sqrt(length),
        relative_endpoint_error=abs(mp.fsum(co)/mp.sqrt(length)-endpoint)/abs(endpoint),
        operator_norm=max(abs(x) for x in ev),
        lowest_eigenvalues=[mp.nstr(x,35) for x in ev[:6]])
    if gamma>0:
        x=mp.lu_solve(c-alpha*mp.eye(dim-1),basis.T*r)
        q=mp.norm(x); energy=((basis.T*r).T*x)[0]
        out.update(residual_over_gamma=eps/gamma,schur_tangent_bound=q,
            schur_sine_bound=q/mp.sqrt(1+q*q),schur_energy_bound=energy,
            lower_ground_bound=alpha-energy,
            normalized_inverse_residual=mp.norm((c-alpha*mp.eye(dim-1))*x-basis.T*r)/max(mp.norm(basis.T*r),mp.mpf('1e-100')))
    else:
        out.update(residual_over_gamma=None,schur_tangent_bound=None)
    return {key:mp.nstr(value,35) if isinstance(value,mp.mpf) else value for key,value in out.items()}


def main():
    path=Path(__file__).with_name('g2_spectral_mp_checks.json')
    results=dict(status='Arbitrary-precision numerical evidence only; no rigorous matrix/source/Fourier-tail error enclosure.',rows=[])
    # Precision, source dimension, quadrature and Fourier cut are varied separately
    # in the saved metadata. Their agreement is a diagnostic, not a certificate.
    configs=[('2',55,80,160),('2.5',55,80,160),('3',55,80,160),
             ('2',70,105,224),('2.5',70,105,224),('3',70,105,224)]
    for lamstr,size,digits,order in configs:
        _,h,meta=repaired_source(lamstr,size,digits,return_mp=True)
        lam=mp.mpf(lamstr); length=2*mp.log(lam)
        nodes,weights=mp.gauss_quadrature(order,'legendre')
        co=coefficients(lam,32,h,nodes,weights)
        w=matrix(lam,32,nodes,weights)
        row=dict(source=meta,quadrature_order=order,finite=[])
        for nmax in (8,16,32):
            lo=32-nmax; hi=32+nmax+1
            info=diagnostic(w[lo:hi,lo:hi],co[lo:hi,:],length,mp.mpf(meta['B_physical']))
            row['finite'].append(info)
            print(json.dumps(dict(lambda_=lamstr,size=size,digits=digits,order=order,**info)),flush=True)
        # Retain the computed finite objects for independent comparison.
        row['coefficient_vector_N32']=[mp.nstr(x,70) for x in co]
        row['matrix_N32']=[[mp.nstr(w[i,j],70) for j in range(w.cols)] for i in range(w.rows)]
        results['rows'].append(row)
        path.write_text(json.dumps(results,indent=2)+'\n')


if __name__=='__main__':
    main()
