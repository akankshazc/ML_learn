import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 22, 30, 22],
        'Score': [85, 90, 75, 80]}

df = pd.DataFrame(data)

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['Age', 'Score'])

print("Sorting by 'Age' (ascending) and then by 'Score' (ascending):\n")
print(df1.to_string(index=False))

print()

# 2. Sort DataFrame by 'Age' in ascending order, and then by 'Score' in descending order
df2 = df.sort_values(by=['Age', 'Score'], ascending=[True, False])

print("Sorting by 'Age' (ascending) and then by 'Score' (descending):\n")
print(df2.to_string(index=False))
