import pandas as pd

# read the data from json file
df = pd.read_json('data.json', orient='records')

# print the data
print(df)
