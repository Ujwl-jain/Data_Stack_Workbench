# =============================================================================
# Q27 - Recursive String Reversal
# Reverse a string using recursion — NO slicing [::-1] or built-in reverse!
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Reverse a string WITHOUT:
#   [::-1]     ← reverse slicing ❌
#   reversed() ← built-in method ❌
#
# Regular slicing like string[1:] is ALLOWED — it's just accessing, not reversing!
#
# reverse("hello") → "olleh"


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — What is Recursion?
# -----------------------------------------------------------------------------
# A function that calls ITSELF with a SMALLER version of the problem
# until it hits a BASE CASE!
#
# Think of Russian dolls 🪆:
#   reverse("hello")
#       → reverse("ello") + "h"
#           → reverse("llo") + "e" + "h"
#               → reverse("lo") + "l" + "e" + "h"
#                   → reverse("o") + "l" + "l" + "e" + "h"
#                       → "o"  ← BASE CASE! empty/single char
#   Result: "o" + "l" + "l" + "e" + "h" = "olleh" ✅
#
# TWO parts every recursive function needs:
#   1. BASE CASE   → when to STOP recursing
#   2. RECURSIVE CASE → call itself with SMALLER input


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — Why string[0] goes at the END
# -----------------------------------------------------------------------------
# To reverse "hello" → "h" must end up LAST
#
# So: reverse(rest_of_string) + first_char
#     reverse("ello")         + "h"
#
# reverse("ello") will eventually return "olle"
# "olle" + "h" = "olleh" ✅
#
# Key insight: recursive call resolves FIRST, then + char happens!


# -----------------------------------------------------------------------------
# ✅ METHOD 1 — Using string[1:] slicing
# -----------------------------------------------------------------------------
# LOGIC:
# Base case  → empty string → return it (nothing left to reverse!)
# Recursive  → reverse(string[1:]) + string[0]
#              (reverse everything after first char, then add first char at end)

def reverse_string(str1):
    if len(str1) == 0:                          # base case — empty string!
        return str1
    return reverse_string(str1[1:]) + str1[0]   # recurse on rest + first char at end!

str1 = 'I am Ujjwal Jain'
print(reverse_string(str1))   # niaJ lawjjU ma I


# -----------------------------------------------------------------------------
# ✅ METHOD 2 — Using index parameter
# -----------------------------------------------------------------------------
# LOGIC:
# Start from LAST index → count DOWN to 0
# Base case  → index < 0 → return "" (gone past start!)
# Recursive  → string[index] + reverse(string, index - 1)

def reverse_string_using_index(str1, index):
    if index < 0:                                              # base case!
        return ""
    return str1[index] + reverse_string_using_index(str1, index - 1)  # current char + rest

str1 = 'hello'
print(reverse_string_using_index(str1, len(str1) - 1))   # olleh


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Method 1  |  reverse_string("hello")
# -----------------------------------------------------------------------------
#
#  ┌─────────────────────────┬──────────────┬────────────────────────────────┐
#  │        call             │  base case?  │         returns                │
#  ├─────────────────────────┼──────────────┼────────────────────────────────┤
#  │ reverse_string("hello") │      ❌      │ reverse("ello") + "h"          │
#  │ reverse_string("ello")  │      ❌      │ reverse("llo")  + "e"          │
#  │ reverse_string("llo")   │      ❌      │ reverse("lo")   + "l"          │
#  │ reverse_string("lo")    │      ❌      │ reverse("o")    + "l"          │
#  │ reverse_string("o")     │      ❌      │ reverse("")      + "o"         │
#  │ reverse_string("")      │      ✅      │ ""  ← stops here!              │
#  └─────────────────────────┴──────────────┴────────────────────────────────┘
#
#  Now builds back up:
#  "" + "o" = "o"
#  "o" + "l" = "ol"
#  "ol" + "l" = "oll"
#  "oll" + "e" = "olle"
#  "olle" + "h" = "olleh" ✅
#
# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Method 2  |  reverse_string_using_index("hello", 4)
# -----------------------------------------------------------------------------
#
#  ┌────────────────────────┬──────────────┬──────────────────────────────────┐
#  │        call            │  base case?  │         returns                  │
#  ├────────────────────────┼──────────────┼──────────────────────────────────┤
#  │ reverse("hello", 4)    │      ❌      │ "o" + reverse("hello", 3)        │
#  │ reverse("hello", 3)    │      ❌      │ "l" + reverse("hello", 2)        │
#  │ reverse("hello", 2)    │      ❌      │ "l" + reverse("hello", 1)        │
#  │ reverse("hello", 1)    │      ❌      │ "e" + reverse("hello", 0)        │
#  │ reverse("hello", 0)    │      ❌      │ "h" + reverse("hello", -1)       │
#  │ reverse("hello", -1)   │      ✅      │ ""  ← stops here!                │
#  └────────────────────────┴──────────────┴──────────────────────────────────┘
#
#  Builds back: "h" + "" = "h" → "e"+"h" = "eh" → "l"+"eh" = "leh"
#             → "l"+"leh" = "lleh" → "o"+"lleh" = "olleh" ✅


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Every recursive function needs: BASE CASE + RECURSIVE CASE
# 2. Base case = smallest input where answer is obvious (empty string, index<0)
# 3. string[1:] allowed — it's accessing, not reversing! Only [::-1] banned!
# 4. First char goes at END → reverse(string[1:]) + string[0]
# 5. Recursive call resolves FIRST — then + happens on the way back up!
# 6. Strings immutable — can't pop! Pass smaller string instead!


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Recursive String Pattern
# -----------------------------------------------------------------------------
#   def recursive_func(string):
#       if len(string) == 0:          # base case
#           return ""
#       return recursive_func(string[1:]) + string[0]  # recursive case
#
# This pattern appears in:
#   - String reversal
#   - Palindrome check via recursion
#   - String permutations
#   - Any "process one char, recurse on rest" problem
