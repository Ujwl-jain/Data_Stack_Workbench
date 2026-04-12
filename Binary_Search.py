# =============================================================================
# Binary Search — Implement on a sorted list using a while loop
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Binary search finds a target in a SORTED list by cutting the search
# space in HALF each time — much faster than checking every element!
#
# Think of it like a guessing game (1 to 100):
#   You guess 50 → "too high" → search 1-49
#   You guess 25 → "too low"  → search 26-49
#   You guess 37 → "correct!" ✅
#
# Visual on a list:
#   list = [1, 3, 5, 7, 9, 11, 13, 15]   target = 11
#
#   Step 1 → mid = index 3 → value 7  → 11 > 7  → search RIGHT half
#   Step 2 → mid = index 5 → value 11 → FOUND! ✅


# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# 1. Define sorted list, take user input as target
# 2. If target not in list → raise error → exit
# 3. Set start = 0, end = len(list) - 1
# 4. While start <= end:
#       → find mid = (start + end) // 2
#       → if list[mid] == target → FOUND! print index → break
#       → if list[mid] < target  → target in RIGHT half → start = mid + 1
#       → if list[mid] > target  → target in LEFT half  → end = mid - 1
# 5. If loop ends without finding → target not in list


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — start and end are INDICES not VALUES
# -----------------------------------------------------------------------------
# ❌ WRONG:
#   start = list_bin[0]   # this is the VALUE at index 0, not the index!
#
# ✅ CORRECT:
#   start = 0             # index 0
#   end = len(list) - 1   # last index
#
# Why? Because mid is calculated from indices:
#   mid = (start + end) // 2   → gives an INDEX number
#   list[mid]                  → use that index to get the VALUE


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — How to find the middle
# -----------------------------------------------------------------------------
# mid = (start + end) // 2    ← integer division, no decimals!
#
# Example:
#   start=0, end=6 → (0+6)//2 = 3  → index 3 is middle ✅
#   start=4, end=6 → (4+6)//2 = 5  → index 5 is middle ✅
#
# Why // not /? 
#   (0+7)/2  = 3.5  → can't use as index! ❌
#   (0+7)//2 = 3    → valid index ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — The 3 Conditions
# -----------------------------------------------------------------------------
# Once you find mid, compare list[mid] with target:
#
#   list[mid] == target → FOUND! return/print index
#   list[mid] < target  → target is BIGGER → must be in RIGHT half
#                       → eliminate left  → start = mid + 1
#   list[mid] > target  → target is SMALLER → must be in LEFT half
#                       → eliminate right → end = mid - 1
#
# Visual:
#   [1, 3, 5, 7, 9, 11, 13, 15]   target = 11
#               ↑ mid=7, too small → start = mid+1
#
#              [9, 11, 13, 15]
#                  ↑ mid=11 → FOUND! ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 4 — Why while loop, not for loop
# -----------------------------------------------------------------------------
# For loop iterates a fixed number of times
# While loop runs based on a CONDITION — perfect here because:
#   → we don't know how many steps it will take
#   → we stop when found OR when search space is exhausted
#
# while start <= end:   ← valid search space exists
# if start > end:       ← search space empty → target not found!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 5 — Why sort first?
# -----------------------------------------------------------------------------
# Binary search ONLY works on sorted lists!
# If unsorted, mid comparison means nothing:
#   [5, 1, 3, 7, 2]  target=3
#   mid=3 → 3 < 3? no, 3 > 3? no → found! but by luck
#   mid=7 → 3 < 7 → search left → but 3 might be on right! ❌


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

list_bin = [2, 4, 1, 5, 56, 12.59, 13]
list_bin.sort()                              # sort first! binary search needs sorted list

a = int(input("Enter the number to find: "))

try:
    if a not in list_bin:
        raise ValueError("Item not found")  # exit early if not in list

    start = 0                               # start = index 0, NOT list[0]!
    end = len(list_bin) - 1                 # end = last index

    while start <= end:                     # valid search space?
        mid = (start + end) // 2            # find middle index

        if list_bin[mid] == a:              # FOUND!
            print(f"Number found at index: {mid}")
            break
        elif list_bin[mid] < a:             # target in RIGHT half
            start = mid + 1                 # eliminate left
        elif list_bin[mid] > a:             # target in LEFT half
            end = mid - 1                   # eliminate right

except:
    print("Item not found")

# Example run:
#   list after sort: [1, 2, 4, 5, 12.59, 13, 56]
#   input: 13
#   Output: Number found at index: 5


# -----------------------------------------------------------------------------
# 🧪 DRY RUN  |  list = [1, 2, 4, 5, 12.59, 13, 56]  |  target = 13
# -----------------------------------------------------------------------------
#
#  Indices:  0    1    2    3     4      5    6
#  Values:  [1,   2,   4,   5,  12.59,  13,  56]
#
#  start=0, end=6
#
#  ┌────────┬──────┬─────┬────────────┬──────────────┬───────────────────────┐
#  │  step  │ start│ end │    mid     │  list[mid]   │      action           │
#  ├────────┼──────┼─────┼────────────┼──────────────┼───────────────────────┤
#  │   1    │  0   │  6  │ (0+6)//2=3 │   5          │ 13>5 → start=3+1=4    │
#  │   2    │  4   │  6  │ (4+6)//2=5 │   13         │ 13==13 → FOUND! ✅    │
#  └────────┴──────┴─────┴────────────┴──────────────┴───────────────────────┘
#
#  Output: Number found at index: 5 ✅
#
# -----------------------------------------------------------------------------
# 🧪 DRY RUN  |  target = 4  (left half case)
# -----------------------------------------------------------------------------
#
#  start=0, end=6
#
#  ┌────────┬──────┬─────┬────────────┬──────────────┬───────────────────────┐
#  │  step  │ start│ end │    mid     │  list[mid]   │      action           │
#  ├────────┼──────┼─────┼────────────┼──────────────┼───────────────────────┤
#  │   1    │  0   │  6  │ (0+6)//2=3 │   5          │ 4<5  → end=3-1=2      │
#  │   2    │  0   │  2  │ (0+2)//2=1 │   2          │ 4>2  → start=1+1=2    │
#  │   3    │  2   │  2  │ (2+2)//2=2 │   4          │ 4==4 → FOUND! ✅      │
#  └────────┴──────┴─────┴────────────┴──────────────┴───────────────────────┘
#
#  Output: Number found at index: 2 ✅


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. start and end are INDICES — never values!
# 2. mid = (start + end) // 2 — always integer division
# 3. 3 conditions: equal (found), less (go right), greater (go left)
# 4. start = mid+1 eliminates left half, end = mid-1 eliminates right half
# 5. while start <= end — loop stops when search space is empty
# 6. Binary search ONLY works on sorted lists — always sort first!
# 7. try/except handles invalid input gracefully


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Binary Search Pattern
# -----------------------------------------------------------------------------
# Whenever you need to search in a sorted list efficiently:
#
#   start = 0
#   end = len(list) - 1
#
#   while start <= end:
#       mid = (start + end) // 2
#       if list[mid] == target:
#           # found!
#       elif list[mid] < target:
#           start = mid + 1    # go right
#       else:
#           end = mid - 1      # go left
#
# This pattern appears in:
#   - Search algorithms
#   - Finding insertion point in sorted list
#   - Guess the number games
#   - Database index lookups
#   - Finding square roots (numerical methods)
