import pandas as pd

# Create a DataFrame
data = {'Name': ['SecUnit', 'Mensah', 'Ratthi', 'Pin-lee', 'Gurathin', 'Bharadwaj', 'Volescu'],
        'Age': [4, 40, 30, 35, 35, 45, 50],
        'Occupation': ['Security', 'Team Leader', 'Biology Specialist', 'Lawyer', 'Systems Specialist', 'Scientist', 'Scientist'], }

df = pd.DataFrame(data)

# display the last 3 rows
print('Last 3 rows:')
print(df.tail(3))
print()

# display the last 5 rows
print('Last 5 rows:')
print(df.tail())
