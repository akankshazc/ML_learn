import numpy as np

# load the saved arrays
load_data = np.load('file1.npz')

# retrieve the arrays using their names
array1 = load_data['file1']
array2 = load_data['file2']

# display the loaded arrays
print(array1)
print(array2)
