import pandas as pd
import matplotlib.pyplot as plt

# Create two DataFrames with different datasets
data1 = {'values': [12, 15, 18, 22, 25, 27, 30, 33, 37, 40]}
data2 = {'values': [8, 10, 14, 20, 24, 28, 32, 36, 42, 45]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Plot two histograms side by side
plt.hist(df1['values'], bins=6, edgecolor='black',
         alpha=0.7, label='Dataset 1')
plt.hist(df2['values'], bins=6, edgecolor='black',
         alpha=0.7, label='Dataset 2', color='orange')
plt.title('Histogram Comparison')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
