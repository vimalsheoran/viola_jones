import numpy as np

import matplotlib.pyplot as plt

def convolve(patch, kernel):
	patch = patch.flatten()
	kernel = kernel.flatten()
	_sum = 0
	for x, y in zip(patch, kernel):
		_sum += (x*y)
	return _sum

def convolution(image, kernel, padding=0, stride=1):
	ix, iy = image.shape
	kx, ky = kernel.shape

	ox = int((ix - kx + 2*padding)/stride + 1)
	oy = int((iy - ky + 2*padding)/stride + 1)

	output_image = np.zeros((ox*oy), dtype=float)
	output_image = np.reshape(output_image, (ox, oy))


	for i in range(0, ox):
		for j in range(0, oy):
			patch = image[i:i+kx, j:j+ky]
			output_image[i][j] = convolve(patch, kernel)
	return output_image