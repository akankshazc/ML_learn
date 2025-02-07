import numpy as np
import time

start = time.time()

array1 = np.array([1, 2, 3, 4, 5])

result = array1 + 10

end = time.time()

print("Vectorization time:", end - start)

start = time.time()

array2 = [1, 2, 3, 4, 5]

for i in range(len(array2)):
    array2[i] += 10

end = time.time()

print("For loop time:", end - start)
