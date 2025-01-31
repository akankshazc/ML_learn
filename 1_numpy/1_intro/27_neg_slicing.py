import numpy as np

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])

# slice the last 3 elements of the array
# using the start parameter
print(numbers[-3:])

# slice elements from 2nd-to-last to 4th-to-last element
# using the start and stop parameters
print(numbers[-5:-2])

# slice every other element of the array from the end
# using the start, stop, and step parameters
print(numbers[-1::-2])
