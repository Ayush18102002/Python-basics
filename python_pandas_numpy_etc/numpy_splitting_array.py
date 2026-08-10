# spitting is reverrse operation of joinining
# joining mergers multiple arrays into one and splitting breaks one array into multiple

# we use array_split() for splitting arrays

import numpy as np
arr = np.array([1,2,3,4,5,6])
newarr = np.array_split(arr,3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

# the return values is a list contaiining three arrays


# if the array has less element then required,  it will adjust from the end accordinngly
newarr2 = np.array_split(arr,4)
print(newarr2)

# We also have the method split() available but it will not adjust the elements when elements are less in source array for splitting like in example above, array_split() worked properly but split() would fail.

# splitting 2-D arrays

arr2 = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr3 = np.array_split(arr2,3)
print(newarr3)


arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr4 = np.array_split(arr3,3)
print(newarr4)

newarr5 = np.array_split(arr3,3,axis = 1)
print(newarr5)

# an alternate solution is using hsplit() oppostite of hstack()

newarr6 = np.hsplit(arr3,3)
print(newarr6)

# similarl to alternate vstack() and dstack() are avaliable as vsplit() and dsplit()

newarr7 = np.vsplit(arr3,3)
print(newarr7)

newarr8 = np.dsplit(arr3,3)
print(newarr8)

