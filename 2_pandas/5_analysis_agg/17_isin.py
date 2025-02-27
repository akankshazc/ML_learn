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

# use isin() method
departments = ['HR', 'IT']
filtered_df = df[df.Department.isin(departments)]

# display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)
