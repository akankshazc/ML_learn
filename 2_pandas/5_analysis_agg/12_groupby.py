import pandas as pd

# create a dictionary containing the data
data = {'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing'],
        'Sales': [1000, 500, 800, 300]}

# create a DataFrame using the data dictionary
df = pd.DataFrame(data)

# group the DataFrame by the Category column and
# calculate the sum of Sales for each category
grouped = df.groupby('Category')['Sales'].sum()

# print the grouped data
print(grouped)
