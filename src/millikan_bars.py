import matplotlib.pyplot as g
import numpy as np


def f(v, u):
    a = (4/3)*np.pi*9.81*886
    b = (((0.5E-3/u)+(0.5E-3/v))/(0.5E-3/v))*(0.00767/300)
    c = np.sqrt((8.2E-3/(2*101485))**2+((9*1.852E-5*(0.5E-3/v))/(2*886*9.81)))
    d = a*(c-(8.2E-3/(2*101485)))**3*b
    return d


t_v = np.array([21.36, 17.35, 17.64, 17.73, 19.03, 14.93, 14.21, 14.87, 14.58, 14.85,
                18.10, 12.57, 15.25, 15.40, 14.91, 14.33, 14.87])
t_u = np.array([2.47, 2.97, 9.47, 8.82, 2.22, 11.87, 2.28, 1.66, 11.66, 2.01,
                1.89, 3.94, 6.93, 2.43, 9.52, 2.83, 1.63])
barList = []
height = [3, 3, 5, 5, 3, 5, 3, 2, 5, 3, 3, 3, 1, 3, 5, 3, 2]

barList.append(np.round(f(t_v, t_u)/1.6E-19))

bars = np.array(barList)
g.bar(bars[0], height)

res9 = (f(t_v[7], t_u[7]) + f(t_v[16], t_u[16])) / 2
res7 = (f(t_v[6], t_u[6]) + f(t_v[9], t_u[9]) + f(t_v[10], t_u[10])) / 3
res6 = (f(t_v[4], t_u[4]) + f(t_v[13], t_u[13]) + f(t_v[15], t_u[15])) / 3
res5 = (f(t_v[0], t_u[0]) + f(t_v[1], t_u[1]) + f(t_v[11], t_u[11])) / 3
res3 = f(t_v[12], t_u[12])
res2 = (f(t_v[2], t_u[2]) + f(t_v[3], t_u[3]) + f(t_v[5], t_u[5]) + f(t_v[8], t_u[8]) + f(t_v[14], t_u[14])) / 5

print("7e-6e: " + str(res7 - res6))
print("6e-5e: " + str(res6 - res5))
print("3e-2e: " + str(res3 - res2))
print("9e-6e-2e: " + str(res9 - res6 - res2))
# print(str(bars))
e_avg = ((res7 - res6) + (res6 - res5) + (res3 - res2) + (res9 - res6 - res2)) / 4
print("e_avg: " + str(e_avg))

g.grid(axis='y')
g.xlabel(r"Ladung $q$ in e", fontsize=16)
g.ylabel(r"Anzahl", fontsize=16)
g.savefig("plots/milli_bars.png")
g.show()
