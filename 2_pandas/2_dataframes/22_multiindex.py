import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('data2.csv')

# sort the data by Series
df = df.sort_values(by='Series')

# create a multiindex
df = df.set_index(['Series', 'Book'])

# print the data
print(df)
