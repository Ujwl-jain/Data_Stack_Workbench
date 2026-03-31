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