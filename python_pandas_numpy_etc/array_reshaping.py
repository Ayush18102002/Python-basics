# reshaping arrays in numpy

# it means changing the shape of an array without changing its data. 
# The reshape() function in NumPy is used to give a new shape to an array without changing its data. 
# It returns a new view object if possible, otherwise it returns a copy of the original array with the new shape.

# reshape from 1-D to 2-D
# 

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4,3)

print(newarr)

# reshape from 1-D to 3-D

new_arr2 = arr.reshape(2, 3, 2)
print(new_arr2)

# can we reshape into any shape 
# yes, as long as the total number of elements remains the same.

#narr2   = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr2 = arr2.reshape(3,3) # it raise and error
# print(newarr2) # ValueError: cannot reshape array of size 8 into shape (3,3)

# return copy and view of an array

arr3 = np.array([1, 2, 3, 4, 5,6,7,8])
print(arr3.reshape(2,4).base)

# unknown dimension
# you are allowed to have one " unknown" dimension in the reshape method.
# Pass -1 as the value of one of the dimensions, and NumPy will calculate this

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr4 = arr4.reshape(2,2,-1)
print(newarr4)

# flattening the array
# flattening means converting a multidimensional array into a 1-D array.

arr5 = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr5.reshape(-1)
print(newarr)

