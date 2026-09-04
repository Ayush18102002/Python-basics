#rounding decimmals

"""
Rounding Decimals
There are primarily five ways of rounding off decimals in NumPy:

truncation
fix
rounding
floor
ceil



"""

# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

import numpy as np

arr = np.trunc([-3.1666, -2.5666, 0, 2.5666, 3.1666])

print(arr)

# using fix() function

arr2 = np.fix([-3.1666, -2.5666, 0, 2.5666, 3.1666])
print(arr2)

# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.

# E.g. round off to 1 decimal point, 3.16666 is 3.2

arr3 = np.around([-3.1666, -2.5666, 0, 2.5666, 3.1666], decimals=1)
print(arr3)

# floor() function rounds off to the nearest integer less than or equal to the input value.
arr4 = np.floor([-3.1666, -2.5666, 0, 2.5666, 3.1666])
print(arr4)

# ceil() function rounds off to the nearest integer greater than or equal to the input value.
arr5 = np.ceil([-3.1666, -2.5666, 0, 2.5666, 3.1666])
print(arr5)

