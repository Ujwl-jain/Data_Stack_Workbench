# =============================================================================
# Q56 - Group Scores by Student
# List of (student, subject, score) tuples → {student: [scores]}
# BONUS: Solve when order inside tuple/set is unknown!
# =============================================================================


# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Input:  [('Alice', 'Math', 85), ('Bob', 'Science', 78), ('Alice', 'English', 90)]
# Output: {'Alice': [85, 90], 'Bob': [78]}
#
# Group all scores under each student's name!
# Same student appears multiple times → collect ALL their scores in a list


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — First time vs Repeat pattern (same as Q48!)
# -----------------------------------------------------------------------------
# if student NOT in dict → dict[student] = [score]    ← start new list!
# else                   → dict[student].append(score) ← add to existing!
#
# Difference from Q48 (transactions):
#   Q48 → accumulated numbers  → dict[name] += amount
#   Q56 → collected into list  → dict[student].append(score)


# -----------------------------------------------------------------------------
# ✅ METHOD 1 — Known order (tuple unpacking)
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Create empty dict
# 2. Unpack each tuple directly → student, subject, score
# 3. First time → create new list, repeat → append to existing
# 4. Return dict

def list_to_dict_ordered(list_student):
    result_dict = {}
    for student, subject, score in list_student:   # direct unpacking!
        if student not in result_dict:
            result_dict[student] = [score]          # start new list!
        else:
            result_dict[student].append(score)      # add to existing!
    return result_dict

list_student = [('Alice', 'maths', 85), ('Bob', 'english', 99),
                ('Alice', 'science', 18), ('Bob', 'hindi', 99)]
print(list_to_dict_ordered(list_student))
# Output: {'Alice': [85, 18], 'Bob': [99, 99]}


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — isinstance() for type checking
# -----------------------------------------------------------------------------
# isinstance(value, type) → returns True/False
#
#   isinstance(85, int)       # True  ✅
#   isinstance('alice', int)  # False ✅
#   isinstance('alice', str)  # True  ✅
#
# Cleaner than isdigit() — works on actual Python types!
# Use when you need to check WHAT TYPE a value is


# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Lookup Table pattern
# -----------------------------------------------------------------------------
# When you can't tell two strings apart (name vs subject) →
# check against a KNOWN reference list!
#
#   known_subjects = ['maths', 'english', 'science', ...]
#   if item in known_subjects → it's a subject!
#   else → it must be a name!
#
# This is called a LOOKUP TABLE — one of the most common patterns in programming!
# Used in: spam filters, language detection, data classification


# -----------------------------------------------------------------------------
# ✅ METHOD 2 — Unknown order (isinstance + lookup table)
# -----------------------------------------------------------------------------
# LOGIC:
# 1. Create empty dict and known subjects list
# 2. Outer loop → each tuple/set
# 3. Reset score, student, subject INSIDE outer loop, OUTSIDE inner loop!
# 4. Inner loop → each item in tuple/set
#       if int → score
#       elif not in subjects list → student (name)
#       else → subject
# 5. AFTER inner loop → check student and update dict
# 6. Return dict

def list_to_dict_unordered(list_student):
    result_dict = {}
    list_subject = ['maths', 'english', 'science', 'hindi', 'physics']

    for tup in list_student:
        score = 0       # reset INSIDE outer, OUTSIDE inner!
        student = ''    # all 3 vars reset for each new tuple
        subject = ''

        for item in tup:
            if isinstance(item, int):          # int → always score!
                score = item
            elif item not in list_subject:     # not a subject → name!
                student = item
            else:                              # in subject list → subject!
                subject = item

        # check AFTER inner loop — all 3 vars fully set!
        if student not in result_dict:
            result_dict[student] = [score]
        else:
            result_dict[student].append(score)

    return result_dict

list_student_unordered = [('Ujjwal', 85, 'maths'), ('english', 'nami', 99),
                           ('Ujjwal', 'science', 18), ('matter', 'hindi', 99)]
print(list_to_dict_unordered(list_student_unordered))
# Output: {'Ujjwal': [85, 18], 'nami': [99], 'matter': [99]}


# -----------------------------------------------------------------------------
# 🧪 DRY RUN — Method 2  |  tup = ('Ujjwal', 85, 'maths')
# -----------------------------------------------------------------------------
#
#  score=0, student='', subject=''  ← reset before inner loop
#
#  ┌──────────┬──────────────────────┬───────────────────────────────┐
#  │   item   │     condition        │         result                │
#  ├──────────┼──────────────────────┼───────────────────────────────┤
#  │ 'Ujjwal' │ not in list_subject  │ student = 'Ujjwal'            │
#  │    85    │ isinstance(85, int)  │ score = 85                    │
#  │ 'maths'  │ in list_subject      │ subject = 'maths'             │
#  └──────────┴──────────────────────┴───────────────────────────────┘
#
#  After inner loop:
#  'Ujjwal' not in result_dict → result_dict['Ujjwal'] = [85] ✅


# -----------------------------------------------------------------------------
# 💡 KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. First time → dict[key] = [value]  |  Repeat → dict[key].append(value)
# 2. isinstance(item, int) → cleanest way to check if something is an integer
# 3. Lookup table → check against known list to classify unknown data
# 4. Reset variables INSIDE outer loop, OUTSIDE inner loop — same lesson as
#    temp in Q60, container in Q51, list_cal in Q19!
# 5. Dictionary check AFTER inner loop — only when all variables are fully set!
# 6. Sets are unordered — never rely on index when using sets!


# -----------------------------------------------------------------------------
# 🔁 PATTERN TO REMEMBER — Unknown Structure Pattern
# -----------------------------------------------------------------------------
# When data structure/order is unknown:
#
#   for element in data:
#       # classify each item by TYPE first
#       if isinstance(item, int):    → numeric field
#       elif item in lookup_list:    → known category field
#       else:                        → remaining field (name/id)
#
# This pattern appears in:
#   - Parsing unknown data formats
#   - Schema inference in databases
#   - Data cleaning pipelines
#   - Any "figure out what this is" problem
