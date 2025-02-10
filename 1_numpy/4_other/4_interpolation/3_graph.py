import numpy as np
import matplotlib.pyplot as plt

# arrays with random data points
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 3, 4, 5, 7, 8])

# generate evenly spaced values between the minimum and maximum x values
x_interp = np.linspace(x.min(), x.max(), 100)

# interp() to interpolate y values
y_interp = np.interp(x_interp, x, y)

# plot the original data points and the interpolated values
plt.plot(x, y, 'bo')
plt.plot(x_interp, y_interp, 'r-')

plt.show()
