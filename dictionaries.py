# ============================================================
#                   DICTIONARIES IN PYTHON
# ============================================================
# A dictionary stores data in KEY-VALUE pairs.
# Used to create a mapping between two related things.
# Example: a person's name mapped to their age, a word to its meaning.
#
# PROPERTIES:
# - Ordered (maintains insertion order since Python 3.7+)
# - Mutable (can be changed after creation)
# - Keys must be UNIQUE -- duplicate keys overwrite the old value
# - Keys must be IMMUTABLE (string, int, tuple) -- lists cannot be keys
# - Values can be ANY data type and can repeat
#
# SYNTAX:
#   dict_name = { key1: value1, key2: value2 }
# ============================================================


# ------------------------------------------------------------
# Creating a Dictionary
# ------------------------------------------------------------

dict1 = {
    'ujjwal': 'Human',
    'bed': 'object'
}

# other ways to create a dictionary:
empty_dict = {}                         # empty dictionary
dict2 = dict(name='ujjwal', age=21)     # using dict() constructor
print(dict2)        # {'name': 'ujjwal', 'age': 21}


# ============================================================
#                   ACCESSING ITEMS
# ============================================================

# ------------------------------------------------------------
# Accessing by key -- two ways
# ------------------------------------------------------------

print(dict1['ujjwal'])          # 'Human'
# NOTE: raises KeyError if key does not exist
# print(dict1['unknown'])       # KeyError: 'unknown'

print(dict1.get('ujjwal'))      # 'Human'
print(dict1.get('unknown'))     # None -- no error, safe to use

# get() with a default fallback value:
print(dict1.get('unknown', 'not found'))    # 'not found'
# useful when you want a custom message instead of None


# ------------------------------------------------------------
# Accessing all keys, values, items
# ------------------------------------------------------------

print(dict1.keys())             # dict_keys(['ujjwal', 'bed'])
print(dict1.values())           # dict_values(['Human', 'object'])
print(dict1.items())            # dict_items([('ujjwal', 'Human'), ('bed', 'object')])

# NOTE: keys(), values(), items() return VIEW objects, not lists.
# They reflect changes made to the dictionary in real time.
# Convert to list if you need a static snapshot:
print(list(dict1.keys()))       # ['ujjwal', 'bed']


# ------------------------------------------------------------
# Looping through a Dictionary
# ------------------------------------------------------------

# loop over keys only
for key in dict1.keys():
    print(f'{key} : {dict1[key]}')

# loop over values only
for value in dict1.values():
    print(value)

# loop over key-value pairs together (most common)
for key, value in dict1.items():
    print(f'{key} : {value}')


# ------------------------------------------------------------
# Checking if a key exists
# ------------------------------------------------------------

if 'ujjwal' in dict1:
    print("key exists")        # key exists

if 'unknown' not in dict1:
    print("key not found")     # key not found

# NOTE: 'in' checks keys only, not values


# ============================================================
#               ADDING AND MODIFYING ITEMS
# ============================================================

person = {'name': 'ujjwal', 'age': 21}

# add a new key-value pair
person['city'] = 'pune'
print(person)       # {'name': 'ujjwal', 'age': 21, 'city': 'pune'}

# modify an existing value
person['age'] = 22
print(person)       # {'name': 'ujjwal', 'age': 22, 'city': 'pune'}

# adding a duplicate key -- overwrites the old value
person['name'] = 'ram'
print(person)       # {'name': 'ram', 'age': 22, 'city': 'pune'}


# ============================================================
#                   DICTIONARY METHODS
# ============================================================


# ------------------------------------------------------------
# update()
# ------------------------------------------------------------
# Merges another dictionary (or key-value pairs) into the existing one.
# If a key already exists -- its value is OVERWRITTEN.
# If a key is new -- it is ADDED to the end.
# Modifies the original dictionary in-place.

dict_update = {122: 45, 123: 89, 124: 69, 167: 78}
ep2 = {222: 78, 566: 90}

dict_update.update(ep2)
print(dict_update)      # {122: 45, 123: 89, 124: 69, 167: 78, 222: 78, 566: 90}

# update with overlapping keys -- overwrites:
dict_update.update({122: 999})
print(dict_update)      # {122: 999, 123: 89, ...} <- 122's value changed


# ------------------------------------------------------------
# get()
# ------------------------------------------------------------
# Returns the value for a given key.
# Returns None (or a custom default) if key does not exist.
# Does NOT raise a KeyError -- safer than direct [] access.

scores = {'math': 90, 'english': 85}
print(scores.get('math'))               # 90
print(scores.get('science'))            # None
print(scores.get('science', 0))         # 0  <- custom default


# ------------------------------------------------------------
# keys(), values(), items()
# ------------------------------------------------------------
# keys()   -- returns all keys as a view object
# values() -- returns all values as a view object
# items()  -- returns all key-value pairs as (key, value) tuples

data = {'a': 1, 'b': 2, 'c': 3}
print(data.keys())      # dict_keys(['a', 'b', 'c'])
print(data.values())    # dict_values([1, 2, 3])
print(data.items())     # dict_items([('a', 1), ('b', 2), ('c', 3)])


# ------------------------------------------------------------
# copy()
# ------------------------------------------------------------
# Returns a SHALLOW COPY of the dictionary.
# Changes to the copy do NOT affect the original (for flat dicts).
# For nested dicts, use copy.deepcopy() for a fully independent copy.

original = {'name': 'ujjwal', 'age': 21}
copy_dict = original.copy()
copy_dict['name'] = 'ram'

print(original)         # {'name': 'ujjwal', 'age': 21}  <- unchanged
print(copy_dict)        # {'name': 'ram', 'age': 21}


# ------------------------------------------------------------
# setdefault()
# ------------------------------------------------------------
# Returns the value of a key if it EXISTS.
# If the key does NOT exist -- inserts it with the given default value.
# Useful for safely initializing keys without overwriting existing ones.

info = {'name': 'ujjwal'}
info.setdefault('age', 21)      # key doesn't exist -> inserts age: 21
print(info)             # {'name': 'ujjwal', 'age': 21}

info.setdefault('name', 'ram')  # key EXISTS -> does NOT overwrite
print(info)             # {'name': 'ujjwal', 'age': 21}  <- name unchanged


# ------------------------------------------------------------
# fromkeys()
# ------------------------------------------------------------
# Creates a NEW dictionary from a sequence of keys.
# All keys get the SAME default value (None if not specified).
# Called on the dict class itself, not on an instance.

keys = ['name', 'age', 'city']
new_dict = dict.fromkeys(keys)
print(new_dict)         # {'name': None, 'age': None, 'city': None}

new_dict2 = dict.fromkeys(keys, 'unknown')
print(new_dict2)        # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# useful for initializing a dictionary with placeholder values


# ------------------------------------------------------------
# clear()
# ------------------------------------------------------------
# Removes ALL items from the dictionary.
# The dictionary still EXISTS -- it just becomes empty {}.
# Different from del dict_name which removes the variable entirely.

dict_clear = {122: 45, 123: 89, 124: 69, 167: 78}
dict_clear.clear()
print(dict_clear)       # {}  <- empty, variable still exists


# ------------------------------------------------------------
# pop()
# ------------------------------------------------------------
# Removes a specific key and RETURNS its value.
# Raises KeyError if the key does not exist.
# Pass a default as second argument to avoid the error.

dict_pop = {122: 45, 123: 89, 124: 69, 167: 78}
removed = dict_pop.pop(122)
print(removed)          # 45   <- the value that was removed
print(dict_pop)         # {123: 89, 124: 69, 167: 78}

# safe pop with default -- no KeyError if key is missing:
val = dict_pop.pop(999, 'not found')
print(val)              # 'not found'


# ------------------------------------------------------------
# popitem()
# ------------------------------------------------------------
# Removes and returns the LAST inserted key-value pair as a tuple.
# Does NOT take any arguments -- it always removes the last item.
# Raises KeyError if the dictionary is empty.
# NOTE: your original code passed 122 as argument -- that is wrong.

dict_popitem = {122: 45, 123: 89, 124: 69, 167: 78}
removed_item = dict_popitem.popitem()   # no argument needed
print(removed_item)     # (167, 78)   <- last item removed as tuple
print(dict_popitem)     # {122: 45, 123: 89, 124: 69}


# ------------------------------------------------------------
# del keyword
# ------------------------------------------------------------
# del is a Python keyword, not a method.
# Two uses:
#   del dict_name         -- deletes the entire dictionary variable
#   del dict_name[key]    -- deletes a specific key-value pair

dict_del = {122: 45, 123: 89, 124: 69, 167: 78}

del dict_del[122]           # removes only the key 122
print(dict_del)             # {123: 89, 124: 69, 167: 78}

# del dict_del              # removes the entire variable
# print(dict_del)           # NameError: name 'dict_del' is not defined

# ============================================================
#                   DICTIONARY COMPREHENSION
# ============================================================
# A concise way to create a dictionary in one line.
# Same idea as list comprehension but produces a dict.
#
# SYNTAX:
#   {key_expr : value_expr for item in iterable}
#   {key_expr : value_expr for item in iterable if condition}
# ============================================================

# regular way -- building a dict with a loop:
squares = {}
for i in range(1, 6):
    squares[i] = i * i
print(squares)      # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# same thing with dict comprehension:
squares = {i: i * i for i in range(1, 6)}
print(squares)      # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# with a condition -- only even numbers:
even_squares = {i: i * i for i in range(1, 11) if i % 2 == 0}
print(even_squares) # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# swapping keys and values:
original = {'name': 'ujjwal', 'city': 'pune', 'lang': 'python'}
swapped  = {value: key for key, value in original.items()}
print(swapped)      # {'ujjwal': 'name', 'pune': 'city', 'python': 'lang'}

# from two lists using zip -- clean one liner:
keys   = ['name', 'age', 'city']
values = ['ujjwal', 21, 'pune']
person = {k: v for k, v in zip(keys, values)}
print(person)       # {'name': 'ujjwal', 'age': 21, 'city': 'pune'}

# transforming values -- uppercasing all values:
data    = {'name': 'ujjwal', 'city': 'pune', 'lang': 'python'}
uppered = {k: v.upper() for k, v in data.items()}
print(uppered)      # {'name': 'UJJWAL', 'city': 'PUNE', 'lang': 'PYTHON'}

# filtering keys -- keep only items where value is above 50:
marks = {'maths': 90, 'english': 45, 'science': 78, 'sst': 38}
passed = {sub: mark for sub, mark in marks.items() if mark >= 50}
print(passed)       # {'maths': 90, 'science': 78}



# ============================================================
#                    QUICK REFERENCE SUMMARY
# ============================================================
#
#  Method/Keyword     Returns            Modifies?    Use When
#  ──────────────────────────────────────────────────────────────────
#  dict[key]          Value              No           Access value, raises KeyError if missing
#  get(key)           Value or None      No           Safe access, no error if missing
#  get(key, default)  Value or default   No           Access with a fallback value
#  keys()             View of keys       No           Iterate or check all keys
#  values()           View of values     No           Iterate or check all values
#  items()            View of pairs      No           Iterate key-value pairs together
#  update(dict2)      None               Yes          Merge another dict in
#  copy()             Shallow copy       No           Duplicate safely
#  setdefault(k, v)   Value              Yes          Init key only if not already there
#  fromkeys(seq, v)   New dictionary     No           Build dict from a list of keys
#  clear()            None               Yes          Wipe all items, keep variable
#  pop(key)           Removed value      Yes          Remove by key, get its value back
#  popitem()          Removed (k,v)      Yes          Remove last inserted item
#  del dict[key]      Nothing            Yes          Delete specific key-value pair
#  del dict           Nothing            Yes          Delete entire dictionary variable
#
#  Common Rules:
#  ──────────────────────────────────────────────────────────────────
#  1. Keys must be unique -- duplicates overwrite the old value
#  2. Keys must be immutable -- strings, ints, tuples are fine
#  3. Use get() over [] when unsure if a key exists
#  4. popitem() takes NO arguments -- pop() takes a key argument
#  5. clear() empties the dict but keeps the variable alive
#  6. del removes the variable entirely, clear() does not
#
# ============================================================
