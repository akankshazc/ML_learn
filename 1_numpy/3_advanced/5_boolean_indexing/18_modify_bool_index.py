import numpy as np

# create an array of numbers
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# make a copy of the array
numbers_copy = numbers.copy()

# change all odd numbers to 0 in the copy
numbers_copy[numbers % 2 != 0] = 0

# print the modified copy
print(numbers_copy)
