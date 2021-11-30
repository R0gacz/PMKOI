import time as t
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as ig
start = -5
stop = 5
step = 0.0001
samples = int((stop - start) / step)

x = np.linspace(start, stop, samples)

y = x**2 + np.random.randn(len(x))

def Inegr(y1, dx, metod):
    steps = y/dx
    I = 0
    if metod == 'trapez':
        for i in range(1, len(steps)):
            yield I
            I +=(((y1[i-1]+y1[i])*dx)/2)
        yield I

    if metod == 'simps1/3':
        yield I
        I += y1[0]
        for i in range(1, len(steps)-2):
            if i%2 == 0:
                yield I*dx/3
                I += 2*y[i]

            else:
                yield I*dx/3
                I += 4*y[i]
        yield I * dx / 3
        yield (I+ y[-1])*dx/3

    if metod == 'simps3/8':
        yield I
        I += y1[0]
        for i in range(1, len(steps) - 2):
            if i % 3 == 0:
                yield I * 3 * dx / 8
                I * 3 * dx / 8
                I += 2 * y[i]
            else:
                yield I * 3 * dx / 8
                I += 3 * y[i]
        yield I * 3 * dx / 8
        yield (I + y[-1]) * 3 * dx / 8





example_integral = Inegr(y,step,'trapez')
I1 = []
for i in example_integral:
    I1.append(i)


example_integral = Inegr(y,step,"simps1/3")
I2 = []
for i in example_integral:
    I2.append(i)


example_integral = Inegr(y,step,"simps3/8")
I3= []
for i in example_integral:
    I3.append(i)


plt.figure(dpi=150)
plt.plot(x,y, 'r-')
plt.plot(x,I1, 'b-')
#plt.plot(x,I2, 'g-')
#plt.plot(x,I3, 'y-')
plt.grid()
plt.xlim(start,stop)
plt.show()
