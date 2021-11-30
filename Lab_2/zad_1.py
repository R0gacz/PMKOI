import numpy as np
import torch as tc
import time as t
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse
import torch.nn.functional as F
from scipy import signal

step = 0.1
start = -3
stop = 3
samples = int((stop - start) / step)
noise_level = 0.001

x = np.linspace(start, stop, samples)
print(x)
y = x**3 + 3*x + 5

y_noise = y + np.random.randn(x.shape[0])*noise_level
dy_real = 3*x**2 + 3
dy_numerical = np.gradient(y_noise, step)

def dy_func(y, step, mode):
    pochodna = []
    steps = int(len(y))

    if mode == 'central':
        pochodna.append((y[1] - y[0])/step)
        for i in range(1, steps-1):
            pochodna.append((y[i+1]-y[i-1])/(2*(step)))
        pochodna.append((y[steps-1] - y[steps-2]) / step)

    if mode == 'forward':
        for i in range(steps-1):
            pochodna.append((y[i+1]-y[i])/step)
        pochodna.append((y[steps-1] - y[steps-2]) / step)

    if mode == 'back':
        pochodna.append((y[1] - y[0])/step)
        for i in range(1, steps):
            pochodna.append((y[i]-y[i-1])/(step))

    return pochodna

b_c = t.time()
centr = dy_func(y_noise, step ,'central')
e_c = t.time()

b_f = t.time()
forward = dy_func(y_noise, step ,'forward')
e_f = t.time()

b_b = t.time()
back = dy_func(y_noise, step ,'back')
e_b = t.time()

print("Mean square error for center method: ",mse(centr,dy_real))
print("Compilation time:", b_c-e_c ,"\n")
print("Mean square error for forward method: ",mse(forward,dy_real))
print("Compilation time:", b_f-e_f ,"\n")
print("Mean square error for back method: ",mse(back,dy_real))
print("Compilation time:", b_b-e_b ,"\n")

plt.figure(dpi=150)
plt.plot(x, y_noise, "r-", color= "black", lw = 0.6, label= 'function')
plt.plot(x, dy_real, "-", color= "grey", lw = 0.6, label= 'real')
plt.plot(x, centr, "-" , color= "green", lw = 0.6, label = 'central')
plt.plot(x, forward, "-" , color = "blue", lw = 0.6, label = 'forward')
plt.plot(x, back, "-" , color = "red", lw = 0.6, label = 'back')
plt.xlim(-3,3)
plt.grid()
plt.legend()
plt.show()

"""
metoda centralna najdokładniejsza, najwolniejsza
metoda wstecz gdy pochodna liczona w czasie rzeczywistym pomiarów - nie znamy wartości funkcji w przód

"""