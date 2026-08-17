# ============================================================
#                   LAMBDA FUNCTIONS
# ============================================================
# A lambda is a small ANONYMOUS function -- a function without a name.
# Used when you need a simple one-line function for a short time.
# Lambda functions can take any number of arguments but only ONE expression.
# The expression is automatically returned -- no 'return' keyword needed.
#
# SYNTAX:
#   lambda parameters : expression
#
# WHEN TO USE:
# - When the function logic is simple and used only once or twice
# - When passing a function as an argument to another function
# - To avoid writing a full def block for a tiny operation
# ============================================================


# ------------------------------------------------------------
# Basic Lambda -- compared to a regular function
# ------------------------------------------------------------

# regular function
def add(a, b):
    return a + b

print(add(3, 5))        # 8

# same thing as a lambda
add_lambda = lambda a, b: a + b
print(add_lambda(3, 5)) # 8

# lambda with a single argument
square = lambda x: x ** 2
print(square(4))        # 16

# lambda with no arguments
greet = lambda: "hello ujjwal"
print(greet())          # hello ujjwal


# ------------------------------------------------------------
# Lambda with conditional expression
# ------------------------------------------------------------
# You can use a one-line if-else inside a lambda (ternary style).
# SYNTAX: lambda x: value_if_true if condition else value_if_false

is_even = lambda x: "even" if x % 2 == 0 else "odd"
print(is_even(4))       # even
print(is_even(7))       # odd

greater = lambda a, b: a if a > b else b
print(greater(10, 20))  # 20


# ------------------------------------------------------------
# Lambda with built-in functions -- the real power
# ------------------------------------------------------------
# Lambda is most useful when passed as an argument to functions
# like sorted(), map(), filter(), and max().


# sorted() with lambda -- sort by a custom rule
students = [('ujjwal', 85), ('ram', 92), ('shyam', 78)]

sorted_by_marks = sorted(students, key=lambda student: student[1])
print(sorted_by_marks)
# [('shyam', 78), ('ujjwal', 85), ('ram', 92)]  <- ascending by marks

sorted_desc = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_desc)
# [('ram', 92), ('ujjwal', 85), ('shyam', 78)]  <- descending by marks


# map() with lambda -- apply a function to every item in a list
# SYNTAX: map(function, iterable) -- returns a map object, convert to list
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)          # [1, 4, 9, 16, 25]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)          # [2, 4, 6, 8, 10]


# filter() with lambda -- keep only items where condition is True
# SYNTAX: filter(function, iterable) -- returns a filter object, convert to list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)            # [2, 4, 6, 8, 10]

greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(greater_than_5)   # [6, 7, 8, 9, 10]


# max() / min() with lambda -- find max/min by a custom rule
students = [('ujjwal', 85), ('ram', 92), ('shyam', 78)]

top_student = max(students, key=lambda student: student[1])
print(top_student)      # ('ram', 92)


# ============================================================
#                    QUICK REFERENCE SUMMARY
# ============================================================
#
#  Feature              Regular Function (def)     Lambda Function
#  ──────────────────────────────────────────────────────────────────
#  Has a name           Yes                        No (anonymous)
#  Number of lines      Multiple                   One line only
#  return keyword       Required                   Not needed (auto)
#  Number of args       Any                        Any
#  Expressions          Multiple                   ONE only
#  Can have loops       Yes                        No
#  Best used for        Complex reusable logic     Short one-off logic
#
#  Common uses:
#  ──────────────────────────────────────────────────────────────────
#  sorted(list, key=lambda x: x[1])     sort by second element
#  map(lambda x: x*2, list)             apply operation to all items
#  filter(lambda x: x>5, list)          keep items matching condition
#  max(list, key=lambda x: x[1])        find max by custom rule
#
#  Rules:
#  ──────────────────────────────────────────────────────────────────
#  1. Lambda can only have ONE expression -- no multi-line logic
#  2. No loops, no if-elif-else blocks (only ternary if-else)
#  3. If logic is complex, always prefer a regular def function
#  4. map() and filter() return objects -- wrap in list() to see output
#
# ============================================================
