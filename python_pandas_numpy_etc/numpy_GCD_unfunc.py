# numpy GCD greatest common divisor 

# finding GCD

# the GCD also known as HCF(highest common factor) is the biggest no. that is common factor of both of the number 

import numpy as np
num1 = 6
num2 = 9

x = np.gcd(num1,num2)
print(x)

# Returns: 3 because that is the highest number both numbers can be divided by (6/3=2 and 9/3=3).

# finding GCD in array

# to find the HCM of all values in an array , you can use the reduce() method.

# The reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array by one dimension.

arr = np.array([20,8,32,36,16])

x1 = np.gcd.reduce(arr)

print(x1)

# Returns: 4 because that is the highest number all values can be divided by.