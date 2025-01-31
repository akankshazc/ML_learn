import numpy as np

first_array = np.array([10, 20, 35, 42, 56])
second_array = np.array([3, 4, 6, 8, 10])

# Using the % operator
result1 = first_array % second_array
print("Using the % operator:", result1)

# using the mod() function
result2 = np.mod(first_array, second_array)
print("Using the mod() function:", result2)
