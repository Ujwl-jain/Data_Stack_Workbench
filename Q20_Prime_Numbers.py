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
# ✅ METHOD 1 — Normal Loop
# -----------------------------------------------------------------------------

n = 10
list_prime = []

def is_prime(n):
    if n < 2:
        return False          # 0, 1, negatives → not prime
    for i in range(2, n):    # check every number from 2 to n-1
        if n % i == 0:
            return False      # divisor found → not prime
    return True               # no divisors found → prime!

for i in range(2, n + 1):    # loop from 2 to N (inclusive)
    if is_prime(i):           # if True → it's prime
        list_prime.append(i)

print(list_prime)
# Output: [2, 3, 5, 7]


# -----------------------------------------------------------------------------
# ✅ METHOD 2 — List Comprehension (Same result, 1 line!)
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
