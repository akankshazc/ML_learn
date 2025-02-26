import pandas as pd

# create a dataframe with date strings in day-first format
df = pd.DataFrame({'date': ['13-02-2021', '22-03-2022', '30-04-2023']})

# convert the 'date' column to datetime with day-first format
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

print(df)
