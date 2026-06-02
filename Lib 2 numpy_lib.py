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
lspave =np.linspace(1,4,4)
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

# identity
'''
this will give tne n*n identical matrix

below gives the identitcal matrix of 45 x 45
'''
ide = np.identity(45)
print(ide)
print(ide.shape)
print()

# reshape()
# this will give the array from 0 to 98
arr = np.arange(99)
# now we can write the same as this, this will devide the 1D array into equally arrays by n qhich is 3 here.
arr = arr.reshape(3,33)
print(arr)

# this will give error as 3*31 will 93 and total elements are 99
# arr1 = arr.reshape(3,31)
# print(arr1)

# ravel()
'''
this will convert the arrays, into 1D array
'''
arr = arr.ravel()
print(arr.shape)
print(arr)

# --------------------------------------
# AXIS
'''
1d Array - will have only 1 axis, axis 0, as there is only 1 single rows in it
2d array - will have 2 axis, axis 0 for rows and axis 1 for columns

on numpys some function can be perfomed based on axis

1d array is kind of confusing as it contains only 1 rows and 1 axis, 
generally 2D is more preferrable to work on, but for some knowlege go through the 3d,4d,5d arrays as well

for example:
1d array = [1,2,3,4,5]
2d array =[[1,2,3],
            [3,4,5],
            [5,6,1]], contains 2 axis axis 0 for row and 1 for columns
'''

array_axis = [[1,2,3],[4,5,6],[7,1,8]]
axis = np.array(array_axis)
print(axis)

# perform the axis function

# here we are adding the arrays of a particular axis, 
# here the axis 0, for every element in each row sum will return
axis_sum = axis.sum(axis=0)
print(axis_sum)
print(axis.sum(axis=0))

# here the axis 1, for every element in each columns sum will return
axis_sum = axis.sum(axis=1)
print(axis_sum)
print(axis.sum(axis=1))

# transpose
'''
this will transpone an array, where row becomes column and column becomes row
'''
print(axis.T)

# flat
'''
this will flat the array and we can access each element using loop
'''
for i in axis.flat:
    print(i)

# ndim
'''
provides the dimension of array
'''
print(axis.ndim)
print(axis.size)

# nbytes
'''
which tells the total bytes consumed by array
'''
print(axis.nbytes)

# ---------------------------------------------------------
# functions to be perfomed in 1d array
one  = np.array([10,2,3,4,5,6,71,8])

# give the index number of the highest value in the array for the abov array it will show 6th index which is 71
print(one.argmax())

# give the index number of the lowes value in the array for the abov array it will show 1st index which value is 2
print(one.argmin())

# return an array of sorted indexing,x means this function sort on the basis of indexing and return the same positions as an array like: [1 2 3 4 5 7 0 6]
# it is in ascending order, also tells that in which order should be our values be sorted.
print(one.argsort())

# same functions to be perfor on 2d array
two = np.array([[1,2,3],
                [4,5,6],
                [7,1,8]])
print(two)

# arg max and arg min works in this way - > it will first flat the 2d array and give the indexing of numbe rwhich has highest or lowest value in above case it is at 8th and 0th index, which is 8 and 1
print(two.argmin())

print(two.argmax())

# give the indexing of highest or lowest value from axis = 0  as 1d array 
print(two.argmax(axis = 0))
print(two.argmin(axis = 0))

print(two.argmax(axis = 1))
print(two.argmin(axis = 1))

# works like argsort in 1d array, basically provide the 2d array of sorted array based on indexing of a value. 
# but its output is limited to each row and column means like this: [[0 2 0]
                                                                    # [1 0 1]
                                                                    # [2 1 2]],  means it will not do flattening of 2d array, pleas explain how this work. 
print(two.argsort(axis = 0))
print(two.argsort(axis = 0))


# -----------------------------------------------
# Mathmatical oprration in numpy

# add using 2 2d arrays - done using element + element like whatever element was at 0th indexing of 1st arrat will add with whatever idnexing is at 2nd array

arr1 = np.array([[1,2,3],
                [4,5,6],
                [7,1,8]])

arr2 =  np.array([[2,5,3],
                [1,5,1],
                [1,1,0]])

print(arr1 + arr2)

# subtract - done using element - element like whatever element was at 0th indexing of 1st arrat will minus with whatever idnexing is at 2nd array

print(arr1 - arr2)

# multiply - done using element * element like whatever element was at 0th indexing of 1st arrat will multiple with whatever idnexing is at 2nd array
print(arr1 * arr2)

# divide - done using element / element like whatever element was at 0th indexing of 1st arrat will divide with whatever idnexing is at 2nd array
print(arr1 / arr2)

# sqrt - squareroot the values of each element in the array
print(np.sqrt(arr1))

# sum() - sum of all ekements in the array
print(arr1.sum())

# max() - provide the largest value inside an array
print(arr1.max())

# min() - provide the lowes values inside an array
print(arr1.min())

# where - helps you to find a specific values like this tells us at which position we can find the values greater than 5 - (array([1, 2, 2]), array([2, 0, 2]))
print(np.where(arr1 > 5))

# count_nonzero - gives the count of non zero values inside an array
print(np.count_nonzero(arr1))

# nonzero() - returns a tuple of each dimension stating position of non zero values - (array([0, 0, 0, 1, 1, 1, 2, 2, 2]), array([0, 1, 2, 0, 1, 2, 0, 1, 2]))
print(np.nonzero(arr1))


# --------------------------------------------
'''
To prove: numpy takes less space, as for how:
'''

import sys

# python array(list)
py_ar = [1,2,3,4]

# numpy_array
np_ar = np.array(py_ar)

# getsize of will tell the size of an element in bytes
print(sys.getsizeof(1) * len(py_ar)) # shows 132 bytes
print(np_ar.itemsize * np_ar.size)  #shows 32 bytes

# hence proved, np array takes less size compare to normal array


'''
For more information on numpy practice attributes and methods mentioned in this website : https://docs.scipy.org/doc/numpy-1.6.0/reference/generated/numpy.ndarray.html
'''
