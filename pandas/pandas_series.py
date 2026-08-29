# series in pandas

# it is like a column in a table 
# it is 1-D dimensional array holding data of any type

import pandas as pd

a = [1,2,4]

myvar = pd.Series(a)

print(myvar)


# lables :
# if nothing else is specified , the values are labled with their index no. first value has index 0,
# second value has index 1 etc.

# this label can be used to access a specified value

print(myvar[0])

# create labels with index

b = [1,7,2]

myvar2 = pd.Series(b, index = ["x","y","z"])
print(myvar2)

print(myvar2["y"])

# key/value objects as series

calories = {"day1":420, "day2":380, "day3":390}  # the keys of the dictonaries becomes labels
myvar3 = pd.Series(calories)
print(myvar3)

# item selection from the index

myvar4 = pd.Series(calories, index = ["day1","day2"])
print(myvar4)

# data frames  -- data sets in pandas are ususlly multif=dimensional table, called DataFrames
# series is like a column, a DataFrames is the whole table
# create a DataFrames from two series 

data = {
    "calories" : [420,380,390],
    "duration" : [50,40,45]
}

myvar5 = pd.DataFrame(data)
print(myvar5)

