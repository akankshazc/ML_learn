import numpy as np

array1 = np.array([3, 2, 6, 1, 8, 5, 7, 4])

# create a list of indices to assign new values
indices = [1, 3, 6]

# create a new array of values to assign
new_values = [10, 20, 30]

# use fancy indexing to assign new values to specific elements
array1[indices] = new_values

print(array1)
