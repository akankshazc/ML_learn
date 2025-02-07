import numpy as np

# create an array of integers
array1 = np.array([1, 2, 4, 9, 11, 16, 18, 22, 26, 31, 33, 47, 51, 52])

# create a boolean mask using combined logical operators
boolean_mask = (array1 < 12) | (array1 > 45)

# apply the boolean mask to the array
result = array1[boolean_mask]

print(result)
