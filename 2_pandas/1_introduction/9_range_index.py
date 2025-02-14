import pandas as pd

# create a dictionary of data
data = {'Name': ['SecUnit', 'Mensah', 'Ratthi', 'Pin-lee', 'Gurathin', 'Bharadwaj', 'Volescu'],
        'Age': [4, 40, 30, 35, 35, 45, 50],
        'Occupation': ['Security', 'Team Leader', 'Biology Specialist', 'Lawyer', 'Systems Specialist', 'Scientist', 'Scientist'], }

# create a range index
df = pd.DataFrame(data, index=pd.RangeIndex(
    start=1, stop=8, step=1, name='Index'))

# print the DataFrame
print(df)
