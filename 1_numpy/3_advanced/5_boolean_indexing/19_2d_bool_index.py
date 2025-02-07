import numpy as np

# create a 2D  array
array1 = np.array([[1, 7, 9],
                   [14, 19, 21],
                   [25, 29, 35]])

# create a boolean mask based on the condition
# that elements are greater than 10
boolean_mask = array1 > 10

# select only the elements that satisfy the condition
result = array1[boolean_mask]

print(result)
