import numpy as np

# create datetime64 objects for two dates
date1 = np.datetime64('2023-04-01')
date2 = np.datetime64('2023-05-01')

# calculate the number of business days between the two dates
num_business_days = np.busday_count(date1, date2)

# display the number of business days between the two dates
print("Number of business days between", date1,
      "and", date2, "is", num_business_days)
