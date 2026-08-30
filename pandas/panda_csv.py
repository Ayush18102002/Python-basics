# panda read csv

# a simple way to store bigcdata sets is use CSV files(comma separated files)
# it contains plain text and is well known format that can be ready by everyone including pandas


import pandas as pd
df = pd.read_csv('data.csv')
#print(df.to_string())  # use to_string() to print the entire DataFrame.


# if you have a large dtafrae with many rows pandas will only return the first  rows and the last  rows

#print(df)


# max_rows
# the no. of rows returned is defined in pandas option settings
# you can check your system maximum rows with the pd.options.display.max_rows statement

print(pd.options.display.max_rows)

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

# you can change the maximum rows no. with the same statements

pd.options.display.max_rows = 9999

print(df)