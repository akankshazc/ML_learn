import pandas as pd

# create a dataframe with date strings
df = pd.DataFrame({'date': ['2021-01-13', '2022-10-22', '2023-12-03']})

# convert the 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

print(df)
