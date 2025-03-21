"""Generate Random Number
NumPy offers the random module to work with random numbers.

ExampleGet your own Python Server
Generate a random integer from 0 to 100:
"""
from numpy import random

x = random.randint(100)

print(x)





"""
Generate Random Float
The random module's rand() method returns a random float between 0 and 1.

Example
Generate a random float from 0 to 1:
"""

from numpy import random

x = random.rand()

print(x)





"""
Generate Random Array
In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.

Integers
The randint() method takes a size parameter where you can specify the shape of an array.
"""
#Generate a 1-D array containing 5 random integers from 0 to 100:
from numpy import random

x=random.randint(100, size=(5))

print(x)

# [39 72 16 79 80]




#Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x = random.randint(100, size=(3, 5))

print(x)




# The rand() method also allows you to specify the shape of the array.
x = random.rand(5)

print(x)
#[0.76977097 0.71075702 0.37786036 0.45629499 0.16503157]



#Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x = random.rand(3, 5)

print(x)




"""
Generate Random Number From Array
The choice() method allows you to generate a random value based on an array of values.

The choice() method takes an array as a parameter and randomly returns one of the values.
"""

x = random.choice([3, 5, 7, 9])

print(x)
# The choice() method also allows you to return an array of values.





#Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)

"""
[[3 5 7 9 3]
 [5 9 3 7 5]
 [5 5 9 9 5]]
"""
