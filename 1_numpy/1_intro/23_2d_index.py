import numpy as np

# create a 2D array
array1 = np.array([[1, 3, 5, 7],
                   [9, 11, 13, 15],
                   [2, 4, 6, 8]])


# access the element at the second row and fourth column
element1 = array1[1, 3]
print("4th Element at 2nd Row:", element1)

# access the element at the first row and second column
element2 = array1[0, 1]
print("2nd Element at First Row:", element2)

# access the second row of the array
second_row = array1[1, :]
print("Second Row:", second_row)

# access the third column of the array
third_col = array1[:, 2]
print("Third Column:", third_col)
