# numpy LCM lowest commont multiple

# finding LCM(Lowest Common Multiple)

# The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.

import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1,num2)
print(x)



# output 12 because that is the lowest common multiple of both numbers (4*3=12 and 6*2=12).


# finding LCM in arrays

# to find the LCM of all values in an array, you can use the reduce() method

# the reduce() method will use the unfunc, in this case the lcm() function, on each element, and reduce the array by one dmension


arr = np.array([3,6,9])
x1 =np.lcm.reduce(arr)
print(x1)

# Returns: 18 because that is the lowest common multiple of all three numbers (3*6=18, 6*3=18 and 9*2=18)


# Find the LCM of all values of an array where the array contains all integers from 1 to 10:

arr1 = np.arange(1,11)
x2 = np.lcm.reduce(arr1)
print(x)

