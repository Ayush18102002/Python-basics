# numpy

# it is a libarary to used for working with arrays
# it is used for working with numerical data and mathematical operations
# it also has function for working in domain of linear algebra , fourier transformation and matrics.


# we use numppy beacause it s faster and more efficient than python lists
# the array object in numpy is called ndarray
# numpy arrays are faster than python lists because they are stored at one continous place in memory unlike lists which are scattered in memory

"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

"""

# create a numpy ndarray object 
# numpy is used to work wit array. the array abject in numpy is called ndarray
# we can create ndarray using array() function that we already did above 

# dimeansion is array 

# a dimenson in array is one level of array depth(nested array)

# 0-D array - it also known as scalar because it contains only elements

"""
arr1 = np.array(42)
print(arr1)
"""

# 1-D array - an array that has 0-D arrays as its element is called uni-dimensional or 1-D array

"""
arr2 = np.array([2,8,9,4,2,4])
print(arr2)
""" 

# 2-D array - that has 1-D arrays as its elements is called a 2-D array
# these are often used to represent matrix or 2nd order tenson
# it represent row and columns

"""
arr3 = np.array([[1,2,3],[4,5,6]])
print(arr3)
"""

# 3-D array - an array that has 2-D arrays(matrices) as its elements is called 3-D array
# these are often used to represent a 3rd order tensor 

"""
arr4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr4)
"""

# check the number of dimensions

# we use ndim → tells you how many axes (levels of nesting) the array has. it means how many dimesion the array have 

# from the above codes 

"""
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim) 
"""

# higher dimensional arrays

# an array have any number of dimensons
# when the array is created you can define the number of dimensions by using the ndim argumnets

"""
arr5 = np.array([1,2,3,4], ndmin = 5)
print(arr5)
print(arr5.ndim)
print('number of dimesions : ', arr5.ndim) 
"""

# access array elements 
# you can acess an array elements by referring to its index number 
# the indexing starts with 0

"""
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr[0])
"""
# also we can perform negative indexing to access an array elements
"""
print(arr[-1]) # it will return the last element of the array
"""
# we can perform the addition , subtraction , multiplication and division of the array elements
"""
print(arr + 5) # it will add 5 to each element of the array
print(arr - 2) # it will subtract 2 from each element of the array
print(arr * 3) # it will multiply each element of the array by 3
print(arr / 2) # it will divide each element of the array by 2  

print(arr ** 2) # it will square each element of the array

print(arr[2] + arr[3]) # it will add the 2nd and 3rd element of the array
"""

# acessing the 2-D array 

# to access elements in a 2-D array, we use comma separated indices representing the dimension and the index of the element we want to access
"""
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d)
print(arr2d[0,1]) # it will return the element at row 0, column 1 (which is 2)
"""

# 3-D array 
# to acess elemets from 3-D arrays we can use comma seperated integers representing the dimensons and the index of the elements
"""
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0,1,2])
"""

# negative indexing in 2-D array
"""
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

"""
# slicing arrays 
# slicing in python means taking elements from one given index to another given index
# we can slice numpy arrays using the colon : operator
# we pass alice instead of index like this [start:end] . it will return the elements from start index to end index - 1
# we acn also define the step like this [start:end:step] . it will return the elements from start index to end index - 1 , with the given step

import numpy as np

arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
# negative slicing 
print(arr[-3:-1])
# using step in slicing
print(arr[1:5:2])
print(arr[::2])

# slicing 2-D arrays    
arr2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr2d[1, 1:4]) # it will return the elements from row 1, column 1 to column 3 (which is [7,8,9])
print(arr2d[0:2, 2]) # it will return the elements from row 0 to row 1, column 2 (which is [3,8])
print(arr2d[0:2, 1:4]) # it will return the elements from row 0 to row 1, column 1 to column 3

