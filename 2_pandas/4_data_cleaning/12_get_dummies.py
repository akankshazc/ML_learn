import pandas as pd

# create a Panda Series
data = pd.Series(['A', 'B', 'A', 'C', 'B'])

# using get_dummies on the Series
dummies = pd.get_dummies(data)

print(dummies)
