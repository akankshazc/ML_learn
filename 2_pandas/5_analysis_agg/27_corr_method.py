import pandas as pd

# create dataframe
data = {
    "Temperature": [22, 25, 32, 28, 30],
    "Ice_Cream_Sales": [105, 120, 135, 130, 125]
}

df = pd.DataFrame(data)

# calculate different correlation coefficients
pearson = df['Temperature'].corr(df["Ice_Cream_Sales"])
kendall = df['Temperature'].corr(df["Ice_Cream_Sales"], method='kendall')
spearman = df['Temperature'].corr(df["Ice_Cream_Sales"], method='spearman')

# display different correlation coefficient
print(f"Pearson's Coefficient: {pearson}")
print(f"Kendall's Coefficient: {kendall}")
print(f"Spearman's Coefficient: {spearman}")
