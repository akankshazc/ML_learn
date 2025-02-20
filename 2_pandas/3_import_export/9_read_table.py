import pandas as pd

# read the file using read_table()
df = pd.read_table("data.txt", sep='\s+',
                   names=['Patient', 'Age', 'Diagnosis'])

print(df)
