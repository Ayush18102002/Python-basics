# data of wrong format 
# cells with data of wrong format can make it diffucult, or even impossibel , to analyze data
# to fix it , you have 2 options : remove the rows, or convert all celss in the colimns into the same format

# convert into coreect format

# pandas has a to_datetime() method for this:

import pandas as pd

# df = pd.read_csv('data.csv')

# df['Date'] = pd.to_datetime(df['Date'],format='mixed')
# print(df.to_string())

# removing rows
# the result from the converting in the example above gave us NaT value , which ccan be handled as a NULL value, and we can remove the row by usingthe dropna() method.

# df.dropna(sunset=['Date'],inplace=True)
