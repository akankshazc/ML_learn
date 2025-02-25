import pandas as pd

# create a categorical Series
data = ['A', 'B', 'A', 'C', 'B']
cat_series = pd.Series(data, dtype="category")

# create a dictionary for renaming categories
category_mapping = {"A": "Category A", "B": "Category B", "C": "Category C"}

# rename categories using .rename_categories() and recreate the Series
cat_series_renamed = cat_series.cat.rename_categories(category_mapping)

print(cat_series_renamed)
