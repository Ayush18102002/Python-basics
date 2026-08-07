# iterating in numpy array
# it means going through elements one by one

import numpy as np
arr = np.array([1,2,3,4,5])
for x in arr:
    print(x)
print(" one line output : ", end = " complete")
print("\n")
# in 2-D array we can iterate through each element one by one using 2 for loops

arr1 = np.array([[1,2,3],[4,5,6]])
for x in arr1:
    for y in x:
        print(y)
print(" one line output : ", end = " complete")
print("\n")

# we can also iterate using only  one for loop

for x in arr1:
    print(x)
print(" one line output : ", end = " complete")
print("\n")


# on 3-D array we can iterate through each element one by one using 3 for loops

arr2 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr2:
    for y in x:
        for z in y:
            print(z)
print(" one line output : ", end = " complete")
print("\n")

for x in arr2:
    for y in x:
        print(y)
    print(y)
print(" one line output : ", end = " complete")
print("\n")


# iterating array using nditer() function
# nditer() function is a efficient way to iterate over an array
# in basic for loops , iteration happens in the first dimension and it is not efficient for multi-dimensional arrays'

for x in np.nditer(arr2): # nditer slove the multi dimensional loops problem 
    print(x)
print(" one line output : ", end = " complete")
print("\n")

# we can use this on the 2-D array also
for x in np.nditer(arr1):
    print(x)
print(" one line output : ", end = " complete")
print("\n")

# iterating array with differet data types using nditer() function
# we can use nditer() function to iterate over an array with different data types
# op_dtypes() is used to specify the data type of the output array so we can change the data type of element while iterating
# flags = ['buffered'] is used to make sure that the data is buffered before it is converted to the specified data type its like a extra space

for x in np.nditer(arr, flags = ['buffered'], op_dtypes = ['S']):
    print(x)

# we can use filter and followed buiteration

arr2 = np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr2[:, ::2]):
    print(x)

# eunumerated iteraton using ndenumerate() function
# ndenumerate() function is used to iterate over an array and return the index and the value of each element

arr3 = np.array([1,2,3])
for idx,x in np.ndenumerate(arr3): # idx is the index of the element and x is the value of the element
    print(idx, x)

# on 2-D array we can use ndenumerate() function to iterate over an array and return the index and the value of each element

arr4 = np.array([[1,2,3],[4,5,6]])
for idx, x in np.ndenumerate(arr4):
    print(idx, x)


