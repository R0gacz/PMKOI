import numpy as np
import torch as tc
import time as t
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error as mse
import torch.nn.functional as F
from scipy import signal

x1 = np.array([2, 3, 5, 1, 2, 6], dtype=np.float32)
x2 = np.array([1,2,3], dtype=np.float32)



def splot(x_1, x_2, mode):

    if len(x_2) > len(x_1):
        i = x_1
        x_1= x_2
        x_2 = i

    x_2 = np.flip(x_2)

    if mode == 'full':
        x_1zeros = np.zeros(len(x_2) - 1)
        x_1 = np.append(x_1zeros, x_1)
        x_1 = np.append(x_1, x_1zeros)



    x_wy = []
    zakres = len(x_1) - (len(x_2)-1)


    for i in range(zakres):
        iloczyn = np.multiply(x_1[i:i + len(x_2)], x_2)
        x_wy.append(sum(iloczyn))

    return x_wy

b_1 = t.time()
result1 = splot(x2,x1,"full")
e_1 = t.time()
print('Result 1:', result1)
print("Time1: ", e_1-b_1)


b_2 = t.time()
result2 = splot(x1,x2, 'valid')
e_2 = t.time()
print('Result 2:', result2)
print("Time1: ", e_2-b_2)


b_3 = t.time()
result3 = signal.convolve(x1, x2, mode='full')
e_3 = t.time()
print('Result 3:', result3)
print("Time1: ", e_3-b_3)

b_4 = t.time()
result4 = signal.convolve(x1, x2, mode= 'valid')
e_4 = t.time()
print('Result 4:', result4)
print("Time1: ", e_4-b_4)