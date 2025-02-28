import pandas as pd
import matplotlib.pyplot as plt

weight = [0.48, 1.7, 2, 3]

# create a DataFrame
data = {'Weight': weight}
df = pd.DataFrame(data)

# histogram using Pandas
df['Weight'].plot(kind='hist', bins=10, edgecolor='black', color='blue')
plt.show()
