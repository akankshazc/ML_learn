import pandas as pd

# create a sample dataframe with mixed date formats
df = pd.DataFrame({'date': ['2022-12-01', '01/02/2022',
                  '2022-03-23', '03/02/2022', '3 4 2023', '2023.9.30']})

# convert the date column to datetime format
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)

print(df)
