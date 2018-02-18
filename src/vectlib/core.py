import math

def vect_add(x,y):
	return [x_i + y_i for x_i, y_i in zip(x,y)]


def vect_substract(x,y):
	return [x_i - y_i for x_i, y_i in zip(x,y)]

def vect_scalar_multiply(c,x):
	return [x_i * c for i, x_i in enumerate(x)]

def vect_sum(vect_list):
	return reduce(vect_add, vect_list)

def vect_dot(x, y):
	return sum([ x_i * y_i for x_i , y_i in zip(x,y)])

def sum_squared(x):
	return vect_dot(x,x)

def vect_magnitude(x):
	return math.sqrt(sum_squared(x))

def vect_distance(x,y):
	return vect_magnitude(vect_substract(x,y))