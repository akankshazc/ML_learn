import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10, 15, 20, 25, 30, 35]
}

df = pd.DataFrame(data)

# applying multiple aggregation functions to a single column
result = df.groupby('Category')['Value'].agg(['sum', 'mean', 'max', 'min'])
print(result)
