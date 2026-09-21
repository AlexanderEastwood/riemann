"""Accurate lambda=3 even ground vector: N=120, 1024-bit assembly, eigsy at 220 digits. Saved as JSON strings."""
import sys, json, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation'); sys.path.insert(0,'evidence/diag_true_symbol')  # run from repo root
import mpmath as mp
from flint import ctx
from assembly_general import sequences, block
from cert import tomp
lam,N,bits,dps=3,120,1024,220
ctx.prec=bits; L,b,d,a=sequences(lam,N+8,bits); rows=list(range(N+1))
mp.mp.dps=dps; W=tomp(block(rows,rows,'even',b,d),dps)
t=time.time(); E,Q=mp.eigsy(W); i=min(range(len(E)),key=lambda k:E[k]); v=Q[:,i]
print(f"lambda={lam} N={N}: eps_N={mp.nstr(E[i],12)}  second even={mp.nstr(sorted(E)[1],6)}  [{time.time()-t:.0f}s]")
json.dump({"lambda":lam,"N":N,"bits":bits,"dps":dps,"L":str(L.mid()),"eps":mp.nstr(E[i],60),"v":[mp.nstr(v[k],80) for k in range(N+1)]},open('ground_l3_N120.json','w'))
print("saved ground_l3_N120.json; |v0..v5| =",[mp.nstr(abs(v[k]),4) for k in range(6)], " |v_60|,|v_120| =",mp.nstr(abs(v[60]),3),mp.nstr(abs(v[120]),3))
