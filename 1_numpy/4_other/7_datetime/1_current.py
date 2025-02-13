import numpy as np

# get the current date and time
result = np.datetime64('now')

print("Current date and time:")
print(result)

# get the current date
date_today = np.datetime64('today', 'D')

print("Today's date:")
print(date_today)
