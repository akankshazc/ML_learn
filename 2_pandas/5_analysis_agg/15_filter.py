import pandas as pd

# create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['HR', 'Marketing', 'Marketing', 'IT'],
        'Salary': [50000, 60000, 55000, 70000]}

df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# use the filter() method to select columns based on a condition
filtered_df = df.filter(items=['Name', 'Salary'])

# display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)
