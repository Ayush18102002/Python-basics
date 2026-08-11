# getting some elements out of an existing array and creating a new array out of them is called filtering 
# in numpy you can filter an array using a boolean index list

# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

import numpy as np
arr = np.array([41,42,43,44])
x = [True, False, True, False]

newarr = arr[x]
print(newarr)

# creating the filter array

# creating the filtere array that will return only values highr than 42

filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr1 = arr[filter_arr]
print(filter_arr)
print(newarr1)

# creating a filter arrrau that will return only even elements from the original array

arr2 = np.array([1,2,3,4,5,6,7])

filter_arr2 = []

for i in arr2:
    if i%2==0:
        filter_arr2.append(True)
    else:
        filter_arr2.append(False)
        
newarr2 = arr2[filter_arr2]
print(filter_arr2)
print(newarr2)

# creating filter directly from array

filter_arr3 = arr2 % 2 == 0
newarr3 = arr2[filter_arr3]
print(filter_arr3)
print(newarr3)


filter_arr4 = arr > 42
newarr4 = arr[filter_arr4]
print(filter_arr4)
print(newarr4)