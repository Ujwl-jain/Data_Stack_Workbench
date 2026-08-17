# =============================================================================
# Q27 [Hard] - Palindrome Substrings
# Find all substrings of a string that are palindromes,
# return them sorted by length.
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# A PALINDROME is a string that reads the same forwards and backwards.
#   "racecar" → palindrome ✅
#   "madam"   → palindrome ✅
#   "hello"   → NOT a palindrome ❌
#
# A SUBSTRING is any continuous slice of a string.
#   For "abba" → "a", "ab", "abb", "abba", "b", "bb", "bba", "b", "ba", "a"
#
# Your job:
#   1. Find ALL substrings
#   2. Keep only the ones that are palindromes
#   3. Return them sorted by length (longest first)
#
# Example:
#   Input  : "abba"
#   Output : ['a', 'b', 'b', 'a', 'bb', 'abba']  ← sorted by length


# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# 1. Declare the string, create an empty list to store palindromes
# 2. Outer loop → controls START position (moves forward one by one)
# 3. Inner loop → controls END position (stretches forward from start)
# 4. Extract substring using string[start:end]
# 5. Check if substring == substring[::-1]  (palindrome check)
# 6. If yes → append to list
# 7. After both loops → sort list by length using sorted(list, key=len)
# 8. Print result


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — How to Get All Substrings (Two Loop Trick)
# -----------------------------------------------------------------------------
# Think of START and END as two walls sliding across the string:
#
#  string = "abba"
#  index:   0  1  2  3
#  char:    a  b  b  a
#
#  start=0 → end slides from 1 to 4:
#      string[0:1] = "a"
#      string[0:2] = "ab"
#      string[0:3] = "abb"
#      string[0:4] = "abba"
#
#  start=1 → end slides from 2 to 4:
#      string[1:2] = "b"
#      string[1:3] = "bb"
#      string[1:4] = "bba"
#
#  start=2 → end slides from 3 to 4:
#      string[2:3] = "b"
#      string[2:4] = "ba"
#
#  start=3 → end slides from 4 to 4:
#      string[3:4] = "a"
#
# WHY range(start+1, len(string)+1)?
#   → start+1   : end must always be AHEAD of start (min slice = 1 char)
#   → len+1     : slicing is EXCLUSIVE, need +1 to include the last character
#                 "abba"[0:4] = "abba" ✅  |  "abba"[0:3] = "abb" ❌


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Palindrome Check with [::-1]
# -----------------------------------------------------------------------------
# [::-1] reverses a string in Python
#   "abba"[::-1]    = "abba"   → same!  palindrome ✅
#   "hello"[::-1]   = "olleh"  → different! not palindrome ❌
#
# IMPORTANT: Extract the substring FIRST, then reverse IT:
#   sub = string[start:end]    ← get the substring
#   sub == sub[::-1]           ← reverse the substring, not the whole string!


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


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

str_sub = 'Hello'

list_sub = []
for start in range(len(str_sub)):
    for end in range(start + 1, len(str_sub) + 1):
        sub = str_sub[start:end]       # extract substring
        if sub == sub[::-1]:           # check if palindrome
            list_sub.append(sub)       # keep it if yes

sort_sub = sorted(list_sub, key=len, reverse=True)   # sort by length
print(sort_sub)
# Output: ['l', 'e', 'H', 'o', 'l']
# (only single chars are palindromes in "Hello")

# Let's also test with a better example:
str_sub2 = 'abba'
list_sub2 = []
for start in range(len(str_sub2)):
    for end in range(start + 1, len(str_sub2) + 1):
        sub = str_sub2[start:end]
        if sub == sub[::-1]:
            list_sub2.append(sub)

sort_sub2 = sorted(list_sub2, key=len, reverse=True)
print(sort_sub2)
# Output: ['abba', 'bb', 'a', 'b', 'b', 'a']


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Step by Step  |  Input: 'abba'
# -----------------------------------------------------------------------------
#
#  list_sub starts as []
#
#  start=0:
#  ┌───────┬───────┬──────────┬─────────────┬────────────┬──────────────────────────┐
#  │ start │  end  │  slice   │     sub     │ palindrome?│  list_sub                │
#  ├───────┼───────┼──────────┼─────────────┼────────────┼──────────────────────────┤
#  │   0   │   1   │  [0:1]   │    "a"      │  "a"=="a"  ✅ │ ["a"]               │
#  │   0   │   2   │  [0:2]   │    "ab"     │ "ab"=="ba" ❌ │ ["a"]               │
#  │   0   │   3   │  [0:3]   │    "abb"    │"abb"=="bba"❌ │ ["a"]               │
#  │   0   │   4   │  [0:4]   │    "abba"   │"abba"=="abba"✅│ ["a","abba"]       │
#  ├───────┼───────┼──────────┼─────────────┼────────────┼──────────────────────────┤
#  start=1:
#  │   1   │   2   │  [1:2]   │    "b"      │  "b"=="b"  ✅ │ ["a","abba","b"]    │
#  │   1   │   3   │  [1:3]   │    "bb"     │ "bb"=="bb" ✅ │ ["a","abba","b","bb"]│
#  │   1   │   4   │  [1:4]   │    "bba"    │"bba"=="abb"❌ │ (no change)         │
#  ├───────┼───────┼──────────┼─────────────┼────────────┼──────────────────────────┤
#  start=2:
#  │   2   │   3   │  [2:3]   │    "b"      │  "b"=="b"  ✅ │ [...,"b"]           │
#  │   2   │   4   │  [2:4]   │    "ba"     │ "ba"=="ab" ❌ │ (no change)         │
#  ├───────┼───────┼──────────┼─────────────┼────────────┼──────────────────────────┤
#  start=3:
#  │   3   │   4   │  [3:4]   │    "a"      │  "a"=="a"  ✅ │ [...,"a"]           │
#  └───────┴───────┴──────────┴─────────────┴────────────┴──────────────────────────┘
#
#  list_sub = ["a", "abba", "b", "bb", "b", "a"]
#
#  After sorted(list_sub, key=len, reverse=True):
#  → ['abba', 'bb', 'a', 'b', 'b', 'a']  ✅


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Two loops (start + end) is the standard way to generate ALL substrings
# 2. Always extract substring into a variable first → then reverse it
# 3. [::-1] is the Pythonic way to reverse any sequence
# 4. sorted(list, key=len) sorts by length — no () on len!
# 5. () means CALLING — only add () when you want to execute something


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Two Loop Substring Pattern
# -----------------------------------------------------------------------------
# Whenever you need ALL substrings of a string:
#
#   for start in range(len(string)):
#       for end in range(start+1, len(string)+1):
#           sub = string[start:end]
#           # process sub here
#
# This pattern appears in:
#   - Palindrome substring problems
#   - Longest substring problems
#   - Substring search problems
#   - Anagram finding problems
