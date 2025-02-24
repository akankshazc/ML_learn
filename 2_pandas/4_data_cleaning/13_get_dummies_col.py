import pandas as pd

# sample data
data = {'Color': ['Red', 'Green', 'Blue', 'Green', 'Red']}

# creating a DataFrame
df = pd.DataFrame(data)

# using get_dummies to convert the categorical column
dummies = pd.get_dummies(df['Color'])

# concatenating the dummies DataFrame with the original DataFrame
df = pd.concat([df, dummies], axis=1)

print(df)
