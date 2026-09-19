"""Cycle d'hysteresis M(H) d'un materiau dur (exercice "Materiau ferromagnetique").

Sert aux questions 2 et 4 : la reponse d'un ferromagnetique n'est pas lineaire, et
c'est la largeur du cycle qui permet de garder M > 0 avec un courant negatif, tant
que |H| reste inferieur au champ coercitif H_c.

Regenerer avec :  ../../../.venv/bin/python ferromagnetisme1_4.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

w = 0.55                                   # largeur de transition, en unites de H_c
h = np.linspace(-3, 3, 2001)
descroissant = np.tanh((h + 1) / w)        # branche suivie quand H decroit (basculement en -H_c)
croissant = np.tanh((h - 1) / w)           # branche suivie quand H croit  (basculement en +H_c)

fig, ax = plt.subplots(figsize=(7.0, 4.2))
ax.axhline(0, color="0.75", lw=0.8)
ax.axvline(0, color="0.75", lw=0.8)
ax.plot(h, croissant, color="#6BB6E8", lw=2.0)
ax.plot(h, descroissant, color="#1B2E6B", lw=2.2)
# sens de parcours
for hx, br, dx in ((1.6, "d", -1), (-1.6, "c", 1)):
    y = np.tanh((hx + 1) / w) if br == "d" else np.tanh((hx - 1) / w)
    c = "#1B2E6B" if br == "d" else "#6BB6E8"
    ax.annotate("", xy=(hx + 0.35 * dx, y), xytext=(hx, y),
                arrowprops=dict(arrowstyle="-|>", color=c, lw=1.6))

# point de fonctionnement : courant negatif, aimantation toujours positive
hop = -0.55
ax.plot(hop, np.tanh((hop + 1) / w), "o", color="#C0392B", ms=8, zorder=5)
ax.annotate("$I<0$ et pourtant $M>0$", xy=(hop, np.tanh((hop + 1) / w)),
            xytext=(-2.9, 0.35), fontsize=10, color="#C0392B",
            arrowprops=dict(arrowstyle="->", color="#C0392B", lw=1.1))

# reperes M_r et H_c
ax.plot(0, np.tanh(1 / w), "o", color="0.35", ms=5)
ax.annotate("$M_r$", xy=(0, np.tanh(1 / w)), xytext=(0.12, np.tanh(1 / w) + 0.04),
            fontsize=11, color="0.25")
ax.plot(-1, 0, "o", color="0.35", ms=5)
ax.annotate("$-H_c$", xy=(-1, 0), xytext=(-1.42, -0.22), fontsize=11, color="0.25")

ax.set_xlabel("$H$"); ax.set_ylabel("$M$")
ax.set_xlim(-3, 3); ax.set_ylim(-1.25, 1.25)
ax.set_xticks([]); ax.set_yticks([])
ax.grid(False)
for bord in ("top", "right"):
    ax.spines[bord].set_visible(False)

fig.tight_layout()
fig.savefig("../ferromagnetisme1_4.pdf", bbox_inches="tight")
