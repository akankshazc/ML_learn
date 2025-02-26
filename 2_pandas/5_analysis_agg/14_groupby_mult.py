import pandas as pd

# create a DataFrame with student data
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Grade': ['A', 'B', 'A', 'A', 'B'],
    'Score': [90, 85, 92, 88, 78]
}

df = pd.DataFrame(data)

# define the aggregate functions to be applied to the Score column
agg_functions = {
    # calculate both mean and maximum of the Score column
    'Score': ['mean', 'max']
}

# group the DataFrame by Gender and Grade, then apply the aggregate functions
grouped = df.groupby(['Gender', 'Grade']).aggregate(agg_functions)

# print the resulting grouped DataFrame
print(grouped)
