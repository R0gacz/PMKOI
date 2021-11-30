import numpy as np
import scipy.linalg

A = np.array([
    [2, 5, 3],
    [8, 7, 5],
    [5, -2, 3],], dtype=np.float32)

def gaussian_elimination(macierz):
    for i in range(len(macierz) - 1):
        for j in range(i + 1, len(macierz)):
            ratio = macierz[j, i] / A[i, i]
            for k in range(len(A)):
                macierz[j, k] = macierz[j, k] - ratio * macierz[i, k]

    return macierz




print(gaussian_elimination(A))