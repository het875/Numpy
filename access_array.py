import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])


arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])


"""
Access 2-D Arrays
To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.
"""
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])


"""
Access 3-D Arrays
To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.
"""

arr = np.array([[[1, 2, 3], 
                 [4, 5, 6]], 
                [[7, 8, 9], 
                [10, 11, 12]]])

print(arr[0, 1, 2])


arr = np.array([[1,2,3,4,5], 
                [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])