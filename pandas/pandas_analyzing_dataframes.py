# pandas analyzing dataframes

# one of the most used method for getting a quick overview of the  DataFrame is the 
# head() method
# 
# the head() method return the header and specified no. of rows, starting from the top 


import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10)) # return the first 10 rows 

# if we not specified the no. of rows the head() method will return the top 5 rows

print(df.head())

# there is also a tail() method for viewing the last rows of the DataFrame

# the tail() method return the header and a specified no. of rows, staring from the bottom


print(df.tail())

# info about the data

# the DataFrame object has a method called info(), that gives you more info. about the data set

print(df.info())