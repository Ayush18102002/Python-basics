# normal(Gaussian) Distribution
# it is also called the gaussian distribution oater the german mathematician carl friedrich gauss

# It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

# Use the random.normal() method to get a Normal Data Distribution.

# it has three parameters

# loc - (Mean) where the peak of the bell exists.

# scale - (Standard Deviation) how flat the graph distribution should   

# size - the shape of the returned array


from numpy import random

x= random.normal(size = (2,3))
print(x)


# generate a random normal distribution of size 2*3 with mean at 1 and standard deviation of 2

x1 = random.normal(loc = 1, scale = 2, size = (2,3))
print(x1)


# visualzation of normal distribution 
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.normal(size =1000), kind="kde")
plt.show()
