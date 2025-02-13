import numpy as np

# create a datetime64 object for today
today = np.datetime64('today')

# add one day to today's date
tomorrow = today + np.timedelta64(1, 'D')

# create datetime64 objects for two dates
date1 = np.datetime64('2023-05-01')
date2 = np.datetime64('2023-04-01')

# calculate the number of days between the two dates
num_days = date1 - date2

# display the results
print("Today's date:", today)
print("Tomorrow's date:", tomorrow)
print("Number of days between", date1, "and", date2, "is", num_days)
