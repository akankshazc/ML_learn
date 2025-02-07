import numpy as np

# create an array of numbers
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# create a boolean mask
boolean_mask = array1 % 2 == 0

# boolean indexing to filter the even numbers
result = array1[boolean_mask]

print(result)
