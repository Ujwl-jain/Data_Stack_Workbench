# =============================================================================
# Q57 - Sort and Deduplicate Coordinate Tuples
# Sort list of (x,y) tuples by x then y, return only unique coordinates
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Input:  [(1,2), (4,2), (4,1), (2,3), (1,2), (4,2), (1,9), (9,7)]
# Output: [(1,2), (1,9), (2,3), (4,1), (4,2), (9,7)]
#
# Two tasks:
#   1. Remove duplicates → (1,2) and (4,2) appear twice
#   2. Sort by x first, then y as tiebreaker


# -----------------------------------------------------------------------------
# 🧠 LOGIC
# -----------------------------------------------------------------------------
# 1. Remove duplicates FIRST using set() → set destroys order!
# 2. Convert back to list
# 3. Sort using lambda with tuple key (x[0], x[1])
# 4. Return sorted unique list
#
# ORDER MATTERS:
#   ❌ Sort first → then set() → destroys sorted order!
#   ✅ Set first  → then sort() → clean result!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — set() removes duplicates automatically
# -----------------------------------------------------------------------------
# set() keeps only UNIQUE elements — duplicates silently dropped!
#
#   coords = [(1,2), (4,2), (1,2), (4,2)]
#   set(coords) → {(1,2), (4,2)}   ← duplicates gone! ✅
#
# WHY tuples work inside sets but lists don't:
#   Sets require IMMUTABLE elements
#   Tuples → immutable ✅ → work inside sets!
#   Lists  → mutable   ❌ → can't go inside sets!
#
# Always convert back to list after set():
#   list(set(coords))  → back to list for sorting!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — sorted() with [] wrapping bug
# -----------------------------------------------------------------------------
# sorted() ALREADY returns a list — wrapping in [] makes list inside list!
#
# ❌ WRONG:
#   final = [sorted(unique, key=lambda x: (x[0], x[1]))]
#   → [[( 1, 2), (1, 9), ...]]   extra brackets!
#
# ✅ CORRECT:
#   final = sorted(unique, key=lambda x: (x[0], x[1]))
#   → [(1, 2), (1, 9), ...]      clean list!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Lambda tuple key for multi-criteria sort
# -----------------------------------------------------------------------------
# key=lambda x: (x[0], x[1])
#   → sort by x coordinate first
#   → if x values equal → sort by y coordinate (tiebreaker)
#
# Same pattern from Q35! Python compares tuple keys left to right.
# Note: for coordinates (x[0], x[1]) is same as just x since
# Python already compares tuples element by element by default!
# But explicit is cleaner and more readable.


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

def cordinator(coords):
    unique_coords = list(set(coords))                              # remove duplicates!
    final_coords = sorted(unique_coords, key=lambda x: (x[0], x[1]))  # sort by x then y!
    return final_coords

coords = [(1,2), (4,2), (4,1), (2,3), (1,2), (4,2), (1,9), (9,7)]
result = cordinator(coords)
print(f"the result for the coordinator question is {result}")
# Output: [(1, 2), (1, 9), (2, 3), (4, 1), (4, 2), (9, 7)]


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — set() removing duplicates
# -----------------------------------------------------------------------------
#
#  Input: [(1,2), (4,2), (4,1), (2,3), (1,2), (4,2), (1,9), (9,7)]
#
#  set() processes each tuple:
#  ┌────────┬──────────────────────────────────────┐
#  │ tuple  │ action                               │
#  ├────────┼──────────────────────────────────────┤
#  │ (1,2)  │ new → add to set                     │
#  │ (4,2)  │ new → add to set                     │
#  │ (4,1)  │ new → add to set                     │
#  │ (2,3)  │ new → add to set                     │
#  │ (1,2)  │ already exists → SKIP! ✅            │
#  │ (4,2)  │ already exists → SKIP! ✅            │
#  │ (1,9)  │ new → add to set                     │
#  │ (9,7)  │ new → add to set                     │
#  └────────┴──────────────────────────────────────┘
#
#  unique_coords = [(1,2), (4,2), (4,1), (2,3), (1,9), (9,7)]  ← 6 items!
#
#
# 🧪 DRY RUN — sorted() with lambda key
# -----------------------------------------------------------------------------
#
#  key=lambda x: (x[0], x[1]) generates sort key for each tuple:
#
#  ┌──────────┬───────────────────┐
#  │  tuple   │  key generated    │
#  ├──────────┼───────────────────┤
#  │  (1, 2)  │     (1, 2)        │
#  │  (4, 2)  │     (4, 2)        │
#  │  (4, 1)  │     (4, 1)        │
#  │  (2, 3)  │     (2, 3)        │
#  │  (1, 9)  │     (1, 9)        │
#  │  (9, 7)  │     (9, 7)        │
#  └──────────┴───────────────────┘
#
#  Sort keys by first element, tiebreak by second:
#  (1,2) → x=1, y=2  ┐ x=1 tie! → compare y → 2 < 9
#  (1,9) → x=1, y=9  ┘
#  (2,3) → x=2
#  (4,1) → x=4, y=1  ┐ x=4 tie! → compare y → 1 < 2
#  (4,2) → x=4, y=2  ┘
#  (9,7) → x=9
#
#  ✅ Final: [(1,2), (1,9), (2,3), (4,1), (4,2), (9,7)]


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. set() removes duplicates — tuples work in sets (immutable), lists don't!
# 2. Remove duplicates FIRST, sort AFTER — set() destroys order!
# 3. sorted() returns a list — never wrap in [] or you get list inside list!
# 4. Lambda tuple key → (x[0], x[1]) → sort by x, tiebreak by y
# 5. Python compares tuple keys left to right — tiebreaker is automatic!


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Deduplicate then Sort
# -----------------------------------------------------------------------------
#   unique = list(set(data))                        # step 1: deduplicate
#   result = sorted(unique, key=lambda x: (x[0], x[1]))  # step 2: sort
#
# This pattern appears in:
#   - Coordinate processing
#   - Removing duplicate records
#   - Unique sorted leaderboards
#   - Any "unique + sorted" problem
