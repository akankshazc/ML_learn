import numpy as np

# create a 3D array with shape (2, 3, 4)
array1 = np.array([[[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]],

                   [[13, 14, 15, 16],
                    [17, 18, 19, 20],
                    [21, 22, 23, 24]]])

# access a specific element of the array
element = array1[1, 2, 1]

# print the value of the element
print(element)
