import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.interpolate as interp

start = 0
stop = 12
step = 0.5
divider = 3
x = np.arange(start, stop + step, step)
y = np.cos(x)
x_dense = np.arange(start, stop + step/divider, step/divider)
y_dense = np.cos(x_dense)

def interpol(x, y, x_new, mode):
    y1 =[]
    steps = int(len(y))
    divider_new = int(len(x_new)/(len(x)-1))

    if mode == 'linear':

        for i in range(0, steps-1):
            for j in range(0,divider_new):
                y1.append(y[i]+(y[i + 1] - y[i])*(x_new[divider_new*i+j] - x[i]) / (x[i+1] - x[i]))

        y1.append(y[-1])




    if mode == 'nearest':

        y1.append(y[0])
        y1.append(y[0])


        for i in range(1, steps):
            for j in range(0,divider_new):
                y1.append(y[i])




    return y1


def mse(x1, x2):
    return np.mean(np.sqrt((x1-x2)**2))



b_t = time.time()
y_near_own = interpol(x, y, x_dense, 'nearest')
e_t = time.time()
print("Time: ", e_t - b_t)


b_t = time.time()
y_lin_own = interpol(x, y, x_dense, 'linear')
e_t = time.time()
print("Time: ", e_t - b_t)

print("Linear error: ", mse(y_dense, y_lin_own))
print("Nearest error: ", mse(y_dense, y_near_own[0:-1]))

plt.figure(dpi=150)
plt.plot(x, y, "ro", label='before interpolation')
plt.plot(x_dense, y_dense, "m-+", label='ideal', lw=1)
plt.plot(x_dense, y_lin_own, "b--x", label='mlinear', lw=1)
plt.plot(x_dense, y_near_own[0:-1], "g--x", label='nearst', lw=1)
plt.grid(True)
plt.xlim([start-step, stop+step])
plt.legend()
plt.show()


y_interp_linear = interp.interp1d(x, y, kind='linear', bounds_error=False)
y_interp_nearest = interp.interp1d(x, y, kind='nearest', bounds_error=False)

b_t = time.time()
y_linear = y_interp_linear(x_dense)
e_t = time.time()
print("Time:", e_t - b_t)
b_t = time.time()
y_nearest = y_interp_nearest(x_dense)
e_t = time.time()
print("Time:", e_t - b_t)

print("Linear error: ", mse(y_dense, y_linear))
print("Nearest error: ", mse(y_dense, y_nearest))