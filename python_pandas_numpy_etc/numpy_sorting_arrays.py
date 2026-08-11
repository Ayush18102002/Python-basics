# sorting means putting elements in an orderred sequence.
# ordered sequence is nay sequence that has an order corresponding to element, like numeric , aplhabetic , ascending or descending
# we ca use sort() function to sort the array

import numpy as np
arr = np.array([3,2,0,1])
print(np.sort(arr))
# this method returns a copy of the array , leaving the original array unchanged 


# we can sort array of string 

arr1 = np.array(['banana', 'cheery', 'apple'])
print(np.sort(arr1))


# sort boolean 

arr2 = np.array([True, False, True])
print(np.sort(arr2))


# sorting 2-D array

arr3 = np.array([[3,2,4],[5,0,1]])
print(np.sort(arr3))