# join() - it is a iterable method but string only

# Means take elements from iterable(string, list, tuple, dictonaries) and join them using a seperator like ' ' , ',' etc

#  syntax - "seperator".join(iterable)

# example:
word = ['I am','Ujjwal','Jain']
result = ' '.join(word)
print(result)

# RULES:
# 1. Elements must be string
# 2. Can be used with any iterable like tuple, list, string, dictonary

# Tuple:
T = ('1','2','3')
# Sets - order may vary as set is unordered
S = {'I','Love','God'}  
# Dictonary
D = {'a': 1, 'b':2}

r1 = '-'.join(T)
r2 = ' '.join(S) 
r3 = '-'.join(D)

# if value is needed from dict
r4 = ','.join(str(v) for v in D.values())

print(r1)
print(r2)
print(r3)
print(r4)

# ---------------------------------------------------------------------------------------------

# Split() - it is a string method

# Means - Break string into list

# syntax: string.split(seprator)

# example:
Text = 'I love python'
r= Text.split()
print(r)

# RULES:
# 1. Can be used only with string

# it can also split the string using character, 't' will be used as cutting point
r2 = Text.split('t')
print(r2)


# -------------------------------------------------------------------------------------------------------------
# Using both the split() and join() together  -  It is usefull for cleaning the string using various methods

# POINTS TO REMEMBER:
# 1.Split() is a string method which returns list
# 2.join() is a iterable method which works on any iterable as long as it is string
# 3. Split returns the list which pass to joins to convert it into a string or clean string


words = '  I Love  Python   '
result1 = words.split()
print(result1)

# then join( ) to remove the extra spacing in the string
result2 = ' '.join(result1)
print(result2)

# ---------------------------------------------------------------------------------

# Get() method - it is a dictonary methond

# synatax - dictonary.get(Key, default value)
# 1. if key exist, it returns the value 
# 2. if key not exist, it returns the default value
# example:

# if key exist
d1 = {'a' :5,'b':2,'c':4}
result3 = d1.get('a',0)
print(result3)

# if key not exist, it returns the default value
print(d1.get('d','Not exist'))

# BEST WAY TO REMEMBER
# if key exist:
#     returns the Value
# else:
#     return default value

# -----------------------------------------------------------------------------------------------------------------------

# sort() - sort is a list method

# sort is a list method, it sort the elements inside the list
#  it works only with list, and it change the orignial list 
# example:

list_sort=[4,1,5,62,7,2]
list_sort.sort()
print(list_sort)

# this will not work cause sort will happen inside the list and result will return as none

numbers = [3,1,2]
result_sort = numbers.sort()
print(result_sort)

# sorted() - it is iterable method works with any iterable list, tuple, dictonaries, string, sets

#  it is a built in function, it does not change the reat data but returns it as new sorted list for any iterable
#  means any iterable will get sorted but returns as list
#  usually sorting happens in ascending order but can use reverse as true to make it descending

# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — sorted() with key=len
# -----------------------------------------------------------------------------
# sorted(list, key=len)          → shortest first
# sorted(list, key=len, reverse=True)  → longest first
#
# key=len means: "use length as the measuring stick for sorting"
# NO () on len — you pass the function itself, not call it!
#   key=len    ✅  passing the function
#   key=len()  ❌  calling the function (gives error)
#
# Example:
#   sorted(["ab", "a", "abc", "b"], key=len)
#   → ["a", "b", "ab", "abc"]

list_sorted=[4,1,5,62,7,2]
result_sorted = sorted(list_sorted)
print(list_sorted)
print(result_sorted)

# Code to work sorted with different iteration

# list
list_sorted = ['python', 'is', 'my', 'love']
sorted_list = sorted(list_sorted)



# tuple
tuple_sorted = (5,10,9,11,2,1)
sorted_tuple = sorted(tuple_sorted)

# string
# Since uppercase letters come before lowercase letters, "Python" stays first.
string_sorted = 'Python is love a gg'
sorted_string = sorted(string_sorted.split())

s_str = 'list' 
sorted_strin2 = sorted(s_str)
print(sorted_strin2)

# set
set_sorted = {'python', 'is', 'love'}
sorted_set = sorted(set_sorted)

# dictionary, using reverse here to make the sorted items in descending order
# sorted(dictionary.items(), key=lambda x: x[1])
# basically it will sorted the dictionary based on either key or value, 
# .item() will create a list of tuple of key value pair, 
# lambda x:x[0 or 1] if 0 it will sort based on key else value
# by default dictonary are sorted based on key like sorted(dict.items()) 
dict_sorted = {'fruit' : 1, 'salad':9, 'veggies': 3}
sorted_dict = sorted(dict_sorted.items(), key= lambda x:x[0], reverse=True)


print(sorted_list)
print(sorted_tuple)
print(sorted_set)
print(sorted_string)
print(sorted_dict)

# ------------------------------------------------------------------
#  len()

# ------------------------------------------------------------------
# strip()