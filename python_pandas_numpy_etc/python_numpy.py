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

"""
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
"""

# numpy data types
# string data type in numpy is called str_ or string_ . it is used to represent text data. it can be used to represent both fixed-length and variable-length strings. the default length of a string is 1 character. we can specify the length of a string by using the dtype argument when creating an array. we can also use the numpy.char module to perform various string operations on numpy arrays.
# integer data type in numpy is called int_ or intc . it is used to represent integer data. it can be used to represent both signed and unsigned integers. the default size of an integer is 4 bytes. we can specify the size of an integer by using the dtype argument when creating an array. we can also use the numpy.int32 and numpy.int64 data types to represent 32-bit and 64-bit integers respectively.
# floating point data type in numpy is called float_ or floatc . it is used to represent floating point data. it can be used to represent both single-precision and double-precision floating point numbers. the default size of a floating point number is 8 bytes. we can specify the size of a floating point number by using the dtype argument when creating an array. we can also use the numpy.float32 and numpy.float64 data types to represent 32-bit and 64-bit floating point numbers respectively.
# boolean data type in numpy is called bool_ . it is used to represent boolean data. it can be used to represent both True and False values. the default size of a boolean value is 1 byte. we can specify the size of a boolean value by using the dtype argument when creating an array. we can also use the numpy.bool8 data type to represent 8-bit boolean values.
# complex data type in numpy is called complex_ or complexc . it is used to represent complex numbers. it can be used to represent both single-precision and double-precision complex numbers. the default size of a complex number is 16 bytes. we can specify the size of a complex number by using the dtype argument when creating an array. we can also use the numpy.complex64 and numpy.complex128 data types to represent 64-bit and 128-bit complex numbers respectively.



import numpy as np
arr = np.array([1,2,3,4])
print(arr.dtype)

arr1 = np.array(['apple','banana','cherry'])

print(arr1.dtype) # <class 'numpy.str_'>


# creating array with difine data types
# dtype also use to define the data type of the array when creating it. we can use the dtype argument to specify the data type of the array. we can also use the numpy.astype() method to change the data type of an existing array.

arr2 = np.array([1,2,3,4], dtype = 'S') # S means string data type
print(arr2)
print(arr2.dtype)

# for i,u,f,S and U we can define size as well

arr3 = np.array([1,2,3,4], dtype = 'i4')
print(arr3)
print(arr3.dtype)

# what if a values can not be converted - then numpy will raise valueerror

# arr4 = np.array(['apple','banana','cherry'], dtype = 'i4') # it will raise valueerror because string can not be converted to integer
# print(arr4)
# print(arr4.dtype)

#converting data type on existing arrays 
# the best way to change the data type of an existing array is to use the astype() method. it creates a new array and does not change the original array.

arr5 = np.array([1.1,2.2,3.3,4.4])

new_arr = arr5.astype('i') # it will convert the float data type to integer data type
print(new_arr)
print(new_arr.dtype)

# we can pass int paramter instead of 'i'


arr6 = np.array([1.1,2.1,3.1])

new_arr1 = arr6.astype(int)
print(new_arr1)
print(new_arr.dtype)

new_arr2 = arr6.astype(bool)
print(new_arr2)
print(new_arr2.dtype)