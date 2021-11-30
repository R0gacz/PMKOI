import numpy as np
import torch as tc
import time as t
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse
import torch.nn.functional as F
from scipy import signal

step = 0.01
start = -3
stop = 3
samples = int((stop - start) / step)
noise_level = 0.0001

x = np.linspace(start, stop, samples)
y = x**3 + 3*x + 5

y_noise = y + np.random.randn(x.shape[0])*noise_level
dy1_real = 3*x**2 + 3
dy2_real = 6*x
dy3_real = np.ones(np.size(dy2_real))*6
dy_numerical = np.gradient(y_noise, step)

def dy_f(y, step, nr):
    steps = int(len(y))
    if nr == 1:
        pochodna = []
        pochodna.append((y[1] - y[0])/step)
        for i in range(1, steps-1):
            pochodna.append((y[i+1]-y[i-1])/(2*(step)))
        pochodna.append((y[steps-1] - y[steps-2]) / step)

    if nr == 2:
        pochodna = []
        pochodna.append((y[1] - y[0])/step)
        for i in range(1, steps-1):
            pochodna.append((y[i+1]-2*y[i]-y[i-1])/(step**2))
        pochodna.append((y[steps-1] - y[steps-2]) / step)

    if nr == 3:
        pochodna = []
        pochodna.append((y[1] - y[0])/step)
        for i in range(1, steps-1):
            pochodna.append((y[i+1]-y[i-1])/(2*(step)))
        pochodna.append((y[steps-1] - y[steps-2]) / step)

    return pochodna

dy1 = dy_f(y_noise, step, 1)
dy2 = dy_f(y_noise, step, 2)
dy3 = dy_f(y_noise, step, 3)

plt.figure(figsize =(20,4),dpi=150)
plt.subplot(1,4,1)
plt.plot(x, y_noise, "r-", color= "black", lw = 0.6, label= 'function')
plt.xlim(-3,3)
plt.grid()
plt.legend()

plt.subplot(1,4,2)
plt.plot(x, dy1_real, "-", color= "grey", lw = 0.6, label= 'dy1_real')
plt.plot(x, dy1, "-" , color= "green", lw = 0.6, label = 'dy1')
plt.xlim(-3,3)
plt.grid()
plt.legend()

plt.subplot(1,4,3)
plt.plot(x, dy2, "-" , color = "blue", lw = 0.6, label = 'dy2')
plt.plot(x, dy2_real, "-", color= "grey", lw = 0.6, label= 'dy2_real')
plt.xlim(-3,3)
plt.grid()
plt.legend()

plt.subplot(1,4,4)
plt.plot(x, dy3, "-" , color = "red", lw = 0.6, label = 'dy3')
plt.plot(x, dy3_real, "-", color= "grey", lw = 0.6, label= 'dy3_real')
plt.xlim(-3,3)
plt.grid()
plt.legend()
plt.show()


def splot(x_1, x_2):
    x_2 = np.flip(x_2)
    x_wy = []
    s = lambda a, b: x_1[a:b]*x_2[a:b]
#    if x_2<x_1:

    for i in range( len(x_2) - 1)) / 2, len(x_1) - (len(x_2)-1))):
        lp = i - len(x_2) - 1) / 2
        x_wy.append(sum(i,))

    return x_wy

result = signal.convolve(x1, x2)
print(result)

result2 = splot(x1,x2)
print(result2)

if mode == 'conv':
    for j in range(nr):
        x_2 = np.array([-1, 0, 1])
        x_wy = []
        zakres = len(y1) - (len(x_2) - 1)

        for i in range(zakres):
            iloczyn = np.multiply(y1[i:i + len(x_2)], x_2)
            x_wy.append(sum(iloczyn) / (2 * step))
        y1 = x_wy

    return x_wy