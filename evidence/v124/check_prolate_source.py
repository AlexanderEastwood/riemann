"""High-precision Legendre-Galerkin illustrations, not interval certificates.

Even angular PSWFs solve -((1-x*x)y')' + c*c*x*x*y = theta*y
on [-1,1], with L2 norm one. The indices 0 and 4 are even-block
eigenvectors 0 and 2. No zeta zeros or RH assumptions are used.
"""
import json
from pathlib import Path
import mpmath as mp


def modes(c, size, digits=85):
    mp.mp.dps = digits
    c = mp.mpf(c)
    a = lambda j: (j+1)/mp.sqrt((2*j+1)*(2*j+3)) if j >= 0 else mp.mpf(0)
    mat = mp.matrix(size)
    for k in range(size):
        ell = 2*k
        mat[k,k] = ell*(ell+1)+c*c*(a(ell)**2+a(ell-1)**2)
        if k+1 < size:
            mat[k,k+1] = mat[k+1,k] = c*c*a(ell)*a(ell+1)
    eigenvalues, vectors = mp.eigsy(mat)
    lam = mp.sqrt(c/(2*mp.pi))
    result = {}
    for n in (0,4):
        col = n//2
        center = mp.fsum(vectors[k,col]*mp.sqrt(mp.mpf(4*k+1)/2)
                         *(-1)**k*mp.binomial(2*k,k)/4**k for k in range(size))
        sign = mp.sign(center)
        endpoint = sign*mp.fsum(vectors[k,col]*mp.sqrt(mp.mpf(4*k+1)/2) for k in range(size))
        center *= sign
        integral = sign*mp.sqrt(2)*vectors[0,col]
        chi = lam*integral/center
        result[n] = {"center": center/mp.sqrt(lam), "endpoint": endpoint,
                     "chi": chi, "loss": 1-chi**2}
    a0 = -result[4]["chi"]*result[4]["center"]
    a4 = result[0]["chi"]*result[0]["center"]
    bp = a0*result[0]["endpoint"]+a4*result[4]["endpoint"]
    at_zero = (result[0]["chi"]-result[4]["chi"])*result[0]["center"]*result[4]["center"]
    rows = {"c": int(c), "size": size, "digits": digits,
        "endpoint_ratio_divided_by_c_squared": abs(result[4]["endpoint"]/result[0]["endpoint"])/c**2,
        "endpoint_noncancellation_ratio": (abs(a0*result[0]["endpoint"])+abs(a4*result[4]["endpoint"]))/abs(bp),
        "value_zero_to_endpoint_ratio": abs(at_zero/bp),
        "normalized_repair_scale": abs(at_zero/bp)/(c**mp.mpf('1.75')*mp.exp(-c))}
    for n in (0,4):
        loss = result[n]["loss"]
        fuchs = 4*mp.sqrt(mp.pi)*8**n/mp.factorial(n)*c**(n+mp.mpf('.5'))*mp.exp(-2*c)
        rows[f"loss_{n}_over_fuchs"] = loss/fuchs
        rows[f"endpoint_squared_{n}_over_c_loss"] = result[n]["endpoint"]**2/(c*loss)
    return {k:(mp.nstr(v,24) if isinstance(v,mp.mpf) else v) for k,v in rows.items()}


def main():
    rows=[]
    for c in (10,20,30,40):
        row=modes(c,50)
        rows.append(row)
        print(json.dumps(row),flush=True)
    convergence=modes(40,65,105)
    result={"scope":"Arbitrary-precision finite Legendre-Galerkin approximations only; no certified truncation or roundoff bound and no RH inference.",
            "rows":rows,"larger_dimension_and_precision_check":convergence}
    Path(__file__).with_name("prolate_source_checks.json").write_text(json.dumps(result,indent=2)+"\n")
    print('Completed larger-dimension comparison:',json.dumps(convergence),flush=True)


if __name__ == '__main__':
    main()
