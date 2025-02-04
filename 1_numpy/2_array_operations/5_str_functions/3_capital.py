import numpy as np

# define array with 3 string elements
array = np.array(['apple', 'banana', 'cherry'])

# capitalize the first letter of each string in array
result = np.char.capitalize(array)

print(result)
