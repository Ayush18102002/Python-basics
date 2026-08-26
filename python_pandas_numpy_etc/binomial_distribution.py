# binomial distribution is a dicrete distribution 

# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

# It has three parameters:

# n - number of trials.

# p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).

# size - The shape of the returned array.

from numpy import random

x= random.binomial(n =10, p=0.5, size = 10)
print(x)

# visualization of binomial distribution

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=10, p=0.5, size = 1000))
plt.show()

