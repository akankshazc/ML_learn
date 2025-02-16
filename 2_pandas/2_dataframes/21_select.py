import pandas as pd

# Select rows based on a List of Values

# read data from csv file
df = pd.read_csv('data1.csv')

# create a list of names to select
names = ['Mensah', 'Sirat', 'Gurathin']

# use isin() method to select rows based on a list of values
result = df[df['Name'].isin(names)]

print(result.to_string(index=False))
