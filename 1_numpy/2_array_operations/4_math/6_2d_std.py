import numpy as np

# create a 2D array
array1 = np.array([[2, 5, 9],
                   [3, 8, 11],
                   [4, 6, 7]])

# compute standard deviation along horizontal axis
result1 = np.std(array1, axis=1)
print("Standard deviation along horizontal axis:", result1)

# compute standard deviation along vertical axis
result2 = np.std(array1, axis=0)
print("Standard deviation  along vertical axis:", result2)

# compute standard deviation of entire array
result3 = np.std(array1)
print("Standard deviation of entire array:", result3)
