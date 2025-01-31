import numpy as np

# create a 2D array
array1 = np.array([[1, 3, 5, 7],
                   [9, 11, 13, 15],
                   [2, 4, 6, 8]])


# slice the array to get the first two rows and columns
subarray1 = array1[:2, :2]

# slice the array to get the last two rows and columns
subarray2 = array1[1:3, 2:4]

# print the subarrays
print("First Two Rows and Columns: \n", subarray1)
print("Last two Rows and Columns: \n", subarray2)
