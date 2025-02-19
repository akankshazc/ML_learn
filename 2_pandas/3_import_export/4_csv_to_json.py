import pandas as pd

# read the csv file
df = pd.read_csv('data4.csv')

# convert to JSON
# orient='records' means that each row is converted to a dictionary
df.to_json('data.json', orient='records', indent=4)

# print the json output in the console
print(df.to_json(orient='records', indent=4))
