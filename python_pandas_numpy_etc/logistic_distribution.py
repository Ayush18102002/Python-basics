# logistic distribution

# it is used to describe growth 

# used extensive in machine learning in logstic regression, nural networks etc.

# it has 3 parameter

# loc - mean , where the peak is , default 0.
# scale - standard deviation, the faltness of distribution. dafault 1.
# size - the shape of the returned array

# draw 2*3 smaples from  a logistic distribution with mean at 1 and stddev 2.0.


from numpy import random

x = random.logistic(loc=1, scale=2, size=(2,3))
print(x)

# visualization of logistic distribution
import matplotlib.pyplot as plt
import seaborn as sns
# sns.displot(random.logistic(size = 1000), kind = "kde")
# plt.show()

# difference between logistic and normal dist.

# Both distributions are near identical, but logistic distribution has more area under the tails, meaning it represents more possibility of occurrence of an event further away from mean.
# For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.

data = {
    "normal" : random.normal(scale=2,size=1000),
    "logistic" : random.logistic(size=1000)

}

# sns.displot(data, kind= "kde")

# plt.show()

