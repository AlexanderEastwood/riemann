"""Whole-head certificate with one joint remote Gram, retaining its cross block."""
from simultaneous_trial import *

def run(parity='even',M=4096,steps=16,bits=768,J=65536):
 begin=time.time();L,b,d,a,N,Mi,head,X,Z,C,mu,g,xhash,ihash=init(parity,J,bits);offset=0 if parity=='even' else 1;dh=len(head);di=N-16
 stem=f'simultaneous_{parity}_M{M}_s{steps}_normalized'
 w=json.loads(gzip.decompress((BASE/(stem+'_witness.json.gz')).read_bytes()));data=json.loads((BASE/(stem+f'_ingredients_b{bits}.json')).read_text())
 assert data['trial_witness_sha256']==hashlib.sha256((BASE/(stem+'_witness.json.gz')).read_bytes()).hexdigest()
 assert w['outer_sha256']==data['outer_sha256']==xhash and w['inner_sha256']==data['inner_sha256']==ihash
 assert data['J']==J and data['bits']==bits and data['M']==M
 mats={n:arb_mat([[arb(x) for x in row] for row in mat]) for n,mat in data['matrices'].items()};H=mats['H']
 G=arb_mat(M+1-offset,dh)
 for j,raw in enumerate(w['dyadic_columns']):
  for i,(n,e) in enumerate(w['base_columns'][j]):G[i,j]=arb(n)*arb(2)**e
  for i,(n,e) in enumerate(raw):G[17-offset+i,j]-=arb(n)*arb(2)**e
 Gi=arb_mat([[int(i==j) if i<di else -Z[i-di,j] for j in range(di)] for i in range(Mi-16)])*C.transpose()
 both=arb_mat(M+1-offset,di+dh)
 for i in range(Gi.nrows()):
  for j in range(di):both[17-offset+i,j]=Gi[i,j]
 for i in range(G.nrows()):
  for j in range(dh):both[i,di+j]=G[i,j]
 hh=arb(9)/16;pp=sum((arb(p).log()/arb(m).sqrt() for m,p in pairs(4)),arb(0));bs=(4*hh+pp+1+arb.pi()/4)/arb.pi()
 Gamma=remote(both,list(range(offset,M+1)),M,J,64,parity,b,bs)/g(J+1)
 YY=arb_mat([[Gamma[i,j] for j in range(di)] for i in range(di)]);YK=arb_mat([[Gamma[i,di+j] for j in range(dh)] for i in range(di)]);KK=arb_mat([[Gamma[di+i,di+j] for j in range(dh)] for i in range(dh)])
 rho=sum((YY[i,i] for i in range(di)),arb(0));assert rho<mu
 bbar=H-YK
 scalar=KK+bbar.transpose()*bbar/(mu-rho)
 low_scalar=sym(mats['K']-mats['V']-scalar);sg=ldl(low_scalar)[0]
 denom=arb_mat([[mu*int(i==j)-YY[i,j] for j in range(di)] for i in range(di)])
 invprod=denom.solve(bbar,algorithm='lu')
 correction=KK+bbar.transpose()*invprod;lower=sym(mats['K']-mats['V']-correction);gate,piv=ldl(lower)
 out={'status':'PASS_COMPLETE_HEAD' if gate['status']=='PASS' else 'INCONCLUSIVE_JOINT_BOUND','parity':parity,'M':M,'J':J,'steps':steps,'bits':bits,'rho_joint':rho.str(80),'scalar_gate':sg,'joint_gate':gate,'outer_sha256':xhash,'inner_sha256':ihash,'seconds':time.time()-begin,'scope':'One common Gram majorizes all remote inner and outer sources and their cross block. A failed lower bound is not a negative Weil vector.'}
 (BASE/(stem+f'_joint_report_b{bits}.json')).write_text(json.dumps(out,indent=2)+'\n')
 (BASE/(stem+f'_joint_lower_b{bits}.json')).write_text(json.dumps({'lower':dumpmat(lower),'scalar_lower':dumpmat(low_scalar),'rho':rho.str(220)})+'\n')
 print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--parity',default='even');p.add_argument('--M',type=int,default=4096);p.add_argument('--J',type=int,default=65536);p.add_argument('--steps',type=int,default=16);p.add_argument('--bits',type=int,default=768);run(**vars(p.parse_args()))
