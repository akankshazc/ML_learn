import pandas as pd

# create a dictionary
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# create a series from the dict
s = pd.Series(data)

# create a series with custom index labels
s2 = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])

# display the series
print(s)
print(s2)
