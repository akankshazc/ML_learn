import pandas as pd

# create a dictionary
data = {'Patient': ['John', 'Jane', 'Anne', 'Bob', 'Jacob'],
        'Age': [25, 60, 35, 49, 30],
        'Diagnosis': ['Schizophrenia', 'Diabetes', 'Depression', 'Hypertension', 'Asthma']}

# create a DataFrame
df = pd.DataFrame(data)

# write dataframe to json file
df.to_json('data2.json', orient='records', indent=4)
