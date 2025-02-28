import pandas as pd

# create dataframe
data = {
    "Temperature": [22, 25, 32, 28, 30],
    "Ice_Cream_Sales": [105, 120, 135, 130, 125]
}

df = pd.DataFrame(data)

# calculate correlation matrix
print(df.corr())
