import pandas as pd

# load the data
df = pd.read_csv('data1.csv')

# access the Name column
names = df['Name']

# print the names
print(names)
