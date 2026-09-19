"""Diagramme de Bode du capteur inductif differentiel (question 2d).

H(w) = H_0 * (j w/w_0) / (1 + j w/w_0), avec H_0 = dL/L_e et w_0 = R/(2 L_e).
Passe-haut du premier ordre : on trace le gain rapporte a H_0, de sorte que le
plateau haute frequence soit a 0 dB. C'est dans ce plateau qu'il faut travailler,
la sortie y vaut H_0 = dL/L_e independamment de la frequence.

Regenerer avec :  ../../../.venv/bin/python electronique_capteur_inductif_4.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

x = np.logspace(-2, 2, 4001)
H = 1j * x / (1 + 1j * x)

fig, (ax_g, ax_p) = plt.subplots(1, 2, figsize=(11, 3.8))

for ax in (ax_g, ax_p):
    ax.axvspan(10, 100, color="#6BB6E8", alpha=0.18, lw=0)
    ax.set_xlabel(r"$x=\omega/\omega_0$")
    ax.grid(True, which="both", lw=0.5, color="0.88")
    ax.set_xlim(1e-2, 1e2)

ax_g.semilogx(x, 20 * np.log10(np.abs(H)), color="#1B2E6B", lw=2.0)
ax_g.semilogx([1e-2, 1], [-40, 0], color="0.6", ls="--", lw=1.2)
ax_g.axhline(0, color="0.6", ls="--", lw=1.2)
ax_g.set_ylabel(r"$20\log|\underline{H}/H_0|$  (dB)")
ax_g.set_ylim(-42, 8)
ax_g.text(11, -30, "zone de travail\n" + r"$\omega\gg\omega_0$", fontsize=9.5, color="#2E7EBB")

ax_p.semilogx(x, np.angle(H), color="#1B2E6B", lw=2.0)
ax_p.set_ylabel(r"$\arg\underline{H}$")
ax_p.set_ylim(-0.1, np.pi / 2 + 0.2)
ax_p.set_yticks([0, np.pi / 4, np.pi / 2])
ax_p.set_yticklabels(["$0$", r"$\pi/4$", r"$\pi/2$"])

fig.tight_layout()
fig.savefig("../electronique_capteur_inductif_4.pdf", bbox_inches="tight")
