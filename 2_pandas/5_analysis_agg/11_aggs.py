import pandas as pd

data = {
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Value1': [10, 15, 20, 25, 30, 35],
    'Value2': [5, 8, 12, 15, 18, 21]
}

df = pd.DataFrame(data)

agg_funcs = {

    # applying 'sum' to Value1 column
    'Value1': 'sum',

    # applying 'mean' and 'max' to Value2 column
    'Value2': ['mean', 'max']
}

result = df.groupby('Category').aggregate(agg_funcs)
print(result)
