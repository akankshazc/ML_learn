import numpy as np

array1 = np.array([[1, 3],
                   [5, 7]])
array2 = np.array([[2, 4],
                   [6, 8]])

# inner() for 2D arrays
result = np.inner(array1, array2)

print(result)
