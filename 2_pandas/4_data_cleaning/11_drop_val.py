import pandas as pd

# create dataframe
data = {
    'Name': ['John', 'Michael', 'Tom', 'Alex', 'Ryan'],
    'Age': [8, 9, 7, 8, 10],
    'Gender': ['M', 'M', 'M', 'M', 'M'],
    'Standard': [3, 4, 12, 3, 5]
}
df = pd.DataFrame(data)

# remove mistaken values
for i in df.index:
    if df.loc[i, 'Standard'] > 8:
        df.drop(i, inplace=True)

print(df)
