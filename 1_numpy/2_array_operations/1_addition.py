import numpy as np

first_array = np.array([1, 2, 3, 5, 7, 11, 13, 17, 19, 23])
second_array = np.array([29, 31, 37, 41, 43, 47, 53, 59, 61, 67])

# using the + operator
result1 = first_array + second_array
print("Using the + operator: ", result1)

# using the add() function
result2 = np.add(first_array, second_array)
print("Using the add() function: ", result2)
