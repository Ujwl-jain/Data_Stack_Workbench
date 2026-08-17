# ============================================================
#               MAP, FILTER, REDUCE IN PYTHON
# ============================================================
# These are built-in higher-order functions -- meaning they
# take another function as an argument and apply it to data.
#
# All three follow the same pattern:
#   function(what_to_do, what_to_do_it_on)
#
#  map()    -- transform every element      -> returns map object
#  filter() -- keep elements that pass test -> returns filter object
#  reduce() -- collapse all elements to one -> returns single value
#
# map() and filter() return lazy objects for efficiency -- they
# do not process the data until you actually need it.
# Wrap in list() to see the result immediately.
#
# reduce() must be imported from functools -- it is not built-in.
# ============================================================


# ============================================================
#                         MAP
# ============================================================
# Applies a function to EVERY element in an iterable.
# Returns a map object -- convert to list/tuple/set to use it.
#
# SYNTAX:
#   map(function, iterable)
#
# Think of it as: "do this to each item"
# ============================================================

# the problem map solves -- doing the same operation on every element:
def cube(x):
    return x * x * x

print(cube(2))          # 8  <- works but only for one value at a time

# without map -- manual loop:
l = [12, 4, 12, 1, 4]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)             # [1728, 64, 1728, 1, 64]

# with map -- cleaner, same result:
newl = list(map(cube, l))
print(newl)             # [1728, 64, 1728, 1, 64]
# NOTE: pass the function NAME only -- cube, not cube()
# cube() would CALL it immediately, cube passes it as an argument

# with map + lambda -- one liner, no need to define a separate function:
newl = list(map(lambda x: x * x * x, l))
print(newl)             # [1728, 64, 1728, 1, 64]


# ------------------------------------------------------------
# map() with multiple iterables
# ------------------------------------------------------------
# map() can take more than one iterable if the function needs
# two arguments -- it pairs up elements by position.

a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)           # [11, 22, 33]  <- 1+10, 2+20, 3+30


# ------------------------------------------------------------
# map() with built-in functions
# ------------------------------------------------------------
words = ['ujjwal', 'python', 'map']
upper = list(map(str.upper, words))
print(upper)            # ['UJJWAL', 'PYTHON', 'MAP']

numbers = ['1', '2', '3', '4']
integers = list(map(int, numbers))
print(integers)         # [1, 2, 3, 4]  <- converted all strings to int


# ============================================================
#                        FILTER
# ============================================================
# Filters elements from an iterable based on a condition.
# Keeps only elements where the function returns TRUE.
# Returns a filter object -- convert to list/tuple/set to use it.
#
# SYNTAX:
#   filter(function, iterable)
#
# The function must return a boolean (True/False).
# This function is called a PREDICATE.
# Think of it as: "keep this item only if condition is True"
# ============================================================

l = [12, 4, 12, 1, 4]

# with a named function as predicate:
def filter_f(a):
    return a >= 4       # returns True or False for each element

result = list(filter(filter_f, l))
print(result)           # [12, 4, 12, 4]  <- 1 was removed (1 >= 4 is False)


# with filter + lambda -- one liner:
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)            # [12, 4, 12, 4]  <- only even numbers kept

odds = list(filter(lambda x: x % 2 != 0, l))
print(odds)             # [1]  <- only odd numbers kept

# filtering strings:
words = ['apple', 'banana', 'avocado', 'cherry', 'apricot']
a_words = list(filter(lambda w: w.startswith('a'), words))
print(a_words)          # ['apple', 'avocado', 'apricot']

# filtering out None and falsy values:
data = [1, None, 0, 'hello', '', False, 42]
clean = list(filter(None, data))    # passing None keeps only truthy values
print(clean)            # [1, 'hello', 42]


# ============================================================
#                        REDUCE
# ============================================================
# Applies a function to the first TWO elements, takes the result,
# applies the function to that result and the NEXT element,
# and continues until the entire iterable is reduced to ONE value.
#
# SYNTAX:
#   reduce(function, iterable)
#
# Must be imported from functools -- not a built-in like map/filter.
# Think of it as: "combine everything down to a single result"
#
# HOW IT WORKS STEP BY STEP (for [1, 4, 51, 2, 4] with addition):
#   step 1: 1  + 4  = 5
#   step 2: 5  + 51 = 56
#   step 3: 56 + 2  = 58
#   step 4: 58 + 4  = 62
#   result: 62
# ============================================================

from functools import reduce

numbers = [1, 4, 51, 2, 4]

# with a named function:
def mysum(x, y):
    return x + y

result = reduce(mysum, numbers)
print(result)           # 62

# with reduce + lambda -- one liner:
result = reduce(lambda x, y: x + y, numbers)
print(result)           # 62

# NOTE: avoid shadowing built-in names -- 'sum' is a built-in function
# naming your variable 'sum' overwrites it for the rest of the program
total = reduce(lambda x, y: x + y, numbers)    # 'total' is a better name


# ------------------------------------------------------------
# More reduce examples
# ------------------------------------------------------------

# finding the maximum without max():
biggest = reduce(lambda x, y: x if x > y else y, numbers)
print(biggest)          # 51

# finding the minimum without min():
smallest = reduce(lambda x, y: x if x < y else y, numbers)
print(smallest)         # 1

# multiplying all elements:
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)          # 120  <- 1*2*3*4*5

# reduce with an initial value -- third argument sets starting point:
result = reduce(lambda x, y: x + y, numbers, 100)
print(result)           # 162  <- starts from 100 instead of first element


# ============================================================
#              MAP vs FILTER vs REDUCE -- SIDE BY SIDE
# ============================================================

numbers = [1, 2, 3, 4, 5]

# map    -- transform each element -- same length list returned
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)          # [2, 4, 6, 8, 10]

# filter -- keep some elements -- shorter or equal length list returned
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)            # [2, 4]

# reduce -- collapse to one value -- single value returned
total = reduce(lambda x, y: x + y, numbers)
print(total)            # 15


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Function    Import needed?   Input          Output
#  ──────────────────────────────────────────────────────────────
#  map()       No               func, iter     map object (same length)
#  filter()    No               func, iter     filter object (shorter/equal)
#  reduce()    Yes (functools)  func, iter     single value
#
#  All three accept:
#  - A named function    map(cube, l)
#  - A lambda function   map(lambda x: x*3, l)
#  - A built-in          map(str.upper, l)
#
#  Common Rules:
#  ──────────────────────────────────────────────────────────────
#  1. map() and filter() return lazy objects -- wrap in list() to see output
#  2. Pass function NAME only -- cube not cube() -- no parentheses
#  3. filter() predicate must return True or False
#  4. reduce() needs at least 2 elements in the iterable
#  5. Avoid naming variables sum, min, max -- these are built-in functions
#  6. reduce() accepts an optional third argument as initial value
#
# ============================================================
