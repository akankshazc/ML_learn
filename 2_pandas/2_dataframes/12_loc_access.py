import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('data1.csv')

# access a single row
secunit = df.iloc[0]

# print the row
print('Single row:')
print(secunit)
print()

# acess multiple rows
row_list = df.loc[[0, 3, 5]]

# print the rows
print('Multiple rows:')
print(row_list)
print()

# access a list of columns
column_list = df.loc[:, ['Name', 'Age']]

# print the columns
print('List of columns:')
print(column_list)
print()

# access second row of the first column
specific_value = df.loc[1, 'Name']

# print the value
print('Specific value:')
print(specific_value)
