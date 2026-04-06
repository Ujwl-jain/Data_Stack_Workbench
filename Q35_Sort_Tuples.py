# =============================================================================
# Q35 [Medium] - Sort a List of Tuples
# Sort by second element, then first element as tiebreaker
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Sort list of tuples by SECOND element first.
# If two tuples have same second element → sort by FIRST element as tiebreaker!
#
# Example:
#   [(1,3), (2,1), (4,1), (3,2)]
#   (2,1) and (4,1) → both have second=1 → tiebreak by first → 2 < 4
#   Output: [(2,1), (4,1), (3,2), (1,3)]


# -----------------------------------------------------------------------------
# 🧠 LOGIC
# -----------------------------------------------------------------------------
# 1. Use sorted() with key=lambda
# 2. Lambda returns a TUPLE (x[1], x[0]) as the sorting key
# 3. Python sorts key tuples left to right → second element first, first element second
# 4. Tiebreaker happens automatically when first key values are equal!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — What is a Lambda?
# -----------------------------------------------------------------------------
# A lambda is a MINI FUNCTION in one line!
#
# Normal function:            Lambda equivalent:
#   def get_second(x):          lambda x: x[1]
#       return x[1]
#
# x = input (each tuple)
# x[1] = what it returns
#
# Used inside sorted() as the key:
#   sorted(list, key=lambda x: x[1])   ← sort by second element


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Tuple key for tiebreaker
# -----------------------------------------------------------------------------
# Return a TUPLE from lambda to sort by multiple criteria:
#
#   key=lambda x: (x[1], x[0])
#                   ↑       ↑
#             primary   tiebreaker
#
# Python compares tuples LEFT TO RIGHT — exactly like tiebreaker rules!
#   First compares x[1] → if equal → compares x[0]
#
# Same idea works for any number of tiebreakers:
#   key=lambda x: (x[2], x[1], x[0])   ← sort by 3rd, then 2nd, then 1st


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

list_tup = [(1, 3), (2, 1), (4, 1), (3, 2)]

final_list = sorted(list_tup, key=lambda x: (x[1], x[0]))
print(final_list)
# Output: [(2, 1), (4, 1), (3, 2), (1, 3)]


# -----------------------------------------------------------------------------
# 🧪 DRY RUN  |  Input: [(1,3), (2,1), (4,1), (3,2)]
# -----------------------------------------------------------------------------
#
#  Step 1 — Generate key for each tuple:
#  ┌────────────────┬──────────────────────────┐
#  │ Original tuple │ Key generated (x[1],x[0])│
#  ├────────────────┼──────────────────────────┤
#  │   (1, 3)       │        (3, 1)             │
#  │   (2, 1)       │        (1, 2)             │
#  │   (4, 1)       │        (1, 4)             │
#  │   (3, 2)       │        (2, 3)             │
#  └────────────────┴──────────────────────────┘
#
#  Step 2 — Sort keys smallest to largest:
#  (1,2) → first element=1, second=2
#  (1,4) → first element=1, second=4  ← same first! tiebreak → 2<4
#  (2,3) → first element=2
#  (3,1) → first element=3
#
#  Step 3 — Map back to original tuples:
#  (1,2) → (2,1)
#  (1,4) → (4,1)
#  (2,3) → (3,2)
#  (3,1) → (1,3)
#
#  ✅ Output: [(2,1), (4,1), (3,2), (1,3)]


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. lambda x: expression  →  mini function, x is input, expression is return
# 2. key=lambda x: x[1]    →  sort by second element
# 3. key=lambda x: (x[1], x[0])  →  sort by second, tiebreak by first
# 4. Python compares tuples left to right — tiebreaker is automatic!
# 5. No () on len, no () on lambda — pass the function, don't call it!


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Lambda Sort Pattern
# -----------------------------------------------------------------------------
# Single criteria:    sorted(lst, key=lambda x: x[1])
# Two criteria:       sorted(lst, key=lambda x: (x[1], x[0]))
# Reverse order:      sorted(lst, key=lambda x: x[1], reverse=True)
#
# This pattern appears in:
#   - Sorting tuples by any element
#   - Sorting list of dicts by a key
#   - Leaderboard rankings
#   - Any multi-criteria sort problem
