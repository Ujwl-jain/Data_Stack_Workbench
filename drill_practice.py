# INTERMEDIATE DRILL 3 — Enhanced Vowel & Consonant Count
# Problem:

# Given a string:

# s = "Data Analyst!"

# Requirements:

# Count vowels (a, e, i, o, u), case-insensitive

# Count consonants (all alphabetic letters not vowels)

# Ignore special characters, numbers, or spaces

# Return total vowels and consonants


c_vowel = 0
c_consonant = 0

s = 'Data Analyst'.lower()

vowels = ['a','e','i','o','u']
for char in s:
    if char in vowels:
        c_vowel = c_vowel + 1
    
    elif char.isalpha() and char not in vowels:
        c_consonant = c_consonant +1
    
    else:
        pass

print("total count of vowels: ", c_vowel)
print("total count of consonant: ", c_consonant)

# ---------------------------------------------------------------

# Increase Difficulty Slightly

# New Drill (Level Up):

# Given:

# s = "Data Analyst 2026!!!"

# Return:

# Total vowels

# Total consonants

# Total digits

# Total special characters (everything that is NOT letter or digit)

# c_consonant, c_vowel, c_digit, c_sp_char = 0, put the counter as 0

# just asking, you did not said that ignore space so i am counting space in special character

#  create the vowels list
# after that loop starts, with if elif conditions using if -> char is vowol, elif -> string isaplha() , elif -> string isdigit(), else -> string isspecial charater()

c_vowel = c_consonant = c_digit = c_sp_char = 0
s = 'Data Analyst 2026!!!'.lower()

vowels = ['a','e','i','o','u']
for char in s:
    if char in vowels:
        c_vowel = c_vowel + 1
    
    elif char.isalpha() and char not in vowels:
        c_consonant = c_consonant +1

    elif char.isdigit():
        c_digit = c_digit +1
    
    else:
        c_sp_char = c_sp_char +1

print("total count of vowels: ", c_vowel)
print("total count of consonant: ", c_consonant)
print("total count of digit: ", c_digit)
print("total count of sp character: ", c_sp_char)

# ----------------------------------------------------------------------------


# Next Drill (slightly more algorithmic):

# Given a string:

# s = "programming"

# Return a dictionary showing frequency of each character.

# Expected:

# {'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}

d_freq = {}

s = 'programming'
for char in s:
    if char not in d_freq:
        d_freq[char] = 1
    else:
        d_freq[char] += 1

print(d_freq)

# Now that we have:

# {'p':1,'r':2,'o':1,'g':2,'a':1,'m':2,'i':1,'n':1}

# New problem:

# Find the character with the highest frequency.

# Expected result for "programming":

# r → 2
# g → 2
# m → 2

# But if we want only one max character, we return the first one encountered.

# Explain your logic first, not code.

max_ch = '' 
max_c = 0

for key, value in d_freq.items():
    if value > max_c:
        max_ch = key
        max_c = value
    
    else:
        pass

# ---------------------------------------------------------------------
# Reminder of the goal:

# Input:

# s = "programming"

# Step 1 → build frequency dictionary

# {'p':1, 'r':2, 'o':1, 'g':2, 'a':1, 'm':2, 'i':1, 'n':1}

# Step 2 → group characters by frequency

# Expected structure:

# {
# 1: ['p','o','a','i','n'],
# 2: ['r','g','m']
# }

# Your task:

# build freq_dict

# build group_freq

d_freq = {}
group_freq = {}

s = 'programming'
for char in s:
    if char not in d_freq:
        d_freq[char] = 1
    else:
        d_freq[char] += 1

for char,value in d_freq.items():
    if value not in group_freq:
        group_freq[value] = [char]
    
    else:
        group_freq[value].append(char)


# ---------------------------------------------
# Next Drill (Slightly Harder)

# Input:

# s = "aaabbccccdd"

# Expected Output:

# {
# 3:['a'],
# 2:['b','d'],
# 4:['c']
# }

# Rules:

# 1️⃣ First build frequency dictionary
# 2️⃣ Then group characters by count
# 3️⃣ Same structure you used

from collections import Counter
d_freq = {}
group_freq = {}

s = 'aaabbccccdd'

d_freq = Counter(s)
g_freq = {}
for char,value in d_freq.items():
    if value not in g_freq:
        g_freq[value] = [char]
    
    else:
        g_freq[value].append(char)

print(g_freq)


# -------------------------------------------------------------
# Next Drill (Now we increase difficulty)

# Input:

# s = "python is powerful and python is easy"

# Goal:

# Return word frequency.

# Expected:

# {
# 'python':2,
# 'is':2,
# 'powerful':1,
# 'and':1,
# 'easy':1
# }
# Rules

# Do it without Counter first.

# Steps:

# 1️⃣ split the sentence
# 2️⃣ loop through words
# 3️⃣ build dictionary frequency

# Write the code.

s = "python is powerful and python is easy"

# using counter
a=Counter(s.split())

# using loop and if else
w_freq = {}

for word in s.split():
    if word not in w_freq:
        w_freq[word] = 1
    else:
        w_freq[word] += 1

print(a)
print(w_freq)


# --------------------------------------------------------------
# Input:

# s = "data science data engineering data analytics"

# Step 1
# Build word frequency dictionary.

# Expected:

# {
# 'data':3,
# 'science':1,
# 'engineering':1,
# 'analytics':1
# }

# Step 2
# Sort it by frequency descending.

# Expected:

# [
# ('data',3),
# ('science',1),
# ('engineering',1),
# ('analytics',1)
# ]
# Your Task

# Write the full code:

# 1️⃣ Build frequency dictionary
# 2️⃣ Sort by value using sorted()


s = "data science data engineering data analytics"

# using counter
a=Counter(s.split())

# using loop and if else
w_freq = {}

for word in s.split():
    if word not in w_freq:
        w_freq[word] = 1
    else:
        w_freq[word] += 1

sorted_w  = sorted(w_freq.items(), key = lambda x:x[1], reverse = True)

print(a)
print(w_freq)
print(sorted_w)