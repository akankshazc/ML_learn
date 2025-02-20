import pandas as pd

# define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)
print()

# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()

print("Cleaned Data:\n", df_cleaned)
