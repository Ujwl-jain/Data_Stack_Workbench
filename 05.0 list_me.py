# LIST

# it is a collection of data items
# they store mupltiple item in a single variable
# it is seperated by comma(,)and within a squar bracket-[]
# it can be change/mutable, we can alter the list
# indexing starts from 0 as well here 
# example:

list_ex = [1, 'ujjwal', "true", 2, True]
print(list_ex) # returns the list
print(type(list_ex)) # returns its type
print(list_ex[1]) # returns the 2nd item of list as the indexing is 1

# ---------------- INDEXING IN LIST --------------------------
# Postive indexing - 
list_ex = [1, 'ujjwal', "true", 2, True]
print(list_ex[1]) # returns the 2nd item of list as the indexing is 

# negative indexing - Negative indexing starts from the end of the list 
print(list_ex[-2]) #negetive indexing looks from back 

print(list_ex[len(list_ex) -2 ]) 
# lets just put the len of list by default to make it easier
# len(list_ex) = 5
# so it becomes: 5 - 2 = 3
# therefore → list_ex[3]

print(list_ex[5-2]) #it becomes like this 
print(list_ex[3]) #so -2 will give the value at indexing 3,

# it is how we converted negative to positive  

# -----------------------------------------------------------------------
list_l = [10,20,30,40,50]

# a, b = b, a  ← Python lets you swap two things in ONE line like this!
list_l[0], list_l[-1] = list_l[-1] , list_l[0]
print(list_l)


# ------------------ RANGE OF INDEXING OR SLICING OF LIST -------------------
list_slice = [1,7,11,23,5,6,78,21,34]

# Index:      0  1  2  3  4  5  6  7  8
# Values:     1  7 11 23  5  6 78 21 34

# Negative:  -9 -8 -7 -6 -5 -4 -3 -2 -1


# Print the entire list
print(list_slice[:])

# both are same as 0 is by default if no value is given before :
print(list_slice[0:3]) 

print(list_slice[:3]) # by default 0 before :
print(list_slice[1:]) # by default end of list after :


# Negative indexing 

# here put a len(list) to before ':' make it easier for yourself
print(list_slice[:-2]) #this becomes
print(list_slice[:len(list_slice) - 2]) # this becomes list_slice[0 : len(list_slice) - 2]
print(list_slice[:9-2]) 
print(list_slice[:7]) 
# elements from index 0 → 6 will be returned
# index 7 is NOT included (end index is always excluded)

# that is how you convert a negative indexing to positive


# Reversing a list
print(list_slice[::-1]) 

# --------------------------------------------

print(list_slice[-1:-5])
# returns [] (empty list)

# because slicing moves forward by default (step = +1)
# but here start > end so nothing is returned


print(list_slice[-7:-2])
# this works and returns elements


# Important rule:
# slicing direction depends on STEP or jumpindex
# in my language if start and end are negative either convert it to positive by adding len(list),
# or start has to be less than end

# -----------------------------------------

# list[start : end : step or jumpindex]
# it will return the elements by skipping 1
# to make it easier -lets just assume, by default jumpindex is 1 if moving forward, or -1 if moving backwards
# negative indexing works same here too.

print(list_slice[1:8:2])
# step = 2
# returns elements by skipping one element

print(list_slice[1:8:-2]) 
# returns []

# because step is negative but start < end
# direction mismatch

print(list_slice[8:1:-2]) # this moves backward and skip 1 element
# this will work cause start> end

# -----------------------------------------------

# IMPORTANT RULE
# If step or jumpindex is positive:
#     start should be smaller than end

# If step or jumpindex is negative:
#     start should be greater than end




# ------------------ LIST COMPREHENSION ----------------------

# ---------------------- LIST COMPREHENSION ----------------------

# List comprehension is used to create a new list from another iterable
# such as a list, tuple, dictionary, set, string, or any iterable object.

# It provides a shorter and more Pythonic way of writing loops
# when creating lists.


# Syntax
# new_list = [expression for item in iterable if condition]


# expression
# The operation applied to each item before adding it to the new list

# item
# Variable representing each element in the iterable

# iterable
# Any object that can be looped over (list, tuple, string, set, etc.)

# condition (optional)
# Filters elements; only items that satisfy the condition are added


# Example 1: simple list comprehension
nums = [1,2,3,4,5]

squares = [x*x for x in nums]

print(squares)
# [1,4,9,16,25]


# Example 2: with condition
nums = [1,2,3,4,5,6]

even_nums = [x for x in nums if x % 2 == 0]

print(even_nums)
# [2,4,6]


# Example 3: using string iterable
word = "python"

letters = [char for char in word]

print(letters)
# ['p','y','t','h','o','n']


# Example 4: using split() to convert string to list
sentence = "Python is powerful"

words = [word for word in sentence.split()]

print(words)
# ['Python','is','powerful']


# ------------------------------------ LIST METHODS -----------------------------------------


# ------------------------------------------------------------
# 1. append()
# ------------------------------------------------------------
# Adds a SINGLE item to the END of the list.
# Modifies the original list in-place (returns None).
# NOTE: appending a list adds it as ONE nested element.
 
list_example = [1, 12, 45, 11, 2, 0, 6]
list_example.append(9)
print(list_example)        # [1, 12, 45, 11, 2, 0, 6, 9]
 
list_example.append([10, 11])   # adds as a nested list
print(list_example)        # [1, 12, 45, 11, 2, 0, 6, 9, [10, 11]]
 
 
# ------------------------------------------------------------
# 2. sort()
# ------------------------------------------------------------
# Sorts the list IN-PLACE in ascending order by default.
# Use reverse=True for descending order.
# Returns None — it does NOT create a new list.
# TIP: Use sorted(list) if you want a NEW sorted list instead.
 
list_sort = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
list_sort.sort()                    # ascending order
print(list_sort)           # [1, 3, 3, 3, 4, 4, 4, 12, 45, 512]
 
list_sort.sort(reverse=True)        # descending order
print(list_sort)           # [512, 45, 12, 4, 4, 4, 3, 3, 3, 1]
 
# sorted() → returns a new list, original stays unchanged
original = [5, 2, 8, 1]
new_sorted = sorted(original)
print(original)            # [5, 2, 8, 1]   ← unchanged
print(new_sorted)          # [1, 2, 5, 8]   ← new sorted list
 
 
# ------------------------------------------------------------
# 3. reverse()
# ------------------------------------------------------------
# Reverses the list IN-PLACE (does NOT sort — just flips order).
# Returns None.
#     COMMON MISTAKE: forgetting () makes it do nothing!
 
list_rev = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
# list_rev.reverse    ←   WRONG: just references method, does nothing
list_rev.reverse()                  #  correct
print(list_rev)            # [4, 3, 4, 3, 1, 45, 512, 4, 12, 3]
 
 
# ------------------------------------------------------------
# 4. index()
# ------------------------------------------------------------
# Returns the INDEX of the FIRST occurrence of a given item.
# Raises ValueError if the item is not found.
 
list_index = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
print(list_index.index(1))          # 5  (1 is at position 5)
print(list_index.index(3))          # 0  (first 3 is at position 0)
 
# Optional: index(item, start, end) — search within a slice
print(list_index.index(3, 1))       # 6  (next 3 after index 1)
 
 
# ------------------------------------------------------------
# 5. count()
# ------------------------------------------------------------
# Returns the NUMBER OF TIMES an item appears in the list.
# Returns 0 if item is not found (does NOT raise an error).
 
list_count = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
print(list_count.count(3))          # 3  (3 appears 3 times)
print(list_count.count(4))          # 3  (4 appears 3 times)
print(list_count.count(99))         # 0  (not in list)
 
 
# ------------------------------------------------------------
# 6. copy()
# ------------------------------------------------------------
# Returns a SHALLOW COPY of the list.
# Changes to the copy do NOT affect the original list.
#     SHALLOW means: nested lists/objects are still SHARED.
#     Use copy.deepcopy() for a fully independent copy.
 
list_copy = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
m_copy = list_copy.copy()
m_copy[0] = 'ujjwal'
print(m_copy)              # ['ujjwal', 12, 4, 512, 45, 1, 3, 4, 3, 4]
print(list_copy)           # [3, 12, 4, 512, 45, 1, 3, 4, 3, 4] ← unchanged
 
# Shallow copy warning with nested lists:
import copy
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0][0] = 99
print(nested)              # [[99, 2], [3, 4]] ← inner list IS affected!
 
deep = copy.deepcopy(nested)
deep[0][0] = 0
print(nested)              # [[99, 2], [3, 4]] ← inner list NOT affected 
 
 
# ------------------------------------------------------------
# 7. insert()
# ------------------------------------------------------------
# Inserts an item at a SPECIFIC INDEX.
# All elements from that index onward shift to the right.
# Syntax: list.insert(index, item)
 
list_insert = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
list_insert.insert(3, 'yayaya')     # insert at index 3
print(list_insert)         # [3, 12, 4, 'yayaya', 512, 45, 1, 3, 4, 3, 4]
 
# insert at start
list_insert.insert(0, 'start')
print(list_insert)         # ['start', 3, 12, 4, 'yayaya', 512, ...]
 
# insert at end (same as append)
list_insert.insert(len(list_insert), 'end')
print(list_insert[-1])     # 'end'
 
 
# ------------------------------------------------------------
# 8. extend()
# ------------------------------------------------------------
# Adds ALL ITEMS from another iterable (list, tuple, set, etc.)
# to the END of the existing list.
# Modifies the original list in-place (returns None).
#     DIFFERENCE from append():
#     append([4,5]) → adds [4,5] as ONE element (nested)
#     extend([4,5]) → adds 4 and 5 as SEPARATE elements
 
list_extend = [3, 12, 4, 512, 45, 1, 3, 4, 3, 4]
list_extended = ['a', 'b', 'c']
list_extend.extend(list_extended)
print(list_extend)         # [3, 12, 4, 512, 45, 1, 3, 4, 3, 4, 'a', 'b', 'c']
 
# extend works with any iterable:
list_extend.extend((10, 20))        # tuple
list_extend.extend("XY")           # string → adds 'X', 'Y' separately
print(list_extend[-4:])    # [10, 20, 'X', 'Y']
 
 
# ------------------------------------------------------------
# 9. Concatenation using + operator
# ------------------------------------------------------------
# Joins two lists and returns a BRAND NEW list.
# Original lists remain UNCHANGED.
# Unlike extend(), this does NOT modify either list in-place.
 
a = [1, 2, 4]
b = [3, 4, 6]
c = a + b
print(a)                   # [1, 2, 4]       ← unchanged
print(b)                   # [3, 4, 6]       ← unchanged
print(c)     

# ------------------------------------------------------------
# 10. remove()
# ------------------------------------------------------------
# Removes the FIRST OCCURRENCE of a given item from the list.
# Modifies the list in-place (returns None).
# ⚠️  Raises ValueError if the item is NOT found in the list.
# ⚠️  Only removes the FIRST match — not all duplicates.
 
list_remove = [3, 12, 4, 3, 45, 1, 3]
list_remove.remove(3)               # removes first 3 only
print(list_remove)         # [12, 4, 3, 45, 1, 3] ← only first 3 is gone
 
# to remove ALL occurrences, use a loop or list comprehension:
list_remove2 = [3, 12, 4, 3, 45, 1, 3]
list_remove2 = [x for x in list_remove2 if x != 3]
print(list_remove2)        # [12, 4, 45, 1] ← all 3s removed
 
# ⚠️  ValueError example (commented out to avoid crashing):
# list_remove.remove(999)  # ❌ ValueError: list.remove(x): x not in list
 
 
# ------------------------------------------------------------
# 11. pop()
# ------------------------------------------------------------
# Removes AND RETURNS the item at the given index.
# Defaults to the LAST item if no index is provided.
# ⚠️  Raises IndexError if the index is out of range.
# KEY DIFFERENCE from remove():
#     remove(x) → finds item by VALUE, returns None
#     pop(i)    → finds item by INDEX, returns the removed item
 
list_pop = [3, 12, 4, 512, 45, 1]
popped = list_pop.pop()             # removes & returns last item
print(popped)              # 1
print(list_pop)            # [3, 12, 4, 512, 45]
 
popped_at = list_pop.pop(2)         # removes & returns item at index 2
print(popped_at)           # 4
print(list_pop)            # [3, 12, 512, 45]
 
# common use case: pop() is used to implement stacks (LIFO)
stack = [1, 2, 3, 4]
stack.append(5)             # push
print(stack.pop())          # pop → 5  (last in, first out)
 
 
# ------------------------------------------------------------
# 12. clear()
# ------------------------------------------------------------
# Removes ALL items from the list.
# The list still EXISTS — it just becomes empty [].
# ⚠️  DIFFERENCE from del:
#     list.clear() → empties the list, list object still exists
#     del list      → deletes the entire list variable completely
 
list_clear = [3, 12, 4, 512, 45, 1]
list_clear.clear()
print(list_clear)          # []  ← empty list, variable still exists
 
# del comparison (commented out):
# del list_clear            # after this, accessing list_clear raises NameError
 
#  13. Map()    

# map(what function to apply, which list)
# list(map(int, list_s))

# # same as saying:
# # "apply int() to every item in list_s"

# map(function, list)   # 1. takes a function and a list
#                       # 2. applies function to every item
# list(map(...))        # 3. always wrap with list() to get usable result

# ============================================================
#                        zip()
# ============================================================
# Combines two or more iterables element by element into tuples.
# Returns a zip object -- convert to list to see the result.
# Stops at the SHORTEST iterable if lengths are unequal.
#
# SYNTAX:
#   zip(iterable1, iterable2, ...)
# ============================================================

names  = ['ujjwal', 'ram', 'shyam']
scores = [95, 87, 76]
grades = ['A', 'B', 'C']

# basic zip -- pairs elements by position:
zipped = list(zip(names, scores))
print(zipped)       # [('ujjwal', 95), ('ram', 87), ('shyam', 76)]

# zip three iterables:
zipped3 = list(zip(names, scores, grades))
print(zipped3)      # [('ujjwal', 95, 'A'), ('ram', 87, 'B'), ('shyam', 76, 'C')]

# looping over zip directly -- most common use:
for name, score in zip(names, scores):
    print(f"{name} scored {score}")
# ujjwal scored 95
# ram    scored 87
# shyam  scored 76

# unequal lengths -- stops at shortest:
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
print(list(zip(a, b)))      # [(1, 'a'), (2, 'b'), (3, 'c')]  <- 4,5 are dropped

# converting two lists into a dictionary using zip:
keys   = ['name', 'age', 'city']
values = ['ujjwal', 21, 'pune']
person = dict(zip(keys, values))
print(person)       # {'name': 'ujjwal', 'age': 21, 'city': 'pune'}
 
# ============================================================
#                    QUICK REFERENCE SUMMARY
# ============================================================
#
#  Method/Op        Modifies Original?   Returns              Use When
#  ──────────────────────────────────────────────────────────────────────
#  append(x)        ✅ Yes               None                 Add 1 item to end
#  sort()           ✅ Yes               None                 Sort in-place
#  sorted()         ❌ No                New list             Sort without changing original
#  reverse()        ✅ Yes               None                 Flip order in-place
#  index(x)         ❌ No                Index (int)          Find position of item
#  count(x)         ❌ No                Count (int)          Count occurrences
#  copy()           ❌ No                Shallow copy         Duplicate list safely
#  insert(i, x)     ✅ Yes               None                 Add item at specific index
#  extend(iter)     ✅ Yes               None                 Add many items to end
#  list1 + list2    ❌ No                New list             Merge into new list
#  remove(x)        ✅ Yes               None                 Remove first match by value
#  pop(i)           ✅ Yes               Removed item         Remove & retrieve by index
#  clear()          ✅ Yes               None                 Wipe list completely
