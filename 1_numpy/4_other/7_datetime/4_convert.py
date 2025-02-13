import numpy as np
from datetime import datetime

# create a datetime object
dt = datetime(2023, 4, 29, 12, 34, 56)

# convert datetime to datetime64 object
dt64 = np.datetime64(dt)

# print the datetime64 object
print(dt64)
