import pandas as pd

# read the fixed-width file
df = pd.read_fwf('data.txt', colspecs=[(0, 4), (5, 7), (8, 25)], names=[
                 'Patient', 'Age', 'Diagnosis'])

print(df)
