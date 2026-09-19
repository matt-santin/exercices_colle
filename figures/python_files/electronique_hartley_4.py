"""Phase des trois filtres du second ordre (exercice "Oscillateur quasi-sinusoidal",
question 3).

Avec un amplificateur de gain reel positif dans la boucle, la condition de phase
s'ecrit arg H = 0 a une pulsation finie non nulle. Seul le passe-bande y satisfait :
le passe-bas ne s'annule qu'en w = 0, le passe-haut qu'asymptotiquement.
Trace pour Q = 2 ; les limites de phase ne dependent pas de Q.

Regenerer avec :  ../../../.venv/bin/python electronique_hartley_4.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

Q = 2.0
x = np.logspace(-2, 2, 4001)
jx = 1j * x
den = 1 + jx / Q + jx**2

courbes = [
    (1 / den,        "passe-bas",    "#6BB6E8", "--"),
    (jx**2 / den,    "passe-haut",   "#2E7EBB", ":"),
    (1 / (1 + 1j * Q * (x - 1 / x)), "passe-bande", "#1B2E6B", "-"),
]

fig, ax = plt.subplots(figsize=(8.5, 4))
ax.axhline(0, color="0.45", lw=1.4)
for H, nom, couleur, style in courbes:
    ax.semilogx(x, np.angle(H), color=couleur, ls=style, lw=2.0, label=nom)

ax.plot(1, 0, "o", color="#1B2E6B", ms=8, zorder=5)
ax.annotate(r"$\arg\underline{H}=0$ en $\omega=\omega_0$", xy=(1.05, 0.05),
            xytext=(2.2, 1.75), fontsize=10, color="#1B2E6B",
            arrowprops=dict(arrowstyle="->", color="#1B2E6B", lw=1.1))

ax.set_xlabel(r"$\omega/\omega_0$"); ax.set_ylabel(r"$\arg\underline{H}$")
ax.set_xlim(1e-2, 1e2); ax.set_ylim(-np.pi - 0.2, np.pi + 0.2)
ax.set_yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])
ax.set_yticklabels([r"$-\pi$", r"$-\pi/2$", "$0$", r"$\pi/2$", r"$\pi$"])
ax.grid(True, which="both", lw=0.5, color="0.88")
ax.legend(loc="lower left", frameon=True, fontsize=9.5)

fig.tight_layout()
fig.savefig("../electronique_hartley_4.pdf", bbox_inches="tight")

for H, nom, _, _ in courbes:
    a = np.angle(H)
    print("%-12s phase : %+.3f -> %+.3f rad" % (nom, a[0], a[-1]))
