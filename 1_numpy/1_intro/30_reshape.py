import numpy as np

array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])

# reshape a 1D array into a 2D array
# with 2 rows and 4 columns
result1 = np.reshape(array1, (2, 4))
print("With 2 rows and 4 columns: \n", result1)

# reshape a 1D array into a 2D array with a single row
result2 = np.reshape(array1, (1, 8))
print("\nWith a single row: \n", result2)

# reshape the 1D array to a 3D array
result3 = np.reshape(array1, (2, 2, 2))
print("1D to 3D Array: \n", result3)
