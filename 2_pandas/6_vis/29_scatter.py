import pandas as pd
import matplotlib.pyplot as plt

car = ["Caterham", "Tesla", "Audi", "BMW", "Ford", "Jeep"]
weight = [0.48, 1.7, 2, 2, 2.3, 3]

# create a DataFrame
data = {'Car': car, 'Weight': weight}
df = pd.DataFrame(data)

# scatter plot using Pandas
df.plot(x='Car', y='Weight', kind='scatter', marker='o', color='blue')
plt.xlabel('Car')
plt.ylabel('Weight')
plt.title('Car Weights (Scatter Plot)')
plt.grid(True)
plt.show()
