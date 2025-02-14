import pandas as pd

# create a dataframe
data = {'Name': ['SecUnit', 'Mensah', 'Ratthi', 'Pin-lee', 'Gurathin', 'Bharadwaj', 'Volescu'],
        'Age': [4, 40, 30, 35, 35, 45, 50],
        'Occupation': ['Security', 'Team Leader', 'Biology Specialist', 'Lawyer', 'Systems Specialist', 'Scientist', 'Scientist'], }

df = pd.DataFrame(data)

# display original dataframe
print("Original DataFrame:")
print(df)
print("\n")

# rename index
df.rename(index={0: 'a', 1: 'b', 2: 'c', 3: 'd',
          4: 'e', 5: 'f', 6: 'g'}, inplace=True)

# display updated dataframe
print("Updated DataFrame:")
print(df)
print("\n")
