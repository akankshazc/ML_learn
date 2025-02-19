import pandas as pd

# read the json file not in dictionary format
# orient = 'values' means that the file contains array of arrays
df = pd.read_json('data1.json', orient='values', lines=False)

# print the data
print(df)
