# =============================================================================
# Q19 [Hard] - Multiplication Table (1-10) as 2D List
# Generate using both normal loops AND nested list comprehension
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# A multiplication table (1-10) looks like this:
#
#   1×1=1,   1×2=2,   1×3=3  ...  1×10=10
#   2×1=2,   2×2=4,   2×3=6  ...  2×10=20
#   ...
#   10×1=10, 10×2=20  ...    ...  10×10=100
#
# A 2D list = a list of lists:
#   [
#     [1,  2,  3  ... 10],    ← row 1
#     [2,  4,  6  ... 20],    ← row 2
#     ...
#     [10, 20, 30 ... 100]    ← row 10
#   ]
#
# Final result → 1 big list containing 10 lists, each with 10 numbers


# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# 1. Create empty final_list to store all rows
# 2. Outer loop → row from 1 to 10 (each row = one multiplication table)
# 3. Create empty list_cal INSIDE outer loop (resets for each new row!)
# 4. Inner loop → column from 1 to 10
# 5. Multiply row × column → append result to list_cal
# 6. After inner loop finishes → append list_cal to final_list
# 7. Print final_list
#
# ⚠️  COMMON MISTAKE: list_cal must be created INSIDE outer loop, OUTSIDE inner loop
#     If created inside inner loop → resets every column → loses previous values!


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — Why range(1, 11) not range(1, 10)?
# -----------------------------------------------------------------------------
# range(1, 10) = 1,2,3,4,5,6,7,8,9      ← misses 10!
# range(1, 11) = 1,2,3,4,5,6,7,8,9,10   ✅
#
# Remember: range is EXCLUSIVE at the end — always +1 to include last number


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Building a 2D List
# -----------------------------------------------------------------------------
# 2D list = list of lists
# Pattern:
#   outer_list = []
#   for ...:
#       inner_list = []        ← reset for each row
#       for ...:
#           inner_list.append(value)
#       outer_list.append(inner_list)   ← append after inner loop


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — List Comprehension vs Normal Loop
# -----------------------------------------------------------------------------
# Normal loop (verbose but clear):
#   for row in range(1,11):
#       list_cal = []
#       for column in range(1,11):
#           list_cal.append(row * column)
#       table_list.append(list_cal)
#
# List comprehension (concise, Pythonic):
#   [[row*column for column in range(1,11)] for row in range(1,11)]
#
# How to read comprehension RIGHT TO LEFT:
#   → for row in range(1,11)           ← outer loop
#   → for column in range(1,11)        ← inner loop
#   → row*column                       ← expression/calculation
#   → [row*column for column in ...]   ← inner list (one row)
#   → [[...] for row in ...]           ← outer list (all rows)


# -----------------------------------------------------------------------------
# ✅ METHOD 1 — Normal Loop
# -----------------------------------------------------------------------------

table_list = []

for row in range(1, 11):
    list_cal = []                        # reset inner list for each row
    for column in range(1, 11):
        mat = row * column               # calculate product
        list_cal.append(mat)             # add to current row
    table_list.append(list_cal)          # add completed row to final list

print(table_list)


# -----------------------------------------------------------------------------
# ✅ METHOD 2 — Nested List Comprehension (Same result, 1 line!)
# -----------------------------------------------------------------------------

list_Comp = [[row * column for column in range(1, 11)] for row in range(1, 11)]

print(list_Comp)


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Normal Loop  |  Simplified to range(1,4) for clarity
# -----------------------------------------------------------------------------
#
#  table_list = []
#
#  ┌─────┬────────┬──────────────┬─────────────────────┬──────────────────────────┐
#  │ row │ column │  row*column  │      list_cal        │       table_list         │
#  ├─────┼────────┼──────────────┼─────────────────────┼──────────────────────────┤
#  │  1  │   1    │   1×1 = 1    │ [1]                 │ []                       │
#  │  1  │   2    │   1×2 = 2    │ [1, 2]              │ []                       │
#  │  1  │   3    │   1×3 = 3    │ [1, 2, 3]           │ []                       │
#  │     │        │ ← inner done │                     │ [[1,2,3]]  ← appended!   │
#  ├─────┼────────┼──────────────┼─────────────────────┼──────────────────────────┤
#  │  2  │   1    │   2×1 = 2    │ [2]                 │ [[1,2,3]]                │
#  │  2  │   2    │   2×2 = 4    │ [2, 4]              │ [[1,2,3]]                │
#  │  2  │   3    │   2×3 = 6    │ [2, 4, 6]           │ [[1,2,3]]                │
#  │     │        │ ← inner done │                     │ [[1,2,3],[2,4,6]] ✅     │
#  ├─────┼────────┼──────────────┼─────────────────────┼──────────────────────────┤
#  │  3  │   1    │   3×1 = 3    │ [3]                 │ [[1,2,3],[2,4,6]]        │
#  │  3  │   2    │   3×2 = 6    │ [3, 6]              │ [[1,2,3],[2,4,6]]        │
#  │  3  │   3    │   3×3 = 9    │ [3, 6, 9]           │ [[1,2,3],[2,4,6]]        │
#  │     │        │ ← inner done │                     │ [[1,2,3],[2,4,6],[3,6,9]]│
#  └─────┴────────┴──────────────┴─────────────────────┴──────────────────────────┘
#
#  ✅ Final Output (1-3 table): [[1,2,3], [2,4,6], [3,6,9]]
#
# -----------------------------------------------------------------------------
# 🧪 DRY RUN — List Comprehension  |  Same range(1,4) example
# -----------------------------------------------------------------------------
#
#  [[row*column for column in range(1,4)] for row in range(1,4)]
#
#  Step 1 → outer loop picks row=1
#           inner → [1×1, 1×2, 1×3] = [1, 2, 3]
#
#  Step 2 → outer loop picks row=2
#           inner → [2×1, 2×2, 2×3] = [2, 4, 6]
#
#  Step 3 → outer loop picks row=3
#           inner → [3×1, 3×2, 3×3] = [3, 6, 9]
#
#  Final → [[1,2,3], [2,4,6], [3,6,9]] ✅  (same as normal loop!)


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. range(1, 11) not range(1, 10) — always +1 to include last number
# 2. Inner list must be RESET inside outer loop, OUTSIDE inner loop
# 3. Append inner list to outer list AFTER inner loop completes
# 4. List comprehension = same logic, just written inside-out in one line
# 5. Read comprehension right to left → outer loop first, inner loop second


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — 2D List Building Pattern
# -----------------------------------------------------------------------------
# Whenever you need to build a 2D list (matrix/table):
#
#   METHOD 1 (Normal):
#   result = []
#   for i in range(...):
#       row = []
#       for j in range(...):
#           row.append(expression)
#       result.append(row)
#
#   METHOD 2 (Comprehension):
#   result = [[expression for j in range(...)] for i in range(...)]
#
# This pattern appears in:
#   - Multiplication tables
#   - Matrix operations
#   - Game boards (chess, tic-tac-toe)
#   - Image pixel grids
#   - Distance/cost matrices
