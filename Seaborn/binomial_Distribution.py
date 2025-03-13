"""
Binomial Distribution
Binomial Distribution is a Discrete Distribution.

It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

It has three parameters:

n - number of trials.

p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.

"""


from numpy import random

x = random.binomial(n=10, p=0.5, size=10)

print(x)
# Example
# Draw samples from the distribution:
#
# x = random.binomial(n=10, p=0.5, size=10)
#
# Output
# [6 5 5 5 5 5 5 5 5 5]
# The values in the array are the counts of the number of successful trials.


# Visualization of Binomial Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.10, size=1000), hist=True, kde=False)

plt.show()


"""
Difference Between Normal and Binomial Distribution
The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale.
"""
# Example
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()