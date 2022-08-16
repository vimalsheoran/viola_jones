import numpy as np

def rectangle_vertical_filter(x, y, black_white):
	_filter = np.zeros((x*y), dtype=float)
	if black_white == 'black_white':
		begin = int((x*y)/2)
		end = (x*y)
	else:
		begin = 0
		end = (x*y)/2
	_filter[begin:end] = 255
	return np.reshape(_filter, (x, y))

def rectangle_horizontal_filter(x, y, black_white):
	_filter = np.zeros((x*y), dtype=float)
	mask = []
	offset = 0
	if black_white == 'black_white':
		begin = int(x/2)
		end = x
	else:
		begin = 0
		end = int(x/2)
	for i in range(0, x):
		mask.extend([i+offset for i in range(begin, end)])
		offset += x
	_filter[mask] = 255
	return np.reshape(_filter, (x, y))

def get_filter(
	xshape=24, 
	yshape=24, 
	filter_type='rect_vert', 
	black_white='black_white'):

	if filter_type == 'rect_vert':
		return rectangle_vertical_filter(xshape, yshape, black_white)

	if filter_type == 'rect_hrzn':
		return rectangle_horizontal_filter(xshape, yshape, black_white)
