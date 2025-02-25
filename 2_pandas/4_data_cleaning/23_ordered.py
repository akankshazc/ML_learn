import pandas as pd

# create an ordered categorical Series
data = ['low', 'medium', 'high', 'low', 'medium']
ordered_cat_series = pd.Categorical(
    data, categories=['low', 'medium', 'high'], ordered=True)

# check if the categorical variable is ordered
is_ordered = ordered_cat_series.ordered

print("Is ordered:", is_ordered)
