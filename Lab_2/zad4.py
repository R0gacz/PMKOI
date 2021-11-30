import numpy as np
import torch as tc
import time as t
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse
import torch.nn.functional as F
from scipy import signal

step = 1
start = 0
stop = 3
samples = int((stop - start) / step)
x = np.linspace(start, stop, samples)
y = np.linspace(start, stop, samples)
z = np.linspace(start, stop, samples)

xs, ys, zs = np.meshgrid(x, y, z)

fs = np.cos(xs)*np.sin(ys)*np.cos(zs)
print(fs)
print(fs.shape)

def dN(F, step):
    N = int(len(F.shape))
    for i in range(F.shape[N]):


    grad = np.sqrt()
    return grad



#dN(fs, step)