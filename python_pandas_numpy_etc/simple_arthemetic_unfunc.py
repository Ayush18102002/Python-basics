# Simple Arithemetic
"""
Simple Arithmetic
You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.

Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.

All of the discussed arithmetic functions take a where parameter in which we can specify that condition.


"""

# ADDITION
# The add() function sums the content of two arrays, and return the results in a new array.

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([4, 5, 6, 7])

newarr = np.add(arr1, arr2)

print(newarr)

# Subtraction
# The subtract() function subtracts the content of two arrays, and return the results in a

newarr2 = np.subtract(arr1, arr2)
print(newarr2)


# Multiplication
# The multiply() function multiplies the content of two arrays, and return the results in a
newarr3 = np.multiply(arr1, arr2)   
print(newarr3)

# Division
# The divide() function divides the content of two arrays, and return the results in a
newarr4 = np.divide(arr1, arr2)
print(newarr4)


# power 
# The power() function raises the content of two arrays, and return the results in a    
newarr5 = np.power(arr1, arr2)
print(newarr5)

# remainder
# The remainder() function returns the remainder of the division of the content of two arrays, and
# Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, and return the results in a new array.
newarr6 = np.remainder(arr1, arr2)
print(newarr6)    


# Quotient and MOd
# The modf() function returns the fractional and integral parts of the array as a separate array.
newarr7 = np.modf(arr1) 
print(newarr7)

# Absolute Values
# The absolute() function returns the absolute value of each element in the array.
newarr8 = np.absolute(arr1)
print(newarr8)