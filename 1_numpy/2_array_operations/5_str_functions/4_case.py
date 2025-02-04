import numpy as np

array = np.array(['iNdiAn', 'jApan', 'AustraLia', 'GerMANY', 'frANCE'])

# convert all string elements in the array to upper case
result1 = np.char.upper(array)

# convert all string elements in the array to lower case
result2 = np.char.lower(array)

print("To Upper Case:", result1)
print("To Lower Case:", result2)
