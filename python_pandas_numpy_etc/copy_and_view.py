# copy and view in numpy
# the difference between a copy and a view is that the copy is a new array, and the view is just a view of the original array. 
# The copy owns the data and any changes made to the copy will not affect the original array, and any changes made to the original array will not affect the copy. 
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

import numpy as np
arr = np.array([1,2,3,4,5])

x = arr.copy() # it will create a copy of the original array
y = arr.view() # it will create a view of the original array

arr[0] = 42

print(arr)
print(x) # in the copy the original array is not affected
print(y) # in the view the original array is affected because it is just a view of the original array

# check if array owns its data 
# the base attribute is used to check if an array owns its data
print(x.base) # None because the copy owns its data
print(y.base) # <class 'numpy.ndarray'> because the view does not own its data
