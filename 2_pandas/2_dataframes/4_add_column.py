import pandas as pd

# Create a DataFrame
data = {'Name': ['SecUnit', 'Mensah', 'Ratthi', 'Pin-lee', 'Gurathin', 'Bharadwaj', 'Volescu', 'Perihelion', 'Iris', 'Seth', 'Martin',
                 'Kydi', 'Tariq', 'Three', 'Sirat'],
        'Age': [4, 40, 30, 35, 35, 45, 50, 19, 20, 42, 45, 38, 28, 7, 37],
        'Occupation': ['Security', 'Team Leader', 'Biology Specialist', 'Lawyer', 'Systems Specialist', 'Scientist', 'Scientist',
                       'Research Vessel', 'Mission Leader', 'Team Leader', 'Team Leader', 'Scientist', 'Mission Specialist', 'Security',
                       'Negotiator']}

df = pd.DataFrame(data)

# declare a new list
organization = ['PreservationAux', 'PreservationAux', 'PreservationAux', 'PreservationAux', 'PreservationAux', 'PreservationAux',
                'PreservationAux', 'University', 'University', 'University', 'University', 'University', 'University', 'University',
                'The Company']

# assign the list as a column to the DataFrame
df['Organization'] = organization

# print the DataFrame
print(df)
