# 1️. Reverse Words in a Sentence

# Write a program that takes a sentence from the user and reverses the order of words.

# Example
# Input

# I love python

# Output

# python love I

# Concepts used:

# string methods

# list

# slicing

# join()

s_reverse = 'I love python'

# Solution 1
reverse_s = s_reverse.split()

s = reverse_s[::-1]

s_result = " ".join(s)

print(s_result)

# Solution 2 - but it will reverse the string not exactly how question wants though

reverse_s = s_reverse[::-1]
print(reverse_s) # nohtyp evol I

# ------------------------------------------------------
# 2️. Find Second Largest Number in List

# Given a list of numbers, find the second largest number.

# Example

# Input: [10, 45, 23, 67, 67, 12]
# Output: 45

# Concepts:
# list
# sorting
# remove duplicates
# if conditions

sec_lar = [10, 45, 23, 67, 67, 12]
list_dupl = list(set(sec_lar))
print(list_dupl)
list_dupl.sort()
print(list_dupl)
print(list_dupl[-2])

# --------------------------------------------------------
# 3. Palindrome Checker

# Check if a string is a palindrome.

# Example

# Input: madam
# Output: Palindrome

# Concepts:

# slicing

# if else

# strings

str_palindrome = 'madam'
if str_palindrome == str_palindrome[::-1]:
    print('palindrome')
else:
    print("not palindrom")

# -----------------------------------------------------------------------------
# 4. Count Vowels and Consonants

# Take a string from the user and count:

# number of vowels

# number of consonants

# Example

# Input: hello
# Output:
# Vowels: 2
# Consonants: 3

# Concepts:

# string

# if-else

# loops

# membership (in)

str1 = 'My self ujjwal jain, I am 24 years old'
str_vowels = str_consonant = str_extra = 0
vowels = ['a','e','i','o','u']
for char in str1.lower():
    if char in vowels:
        str_vowels += 1
    elif char.isalpha():
        str_consonant += 1
    else:
        str_extra += 1
print('----------------------------------')
print(str_vowels)
print(str_consonant)
print(str_extra)


# ---------------------------------------------------------------------------------------------
# 5️. Remove Duplicates from List

# Given a list, remove duplicate values.

# Example

# Input: [1,2,2,3,4,4,5]
# Output: [1,2,3,4,5]

# Concepts:

# list

# loops

# condition

# type casting (optional using set)
list_inp = [1,2,2,3,4,4,5]

unique_list = []
for i in list_inp:
    if i not in unique_list:
        unique_list.append(i)
    else:
        pass

print(unique_list)

# -----------------------------------------------------------------------
# 6. Extract Domain from Email

# Given an email address, extract the domain.

# Example

# Input: user@gmail.com
# Output: gmail.com

# Concepts:

# strings

# slicing

# split()

str_domain = 'ujjwal24jain24@gmail.com'
domain = str_domain.split('@')

print(domain[1])

# ----------------------- or ------------------------------

if '@' in str_domain:
    domain = str_domain.split('@')[1]
    print(domain)
else:
    print("Invalid email address!")

# --------------------------------------------------------------------------
# 7️. Swap First and Last Element of List

# Write a program that swaps first and last elements.

# Example

# Input: [10,20,30,40,50]
# Output: [50,20,30,40,10]

# Concepts:

# list indexing

# tuple unpacking

list_l = [10,20,30,40,50]

# a, b = b, a  ← Python lets you swap two things in ONE line like this!
list_l[0], list_l[-1] = list_l[-1] , list_l[0]
print(list_l)

# --------------------------------------------------------------------------

# 8️. Convert List of Strings to Integers

# Convert the following list into integers.

# ["10","20","30","40"]

# Expected output

# [10,20,30,40]

# Concepts:

# type casting

# list

# loop

list_str = ["10","20","30","40"]
list_int = []

# using append to append inside the list after converting it into int
for str1 in list_str:
    list_int.append(int(str1))

print(list_int)


# ----------------------------------------------------------------------------

# 9️ Find Most Frequent Character

# Find the character that appears the most times in a string.

# Example

# Input: banana
# Output: a

# Concepts:

# string

# dictionary or list counting

# max()

s_str = 'banana'
f_dict = {}

for char in s_str:
    if char not in f_dict:
        f_dict[char] = 1
    else:
        f_dict[char] += 1

print(f_dict)
m_frequent = max(f_dict, key = f_dict.get)
print(max(m_frequent))
# --------------------------------------------------------------------------
# 10 Check if Two Strings are Anagrams

# Two strings are anagrams if they contain the same letters.

# Example

# listen
# silent

# Output

# Anagram

# Concepts:

# sorting

# strings

# condition

s_str1 = 'listen'
s_str2 = 'silent'

s_list = list(s_str1) 
s_list2 = list(s_str2) 

s_list.sort()
s_list2.sort()

if s_list == s_list2:
    print('they are anagram')
else:
    print('they are not anagram')

# ----- or -------
s_str1 = 'listen'
s_str2 = 'silent'

if sorted(s_str1) == sorted(s_str2):
    print('they are anagram')
else:
    print('they are not anagram')

# --------------------------------------------------------------------------
# 11 Flatten a Nested List

# Convert this list into a single list.

# [[1,2],[3,4],[5,6]]

# Output

# [1,2,3,4,5,6]

# Concepts:

# nested loops

# list
list_1 =  [[1,2],[3,4],[5,6]]

list_2 = []
for items in list_1:
    for sub_items in items:
        list_2.append(sub_items)

print(list_2)

# ---or----

# using list comprehension - still need to learn
list_1 = [[1,2],[3,4],[5,6]]

list_2 = [sub_items for items in list_1 for sub_items in items]

print(list_2)  # [1, 2, 3, 4, 5, 6] 

# -------------------------------------------------------------------------
# 12 Capitalize First Letter of Every Word

# Input

# hello world python

# Output

# Hello World Python

# Concepts

# string methods

# split()

# join()

s_cap = 'hello world python'

r_cap = s_cap.split()
print(r_cap)
r_capital =[]
for word in r_cap:
    r_capital.append(word.capitalize())

final_cap = ' '.join(r_capital)
print(final_cap)

# -----or ----------
s_cap = 'hello world python'
print(s_cap.title())


# -------------------------------------------------------------------------
# 13 Find All Even Numbers from List

# Given

# [12,15,18,21,24,30]

# Output

# [12,18,24,30]

# Concepts

# list

# if

# modulus %

list_all = [12,15,18,21,24,30]

list_even = [] 
list_odd = [] 
for item in list_all:
    if item % 2 == 0:
        list_even.append(item)
    else:
        list_odd.append(item)

print(list_even)
print(list_odd)

# --------------------------------------------------------------------------
# 14 Tuple Unpacking Example

# Given

# person = ("John", 25, "Engineer")

# Print

# Name: John
# Age: 25
# Profession: Engineer

# Concepts

# tuples

# unpacking

person = ("John", 25, "Engineer")

name, age, profession = person
print(name,age,profession)

# --------------------------------------------------------------------------
# 1️5 Rotate a List

# Rotate a list left by 2 positions

# Input

# [1,2,3,4,5]

# Output

# [3,4,5,1,2]

# Concepts

# slicing

# list

list_rotate = [1,2,3,4,5]
list_1 = list_rotate[:2]
list_2 = list_rotate[2:]

rotate = list_2 + list_1
print(rotate)

# -------------------------------------------------------------------------
# 1️⃣6️⃣ Compress a String

# Convert

# aaabbcccc

# into

# a3b2c4

# Concepts

# string

# loops

# conditions

# compress_s = 'aaabbcccc'
# current_char = compress_s[0] #starting for a string
# count = 0
# result = ''
# for char in compress_s:
#     if current_char != char:
#         current_char = char
#         count = 1
#     else:
#         count += 1

#     result += current_char + str(count)
# print(result)


compress_s = 'aaabbcccc'
current_char = compress_s[0]  # start with first character 'a'
count = 1                      # count starts at 1 (first char already counted)
result = ''                    # final compressed string

for char in compress_s[1:]:    # start from 2nd character (first is already in current_char)
    if current_char != char:   # character changed!
        result += current_char + str(count)  # save previous char + count → 'a3'
        current_char = char    # update to new character
        count = 1              # reset count for new character
    else:
        count += 1             # same character, keep counting

# ⚠️ after loop ends, last character is never saved inside loop!
# so save it manually here
result += current_char + str(count)

print(result)  # a3b2c4 

# --------------------------------------------------------------------------
# Even or Odd (if-else + type casting)

# Write a program that:

# Takes an integer input from the user.

# Prints:

# "Even" if the number is divisible by 2

# "Odd" otherwise.

# Example:

# Input: 7
# Output: Odd



