"""Diagramme de Bode du coupe-bande L//C + R (exercice "Effet d'un filtre passif RLC parallele").

Convention canonique : H(x) = (1 + (jx)^2) / (1 + jx/Q + (jx)^2),  x = w/w0.
Q = R sqrt(C/L) : plus Q est grand, plus la bande rejetee est etroite.

Regenerer avec :  python electronique_rlc_parallele_2.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

w0 = 6.29e6                       # rad/s, valeurs de l'enonce (L = 0,10 mH, C = 0,253 nF)
w = np.logspace(0, 12, 200001)
x = w / w0

fig, (ax_g, ax_p) = plt.subplots(1, 2, figsize=(12, 4))

for Q, couleur in zip([0.1, 1, 10], ["#6BB6E8", "#2E7EBB", "#1B2E6B"]):
    H = (1 - x**2) / (1 - x**2 + 1j * x / Q)
    ax_g.semilogx(w, 20 * np.log10(np.abs(H)), color=couleur, label=f"$Q = {Q:g}$")
    ax_p.semilogx(w, np.angle(H), color=couleur, label=f"$Q = {Q:g}$")

ax_g.set_xlabel(r"$rad.s^{-1}$"); ax_g.set_ylabel(r"$G_{dB}$")
ax_g.set_ylim(-65, 5); ax_g.grid(True, which="major", lw=0.5, color="0.8")
ax_g.legend(loc="lower left", frameon=True)

ax_p.set_xlabel(r"$rad.s^{-1}$"); ax_p.set_ylabel(r"$\varphi$")
ax_p.set_ylim(-np.pi / 2 * 1.15, np.pi / 2 * 1.15)
ax_p.set_yticks([-np.pi / 2, 0, np.pi / 2]); ax_p.set_yticklabels([r"$-\pi/2$", r"$0$", r"$\pi/2$"])
ax_p.grid(True, which="major", lw=0.5, color="0.8")
ax_p.legend(loc="upper left", frameon=True)

fig.tight_layout()
fig.savefig("../electronique_rlc_parallele_2.pdf", bbox_inches="tight")
