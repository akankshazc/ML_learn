import pandas as pd
import numpy as np

# Creating the DataFrame
data = {'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03', '2023-01-03'],
        'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles', 'Chicago'],
        'Temperature': [32, 75, 30, 77, np.nan, 76, np.nan]}
df = pd.DataFrame(data)

# create a pivot table
pivot_df = df.pivot_table(index='Date', columns='City', values='Temperature')

print("\nDefault Pivot Table\n", pivot_df)

# create a pivot table with dropna=True
pivot_df_dropna = df.pivot_table(
    index='Date', columns='City', values='Temperature', dropna=False)

print("\nPivot Table with dropna=False:\n", pivot_df_dropna)
