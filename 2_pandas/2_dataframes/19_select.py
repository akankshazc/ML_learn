import pandas as pd

# Select Rows based on Specific Criteria

# read the data from the csv file
df = pd.read_csv('data1.csv')

# select rows where Age is greater than 25
selected_rows = df[df['Age'] > 25]

# print the rows
print(selected_rows)
