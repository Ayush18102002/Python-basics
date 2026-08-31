# SciPy
# it is a scientific computation library that uses numpy underneath 
# it stands for scientific python
# it provides more utility function for optimization , stats and signall processing 
# like numpy, scipy is open source so we can use it freely 


# why use scipy
# if scipy uses numpy underneath, why can we not just use numpy?
# scipy has optimized and added function that are frequently used in nnumpy and data science 

# Which language is scipy written in 
# SciPy is predominantly written in python, but a few segments are written in c.



# Once SciPy is installed, import the SciPy module(s) you want to use in your applications by adding the from scipy import module statement:


from scipy import constants


# how many cubic meters are in one liter:
print(constants.liter)

# constants: SciPy offers a set of mathematical constants, one of them is liter which returns 1 liter as cubic meters.

import scipy 
print(scipy.__version__)