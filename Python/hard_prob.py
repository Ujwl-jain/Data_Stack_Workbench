# ---------------------------------------------------------------------------------------------------------
#[Hard]   Implement a Caesar cipher: shift each letter by k positions, preserve case and non-letters. - explanation in hard_prob.py

# -----------------------------------------------------------------------------
#  UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# A Caesar cipher is one of the oldest encryption techniques.
#
# Rules:
#   - Shift every LETTER forward by k positions in the alphabet
#   - If k = 3 → A becomes D, B becomes E, Z wraps around to C
#   - UPPERCASE stays uppercase, LOWERCASE stays lowercase
#   - Non-letters (spaces, punctuation, digits) are LEFT UNTOUCHED
#
# Example:
#   Input  : "Hello, World!"   k = 3
#   Output : "Khoor, Zruog!"
 
'''
Logic:

# 1. Take the input string and value k
# 2. Create an empty result string
# 3. Loop through each character in the string
# 4. If the character is LOWERCASE → shift using 'a' as base
# 5. If the character is UPPERCASE → shift using 'A' as base
# 6. If it's anything else (space, digit, punctuation) → keep as-is
# 7. Add the processed character to the result string
# 8. Print the final result
'''

# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — How Shifting Works (ord + chr + % 26)
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
 

str_CC = 'Hello! World$!'
k = 3
str_c = ''
for char in str_CC:
    if char.isdigit():
        pass
    elif char.isalpha() and char.islower():
        char =  chr(((ord(char) - ord('a')) + k) % 26 + ord('a'))
    elif char.isalpha and char.isupper():
        char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    else:
        char = char

    str_c = str_c + char

print(str_c)


# or - isalpha() is removed cause islower and isupper is indicating that the char is character not digit

str_CC = 'Hello! World$!'
k = 3
str_c = ''

for char in str_CC:
    if char.islower():
        char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
    elif char.isupper():
        char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    str_c = str_c + char

print(str_c)


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Step by Step  |  Input: 'Hello! World$!'  |  k = 3
# -----------------------------------------------------------------------------
#
#  str_c starts as ''
#
#  Step  | char | Condition   | Calculation                        | Result | str_c
#  ------+------+-------------+------------------------------------+--------+----------------
#    1   |  H   | isupper()   | (72-65+3)%26+65 = 10%26+65 = 75   |  K     | 'K'
#    2   |  e   | islower()   | (101-97+3)%26+97 = 7%26+97 = 104  |  h     | 'Kh'
#    3   |  l   | islower()   | (108-97+3)%26+97 = 14%26+97 = 111 |  o     | 'Kho'
#    4   |  l   | islower()   | same as above                      |  o     | 'Khoo'
#    5   |  o   | islower()   | (111-97+3)%26+97 = 17%26+97 = 114 |  r     | 'Khoor'
#    6   |  !   | else        | unchanged                          |  !     | 'Khoor!'
#    7   |  ' ' | else        | unchanged                          |  ' '   | 'Khoor! '
#    8   |  W   | isupper()   | (87-65+3)%26+65 = 25%26+65 = 90   |  Z     | 'Khoor! Z'
#    9   |  o   | islower()   | (111-97+3)%26+97 = 17%26+97 = 114 |  r     | 'Khoor! Zr'
#   10   |  r   | islower()   | (114-97+3)%26+97 = 20%26+97 = 117 |  u     | 'Khoor! Zru'
#   11   |  l   | islower()   | same as step 3                     |  o     | 'Khoor! Zruo'
#   12   |  d   | islower()   | (100-97+3)%26+97 = 6%26+97 = 103  |  g     | 'Khoor! Zruog'
#   13   |  $   | else        | unchanged                          |  $     | 'Khoor! Zruog$'
#   14   |  !   | else        | unchanged                          |  !     | 'Khoor! Zruog$!'
#
#  Final Output: 'Khoor! Zruog$!'

# -----------------------------------------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. islower() and isupper() already imply isalpha() — no need to check both!
# 2. Always call methods with ()  →  char.isalpha()  NOT  char.isalpha
# 3. % 26 is the wrap-around trick for any circular sequence of 26 items
# 4. ord() and chr() are your best friends for character manipulation
# 5. Build result string by concatenating inside the loop
 
 
# -----------------------------------------------------------------------------
# PATTERN TO REMEMBER
# -----------------------------------------------------------------------------
# Whenever you need to "shift within a fixed range":
#   new_value = (current_position + shift) % range_size
#
# This pattern appears in:
#   - Caesar cipher (letters, range = 26)
#   - Circular arrays / queues
#   - Clock arithmetic (hours, range = 12 or 24)
#   - Day of week calculations (range = 7)





# --------------------------------------------------------------------------------------------------
#[Hard]   Find all substrings of a string that are palindromes and return them sorted by length.

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

str_sub = 'abba'

list_sub = []
for start in range(len(str_sub)):
    for end in range(start+1, len(str_sub) + 1):
        sub = str_sub[start:end]
        if sub == sub[::-1]:
            list_sub.append(sub)
        else:
            pass

sort_sub = sorted(list_sub, key = len, reverse= True)
print(sort_sub)


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
 


# -------------------------------------------------------------------------------------
# =============================================================================
# Q19 [Hard] - Multiplication Table (1-10) as 2D List
# Generate using both normal loops AND nested list comprehension
# =============================================================================
 
 
# -----------------------------------------------------------------------------
#  UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# A multiplication table (1-10) looks like this:
#
#   1×1=1,   1×2=2,   1×3=3  ...  1×10=10
#   2×1=2,   2×2=4,   2×3=6  ...  2×10=20
#   ...
#   10×1=10, 10×2=20  ...    ...  10×10=100
#
# A 2D list = a list of lists:
#   [
#     [1,  2,  3  ... 10],    ← row 1
#     [2,  4,  6  ... 20],    ← row 2
#     ...
#     [10, 20, 30 ... 100]    ← row 10
#   ]
#
# Final result → 1 big list containing 10 lists, each with 10 numbers
 
 
# -----------------------------------------------------------------------------
#    LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# 1. Create empty final_list to store all rows
# 2. Outer loop → row from 1 to 10 (each row = one multiplication table)
# 3. Create empty list_cal INSIDE outer loop (resets for each new row!)
# 4. Inner loop → column from 1 to 10
# 5. Multiply row × column → append result to list_cal
# 6. After inner loop finishes → append list_cal to final_list
# 7. Print final_list
#
#     COMMON MISTAKE: list_cal must be created INSIDE outer loop, OUTSIDE inner loop
#     If created inside inner loop → resets every column → loses previous values!
 
 
# -----------------------------------------------------------------------------
#  KEY CONCEPT 1 — Why range(1, 11) not range(1, 10)?
# -----------------------------------------------------------------------------
# range(1, 10) = 1,2,3,4,5,6,7,8,9      ← misses 10!
# range(1, 11) = 1,2,3,4,5,6,7,8,9,10   ✅
#
# Remember: range is EXCLUSIVE at the end — always +1 to include last number
 
 
# -----------------------------------------------------------------------------
#  KEY CONCEPT 2 — Building a 2D List
# -----------------------------------------------------------------------------
# 2D list = list of lists
# Pattern:
#   outer_list = []
#   for ...:
#       inner_list = []        ← reset for each row
#       for ...:
#           inner_list.append(value)
#       outer_list.append(inner_list)   ← append after inner loop
 
 
# -----------------------------------------------------------------------------
#  KEY CONCEPT 3 — List Comprehension vs Normal Loop
# -----------------------------------------------------------------------------
# Normal loop (verbose but clear):
#   for row in range(1,11):
#       list_cal = []
#       for column in range(1,11):
#           list_cal.append(row * column)
#       table_list.append(list_cal)
#
# List comprehension (concise, Pythonic):
#   [[row*column for column in range(1,11)] for row in range(1,11)]
#
# How to read comprehension RIGHT TO LEFT:
#   → for row in range(1,11)           ← outer loop
#   → for column in range(1,11)        ← inner loop
#   → row*column                       ← expression/calculation
#   → [row*column for column in ...]   ← inner list (one row)
#   → [[...] for row in ...]           ← outer list (all rows)
 
 
# -----------------------------------------------------------------------------
# METHOD 1 — Normal Loop
# -----------------------------------------------------------------------------
 
table_list = []
 
for row in range(1, 11):
    list_cal = []                        # reset inner list for each row
    for column in range(1, 11):
        mat = row * column               # calculate product
        list_cal.append(mat)             # add to current row
    table_list.append(list_cal)          # add completed row to final list
 
print(table_list)
 
 
# -----------------------------------------------------------------------------
# METHOD 2 — Nested List Comprehension (Same result, 1 line!)
# -----------------------------------------------------------------------------
 
list_Comp = [[row * column for column in range(1, 11)] 
             for row in range(1, 11)]
 
print(list_Comp)
 
 
# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Normal Loop  |  Simplified to range(1,4) for clarity
# -----------------------------------------------------------------------------
#
#  table_list = []
#
#  ┌─────┬────────┬──────────────┬─────────────────────┬──────────────────────────┐
#  │ row │ column │  row*column  │      list_cal        │       table_list         │
#  ├─────┼────────┼──────────────┼─────────────────────┼──────────────────────────┤
#  │  1  │   1    │   1×1 = 1    │ [1]                 │ []                       │
#  │  1  │   2    │   1×2 = 2    │ [1, 2]              │ []                       │
#  │  1  │   3    │   1×3 = 3    │ [1, 2, 3]           │ []                       │
#  │     │        │ ← inner done │                     │ [[1,2,3]]  ← appended!   │
#  ├─────┼────────┼──────────────┼─────────────────────┼──────────────────────────┤
#  │  2  │   1    │   2×1 = 2    │ [2]                 │ [[1,2,3]]                │
#  │  2  │   2    │   2×2 = 4    │ [2, 4]              │ [[1,2,3]]                │
#  │  2  │   3    │   2×3 = 6    │ [2, 4, 6]           │ [[1,2,3]]                │
#  │     │        │ ← inner done │                     │ [[1,2,3],[2,4,6]] ✅     │
#  ├─────┼────────┼──────────────┼─────────────────────┼──────────────────────────┤
#  │  3  │   1    │   3×1 = 3    │ [3]                 │ [[1,2,3],[2,4,6]]        │
#  │  3  │   2    │   3×2 = 6    │ [3, 6]              │ [[1,2,3],[2,4,6]]        │
#  │  3  │   3    │   3×3 = 9    │ [3, 6, 9]           │ [[1,2,3],[2,4,6]]        │
#  │     │        │ ← inner done │                     │ [[1,2,3],[2,4,6],[3,6,9]]│
#  └─────┴────────┴──────────────┴─────────────────────┴──────────────────────────┘
#
#  ✅ Final Output (1-3 table): [[1,2,3], [2,4,6], [3,6,9]]
#
# -----------------------------------------------------------------------------
# 🧪 DRY RUN — List Comprehension  |  Same range(1,4) example
# -----------------------------------------------------------------------------
#
#  [[row*column for column in range(1,4)] for row in range(1,4)]
#
#  Step 1 → outer loop picks row=1
#           inner → [1×1, 1×2, 1×3] = [1, 2, 3]
#
#  Step 2 → outer loop picks row=2
#           inner → [2×1, 2×2, 2×3] = [2, 4, 6]
#
#  Step 3 → outer loop picks row=3
#           inner → [3×1, 3×2, 3×3] = [3, 6, 9]
#
#  Final → [[1,2,3], [2,4,6], [3,6,9]] ✅  (same as normal loop!)
 
 
# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. range(1, 11) not range(1, 10) — always +1 to include last number
# 2. Inner list must be RESET inside outer loop, OUTSIDE inner loop
# 3. Append inner list to outer list AFTER inner loop completes
# 4. List comprehension = same logic, just written inside-out in one line
# 5. Read comprehension right to left → outer loop first, inner loop second
 
 
# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — 2D List Building Pattern
# -----------------------------------------------------------------------------
# Whenever you need to build a 2D list (matrix/table):
#
#   METHOD 1 (Normal):
#   result = []
#   for i in range(...):
#       row = []
#       for j in range(...):
#           row.append(expression)
#       result.append(row)
#
#   METHOD 2 (Comprehension):
#   result = [[expression for j in range(...)] for i in range(...)]
#
# This pattern appears in:
#   - Multiplication tables
#   - Matrix operations
#   - Game boards (chess, tic-tac-toe)
#   - Image pixel grids
#   - Distance/cost matrices




# --------------------------------------------------------------------------------

# =============================================================================
# Q20 [Hard] - Find All Prime Numbers up to N
# Using helper function + normal loop, then list comprehension
# =============================================================================
 
 
# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# A PRIME NUMBER is a number that is:
#   - Greater than 1
#   - Divisible ONLY by 1 and itself
#
# Examples:
#   2  → divisible by 1, 2 only          ✅ prime
#   3  → divisible by 1, 3 only          ✅ prime
#   4  → divisible by 1, 2, 4            ❌ not prime (2 divides it!)
#   17 → divisible by 1, 17 only         ✅ prime
#
# A HELPER FUNCTION means writing a separate is_prime(n) function
# that returns True or False — then using it in the main loop/comprehension
 
 
# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# HELPER FUNCTION is_prime(n):
#   1. If n < 2 → return False immediately (0, 1, negatives are not prime)
#   2. Loop i from 2 to n-1 (range(2, n))
#   3. If n % i == 0 → divisor found → return False immediately
#   4. If loop completes without finding divisor → return True
#
# MAIN LOGIC:
#   1. Set N, create empty list
#   2. Loop num from 2 to N (range(2, N+1)) — +1 to include N!
#   3. Call is_prime(num) → if True → append to list
#   4. Print list
 
 
# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — Why a Loop INSIDE the Function?
# -----------------------------------------------------------------------------
# To check if n is prime, you must check EVERY number from 2 to n-1
# That requires its OWN loop inside the function!
#
# For n = 7:
#   range(2, 7) = [2, 3, 4, 5, 6]
#   7 % 2 = 1  → continue
#   7 % 3 = 1  → continue
#   7 % 4 = 3  → continue
#   7 % 5 = 2  → continue
#   7 % 6 = 1  → continue
#   → loop ends → return True ✅
#
# For n = 6:
#   range(2, 6) = [2, 3, 4, 5]
#   6 % 2 = 0  → divisor found → return False immediately ❌
 
 
# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Why return True is OUTSIDE the loop
# -----------------------------------------------------------------------------
# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False    ← exits function IMMEDIATELY if divisor found
#     return True             ← only reached if loop finished with NO divisors!
#
# Think of it like a security guard:
#   → checks every number 2 to n-1
#   → finds a divisor? → "STOP, not prime!" → exits immediately
#   → checked all? none divide evenly? → "all clear, prime!" → return True
#
# If return True was INSIDE the loop:
#   → would return True after checking just the FIRST number → WRONG! ❌
 
 
# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — range(2, n) automatically stops at n-1
# -----------------------------------------------------------------------------
# range(2, n) is EXCLUSIVE at the end → stops at n-1
# So you never divide n by itself — which is exactly what we want!
#
# For n = 3:  range(2, 3) = [2]     only checks 2, never checks 3 ✅
# For n = 7:  range(2, 7) = [2,3,4,5,6]  never checks 7 ✅
 
 
# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 4 — range(2, N+1) in main loop
# -----------------------------------------------------------------------------
# range(N)      = 0 to N-1  → misses N! ❌
# range(2, N+1) = 2 to N    → perfect!  ✅
#
# Start from 2 because 0 and 1 are never prime (handled by is_prime anyway)
 
 
# -----------------------------------------------------------------------------
#  METHOD 1 — Normal Loop
# -----------------------------------------------------------------------------

n = 10
list_prime = []

def is_prime(n):
    if n<2:
        return False                 # 0, 1, negatives → not prime
    for i in range(2,n):             # check every number from 2 to n-1
        if n % i == 0:
            return False  # divisor found → not prime
    return True               # no divisors found → prime!
    
for i in range(2,n+1):              # loop from 2 to N (inclusive)
    if is_prime(i) == True:         # if True → it's prime
        list_prime.append(i)

print(list_prime)

# -----------------------------------------------------------------------------
#  METHOD 2 — List Comprehension (Same result, 1 line!)
# -----------------------------------------------------------------------------
 
prime_list = [i for i in range(2, n + 1) if is_prime(i)]
print(prime_list)
# Output: [2, 3, 5, 7]
 
 
# -----------------------------------------------------------------------------
# 🧪 DRY RUN — is_prime() function  |  Checking each number up to 10
# -----------------------------------------------------------------------------
#
#  ┌─────┬──────────────────────────┬────────────┬──────────────┐
#  │  n  │  divisors checked        │  result    │  reason      │
#  ├─────┼──────────────────────────┼────────────┼──────────────┤
#  │  0  │  n < 2                   │  False     │  too small   │
#  │  1  │  n < 2                   │  False     │  too small   │
#  │  2  │  range(2,2) = []  empty! │  True  ✅  │  no divisors │
#  │  3  │  3%2=1                   │  True  ✅  │  no divisors │
#  │  4  │  4%2=0 → stop!           │  False ❌  │  2 divides 4 │
#  │  5  │  5%2=1, 5%3=2, 5%4=1    │  True  ✅  │  no divisors │
#  │  6  │  6%2=0 → stop!           │  False ❌  │  2 divides 6 │
#  │  7  │  7%2,3,4,5,6 → all ≠ 0  │  True  ✅  │  no divisors │
#  │  8  │  8%2=0 → stop!           │  False ❌  │  2 divides 8 │
#  │  9  │  9%2=1, 9%3=0 → stop!   │  False ❌  │  3 divides 9 │
#  │ 10  │  10%2=0 → stop!          │  False ❌  │  2 divides 10│
#  └─────┴──────────────────────────┴────────────┴──────────────┘
#
#  Primes found: [2, 3, 5, 7] ✅
#
# -----------------------------------------------------------------------------
# 🧪 DRY RUN — List Comprehension  |  n = 10
# -----------------------------------------------------------------------------
#
#  [i for i in range(2, 11) if is_prime(i)]
#
#  i=2  → is_prime(2) = True  → include  → [2]
#  i=3  → is_prime(3) = True  → include  → [2, 3]
#  i=4  → is_prime(4) = False → skip
#  i=5  → is_prime(5) = True  → include  → [2, 3, 5]
#  i=6  → is_prime(6) = False → skip
#  i=7  → is_prime(7) = True  → include  → [2, 3, 5, 7]
#  i=8  → is_prime(8) = False → skip
#  i=9  → is_prime(9) = False → skip
#  i=10 → is_prime(10)= False → skip
#
#  ✅ Final Output: [2, 3, 5, 7]
 
 
# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Helper functions make code reusable — write once, call many times
# 2. return False INSIDE loop = exit immediately when condition met
# 3. return True OUTSIDE loop = only reached when loop completes with no hits
# 4. range(2, n) automatically never checks n itself (exclusive end)
# 5. range(2, N+1) in main loop — always +1 to include N
# 6. if is_prime(i) is cleaner than if is_prime(i) == True
# 7. n = 2 is special — range(2, 2) is empty → loop skipped → return True ✅
 
 
# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Helper Function + Filter Pattern
# -----------------------------------------------------------------------------
# Whenever you need to filter numbers based on a complex condition:
#
#   def check_condition(n):     ← helper function
#       # complex logic here
#       return True or False
#
#   # Normal loop version:
#   result = []
#   for i in range(...):
#       if check_condition(i):
#           result.append(i)
#
#   # Comprehension version:
#   result = [i for i in range(...) if check_condition(i)]
#
# This pattern appears in:
#   - Prime numbers
#   - Perfect numbers
#   - Armstrong numbers
#   - Any "find all numbers that satisfy X" problem
 

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

str_func = 'hello world-government'
list_string = []

def is_split(deli):
    temp = ''
    for char in str_func:
        if char == deli:
            list_string.append(temp)
            temp = ''
        else:
            temp = temp + char

    list_string.append(temp)
    print(list_string)


def is_join(deli):
    join_string = ''
    for element in range(len(list_string)):
        if element == len(list_string) - 1:
            join_string = join_string + list_string[element]
        else:
            join_string = join_string + list_string[element] + deli

    print(join_string)

is_split(deli = ' ')
is_join(deli = '-')

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
