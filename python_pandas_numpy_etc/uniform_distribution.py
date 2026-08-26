# uniform distribution

# used to describe probabilities where every events has equal chances of occuring

# generation of random no.

# it has 3 parameter

# low - lower bound - defaulit 0.0
# high  - upper bound - default 1.0
# size - the shape of the returned array

# create a 2*3 uniform distribution sample:

from numpy import random

x = random.uniform(size =(2,3))
print(x)


# visualization of uniform distribution

import matplotlib.pyplot as plt
import seaborn as sns 

# sns.displot(random.uniform(size=1000), kind= "kde")
# plt.show()

