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

