import numpy as np

# create a 2D array
array1 = np.array([[1, 3, 5],
                   [11, 7, 9],
                   [13, 18, 29]])

# create an array of row indices
row_indices = np.array([0, 1])

# use fancy indexing to select specific rows
selected_rows = array1[row_indices, :]

print(selected_rows)
