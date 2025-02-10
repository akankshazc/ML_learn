import numpy as np

# create an array of data
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3])

# create bin to set the interval
bin = [0, 5, 10]

# create histogram
graph = np.histogram(data, bin)

print(graph)
