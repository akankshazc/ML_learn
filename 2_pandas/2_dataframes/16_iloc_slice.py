import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('data1.csv')

# slice rows from 1 to 4
slice_rows = df.iloc[1:5]

# slice columns from position 0 to 2
slice_columns = df.iloc[:, 0:3]

# display results
print("Slice Rows:")
print(slice_rows)

print("\nSlice Columns:")
print(slice_columns)
