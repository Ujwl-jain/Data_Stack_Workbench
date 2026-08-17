# TUPLES:

'''
TUPLES are ordered collection, stores multiple data items,
stores within  '()', these are immutable means it can not be changed once created.

if we are working on a complex program we dont want a series of data item can not be changed 
then when we will use tuple,
'''

tuple1  = (1,2,3, 'string', True)
print(type(tuple1), tuple1)
print(tuple1[0])
print(tuple1[2])
print(tuple1[4])


if 'string' in tuple1:
    print("yes")
# this will not work as we can not change the tuple
# tuple1[0] = 90
# print(tuple1)

# ---------------- INDEXING IN TUPLE --------------------------

# Tuple is same as list for indexing
# Only difference → tuple is immutable (cannot change values)

tuple_ex = (1, 'ujjwal', "true", 2, True)


# Positive indexing
# Index starts from 0 and moves left → right

print(tuple_ex[1])  
# returns 'ujjwal'


# Negative indexing
# Starts from end of tuple

print(tuple_ex[-2])  
# returns 2


# Converting negative to positive indexing

print(tuple_ex[len(tuple_ex) - 2])
# len = 5 → 5 - 2 = 3 → tuple_ex[3]

print(tuple_ex[5 - 2])
print(tuple_ex[3])
# result → 2


# Rule:
# negative index = len(tuple) + negative_index


# ------------------ SLICING IN TUPLE -------------------

tuple_slice = (1,7,11,23,5,6,78,21,34)


# Print entire tuple
print(tuple_slice[:])
# same as tuple_slice[0:len(tuple_slice)]


# Basic slicing
print(tuple_slice[0:3])
print(tuple_slice[:3])      # default 0 before :
print(tuple_slice[1:])      # default end after :


# ---------------- NEGATIVE INDEXING ----------------

# len(tuple_slice) = 9

print(tuple_slice[:-2])
# means → tuple_slice[0 : len(tuple_slice) - 2]

print(tuple_slice[:len(tuple_slice) - 2])

print(tuple_slice[:9-2])

print(tuple_slice[:7])
# elements from index 0 → 6 (end not included)
# because step is negative but start < end
# direction mismatch


# ---------------- IMPORTANT BEHAVIOR ----------------

print(tuple_slice[-1:-5])
# returns empty tuple ()
# because default step = +1 and start > end


print(tuple_slice[-7:-2])
# works and returns elements


# ---------------- STEP / JUMP INDEX ----------------

# tuple[start : end : step]

print(tuple_slice[1:8:2])
# step = 2 → skip one element

print(tuple_slice[1:8:-2])
# returns empty tuple ()
# because direction mismatch
# because step is negative but start < end
# direction mismatch


# ---------------- IMMUTABILITY (IMPORTANT) ----------------

# tuple elements cannot be changed

# this will give error
# tuple_slice[0] = 100


# slicing always returns a NEW tuple

new_tuple = tuple_slice[1:4]

print(new_tuple)
# (7, 11, 23)


# ------------------------------ Operations on tuple ----------------------------
# tuples method

# though we can not change the tuple but some method can use to manipulate tuple but not in a direct way
# why not direct way
'''
we first need to convert the tuple into list do the changes and convert back to tuple again
'''
countries = ("spain", "italy", "india" ,"france")
temp = list(countries)
temp.append("england")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# however we can concatinate the 2 tuples together cause we are creating new tuple consist of 2 tuple not changing in exsiting tuple
countries1 = ("India", "finland")
countries2 = ("Sri lanka", "australia")

worldcupsemi = countries1 + countries2
print(worldcupsemi)

# Methods ->
tuple1 = (1,23,51, 1,2,1,4,6,1, 'Ujjwal', 'JAIN')
# 1. Count()
# returns the number of times the given element appears in the tuple

count_t = tuple1.count("JAIN")
print(count_t)

# # Index()
# return the first occurence of given element from the tuple

index_t = tuple1.index("JAIN")
print(index_t)

# synatx - tuple.index(element, start, end)
index_t2 = tuple1.index(1, 4,8) # means it will slice it from indexing 4 to 8


# length()
res1 = len(tuple1)
print(res1)

# we can perform any method from list once we convert the tuple to list.


# Namedtuples(need to learn this)
