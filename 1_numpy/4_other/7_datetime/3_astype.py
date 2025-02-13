import numpy as np
from datetime import datetime

# create a datetime64 object
dt64 = np.datetime64('2023-04-29T12:34:56')

# convert datetime64 to datetime object
dt = dt64.astype(datetime)

# print the datetime object
print(dt)
