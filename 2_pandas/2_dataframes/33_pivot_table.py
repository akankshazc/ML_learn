import pandas as pd

data = {'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
        'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'Temperature': [32, 75, 30, 77, 33, 78],
        'Humidity': [80, 10, 85, 5, 81, 7]}

df = pd.DataFrame(data)

# calculate mean temperature for each city using pivot_table()
mean_temperature = df.pivot_table(
    index='City', values='Temperature', aggfunc='mean')

print(mean_temperature)
