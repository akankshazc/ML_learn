import pandas as pd

# sample data
data = {
    'A': [1, 2, 2, 3, 3, 4],
    'B': [5, 6, 6, 7, 8, 8]
}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df.to_string(index=False))

# detect duplicates
print("\nDuplicate Rows:\n", df[df.duplicated()].to_string(index=False))

# remove duplicates based on column 'A'
df.drop_duplicates(subset=['A'], keep='first', inplace=True)

print("\nDataFrame after removing duplicates based on column 'A':\n",
      df.to_string(index=False))
