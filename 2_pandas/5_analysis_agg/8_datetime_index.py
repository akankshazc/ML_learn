import pandas as pd

# create a list of datetime values
dates = ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05']

# create a DataFrame with a DateTimeIndex
df = pd.DataFrame({'values': [10, 20, 30, 40, 50]},
                  index=pd.to_datetime(dates))

print(df)
