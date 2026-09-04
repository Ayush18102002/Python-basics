# summations

"""
What is the difference between summation and addition?

Addition is done between two arguments whereas summation happens over n elements.


"""

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5])

newarr = np.add(arr1, arr2)

print(newarr)

# output: [ 2  4  6  8 10]

newarr1 = np.sum([arr1, arr2])

print(newarr1)

# output: 30

# summation over an axis

# if you specify axis =1 , Numpy will sum the numbers in each array and return an array with the sum of each array.

newarr2 = np.sum([arr1, arr2], axis=1)
print(newarr2)

# output: [15 15]

# cummulative summation

"""
Cummulative sum means partially adding the elements in array.

E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

Perfom partial sum with the cumsum() function.

"""
newarr3 = np.cumsum(arr1)
print(newarr3)

# output: [ 1  3  6 10 15]