import pandas as pd

# Create a DataFrame
data = {'Name': ['SecUnit', 'Mensah', 'Ratthi', 'Pin-lee', 'Gurathin', 'Bharadwaj', 'Volescu', 'Perihelion', 'Iris', 'Seth', 'Martin',
                 'Kydi', 'Tariq', 'Three', 'Sirat'],
        'Age': [4, 40, 30, 35, 35, 45, 50, 19, 20, 42, 45, 38, 28, 7, 37],
        'Occupation': ['Security', 'Team Leader', 'Biology Specialist', 'Lawyer', 'Systems Specialist', 'Scientist', 'Scientist',
                       'Research Vessel', 'Mission Leader', 'Team Leader', 'Team Leader', 'Scientist', 'Mission Specialist', 'Security',
                       'Negotiator']}

df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame")
print(df)
print()

# delete age column
df.drop('Age', axis=1, inplace=True)

# display the modified DataFrame
print("Modified DataFrame")
print(df)
