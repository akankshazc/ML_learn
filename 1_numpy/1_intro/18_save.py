import numpy as np

# create a NumPy array
array1 = np.array([[1, 5, 9],
                   [7, 30, 15]])

# save the array to a file
np.save('file1.npy', array1)
