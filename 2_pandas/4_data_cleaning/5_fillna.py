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

# replace missing values with 0
df.fillna(value=0, inplace=True)

print(df)
