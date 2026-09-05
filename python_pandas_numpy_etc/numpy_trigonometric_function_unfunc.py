# numpy trigonometric functions

# numpy provides the unfunc sin(), cos() and tan() that take values in radians and produce
# the corresponding sin, cos and tan values

# find sine values of PI/2


import numpy as np

x = np.sin(np.pi/2)

print(x)

# Find sine values for all of the values in arr:

arr1 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x1 = np.sin(arr1)

print(x1)

# convert degree into radians
# By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
# 
# # note : radians values are pi/180*degre_values
# 
# # convert all the values in following array arr to radians
# 

arr2 = np.array([90,180,270,360])

x2 =np.deg2rad(arr2)
print(x2)

# Radians to Degrees

# Convert all of the values in following array arr to degrees:

arr3 = np.array([np.pi/2, np.pi, .5*np.pi, 2*np.pi])
x3 = np.deg2rad(arr3)
print(x3)

"""
Finding Angles
Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.


"""

x4 = np.arcsin(1.0)
print(x4)


# Angles of Each Value in Arrays

# Find the angle for all of the sine values in the array

arr4 = np.array([1, -1, 0.1])
x5 = np.arcsin(arr4)
print(x5)

"""
Hypotenues
Finding hypotenues using pythagoras theorem in NumPy.

NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.

"""

base = 4 
prep = 4

x6 = int(np.hypot(base,prep))

print(x6)

