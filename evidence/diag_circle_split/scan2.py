"""Validate the off-grid symbol against sequences() d_n, and get full lobe geometry."""
import sys, math
sys.path.insert(0,'evidence/v124/g2_schur_cancellation')  # run from repo root
from symbol_scan import make_beta
from assembly_general import sequences
from flint import ctx
zeros=[14.1347,21.0220,25.0109,30.4249,32.9351,37.5862,40.9187,43.3271,48.0052,49.7738,52.9703,56.4462,59.3470,60.8318,65.1125,67.0798,69.5464,72.0672,75.7047,77.1448,79.3374,82.9104,84.7355,87.4253,88.8091,92.4919,94.6513,95.8706,98.8312,101.318,103.726,105.447,107.169,111.030,111.875,114.320,116.227,118.791]
for lam in (3,4,6,8):
    beta,L=make_beta(lam)
    ctx.prec=192; Lq,b,d,a=sequences(lam,40,192)
    # validation on the lattice
    err=max(abs(beta(2*math.pi*n/L)-float(d[n].mid())) for n in range(0,25))
    # full lobe list on [0,120]
    dt=0.005; ts=[i*dt for i in range(int(120/dt)+1)]; v=[beta(t) for t in ts]
    lobes=[];cur=None
    for t,x in zip(ts,v):
        if x<0 and cur is None: cur=t
        if x>=0 and cur is not None: lobes.append((cur,t)); cur=None
    if cur is not None: lobes.append((cur,120.0))
    pos=[t for t,x in zip(ts,v) if x>=0]
    print(f"\nlambda={lam}  L={L:.4f}  2pi/L={2*math.pi/L:.3f}   |beta(t_n)-d_n| max = {err:.1e}   beta(0)={v[0]:+.4f}")
    print("  lobes (start,end,width,width*L, depth, nearest zero, dist):")
    for a_,b_ in lobes:
        seg=[x for t,x in zip(ts,v) if a_<=t<=b_]; depth=min(seg); mid=(a_+b_)/2
        z=min(zeros,key=lambda z:abs(z-mid))
        print(f"    [{a_:7.3f},{b_:7.3f}]  w={b_-a_:5.3f}  wL={(b_-a_)*L:5.2f}  depth={depth:+7.3f}  z={z:7.3f} d={abs(z-mid):6.2f}")
    print(f"  negative measure (2-sided) on [-120,120]: {2*sum(b_-a_ for a_,b_ in lobes):.3f};  KMS count (L/2pi)*|neg| = {L/(2*math.pi)*2*sum(b_-a_ for a_,b_ in lobes):.2f};  last lobe ends at t={lobes[-1][1]:.2f}")
