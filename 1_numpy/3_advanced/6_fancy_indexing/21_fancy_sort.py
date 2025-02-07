import numpy as np

array1 = np.array([3, 2, 6, 1, 8, 5, 7, 4])

# sort array1 using fancy indexing
sorted_array = array1[np.argsort(array1)]

print(sorted_array)

# sort array1 using fancy indexing in descending order
sorted_array_desc = array1[np.argsort(-array1)]

print(sorted_array_desc)
