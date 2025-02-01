import numpy as np

x1 = np.array([True, False, True])
x2 = np.array([False, False, True])

# Logical AND
print(np.logical_and(x1, x2))

# Logical OR
print(np.logical_or(x1, x2))

# Logical NOT
print(np.logical_not(x1))
