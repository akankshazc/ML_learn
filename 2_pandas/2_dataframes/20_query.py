import pandas as pd

# Select data using query() method

# read the data from the csv file
df = pd.read_csv('data1.csv')

# select rows with age > 25
selected_rows = df.query('Age > 25')

print(selected_rows.to_string(index=False))
