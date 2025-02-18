import pandas as pd

# create a DataFrame
data = {'Date': ['2023-08-01', '2023-08-02'],
        'Category_A': [10, 20],
        'Category_B': [30, 40]}
df = pd.DataFrame(data)

# set 'Date' column as the index
df.set_index('Date', inplace=True)

# stack the columns into rows
stacked_df = df.stack()
print("Stack:\n", stacked_df)
print()

# unstack the rows back to columns
unstacked_df = stacked_df.unstack()
print("Unstack: \n", unstacked_df)
