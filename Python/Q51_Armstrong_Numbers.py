# =============================================================================
# Q51 [Hard] - Armstrong Numbers between 1 and 1000
# Using loops — e.g. 153 = 1³ + 5³ + 3³
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# An ARMSTRONG NUMBER (narcissistic number) is a number that equals
# the SUM OF ITS OWN DIGITS each raised to the power of NUMBER OF DIGITS!
#
# Examples:
#   153  → 3 digits → 1³ + 5³ + 3³ = 1 + 125 + 27  = 153  ✅
#   370  → 3 digits → 3³ + 7³ + 0³ = 27 + 343 + 0  = 370  ✅
#   9    → 1 digit  → 9¹            = 9              = 9    ✅
#   1634 → 4 digits → 1⁴+6⁴+3⁴+4⁴  = 1634           ✅
#
# The number of digits DETERMINES the power!
# 3-digit number → each digit raised to power 3
# 4-digit number → each digit raised to power 4


# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# 1. Loop i from 1 to 1000
# 2. Convert i to string → store as digit (needed for len and looping!)
# 3. Set container = 0  (accumulates the sum)
# 4. Find power = len(digit)  (number of digits = the power!)
# 5. Loop through each char in digit
# 6. container += int(char) ** power
# 7. After inner loop → if container == i → print i (it's Armstrong!)


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — Why convert to string?
# -----------------------------------------------------------------------------
# You need to do TWO things that only work on strings:
#   1. len(i)      → ❌ integers have no length!
#      len(digit)  → ✅ strings have length!
#
#   2. for char in i      → ❌ can't loop through integers!
#      for char in digit  → ✅ loops through each character!
#
# Always STORE the conversion — don't throw it away:
#   str(i)          # ❌ converts but throws away!
#   digit = str(i)  # ✅ stored and reusable!
#
# digit serves THREE purposes:
#   → len(digit)  = number of digits = the POWER
#   → for char in digit = extract each DIGIT
#   → int(char) = convert each digit back to number for calculation


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — container must be reset inside outer loop!
# -----------------------------------------------------------------------------
# container = 0 must be INSIDE the outer loop — resets for each new number!
#
# ❌ WRONG — container keeps accumulating across all numbers!
#   container = 0
#   for i in range(1, 1001):
#       for char in digit:
#           container += ...
#
# ✅ CORRECT — fresh container for each number:
#   for i in range(1, 1001):
#       container = 0       ← reset here!
#       for char in digit:
#           container += ...
#
# Same lesson as temp string in custom split — reset INSIDE outer, OUTSIDE inner!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Typos create silent bugs!
# -----------------------------------------------------------------------------
# Python treats differently spelled variables as COMPLETELY different variables!
#
#   container = 0                        # variable 1
#   conatiner = container + (...)        # variable 2 — typo!
#
# Python doesn't crash — it just creates a NEW variable called 'conatiner'
# while 'container' stays 0 forever → wrong result, no error message!
#
# This is one of the sneakiest bugs — always double check variable names! 🔍


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 4 — Check and print INSIDE the outer loop
# -----------------------------------------------------------------------------
# Armstrong check must happen AFTER inner loop but INSIDE outer loop:
#
# ❌ WRONG — only checks/prints last number:
#   for i in range(1, 1001):
#       ...
#   if container == i:   # outside loop!
#       print(i)
#
# ✅ CORRECT — checks every number:
#   for i in range(1, 1001):
#       ...inner loop...
#       if container == i:   # inside outer, after inner!
#           print(i)


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

for i in range(1, 1001):
    digit = str(i)               # convert to string → enables len() and looping!
    container = 0                # reset for each number!
    power = len(digit)           # number of digits = the power!

    for char in digit:           # extract each digit
        container = container + (int(char) ** power)  # sum of digit^power

    if container == i:           # Armstrong check!
        print(f"Armstrong number: {i}")

# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407


# -----------------------------------------------------------------------------
# 🧪 DRY RUN  |  i = 153
# -----------------------------------------------------------------------------
#
#  digit   = "153"
#  power   = len("153") = 3
#  container = 0
#
#  ┌──────┬───────────┬──────────────────────┬───────────┐
#  │ char │  int(char)│  int(char) ** power  │ container │
#  ├──────┼───────────┼──────────────────────┼───────────┤
#  │ '1'  │     1     │    1³ = 1            │   0+1=1   │
#  │ '5'  │     5     │    5³ = 125          │  1+125=126│
#  │ '3'  │     3     │    3³ = 27           │ 126+27=153│
#  └──────┴───────────┴──────────────────────┴───────────┘
#
#  container = 153 == i = 153  ✅  → Armstrong number!
#
# -----------------------------------------------------------------------------
# 🧪 DRY RUN  |  i = 100  (not Armstrong)
# -----------------------------------------------------------------------------
#
#  digit   = "100"
#  power   = len("100") = 3
#  container = 0
#
#  ┌──────┬───────────┬──────────────────────┬───────────┐
#  │ char │  int(char)│  int(char) ** power  │ container │
#  ├──────┼───────────┼──────────────────────┼───────────┤
#  │ '1'  │     1     │    1³ = 1            │   0+1=1   │
#  │ '0'  │     0     │    0³ = 0            │   1+0=1   │
#  │ '0'  │     0     │    0³ = 0            │   1+0=1   │
#  └──────┴───────────┴──────────────────────┴───────────┘
#
#  container = 1 ≠ i = 100  ❌  → NOT Armstrong, skip!


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Convert to string to use len() and loop through digits
# 2. Always STORE conversions — str(i) alone throws the result away!
# 3. Reset container INSIDE outer loop, OUTSIDE inner loop
# 4. power = len(digit) — number of digits determines the power automatically!
# 5. Armstrong check AFTER inner loop but INSIDE outer loop
# 6. Typos create silent bugs — Python makes a new variable, no error! 🔍


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Digit Processing Pattern
# -----------------------------------------------------------------------------
# Whenever you need to process individual digits of a number:
#
#   for i in range(...):
#       digit = str(i)          # convert to string first!
#       result = 0              # reset accumulator inside outer loop!
#       power = len(digit)      # get number of digits
#
#       for char in digit:      # loop through each digit
#           result += int(char) ** power   # process each digit
#
#       if result == i:         # check condition after inner loop
#           print(i)
#
# This pattern appears in:
#   - Armstrong numbers
#   - Perfect numbers
#   - Digital root calculations
#   - Any "process each digit" problem
