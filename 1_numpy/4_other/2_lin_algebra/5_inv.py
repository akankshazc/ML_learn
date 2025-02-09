import numpy as np

# define a 2x2 matrix
array1 = np.array([[2, 4],
                  [6, 8]])

# compute the inverse of the matrix
result = np.linalg.inv(array1)

print(result)
