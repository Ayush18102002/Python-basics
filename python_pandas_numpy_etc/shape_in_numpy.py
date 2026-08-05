# shape
# numpy array have an attribute called shape that return a tuple with each index having the number of corresponding elements in that dimension

import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8]])   

print(arr.shape) # it will return (2,4) because there are 2 rows and 4 columns in the array


arr2 = np.array([1,2,3,4], ndmin=5)
print('shape of the array :' , arr2.shape)


# what does the shape tuple represent ?
#  integer at every index tells about the bnumber of element the corresponding dimension has
# In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.
