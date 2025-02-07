import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# select a single element
simple_indexing = array1[5]

print("Simple Indexing:", simple_indexing)

# select multiple elements
fancy_indexing = array1[[1, 2, 5, 7, 0]]

print("Fancy Indexing:", fancy_indexing)
