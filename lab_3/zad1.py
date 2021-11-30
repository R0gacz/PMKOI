import time as t
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
start = -np.pi
stop = np.pi
step = 0.0001
samples = int((stop - start) / step)

x = np.linspace(start, stop, samples)
y = np.cos(x)

def Inegr(y1, dx, metod):
    steps = y/step
    I = 0
    if metod == 'trapez':
        for i in range(1, len(steps)):
            I +=(((y1[i-1]+y1[i])*dx)/2)

    if metod == 'simps1/3':
        I += y1[0] + y[-1]
        for i in range(1, len(steps)-1):
            if i%2 == 0:
                I += 2*y[i]
            else:
                I += 4*y[i]

        I=I*dx/3

    if metod == 'simps3/8':
        I += y1[0] + y[-1]
        for i in range(1, len(steps) - 1):
            if i % 3 == 0:
                I += 2 * y[i]
            else:
                I += 3 * y[i]

        I = I * 3 * dx / 8

    return I

b_t = t.time()
a = Inegr(y,step,'trapez')
e_t = t.time()
print(a)
print("Time: ", e_t-b_t, '\n')

b_t = t.time()
a = Inegr(y,step,'simps1/3')
e_t = t.time()
print(a)

print("Time: ", e_t-b_t, '\n')
b_t = t.time()
a = Inegr(y,step,'simps3/8')
e_t = t.time()
print(a)
print("Time: ", e_t-b_t, '\n')

b_t = t.time()
result_trapezoidal_2 = integrate.trapz(y, dx=step)
e_t = t.time()
print("Result trapezoidal_2: ", result_trapezoidal_2)
print("Elapsed time: ", e_t - b_t)

b_t = t.time()
result_simpson_2 = integrate.simps(y, dx=step)
e_t = t.time()
print("Result simpson_2: ", result_simpson_2)
print("Elapsed time: ", e_t - b_t)