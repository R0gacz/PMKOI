import numpy as np


def solve_equations(A, y):
    for i in range(len(y) - 1):

        for j in range(i + 1, len(y)):
            ratio_1 = A[j, i] / A[i, i]

            for k in range(len(y)):
                A[j, k] = A[j, k] - ratio_1 * A[i, k]

    x = np.zeros(y.shape)
    for l in range(len(y) - 1, -1, -1):
        if l == len(y) - 1:
            x[l] = y[l] / A[l, l]
        else:
            ratio_2 = 1 / A[l, l]
            x[l] = ratio_2 * (y[l] - np.sum(A[l, l + 1:] @ x[l + 1:]))
    return x


pass

A1 = np.array([
    [2, 5, 3],
    [8, 7, 5],
    [5, -2, 3],
], dtype=np.float32)
y1 = np.array([10, 7, 4])

print(solve_equations(A1, y1))
print(np.linalg.inv(A1) @ y1)