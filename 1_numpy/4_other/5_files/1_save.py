import numpy as np

# create two NumPy arrays
array1 = np.array([2, 6, 10])
array2 = np.array([4, 8, 12])

# save the two arrays into a single file
np.savez('file1.npz', file1=array1, file2=array2)
