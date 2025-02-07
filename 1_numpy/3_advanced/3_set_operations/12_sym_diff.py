import numpy as np

A = np.array([1, 3, 5])
B = np.array([0, 2, 3])

# symmetric difference of two arrays
result = np.setxor1d(A, B)

print(result)
