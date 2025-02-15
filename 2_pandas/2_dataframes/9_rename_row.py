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

# rename column one index labels
df.rename(index={0: 'First', 1: 'Second', 2: 'Third', 3: 'Fourth', 4: 'Fifth', 5: 'Sixth', 6: 'Seventh', 7: 'Eighth', 8: 'Ninth', 9: 'Tenth',
                 10: 'Eleventh', 11: 'Twelfth', 12: 'Thirteenth', 13: 'Fourteenth', 14: 'Fifteenth'}, inplace=True)

# display the DataFrame after renaming the column index labels
print("DataFrame after renaming the column index labels")
print(df)
