import numpy as np

# to generate a 1D array of 10 random integers from 0 to 100
integer_array = np.random.randint(0, 100, 10)

print("1D array of 10 random integers from 0 to 100:\n", integer_array)

# to generate a 1D array of 10 random floats from 0 to 1
float_array = np.random.rand(10)

print("1D array of 10 random floats from 0 to 1:\n", float_array)

# to generate a 2D array of 3x3 random integers from 0 to 100
integer_array_2d = np.random.randint(0, 100, (3, 3))

print("2D array of 3x3 random integers from 0 to 100:\n", integer_array_2d)
