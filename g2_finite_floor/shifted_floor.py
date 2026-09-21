"""Complete shifted Weil-form certificates; no positive weighted-tail metric.

Uses the archived, audited Arb coefficient assembly without modification.
Exact finite head, explicit rows to J, and moment enclosure beyond J.
The zero solve Z=0 is deliberate. Floating Cholesky only proposes an exact
dyadic congruence; every acceptance gate is outward Arb arithmetic.
"""
import argparse, json, time, hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import cholesky, solve_triangular, eigh
from threadpoolctl import threadpool_limits
from assembly_general import arb, arb_mat, ctx, sequences, pairs, prime_bound

def actual_block(rows, cols, parity, b, d):
    def signed(n,m):
        if n==m: return d[abs(n)]
        bn=b[abs(n)] if n>=0 else -b[abs(n)]
        bm=b[abs(m)] if m>=0 else -b[abs(m)]
        return (bn-bm)/(n-m)
    rt=arb(2).sqrt()
    def e(n,m):
        if n==m==0:return d[0]
        if n==0 or m==0:return rt*signed(n,m)
        return signed(n,m)+(1 if parity=='even' else -1)*signed(n,-m)
    return arb_mat([[e(n,m) for m in cols] for n in rows])

def setup(lam,N,J,r,bits,parity):
    L,b,d,a=sequences(lam,J,bits,K=64)
    head=list(range(0 if parity=='even' else 1,N+1));nh=len(head)
    F=actual_block(head,head,parity,b,d)
    R=actual_block(list(range(N+1,J+1)),head,parity,b,d)
    Sm=arb_mat(r,nh);Tm=arb_mat(r,nh)
    rt=arb(2).sqrt()
    for col,m in enumerate(head):
        if m==0:
            Sm[0,col]=1
            continue
        power=arb(1)
        for j in range(r):
            if (j%2==0)==(parity=='even'):Sm[j,col]=rt*power
            else:Tm[j,col]=rt*power*b[m]
            power*=arb(m)/N
    powers=[arb(N)**j for j in range(2*r-1)]
    ps=[arb(j+2).zeta(arb(J+1)) for j in range(2*r-1)]
    H=arb_mat([[2*powers[j+k]*ps[j+k] if (j+k)%2==0 else 0 for k in range(r)] for j in range(r)])
    P=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(lam)),arb(0))
    h=(L/4).sinh()**2;Bstar=(4*h+P+1+arb.pi()/4)/arb.pi()
    cmr=2*sum(((arb(m)/N)**(2*r) for m in range(1,N+1)),arb(0))
    delta2=8*Bstar**2*cmr*arb(N)**(2*r)*arb(2*r+2).zeta(arb(J+1))/(1-arb(N)/(J+1))**2
    ident=arb_mat([[int(i==j) for j in range(nh)] for i in range(nh)])
    tau=arb(1)/10
    U=(1+tau)*(2*Bstar**2*Sm.transpose()*H*Sm+2*Tm.transpose()*H*Tm)+(1+1/tau)*delta2*ident
    RL=arb(1)/lam/(1-arb(1)/lam**4)
    assert arb(1)>=arb(1)/4+RL
    kap=prime_bound(lam)+2/(2*arb.pi()*(N+1)/L)
    if parity=='odd':kap+=arb.pi()/2+4*h*L/(arb.pi()**2*N)
    def g(n):
        t=2*arb.pi()*n/L
        E=1/(15*t)+arb(7)/(2*t*t)+arb.pi()/(2*L*t)+(2+2*RL)/(L*t*t)
        return (arb(n)/L).log()-E-kap
    gs=[g(n) for n in range(N+1,J+1)]
    return F,R,U,ident,gs,g(J+1),{'g_start':gs[0].str(45),'g_remote':g(J+1).str(45),'kappa':kap.str(45),'Bstar':Bstar.str(45),'moment_remainder_squared':delta2.str(45)}

def test_shift(data,shift):
    F,R,U,I,gs,gJ,meta=data;d=arb(shift);nh=F.nrows()
    if not gs[0]+d>0:return {'shift':shift,'status':'TAIL GATE FAIL'}
    weighted=arb_mat([[R[i,j]/(gs[i]+d) for j in range(nh)] for i in range(R.nrows())])
    lower=F+d*I-R.transpose()*weighted-U/(gJ+d)
    mid=np.array([[float(lower[i,j].mid()) for j in range(nh)] for i in range(nh)])
    try:
        with threadpool_limits(2):
            L=cholesky(mid,lower=True)
            C=solve_triangular(L,np.eye(nh),lower=True)
    except Exception as ex:
        return {'shift':shift,'status':'PROPOSAL FAIL','min_midpoint_eigenvalue':float(eigh(mid,subset_by_index=[0,0],eigvals_only=True)[0])}
    Cb=arb_mat([[arb(float(x)) for x in row] for row in C])
    assert all(Cb[i,j].is_exact() for i in range(nh) for j in range(nh))
    assert all(Cb[i,i]!=0 for i in range(nh))
    assert all(Cb[i,j]==0 for i in range(nh) for j in range(i+1,nh))
    Y=Cb*lower*Cb.transpose()
    margins=[Y[i,i]-sum((abs(Y[i,j]) for j in range(nh) if i!=j),arb(0)) for i in range(nh)]
    ok=all(x>0 for x in margins)
    minmargin=min(float(x.lower()) for x in margins)
    out={'shift':shift,'status':'PASS' if ok else 'INTERVAL GATE FAIL','all_rows_positive':ok,'congruence_margin_display':minmargin,'tail_floor':(gs[0]+d).str(45),'remote_floor':(gJ+d).str(45)}
    if ok:
        out['C_dyadic']=[[[str(m),int(e)] for m,e in [Cb[i,j].man_exp() for j in range(nh)]] for i in range(nh)]
    return out

def trial(F):
    n=F.nrows();mid=np.array([[float(F[i,j].mid()) for j in range(n)] for i in range(n)])
    with threadpool_limits(2):vals,V=eigh(mid,subset_by_index=[0,0])
    v=arb_mat([[arb(float(x))] for x in V[:,0]])
    assert all(v[i,0].is_exact() for i in range(n))
    q=(v.transpose()*F*v)[0,0]/(v.transpose()*v)[0,0]
    return {'midpoint_eigenvalue_not_certificate':float(vals[0]),'rayleigh_interval':q.str(65),'upper_below_1e_minus8':bool(q<arb(1)/10**8),'certified_negative':bool(q<0),'vector_dyadic':[[str(m),int(e)] for m,e in [v[i,0].man_exp() for i in range(n)]]}

def main():
    p=argparse.ArgumentParser();p.add_argument('--lam',type=int,required=True);p.add_argument('--parity',required=True);p.add_argument('--N',type=int,default=128);p.add_argument('--J',type=int,default=2048);p.add_argument('--r',type=int,default=16);p.add_argument('--bits',type=int,default=160);p.add_argument('--shifts',default='5,6,7,8,9,10')
    args=p.parse_args();begin=time.time();data=setup(args.lam,args.N,args.J,args.r,args.bits,args.parity)
    print('setup',args.lam,args.parity,round(time.time()-begin,2),flush=True)
    out={'parameters':vars(args),'scope':'Complete physical parity form including infinite tail; no weighted cD metric, no RH assumption','tail':data[-1],'trial':trial(data[0]),'attempts':[]}
    for s in args.shifts.split(','):
        ans=test_shift(data,s);out['attempts'].append(ans)
        print({k:v for k,v in ans.items() if k!='C_dyadic'},flush=True)
        if ans['status']=='PASS':break
    out['seconds']=round(time.time()-begin,3)
    dest=Path(__file__).with_name(f'floor_l{args.lam}_{args.parity}_N{args.N}_b{args.bits}.json')
    dest.write_text(json.dumps(out,indent=2)+'\n')
    print('saved',dest.name,flush=True)
if __name__=='__main__':main()
