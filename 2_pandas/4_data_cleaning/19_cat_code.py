import pandas as pd

# create a categorical Series
data = ['A', 'B', 'A', 'C', 'B']
cat_series = pd.Series(data, dtype="category")

# using .cat accessor
print(cat_series.cat.categories)
print(cat_series.cat.codes)
