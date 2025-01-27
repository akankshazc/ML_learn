import numpy as np

# create an empty array of length 4
array = np.empty(4)

print(array)

# n-d arrays with np.empty

# create an empty 2D array with 2 rows and 2 columns
array1 = np.empty((2, 2))

print("2-D Array: ")
print(array1)

# create an empty 3D array of shape (2, 2, 2)
array2 = np.empty((2, 2, 2))

print("\n3-D Array: ")
print(array2)
