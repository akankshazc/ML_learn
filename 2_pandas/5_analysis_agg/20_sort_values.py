import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [28, 22, 25]}
df = pd.DataFrame(data)

# sort DataFrame by Age in ascending order
sorted_df = df.sort_values(by='Age')

print(sorted_df.to_string(index=False))
