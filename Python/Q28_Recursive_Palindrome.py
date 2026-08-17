# =============================================================================
# Q28 - Recursive Palindrome Check
# Check if a string is a palindrome using recursion — NO slicing!
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Palindrome = string that reads same forwards and backwards
#   "racecar" → palindrome ✅
#   "abba"    → palindrome ✅
#   "abca"    → NOT palindrome ❌
#
# Rules:
#   NO [::-1]          ← reverse slicing banned
#   NO string[a:b]     ← ANY colon slicing banned
#   Only string[index] ← single index access allowed ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — Slicing vs Indexing
# -----------------------------------------------------------------------------
# SLICING  → uses colon (:) → string[1:-1], string[0:3]  ❌ not allowed!
# INDEXING → single index   → string[0], string[len-1]   ✅ allowed!
#
# string[0 + 1 : len(string) - 1]  ← has colon → SLICING ❌
# string[0], string[len(string)-1] ← no colon  → INDEXING ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — Two Base Cases for Palindrome
# -----------------------------------------------------------------------------
# Odd length  → "racecar" → middle char "e" left → 1 char → always True!
# Even length → "abba"    → nothing left after checks → 0 chars → always True!
#
# So: if len <= 1 OR start >= end → return True


# -----------------------------------------------------------------------------
# ✅ METHOD 1 — Reverse then Compare (using helper function)
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Reverse string using recursive reverse from Q27
# 2. Compare reversed string with original
# 3. If equal → palindrome!

def reverse_string_using_index(str_to_reverse, index):
    if index < 0:
        return ""
    return str_to_reverse[index] + reverse_string_using_index(str_to_reverse, index - 1)

def palindrom_checker_m1(str_palindrom):
    reverse_string = reverse_string_using_index(str_palindrom, len(str_palindrom) - 1)
    if str_palindrom == reverse_string:
        return True
    else:
        return False

str1 = 'racecar'
result = palindrom_checker_m1(str1)
print(f"Method 1: {result}")   # True


# -----------------------------------------------------------------------------
# ✅ METHOD 2 — First vs Last char (with len shrinking)
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Base case → len <= 1 → return True
# 2. If first char != last char → return False
# 3. Else → recurse with inner string (uses [1:-1] slicing)
#
# ⚠️ NOTE: str[1:-1] is technically slicing — use Method 3 to fully avoid!

def palindrom_checker_m2(str_palindrom):
    if len(str_palindrom) <= 1:
        return True
    elif str_palindrom[0] != str_palindrom[len(str_palindrom) - 1]:
        return False
    else:
        return palindrom_checker_m2(str_palindrom[0 + 1:len(str_palindrom) - 1])

str1 = 'abca'
result = palindrom_checker_m2(str1)
print(f"Method 2: {result}")   # False


# -----------------------------------------------------------------------------
# ✅ METHOD 3 — Start/End Index (truly NO slicing!)
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Pass start=0 and end=len-1 as parameters
# 2. Base case → start >= end → return True (met in middle!)
# 3. If str[start] != str[end] → return False
# 4. Else → recurse with start+1, end-1 (move both inward!)

def palindrom_checker_m3(str_palindrom, start, end):
    if start >= end:                                    # base case!
        return True
    if str_palindrom[start] != str_palindrom[end]:     # mismatch!
        return False
    else:
        return palindrom_checker_m3(str_palindrom, start + 1, end - 1)  # move inward!

str1 = 'abba'
result = palindrom_checker_m3(str1, 0, len(str1) - 1)
print(f"Method 3: {result}")   # True


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Method 3  |  "racecar"
# -----------------------------------------------------------------------------
#
#  start=0, end=6
#
#  ┌───────┬─────┬─────┬──────────────┬───────────────────────────────┐
#  │ call  │start│ end │  comparison  │         action                │
#  ├───────┼─────┼─────┼──────────────┼───────────────────────────────┤
#  │   1   │  0  │  6  │  r == r  ✅  │ recurse(str, 1, 5)            │
#  │   2   │  1  │  5  │  a == a  ✅  │ recurse(str, 2, 4)            │
#  │   3   │  2  │  4  │  c == c  ✅  │ recurse(str, 3, 3)            │
#  │   4   │  3  │  3  │ start>=end   │ return True ← base case! ✅   │
#  └───────┴─────┴─────┴──────────────┴───────────────────────────────┘
#
#  Builds back: True → True → True → True ✅
#
# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Method 3  |  "abca"
# -----------------------------------------------------------------------------
#
#  ┌───────┬─────┬─────┬──────────────┬───────────────────────────────┐
#  │ call  │start│ end │  comparison  │         action                │
#  ├───────┼─────┼─────┼──────────────┼───────────────────────────────┤
#  │   1   │  0  │  3  │  a == a  ✅  │ recurse(str, 1, 2)            │
#  │   2   │  1  │  2  │  b != c  ❌  │ return False immediately!     │
#  └───────┴─────┴─────┴──────────────┴───────────────────────────────┘
#
#  ✅ Output: False


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Slicing = colon (:) anywhere → string[1:-1] is slicing!
#    Indexing = single index only → string[0] is NOT slicing!
# 2. Two base cases → len<=1 (Method 2) OR start>=end (Method 3)
# 3. Both odd and even palindromes handled by same base case!
# 4. Method 3 is the cleanest — no slicing, no helper function needed!
# 5. start+1, end-1 = moving both pointers inward each call!
# 6. return False immediately when mismatch found — no need to continue!


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Two Pointer Recursive Pattern
# -----------------------------------------------------------------------------
#   def check(string, start, end):
#       if start >= end:          # base case — pointers met!
#           return True
#       if string[start] != string[end]:  # mismatch!
#           return False
#       return check(string, start+1, end-1)  # move inward!
#
# This pattern appears in:
#   - Palindrome check
#   - String matching from both ends
#   - Balanced bracket checking
#   - Any "compare from both ends" problem
