import pandas as pd

# create a categorical Series
data = ['A', 'B', 'A', 'C', 'B']
cat_series = pd.Series(data, dtype="category")

# add new categories and reassign the variable
new_categories = ['D', 'E']
cat_series = cat_series.cat.add_categories(new_categories)

print(cat_series)
