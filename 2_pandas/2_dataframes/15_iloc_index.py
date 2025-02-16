import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('data1.csv')

# access single row
single_row = df.iloc[0]

# access multiple rows
multiple_rows = df.iloc[[0, 3, 4]]

# access columns 0 and 2
column_list = df.iloc[:, [0, 2]]

# access specific value
specific_value = df.iloc[1, 1]

# display the results
print("Single row:")
print(single_row)

print("\nMultiple rows:")
print(multiple_rows)

print("\nColumns 0 and 2:")
print(column_list)

print("\nSpecific value:")
print(specific_value)
