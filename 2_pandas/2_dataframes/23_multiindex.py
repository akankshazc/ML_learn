import pandas as pd

# Access rows with Multiindex

# read data from csv
df = pd.read_csv('data2.csv')

# sort the data by series
df = df.sort_values(by='Series')

# set the index to 'Series' and 'Book'
df = df.set_index(['Series', 'Book'])

# access all entries under 'The Expanse'
expanse = df.loc['The Expanse']

# access all entries under 'Ancillary Justice'
ancillary = df.loc[('Imperial Radch', 'Ancillary Justice')]

print('The Expanse:')
print(expanse)
print('\nAncillary Justice:')
print(ancillary)
