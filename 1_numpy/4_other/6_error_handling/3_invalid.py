import numpy as np

# set the invalid parameter to 'raise'
np.seterr(invalid='raise')

# try taking the square root of a negative number
x = np.sqrt(-1)
