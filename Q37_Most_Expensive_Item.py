# =============================================================================
# Q37 [Hard] - Find Most Expensive Item Without max()
# Given a list of (item, price) tuples
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Find the most expensive item from a list of (item, price) tuples
# WITHOUT using max()!
#
# Input:  [('apple', 30), ('laptop', 80000), ('pen', 10), ('phone', 50000)]
# Output: laptop 80000


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — Tuple Unpacking in Loop
# -----------------------------------------------------------------------------
# Python can unpack a tuple DIRECTLY in the loop!
#
# Without unpacking:          With unpacking:
#   for t in items:             for item, price in items:
#       t[0]  # item                item   ✅ cleaner!
#       t[1]  # price               price  ✅
#
# Same as:  a, b = (1, 2)  → a=1, b=2
# Loop just does it automatically for each tuple!


# -----------------------------------------------------------------------------
# ✅ METHOD 1 — Sorting with Lambda (reverse=True → biggest first)
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Sort by second element (price) in REVERSE order
# 2. First element of sorted list = most expensive
# 3. Unpack first tuple to get item and price separately

list_items = [('apple', 30), ('laptop', 80000), ('pen', 10), ('phone', 50000)]

final_list = sorted(list_items, key=lambda x: x[1], reverse=True)
item, price = final_list[0]        # unpack first tuple — not whole tuple!
print(item, price)
# Output: laptop 80000


# -----------------------------------------------------------------------------
# ✅ METHOD 2 — Manual Max Loop (no sorting needed!)
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Start with max_price = 0, max_item = ''
# 2. Loop through each (item, price) using tuple unpacking
# 3. If price > max_price → update both max_price and max_item
# 4. After loop → max_item and max_price hold the answer
#
# Same pattern as bubble sort — "keep track of biggest seen so far!"

max_item = ''
max_price = 0
for item, price in list_items:
    if price > max_price:
        max_price = price
        new_item = item

print(new_item, max_price)
# Output: laptop 80000


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Tuple unpacking in loop → for item, price in list  (cleaner than t[0], t[1])
# 2. final_list[0] returns WHOLE tuple → unpack it to get separate values!
# 3. Method 1 (sort) → simple but sorts entire list just to find one value
# 4. Method 2 (loop) → more efficient, only one pass through list
# 5. Manual max pattern → start at 0, update when bigger found
#    Same idea used in bubble sort — "keep track of biggest seen so far!"


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Manual Max Pattern
# -----------------------------------------------------------------------------
#   max_val  = 0
#   max_item = ''
#   for item, value in list_of_tuples:
#       if value > max_val:
#           max_val  = value    # update max
#           max_item = item     # track which item had the max
#
# This pattern appears in:
#   - Finding most expensive item
#   - Finding highest score
#   - Finding longest word
#   - Any "find the biggest without max()" problem
