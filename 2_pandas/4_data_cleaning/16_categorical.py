import pandas as pd

data = ['red', 'blue', 'green', 'red', 'blue']

# create a categorical column
categorical_data = pd.Categorical(data)

print(categorical_data)
