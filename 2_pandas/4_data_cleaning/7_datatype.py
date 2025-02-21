import pandas as pd

# create dataframe
data = {
    'Country': ['USA', 'Canada', 'Australia', 'Germany', 'Japan'],
    'Date': ['2023-07-20', '2023-07-21', '2023-07-22', '2023-07-23', '2023-07-24'],
    'Temperature': [25.5, '28.0', 30.2, 22.8, 26.3]
}
df = pd.DataFrame(data)

# convert temperature column to float
df['Temperature'] = df['Temperature'].astype(float)

# calculate the mean temperature
mean_temperature = df['Temperature'].mean()

print(mean_temperature)
