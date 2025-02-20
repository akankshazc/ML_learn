import pandas as pd

# read the file using read_csv()
df = pd.read_csv("data.txt", sep='\s+', header=None,
                 names=['Patient', 'Age', 'Diagnosis'])

print(df)
