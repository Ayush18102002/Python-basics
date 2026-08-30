# pandas cleaning data 

# data cleaning means fixing big data in your dataset
# bad data colud be
### empty cells
### data in wrong format
### wrong data
### Duplicates 

# cleaning empty cells

# empty cellls can potentially give ou a wrong result when you analyze data


# removes rows 

# one ways to deal with empty cells is to remove rows that conatains empty cells

import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())
new_df = df.dropna()  # dropna() method return a new dataframe and will not change the original
print(new_df.to_string())

# if you want to change the original dataframes use he inplace=True arguments

df.dropna(inplace=True)
print(df.to_string)

# Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.

print(df.info())


# replace empty values

# another way of dealing with empty celss is to insert a new value instead
# this way you do not have to delete entire rows just because of some empty cells
# the fillna() methods allows us to replace empty cells with a values

df1 = pd.read_csv('data.csv')
print(df1.info())

df1.fillna(130, inplace=True) # replace NULL values with the bumber 130.
print(df1.info())

# replace only for specified columns

# to only replace empty values for one column, specify the column name for the DataFrame

df2 = pd.read_csv('data.csv')
print(df2.info())
df2.fillna({"Calories":130}, inplace=True)
print(df2.info())

# replacing using mean, median , mode

# a common way to replace empty cells , is to calculate the mean , median or mode values of the column

# pasndas uses the mean(), median(), mode() method to calculate the respective calues for a specified column


df3 = pd.read_csv('data.csv')

x = df3["Calories"].mean()

df3.fillna({"Calories":x},inplace=True)

print(df3.to_string())

df4 = pd.read_csv('data.csv')

y = df4["Calories"].median()
df4.fillna({"Calories":y}, inplace=True)
print(df4.to_string())



df5 = pd.read_csv('data.csv')

z = df5["Calories"].mode()[0]

df5.fillna({"Calories":z}, inplace=True)
print(df5.to_string())