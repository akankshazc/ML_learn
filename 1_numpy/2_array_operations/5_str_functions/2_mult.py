import numpy as np

# define array with three string elements
array1 = np.array(['A', 'B', 'C'])

#  repeat each element in array1 two times
result = np.char.multiply(array1, 2)

print(result)
