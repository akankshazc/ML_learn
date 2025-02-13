import matplotlib.pyplot as plt
import numpy as np

car = np.array(["Caterham", "Tesla", "Audi",  "BMW", "Ford", "Jeep"])
weight = np.array([0.48, 1.7, 2, 2, 2.3, 3])

# create a bar graph
plt.bar(car, weight)

plt.title('Bar Graph')

plt.show()
