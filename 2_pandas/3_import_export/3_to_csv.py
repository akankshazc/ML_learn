import pandas as pd

# create a dictionary
data = {'Patient': ['John', 'Jane', 'Anne', 'Bob'],
        'Age': [25, 60, 35, 49],
        'Diagnosis': ['Schizophrenia', 'Diabetes', 'Depression', 'Hypertension']}

# create a DataFrame
df = pd.DataFrame(data)

# write dataframe to csv file
df.to_csv('data5.csv', sep=';', index=False, header=True)
