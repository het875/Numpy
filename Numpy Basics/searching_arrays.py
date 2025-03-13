"""
Searching Arrays
You can search an array for a certain value, and return the indexes that get a match.

To search an array, use the where() method."""


import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
# (array([3, 5, 6]),)

"""
The example above will return a tuple: (array([3, 5, 6],)

Which means that the value 4 is present at index 3, 5, and 6.
"""



# Find the indexes where the values are odd:
x = np.where(arr%2 == 1)

print(x)



#Find the indexes where the values are even:
x = np.where(arr%2 == 0)

print(x)





"""
Search Sorted
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
"""

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
"""
Example explained: The number 7 should be inserted on index 1 to remain the sort order.

The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.
"""







"""
Search From the Right Side
By default the left most index is returned, but we can give side='right' to return the right most index instead.
"""

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)

"""
Example explained: The number 7 should be inserted on index 2 to remain the sort order.

The method starts the search from the right and returns the first index where the number 7 is no longer less than the next value.
"""



