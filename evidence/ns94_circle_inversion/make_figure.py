"""Draw an illustrative exact-coordinate control, not a zeta computation."""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def invert(z: complex, c: float, r: float) -> complex:
    return c+r*r/(z.conjugate()-c)


def main() -> None:
    fig, axes=plt.subplots(1,2,figsize=(9,4.7),layout='constrained')
    points=[complex(x,y) for x in [0.25,0.75] for y in [-1.0,1.0]]
    left,right=axes
    for ax in axes:
        ax.axhline(0,color='#bbb',lw=0.7)
        ax.axvline(.5,color='#929292',lw=1,linestyle='--')
        ax.set_aspect('equal')
        ax.spines[['top','right']].set_visible(False)
        ax.set_xlabel('Real coordinate')
        ax.set_ylabel('Imaginary coordinate')
    for c in [0.,1.]:
        left.add_patch(Circle((c,0),.5,fill=False,color='#b2b9bd',lw=1.5))
    left.scatter([z.real for z in points],[z.imag for z in points],color='#7a2856',s=40,zorder=3)
    left.set(xlim=(-.55,1.55),ylim=(-1.2,1.2),title='Four symmetric off-line points')
    for c,centre,col in [(0.,.25,'#176b93'),(1.,.75,'#ba5727')]:
        right.add_patch(Circle((centre,0),.25,fill=False,color=col,lw=2))
        images=[invert(z,c,.5) for z in points]
        right.scatter([z.real for z in images],[z.imag for z in images],color=col,s=35,zorder=3)
    right.set(xlim=(-.08,1.08),ylim=(-.38,.38),title='Two images: two points inside each')
    fig.suptitle('A geometric control, not a picture of actual zeta zeros',fontsize=12)
    fig.savefig(Path(__file__).with_name('inversion-control.png'),dpi=180,facecolor='white')
    plt.close(fig)

if __name__=='__main__':
    main()
