"""Reponse indicielle du dephaseur (exercice "Deformation d'un signal par un filtre
actif", question 4).

u_s(t) = E (1 - 2 exp(-t/RC)) pour t >= 0 : la sortie part a -E, traverse zero en
t = RC ln 2, puis tend vers +E. Le gain vaut pourtant 1 a toute frequence : un
echelon possede du spectre bien au-dela de w_0, la condition de phase lineaire de
la question 3 est donc massivement violee.

Regenerer avec :  python electronique_dephaseur_4.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

t = np.linspace(-1, 6, 3001)                       # t/RC
ue = np.where(t < 0, 0.0, 1.0)
us = np.where(t < 0, 0.0, 1 - 2 * np.exp(-np.clip(t, 0, None)))

fig, ax = plt.subplots(figsize=(8, 4))
ax.axhline(0, color="0.75", lw=0.8)
ax.plot(t, ue, color="0.55", ls="--", lw=1.6, label="entrée $U_e/E$")
ax.plot(t, us, color="#1B2E6B", lw=2.0, label="sortie $U_s/E$")

ax.plot(np.log(2), 0, "o", color="#2E7EBB", ms=7, zorder=5)
ax.annotate(r"$t=RC\ln 2$", xy=(np.log(2), 0), xytext=(np.log(2) + 0.35, -0.32),
            fontsize=9.5, color="#2E7EBB")
ax.annotate(r"$U_s(0^+)=-E$", xy=(0, -1), xytext=(0.45, -1.05),
            fontsize=9.5, color="#1B2E6B")

ax.set_xlabel("$t/RC$"); ax.set_ylabel("amplitude")
ax.set_xlim(-1, 6); ax.set_ylim(-1.35, 1.35)
ax.grid(True, which="major", lw=0.5, color="0.85")
ax.legend(loc="lower right", frameon=True, fontsize=9.5)

fig.tight_layout()
fig.savefig("../electronique_dephaseur_4.pdf", bbox_inches="tight")
