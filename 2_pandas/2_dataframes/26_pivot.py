import pandas as pd

# create a DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)
print("Original Dataframe:\n", df)

# create a pivot table
pivot_table_df = df.pivot_table(
    index='Category', values='Value', aggfunc='mean')
print("Reshaped Dataframe:\n", pivot_table_df)
