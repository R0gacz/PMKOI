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
noise_level = 0.00000001

x = np.linspace(start, stop, samples)
y = x**3 + 3*x + 5

y_noise = y + np.random.randn(x.shape[0])*noise_level
dy1_real = 3*x**2 + 3
dy2_real = 6*x
dy3_real = np.ones(np.size(dy2_real))*6
dy_numerical = np.gradient(y_noise, step)

def dy_f(y, step, nr, mode):
    steps = int(len(y))
    y1 = y

    if mode == 'seq':
        for j in range(nr):
            pochodna = []
            pochodna.append((y1[1] - y1[0])/step)
            for i in range(1, steps-1):
                pochodna.append((y1[i+1]-y1[i-1])/(2*(step)))
            pochodna.append((y1[steps-1] - y1[steps-2]) / step)
            y1 = pochodna

        return y1

    if mode == 'conv':
        if nr == 1:
            x_2 = np.array([-1, 0, 1])
            what_step = 2 * step
        if nr == 2:
            x_2 = np.array([1, -2, 1])
            what_step = step ** 2
        if nr == 3:
            x_2 = np.array([-1, 2, 0, -2, 1])
            what_step = 2 * step ** 3
        if nr == 4:
            x_2 = np.array([1, -4, 6, -4, 1])
            what_step = step ** 4

        x_wy = []
        zakres = len(y1) - (len(x_2) - 1)

        for i in range(zakres):
            iloczyn = np.multiply(y1[i:i + len(x_2)], x_2)
            x_wy.append(sum(iloczyn) / (what_step))
        x_wy

        return x_wy




dy1 = dy_f(y_noise, step, 1, "seq")
dy2 = dy_f(y_noise, step, 2, "seq")
dy3 = dy_f(y_noise, step, 3, "seq")
dy1c = dy_f(y_noise, step, 1, 'conv')
dy2c = dy_f(y_noise, step, 2, 'conv')
dy3c = dy_f(y_noise, step, 3, 'conv')

plt.figure(figsize =(20,4),dpi=100)
plt.subplot(1,4,1)
plt.plot(x, y_noise, "r-", color= "black", lw = 0.6, label= 'function')
plt.xlim(-3,3)
plt.grid()
plt.legend()

plt.subplot(1,4,2)
plt.plot(x[1:len(x)-1], dy1c, "-", color= "blue", lw = 1, label= 'dy1_conv')
plt.plot(x, dy1, "--" , color= "red", lw = 0.6, label = 'dy1_seq')
plt.plot(x, dy1_real, "-", color= "grey", lw = 0.6, label= 'dy1_real')
plt.xlim(-3,3)
plt.grid()
plt.legend()

plt.subplot(1,4,3)
plt.plot(x[1:len(x)-1], dy2c, "-", color= "blue", lw = 1, label= 'dy2_conv')
plt.plot(x[2:len(x)-2], dy2[2:len(x)-2], "--" , color = "red", lw = 0.6, label = 'dy2_seq')
plt.plot(x, dy2_real, "-", color= "grey", lw = 0.6, label= 'dy2_real')
plt.xlim(-3,3)
plt.grid()
plt.legend()

plt.subplot(1,4,4)
plt.plot(x[2:len(x)-2], dy3c, "-", color= "blue", lw = 1, label= 'dy3_conv')
plt.plot(x[3:len(x)-3], dy3[3:len(x)-3], "--" , color = "red", lw = 0.6, label = 'dy3_seq')
plt.plot(x, dy3_real, "-", color= "grey", lw = 0.6, label= 'dy3_real')
plt.xlim(-3,3)
plt.grid()
plt.legend()
plt.show()
