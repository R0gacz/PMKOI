from skimage import io
from skimage import color
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
array = io.imread("pepe.jpg")
array = color.rgb2gray(array)

grad_y, grad_x = np.gradient(array)

rows = 1
cols = 4

sum_xx = np.cumsum(grad_x, axis=1)
sum_yy = np.cumsum(grad_y, axis=0)
sum_xy = np.cumsum(grad_x, axis=0)
sum_yx = np.cumsum(grad_y, axis=1)

total = sum_xx + sum_yy

plt.figure(dpi=250)
plt.subplot(rows, cols, 1)
plt.imshow(array, cmap='gray')
plt.axis('off')
plt.subplot(rows, cols, 2)
plt.imshow(grad_x, cmap='gray')
plt.axis('off')
plt.subplot(rows, cols, 3)
plt.imshow(grad_y, cmap='gray')
plt.axis('off')
plt.subplot(rows, cols, 4)
plt.imshow(total, cmap='gray')
plt.axis('off')

print("Min/Max", np.min(array), np.max(array))
print("Diff: ", np.mean(np.abs(array-total)))

plt.figure(dpi=250)
plt.subplot(rows, cols, 1)
plt.imshow(array, cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.subplot(rows, cols, 2)
plt.imshow(grad_x, cmap='gray')
plt.axis('off')
plt.subplot(rows, cols, 3)
plt.imshow(grad_y, cmap='gray')
plt.axis('off')
plt.subplot(rows, cols, 4)
plt.imshow(total, cmap='gray', vmin=0, vmax=1)
plt.axis('off')

normalize = lambda image: (image - np.min(image)) / (np.max(image) - np.min(image))

plt.figure(dpi=250)
plt.subplot(rows, cols, 1)
plt.imshow(normalize(array), cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.subplot(rows, cols, 2)
plt.imshow(grad_x, cmap='gray')
plt.axis('off')
plt.subplot(rows, cols, 3)
plt.imshow(grad_y, cmap='gray')
plt.axis('off')
plt.subplot(rows, cols, 4)
plt.imshow(normalize(total), cmap='gray', vmin=0, vmax=1)
plt.axis('off')

print("Min/Max input", np.min(normalize(array)), np.max(normalize(array)))
print("Min/Max integral", np.min(normalize(total)), np.max(normalize(total)))
print("Diff: ", np.mean(np.abs(normalize(array)-normalize(total))))
plt.figure(dpi=100)
plt.imshow(np.abs(normalize(array)-normalize(total)), cmap='gray', vmin=0, vmax=1)
plt.figure(dpi=100)
plt.imshow(np.abs(normalize(array)-normalize(total)), cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.figure(dpi=100)
plt.imshow(normalize(array)-normalize(total), cmap='gray', vmin=0, vmax=1)
plt.show()
print("Diff: ", np.mean(normalize(array)-normalize(total)))