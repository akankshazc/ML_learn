import numpy as np

# create a NumPy array
array2 = np.array([[1, 3, 5],
                   [7, 9, 11]])

# save the array to a file
np.savetxt('file2.txt', array2)
