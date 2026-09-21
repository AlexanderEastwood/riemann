"""Replay the finite lambda8 generalized-margin bracket; no complete-tail claim."""
from window_scaling_probe import *
ctx.prec=4096
path=BASE/'window_scaling_l8_metric_witness_b4096.json'
w=json.loads(path.read_text())
read=lambda name:arb_mat([[arb(t) for t in row] for row in w[name]])
K=read('K_normalized');S=read('Schur_normalized');z=read('probe');n=K.nrows();delta=arb(w['delta'])
assert ldl(K)[0]['status']=='PASS'
assert all(abs(K[i,j]-int(i==j))<arb('1e-20') for i in range(n) for j in range(n))
A=sym(S-delta*K);V=congruence(A);assert all(V[i,i]>0 for i in range(n))
gate=ldl(sym(V.transpose()*A*V))[0];assert gate['status']=='PASS'
gate['method']='Verified congruence before LDL; avoids interval elimination wrapping after decimal serialization.'
den=(z.transpose()*K*z)[0,0];assert den>0
rayleigh=(z.transpose()*S*z)[0,0]/den
assert rayleigh>0 and rayleigh<arb('5.755e-101')
assert delta>arb('5.697e-101')
# Certified norm upper; selecting a row maximum by binary64 midpoint is unsafe.
kmax=arb(1)+n*arb('1e-20')
I=arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
Sinv=S.solve(I,algorithm='precond');trace=sum((Sinv[i,i] for i in range(n)),arb(0));assert trace>0
trace_lower=1/(trace*kmax)
r={'status':'PASS_FINITE_MARGIN_BRACKET','lambda':8,'retained_cut':256,'test_cut':384,'head_dimension':65,'bits':4096,'lower_decimal':'5.697e-101','upper_decimal':'5.755e-101','delta':delta.str(80),'lower_gate':gate,'Rayleigh_upper':rayleigh.upper().str(80),'auxiliary_trace_lower':trace_lower.lower().str(80),'witness_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'Positive finite generalized margin only; all modes beyond384 absent. This is not a bound for the complete residual correction.'}
(BASE/'window_scaling_l8_margin_bracket_b4096.json').write_text(json.dumps(r,indent=2)+'\n')
p=BASE/'window_scaling_l8_even_r256_o384_b4096.json';q=json.loads(p.read_text());q['finite_trace_inverse_margin_lower']=r['auxiliary_trace_lower'];q['finite_relative_margin_bracket']={'lower':r['lower_decimal'],'upper':r['upper_decimal'],'certificate':'window_scaling_l8_margin_bracket_b4096.json'};q['double_precision_spectrum_limitation']='Values of theta within1e-14 of0 or1 are unresolved binary64 diagnostics; do not use their signs or derive a gap from1-theta. The certified bracket is separate.';q['worst_direction_headroom_FINITE']=None;q['worst_direction_headroom_precision_note']='1+O(1e-101), unresolved in binary64';p.write_text(json.dumps(q,indent=2)+'\n')
print(json.dumps(r,indent=2))
