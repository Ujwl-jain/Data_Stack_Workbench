# =============================================================================
# Q52 [Hard] - GCD using Euclidean Algorithm
# Find Greatest Common Divisor of two numbers using a loop
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# GCD = largest number that divides BOTH numbers evenly!
#
#   GCD(12, 8)  = 4  → 4 divides both 12 and 8   ✅
#   GCD(48, 18) = 6  → 6 divides both 48 and 18  ✅
#
# EUCLIDEAN ALGORITHM — 2000 year old algorithm! 🏛️
#
#   GCD(48, 18):
#   48 % 18 = 12  → now find GCD(18, 12)
#   18 % 12 = 6   → now find GCD(12, 6)
#   12 % 6  = 0   → remainder is 0 → GCD = 6! ✅
#
# Pattern:
#   Keep replacing (a, b) with (b, a % b)
#   Stop when b == 0
#   Answer = whatever a is at that point!


# -----------------------------------------------------------------------------
# 🧠 LOGIC
# -----------------------------------------------------------------------------
# 1. while b != 0 → keep going until remainder is 0
# 2. Inside loop → a, b = b, a % b  (simultaneous swap!)
# 3. When b == 0 → loop stops → return a


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — Why while loop not for loop?
# -----------------------------------------------------------------------------
# We don't know how many iterations it will take to reach b == 0
# while loop runs based on CONDITION — perfect here!
# Same reason as guessing game — "keep going until condition met"


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Simultaneous swap (same as bubble sort!)
# -----------------------------------------------------------------------------
#   a, b = b, a % b
#
# Both sides evaluated SIMULTANEOUSLY — same pattern from Q50!
#   a gets old b
#   b gets old a % b
#
# ❌ WRONG — sequential overwrites a before using it!
#   a = b
#   b = a % b   ← a is already changed! wrong result!
#
# ✅ CORRECT — simultaneous:
#   a, b = b, a % b   ← both use OLD values! ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — No if/else needed inside loop!
# -----------------------------------------------------------------------------
# Let the WHILE CONDITION handle the stopping — don't add early returns!
#
# ❌ Overcomplicated:
#   while b != 0:
#       r = a % b
#       if r == 0:
#           return a    # early return breaks the flow!
#       else:
#           ...
#
# ✅ Clean — while condition handles everything:
#   while b != 0:
#       a, b = b, a % b   # just update!
#   return a              # outside loop — only reached when b == 0!


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

def GCD(a, b):
    while b != 0:        # keep going until remainder is 0
        a, b = b, a % b  # swap simultaneously!
    return a             # when b==0, a is the GCD!

result = GCD(48, 18)
print(result)   # Output: 6


# -----------------------------------------------------------------------------
# 🧪 DRY RUN  |  GCD(48, 18)
# -----------------------------------------------------------------------------
#
#  ┌────────┬─────┬─────┬──────────┬──────────────────────────┐
#  │  step  │  a  │  b  │  a % b   │         action           │
#  ├────────┼─────┼─────┼──────────┼──────────────────────────┤
#  │ start  │ 48  │ 18  │  48%18=12│ b≠0 → a,b = 18, 12       │
#  │   1    │ 18  │ 12  │  18%12=6 │ b≠0 → a,b = 12, 6        │
#  │   2    │ 12  │  6  │  12%6=0  │ b≠0 → a,b = 6, 0         │
#  │   3    │  6  │  0  │    -     │ b==0 → loop stops!        │
#  └────────┴─────┴─────┴──────────┴──────────────────────────┘
#
#  return a = 6  ✅


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. GCD = largest number dividing both evenly
# 2. Euclidean algorithm → keep replacing (a,b) with (b, a%b) until b==0
# 3. while loop — don't know iterations upfront, condition-based stopping
# 4. Simultaneous swap → a,b = b, a%b — same pattern as bubble sort!
# 5. No if/else inside loop — let while condition handle stopping!
# 6. return OUTSIDE loop — only reached when b==0, a holds the answer!


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Euclidean GCD Pattern
# -----------------------------------------------------------------------------
#   def GCD(a, b):
#       while b != 0:
#           a, b = b, a % b
#       return a
#
# This pattern appears in:
#   - GCD calculations
#   - Simplifying fractions (divide by GCD!)
#   - LCM calculations → LCM(a,b) = (a*b) // GCD(a,b)
#   - Cryptography (RSA algorithm uses GCD!)
