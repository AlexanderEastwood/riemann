"""One finite residual repair of a proposed bad direction; full verification separate."""
from window_scaling_probe import *
def propose(extra=16,bits=768,cbits=512,M=4096,J=65536):
 start=time.time();parity='odd';oldstem=f'simultaneous_odd_M{M}_s16_normalized';raw=(BASE/(oldstem+'_witness.json.gz')).read_bytes();w=json.loads(gzip.decompress(raw));data=json.loads((BASE/(oldstem+f'_ingredients_b{bits}.json')).read_text());assert hashlib.sha256(raw).hexdigest()==data['trial_witness_sha256']
 mats={k:arb_mat([[arb(t) for t in row] for row in v]) for k,v in data['matrices'].items()};mu=arb(data['mu']);rho=arb(data['rho']);tau=arb(1)/20
 U=mats['V']+mats['E']+((1+tau)*mats['HGram']+(1+1/tau)*rho*mats['E'])/mu
 Knum=asfloat(mats['K']);Unum=asfloat(U);Cnum=np.linalg.cholesky(Knum);cinv=np.linalg.inv(Cnum);vals,vecs=np.linalg.eigh(cinv@Unum@cinv.T);vnum=np.linalg.solve(Cnum.T,vecs[:,-1]);v=[arb(float(x)) for x in vnum]
 L,b,d,a,N,Mi,head,X,Z,C,mu,g,xhash,ihash=init('odd',J,bits);assert xhash==w['outer_sha256'] and ihash==w['inner_sha256'];di=N-16;nm=Mi-N
 ctx.prec=cbits;ell=[(x/dot(v,v)).mid() for x in v]
 fs=[];oldx=[]
 for j in range(16):
  f=[arb(n)*arb(2)**e for n,e in w['base_columns'][j]]+[arb(0)]*(M-256)
  x=[arb(n)*arb(2)**e for n,e in w['dyadic_columns'][j]];oldx.append(x)
  for i,t in enumerate(x):f[i+16]-=t
  fs.append(f)
 f=[sum((fs[j][i]*v[j] for j in range(16)),arb(0)).mid() for i in range(M)]
 gs=[g(n) for n in range(N+1,M+1)];Ct=C.transpose();Zt=Z.transpose();shift=arb(1)/10**8
 def op(v):return action(v,17,'odd',b,d,a,arb(0))
 def pre(v):
  h=v[:di];k=v[di:];z=[k[i]/gs[i] for i in range(len(k))];az=action([arb(0)]*di+z,17,'odd',b,d,a,shift)
  ztk=mv(Zt,k[:nm]);ztaz=mv(Zt,az[di:di+nm]);hh=[h[i]-ztk[i]-az[i]+ztaz[i] for i in range(di)]
  u=[x/mu for x in mv(Ct,mv(C,hh))];zu=mv(Z,u);graph=u+[-x for x in zu]+[arb(0)]*(M-Mi);rg=action(graph,17,'odd',b,d,a,shift)[di:]
  far=[z[i]-rg[i]/gs[i]-(zu[i] if i<nm else 0) for i in range(len(z))]
  return [t.mid() for t in u+far]
 rhs=[t.mid() for t in f_action(f,M,'odd',b,d,a)[16:]];x=[arb(0)]*len(rhs);res=rhs.copy();z=pre(res);p=z.copy();rz=dot(res,z);hist=[]
 for j in range(extra):
  ap=op(p);den=dot(p,ap);assert den>0;alpha=(rz/den).mid();x=[(xx+alpha*pp).mid() for xx,pp in zip(x,p)];res=[(rr-alpha*aa).mid() for rr,aa in zip(res,ap)]
  z=pre(res);new=dot(res,z);assert new>0;beta=(new/rz).mid();p=[(zz+beta*pp).mid() for zz,pp in zip(z,p)];rz=new;hist.append(dot(res,res).str(40));print('rank-one step',j+1,hist[-1],round(time.time()-start,1),flush=True)
 newcols=[]
 for j in range(16):
  xx=[(oldx[j][i]+x[i]*ell[j]).mid() for i in range(len(x))];newcols.append([[str(t.man_exp()[0]),int(t.man_exp()[1])] for t in xx])
 w.update({'steps':16+extra,'proposal_kind':'16 independent initial CG steps per column, then one rank-one repair with extra steps; final rounding may add tiny full-rank perturbations','rank_one_extra_steps':extra,'parent_witness_sha256':hashlib.sha256(raw).hexdigest(),'direction_dyadics':[[str(t.man_exp()[0]),int(t.man_exp()[1])] for t in v],'dual_dyadics':[[str(t.man_exp()[0]),int(t.man_exp()[1])] for t in ell],'dyadic_columns':newcols,'rank_one_recursive_residual2':hist,'candidate_generalized_eigenvalues':vals.tolist(),'candidate_bits':cbits})
 stem=f'simultaneous_odd_M{M}_s{16+extra}_normalized';(BASE/(stem+'_witness.json.gz')).write_bytes(gzip.compress(json.dumps(w).encode()));print('FROZEN',stem,flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--extra',type=int,default=16);s=p.parse_args();propose(s.extra)
