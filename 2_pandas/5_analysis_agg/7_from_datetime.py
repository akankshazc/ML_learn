import pandas as pd

# create a dataframe with a datetime column
df = pd.DataFrame({'datetime': ['2021-01-01', '2024-02-02', '2023-03-03']})

# convert the 'datetime' column to datetime type
df['datetime'] = pd.to_datetime(df['datetime'])

# get the day of the week
df['day_of_week'] = df['datetime'].dt.day_name()

# get the week of the year
df['week_of_year'] = df['datetime'].dt.isocalendar().week

# check for leap year
df['leap_year'] = df['datetime'].dt.is_leap_year

print(df)
