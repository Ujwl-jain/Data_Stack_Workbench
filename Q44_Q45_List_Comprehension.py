# =============================================================================
# Q44 & Q45 - List Comprehension Problems
# Q44: Sentences → list of word lists
# Q45: Clamp numbers between 0 and 100
# =============================================================================


# =============================================================================
# Q44 - List of Sentences → List of Word Lists
# =============================================================================

# Input:  ['i am', 'ujjwal jain i am', 'you are not ujjwal']
# Output: [['i', 'am'], ['ujjwal', 'jain', 'i', 'am'], ['you', 'are', 'not', 'ujjwal']]

list_of_sentence = ['i am', 'ujjwal jain i am', 'you are not ujjwal']

# Normal loop:
nested_list = []
for sen in list_of_sentence:
    nested_list.append(sen.split())
print(nested_list)

# List comprehension:
nested_list_comp = [word.split() for word in list_of_sentence]
print(nested_list_comp)

# NOTE: split() vs split(' ')
#   split(' ')  → splits by space only, struggles with double spaces
#   split()     → splits by ANY whitespace, handles edge cases! ✅


# =============================================================================
# Q45 - Clamp Numbers Between 0 and 100
# =============================================================================

# Input:  [-1, -4, 144, 451, 6, -8, 2, 300, 8]
# Output: [0, 0, 100, 100, 6, 0, 2, 100, 8]

list_number = [-1, -4, 144, 451, 6, -8, 2, 300, 8]

# Normal loop:
updated_list = []
for num in list_number:
    if num < 0:
        updated_list.append(0)
    elif num > 100:
        updated_list.append(100)
    else:
        updated_list.append(num)
print(updated_list)

# List comprehension (ternary operator):
updated_list_comp = [0 if num < 0 else 100 if num > 100 else num for num in list_number]
print(updated_list_comp)


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT — Ternary in Comprehension
# -----------------------------------------------------------------------------
# Normal if/elif/else CANNOT go inside comprehension!
# Use TERNARY operator instead:
#
#   value_if_true if condition else value_if_false
#
# Single condition:
#   [0 if num < 0 else num  for num in list]
#
# Double condition (nested ternary):
#   [0 if num < 0 else 100 if num > 100 else num  for num in list]
#    ↑ first check        ↑ second check  ↑ default
#
# RULE — expression BEFORE for, loop ALWAYS at end:
#   TRANSFORMING → ternary before for   → [expression    for x in list]
#   FILTERING    → condition after for  → [x for x in list  if condition]


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Ternary Comprehension
# -----------------------------------------------------------------------------
# [0 if num < 0 else 100 if num > 100 else num for num in list_number]
#
# Read as:
#   "For each num → give me 0 if negative, 100 if over 100, else keep num"
#
# ┌─────┬───────────┬──────────────────────────────┬────────┐
# │ num │ condition │         which branch?         │ result │
# ├─────┼───────────┼──────────────────────────────┼────────┤
# │ -1  │  -1 < 0   │ first condition true → 0      │   0    │
# │ -4  │  -4 < 0   │ first condition true → 0      │   0    │
# │ 144 │  144 > 100│ second condition true → 100   │  100   │
# │ 451 │  451 > 100│ second condition true → 100   │  100   │
# │  6  │  0≤6≤100  │ both false → keep num         │   6    │
# │ -8  │  -8 < 0   │ first condition true → 0      │   0    │
# │  2  │  0≤2≤100  │ both false → keep num         │   2    │
# │ 300 │  300 > 100│ second condition true → 100   │  100   │
# │  8  │  0≤8≤100  │ both false → keep num         │   8    │
# └─────┴───────────┴──────────────────────────────┴────────┘
#
# ✅ Output: [0, 0, 100, 100, 6, 0, 2, 100, 8]


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Ternary = inline if/else → value_if_true if condition else value_if_false
# 2. Nest two ternaries for two conditions
# 3. Expression ALWAYS comes before for in comprehension
# 4. Transforming → ternary before for | Filtering → if after for
# 5. split() without argument is cleaner than split(' ')
