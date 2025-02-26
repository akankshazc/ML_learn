import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# calculate total sum of the Value column
total_sum = df['Value'].aggregate('sum')
print("Total Sum:", total_sum)

# calculate the mean of the Value column
average_value = df['Value'].aggregate('mean')
print("Average Value:", average_value)

# calculate the maximum value in the Value column
max_value = df['Value'].aggregate('max')
print("Maximum Value:", max_value)
