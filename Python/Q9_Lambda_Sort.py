# =============================================================================
# Q9 - Lambda Sort by Score Descending
# Sort list of (name, subject, score) tuples by score descending
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Sort a list of tuples by score in DESCENDING order (highest first)
# With tiebreaker by name
#
# Input:  [('alice', 'maths', 85), ('matter', 'english', 98),
#          ('alice', 'ciene', 18), ('matter', 'hindi', 99),
#          ('harry', 'sst', 77),   ('DJ', 'sports', 99)]
#
# Output: sorted by score high→low, same score → sorted by name


# -----------------------------------------------------------------------------
# 🧠 LOGIC
# -----------------------------------------------------------------------------
# Use sorted() with lambda key
# Sort by score (index 2) descending, name (index 0) as tiebreaker
# Two approaches — reverse=True OR minus trick


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — reverse=True reverses EVERYTHING
# -----------------------------------------------------------------------------
# ❌ PROBLEM with reverse=True on tuple key:
#
#   sorted(data, key=lambda x: (x[2], x[0]), reverse=True)
#
#   Both x[2] AND x[0] get reversed:
#   score → descending ✅
#   name  → Z to A     ❌ (wanted A to Z!)
#
# Use when you want ALL criteria reversed — otherwise use minus trick!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — The Minus Trick (-x[2])
# -----------------------------------------------------------------------------
# Negate a number to flip its sort direction WITHOUT reverse=True!
#
#   score=99 → -99   (now smallest = was biggest!)
#   score=85 → -85
#   score=77 → -77
#
#   Sorting -99, -85, -77 ASCENDING = sorting 99, 85, 77 DESCENDING! 🎯
#
# Each field gets its OWN direction:
#   key=lambda x: (-x[2], x[0])
#                   ↑        ↑
#              descending  ascending
#              (minus)     (normal)
#
# ⚠️  Only works for NUMBERS — can't negate strings (-x[0] breaks!)


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Key is TEMPORARY, never touches actual data!
# -----------------------------------------------------------------------------
# The key is just a LABEL used for comparison — thrown away after sorting!
#
#   Original data  →  Temp key (sorting only)  →  Final output
#   ('alice', 85)  →     (-85, 'alice')         →  ('alice', 85)
#   ('matter', 99) →     (-99, 'matter')         →  ('matter', 99)
#
# Python uses negative keys to DECIDE ORDER
# then puts ORIGINAL tuples in that order!
#
# Think of it like a race 🏃:
#   Runners line up by negative score (key)
#   -99 goes first → runner still has real name and score!
#   Final result → runners in order, all with ORIGINAL data ✅
#
# Same reason key=len in Q27 didn't replace strings with numbers —
# len was just the measuring stick, strings stayed as strings!


# -----------------------------------------------------------------------------
# ✅ METHOD 1 — reverse=True (both criteria reversed)
# -----------------------------------------------------------------------------

data = [('alice', 'maths', 85), ('matter', 'english', 98),
        ('alice', 'ciene', 18), ('matter', 'hindi', 99),
        ('harry', 'sst', 77),   ('DJ', 'sports', 99)]

final_list = sorted(data, key=lambda x: (x[2], x[0]), reverse=True)
print(final_list)
# score descending ✅, name Z→A (reverse alphabetical) ⚠️


# -----------------------------------------------------------------------------
# ✅ METHOD 2 — Minus trick (score descending, name ascending)
# -----------------------------------------------------------------------------

final_list2 = sorted(data, key=lambda x: (-x[2], x[0]))
print(final_list2)
# score descending ✅, name A→Z ✅  (each field its own direction!)


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Minus Trick  |  key=lambda x: (-x[2], x[0])
# -----------------------------------------------------------------------------
#
#  Step 1 — Generate temp keys:
#  ┌──────────────────────────┬──────────────────────┐
#  │       Original tuple     │      Temp key         │
#  ├──────────────────────────┼──────────────────────┤
#  │ ('alice', 'maths', 85)   │    (-85, 'alice')     │
#  │ ('matter', 'english', 98)│    (-98, 'matter')    │
#  │ ('alice', 'ciene', 18)   │    (-18, 'alice')     │
#  │ ('matter', 'hindi', 99)  │    (-99, 'matter')    │
#  │ ('harry', 'sst', 77)     │    (-77, 'harry')     │
#  │ ('DJ', 'sports', 99)     │    (-99, 'DJ')        │
#  └──────────────────────────┴──────────────────────┘
#
#  Step 2 — Sort temp keys ascending:
#  (-99, 'DJ')      ← -99 smallest, 'DJ' < 'matter' tiebreak ✅
#  (-99, 'matter')  ← -99 tie → compare name → D < m
#  (-98, 'matter')
#  (-85, 'alice')
#  (-77, 'harry')
#  (-18, 'alice')
#
#  Step 3 — Return ORIGINAL tuples in that order (keys thrown away!):
#  ('DJ', 'sports', 99)      ← no negative in output! ✅
#  ('matter', 'hindi', 99)
#  ('matter', 'english', 98)
#  ('alice', 'maths', 85)
#  ('harry', 'sst', 77)
#  ('alice', 'ciene', 18)


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. reverse=True reverses ALL criteria — use when everything goes same direction
# 2. Minus trick (-x[n]) → flips ONE numeric field direction independently
# 3. Key is TEMPORARY — only used for comparison, never appears in output!
# 4. Can't negate strings — minus trick only works for numbers
# 5. Adjusting index in lambda → works for any tuple size (2, 3, 4 elements)


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Mixed Direction Sort
# -----------------------------------------------------------------------------
#   # All same direction:
#   sorted(data, key=lambda x: (x[1], x[0]), reverse=True)
#
#   # Mixed directions (numbers only):
#   sorted(data, key=lambda x: (-x[2], x[0]))
#   #                            ↑        ↑
#   #                       descending  ascending
#
# This pattern appears in:
#   - Leaderboards (score high→low, name A→Z)
#   - Product listings (price low→high, rating high→low)
#   - Any multi-criteria sort with different directions
