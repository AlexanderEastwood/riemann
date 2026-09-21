"""Physical one-dimensional head audit by exact finite shorting."""
from window_resolution_probe import *
def run(path):
 raw=json.loads(Path(path).read_text());ctx.prec=raw['metadata']['bits'];forms={int(k):arb_mat([[arb(t) for t in row] for row in v]) for k,v in raw['forms'].items()};cols={};energy={};head=raw['metadata']['head'];out={'head_input':head,'metadata':raw['metadata'],'constant_head':{},'comparisons':[],'scope':'Schur complements retaining only physical mode0; every other mode through each cutoff eliminated. Finite only.'}
 for M,S in forms.items():
  n=S.nrows();gate_scaled(S);rhs=arb_mat([[int(i==0)] for i in range(n)]);z=S.solve(rhs,algorithm='precond');assert z[0,0]>0
  cols[M]=z;energy[M]=1/z[0,0];out['constant_head'][str(M)]={'energy':energy[M].str(100),'log10_energy':(energy[M].log()/arb(10).log()).str(80)}
 for left,right in zip(sorted(forms),sorted(forms)[1:]):
  m=energy[right]/energy[left];assert m>0 and m<1
  out['comparisons'].append({'left':left,'right':right,'constant_head_margin':m.str(100),'normalizing_congruence_condition':'1 (scalar)','relative_infinity_scope':'No complete-tail claim.'})
 p=Path(path).with_name(Path(path).stem+'_constant_head.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':run(sys.argv[1])
