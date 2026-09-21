"""Convention check for the primitive-tail proof, not proof evidence for RH.

The compact even test source h(x)=x^2-(5/3)x^4, |x|<=1, has h(0)=0,
integral h=0 and a nonzero endpoint. Faulhaber sums and a Hurwitz-zeta
antiderivative evaluate the Riemann sum and its logarithmic primitive.
The derivative comparison is numerical and deliberately avoids cut points.
"""
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 70

def powers(n):
    return n*(n+1)*(2*n+1)/6, n*(n+1)*(2*n+1)*(3*n*n+3*n-1)/30

def eh(u):
    n = mp.floor(1/u)
    s2,s4 = powers(n)
    return mp.sqrt(u)*(u*u*s2-mp.mpf(5)/3*u**4*s4)

def primitive(u):
    n = mp.floor(1/u)
    s2,s4 = powers(n)
    return (mp.mpf(2)/5*u**mp.mpf('2.5')*s2
            -mp.mpf(10)/27*u**mp.mpf('4.5')*s4
            +mp.mpf(4)/135*mp.zeta(mp.mpf('.5'),n+1))

def main():
    rows=[]
    worst=mp.mpf(0)
    for n in (10,100,1000,10000):
        for theta in ('0.2','0.5','0.8'):
            u=1/(n+mp.mpf(theta))
            k=eh(u)
            p=primitive(u)
            error=abs(mp.diff(lambda x:primitive(mp.exp(x)),mp.log(u))-k)
            worst=max(worst,error)
            rows.append({'n':n,'fractional_part':theta,
                         'u':mp.nstr(u,20),
                         'E_h_over_sqrt_u':mp.nstr(k/mp.sqrt(u),20),
                         'primitive_over_u_3_2':mp.nstr(p/u**mp.mpf('1.5'),20),
                         'derivative_absolute_error':mp.nstr(error,6)})
    assert worst<mp.mpf('1e-50')
    result={'scope':'70-digit toy-source convention checks only; no certified numerical bounds and no RH inference.',
            'source':'h(x)=x^2-(5/3)x^4 on [-1,1], zero outside',
            'max_derivative_absolute_error':mp.nstr(worst,10),'rows':rows}
    Path(__file__).with_name('bv_radical_passage_checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
