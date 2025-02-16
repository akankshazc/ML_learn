import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('data1.csv')

# boolean indexing with .loc
boolean_index = df.loc[df['Age'] > 30]

print('Filtered DataFrame:')
print(boolean_index)
