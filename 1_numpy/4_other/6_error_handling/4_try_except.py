import numpy as np

array1 = np.array([1, 4, 3])
array2 = np.array([0, 2, 0])

# try to divide the arrays
try:
    result = array1/array2

except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")
