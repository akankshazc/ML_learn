import pandas as pd

# create a DataFrame
data = {'Date': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02'],
        'Category': ['A', 'B', 'A', 'B'],
        'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

print("Original Dataframe:\n", df)

# pivot the  DataFrame
pivot_df = df.pivot(index='Date', columns='Category', values='Value')
print("Reshaped DataFrame:\n", pivot_df)
