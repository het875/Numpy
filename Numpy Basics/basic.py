import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


#Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)


"""
3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.
"""
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

