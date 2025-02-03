import numpy as np

# create an array
array1 = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

# compute the 25th percentile of the array
result1 = np.percentile(array1, 25)
print("25th percentile:", result1)

# compute the 75th percentile of the array
result2 = np.percentile(array1, 75)
print("75th percentile:", result2)
