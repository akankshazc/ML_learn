import pandas as pd

# create a categorical Series
data = ['A', 'B', 'A', 'C', 'B']
cat_series = pd.Series(data, dtype="category")

print(cat_series)
