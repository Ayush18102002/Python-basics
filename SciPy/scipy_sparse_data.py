# what is sparse data

# sparse data is data that has mostly unused elements(elements that don't carry any information).
# it can be an array like this one 
# [1,0,2,0,2,3,0,0,0,0,0,0,0]

# sparse data : is a data set where most of the item values are zero.
# dense array : is the opposite of a sparse array: most of the values are not zero


# how to wrok with sparse data
# scipy has a module scipy.sparse that provodes functions to deal with sparse data

# how to work with sparse data
# it has a module scipy.sparse that provides func. to deal with sparse data
# there are 2 type of sparse matrices 
# csc - compressed sparse column. for efficient arithmetic, fast column slicing 
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products


# CSR Matrix
# We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix()

import numpy as np
from scipy.sparse import csr_matrix
arr = np.array([0,0,0,0,0,1,1,0,2])

print(csr_matrix(arr))

#sparse matrix methods
# viewing stored data(not the zero itmes) with the data property

arr2 = np.array([[0,0,0],[0,0,1],[1,0,2]])

print(csr_matrix(arr).data)

# counting nonzeros with the count_nonzero() method:
print(csr_matrix(arr).count_nonzero())

# removing zero-entries from the matrix with the eliminated_zeros() method:

mat = csr_matrix(arr2)
mat.eliminate_zeros()
print(mat)

# eliminating duplicte entries with the sum_duplicates() method:
mat1 = csr_matrix(arr2)
mat1.sum_duplicates()
print(mat1)


# Converting from csr to csc with the tocsc() method:


newarr = csr_matrix(arr2).tocsc()
print(newarr)

# Note: Apart from the mentioned sparse specific operations, sparse matrices support all of the operations that normal matrices support e.g. reshaping, summing, arithemetic, broadcasting etc.