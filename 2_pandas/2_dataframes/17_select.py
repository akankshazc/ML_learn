import pandas as pd

# Select Data using Indexing and Slicing

# Read the data from the CSV file
df = pd.read_csv('data1.csv')

# select a single column
name_column = df['Name']

print('Selecting a single column:')
print(name_column)
print()

# select multiple columns
name_and_age_columns = df[['Name', 'Age']]

print('Selecting multiple columns:')
print(name_and_age_columns)
print()

# selecting rows using slicing
selected_rows = df[1:5]

print('Selecting rows 1 to 4 using slicing:')
print(selected_rows.to_string(index=False))
print()
