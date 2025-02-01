import numpy as np

array1 = np.array([9, 12, 21])
array2 = np.array([21, 12, 9])

# use of less()
result = np.less(array1, array2)
print("Using less():", result)

# use of less_equal()
result = np.less_equal(array1, array2)
print("Using less_equal():", result)

# use of greater()
result = np.greater(array1, array2)
print("Using greater():", result)

# use of greater_equal()
result = np.greater_equal(array1, array2)
print("Using greater_equal():", result)

# use of equal()
result = np.equal(array1, array2)
print("Using equal():", result)

# use of not_equal()
result = np.not_equal(array1, array2)
print("Using not_equal():", result)
