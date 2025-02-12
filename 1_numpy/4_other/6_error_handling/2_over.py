import numpy as np

# set behavior for floating-point overflow to 'raise'
np.seterr(over='raise')

calc1 = np.exp(1000)

print(calc1)
