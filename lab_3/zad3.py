import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

start = -2
stop = 2
step = 0.01
samples = int((stop - start) / step)

x = np.linspace(start, stop, samples)
y = np.linspace(start, stop, samples)

xs, ys = np.meshgrid(x,y)
zs = xs**2 + ys**2
# 42.6667

def Integr(z, x_step, y_step):
    xsteps = int((stop - start) / step)
    ysteps = int((stop - start) / step)
    I2 = 0
    I = [0]
    for j in range(1, xsteps+1):
        I1 = 0
        for i in range(1, ysteps):
            I1 += ((z[j-1][i - 1] + z[j-1][i]) * y_step) / 2

        I.append(I1)
        I2 += ((I[j - 1] + I[j]) * x_step) / 2
    return I2



b_t = time.time()
print(Integr(zs,step,step))
e_t = time.time()
print("Time: ", e_t - b_t)


b_t = time.time()
print("2-D Integral Gaussian 2-D: ", integrate.dblquad(lambda y, x: y**2 + x**2, -2, 2, -2, 2))
e_t = time.time()
print("Time: ", e_t - b_t)