# it is used for describing time till next event. e.g. failure/sucess etc.
# 2 parameter
# scale - inverse of rate , default 1.0
# size - the shape of the returned array


# draw out a sample for exponential distribution with 2.0 scale with 2*3 size

from numpy import random 
x = random.exponential(scale=2, size=(2,3))
print(x)


# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.displot(random.exponential(size=1000), kind="kde")
# plt.show()

# relation between poisson and exponential distribution

# poisson distribution deals with number of occurences of an event in a time period whereas
# exponential dist. deals with the time between these events.


