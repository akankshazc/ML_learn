import pandas as pd

# create a 2D list
data = [['SecUnit', 4, 'Security'],
        ['Mensah', 40, 'Team Leader'],
        ['Ratthi', 30, 'Biology Specialist'],
        ['Pin-lee', 35, 'Lawyer'],
        ['Gurathin', 35, 'Systems Specialist'],
        ['Bharadwaj', 45, 'Scientist'],
        ['Volescu', 50, 'Scientist']]

# create a DataFrame from the list
df = pd.DataFrame(data, columns=['Name', 'Age', 'Role'])

# print the DataFrame
print(df)
