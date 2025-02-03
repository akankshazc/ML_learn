import numpy as np

# create a 2D array
array1 = np.array([[2, 4, 6],
                   [8, 10, 12],
                   [14, 16, 18]])

# compute median along horizontal axis
result1 = np.median(array1, axis=1)

print("Median along horizontal axis :", result1)

# compute median along vertical axis
result2 = np.median(array1, axis=0)

print("Median along vertical axis:", result2)

# compute median of entire array
result3 = np.median(array1)

print("Median of entire array:", result3)
