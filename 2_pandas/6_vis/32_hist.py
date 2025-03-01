import pandas as pd
import matplotlib.pyplot as plt

# create a DataFrame
data = {'values': [18, 21, 22, 25, 28, 30, 32, 34,
                   35, 36, 38, 40, 42, 45, 50, 55, 60, 65, 70]}
df = pd.DataFrame(data)

# plot a histogram
plt.hist(df['values'], bins=10)
plt.show()
