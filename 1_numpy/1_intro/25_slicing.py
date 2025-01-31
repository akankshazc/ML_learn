import numpy as np

# create a 1D array
array1 = np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])

# slice array1 from index 2 to index 6 (exclusive)
print(array1[2:6])

# slice array1 from index 0 to index 8 (exclusive) with a step size of 2
print(array1[0:8:2])

# slice array1 from index 3 up to the last element
print(array1[3:])

# items from start to end
print(array1[:])
