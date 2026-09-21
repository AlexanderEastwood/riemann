"""Prime-free control: same window matrix with the prime sum removed.
If lmin collapses at the same rate, the collapse is archimedean (Landau-Widom)."""
import sys, importlib.util, time
sys.path.insert(0,'evidence/v124/g2_schur_cancellation')  # run from repo root
from cert import tomp
import mpmath as mp
from flint import ctx
spec=importlib.util.spec_from_file_location('ag_np','/private/tmp/claude-501/-Users-alex-riemann/b264d4b5-8b73-4067-8964-f1b34048a6fe/scratchpad/circle/noprime/assembly_general.py')
ag=importlib.util.module_from_spec(spec); spec.loader.exec_module(ag)
ag.pairs=lambda lam: []          # remove every prime power; cache dir is the noprime/ copy
import assembly_general as agp   # the prime version, cached in margin/
print("%-4s %-5s %-4s %-14s %-14s %-8s"%("lam","par","N","lmin PRIMES","lmin NOPRIME","secs"))
for lam,bits,dps in ((3,768,260),(4,768,260),(5,2048,600),(6,2048,600),(8,2048,600)):
    for par in ('even','odd'):
        t=time.time(); ctx.prec=bits; N=64
        rows=list(range(0 if par=='even' else 1,N+1))
        L,b,d,a=agp.sequences(lam,N+8,bits);  Mp=agp.block(rows,rows,par,b,d)
        L2,b2,d2,a2=ag.sequences(lam,N+8,bits); Mn=ag.block(rows,rows,par,b2,d2)
        mp.mp.dps=dps
        lp=min(mp.eigsy(tomp(Mp,dps),eigvals_only=True)); ln=min(mp.eigsy(tomp(Mn,dps),eigvals_only=True))
        mp.mp.dps=8
        print("%-4d %-5s %-4d %-14s %-14s %-8.0f"%(lam,par,N,mp.nstr(lp,5),mp.nstr(ln,5),time.time()-t),flush=True)
