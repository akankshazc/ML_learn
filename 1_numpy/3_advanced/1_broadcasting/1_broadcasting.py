import numpy as np

# create 1-D array
array1 = np.array([1, 2, 3])

# create 2-D array
array2 = np.array([[1], [2], [3]])

# add arrays of different dimension
# size of array1 expands to match with array2
sum = array1 + array2

print(sum)