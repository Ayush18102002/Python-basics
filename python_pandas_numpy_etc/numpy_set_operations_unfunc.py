# numpy set operations

"""
What is a Set
A set in mathematics is a collection of unique elements.

Sets are used for operations involving frequent intersection, union and difference operations.

Create Sets in NumPy
We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.

"""

import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)

print(x)

# Finding Union
# To find the unique values of two arrays, use the union1d() method.


arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr2,arr3)
print(newarr)


"""
Finding Intersection
To find only the values that are present in both arrays, use the intersect1d() method.

"""

newarr1 = np.intersect1d(arr2,arr3, assume_unique=True)

print(newarr1)

"""
Note: the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
"""

"""
Finding Difference
To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.

"""

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr2 = np.setdiff1d(set1,set2,assume_unique=True)

print(newarr2)

"""
Note: the setdiff1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.

"""

"""
Finding Symmetric Difference
To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
"""
newarr3 = np.setxor1d(set1, set2, assume_unique=True)

print(newarr3)

"""
Note: the setxor1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
"""