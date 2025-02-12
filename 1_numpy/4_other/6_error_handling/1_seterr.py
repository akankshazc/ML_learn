import numpy as np

# set behavior for division by zero to 'raise'
np.seterr(divide='raise')

# divide array1 by array2
array1 = np.array([1, 2, 3])
array2 = np.array([0, 2, 0])
result = np.divide(array1, array2)

print(result)
