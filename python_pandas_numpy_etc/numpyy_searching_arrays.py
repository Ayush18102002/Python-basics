# you can search arrays for certain value and return the indexes that get a match
# to search an array use the where() method

import numpy as np
arr  = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)
print(x) # (array([3, 5, 6],) which ,ean the value 4 present at index 3,5,6


# find the index which value  is odd

arr2 = np.array([10,14,93,41,8,7])
x1 = np.where(arr2%2==1)
print(x1)

# find the index which value is even 

x2 = np.where(arr2%2==0)
print(x2)

#search sorted 
# find the indexes wheere the value 7 should  be inserted
arr3 = np.array([6,7,8,9]) 
x3 = np.searchsorted(arr3,7)  # searchsorted() should we only works on the sorted array
print(x3)

# search from the right side  
# by deafault the left most index is returned but we can give side = 'right' to return the right most index instead

x4 = np.searchsorted(arr3,7,side = 'right')
print(x4)

# multiple values
# to search for more than one values , use an array with the specified value
arr4 = np.array([1,3,5,7])
x = np.searchsorted(arr4,[2,4,6])
print(x)

#The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.