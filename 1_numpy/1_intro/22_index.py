import numpy as np

array1 = np.array([1, 3, 5, 7, 9])

# access numpy elements using index
print(array1[0])    # prints 1
print(array1[2])    # prints 5
print(array1[4])    # prints 9

# create a numpy array
numbers = np.array([2, 4, 6, 8, 10])

# change the value of the first element
numbers[0] = 12
print("After modifying first element:", numbers)

# change the value of the third element
numbers[2] = 14
print("After modifying third element:", numbers)

# access the last element
print(numbers[-1])

# access the second-to-last element
print(numbers[-2])

# modify the last element
numbers[-1] = 13
print(numbers)

# modify the second-to-last element
numbers[-2] = 17
print(numbers)
