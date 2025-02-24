import pandas as pd

# sample data
data = {'Color': ['Red', 'Green', 'Blue', 'Green', 'Red']}

# creating a DataFrame
df = pd.DataFrame(data)

# getting dummies without dropping any columns
dummies_all = pd.get_dummies(df['Color'])

# concatenating the dummies DataFrame with the original DataFrame
df_all = pd.concat([df, dummies_all], axis=1)

print("DataFrame with all dummy columns:")
print(df_all)
print("\n")

# getting dummies and dropping the first category column ('Blue' in this case)
dummies = pd.get_dummies(df['Color'], drop_first=True)

# concatenating the dummies DataFrame with the original DataFrame
df = pd.concat([df, dummies], axis=1)

print("DataFrame after dropping 'Blue':")
print(df)
