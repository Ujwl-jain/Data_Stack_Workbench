# =============================================================================
# Q50 [Hard] - Bubble Sort
# Implement using nested loops and count the number of swaps made
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Bubble sort is a sorting algorithm that works by REPEATEDLY comparing
# two ADJACENT elements and swapping them if they're in the wrong order.
#
# It's called "bubble" because larger numbers BUBBLE UP to the end
# of the list with each pass! 🫧
#
# Visual — one pass through [5, 3, 8, 1]:
#   [5, 3, 8, 1] → compare 5,3 → swap! → [3, 5, 8, 1]
#   [3, 5, 8, 1] → compare 5,8 → ok!   → [3, 5, 8, 1]
#   [3, 5, 8, 1] → compare 8,1 → swap! → [3, 5, 1, 8]
#   After one pass → 8 bubbled to the end! ✅
#   Repeat for remaining elements until fully sorted!


# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# 1. Define unsorted list, set swap counter to 0
# 2. Outer loop → controls number of PASSES → range(len(list)-1)
# 3. Inner loop → compares ADJACENT pairs → range(len(list) - 1 - i)
#                 shrinks each pass — last elements already sorted!
# 4. If list[j] > list[j+1] → swap simultaneously → increment counter
# 5. Print sorted list and total swap count


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — Python Simultaneous Swap
# -----------------------------------------------------------------------------
# ❌ WRONG — overwrites value before saving it!
#   list[i] = list[i+1]    # original list[i] is LOST!
#   list[i+1] = list[i]    # now both are same value!
#
# ✅ CORRECT — Python swaps SIMULTANEOUSLY in one line!
#   list[i], list[i+1] = list[i+1], list[i]
#
# Think of it like two people swapping seats at the SAME TIME
# not one after the other!
#
# Python evaluates the RIGHT side completely first:
#   right side = (list[i+1], list[i]) → tuple created in memory
#   then assigns back to left side simultaneously ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Why outer loop uses len(list) - 1
# -----------------------------------------------------------------------------
# List has 6 elements — how many PASSES do you need?
#
#   Pass 1 → biggest bubbles to end
#   Pass 2 → 2nd biggest settles
#   Pass 3 → 3rd biggest settles
#   Pass 4 → 4th biggest settles
#   Pass 5 → 5th biggest settles
#   Pass 6 → ??? → only 1 element left → already sorted by default!
#
#   6 elements need only 5 passes!
#   Last element is always already in place — no pass needed for it!
#
#   range(len(lst) - 1)  →  6-1 = 5 passes ✅
#   range(len(lst))      →  6 passes → last pass does NOTHING, waste! ❌


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Why inner loop uses len(list) - 1 - element
# -----------------------------------------------------------------------------
# After each pass, ONE MORE element is sorted at the end — no need to check it again!
#
#   Pass 1 done → [3, 5, 1, 8] → 8 is sorted, don't touch it!
#   Pass 2 done → [3, 1, 5, 8] → 5, 8 sorted, don't touch them!
#   Pass 3 done → [1, 3, 5, 8] → done! ✅
#
# In numbers (6 element list):
#   element=0 → range(6-1-0) = range(5) → checks 5 pairs ✅
#   element=1 → range(6-1-1) = range(4) → checks 4 pairs (last sorted!) ✅
#   element=2 → range(6-1-2) = range(3) → checks 3 pairs ✅
#   element=3 → range(6-1-3) = range(2) → checks 2 pairs ✅
#   element=4 → range(6-1-4) = range(1) → checks 1 pair  ✅
#
# The -1 stops inner loop from going out of bounds (ele+1 would crash!)
# The -element shrinks the window — ignores already sorted tail!
#
# Without -element → every pass checks ALL pairs → wastes time! ❌


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 4 — How the loops actually work (code → theory connection)
# -----------------------------------------------------------------------------
# Your two loop variables do very different jobs:
#
#   `element` = which PASS you're on (outer loop)
#   `ele`     = which PAIR you're comparing right now (inner loop)
#
# `element` NEVER touches the list directly!
# It only controls how many times the inner loop runs:
#
#   element=0 → pass 1 → ele walks 0,1,2,3,4  (full length)
#   element=1 → pass 2 → ele walks 0,1,2,3    (shorter)
#   element=2 → pass 3 → ele walks 0,1,2      (even shorter)
#
# `ele` IS the moving finger — it's the actual index used to compare:
#   unsorted_lst[ele] vs unsorted_lst[ele+1]
#   → always comparing TWO neighbors at current position
#   → ele moves forward by 1 each iteration regardless of swap or not!
#
# Live trace [5, 3, 8, 1]:
#   element=0, ele=0 → [5] vs [3] → swap  → [3, 5, 8, 1]  finger moves →
#   element=0, ele=1 → [5] vs [8] → ok    → [3, 5, 8, 1]  finger moves →
#   element=0, ele=2 → [8] vs [1] → swap  → [3, 5, 1, 8]  pass done!
#
# Finger NEVER goes back — always moves right, swap or not! 🎯


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 5 — Swap counter placement
# -----------------------------------------------------------------------------
# Same lesson as attempt counter in guessing game —
# count ONLY when the condition is met (swap happens):
#
#   if list[ele] > list[ele+1]:
#       swap_count += 1          # count only when swapping!
#       list[ele], list[ele+1] = list[ele+1], list[ele]
#
# Not every comparison = a swap, only some do!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 6 — Clean if condition, no redundant else
# -----------------------------------------------------------------------------
# ❌ Redundant version:
#   if list[ele] <= list[ele+1]:
#       "No swap"                  # string does NOTHING! not even a comment!
#   elif list[ele] > list[ele+1]:
#       swap...
#
# ✅ Clean version — one condition, no else needed:
#   if list[ele] > list[ele+1]:
#       swap...
#   # if condition fails → nothing happens automatically!
#
# Note: "No swap" as a string is NOT a comment — use # for comments
#       and pass as a placeholder if needed


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

unsorted_lst = [32, 4, 52, 1, 5, 2]
swap_count = 0

for element in range(len(unsorted_lst) - 1):           # outer: number of passes
    for ele in range(len(unsorted_lst) - 1 - element): # inner: shrinks each pass!
        if unsorted_lst[ele] > unsorted_lst[ele + 1]:  # wrong order?
            swap_count += 1                             # count the swap
            unsorted_lst[ele], unsorted_lst[ele + 1] = unsorted_lst[ele + 1], unsorted_lst[ele]

print(unsorted_lst, 'and', swap_count)
# Output: [1, 2, 4, 5, 32, 52] and 8


# -----------------------------------------------------------------------------
# 🧪 DRY RUN  |  Input: [32, 4, 52, 1, 5, 2]  |  Simplified to [5, 3, 8, 1]
# -----------------------------------------------------------------------------
#
#  swap_count = 0
#
#  PASS 1 (element=0) → inner range(3) → checks indices 0,1,2
#  ┌──────┬──────┬────────────┬───────────────┬───────────────────┬───────┐
#  │ ele  │ ele+1│  compare   │   action      │      list         │ swaps │
#  ├──────┼──────┼────────────┼───────────────┼───────────────────┼───────┤
#  │  0   │  1   │  5 > 3?  ✅│  swap!        │ [3, 5, 8, 1]      │   1   │
#  │  1   │  2   │  5 > 8?  ❌│  no swap      │ [3, 5, 8, 1]      │   1   │
#  │  2   │  3   │  8 > 1?  ✅│  swap!        │ [3, 5, 1, 8]      │   2   │
#  └──────┴──────┴────────────┴───────────────┴───────────────────┴───────┘
#  → 8 bubbled to end! 🫧
#
#  PASS 2 (element=1) → inner range(2) → checks indices 0,1
#  ┌──────┬──────┬────────────┬───────────────┬───────────────────┬───────┐
#  │  0   │  1   │  3 > 5?  ❌│  no swap      │ [3, 5, 1, 8]      │   2   │
#  │  1   │  2   │  5 > 1?  ✅│  swap!        │ [3, 1, 5, 8]      │   3   │
#  └──────┴──────┴────────────┴───────────────┴───────────────────┴───────┘
#
#  PASS 3 (element=2) → inner range(1) → checks index 0 only
#  ┌──────┬──────┬────────────┬───────────────┬───────────────────┬───────┐
#  │  0   │  1   │  3 > 1?  ✅│  swap!        │ [1, 3, 5, 8]      │   4   │
#  └──────┴──────┴────────────┴───────────────┴───────────────────┴───────┘
#
#  ✅ Final Output: [1, 3, 5, 8]  |  Total swaps: 4


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Bubble sort = compare adjacent pairs, swap if wrong order, repeat
# 2. Python swap → a, b = b, a  (simultaneous, no temp variable needed!)
# 3. Inner loop shrinks each pass → already sorted elements ignored
# 4. Count swaps INSIDE the if condition — not every comparison is a swap
# 5. A plain string like "No swap" does NOTHING — use pass or just omit!
# 6. One clean if condition beats redundant if/elif for opposite cases


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Bubble Sort Pattern
# -----------------------------------------------------------------------------
# Whenever you need to sort by repeatedly comparing adjacent elements:
#
#   swap_count = 0
#   for i in range(len(lst) - 1):              # passes
#       for j in range(len(lst) - 1 - i):      # shrinking window
#           if lst[j] > lst[j+1]:              # wrong order?
#               swap_count += 1
#               lst[j], lst[j+1] = lst[j+1], lst[j]  # swap!
#
# This pattern appears in:
#   - Sorting algorithms (bubble, insertion concepts)
#   - Finding inversions in a list
#   - Ranking systems
#   - Any "compare neighbors and fix" problem
