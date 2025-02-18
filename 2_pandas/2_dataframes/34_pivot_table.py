import pandas as pd

# create a dataframe
data = {'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'Delhi', 'Chennai', 'Delhi', 'Chennai'],
        'Country': ['USA', 'USA', 'USA', 'USA', 'India', 'India', 'India', 'India'],
        'Temperature': [32, 75, 30, 77, 75, 80, 78, 79]}
df = pd.DataFrame(data)

print("Original DataFrame\n", df)
print()

# create a pivot table with multiindex
pivot_df = df.pivot_table(
    index=['Country', 'City'], columns='Date', values='Temperature')

print("Reshaped DataFrame\n", pivot_df)
