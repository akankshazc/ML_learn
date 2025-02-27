import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [28, 22, 25]}
# create a DataFrame with a non-sequential index
df = pd.DataFrame(data, index=[2, 0, 1])

print("Original DataFrame:")
print(df.to_string(index=True))
print("\n")

# sort DataFrame by index in ascending order
sorted_df = df.sort_index()

print("Sorted DataFrame by index:")
print(sorted_df.to_string(index=True))
