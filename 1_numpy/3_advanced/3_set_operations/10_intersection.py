import numpy as np

A = np.array([1, 3, 5])
B = np.array([0, 2, 3])

# intersection of two arrays
result = np.intersect1d(A, B)

print(result)
