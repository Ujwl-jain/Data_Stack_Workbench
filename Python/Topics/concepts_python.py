'''
HERE THERE WILL BE ALL THE CONCEPTS RELATED TO PROGRAMMING WILL EXIST, WHICH ARE USED IN THE MODERN PROGRAMMING

THERE NAME, MEANING.

FOR EXAMPLE:

PALINDROME, MEANS 'DEFINATION AND ITS EXAMPLE'
FIBONACCI SERIES
GREGORIAN TRIANGLE PRGRAM
PASCAL TRIANGLE
A Caesar cipher

'''

'''
1. Ceasar cipher
A Caesar cipher is one of the oldest encryption techniques.
The idea is simple:
You take a piece of text and shift every letter forward by k positions in the alphabet
So if k = 3, then A → D, B → E, Z → C (it wraps around!)
'''

'''
2. ASCII NUMBER


# ---------------------- ASCII RANGES ----------------------

# ASCII → American Standard Code for Information Interchange

# It is a numeric representation of characters
# Every character (A-Z, a-z, 0-9, symbols) has a unique number

# Uppercase letters
# A-Z → 65 to 90

# Lowercase letters
# a-z → 97 to 122

# Digits
# 0-9 → 48 to 57

# Space
# ' ' → 32

# ---------------------- IMPORTANT POINTS ----------------------

# 1. ord() takes a single character only
# 2. chr() takes an integer only
# 3. ASCII is mainly used for character manipulation

'''

'''
3. How Shifting Works (ord + chr + % 26)
# -----------------------------------------------------------------------------
# Python gives us two tools:
#   ord(char)   → converts character to ASCII number  e.g. ord('A') = 65
#   chr(number) → converts ASCII number to character  e.g. chr(68)  = 'D'
#
# SHIFT FORMULA (3 steps):
#   Step 1 → Normalize to 0–25:  ord(char) - ord('A')
#   Step 2 → Add shift + wrap:   (normalized + k) % 26
#   Step 3 → Convert back:       result + ord('A')
#
# For UPPERCASE:  chr((ord(char) - ord('A') + k) % 26 + ord('A'))
# For LOWERCASE:  chr((ord(char) - ord('a') + k) % 26 + ord('a'))
#
# WHY % 26?
#   The alphabet has 26 letters. % 26 keeps the result within 0–25.
#   Example: 'Y' shifted by 3
#     ord('Y') - ord('A') = 24
#     (24 + 3) % 26       = 1    ← wraps around!
#     1 + ord('A')        = 66
#     chr(66)             = 'B'  
'''

'''
4. Palindrome
A palindrome is a string that reads the same forwards and backwards.
Examples:

"racecar" → palindrome ✅
"madam" → palindrome ✅
"hello" → NOT a palindrome ❌
'''

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
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  zip():
#  ──────────────────────────────────────────────────────────────
#  list(zip(a, b))              pairs elements as list of tuples
#  for x, y in zip(a, b)        unpack directly in loop
#  dict(zip(keys, values))      build dict from two lists
#  stops at shortest iterable   longer elements are dropped
#
#  Dict Comprehension:
#  ──────────────────────────────────────────────────────────────
#  {k: v for k, v in iterable}           basic
#  {k: v for k, v in iterable if cond}   with filter
#  {v: k for k, v in dict.items()}       swap keys and values
#  {k: f(v) for k, v in dict.items()}    transform values
#
# ============================================================
