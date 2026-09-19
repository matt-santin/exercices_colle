"""Effet du dephaseur sur U_e = U_0 cos^3(wt) pour w = w_0/3 (exercice "Deformation
d'un signal par un filtre actif").

H(jw) = (1 - jw/w_0)/(1 + jw/w_0) : gain unite, phase phi(w) = -2 arctan(w/w_0).
Les deux harmoniques du signal (rangs 1 et 3) subissent des retards de phase
differents (1,93 RC et 1,57 RC), d'ou la deformation. La courbe de reference est
l'entree retardee du seul retard du fondamental : si le filtre ne deformait pas,
la sortie se superposerait exactement a elle.

Regenerer avec :  python electronique_dephaseur_2.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

phi = lambda x: -2 * np.arctan(x)      # x = w/w_0
x1 = 1 / 3                             # w = w_0/3 pour le fondamental
tau1 = -phi(x1) / (2 * np.pi)          # retard de phase du fondamental, en periodes

t = np.linspace(0, 2, 2001)            # t/T, deux periodes
ue = np.cos(2 * np.pi * t) ** 3
us = 0.75 * np.cos(2 * np.pi * t + phi(x1)) + 0.25 * np.cos(6 * np.pi * t + phi(3 * x1))
ue_ret = np.cos(2 * np.pi * (t - tau1)) ** 3

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(t, ue, color="0.55", ls="--", lw=1.6, label="entrée $U_e/U_0$")
ax.plot(t, ue_ret, color="#6BB6E8", ls=":", lw=2.2,
        label=r"entrée retardée de $\tau_1$ (référence sans déformation)")
ax.plot(t, us, color="#1B2E6B", lw=2.0, label="sortie $U_s/U_0$")

ax.set_xlabel("$t/T$"); ax.set_ylabel("amplitude")
ax.set_xlim(0, 2); ax.set_ylim(-1.3, 1.95)
ax.grid(True, which="major", lw=0.5, color="0.85")
ax.legend(loc="upper center", frameon=True, fontsize=9.5)

fig.tight_layout()
fig.savefig("../electronique_dephaseur_2.pdf", bbox_inches="tight")
