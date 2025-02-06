import numpy as np

A = np.array([1, 3, 5])
B = np.array([0, 2, 3])

# difference of two arrays
result = np.setdiff1d(A, B)

print(result)
