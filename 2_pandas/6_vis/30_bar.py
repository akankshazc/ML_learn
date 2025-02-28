import pandas as pd
import matplotlib.pyplot as plt

car = ["Caterham", "Tesla", "Audi", "BMW", "Ford", "Jeep"]
weight = [0.48, 1.7, 2, 2, 2.3, 3]

# create a DataFrame
data = {'Car': car, 'Weight': weight}
df = pd.DataFrame(data)

# bar graph using Pandas
df.plot(x='Car', y='Weight', kind='bar', color='green')
plt.xlabel('Car')
plt.ylabel('Weight')
plt.title('Car Weights (Bar Graph)')
plt.tight_layout()
plt.show()
