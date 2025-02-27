import pandas as pd

# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['HR', 'Marketing', 'Marketing', 'IT'],
        'Salary': [50000, 60000, 55000, 70000]}

df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# use logical operators to filter
filtered_df = df[df.Salary > 55000]

# display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)
