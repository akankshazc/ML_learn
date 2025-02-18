import pandas as pd

# create a sample DataFrame
data = {'Name': ['Alice', 'Bob'],
        'Math': [90, 85],
        'History': [75, 92]}
df = pd.DataFrame(data)

# melt the DataFrame
melted_df = pd.melt(df, id_vars='Name', var_name='Subject', value_name='Score')

print(melted_df)
