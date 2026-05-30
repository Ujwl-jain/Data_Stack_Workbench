# ============================================================
#                      NUMPY IN PYTHON
# ============================================================
# NumPy (Numerical Python) is a third-party library for
# working with arrays and numerical data efficiently.
#
# WHY NUMPY OVER REGULAR PYTHON LISTS:
#   - Faster         -- operations run in C under the hood
#   - Less memory    -- stores data in compact, typed blocks
#   - Vectorized     -- apply operations to entire arrays without loops
#   - Built-in math  -- sum, min, max, sqrt, etc. all built in
#
# INSTALL: pip install numpy
# IMPORT:  import numpy as np   <- standard alias used everywhere
# DOCS:    https://docs.scipy.org/doc/numpy-1.6.0/reference/generated/numpy.ndarray.html
# ============================================================

import numpy as np
import sys


# ============================================================
#                      NUMPY ARRAYS
# ============================================================
# Core data structure in NumPy is the ndarray (n-dimensional array).
# Unlike Python lists:
#   - All elements must be the SAME data type
#   - Fixed size once created
#   - Much faster for math operations
# ============================================================


# ------------------------------------------------------------
# 1D Array
# ------------------------------------------------------------
myarr = np.array([3, 21, 23, 5, 1])
print(myarr)            # [ 3 21 23  5  1]
print(myarr[0])         # 3  <- indexing same as list
print(myarr[-1])        # 1  <- last element
print(myarr[1:4])       # [21 23  5]  <- slicing works too

# print(myarr[0, 1])    # IndexError -- 1D needs only one index


# ------------------------------------------------------------
# Specifying dtype -- controls memory allocation
# ------------------------------------------------------------
# int16 uses less memory than default int64
# use smaller dtype when values are small to save memory

myarr = np.array([3, 21, 23, 5, 1], dtype=np.int16)
print(myarr.dtype)      # int16

# common dtypes:
# np.int16    -- integer, 16 bits  (range: -32768 to 32767)
# np.int32    -- integer, 32 bits
# np.int64    -- integer, 64 bits  (default for int)
# np.float32  -- float,   32 bits
# np.float64  -- float,   64 bits  (default for float)


# ------------------------------------------------------------
# 2D Array
# ------------------------------------------------------------
# Wrap list in another list -- think rows and columns like a table.
# Indexing: array[row, column]

myarr = np.array([[3, 21, 23, 5, 1]])
print(myarr[0])         # [ 3 21 23  5  1]  <- first row
print(myarr[0, 0])      # 3   <- row 0, column 0
print(myarr[0, 1])      # 21  <- row 0, column 1

# proper multi-row 2D array:
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr2d[1, 2])      # 6  <- row 1, column 2


# ------------------------------------------------------------
# Array attributes
# ------------------------------------------------------------
myarr = np.array([[3, 21, 23, 5, 1]])

print(myarr.shape)      # (1, 5)  <- 1 row, 5 columns
print(myarr.dtype)      # int64
print(myarr.size)       # 5       <- total elements
print(myarr.ndim)       # 2       <- number of dimensions
print(myarr.nbytes)     # total bytes consumed by the array


# ------------------------------------------------------------
# Modifying values
# ------------------------------------------------------------
myarr[0, 1] = 45
print(myarr)            # [[ 3 45 23  5  1]]


# ============================================================
#                  ARRAY CREATION METHODS
# ============================================================


# ------------------------------------------------------------
# Method 1 -- From Python list or tuple
# ------------------------------------------------------------
listarray = np.array([[1, 2, 3],
                      [4, 5, 1],
                      [9, 9, 9]])
print(listarray.shape)  # (3, 3)
print(listarray.dtype)  # int64
print(listarray.size)   # 9

# AVOID -- passing a set gives dtype=object, kills performance:
# object_array = np.array({1, 2, 3})  # dtype=object -- not efficient
# always use list or tuple, stick to int or float dtypes


# ------------------------------------------------------------
# Method 2 -- Intrinsic NumPy functions
# ------------------------------------------------------------

# zeros() -- filled with 0.0, dtype float64 by default
zeros = np.zeros((2, 5))
print(zeros)
print(zeros.dtype)      # float64

# ones() -- filled with 1.0
ones = np.ones((3, 3))
print(ones)

# full() -- filled with a specific value
full = np.full((2, 4), 7)
print(full)             # [[7 7 7 7]
                        #  [7 7 7 7]]

# arange() -- range of values, same idea as range() but returns array
rng = np.arange(15)
print(rng)              # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

# arange with start, stop, step:
rng2 = np.arange(1, 20, 2)
print(rng2)             # [ 1  3  5  7  9 11 13 15 17 19]

# linspace() -- evenly spaced values, you control the COUNT not the step
# SYNTAX: np.linspace(start, stop, num_of_elements)
# stop is INCLUSIVE, dtype is float
lspace = np.linspace(1, 5, 12)
print(lspace)           # 12 equally spaced values from 1 to 5

lspave = np.linspace(1, 4, 4)
print(lspave)           # [1. 2. 3. 4.]

# arange vs linspace:
# arange(1, 5, 0.5)  -- you set the STEP, count varies
# linspace(1, 5, 12) -- you set the COUNT, step is calculated for you

# identity() -- n x n matrix with 1s on diagonal, 0s elsewhere
ide = np.identity(4)
print(ide)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
print(ide.shape)        # (4, 4)

# empty() -- uninitialized array, values are garbage memory
# does NOT mean zeros -- assign values before using
emp = np.empty((4, 6))
print(emp)              # unpredictable values

# empty_like() -- uninitialized array with SAME SHAPE as given array
emp_like = np.empty_like(lspave)
print(emp_like.shape)   # (4,)  <- same shape as lspave


# ============================================================
#                  RESHAPE AND RAVEL
# ============================================================

# reshape() -- change the shape of an array without changing its data
# total elements must remain the same
arr = np.arange(99)             # 99 elements, 1D
arr = arr.reshape(3, 33)        # 3 rows x 33 cols = 99 elements -- works
print(arr)

# arr.reshape(3, 31)            # 3*31 = 93 != 99 -- ValueError

# ravel() -- flatten any array back to 1D
arr = arr.ravel()
print(arr.shape)        # (99,)  <- back to 1D
print(arr)


# ============================================================
#                          AXIS
# ============================================================
# NumPy operations can be performed along a specific axis.
#
# 1D array -- only axis 0 (the single row of elements)
# 2D array -- axis 0 = rows (top to bottom)
#             axis 1 = columns (left to right)
#
# axis=0 means: collapse DOWN each column, give one result per column
# axis=1 means: collapse ACROSS each row, give one result per row
#
# 2D array visual:
#        col0 col1 col2
# row0  [ 1    2    3 ]   axis 1 →
# row1  [ 4    5    6 ]   axis 1 →
# row2  [ 7    1    8 ]   axis 1 →
#         ↓    ↓    ↓
#       axis 0 (down)
# ============================================================

axis = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 1, 8]])

# sum along axis=0 -- adds DOWN each column:
print(axis.sum(axis=0))     # [12  8 17]  <- 1+4+7, 2+5+1, 3+6+8

# sum along axis=1 -- adds ACROSS each row:
print(axis.sum(axis=1))     # [ 6 15 16]  <- 1+2+3, 4+5+6, 7+1+8

# transpose -- rows become columns, columns become rows
print(axis.T)
# [[1 4 7]
#  [2 5 1]
#  [3 6 8]]

# flat -- iterator to loop over every element one by one:
for i in axis.flat:
    print(i)                # 1, 2, 3, 4, 5, 6, 7, 1, 8


# ============================================================
#               argmax, argmin, argsort
# ============================================================

# ------------------------------------------------------------
# 1D array
# ------------------------------------------------------------
one = np.array([10, 2, 3, 4, 5, 6, 71, 8])

print(one.argmax())     # 6  <- index of highest value (71 is at index 6)
print(one.argmin())     # 1  <- index of lowest value  (2 is at index 1)
print(one.argsort())    # [1 2 3 4 5 7 0 6]
# argsort tells you: to sort this array, pick elements in this index order
# position 1 (value 2) first, then position 2 (value 3), ... last position 6 (value 71)


# ------------------------------------------------------------
# 2D array
# ------------------------------------------------------------
two = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 1, 8]])

# without axis -- flattens first, then finds index:
print(two.argmax())     # 8  <- index in flattened array, value 8 is at position 8
print(two.argmin())     # 0  <- index in flattened array, value 1 is at position 0

# with axis=0 -- find argmax/argmin DOWN each column:
print(two.argmax(axis=0))   # [2 1 2]  <- col0: row2 has max(7), col1: row1 has max(5), col2: row2 has max(8)
print(two.argmin(axis=0))   # [0 2 0]  <- col0: row0 has min(1), col1: row2 has min(1), col2: row0 has min(3)

# with axis=1 -- find argmax/argmin ACROSS each row:
print(two.argmax(axis=1))   # [2 2 2]  <- each row's max is at column index 2
print(two.argmin(axis=1))   # [0 0 1]  <- row0 min at col0, row1 min at col0, row2 min at col1

# argsort on 2D array:
print(two.argsort(axis=0))
# [[0 2 0]
#  [1 0 1]
#  [2 1 2]]
# HOW IT WORKS: sorts each COLUMN independently and returns the ROW INDICES
# that would sort it. Does NOT flatten -- works column by column.
# col0: values are 1,4,7 -> already sorted -> row indices [0,1,2]
# col1: values are 2,5,1 -> sorted order is 1,2,5 -> row indices [2,0,1]
# col2: values are 3,6,8 -> already sorted -> row indices [0,1,2]


# ============================================================
#                  MATHEMATICAL OPERATIONS
# ============================================================
# Operations happen ELEMENT BY ELEMENT at matching positions.
# Both arrays must have the same shape.

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 1, 8]])

arr2 = np.array([[2, 5, 3],
                 [1, 5, 1],
                 [1, 1, 0]])

print(arr1 + arr2)      # element-wise addition
print(arr1 - arr2)      # element-wise subtraction
print(arr1 * arr2)      # element-wise multiplication
print(arr1 / arr2)      # element-wise division

print(np.sqrt(arr1))    # square root of every element
print(arr1.sum())       # sum of ALL elements
print(arr1.max())       # largest value in entire array
print(arr1.min())       # smallest value in entire array

# where() -- find positions of elements meeting a condition:
print(np.where(arr1 > 5))
# (array([1, 2, 2]), array([2, 0, 2]))
# means: values > 5 are at [row1,col2], [row2,col0], [row2,col2]
# first array = row positions, second array = column positions

# count_nonzero() -- count of elements that are not zero:
print(np.count_nonzero(arr1))   # 9  <- all elements are non-zero here

# nonzero() -- positions of all non-zero elements:
print(np.nonzero(arr1))
# (array([0,0,0,1,1,1,2,2,2]), array([0,1,2,0,1,2,0,1,2]))
# same format as where() -- row positions and column positions


# ============================================================
#              NUMPY vs PYTHON LIST -- MEMORY PROOF
# ============================================================
# NumPy arrays take significantly less memory than Python lists.

py_ar = [1, 2, 3, 4]
np_ar = np.array(py_ar)

print(sys.getsizeof(1) * len(py_ar))   # 112 bytes  <- Python list
print(np_ar.itemsize * np_ar.size)     # 32 bytes   <- NumPy array

# Python stores each integer as a full object with extra metadata.
# NumPy stores raw values in a compact, fixed-type block.
# As array size grows, this difference becomes massive.


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Attribute        What it tells you
#  ──────────────────────────────────────────────────────────────
#  .shape           Dimensions as tuple -- (rows, cols) for 2D
#  .dtype           Data type -- int64, float64, etc.
#  .size            Total number of elements
#  .ndim            Number of dimensions
#  .nbytes          Total memory used in bytes
#  .itemsize        Memory per element in bytes
#
#  Creation          Output
#  ──────────────────────────────────────────────────────────────
#  np.array([...])   From list or tuple
#  np.zeros((r,c))   All zeros, float64
#  np.ones((r,c))    All ones, float64
#  np.full((r,c),v)  All filled with value v
#  np.arange(s,e,st) Range like range() but returns array
#  np.linspace(s,e,n)n evenly spaced values from s to e
#  np.identity(n)    n x n identity matrix
#  np.empty((r,c))   Uninitialized -- assign before use
#  np.empty_like(a)  Uninitialized, same shape as a
#
#  Operations        What it does
#  ──────────────────────────────────────────────────────────────
#  .reshape(r,c)     Change shape, total elements must stay same
#  .ravel()          Flatten to 1D
#  .T                Transpose -- rows become columns
#  .flat             Iterator over every element
#  .sum(axis=0)      Sum down each column
#  .sum(axis=1)      Sum across each row
#  .argmax()         Index of highest value
#  .argmin()         Index of lowest value
#  .argsort()        Indices that would sort the array
#  np.where(cond)    Positions of elements meeting condition
#  np.sqrt(arr)      Square root of every element
#  np.count_nonzero  Count of non-zero elements
#  np.nonzero(arr)   Positions of all non-zero elements
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. All elements must be the SAME dtype -- avoid dtype=object
#  2. reshape() total elements before and after must match
#  3. axis=0 goes DOWN rows (per column), axis=1 goes ACROSS columns (per row)
#  4. argmax/argmin without axis flattens first then finds index
#  5. Math operations are element-wise -- arrays must be same shape
#  6. np.linspace stop is INCLUSIVE -- np.arange stop is EXCLUSIVE
#
# ============================================================