import pandas as pd

# create dataframe
data = {
    'Name': ['John', 'Anna', 'Johnny', 'Anna', 'John'],
    'Age': [28, 24, 28, 24, 19],
    'City': ['New York', 'Las Vegas', 'New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# check for duplicate entries in columns Name and Age
print(df.duplicated(subset=['Name', 'Age']))
