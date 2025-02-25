import pandas as pd

# create a regular Series
data = ['red', 'blue', 'green', 'red', 'blue']
series1 = pd.Series(data)

# convert the Series to a categorical Series using .astype()
categorical_s = series1.astype('category')

print(categorical_s)
