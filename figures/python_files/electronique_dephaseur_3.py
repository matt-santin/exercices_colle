"""Retard de phase et retard de groupe du dephaseur (exercice "Deformation d'un
signal par un filtre actif", question 3).

phi(w) = -2 arctan(w/w_0), donc
  retard de phase  tau_phi = -phi/w      = RC * 2 arctan(x)/x
  retard de groupe tau_g   = -dphi/dw    = RC * 2/(1 + x^2)        avec x = w/w_0.
Les deux ne coincident (et ne valent 2RC) que pour x << 1 : c'est la condition de
phase lineaire, seule situation ou le filtre retarde sans deformer. Les deux points
marques sont les harmoniques de la question 2 pour w = w_0/3.

Regenerer avec :  python electronique_dephaseur_3.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

x = np.logspace(-2, 1, 2001)
tau_phi = 2 * np.arctan(x) / x
tau_g = 2 / (1 + x**2)

fig, ax = plt.subplots(figsize=(8, 4))
ax.axhline(2, color="0.6", ls="--", lw=1.2)
ax.semilogx(x, tau_phi, color="#1B2E6B", lw=2.0, label=r"retard de phase $\tau_\varphi/RC$")
ax.semilogx(x, tau_g, color="#6BB6E8", lw=2.0, label=r"retard de groupe $\tau_g/RC$")

for xi, nom in [(1 / 3, "fondamental"), (1, "harmonique 3")]:
    yi = 2 * np.arctan(xi) / xi
    ax.plot(xi, yi, "o", color="#2E7EBB", ms=7, zorder=5)
    ax.annotate(f"{nom}\n$\\tau_\\varphi={yi:.2f}\\,RC$", xy=(xi, yi),
                xytext=(xi * 0.72, yi - 0.48), fontsize=9, ha="center", color="#2E7EBB")

ax.text(0.013, 2.06, "$2RC$ : retard commun à toutes les harmoniques",
        fontsize=9, color="0.35")
ax.set_xlabel(r"$x=\omega/\omega_0$"); ax.set_ylabel("retard (en unités de $RC$)")
ax.set_xlim(1e-2, 10); ax.set_ylim(0, 2.35)
ax.grid(True, which="both", lw=0.5, color="0.88")
ax.legend(loc="lower left", frameon=True, fontsize=9.5)

fig.tight_layout()
fig.savefig("../electronique_dephaseur_3.pdf", bbox_inches="tight")
