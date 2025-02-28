import pandas as pd
import numpy as np

# create a dataframe
data = {
    "Temperature": [22, 25, 32, 28, 30],
    "Coffee_Sales": [158, 145, np.nan, np.nan, 140]
}

df = pd.DataFrame(data)

# calculate correlation between Temperature and Ice_Cream_sales
correlation1 = df["Temperature"].corr(df["Coffee_Sales"])

print("With NaN values")
print(df)
print(f"correlation = {correlation1}")
print()

# remove missing values
df.dropna(inplace=True)

# calculate correlation between Temperature and Ice_Cream_sales
correlation2 = df["Temperature"].corr(df["Coffee_Sales"])

print("Without NaN values")
print(df)
print(f"correlation = {correlation2}")
print()
