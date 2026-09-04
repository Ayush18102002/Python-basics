# numpy products

# to find the product of an array, we can use the numpy.prod() function. This function computes the product of array elements over a given axis.

import numpy as np

arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)

# output: 24 because 1*2*3*4 = 24

# find the product of an array over a given axis

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

x1 = np.prod([arr1, arr2])
print(x1)

# output: [ 5 12 21 32] because 1*2*3*4*5*6*7*8 = 40320

# product over an axis 

# if you specify axis=1 , numpy will return the product of each row. If you specify axis=0, numpy will return the product of each column.

newarr = np.prod([arr1,arr2],axis=1)
print(newarr)

# output: [ 24 1680] because 1*2*3*4 = 24 and 5*6*7*8 = 1680


"""
Cummulative Product
Cummulative product means taking the product partially.

E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

Perfom partial sum with the cumprod() function.

"""

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)

# Returns: [5 30 210 1680]