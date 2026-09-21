#!/usr/bin/env python3
"""Directional infinite-complement certificate at lambda=3.

All arithmetic enclosures use Arb. Z is frozen to exact dyadic midpoints;
every omitted output row, including the infinite remote tail, is bounded.
A failed lower bound is not evidence that the Weil operator is negative.
"""
import argparse, json, time, gzip, hashlib
from pathlib import Path
from flint import arb, arb_mat, ctx
from assembly import assemble_sequences, parity_block

BASE=Path(__file__).resolve().parent

def ldl_certificate(A):
    size=A.nrows();D=[];lower=[[arb(0) for j in range(size)] for i in range(size)]
    for j in range(size):
        pivot=A[j,j]-sum((lower[j][k]**2*D[k] for k in range(j)),arb(0))
        if not pivot>0:
            return dict(status='negative' if pivot<0 else 'unresolved',index=j,pivot=pivot.str(55)),D
        D.append(pivot)
        for i in range(j+1,size):
            lower[i][j]=(A[i,j]-sum((lower[i][k]*lower[j][k]*D[k] for k in range(j)),arb(0)))/pivot
    return dict(status='positive',count=size,min_pivot=min(D,key=float).str(55)),D

def run(N=256,M=512,J=1024,r=128,parity='even',bits=768,diagonal=False,witness=None):
    start=time.time();L,b,d=assemble_sequences(J,bits)
    head=list(range(0 if parity=='even' else 1,N+1))
    mid=list(range(N+1,M+1)); support=head+mid
    nh=len(head); ns=len(support)
    F=parity_block(head,head,parity,b,d)
    T=parity_block(mid,mid,parity,b,d)
    B=parity_block(mid,head,parity,b,d)
    if witness:
        w=json.loads(gzip.decompress(Path(witness).read_bytes()))
        assert w['N']==N and w['M']==M and w['parity']==parity
        Z=arb_mat([[arb(m)*arb(2)**e for m,e in row] for row in w['Z_dyadics']])
        assert all(Z[i,j].is_exact() for i in range(Z.nrows()) for j in range(Z.ncols()))
    else:
        Z=T.solve(B,algorithm='lu').mid()
    dyadics=[[[str(v[0]),int(v[1])] for v in [Z[i,j].man_exp() for j in range(Z.ncols())]] for i in range(Z.nrows())]
    wbytes=json.dumps(dict(N=N,M=M,parity=parity,Z_dyadics=dyadics),separators=(',',':')).encode()
    witness_name=f'schur_witness_N{N}_M{M}_{parity}_b{bits}.json.gz'
    (BASE/witness_name).write_bytes(gzip.compress(wbytes,mtime=0))
    witness_sha=hashlib.sha256(wbytes).hexdigest()
    G=arb_mat([[int(i==j) if i<nh else -Z[i-nh,j]
                for j in range(nh)] for i in range(ns)])
    K=F-B.transpose()*Z-Z.transpose()*B+Z.transpose()*T*Z
    print('formed frozen-Z K',parity,time.time()-start,flush=True)
    R=parity_block(list(range(N+1,J+1)),support,parity,b,d)*G
    finite_gram=R.transpose()*R
    print('all finite residual rows',time.time()-start,flush=True)

    # Moments of the full signed-index coefficient rows, represented in the
    # orthonormal parity basis. The +/-m conversion contributes sqrt(2).
    sqrt2=arb(2).sqrt()
    Sm=arb_mat(r,ns);Tm=arb_mat(r,ns)
    for col,m in enumerate(support):
        q=arb(m)/M; power=arb(1)
        for j in range(r):
            if m==0:
                if j==0:Sm[j,col]=1
            else:
                s_nonzero=(j%2==0) if parity=='even' else (j%2==1)
                if s_nonzero:Sm[j,col]=sqrt2*power
                else:Tm[j,col]=sqrt2*power*b[m]
            power*=q
    S=Sm*G; U=Tm*G
    psums=[arb(k+2).zeta(arb(J+1)) for k in range(2*r-1)]
    powers=[arb(M)**k for k in range(2*r-1)]
    H=arb_mat([[2*powers[j+k]*psums[j+k] if (j+k)%2==0 else 0
                for k in range(r)] for j in range(r)])
    pdat=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
    P=sum((arb(p).log()/arb(m).sqrt() for m,p in pdat),arb(0))
    bstar=(arb(4)/3+P+1+arb.pi()/4)/arb.pi()
    leading=2*bstar**2*S.transpose()*H*S+2*U.transpose()*H*U
    cmr=2*sum(((arb(m)/M)**(2*r) for m in range(1,M+1)),arb(0))
    delta2=8*bstar**2*cmr*arb(M)**(2*r)*arb(2*r+2).zeta(arb(J+1))/(1-arb(M)/(J+1))**2
    tau=arb(1)/10**6
    remote=(1+tau)*leading+(1+1/tau)*delta2*(G.transpose()*G)
    print('remote Gram majorant',time.time()-start,flush=True)

    # Recompute the proved positive weighted-prime bound, rather than relying
    # on a decimal approximation to the lower tail constant.
    coeff={2:(85,116),3:(65,87),4:(193,232),5:(137,145),7:(35,29)}
    pp={2:2,3:3,4:2,5:5,7:7}
    prime=sum((arb(a)/c*arb(pp[m]).log()/arb(m).sqrt()
               for m,(a,c) in coeff.items()),arb(0))
    t=2*arb.pi()*(N+1)/L
    error=1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+arb(54)/80)/(L*t*t)
    gamma=(arb(N+1)/L).log()-prime-2/t-error
    if parity=='odd':gamma-=arb.pi()/2+4*L/(3*arb.pi()**2*N)
    assert gamma>0
    if diagonal:
        def g(n):
            tn=2*arb.pi()*n/L
            en=1/(15*tn)+arb(7)/(2*tn*tn)+arb.pi()/(2*L*tn)+(2+arb(54)/80)/(L*tn*tn)
            return gamma+(arb(n)/(N+1)).log()+error-en
        gs=[g(n) for n in range(N+1,J+1)]
        weighted_R=arb_mat([[R[i,j]/gs[i] for j in range(nh)]
                           for i in range(R.nrows())])
        lower=K-R.transpose()*weighted_R-remote/g(J+1)
    else:
        lower=K-(finite_gram+remote)/gamma
    print('begin interval LDL',time.time()-start,flush=True)
    result,pivots=ldl_certificate(lower)
    report=dict(status='PASS: infinite-complement lower form is positive' if result['status']=='positive'
                else 'NO CERTIFICATE: a lower-majorant failure is not operator negativity',
                N=N,M=M,J=J,r=r,parity=parity,bits=bits,diagonal_inverse=diagonal,
                exact_window_lambda=3,tail_gamma=gamma.str(55),
                bstar=bstar.str(55),cmr=cmr.str(55),delta_squared=delta2.str(55),
                tau='1/1000000',ldl=result,
                witness_file=witness_name,witness_uncompressed_sha256=witness_sha,
                pivot_enclosures=[p.str(65) for p in pivots],
                max_finite_gram_diagonal=max((finite_gram[i,i] for i in range(nh)),key=float).str(40),
                max_remote_gram_diagonal=max((remote[i,i] for i in range(nh)),key=float).str(40),
                scope='Fixed window and parity only. No uniform-in-window G2 or RH claim.',
                elapsed_seconds=time.time()-start)
    suffix='_diagonal' if diagonal else ''
    path=BASE/f'infinite_schur_N{N}_M{M}_J{J}_r{r}_{parity}_b{bits}{suffix}.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='pivot_enclosures'},indent=2),flush=True)
    return report

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name,default in [('N',256),('M',512),('J',1024),('r',128),('bits',768)]:
        p.add_argument('--'+name,type=int,default=default)
    p.add_argument('--parity',choices=['even','odd'],default='even')
    p.add_argument('--diagonal',action='store_true')
    p.add_argument('--witness')
    run(**vars(p.parse_args()))
