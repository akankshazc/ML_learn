import numpy as np

# create array of strings
array = np.array(['how', 'are', 'you', 'doing', 'today'])

# join the strings in the array using the dash as the delimiter
result = np.char.join('-', array)

print(result)
