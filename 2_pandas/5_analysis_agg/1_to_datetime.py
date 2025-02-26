import pandas as pd

# create a datetime string
date_string = '2001-12-24 12:38'

print("String:", date_string)

# convert string to datetime
date = pd.to_datetime(date_string)

print("DateTime:", date)
print(type(date))
