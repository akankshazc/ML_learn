import pandas as pd

# Select Data using loc and iloc

# read data from csv file
df = pd.read_csv('data1.csv')

# print original DataFrame
print("Original DataFrame:")
print(df)
print()

# select rows 1 to 4 and columns Name and Age using loc
select_data_loc = df.loc[1:4, ['Name', 'Age']]

# print selected data using loc
print("Selected Data using loc:")
print(select_data_loc)
print()

# select rows 1 to 4 and columns 1 to 2 using iloc
select_data_iloc = df.iloc[1:5, 0:2]

# print selected data using iloc
print("Selected Data using iloc:")
print(select_data_iloc)
print()
