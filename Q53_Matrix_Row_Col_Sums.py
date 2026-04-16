# =============================================================================
# Q53 [Hard] - Matrix Row and Column Sums
# Given a 2D list, compute sum of each row and each column separately
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# matrix = [
#     [2, 4, 5],   ← row 0
#     [5, 1, 5],   ← row 1
#     [5, 6, 7]    ← row 2
# ]
#
# row_sums = [11, 11, 18]      # 2+4+5, 5+1+5, 5+6+7
# col_sums = [12, 11, 17]      # 2+5+5, 4+1+6, 5+5+7


# -----------------------------------------------------------------------------
# 🧠 LOGIC
# -----------------------------------------------------------------------------
# ROW SUMS:
#   outer loop → each row (list inside list)
#   inner loop → each element in that row
#   accumulate total → append to row_sum after inner loop
#
# COLUMN SUMS:
#   outer loop → col index FIXED each pass → range(len(matrix[0]))
#   inner loop → row index CHANGES         → range(len(matrix))
#   access via matrix[row][col] → row changes, col stays fixed!
#   accumulate total → append to col_sum after inner loop


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — len(matrix) vs len(matrix[0])
# -----------------------------------------------------------------------------
#   len(matrix)    = number of ROWS     (how many lists inside)
#   len(matrix[0]) = number of COLUMNS  (length of first row)
#
#   matrix = [[2,4,5],[5,1,5],[5,6,7]]
#   len(matrix)    = 3  → 3 rows
#   len(matrix[0]) = 3  → 3 columns


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — Row vs Column loop structure
# -----------------------------------------------------------------------------
# ROW SUMS — loop directly over elements:
#   for lst in matrix:          ← each row is a list
#       for element in lst:     ← each element in that row
#
# COLUMN SUMS — loop using indices:
#   for col in range(len(matrix[0])):    ← col index fixed
#       for row in range(len(matrix)):   ← row index changes
#           matrix[row][col]             ← row changes, col fixed!
#
# Visual for col=0:
#      col0
#   [  2,  4, 5]   → matrix[0][0] = 2
#   [  5,  1, 5]   → matrix[1][0] = 5
#   [  5,  6, 7]   → matrix[2][0] = 5
#   sum = 12 ✅


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Reset accumulator inside outer loop!
# -----------------------------------------------------------------------------
# Same lesson as Q51 (Armstrong), Q60 (split) — reset INSIDE outer, OUTSIDE inner!
#
#   for col in range(...):
#       col_total = 0          ← reset for each new column!
#       for row in range(...):
#           col_total += ...
#       col_sums.append(col_total)  ← append after inner loop!


# -----------------------------------------------------------------------------
# ✅ FINAL CODE
# -----------------------------------------------------------------------------

list_2d = [
    [2, 4, 5],
    [5, 1, 5],
    [5, 6, 7]
]

row_sum = []
column_sum = []

# ROW SUMS
for lst in list_2d:
    row_total = 0
    for row in lst:
        row_total = row_total + row
    row_sum.append(row_total)

# COLUMN SUMS
for col in range(len(list_2d[0])):      # col index fixed
    col_total = 0
    for row in range(len(list_2d)):     # row index changes
        col_total = col_total + list_2d[row][col]
    column_sum.append(col_total)

print(row_sum)     # [11, 11, 18]
print(column_sum)  # [12, 11, 17]


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Column Sums  |  col=0
# -----------------------------------------------------------------------------
#
#  col=0, col_total=0
#
#  ┌─────┬──────────────────┬───────────┐
#  │ row │  list_2d[row][0] │ col_total │
#  ├─────┼──────────────────┼───────────┤
#  │  0  │  list_2d[0][0]=2 │   0+2=2   │
#  │  1  │  list_2d[1][0]=5 │   2+5=7   │
#  │  2  │  list_2d[2][0]=5 │   7+5=12  │
#  └─────┴──────────────────┴───────────┘
#  column_sum.append(12) ✅
#
#  col=1, col_total=0
#  ┌─────┬──────────────────┬───────────┐
#  │ row │  list_2d[row][1] │ col_total │
#  ├─────┼──────────────────┼───────────┤
#  │  0  │  list_2d[0][1]=4 │   0+4=4   │
#  │  1  │  list_2d[1][1]=1 │   4+1=5   │
#  │  2  │  list_2d[2][1]=6 │   5+6=11  │
#  └─────┴──────────────────┴───────────┘
#  column_sum.append(11) ✅


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. len(matrix) = rows | len(matrix[0]) = columns
# 2. Row sums → loop directly over elements
# 3. Column sums → loop using indices, matrix[row][col], col fixed row changes
# 4. Reset accumulator INSIDE outer loop, OUTSIDE inner loop — same pattern always!
# 5. Append AFTER inner loop — when total is fully accumulated


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Matrix Access Pattern
# -----------------------------------------------------------------------------
#   # Row access (direct):
#   for row in matrix:
#       for element in row:
#
#   # Column access (index):
#   for col in range(len(matrix[0])):
#       for row in range(len(matrix)):
#           matrix[row][col]   ← row changes, col fixed!
#
# This pattern appears in:
#   - Matrix row/col sums
#   - Matrix transpose
#   - Spreadsheet calculations
#   - Image pixel processing (rows and columns of pixels)
