import pandas as pd

ages = pd.Series([28, 22, 25], name='Age')

# sort Series in ascending order
sorted_ages = ages.sort_values()

print(sorted_ages.to_string(index=False))
