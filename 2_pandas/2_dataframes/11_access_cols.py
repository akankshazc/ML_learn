import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('data1.csv')

# access multiple columns
name_age = df[['Name', 'Age']]

print(name_age)
