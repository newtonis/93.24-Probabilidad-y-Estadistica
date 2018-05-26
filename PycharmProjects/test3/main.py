from math import pi,sqrt
import numpy as np
import matplotlib.pyplot as plt

import scipy.optimize as optimization


def func(x , a,b):
	return a+b*x


def grid():
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)


    # Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(0, 4, 0.1)
    minor_ticks = np.arange(0, 4, 0.02)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)


    major_ticks = np.arange(0, 34, 2)
    minor_ticks = np.arange(0, 34, 1)


    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

	# And a corresponding grid
    ax.grid(which='both')

    # Or if you want different settings for the grids:
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)


IfV = [
    (0.01, 1.48), (0.02, 1.50), (0.02, 1.52),
    (0.03, 1.54), (0.04, 1.56), (1.11, 1.71),
    (2.27, 1.66), (1.39, 1.72), (2.17, 1.74),
    (3.01, 1.76), (4.65, 1.78), (6.25, 1.80),
    (8.92, 1.82), (11.8, 1.84), (17.6, 1.88),
    (23.5, 1.9), (28.5, 1.92)]
"""
IfV = [
    (0.2 , 2.48), (0.5 , 2.54) , (0.9 , 2.58) ,
    (1.3 , 2.62), (2.3 , 2.67) , (2.5 , 2.69) ,
    (4.1 , 2.74), (5.5 , 2.77) , (8.7 , 2.85) ,
    (11.6, 2.9 ), (14.5, 2.95) , (16.6, 2.98) ,
    (20.7, 3.04), (32  , 3.17) , (34  , 3.19)
]"""

for i in range(0, len(IfV)):
    print("Medicion " + str(i) + ":" + str(IfV[i]))

# la medicion 5 y 6 estan raras
# y = i
# La variable dependiente es V
# deltay=0.01 (se supone que es mA) lo menor que mide

deltay = 0.01
w = 1 / (deltay ** 2)
xi2 = 0
yi = 0
xi = 0
yi_xi = 0
# Calculo sum de Xi^2
for k in range(0, len(IfV)):
    xi2 += ((IfV[k][1]) ** 2)
# Calculo sum de yi
for k in range(0, len(IfV)):
    yi += (IfV[k][0])
# Calculo sum de xi
for k in range(0, len(IfV)):
    xi += (IfV[k][1])
# Calculo sum de xi*yi
for k in range(0, len(IfV)):
    yi_xi += ((IfV[k][0]) * (IfV[k][1]))

num_a_e = xi2 * yi - xi * (yi_xi)

den_a_e = xi2 * len(IfV) - ((xi) ** 2)

a_e = num_a_e / den_a_e

num_b_e = len(IfV) * yi_xi - xi * yi

# el denominador de a es el mismo que el de b
b_e = num_b_e / den_a_e

print("Resultado: y=" + str(b_e) + "x" + str(a_e))
print("Con a_e=" + str(a_e) + " y " + "con b_e= " + str(b_e))

delta_a_e = (xi2 / (den_a_e * w)) ** (0.5)
delta_b_e = (1 / (den_a_e * w)) ** (0.5)
print("delta a_e=" + str(delta_a_e) + " delta_b_e=" + str(delta_b_e))

grid()
var_x = []
var_y = []
for i in IfV:
    var_x.append(i[1])
    var_y.append(i[0])


xdata = np.array(var_x)
ydata = np.array(var_y)

x0 =  np.array([0,0])
popt, pcov  = optimization.curve_fit(func , np.array(var_x[10:]) ,np.array(var_y[10:]) , x0)


plt.plot(var_x, var_y, 'o' , label = "datos")
plt.title("V(i) Led rojo",fontsize=20)

start = 0
while func( var_x[start] , *popt) < 0:
    start += 1
start -= 1

plt.plot( var_x[start:] , func(np.array(xdata[start:]), *popt) , label="y = " + str(popt[0]) + "+x"+ str(popt[1]) )
plt.legend()
plt.xlabel('V')
plt.ylabel('i')


plt.show()