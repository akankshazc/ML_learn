import pandas as pd

# create a dataframe with date strings in custom format
df = pd.DataFrame({'date': ['2021/22/01', '2022/13/01', '2023/30/03']})

# convert the 'date' column to datetime with custom format
df['date'] = pd.to_datetime(df['date'], format='%Y/%d/%m')

print(df)
