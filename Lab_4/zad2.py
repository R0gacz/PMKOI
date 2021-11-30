import time as t
import numpy as np
import scipy.interpolate as interp
import scipy.signal as sg
import matplotlib.pyplot as plt

start = 0
stop = 10
step = 0.5

x = np.arange(start, stop + step, step)
y = x**4 - 4*x**2  - 84


y_interp_linear = interp.interp1d(x, y, kind='linear')
y_interp_cubic = interp.interp1d(x, y, kind='cubic')
y_interp_nearest = interp.interp1d(x, y, kind='nearest')
y_interp_rbf = interp.Rbf(x, y, function='thin-plate')

divider = 3
x_dense = np.arange(start, stop + step/divider, step/divider)
y_linear = y_interp_linear(x_dense)
y_cubic = y_interp_cubic(x_dense)
y_nearest = y_interp_nearest(x_dense)
y_rbf = y_interp_rbf(x_dense)

# podwójnie pierwsza pochodna
conv1 = [-1, 0, 1]
h = step/divider
dy1_int_linear = sg.convolve((sg.convolve(y_linear, conv1)/(2*h)), conv1)/(2*h)
dy1_int_cubic = sg.convolve((sg.convolve(y_cubic, conv1)/(2*h)), conv1)/(2*h)
dy1_int_nearest = sg.convolve((sg.convolve(y_nearest, conv1)/(2*h)), conv1)/(2*h)
dy1_int_rbf = sg.convolve((sg.convolve(y_rbf, conv1)/(2*h)), conv1)/(2*h)

#druga pochodna
conv2 = [1, -2, 1]
dy2_int_linear = sg.convolve(y_linear, conv2)/(h**2)
dy2_int_cubic = sg.convolve(y_cubic, conv2)/(h**2)
dy2_int_nearest = sg.convolve(y_nearest, conv2)/(h**2)
dy2_int_rbf = sg.convolve(y_rbf, conv2)/(h**2)

dy = 6*x_dense + 8


plt.figure(dpi=150)
plt.subplot(1, 4, 1)
plt.title('knn', loc='center', fontsize=12)
plt.plot(x_dense[1:-1], dy1_int_nearest[3:len(dy1_int_nearest)-3], "b-")
plt.plot(x_dense[1:-1], dy2_int_nearest[2:len(dy2_int_nearest)-2], "g-")
plt.plot(x_dense[1:-1], dy[1:-1], "r--")
plt.grid(True)
plt.xlim([start, stop])

plt.subplot(1, 4, 2)
plt.title('linear', loc='center', fontsize=12)
plt.plot(x_dense[1:-1], dy1_int_linear[3:len(dy1_int_linear)-3], "b-")
plt.plot(x_dense[1:-1], dy2_int_linear[2:len(dy2_int_linear)-2], "g-")
plt.plot(x_dense[1:-1], dy[1:-1], "r--")
plt.grid(True)
plt.xlim([start, stop])

plt.subplot(1, 4, 3)
plt.title('cubic', loc='center', fontsize=12)
plt.plot(x_dense[2:-2], dy1_int_cubic[4:-4], "b--")
plt.plot(x_dense[2:-2], dy2_int_cubic[3:-3], "g-",lw=0.6)
plt.plot(x_dense[2:-2], dy[2:-2], "r--", lw=0.6)
plt.grid(True)
plt.xlim([start, stop])

plt.subplot(1, 4, 4)
plt.title('rbf', loc='center', fontsize=12)
plt.plot(x_dense[2:-2], dy1_int_rbf[4:-4], "b-", label ='podwójnie pierwsza pochodna')
plt.plot(x_dense[2:-2], dy2_int_rbf[3:-3], "g-", label ='druga pochodna')
plt.plot(x_dense[2:-2], dy[2:-2], "r--")
plt.legend()
plt.grid(True)
plt.xlim([start, stop])

plt.show()