"""Chronogramme du multivibrateur astable (exercice "Multivibrateur astable").

L'ALI est sature : u_s bascule entre +V_sat et -V_sat chaque fois que u_-, qui se
charge a travers RC, atteint le seuil u_+ = beta*u_s avec beta = R_1/(R_1+R_2).
Periode T = 2 RC ln(1 + 2 R_1/R_2).

Regenerer avec :  ../../../.venv/bin/python electronique_astable_2.py
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({"text.usetex": False, "font.size": 11})

Vsat, R, C, R1, R2 = 15.0, 10e3, 10e-9, 10e3, 10e3
tau = R * C
beta = R1 / (R1 + R2)
T = 2 * tau * np.log(1 + 2 * R1 / R2)

# integration segment par segment : u_- relaxe vers u_s, bascule au seuil beta*u_s
t = np.linspace(0, 2.5 * T, 6001)
um = np.empty_like(t)
us = np.empty_like(t)
u, s, t0, u0 = beta * Vsat, -1.0, 0.0, beta * Vsat
for i, ti in enumerate(t):
    u = s * Vsat + (u0 - s * Vsat) * np.exp(-(ti - t0) / tau)
    if (s < 0 and u <= -beta * Vsat) or (s > 0 and u >= beta * Vsat):
        t0, u0, s = ti, u, -s
    um[i], us[i] = u, s * Vsat

fig, ax = plt.subplots(figsize=(9, 4))
ax.axhline(beta * Vsat, color="0.6", ls=":", lw=1.2)
ax.axhline(-beta * Vsat, color="0.6", ls=":", lw=1.2)
ax.plot(t * 1e3, us, color="#6BB6E8", lw=2.0, label="$u_s(t)$")
ax.plot(t * 1e3, um, color="#1B2E6B", lw=2.0, label="$u_-(t)$")

ax.annotate("", xy=(0, -18.5), xytext=(T * 1e3, -18.5),
            arrowprops=dict(arrowstyle="<->", color="#2E7EBB", lw=1.2))
ax.text(T * 1e3 / 2, -17.6, "$T$", ha="center", fontsize=11, color="#2E7EBB")
ax.text(2.45 * T * 1e3, beta * Vsat + 0.7, r"$+\beta V_{sat}$",
        ha="right", fontsize=9.5, color="0.4")
ax.text(2.45 * T * 1e3, -beta * Vsat - 2.4, r"$-\beta V_{sat}$",
        ha="right", fontsize=9.5, color="0.4")

ax.set_xlabel("$t$ (ms)"); ax.set_ylabel("tension (V)")
ax.set_xlim(0, 2.5 * T * 1e3); ax.set_ylim(-21, 21)
ax.set_yticks([-15, -7.5, 0, 7.5, 15])
ax.grid(True, which="major", lw=0.5, color="0.88")
ax.legend(loc="upper right", frameon=True, fontsize=9.5)

fig.tight_layout()
fig.savefig("../electronique_astable_2.pdf", bbox_inches="tight")
print("T = %.3f ms, f = %.2f kHz" % (T * 1e3, 1e-3 / T))
