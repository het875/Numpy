"""
What are ufuncs?
ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.

Why use ufuncs?
ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

ufuncs also take additional arguments, like:

where boolean array or condition defining where the operations should take place.

dtype defining the return type of elements.

out output array where the return value should be copied.

What is Vectorization?
Converting iterative statements into a vector based operation is called vectorization.

It is faster as modern CPUs are optimized for such operations.

Add the Elements of Two Lists
list 1: [1, 2, 3, 4]

list 2: [4, 5, 6, 7]

One way of doing it is to iterate over both of the lists and then sum each elements.
"""


import numpy as np

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

result = []

for i, j in zip(list1, list2):
    result.append(i + j)

print(result)
# Output: [5, 7, 9, 11]



x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

# Output: [ 5  7  9 11]