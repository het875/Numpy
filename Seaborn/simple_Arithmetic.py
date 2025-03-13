"""
Simple Arithmetic
You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.

Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.

All of the discussed arithmetic functions take a where parameter in which we can specify that condition.
"""



#1. Addition
#The add() function sums the content of two arrays, and returns the results in a new array.
#Example
#Add the elements of two lists:
import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
print(newarr)
#Output: [30 32 34 36 38 40]



#2. Subtract
#The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.
#Example
#Subtract the elements of two lists:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.subtract(arr1, arr2)

print(newarr)
#Output: [-10  -1   8  17  26  35]



#3. Multiply
#The multiply() function multiplies the values from one array with the values from another array, and return the results in a new array.
#Example
#Multiply the elements of two lists:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.multiply(arr1, arr2)

print(newarr)
#Output: [ 200  420  660  920 1200 1500]



#4. Divide
#The divide() function divides the values from one array with the values from another array, and return the results in a new array.
#Example
#Divide the elements of two lists:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

newarr = np.divide(arr1, arr2)

print(newarr)
#Output: [ 3.33333333  4.          3.          5.          25.          1.81818182]





#5. Power
#The power() function rises the values in array1 to the power of the values in array2, and return the results in a new array.
#Example
#Raise the elements in array1 to the power of the elements in array2:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)
#Output: [          1000        3200000     7290000000 1099511627776000000

#6. Remainder
#The remainder() function returns the remainder of the division of the values in the input array.
#Example
#Return the remainders:
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.remainder(arr1, arr2)

print(newarr)
#Output: [1 6 3 0 0 27]




#7. Quotient and Mod
#The divmod() function return the quotient and the remainder when argument1 is divided by argument2.
#Example
#Return the quotient and mod:

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)

#Output: (array([ 3,  2,  3,  5, 25,  1]), array([1, 6, 3, 0, 0, 27]))



#8. Absolute Values
#Both the absolute() and abs() functions functions do the same absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()
#Example
#Return the absolute values:

import numpy as np

arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)
#Output: [1 2 1 2 3 4]

