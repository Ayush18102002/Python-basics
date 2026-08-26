# pission distrubution

# its a discreate distribution
# it estimates how many times an event can happen in a specific time like if someone eats twice what is the probabilities hw will eat thrice
# it has 2 parameters

# lam - rate or known no. of occurence.
# size - the shape of the returned array.

# generate a random 1 *10 distribution for occurence 2:

from numpy import random

x = random.poisson(lam=2, size=10)

print(x)


# visualization of poisson distribution

import matplotlib.pyplot as plt
import seaborn as sns

# sns.displot(random.poisson(lam=2,size=1000))

# plt.show()

# distance between normal and poisson distribution
# normal dist. is continious whereas the poisson is discreate 

data = {
    "normal" : random.normal(loc=50, scale=7, size=1000),
    "poisson" : random.poisson(lam=50, size=1000)

}

#sns.displot(data, kind = "kde")
# plt.show()


# distance between bionamial and poisson dist.
# binomial dist. only has two possible outcomes, whereas poission dist. can have unlimited possible outcomes

#But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.


data2 = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}

# sns.displot(data2, kind="kde")

# plt.show()