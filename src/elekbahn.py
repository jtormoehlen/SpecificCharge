import matplotlib.pyplot as g
import numpy as np


def K():
    my_0 = 4 * np.pi * 1E-7
    n = 320
    R = 0.135
    return my_0 * np.sqrt(4**3 / 5**3) * (n / R)


def factor(B, E):
    return (2 * E) / (B * B)


def E_K(U_K):
    return U_K / 0.054


def B(I):
    return K() * I


# print("Spulenkonstante" + str(K()))
x_fit = np.arange(0.1E13, 7.5E13, 0.1E13)
x_100 = np.array([1.554, 2.625, 3.696, 4.729, 5.704, 6.660, 7.597, 8.476])
y_100 = np.array([0.1173, 0.1814, 0.2255, 0.3087, 0.4307, 0.5522, 0.6333, 0.8130])
x_100 *= x_100
x_125 = np.array([1.613, 2.660, 3.686, 4.731, 5.693, 6.634, 7.575, 8.493])
y_125 = np.array([0.1230, 0.1846, 0.2671, 0.3938, 0.5174, 0.6836, 0.8498, 1.080])
x_125 *= x_125
x_150 = np.array([1.547, 2.660, 3.642, 4.698, 5.698, 6.623, 7.566, 8.491])
y_150 = np.array([0.1200, 0.2085, 0.2957, 0.4418, 0.6069, 0.7906, 1.013, 1.255])
x_150 *= x_150

fit = np.polyfit(x_100 * factor(B(0.083), E_K(805)), y_100, 1)
p = np.poly1d(fit)
g.plot(x_100 * factor(B(0.083), E_K(805)), y_100, 'o', label=r"$y_0=1.00$cm")
g.plot(x_fit, p(x_fit), '--C0', label=str(np.around(p.c[0] * factor(B(0.083), E_K(805)) * 100, 4)) + r"$\times 10^{11}$C/kg")
fit = np.polyfit(x_125 * factor(B(0.12), E_K(1136)), y_125, 1)
p = np.poly1d(fit)
g.plot(x_125 * factor(B(0.12), E_K(1136)), y_125, 'o', label=r"$y_0=1.25$cm")
g.plot(x_fit, p(x_fit), '--C1', label=str(np.around(p.c[0] * factor(B(0.12), E_K(1136)) * 100, 4)) + r"$\times 10^{11}$C/kg")
fit = np.polyfit(x_150 * factor(B(0.14), E_K(1344)), y_150, 1)
p = np.poly1d(fit)
g.plot(x_150 * factor(B(0.14), E_K(1344)), y_150, 'o', label=r"$y_0=1.50$cm")
g.plot(x_fit, p(x_fit), '--C2', label=str(np.around(p.c[0] * factor(B(0.14), E_K(1344)) * 100, 4)) + r"$\times 10^{11}$C/kg")

g.legend()
g.grid()
g.xlabel(r"$2E_K / B^2 \cdot x^2$", fontsize=16)
g.ylabel(r"Auslenkung $y$ in [cm]", fontsize=16)
g.savefig("plots/elekbahn.png")
g.show()
