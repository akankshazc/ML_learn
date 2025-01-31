import numpy as np

# Array Manipulation Functions

# create a 1D array
a = np.array([1, 2, 3, 4, 5, 6])

# reshape the array to 2D
b = np.reshape(a, (2, 3))

# transpose the 2D array
c = np.transpose(b)

print("Original 1D array:\n", a)
print("\nReshaped 2D array:\n", b)
print("\nTransposed 2D array:\n", c)
