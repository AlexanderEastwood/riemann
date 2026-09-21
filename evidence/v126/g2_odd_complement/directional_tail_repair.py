"""Frozen one-direction finite trials; complete residual verification is separate.
The old head and normalization remain exact. PCG is proposal-only.
"""
from simultaneous_trial import *

def stem(M,steps):return f'directional_odd_M{M}_s{steps}'
def propose(M=8192,steps=24,bits=768,cbits=512):
 begin=time.time();ctx.prec=bits
 raw=(BASE/'simultaneous_odd_M4096_s16_normalized_witness.json.gz').read_bytes();w=json.loads(gzip.decompress(raw))
 vw=json.loads(gzip.decompress((BASE/'simultaneous_odd_M4096_s32_normalized_witness.json.gz').read_bytes()))
 v=[arb(n)*arb(2)**e for n,e in vw['direction_dyadics']]
 L,b,d,a,N,Mi,head,X,Z,C,mu,g,xhash,ihash=init('odd',max(65536,M),bits);di=N-16;nm=Mi-N
 assert w['outer_sha256']==xhash and w['inner_sha256']==ihash
 ctx.prec=max(bits,2048)
 f=[arb(0)]*M
 for j in range(16):
  for i,(n,e) in enumerate(w['base_columns'][j]):f[i]+=arb(n)*arb(2)**e*v[j]
  for i,(n,e) in enumerate(w['dyadic_columns'][j]):f[i+16]-=arb(n)*arb(2)**e*v[j]
 assert all(t.is_exact() for t in f), 'increase precision for exact frozen combination'
 physical_head=f[:16]
 ctx.prec=cbits;gs=[g(n) for n in range(N+1,M+1)];Ct=C.transpose();Zt=Z.transpose();shift=arb(1)/10**8
 def op(v):return action(v,17,'odd',b,d,a,arb(0))
 def pre(v):
  h=v[:di];k=v[di:];z=[k[i]/gs[i] for i in range(len(k))];az=action([arb(0)]*di+z,17,'odd',b,d,a,shift)
  ztk=mv(Zt,k[:nm]);ztaz=mv(Zt,az[di:di+nm]);hh=[h[i]-ztk[i]-az[i]+ztaz[i] for i in range(di)]
  u=[x/mu for x in mv(Ct,mv(C,hh))];zu=mv(Z,u);graph=u+[-x for x in zu]+[arb(0)]*(M-Mi);rg=action(graph,17,'odd',b,d,a,shift)[di:]
  return [t.mid() for t in u+[z[i]-rg[i]/gs[i]-(zu[i] if i<nm else 0) for i in range(len(z))]]
 rhs=[t.mid() for t in f_action(f,M,'odd',b,d,a)[16:]];x=[arb(0)]*len(rhs);res=rhs.copy();z=pre(res);p=z.copy();rz=dot(res,z);hist=[]
 for j in range(steps):
  ap=op(p);den=dot(p,ap);assert den>0;alpha=(rz/den).mid();x=[(xx+alpha*pp).mid() for xx,pp in zip(x,p)];res=[(rr-alpha*aa).mid() for rr,aa in zip(res,ap)]
  z=pre(res);new=dot(res,z);assert new>0;beta=(new/rz).mid();p=[(zz+beta*pp).mid() for zz,pp in zip(z,p)];rz=new
  if j%4==3 or j==steps-1:hist.append({'step':j+1,'recursive_residual2':dot(res,res).str(40)});print(M,hist[-1],round(time.time()-begin,1),flush=True)
 out=physical_head+[(f[i+16]-x[i]).mid() for i in range(len(x))]
 witness={'M':M,'steps':steps,'parity':'odd','candidate_bits':cbits,'parent_witness_sha256':hashlib.sha256(raw).hexdigest(),'outer_sha256':xhash,'inner_sha256':ihash,'direction_dyadics':vw['direction_dyadics'],'dyadics':[[str(t.man_exp()[0]),int(t.man_exp()[1])] for t in out],'history':hist,'scope':'Finite proposal only; same exact physical head as old sixteen-column trial applied to frozen direction.'}
 (BASE/(stem(M,steps)+'_witness.json.gz')).write_bytes(gzip.compress(json.dumps(witness).encode()));print('FROZEN',M,flush=True)

def verify(M=8192,steps=24,bits=1024,J=65536):
 begin=time.time();L,b,d,a,N,Mi,head,X,Z,C,mu,g,xhash,ihash=init('odd',J,bits);di=N-16;nm=Mi-N
 assert J>max(M,Mi)
 raw=(BASE/(stem(M,steps)+'_witness.json.gz')).read_bytes();w=json.loads(gzip.decompress(raw));assert w['M']==M and w['steps']==steps and w['parity']=='odd' and w['outer_sha256']==xhash and w['inner_sha256']==ihash
 dwraw=(BASE/'simultaneous_odd_M4096_s32_normalized_witness.json.gz').read_bytes();dw=json.loads(gzip.decompress(dwraw))
 assert w['direction_dyadics']==dw['direction_dyadics']
 cg=json.loads((BASE/'direction_complement_report_b768.json').read_text());assert cg['status']=='PASS_COMPLETE_COMPLEMENT' and cg['direction_witness_sha256']==hashlib.sha256(dwraw).hexdigest()
 f=[arb(n)*arb(2)**e for n,e in w['dyadics']];v=arb_mat([[arb(n)*arb(2)**e] for n,e in w['direction_dyadics']]);assert len(f)==M and all(t.is_exact() for t in f)
 oldraw=(BASE/'simultaneous_odd_M4096_s16_normalized_witness.json.gz').read_bytes();old=json.loads(gzip.decompress(oldraw));assert hashlib.sha256(oldraw).hexdigest()==w['parent_witness_sha256']
 vh=arb_mat([[arb(n)*arb(2)**e for n,e in col[:16]] for col in old['base_columns']]).transpose()*v
 assert all(f[i]==vh[i,0] for i in range(16))
 data=json.loads((BASE/'simultaneous_odd_M4096_s16_normalized_ingredients_b768.json').read_text());assert data['trial_witness_sha256']==w['parent_witness_sha256'] and data['J']<=J
 Kold=arb_mat([[arb(t) for t in row] for row in data['matrices']['K']]);den=(v.transpose()*Kold*v)[0,0];assert den>0
 print('verified exact head',round(time.time()-begin,1),flush=True)
 wg=f_action(f,J,'odd',b,d,a);K=dot(f,wg[:M]);h=wg[16:N];k=wg[N:];gs=[g(n) for n in range(N+1,J+1)];z=[k[i]/gs[i] for i in range(len(k))]
 rows=[1,16,17,256,N,N+1,Mi,M];dense=block(rows,list(range(1,M+1)),'odd',b,d)*arb_mat([[t] for t in f]);assert all(dense[i,0].overlaps(wg[n-1]) for i,n in enumerate(rows))
 az=action([arb(0)]*di+z,17,'odd',b,d,a,arb(1)/10**8);ztk=mv(Z.transpose(),k[:nm]);ztaz=mv(Z.transpose(),az[di:di+nm]);bb=mv(C,[h[i]-ztk[i]-az[i]+ztaz[i] for i in range(di)]);H=dot(bb,bb);V=dot(k,z)
 hh=arb(9)/16;pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));bs=(4*hh+pp+1+arb.pi()/4)/arb.pi()
 print('verified finite rows',round(time.time()-begin,1),flush=True)
 E=remote(arb_mat([[t] for t in f]),list(range(1,M+1)),M,J,64,'odd',b,bs)[0,0]/g(J+1)
 # The archived upper for remote inner rows beyond65536 also bounds their subset beyondJ.
 rho=arb(data['rho']);assert data['inner_sha256']==ihash and arb(data['mu']).contains(mu)
 U=V+E+(H.sqrt()+(rho*E).sqrt())**2/mu
 s=(K-U)/den
 report={'M':M,'steps':steps,'bits':bits,'J':J,'trial_witness_sha256':hashlib.sha256(raw).hexdigest(),'parent_witness_sha256':w['parent_witness_sha256'],'rho_source_J':data['J'],'rho_upper':rho.str(90),'old_direction_denominator':den.str(90),'K':K.str(90),'finite_far_upper':V.str(90),'remote_outer_upper':E.str(90),'finite_mixed_squared':H.str(90),'complete_correction_upper':U.str(90),'s_lower_interval':s.str(90),'certified_s_rational':'429/1000' if s>arb(429)/1000 else None,'certified_full_head_margin_rational':'428/1000' if s>arb(429)/1000 else None,'status':'PASS_DIRECTION_VS_SIGMA' if s>arb(1)/1000 else 'INCONCLUSIVE_DIRECTION','seconds':time.time()-begin,'scope':'Complete inverse bound for this exact one-direction finite trial, including every row beyond J. Not a cofinal estimate.'}
 (BASE/(stem(M,steps)+f'_report_b{bits}_J{J}.json')).write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--mode',default='both');p.add_argument('--M',type=int,default=8192);p.add_argument('--steps',type=int,default=24);p.add_argument('--bits',type=int,default=1024);p.add_argument('--J',type=int,default=65536);s=p.parse_args()
 if s.mode in ['candidate','both']:propose(s.M,s.steps,s.bits)
 if s.mode in ['verify','both']:verify(s.M,s.steps,s.bits,s.J)
