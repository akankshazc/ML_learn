import numpy as np

numbers = np.array([1.23456, 2.34567, 3.45678, 4.56789])

# round the array to two decimal places
rounded_array = np.round(numbers, 2)

print(rounded_array)

print("Array after floor():", np.floor(numbers))

print("Array after ceil():", np.ceil(numbers))
