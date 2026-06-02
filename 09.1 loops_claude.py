# ============================================================
#                      LOOPS IN PYTHON
# ============================================================
# A loop is a way to execute a block of code REPEATEDLY.
# Python has 2 built-in loop types:
#   1. for loop   → iterate over a sequence a known number of times
#   2. while loop → repeat as long as a condition is True
# NOTE: Python does NOT have a do-while loop (unlike C/Java),
#       but it can be simulated using while + break (shown below).
# ============================================================


# ============================================================
#                        FOR LOOP
# ============================================================
# Used to iterate over any ITERABLE object.
# Iterables: list, tuple, dictionary, set, string, range
# SYNTAX:
#   for variable in iterable:
#       # code block
# The loop runs once for each item in the iterable.
# ============================================================

# ------------------------------------------------------------
# Iterating over a STRING
# ------------------------------------------------------------
# Each character in the string is visited one by one.

a = 'ujjwal'
for i in a:
    print(i)
    if i == 'w':
        print("found 'w' → true")

# Output:
# u
# j
# j
# w
# found 'w' → true
# a
# l


# ------------------------------------------------------------
# Iterating over a LIST
# ------------------------------------------------------------
# Each element in the list is visited one by one.

l = [1, 2, 3, 4]
for i in l:
    print(i)        # 1, 2, 3, 4

# you can also use enumerate() to get index + value together
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
# Output:
# 0 apple
# 1 banana
# 2 mango


# ------------------------------------------------------------
# Iterating over a DICTIONARY
# ------------------------------------------------------------
# By default, iterating gives you the KEYS only.

person = {'name': 'ujjwal', 'age': 21, 'city': 'pune'}

for key in person:
    print(key)                      # prints keys only

for key, value in person.items():   # .items() gives key-value pairs
    print(key, "→", value)

# Output:
# name → ujjwal
# age → 21
# city → pune


# ============================================================
#                     range() FUNCTION
# ============================================================
# range() generates a sequence of numbers — useful when you
# want to loop a specific number of times.
# SYNTAX: range(start, stop, step)
#   start → where to begin (default: 0)
#   stop  → where to end   (EXCLUSIVE — stops at stop-1)
#   step  → how much to increment/decrement each time (default: 1)
# ============================================================

# range(stop) — starts at 0, stops at stop-1
for i in range(5):          # same as range(0, 5)
    print(i)                # 0, 1, 2, 3, 4   ← 5 is NOT included

# range(start, stop) — custom start
for i in range(1, 10):
    print(i)                # 1, 2, 3, 4, 5, 6, 7, 8, 9   ← 10 is NOT included

# range(start, stop, step) — skip numbers
for i in range(1, 10, 2):
    print(i)                # 1, 3, 5, 7, 9   ← jumps by 2 each time

# range with NEGATIVE step — count backwards
for i in range(10, 0, -1):
    print(i)                # 10, 9, 8, ..., 1   ← countdown

# range() with len() — classic way to loop with index
names = ['ujjwal', 'ram', 'shyam']
for i in range(len(names)):
    print(i, names[i])
# Output:
# 0 ujjwal
# 1 ram
# 2 shyam

# ⚠️ NOTE: range() itself is NOT a list — it's a range object.
# Convert to list if you need the values stored:
print(list(range(1, 6)))    # [1, 2, 3, 4, 5]


# ============================================================
#                       WHILE LOOP
# ============================================================
# Executes the block AS LONG AS the condition remains True.
# As soon as the condition becomes False → loop exits.
# SYNTAX:
#   while condition:
#       # code block
# ⚠️  ALWAYS make sure the condition eventually becomes False,
#     otherwise you get an INFINITE LOOP!
# ============================================================

# Basic while loop with a counter
i = 0
while i <= 3:
    print(i)        # 0, 1, 2, 3
    i = i + 1       # ← increment: without this → infinite loop!
print("done with the loop")

# Shorthand increment (more Pythonic)
i = 0
while i <= 3:
    print(i)
    i += 1          # same as i = i + 1


# ------------------------------------------------------------
# While loop with USER INPUT
# ------------------------------------------------------------
# while loop is ideal when you don't know how many times
# the loop should run — e.g. based on user input.

i = int(input("enter a number: "))     # initialize before loop
while i <= 38:                         # keep looping until condition is False
    i = int(input("enter a number: "))
    print(i)
print("done with the loop")


# ------------------------------------------------------------
# Countdown using while loop
# ------------------------------------------------------------
count = 7
while count > 0:
    print(count)    # 7, 6, 5, 4, 3, 2, 1
    count -= 1      # decrement: count = count - 1
# ⚠️  if you used count += 1 here, count would keep growing
#     and the condition count > 0 would NEVER become False → infinite loop


# ------------------------------------------------------------
# else with while loop
# ------------------------------------------------------------
# The else block runs ONCE when the while condition becomes False.
# It does NOT run if the loop was exited using break.

count = 3
while count > 0:
    print(count)    # 3, 2, 1
    count -= 1
else:
    print("condition became False → else block runs now")
# Output: 3, 2, 1, condition became False → else block runs now

# else does NOT run when break is used:
count = 3
while count > 0:
    print(count)
    if count == 2:
        break       # exits loop early
    count -= 1
else:
    print("this will NOT print because loop was broken")


# ------------------------------------------------------------
# Simulating do-while loop in Python
# ------------------------------------------------------------
# Python has no do-while, but you can simulate it like this.
# A do-while runs the body AT LEAST ONCE before checking condition.

i = 10
while True:
    print(i)        # runs at least once even if condition is False
    i += 1
    if i >= 10:     # condition checked AFTER body runs
        break


# ============================================================
#                    BREAK AND CONTINUE
# ============================================================


# ------------------------------------------------------------
# break
# ------------------------------------------------------------
# Immediately EXITS the loop it is inside.
# Code after the loop continues to run.
# Think of it as: "loop ko chod ke nikal jao" (exit the loop)

for i in range(1, 12):
    if i == 9:
        break               # stops the loop entirely when i is 9
    print(5 * i)
print("loop exited after break at i=9")

# Output: 5, 10, 15, 20, 25, 30, 35, 40
# (9th iteration never prints — loop stops before it)

# break in while loop:
x = 0
while True:                 # infinite loop
    if x == 5:
        break               # only way out
    print(x)
    x += 1
# Output: 0, 1, 2, 3, 4


# ------------------------------------------------------------
# continue
# ------------------------------------------------------------
# SKIPS the rest of the current iteration and moves to the NEXT one.
# The loop does NOT exit — it just skips that one round.
# Think of it as: "is iteration ko chod ke agle pe jao" (skip this round)

for i in range(1, 12):
    if i == 9:
        print("skipping iteration 9")
        continue            # skips 9th iteration, continues from 10
    print(5 * i)
print("loop finished — iteration 9 was skipped")

# Output: 5, 10, 15, 20, 25, 30, 35, 40, skipping iteration 9, 50, 55

# continue in while loop:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue            # skip printing 3
    print(i)
# Output: 1, 2, 4, 5, 6   (3 is skipped)


# ------------------------------------------------------------
# Nested Loops
# ------------------------------------------------------------
# A loop inside another loop.
# Inner loop completes ALL its iterations for EACH outer iteration.

for i in range(1, 4):           # outer loop: 3 times
    for j in range(1, 4):       # inner loop: 3 times each
        print(i, j)

# Output:
# 1 1 | 1 2 | 1 3
# 2 1 | 2 2 | 2 3
# 3 1 | 3 2 | 3 3

# classic example — multiplication table:
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end='\t')  # end='\t' prints tab instead of newline
    print()                     # newline after each row


# ============================================================
#                    QUICK REFERENCE SUMMARY
# ============================================================
#
#  Concept             Use When
#  ────────────────────────────────────────────────────────────────
#  for loop            You know how many times to iterate
#  while loop          You loop until a condition changes
#  range(n)            Loop n times (0 to n-1)
#  range(a, b)         Loop from a to b-1
#  range(a, b, step)   Loop with custom step (can go backwards)
#  enumerate()         Need index + value while iterating
#  break               Exit the loop immediately
#  continue            Skip current iteration, go to next
#  else (on loop)      Run once when loop finishes normally (no break)
#  nested loop         Loop inside a loop (e.g. matrix, tables)
#
# ────────────────────────────────────────────────────────────────
#  ⚠️  COMMON MISTAKES
#  ────────────────────────────────────────────────────────────────
#  1. Forgetting to increment in while → infinite loop
#  2. range(5) gives 0-4, NOT 0-5  (stop is always exclusive)
#  3. Modifying a list while iterating over it → unexpected behavior
#  4. break inside nested loop only exits the INNER loop
#  5. else on loop runs only if loop was NOT broken with break
#
# ============================================================
