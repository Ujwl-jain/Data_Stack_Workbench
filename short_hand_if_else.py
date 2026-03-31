# ============================================================
#              SHORTHAND IF-ELSE (TERNARY OPERATOR)
# ============================================================
# Writing an if-else statement in a single line.
# Also called the TERNARY OPERATOR in other languages.
#
# SYNTAX:
#   value_if_true if condition else value_if_false
#
# WHEN TO USE:
#   - Simple, readable conditions that fit cleanly in one line
#   - Assigning a variable based on a condition
#
# WHEN NOT TO USE:
#   - Complex conditions with multiple checks
#   - Multiple if-elif-else blocks
#   - When readability suffers -- clear code beats clever code
# ============================================================


# ------------------------------------------------------------
# Basic syntax -- assigning a value
# ------------------------------------------------------------
# Regular if-else:
value_if_true = 1
value_if_false = 2

if value_if_true > value_if_false:
    result = value_if_true
else:
    result = value_if_false
print(result)           # 2

# Same thing in one line:
result = value_if_true if value_if_true > value_if_false else value_if_false
print(result)           # 2  <- same output, fewer lines


# ------------------------------------------------------------
# Assigning 0 or a value based on condition
# ------------------------------------------------------------
a = 330
b = 3303

c = 9 if a > b else 0
print(c)                # 0  <- because a is NOT greater than b


# ------------------------------------------------------------
# Chained ternary -- multiple conditions in one line
# ------------------------------------------------------------
# Works like if / elif / else chained together.
# NOTE: gets hard to read quickly -- use sparingly.

a = 330
b = 3303

print("A") if a > b else print("=") if a == b else print("B")
# reads as:
#   if a > b   -> print "A"
#   elif a==b  -> print "="
#   else       -> print "B"
# Output: B


# ------------------------------------------------------------
# Using ternary with strings
# ------------------------------------------------------------
age = 20
status = "adult" if age >= 18 else "minor"
print(status)           # 'adult'


# ------------------------------------------------------------
# Using ternary inside print directly
# ------------------------------------------------------------
marks = 75
print("pass" if marks >= 40 else "fail")    # 'pass'


# ------------------------------------------------------------
# Using ternary inside a function
# ------------------------------------------------------------
def absolute(n):
    return n if n >= 0 else -n

print(absolute(-9))     # 9
print(absolute(5))      # 5


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Pattern                              Example
#  ──────────────────────────────────────────────────────────────
#  Assign based on condition            x = a if cond else b
#  Print based on condition             print(a) if cond else print(b)
#  Chained (if / elif / else)           a if c1 else b if c2 else c
#  Inside a function return             return x if x>0 else -x
#  Inside print directly                print("yes" if cond else "no")
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Condition goes in the MIDDLE -- value_if_true if COND else value_if_false
#  2. Both sides must return or produce SOMETHING -- no empty branches
#  3. Chaining works but hurts readability -- avoid beyond 1 level
#  4. Use regular if-else for anything complex -- clarity first
#
# ============================================================