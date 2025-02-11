import numpy as np

array1 = np.array([[2, 4, 6],
                  [8, 10, 12]])

# save the array to a file
np.save('file1.npy', array1)

# load the saved NumPy array
loaded_array = np.load('file1.npy')

# display the loaded array
print(loaded_array)
