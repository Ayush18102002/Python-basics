# pandas plotting 

# oandas uses the plot() method to create diagams
# we can use pyplot, a submodule of the matplotlib library to vizualize the diagram onthe screen

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')

df.plot()
plt.show()

# scatter plot

# specify that you want a scatter plot with the kind arguments
# kind='scatter'

# a scatter plot needs an x-axis and a y-axis

# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

# Include the x and y arguments like this:

# x  = 'Duration' , y ='calories'


import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y='Calories')
plt.show()


df1.plot(kind = 'scatter', x = 'Duration', y='Maxpulse')
plt.show()


# histogram

df1["Duration"].plot(kind='hist')
plt.show()