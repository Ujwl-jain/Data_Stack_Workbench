# NUMPY

'''
PROVIDES EFFIECIENT STORAGE
ALSO PROVIDE BETTER WAYS TO HANDLE DATA PROCESSING
FAST
USE LESS MEMORY TO STORE DATA
'''

import numpy as np

# numpy array
myarr = np.array([3,21,23,5,1])
print(myarr)
# since it is 1 D array it will gett the item at 0th indexing just like as we are perfoming indexing on a list 
print(myarr[0])
# will not work as it is only 1 D array
# print(myarr[0,1])

# can decalre the dtype here for the size allocation or memery allocation
myarr = np.array([3,21,23,5,1], np.int16)
print(myarr)

# above one was the 1D array, here it will be 2D array
myarr = np.array([[3,21,23,5,1]])
print(myarr[0])

# works, it will access the first item of 2D array then get the itema of specified position at 0th index
print(myarr[0,0])
print(myarr[0,1])

# Some function we can perform on numpy
print(myarr.shape)
print(myarr.dtype)

# changing in current numpy array
# means in 2d array at 0the element place it at 1st indexing
myarr[0,1] = 45 
print(myarr)

# -----------------------------------------------------------------------------------
# array creation in mumpy

'''
there are 5 types to create a numpy array
1. convesrion from other python structures like list tuple
for example : above codes are perfect example as we used list in 2 d array

2.intrinsic numy array creation objects eg arange ones, zeros, etc

3.reading arrays from disk, either from standard and custom formats

4. creating arrays from raw bytes through the use of strings or buffers

5. use of special library like random
'''

# 1. convesrion from other python structures like list tuple
# for example : above codes are perfect example as we used list in 2 d array

listarray = np.array([[1,2,3], [4,5,1],[9,9,9]])
print(listarray)
print(listarray.shape)
print(listarray.dtype)
print(listarray.size)

# dtype = object not prefer and effienet , always only Int or Float array
object_array = np.array({1,2,3})
print(object_array.dtype)


# 2.intrinsic numy array creation objects eg arange ones, zeros, etc

# numpys as zero
'''
will create the array of zero for the the give size and shape, consist of only 0, as dtype = float
'''
zeros = np.zeros((2,5))
print(zeros)
print(zeros.shape)
print(zeros.dtype)
print(zeros.size)

# numpys as arrange 
'''
this will gave the array from 0 to n-1, where n is the one given in the arange(n)
this is not list, it is a numpy array

'''
rng = np.arange(15)
print(rng)

# linspace()
'''
this will give the particular elements from n to n range equally
for example as below, this will give 12 elements from 1 to 5, where the space between each element is equal
its dtype is float,
'''
lspace = np.linspace(1,5,12)
lspave =np.linespace(1,4,4)
print(lspace)
print(lspave)

# empty()
'''
this will give the empty array of size 4,6 which gives the empty array with random numbers of element
we can assign the values in those random values
'''
emp = np.empty((4,6))
print(emp)

# empty_like
'''
it will just like empty, but it will take an array as an argument in empty_like,
what this will do it is take the size of that argumented array and create an empty array of same size
'''
emp_like = np.empty_like(lspave)
print(emp_like)