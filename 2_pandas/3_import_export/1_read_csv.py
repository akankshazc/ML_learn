import pandas as pd

# read csv file with some arguments
df = pd.read_csv('data3.csv', header=None, names=[
                 'col1', 'col2', 'col3'], skiprows=2)

print(df)
