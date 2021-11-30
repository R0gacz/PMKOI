import numpy as np
import time
import matplotlib.pyplot as plt
import scipy.interpolate as interp

start = 0
stop = 20
samples = 40
x = np.linspace(start, stop, samples)
y = np.linspace(start, stop, samples)

xs, ys = np.meshgrid(x, y)
zs = np.cos(xs)*np.sin(ys)

def our_interpolate_2d(grid , values , points , mode="linear "):
# mode − linear or nearest
# grid − regular grid (YxXx2)
# values − input values (YxX)
# points − locations to interpolate (Nx2)
    pass

plt.figure(dpi=150, figsize=(5, 5))
plt.imshow(zs, cmap='gray')
plt.grid(False)
plt.axis('off')
plt.show()

#our_near_2d = our_interpolate_2d(zs, zs)