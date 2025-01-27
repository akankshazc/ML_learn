import numpy as np

# create an array with values from 0 to 4
array1 = np.arange(5)

print("Using np.arange(5):", array1)

# create an array with values from 1 to 8 with a step of 2
array2 = np.arange(1, 9, 2)

print("Using np.arange(1, 9, 2):", array2)

# n-d arrays from np.zeros

# create 2D array with 2 rows and 3 columns filled with zeros
array3 = np.zeros((2, 3))

print("2-D Array: ")
print(array3)

# create 3D array with dimensions 2x3x4 filled with zeros
array4 = np.zeros((2, 3, 4))

print("\n3-D Array: ")
print(array4)
