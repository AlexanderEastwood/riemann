"""Certified generalized margin and diagnostics for the complete even certificate."""
from window_scaling_probe import *

def run(bits=896):
 ctx.prec=bits;p=BASE/f'simultaneous_even_M4096_s16_normalized_ingredients_b{bits}.json';data=json.loads(p.read_text())
 witness=BASE/'simultaneous_even_M4096_s16_normalized_witness.json.gz';assert data['trial_witness_sha256']==hashlib.sha256(witness.read_bytes()).hexdigest()
 m={k:arb_mat([[arb(t) for t in row] for row in v]) for k,v in data['matrices'].items()};mu=arb(data['mu']);rho=arb(data['rho']);tau=arb(1)/10
 U=m['V']+m['E']+((1+tau)*m['HGram']+(1+1/tau)*rho*m['E'])/mu
 assert ldl(sym(m['K']-U))[0]['status']=='PASS'
 margin=arb(62629)/100000;gate=ldl(sym((1-margin)*m['K']-U))[0];assert gate['status']=='PASS'
 V=m['head'];vfile=json.loads((OLD/'structured_ceiling_counterwitness.json').read_text());v=arb_mat([[arb(n)/arb(2)**vfile['denominator_exponent']] for n in vfile['numerators']]);alpha=V.solve(v)
 headroom=(alpha.transpose()*m['K']*alpha)[0,0]/(alpha.transpose()*U*alpha)[0,0]
 Knum=asfloat(m['K']);Unum=asfloat(U);eK=np.linalg.eigvalsh(Knum);eU=np.linalg.eigvalsh(Unum);eLow=np.linalg.eigvalsh(Knum-Unum);C=np.linalg.cholesky(Knum);ci=np.linalg.inv(C);theta=np.linalg.eigvalsh(ci@Unum@ci.T)
 result={'certified_dimensionless_margin_lower':'62629/100000','margin_gate':gate,'selected_tau':'1/10','status':'PASS_COMPLETE_EVEN_RELATIVE_MARGIN','bits':bits,'head_dimension':17,'proposal_support':4096,'verification_cutoff':65536,'saved_v124_physical_head_direction_headroom':headroom.str(80),'trial_witness_sha256':data['trial_witness_sha256'],'diagnostics':{'generalized_margin':1-float(theta[-1]),'norm_U_over_min_eigenvalue_K':float(max(abs(eU))/eK[0]),'min_eigenvalue_lower_over_min_eigenvalue_K':float(eLow[0]/eK[0]),'log10_condition_V':lognorm(V)+lognorm(V.inv()),'per_direction_relative_corrections':[float(x) for x in theta]},'scope':'Relative COMPLETE correction bound for this matrix of trials at lambda4 only. Not an ordinary eigenvalue gap or growing-window estimate. Numbers under diagnostics are floating evaluations, distinct from the exact rational interval-certified margin.'}
 (BASE/f'complete_even_relative_margin_b{bits}.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run(int(sys.argv[1]) if len(sys.argv)>1 else 896)
