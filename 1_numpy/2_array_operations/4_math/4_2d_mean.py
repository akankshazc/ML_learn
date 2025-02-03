import numpy as np

# create a 2D array
array1 = np.array([[1, 3],
                   [5, 7]])

# calculate the mean of the entire array
result1 = np.mean(array1)
print("Entire Array:", result1)

# calculate the mean along vertical axis (axis=0)
result2 = np.mean(array1, axis=0)
print("Along Vertical Axis:", result2)

# calculate the mean along  (axis=1)
result3 = np.mean(array1, axis=1)
print("Along Horizontal Axis :", result3)
