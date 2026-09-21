"""Complete old-metric complement bound for an exact frozen dyadic direction.
All matrices are outward-certified complete residual ingredients, not cut tails.
"""
from simultaneous_trial import *

def run(bits=768):
 ctx.prec=bits
 stem='simultaneous_odd_M4096_s16_normalized'
 raw=(BASE/(stem+'_witness.json.gz')).read_bytes();oldw=json.loads(gzip.decompress(raw))
 inp=BASE/(stem+'_ingredients_b768.json');data=json.loads(inp.read_text())
 assert data['trial_witness_sha256']==hashlib.sha256(raw).hexdigest()
 assert data['parity']=='odd' and data['M']==4096 and data['J']==65536
 dwraw=(BASE/'simultaneous_odd_M4096_s32_normalized_witness.json.gz').read_bytes();dw=json.loads(gzip.decompress(dwraw))
 assert dw['parent_witness_sha256']==data['trial_witness_sha256']
 assert dw['base_columns']==oldw['base_columns']
 m={k:arb_mat([[arb(t) for t in row] for row in mat]) for k,mat in data['matrices'].items()}
 K=m['K'];n=K.nrows();assert n==16
 kg=ldl(K)[0];assert kg['status']=='PASS'
 tau=arb(1)/20;sigma=arb(1)/1000;mu=arb(data['mu']);rho=arb(data['rho'])
 U=m['V']+m['E']+((1+tau)*m['HGram']+(1+1/tau)*rho*m['E'])/mu
 v=arb_mat([[arb(nn)*arb(2)**ee] for nn,ee in dw['direction_dyadics']]);assert all(t.is_exact() for row in v.tolist() for t in row)
 den=(v.transpose()*K*v)[0,0];assert den>0
 skip=max(range(n),key=lambda i:float(abs(v[i,0]).mid()));assert not v[skip,0].contains(0)
 # P encloses the EXACT K-dependent projection; it is never frozen at midpoints.
 I=arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
 P=I-v*(v.transpose()*K)/den
 Z=arb_mat([[P[i,j] for j in range(n) if j!=skip] for i in range(n)])
 gate=ldl(sym(Z.transpose()*(sigma*K-U)*Z))[0];assert gate['status']=='PASS',gate
 bad=(v.transpose()*(K-U)*v)[0,0]/den;assert bad<0
 result={'status':'PASS_COMPLETE_COMPLEMENT','bits':bits,'ingredient_bits':768,'lambda':4,'parity':'odd','head_dimension':16,'complement_dimension':15,'sigma':'1/1000','tau':'1/20','K_gate':kg,'complement_gate':gate,'projection_omitted_column':skip,'direction_old_energy':den.str(90),'old_direction_lower_interval':bad.str(90),'trial_witness_sha256':data['trial_witness_sha256'],'direction_witness_sha256':hashlib.sha256(dwraw).hexdigest(),'ingredient_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),'scope':'Complete exact inverse correction is at most sigma times OLD K on its exact K-orthogonal complement. The remaining direction is not certified positive.'}
 (BASE/f'direction_complement_report_b{bits}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 768)
