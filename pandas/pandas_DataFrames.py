# DataFrames 
# a pandas dataframes is a 2 dimensional data structure , like 2 dimensional array or a table with rows and columns


import pandas as pd

data = {
    "calories" : [420,320,840,540,789,234],
    "durations": [20,80,36,78,90,60]
}

df = pd.DataFrame(data)

print(df)

# locate row
# as you can see from the result above the DataFrames is like a table with rows and columns
# pandas use the loc attribute to return one or more soecified row(s)


print(df.loc[0])

# use a list of indexes

print(df.loc[[0,3]]) #it only print the index which is written inside the list not like and range

# names indexes

# with the index argumnet, you can name your own indexes
df1 = pd.DataFrame(data, index = ["day1","day2","day3","day4","day5","day6"])


print(df1)

# locate names indexes
# use the named index in the loc attribute to return the specified row(s).


print(df1.loc["day3"])

# loads file into dataframes


df2 = pd.read_csv('data.csv')

print(df2)


