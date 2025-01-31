import numpy as np

first_array = np.array([1, 2, 3, 4, 5])
second_array = np.array([5, 4, 3, 2, 1])

# using the * operator
result1 = first_array * second_array
print("Using the * operator: ", result1)

# using the multiply() function
result2 = np.multiply(first_array, second_array)
print("Using the multiply() function: ", result2)
