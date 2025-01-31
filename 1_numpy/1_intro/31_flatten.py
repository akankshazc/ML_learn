import numpy as np

# flatten 2D array to 1D
array1 = np.array([[1, 3], [5, 7], [9, 11]])
result1 = np.reshape(array1, -1)
print("Flattened 2D array:", result1)

# flatten 3D array to 1D
array2 = np.array([[[1, 3], [5, 7]], [[2, 4], [6, 8]]])
result2 = np.reshape(array2, -1)
print("Flattened 3D array:", result2)
