import numpy as np

# Array Statistical Functions

# create a numpy array
marks = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# calculate the mean of the array
mean = np.mean(marks)
print("Mean:", mean)

# calculate the median of the array
median = np.median(marks)
print("Median:", median)

# find the minimum and maximum values in the array
min_val = np.min(marks)
max_val = np.max(marks)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)

# calculate the standard deviation of the array
std_dev = np.std(marks)
print("Standard Deviation:", std_dev)

# calculate the variance of the array
variance = np.var(marks)
print("Variance:", variance)

# calculate the sum of the array
sum_val = np.sum(marks)
print("Sum:", sum_val)
