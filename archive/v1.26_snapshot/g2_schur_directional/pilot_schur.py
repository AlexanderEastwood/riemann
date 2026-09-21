#!/usr/bin/env python3
"""Finite-output pilot for the residual Schur certificate. No remote-tail bound.

An adverse sign here invalidates this particular Gamma-only budget, not W.
A positive result omits n>J and is not a continuum positivity certificate.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.linalg import eigh
from flint import arb,arb_mat,ctx
from assembly import assemble_sequences,parity_block

BASE=Path(__file__).resolve().parent


def ldl_pilot(A):
    size=A.nrows();D=[];l=[[arb(0) for j in range(size)] for i in range(size)]
    for j in range(size):
        pivot=A[j,j]-sum((l[j][k]**2*D[k] for k in range(j)),arb(0))
        if not pivot>0:
            return dict(status='negative' if pivot<0 else 'unresolved',index=j,pivot=pivot.str(45))
        D.append(pivot)
        for i in range(j+1,size):
            l[i][j]=(A[i,j]-sum((l[i][k]*l[j][k]*D[k] for k in range(j)),arb(0)))/pivot
    return dict(status='positive',count=size,min_pivot=min(D,key=float).str(45))


def run(N=256,M=512,J=1024,parity='even',bits=768,gamma_override=None,save_blocks=True):
    start=time.time();L,b,d=assemble_sequences(J,bits)
    head=list(range(0 if parity=='even' else 1,N+1))
    mid=list(range(N+1,M+1));outer=list(range(M+1,J+1))
    F=parity_block(head,head,parity,b,d)
    T=parity_block(mid,mid,parity,b,d)
    B=parity_block(mid,head,parity,b,d)
    print('assembled',parity,N,M,J,'seconds',time.time()-start,flush=True)
    Z=T.solve(B,algorithm='lu')
    K=F-B.transpose()*Z
    print('solved intermediate',time.time()-start,flush=True)
    U=parity_block(outer,head,parity,b,d)
    V=parity_block(outer,mid,parity,b,d)
    R=U-V*Z
    G=R.transpose()*R
    # Conservative certified rounded constants from sharp_tail_constants.json.
    if gamma_override is not None:gamma=arb(gamma_override)
    elif N==256:gamma=arb('1.5867') if parity=='even' else arb('0.0148')
    elif N==512:gamma=arb('2.2798') if parity=='even' else arb('0.7085')
    else:raise ValueError('Need proved gamma for selected N')
    S=K-G/gamma
    print('formed finite-output Gram',time.time()-start,flush=True)
    f64=np.array([[float(S[i,j]) for j in range(len(head))] for i in range(len(head))])
    ee,vv=eigh(f64,subset_by_index=[0,min(9,len(head)-1)])
    vector=arb_mat([[arb(str(x))] for x in vv[:,0]])
    naive_ray=(vector.transpose()*S*vector)[0,0]
    kldl=ldl_pilot(K);sldl=ldl_pilot(S)
    result=dict(status='PILOT: excludes residual rows beyond J; no whole-window claim.',
                N=N,M=M,J=J,parity=parity,bits=bits,gamma=gamma.str(20),
                K_ldl=kldl,finite_output_S_ldl=sldl,
                float64_S_bottom=[float(x) for x in ee],
                float_vector_arb_rayleigh=naive_ray.str(45),elapsed_seconds=time.time()-start)
    path=BASE/f'pilot_N{N}_M{M}_J{J}_{parity}.json';path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    # Save exact interval blocks for refinement/reuse, not source inference.
    digits=int(bits*.30103)-8
    data=dict(N=N,M=M,J=J,parity=parity,bits=bits,
              K=[[K[i,j].str(digits) for j in range(len(head))] for i in range(len(head))],
              finite_residual_gram=[[G[i,j].str(digits) for j in range(len(head))] for i in range(len(head))])
    if save_blocks:
        (BASE/f'pilot_blocks_N{N}_M{M}_J{J}_{parity}.json').write_text(json.dumps(data)+'\n')
    return result


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,default=256);p.add_argument('--M',type=int,default=512);p.add_argument('--J',type=int,default=1024);p.add_argument('--parity',default='even');p.add_argument('--bits',type=int,default=768);p.add_argument('--gamma');p.add_argument('--no-save-blocks',action='store_true')
    a=p.parse_args();run(a.N,a.M,a.J,a.parity,a.bits,a.gamma,not a.no_save_blocks)
