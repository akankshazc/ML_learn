import numpy as np

# create two arrays of strings
array1 = np.array(['mensah', 'ratthi', 'gurathin', 'secunit'])
array2 = np.array(['pin-lee', 'ratthi', 'gurathin', 'bharadwaj'])

# check if each element of the arrays is equal
result = np.char.equal(array1, array2)

print(result)
