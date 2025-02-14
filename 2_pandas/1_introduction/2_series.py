import pandas as pd

# create a list
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# create a series with custom index labels
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# display the series
print(s)

# index labels in the series
print(s['c'])
