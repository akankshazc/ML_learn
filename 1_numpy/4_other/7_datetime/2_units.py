import numpy as np

# use datetime64() for different time units
year = np.datetime64('2023', 'Y')
month = np.datetime64('2023-04', 'M')
day = np.datetime64('2023-04-29', 'D')
hour = np.datetime64('2023-04-29T10', 'h')
minute = np.datetime64('2023-04-29T10:30', 'm')
second = np.datetime64('2023-04-29T10:30:15', 's')

print("Year: ", year)
print("Month: ", month)
print("Day: ", day)
print("Hour: ", hour)
print("Minute: ", minute)
print("Second: ", second)
