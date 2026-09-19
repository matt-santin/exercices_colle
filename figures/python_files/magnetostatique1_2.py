"""Profil de champ du solenoide epais (exercice "Solenoide epais a densite de
courant variable").

B(r) = mu_0 j_0 (a^2 - r^2) / (2a) pour r < a, et 0 au-dela : maximal sur l'axe,
nul au bord. C'est l'inverse du fil massif a courant axial, ou B est nul sur l'axe.

Regenerer avec :  ../../../.venv/bin/python magnetostatique1_2.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

x = np.linspace(0, 2.2, 2001)          # r/a
B = np.where(x <= 1, 1 - x**2, 0.0)    # B/B(0)

fig, ax = plt.subplots(figsize=(7.5, 3.6))
ax.plot(x, B, color="#1B2E6B", lw=2.2)
ax.axvline(1, color="0.6", ls="--", lw=1.2)
ax.axhline(0, color="0.75", lw=0.8)

ax.annotate("le champ est nul\ndès le bord", xy=(1.0, 0.0), xytext=(1.25, 0.33),
            fontsize=9.5, color="#2E7EBB",
            arrowprops=dict(arrowstyle="->", color="#2E7EBB", lw=1.1))

ax.set_xlabel("$r/a$")
ax.set_ylabel(r"$B(r)\,/\,\dfrac{\mu_0 j_0 a}{2}$")
ax.set_xlim(0, 2.2); ax.set_ylim(-0.08, 1.12)
ax.set_xticks([0, 0.5, 1, 1.5, 2])
ax.set_yticks([0, 0.5, 1])
ax.grid(True, which="major", lw=0.5, color="0.88")

fig.tight_layout()
fig.savefig("../magnetostatique1_2.pdf", bbox_inches="tight")
