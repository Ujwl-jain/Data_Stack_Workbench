# =============================================================================
# Q30 - Recursive Power Function (x^n)
# Compute x raised to the power n using recursion efficiently
# =============================================================================

# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Write a recursive function to compute x^n (x raised to power n).
# Must follow these rules:
#   - If n is even: x^n = (x^(n/2))^2
#   - If n is odd:  x^n = x * x^(n-1)
# Base case: When n == 0, return 1
#
# n is a non-negative integer. x can be int or float.


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPTS
# -----------------------------------------------------------------------------
# - Recursion breaks the big problem into smaller sub-problems.
# - In every call, n must become smaller (either halved or reduced by 1).
# - Even case is powerful because it reduces n by half quickly → efficient.
# - This technique is called "Exponentiation by Squaring".


# -----------------------------------------------------------------------------
# ✅ MY ORIGINAL CODE (Logically Correct)
# -----------------------------------------------------------------------------
# Your version (always uses n//2 + x*half*half for odd case)
def power_original(x, n):
    if n == 0:
        return 1
    
    half = power_original(x, n // 2)   # Always compute n//2

    if n % 2 == 0:
        return half * half
    else:
        return x * half * half         # This works mathematically!


# -----------------------------------------------------------------------------
# ✅ CORRECTED / QUESTION-COMPLIANT VERSION (Recommended)
# -----------------------------------------------------------------------------
# Follows the exact rules given in the question
def power(x, n):
    if n == 0:                          # Base Case
        return 1
    
    if n % 2 == 0:
        # Even case as per question: x^n = (x^(n/2))^2
        half = power(x, n // 2)
        return half * half
    else:
        # Odd case as per question: x^n = x * x^(n-1)
        return x * power(x, n - 1)


# -----------------------------------------------------------------------------
# 🧪 TEST CASES
# -----------------------------------------------------------------------------
print("Original version:", power_original(3, 6))   # 729
print("Corrected version:", power(3, 6))           # 729
print(power(2, 0))                                 # 1
print(power(5, 1))                                 # 5
print(power(2, 10))                                # 1024
print(power(7, 3))                                 # 343


# -----------------------------------------------------------------------------
# 🧪 DETAILED DRY RUN — Corrected Version | power(3, 6)
# -----------------------------------------------------------------------------
# We will trace every recursive call step by step.

# Call 1: power(3, 6)
#   n = 6 → even
#   So, compute half = power(3, 3)
#   Then return half * half  (we don't know half yet)

# Call 2: power(3, 3)     ← called from above
#   n = 3 → odd
#   So, return 3 * power(3, 2)

# Call 3: power(3, 2)     ← called from above
#   n = 2 → even
#   So, compute half = power(3, 1)
#   Then return half * half

# Call 4: power(3, 1)     ← called from above
#   n = 1 → odd
#   So, return 3 * power(3, 0)

# Call 5: power(3, 0)     ← deepest call
#   n = 0 → Base Case
#   Return 1

# Now unwinding (returning back):

# Back to Call 4: power(3, 1)
#   Received 1 from power(3,0)
#   Returns 3 * 1 = 3

# Back to Call 3: power(3, 2)
#   Received 3 from power(3,1)
#   Returns 3 * 3 = 9

# Back to Call 2: power(3, 3)
#   Received 9 from power(3,2)
#   Returns 3 * 9 = 27

# Back to Call 1: power(3, 6)
#   Received 27 from power(3,3)
#   Returns 27 * 27 = 729 ✅

# Final Result: 729


# -----------------------------------------------------------------------------
# 🧪 DETAILED DRY RUN — Your Original Version | power_original(3, 6)
# -----------------------------------------------------------------------------
# Call 1: power_original(3, 6)
#   n=6 even, half = power_original(3, 3)
#   Will return half * half

# Call 2: power_original(3, 3)
#   n=3 odd, half = power_original(3, 1)
#   Returns 3 * half * half

# Call 3: power_original(3, 1)
#   n=1 odd, half = power_original(3, 0)
#   Returns 3 * half * half

# Call 4: power_original(3, 0)
#   Base case → returns 1

# Unwinding:

# power_original(3,1) → half=1 → 3 * 1 * 1 = 3
# power_original(3,3) → half=3 → 3 * 3 * 3 = 27
# power_original(3,6) → half=27 → 27 * 27 = 729 ✅

# Note: Both versions give same answer, but the corrected one follows the question rules more strictly.


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS & NEW CONCEPTS LEARNED
# -----------------------------------------------------------------------------
# 1. Base case is very important — without it recursion never stops.
# 2. In recursive power, we have two ways to reduce n: halve it (even) or subtract 1 (odd).
# 3. Your original logic was mathematically correct, but the question wanted us to use the exact even/odd rules.
# 4. Detailed dry run helps us understand how values flow back during recursion unwinding.
# 5. This "Exponentiation by Squaring" pattern is very useful and appears in many advanced problems.


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER
# -----------------------------------------------------------------------------
# def power(x, n):
#     if n == 0:
#         return 1
#     if n % 2 == 0:
#         half = power(x, n // 2)
#         return half * half
#     else:
#         return x * power(x, n - 1)