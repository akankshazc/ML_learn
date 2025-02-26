import pandas as pd

# sample data
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 50, 300, 120]}

df = pd.DataFrame(data)

# convert Category column to categorical type
df['Category'] = pd.Categorical(df['Category'])

# group by Category  and calculate the total sales
grouped = df.groupby('Category')['Sales'].sum()

print(grouped)
