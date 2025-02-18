import pandas as pd

# create dataframe
data = {
    'Name': ['John', 'Anna', 'John', 'Anna', 'John'],
    'Age': [28, 24, 28, 24, 19],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# remove duplicates, keep last entries
df.drop_duplicates(keep='last', inplace=True)

print(df)
