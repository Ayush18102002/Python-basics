# chi square distribution

"""
Chi Square distribution is used as a basis to verify the hypothesis.

It has two parameters:

df - (degree of freedom).

size - The shape of the returned array.

"""

# draw out a sample for chi sqaure distribution with degree of freedom 2 with size 2 x 3.

from numpy import random 
x = random.chisquare(df=2, size=(2, 3))

print(x)

# visualization of chi square distribution

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.chisquare(df=2, size=1000), kind='kde')
plt.show()

