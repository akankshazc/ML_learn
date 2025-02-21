import pandas as pd
import numpy as np

# create a dataframe with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, 5],
    'D': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)

# replace missing values with mean
df['A'].fillna(value=df['A'].mean(), inplace=True)

# replace missing values with median
df['B'].fillna(value=df['B'].median(), inplace=True)

# replace missing values with mode
df['C'].fillna(value=df['C'].mode()[0], inplace=True)

print(df)
