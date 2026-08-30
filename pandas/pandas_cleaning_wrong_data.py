# pandas - fixing wrong data


# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".


# replacing values
import pandas as pd
df = pd.read_csv('Data.csv')
df.loc[7,'Duration'] = 45

# for small data sets you might be  able to replace the wrong data one by one but no for big data sets
# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.


#Loop through all values in the "Duration" column.

# If the value is higher than 120, set it to 120:

for x in df.index:
    if df.loc[x,"Duration"] > 120:
        df.loc[x,"Duration"]= 120


# removing rows

# another ways of handling wrong data is to remove the rows that contains wrong data
# This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses.


# Delete rows where "Duration" is higher than 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)