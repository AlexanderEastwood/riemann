"""NS-14: real zeros of the windowed ground transform xi-hat_lambda(z) vs zeta ordinates.
Ground vector by inverse iteration on the N=256 even compression (dps 120)."""
import sys, math, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation')  # run from repo root
from flint import arb, arb_mat, ctx
from assembly_general import sequences, block
from cert import tomp
import mpmath as mp
gam=[14.134725,21.022040,25.010858,30.424876,32.935062,37.586178,40.918719,43.327073,48.005151,49.773832,52.970321,56.446248,59.347044,60.831779,65.112544,67.079811,69.546402,72.067158,75.704691,77.144840,79.337375,82.910381,84.735493,87.425275,88.809111,92.491899,94.651344,95.870634,98.831194,101.317851,103.725538,105.446623,107.168611,111.029536,111.874659,114.320221,116.226680,118.790783]
def ground(lam,N,bits=768,dps=120):
    ctx.prec=bits; L,b,d,a=sequences(lam,N+8,bits); rows=list(range(0,N+1))
    W=tomp(block(rows,rows,'even',b,d),dps); mp.mp.dps=dps
    x=mp.matrix([mp.mpf(1)/(k+1) for k in range(N+1)])
    for _ in range(4):
        x=mp.lu_solve(W,x); x=x/mp.norm(x)
    ray=(x.T*W*x)[0]
    return float(L.mid()),x,ray
def xhat(v,L,z,dps=40):
    mp.mp.dps=dps; z=mp.mpf(z); L=mp.mpf(L); s=v[0]/mp.sqrt(L)*2*mp.sin(z*L/2)/z
    c=mp.sqrt(2/L)
    for n in range(1,len(v)):
        if abs(v[n])<mp.mpf(10)**(-60): break
        w=2*mp.pi*n/L
        s+=c*v[n]*(mp.sin((w-z)*L/2)/(w-z)+mp.sin((w+z)*L/2)/(w+z))
    return s
for lam in (3,4):
    t=time.time(); L,v,ray=ground(lam,256)
    mp.mp.dps=12
    print(f"\nlambda={lam}  L={L:.4f}  Rayleigh={mp.nstr(ray,6)}  |v0|,|v1|,|v2|,|v3| = {[mp.nstr(abs(v[k]),4) for k in range(4)]}   [{time.time()-t:.0f}s]")
    dz=0.01; zs=[0.05+i*dz for i in range(int(120/dz))]; vals=[xhat(v,L,z) for z in zs]
    roots=[]
    for i in range(len(zs)-1):
        if vals[i]==0 or (vals[i]>0)!=(vals[i+1]>0):
            try: r=mp.findroot(lambda z:xhat(v,L,z),(zs[i],zs[i+1]),solver='bisect',tol=1e-20); roots.append(float(r))
            except Exception: roots.append((zs[i]+zs[i+1])/2)
    print(f"  real zeros of xi-hat_{lam} in (0,120]: {len(roots)}   (zeta ordinates below 120: {len(gam)})")
    print("  first zeros vs nearest zeta ordinate:")
    for r in roots[:14]:
        g=min(gam,key=lambda g:abs(g-r)); print(f"    z={r:9.4f}   nearest gamma={g:9.4f}   diff={r-g:+8.4f}")
    sp=[roots[i+1]-roots[i] for i in range(len(roots)-1)]
    print(f"  mean spacing of xi-hat zeros: {sum(sp)/len(sp):.4f}   vs  2pi/L = {2*math.pi/L:.4f}   vs mean zeta spacing below 120: {(gam[-1]-gam[0])/(len(gam)-1):.4f}")
