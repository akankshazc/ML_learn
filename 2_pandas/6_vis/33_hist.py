import pandas as pd
import matplotlib.pyplot as plt

# create a DataFrame with more data
data = {'values': [23, 45, 30, 50, 67, 35, 47, 62, 25, 58, 42, 36, 53, 68, 32]}
df = pd.DataFrame(data)

# plot a customized histogram
plt.hist(df['values'], bins=7, edgecolor='black', color='green', alpha=0.7)
plt.title('Customized Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
