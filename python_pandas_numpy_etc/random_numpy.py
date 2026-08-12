# # random number does not mean a different number every time . random means something that can not be predicted logically

# pseudo random and true random
# Random numbers generated through a generation algorithm are called pseudo random.

# generate random number 

# numpy offers the random modue to work with random numbers

from numpy import random
# it generate a rondom integer from 0 to 100.
x=  random.randint(100)
print(x)    

# generate a random float 
# we use rand() for float 

x1 = random.rand()
print(x1)

# generate random array
# we can generate an array
# the randint() methods takes size parameter where you can specify the shape of an array

# generating a 1-D array containing 5 random integers from 0 to 100
x2 = random.randint(100, size = (5))
print(x2)

# generating the 2-D array containing 3 row and 5 element column integers from 0 to 100.
x3 = random.randint(100, size = (3,5))
print(x3)

# generate random number for float 3,5

x4 = random.rand(3,5)
print(x4)

# choice() methods takes an array as a parameter and randomly return one of the values

x5 = random.choice([3,5,7,9])
print(x5)

# generate a 2-D array that consist of the values in the array parameter

x6 = random.choice([3,5,7,9], size = (18,5))
print(x6)

# random data distribution 
# a random distribution is a set of random numbers that follow a certain probability density function
# The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur.

x7 = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0], size=(100))
print(x7)

# the sum of all probabilities should be 1

# even if you run the example above 100 times the value 9 will neveer occur

x8 = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0], size=(3,5))
print(x8)

# random permutations 
# A permutation refers to an arrangement of elements. e.g. [3,2,1] is a permutation of [1,2,3] and vice versa

# the numpy random module provides two method for this shuffle() and permutation().


# shuffling arrays 
import numpy as np
arr  = np.array([1,2,3,4,5])
print("Before shuffle :",arr)
random.shuffle(arr)
print("after shuffle :",arr)


# the shuffle() method makes changes to the original array
# generate a random permutatio of elements of following arrays

arr1 = np.array([1,2,3,4,5])
print(random.permutation(arr1))

# The permutation() method returns a re-arranged array (and leaves the original array un-changed).

