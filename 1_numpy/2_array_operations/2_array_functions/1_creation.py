import numpy as np

# Array Creation Functions

# create an array using np.array()
array1 = np.array([1, 2, 3, 4, 5])
print("np.array(): \n", array1)

# create an array filled with zeros using np.zeros()
array2 = np.zeros((2, 3))
print("\nnp.zeros(): \n", array2)

# create an array filled with ones using np.ones()
array3 = np.ones((2, 3))
print("\nnp.ones(): \n", array3)

# create an array filled with a specific value using np.full()
array4 = np.full((2, 3), 5)
print("\nnp.full(): \n", array4)

# create an array with a range of values using np.arange()
array5 = np.arange(0, 10, 2)
print("\nnp.arange(): \n", array5)
