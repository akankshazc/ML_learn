import numpy as np

# create an array of integers from 1 to 10
a = np.arange(1, 11)

# to choose a random number from the array a
random_choice = np.random.choice(a)

print(random_choice)
