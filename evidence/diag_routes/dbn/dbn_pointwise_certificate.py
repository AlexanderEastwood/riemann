"""
Pointwise non-vanishing certificate for H_t(x+iy), after Polymath15
(arXiv:1904.12438), Theorem 1.3 ("Effective Riemann-Siegel approximation")
and Corollary 1.4 ("Criterion for non-vanishing"):

    H_t(x+iy)/B_t(x+iy) = f_t(x+iy) + O_<=(e_A + e_B + e_{C,0})
    if |f_t(x+iy)| > e_A + e_B + e_{C,0}   then   H_t(x+iy) != 0,

valid in the region 0 < t <= 1/2, 0 <= y <= 1, x >= 200.  Everything is
evaluated in Arb ball arithmetic through python-flint; the final inequality is
accepted only when Arb can certify it (lower bound of |f_t| strictly above the
upper bound of the error).  Replayed at two precisions.

Formulas transcribed from Writeup/intro.tex of km-git-acc/dbn_upper_bound.
"""
import math
import sys
import time

from flint import arb, acb, ctx


def alpha(s: acb) -> acb:
    # alpha(s) = 1/(2s) + 1/(s-1) + (1/2) Log(s/(2 pi))
    return 1 / (2 * s) + 1 / (s - 1) + (s / (2 * arb.pi())).log() / 2


def log_M0(s: acb) -> acb:
    # log M_0(s) = Log s + Log(s-1) - (s/2) log pi + log(sqrt(2 pi)/16)
    #              + (s/2 - 1/2) Log(s/2) - s/2
    return (
        s.log()
        + (s - 1).log()
        - s / 2 * arb.pi().log()
        + ((2 * arb.pi()).sqrt() / 16).log()
        + (s / 2 - arb(1) / 2) * (s / 2).log()
        - s / 2
    )


def log_Mt(s: acb, t: arb) -> acb:
    return t / 4 * alpha(s) ** 2 + log_M0(s)


def certificate(x_str: str, y_str: str, t_str: str, dps: int) -> dict:
    ctx.dps = dps
    x, y, t = arb(x_str), arb(y_str), arb(t_str)
    pi = arb.pi()

    # N = floor( sqrt(x/(4 pi) + t/16) ), certified by comparing balls
    q = (x / (4 * pi) + t / 16).sqrt()
    N = int(math.floor(float(q.mid())))
    if not (arb(N) <= q and q < arb(N + 1)):
        raise RuntimeError("could not certify N")

    s1 = acb((1 - y) / 2, x / 2)    # (1 - y + i x)/2
    s2 = acb((1 + y) / 2, -x / 2)   # (1 + y - i x)/2
    s3 = acb((1 + y) / 2, x / 2)    # (1 + y + i x)/2

    gamma = (log_Mt(s1, t) - log_Mt(s2, t)).exp()          # M_t(s1)/M_t(s2)
    s_star = s2 + t / 2 * alpha(s2)
    kappa = t / 2 * (alpha(s1) - alpha(s3))
    s_star_c = s_star.conjugate()
    re_s_star = s_star.real
    abs_gamma = abs(gamma)
    abs_kappa = abs(kappa)
    N_pow_kappa = (abs_kappa * arb(N).log()).exp()

    f = acb(0)
    eAB = arb(0)
    log_x4pi = (x / (4 * pi)).log()
    t0 = time.time()
    for n in range(1, N + 1):
        ln = arb(n).log()
        b = (t / 4 * ln * ln).exp()                          # b_n^t
        term1 = b * (-s_star * ln).exp()                     # b_n^t / n^{s_*}
        term2 = b * ((y - s_star_c - kappa) * ln).exp()      # n^y b_n^t / n^{conj(s_*)+kappa}
        f += term1 + gamma * term2
        # e_A + e_B summand
        n_y = (y * ln).exp()
        base = b * (-re_s_star * ln).exp()
        L = log_x4pi - 2 * ln                                # log( x / (4 pi n^2) )
        expo = ((t * t / 16) * L * L + arb("0.626")) / (x - arb("6.66"))
        eAB += (1 + abs_gamma * N_pow_kappa * n_y) * base * (expo.exp() - 1)
    loop_s = time.time() - t0

    # e_{C,0} bound
    three_y = (y * arb(3).log()).exp()
    eC0 = (
        (-(1 + y) / 4 * log_x4pi).exp()
        * (
            -t / 16 * log_x4pi * log_x4pi
            + arb("1.24") * (three_y + 1 / three_y) / (arb(N) - arb("0.125"))
            + (3 * abs(acb(log_x4pi, pi / 2)) + arb("10.44")) / (x - arb("8.52"))
        ).exp()
    )
    err = eAB + eC0
    absf = abs(f)
    certified = bool(absf > err)   # True only if Arb can prove it
    return dict(
        dps=dps, N=N, f=f, absf=absf, eAB=eAB, eC0=eC0, err=err,
        certified=certified, loop_s=loop_s,
    )


def main() -> None:
    pts = [("60000083951.5", "0.2", "0.2"), ("60000083951.5", "1", "0.2"),
           ("1000", "0.4", "0.3")]
    if len(sys.argv) == 4:
        pts = [tuple(sys.argv[1:4])]
    for (xs, ys, ts) in pts:
        print(f"\n=== x={xs}  y={ys}  t={ts} ===")
        for dps in (40, 60):
            r = certificate(xs, ys, ts, dps)
            print(f"[dps={dps}] N={r['N']}  loop {r['loop_s']:.2f}s")
            print("  f_t(x+iy)      =", r["f"].str(22, radius=True))
            print("  |f_t|          =", r["absf"].str(22, radius=True))
            print("  e_A+e_B (bound)=", r["eAB"].str(6, radius=True))
            print("  e_C0    (bound)=", r["eC0"].str(6, radius=True))
            print("  ball radii: |f_t| rad =", r["absf"].rad().str(3), " err rad =", r["err"].rad().str(3), " prec bits =", ctx.prec)
            print("  certified margin lower(|f_t|) - upper(err) =", (r["absf"].lower() - r["err"].upper()).str(8))
            print("  |f_t| > e_A+e_B+e_C0 certified by Arb:", r["certified"])
            if r["certified"]:
                print("  => H_t(x+iy) != 0 at this point (Cor. 1.4 of arXiv:1904.12438)")


if __name__ == "__main__":
    main()
