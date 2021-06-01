import matplotlib.pyplot as g
import numpy as np


def K():
    my_0 = 4 * np.pi * 1E-7
    n = 154
    R = 0.2
    return my_0 * np.sqrt(4**3 / 5**3) * (n / R)


def B(I):
    return K() * I


def x(B, r):
    return B*B*r*r


def B_inhom(r, I):
    my_0 = 4 * np.pi * 1E-7
    n = 154
    R = 0.2
    ex1 = 1 / (np.sqrt((R**2 + (r + (R / 2))**2)**3))
    ex2 = 1 / (np.sqrt((R**2 + (r - (R / 2))**2)**3))
    return ((my_0 * n * R**2 * I)/2) * (ex1 + ex2)


# print("Spulenkonstante" + str(K()))
x_fit = np.arange(1.5E-9, 3.5E-9, 0.1E-9)
I_r_5 = np.array([1.18, 1.26, 1.35, 1.40, 1.47, 1.52])
I_r_4 = np.array([1.45, 1.57, 1.68, 1.76, 1.85, 1.93])
I_r_3 = np.array([1.99, 2.14, 2.26, 2.39, 2.50, 2.61])
I_r_2 = np.array([3.08, 3.29, 3.49, 3.69, 3.85, 4.02])
U_a = np.array([150, 170, 190, 210, 230, 250])

fit = np.polyfit(x(B(I_r_2), 0.02), U_a, 1)
p = np.poly1d(fit)
g.plot(x(B(I_r_2), 0.02), U_a, 'o', label=r"$r=2$cm")
g.plot(x_fit, p(x_fit), '--C0', label=str(np.around(p.c[0] * 1E-11, 4)) + r"$\times 10^{11}$C/kg")
fit = np.polyfit(x(B(I_r_3), 0.03), U_a, 1)
p = np.poly1d(fit)
g.plot(x(B(I_r_3), 0.03), U_a, 'o', label=r"$r=3$cm")
g.plot(x_fit, p(x_fit), '--C1', label=str(np.around(p.c[0] * 1E-11, 4)) + r"$\times 10^{11}$C/kg")
fit = np.polyfit(x(B(I_r_4), 0.04), U_a, 1)
p = np.poly1d(fit)
g.plot(x(B(I_r_4), 0.04), U_a, 'o', label=r"$r=4$cm")
g.plot(x_fit, p(x_fit), '--C2', label=str(np.around(p.c[0] * 1E-11, 4)) + r"$\times 10^{11}$C/kg")
fit = np.polyfit(x(B(I_r_5), 0.05), U_a, 1)
p = np.poly1d(fit)
g.plot(x(B(I_r_5), 0.05), U_a, 'o', label=r"$r=5$cm")
g.plot(x_fit, p(x_fit), '--C3', label=str(np.around(p.c[0] * 1E-11, 4)) + r"$\times 10^{11}$C/kg")

g.legend()
g.grid()
g.xlabel(r"$(Br)^2$ in [(Tm)$^2$]", fontsize=16)
g.ylabel(r"Beschleunigungsspannung $U_a$ in [V]", fontsize=16)
g.savefig("plots/spezladung.png")
g.show()
