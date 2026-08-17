# =============================================================================
# Q60 [Hard] - Implement your own str.split() and str.join()
# Without using built-in .split() or .join() methods
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# You need to build TWO functions from scratch:
#
# FUNCTION 1 — my_split(string, delimiter)
#   Built-in: "hello world".split(" ") → ["hello", "world"]
#   Your job:  break a string into a list of words based on a delimiter
#
# FUNCTION 2 — my_join(list, delimiter)
#   Built-in: " ".join(["hello", "world"]) → "hello world"
#   Your job:  combine a list of words into one string with delimiter between
#
# Example:
#   is_split("hello world", " ") → ["hello", "world"]
#   is_join(["hello", "world"], "-") → "hello-world"


# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# is_split(deli):
#   1. Create empty list and empty temp string (OUTSIDE the loop!)
#   2. Loop through each character in string
#   3. If character == delimiter → append temp to list → reset temp to ""
#   4. If character != delimiter → add character to temp
#   5. After loop → append last temp (last word has no delimiter after it!)
#   6. Print/return list
#
# is_join(deli):
#   1. Create empty result string INSIDE function
#   2. Loop using range(len(list)) to get INDEX numbers
#   3. Use index to get actual word → list[element]
#   4. If last index (element == len-1) → add word only, NO delimiter
#   5. Else → add word + delimiter
#   6. Print/return result string


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — temp string must be OUTSIDE the loop
# -----------------------------------------------------------------------------
# ❌ WRONG — resets on every character!
#   for char in string:
#       temp = ''          ← loses all previous characters each time!
#       temp = temp + char
#
# ✅ CORRECT — declared once before loop
#   temp = ''              ← starts empty once
#   for char in string:
#       temp = temp + char ← keeps building!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Always append AFTER the loop (last word fix)
# -----------------------------------------------------------------------------
# String: "hello world"
#
#   h → temp = "h"
#   e → temp = "he"
#   l → temp = "hel"
#   l → temp = "hell"
#   o → temp = "hello"
#   ' '→ delimiter! → append "hello" → reset temp = ""
#   w → temp = "w"
#   o → temp = "wo"
#   r → temp = "wor"
#   l → temp = "worl"
#   d → temp = "world"
#   → loop ends! "world" never hit a delimiter!
#
#   list_string.append(temp)  ← AFTER loop catches the last word ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Two ways to loop a list
# -----------------------------------------------------------------------------
# Way 1 — loop elements directly:
#   for element in list_string:
#       print(element)          # element = "hello", "world"
#       # ✅ actual word, ❌ no index
#
# Way 2 — loop indices using range:
#   for element in range(len(list_string)):
#       print(element)          # element = 0, 1
#       # ✅ index number, ❌ NOT the word itself
#       print(list_string[element])  # ✅ use index to get actual word
#
# We use Way 2 in is_join because we need the INDEX to check if we're
# at the last element!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 4 — Last element check
# -----------------------------------------------------------------------------
# List of 3 items → indices are 0, 1, 2 → last index = len - 1
#
# if element == len(list_string) - 1:   ✅ correct last index
# if element == len(list_string):       ❌ this index never exists!
#
# Why no delimiter after last word?
#   "hello-world-"  ← extra dash at end, WRONG! ❌
#   "hello-world"   ← clean ending, CORRECT! ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 5 — Declare result string INSIDE function
# -----------------------------------------------------------------------------
# Strings are IMMUTABLE in Python — + creates a NEW object
# If declared outside, modifying inside function won't affect the original!
#
# ❌ WRONG:
#   join_string = ''           # outside function
#   def is_join():
#       join_string = join_string + word   # creates new local string!
#
# ✅ CORRECT:
#   def is_join():
#       join_string = ''       # inside function — safe to modify!
#
# Note: .append() on lists works from outside because it MUTATES the list
# But + on strings creates a NEW string — different behavior!


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

str_func = 'hello world'
list_string = []

def is_split(deli):
    temp = ''                          # declare OUTSIDE loop!
    for char in str_func:
        if char == deli:               # hit delimiter?
            list_string.append(temp)   # save current word
            temp = ''                  # reset for next word
        else:
            temp = temp + char         # keep building word
    list_string.append(temp)           # catch the last word!
    print(list_string)


def is_join(deli):
    join_string = ''                   # declare INSIDE function!
    for element in range(len(list_string)):
        if element == len(list_string) - 1:              # last element?
            join_string = join_string + list_string[element]        # no delimiter
        else:
            join_string = join_string + list_string[element] + deli # add delimiter

    print(join_string)


is_split(deli=' ')
is_join(deli='-')
# Output:
# ['hello', 'world']
# hello-world


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — is_split()  |  Input: 'hello world'  |  deli = ' '
# -----------------------------------------------------------------------------
#
#  temp = ''    list_string = []
#
#  ┌──────┬───────────┬────────────────────────────┬───────────────────┐
#  │ char │ condition │          action             │   temp            │
#  ├──────┼───────────┼────────────────────────────┼───────────────────┤
#  │  h   │ not deli  │ temp = '' + 'h'             │ 'h'               │
#  │  e   │ not deli  │ temp = 'h' + 'e'            │ 'he'              │
#  │  l   │ not deli  │ temp = 'he' + 'l'           │ 'hel'             │
#  │  l   │ not deli  │ temp = 'hel' + 'l'          │ 'hell'            │
#  │  o   │ not deli  │ temp = 'hell' + 'o'         │ 'hello'           │
#  │ ' '  │ == deli!  │ append 'hello' → reset ''   │ ''                │
#  │  w   │ not deli  │ temp = '' + 'w'             │ 'w'               │
#  │  o   │ not deli  │ temp = 'w' + 'o'            │ 'wo'              │
#  │  r   │ not deli  │ temp = 'wo' + 'r'           │ 'wor'             │
#  │  l   │ not deli  │ temp = 'wor' + 'l'          │ 'worl'            │
#  │  d   │ not deli  │ temp = 'worl' + 'd'         │ 'world'           │
#  └──────┴───────────┴────────────────────────────┴───────────────────┘
#  → loop ends → append 'world' (last word!) → list_string = ['hello', 'world'] ✅
#
#
# 🧪 DRY RUN — is_join()  |  Input: ['hello', 'world']  |  deli = '-'
#
#  join_string = ''
#
#  ┌─────────┬──────────────────────────┬──────────────────────┬────────────────┐
#  │ element │   list_string[element]   │     condition        │  join_string   │
#  ├─────────┼──────────────────────────┼──────────────────────┼────────────────┤
#  │    0    │       'hello'            │ 0 != 1 (not last)    │ 'hello-'       │
#  │    1    │       'world'            │ 1 == 1 (last!) ✅    │ 'hello-world'  │
#  └─────────┴──────────────────────────┴──────────────────────┴────────────────┘
#  ✅ Final Output: 'hello-world'


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. temp string must be declared OUTSIDE the loop — inside resets every char!
# 2. Always append temp AFTER the loop to catch the last word
# 3. range(len(list)) gives indices — use list[index] to get actual value
# 4. Last index = len(list) - 1, never len(list)!
# 5. Declare result string INSIDE function — strings are immutable, + makes new object
# 6. .append() mutates lists (works from outside), + on strings does not!


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Character-by-Character String Building
# -----------------------------------------------------------------------------
# Whenever you need to process a string character by character
# and collect chunks between delimiters:
#
#   result_list = []
#   temp = ''                    ← outside loop!
#   for char in string:
#       if char == delimiter:
#           result_list.append(temp)
#           temp = ''            ← reset
#       else:
#           temp += char         ← build
#   result_list.append(temp)     ← catch last chunk!
#
# This pattern appears in:
#   - Custom split implementation
#   - CSV parser
#   - Tokenizer / lexer
#   - Parsing any delimited data
