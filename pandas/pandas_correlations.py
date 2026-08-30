# pandas correlations

# a grate aspect of the pandas module is the corr() method

# the corr() method calculated the realtionship between each column in your data set

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())
print("***********************####################********************")
print(df.corr()) # it find the correlation between each column

# the corr() methods ignores "not numeric" columns

# What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

# perfect correlations is 1.000
# good correlation is  0.922271..so on
# bad correlation is  0.0009403.. so onn



"""
##################################OUTPUT###############################
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0

***********************####################********************

          Duration     Pulse  Maxpulse  Calories
Duration  1.000000 -0.155408  0.009403  0.922717
Pulse    -0.155408  1.000000  0.786535  0.025121
Maxpulse  0.009403  0.786535  1.000000  0.203813
Calories  0.922717  0.025121  0.203813  1.000000

"""