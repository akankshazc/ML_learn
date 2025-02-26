import pandas as pd

# create a dataframe with a datetime column
df = pd.DataFrame({'datetime': ['2021-01-01', '2022-02-02', '2023-03-03']})

# convert the 'datetime' column to datetime type
df['datetime'] = pd.to_datetime(df['datetime'])

# extract year, month, and day into separate columns
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day

print(df)
