# joining numpy arrays
# it means putting contents of two or more arrays in a single array
# in sql we join tables based on a ley whereas in numpy we join arrays by axes
# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

import numpy as np

# joining of the 1-D array

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr =  np.concatenate((arr1,arr2))

print(arr)

#  joining of 2-D array

arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[5,6],[7,8]])

arr5 = np.concatenate((arr3,arr4), axis = 1) # axis  represent the row 

print(arr5)

# joining array using stack function
# stack() function is used to join a sequence of arrays along a new axis
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.

arr6 = np.array([1,2,3])
arr7 = np.array([4,5,6])

arr8 = np.stack((arr6,arr7), axis = 1)

print(arr8)
print("\n")

# numpy provides a helper function hstack() to stack along rows 
# numpy provides a helper function vstack() to stack along columns
# dstack() is used to stack along height which is same as depth

arr9 = np.hstack((arr6,arr7))
print(arr9)

arr10 = np.vstack((arr6,arr7))
print(arr10)

arr11 = np.dstack((arr6,arr7))
print(arr11)

