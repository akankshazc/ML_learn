import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('data1.csv')

# slice rows from index 1 to 3
slice_rows = df.loc[1:3]

print('Sliced rows:')
print(slice_rows)
print()

# slicing columns from 'Name' to 'Age'
slice_columns = df.loc[:, 'Name':'Age']

print('Sliced columns:')
print(slice_columns)
print()
