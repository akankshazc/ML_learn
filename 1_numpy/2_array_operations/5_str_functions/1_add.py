import numpy as np

array1 = np.array(['iPhone: ', 'price: '])
array2 = np.array(['15', '$900'])

# perform element-wise array string concatenation
result = np.char.add(array1, array2)

print(result)
