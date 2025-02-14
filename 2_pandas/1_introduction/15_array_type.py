import pandas as pd

# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

# creating a pandas.array of floating-point numbers
float_array = pd.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype='float')
print(float_array)
print()

# creating a pandas.array of strings
string_array = pd.array(['apple', 'banana', 'cherry', 'date'], dtype='str')
print(string_array)
print()

# creating a pandas.array of boolean values
bool_array = pd.array([True, False, True, False], dtype='bool')
print(bool_array)
print()
