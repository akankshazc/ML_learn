import pandas as pd

# define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],
    'B': [None, 2, 3, 4, 5],
    'C': [1, 2, None, None, 5]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)
