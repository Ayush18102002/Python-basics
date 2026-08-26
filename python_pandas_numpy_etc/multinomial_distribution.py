# multinomial distribution

# it is a generalization of binomial distribution

# it is describe outcomes of multi-nomial scenarios unlike binomail where scenarios must be only one of two 

# 3- parameters

# n - no. of times to run the experiment
# pvals- list of probabilities of outcomes
# size = the shape of the returned  array.

from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)

x2 = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(2,3))

print(x2)