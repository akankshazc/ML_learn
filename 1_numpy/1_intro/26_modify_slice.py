import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# modify elements from index 3 onwards (using start parameter)
numbers[3:] = 20
print(numbers)

# modify the first 3 elements (using stop parameter)
numbers[:3] = 40
print(numbers)

# modify elements from indices 2 to 5 (using start and stop parameter)
numbers[2:5] = 22
print(numbers)

# modify every second element from indices 1 to 5 (using start, stop, and step parameter)
numbers[1:5:2] = 16
print(numbers)
