# numpy hyperbolic functions

"""
Hyperbolic Functions
NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..

"""

import numpy as np

x = np.sinh(np.pi/2)
print(x)


# find cosh values for all of the values in arr:

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x1 = np.cosh(arr)

print(x1)


# find angles

"""
Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).

Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given.

"""

x2 = np.arcsinh(1.0)
print(x2)

# angles of each value in arrays

# find the angle for all of the tanh values in array

arr2 = np.array([0.1,0.2,0.5])

x3 = np.arctanh(arr2)
print(x3)