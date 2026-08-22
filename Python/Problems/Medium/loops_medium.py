# =============================================================================
# Q1 Binary Search — Implement on a sorted list using a while loop
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
list_bin = [2,4,1,5,56,12.59,13]
list_bin.sort()

a = int(input("Enter the number to find: "))
try:
    if a not in list_bin:
        raise ValueError("Item not found")
    
    start = 0
    end = len(list_bin) - 1

    while start<=end:
        mid = (start + end) // 2
        if list_bin[mid] == a:
            print(f"Number is found at indexing: {mid}")
            break
        elif list_bin[mid] < a:
            start = mid+1
        elif list_bin[mid] > a:
            end = mid - 1

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
# PATTERN TO REMEMBER — Binary Search Pattern
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


# ----------------------------------------------------------------------------------------------------
# Q2. Use enumerate and zip together to pair elements from two lists with their index.


# ---------------------------------------------------------------------------------
# =============================================================================
# Q3. Number Guessing Game
# Keep guessing until correct, count attempts
# =============================================================================
 
 
# -----------------------------------------------------------------------------
# 📖 UNDERSTANDING THE QUESTION
# -----------------------------------------------------------------------------
# Build a number guessing game where:
#   - Computer picks a RANDOM number between 1 and 100
#   - User keeps GUESSING until they get it right
#   - Program tells user if guess is TOO HIGH or TOO LOW
#   - Program counts and shows HOW MANY ATTEMPTS it took
#
# Example run:
#   Guess the Number: 50  → Number is lower, guess again
#   Guess the Number: 25  → Number is higher, guess again
#   Guess the Number: 37  → Number is lower, guess again
#   Guess the Number: 31  → You guessed correct in 4 attempts!
 
 
# -----------------------------------------------------------------------------
# 🧠 LOGIC (Plain English — Think Before You Code)
# -----------------------------------------------------------------------------
# 1. Import random library
# 2. Generate random number using random.randint(1, 100) → STORE it in variable!
# 3. Set attempt counter to 0
# 4. while True → loop runs forever until user guesses correctly
# 5. Take user input → convert to int
# 6. Increment counter by 1 (every guess = one attempt, regardless of result)
# 7. If guess == number → print correct + attempts → break
# 8. If guess > number → print too low (number is lower than guess)
# 9. If guess < number → print too high (number is higher than guess)
 
 
# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 1 — import random
# -----------------------------------------------------------------------------
# Python has BUILT-IN LIBRARIES — pre-written code for common tasks
# so you don't have to build from scratch!
#
# random handles anything related to randomness:
#   random.randint(1, 100)  → random integer between 1 and 100 (inclusive)
#   random.choice([1,2,3])  → random item from a list
#   random.shuffle(list)    → shuffles a list in place
#
# You import it because Python only loads what you ask for — keeps things lightweight!
# Think of it like a TOOLBOX — grab it only when needed 🔧
#
# ALWAYS store the result:
#   random.randint(1, 100)        # ❌ generates but throws away!
#   num = random.randint(1, 100)  # ✅ stored and reusable!
 
 
# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 2 — while True vs while condition
# -----------------------------------------------------------------------------
# while True runs FOREVER until a break is hit
# Perfect when you don't know how many iterations you need!
#
# while True:          # run forever
#     ...
#     if correct:
#         break        # only exit when user guesses correctly
#
# vs binary search:
# while start <= end:  # run until search space exhausted
#
# Rule of thumb:
#   → Know the end condition upfront?  → use while condition
#   → End condition is inside the loop? → use while True + break
 
 
# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 3 — Counter placement matters!
# -----------------------------------------------------------------------------
# ❌ WRONG — repetitive, easy to miss a case:
#   if num == a:
#       attempt_count += 1
#   elif num < a:
#       attempt_count += 1
#   elif num > a:
#       attempt_count += 1
#
# ✅ CORRECT — increment ONCE at top of loop, covers all cases:
#   while True:
#       a = int(input(...))
#       attempt_count += 1    # always counts, no matter what!
#       if ...
#
# Every guess = one attempt regardless of result → count before conditions!
 
 
# -----------------------------------------------------------------------------
# 🔑 KEY CONCEPT 4 — count++ doesn't exist in Python!
# -----------------------------------------------------------------------------
# Java/C:  count++    ❌ SyntaxError in Python
# Python:  count += 1 ✅ always use this!
 
 
# -----------------------------------------------------------------------------
# FINAL CODE
# -----------------------------------------------------------------------------
import random

num = random.randint(1,100)


attempt_count = 0
try:
    while True:
        a = int(input("Guess the Number: "))
        attempt_count +=1
        if num == a:
            print(f"You guess correct: {attempt_count}")
            break
        elif num < a:
            print("Number is lower guess again")
        elif num > a:
            print("Number is higher guess again")

except:
    print("Something went wrong")

# -----------------------------------------------------------------------------
# DRY RUN  |  num = 37  (random picked 37)
# -----------------------------------------------------------------------------
#
#  attempt_count = 0
#
#  ┌─────────┬───────┬──────────────┬────────────────────────────┬─────────┐
#  │ attempt │   a   │  condition   │         output             │  count  │
#  ├─────────┼───────┼──────────────┼────────────────────────────┼─────────┤
#  │    1    │  50   │  37 < 50     │ "Number is lower..."       │    1    │
#  │    2    │  25   │  37 > 25     │ "Number is higher..."      │    2    │
#  │    3    │  40   │  37 < 40     │ "Number is lower..."       │    3    │
#  │    4    │  37   │  37 == 37    │ "You guessed correct in    │    4    │
#  │         │       │              │  4 attempts!" → break      │         │
#  └─────────┴───────┴──────────────┴────────────────────────────┴─────────┘
 
 
# -----------------------------------------------------------------------------
# KEY TAKEAWAYS
# -----------------------------------------------------------------------------
# 1. Always STORE the result of random.randint() in a variable
# 2. random is the LIBRARY — num is the actual number!
# 3. while True + break = run until condition inside loop is met
# 4. Place counter BEFORE conditions — counts every attempt once cleanly
# 5. count += 1 is Python's way — no ++ like Java/C!
# 6. try/except catches invalid input (letters instead of numbers)
 
 
# -----------------------------------------------------------------------------
# PATTERN TO REMEMBER — Game Loop Pattern
# -----------------------------------------------------------------------------
# Whenever you need to keep doing something until a condition is met:
#
#   setup = initial_value
#   counter = 0
#
#   while True:
#       user_input = input(...)
#       counter += 1              # count at top!
#
#       if correct_condition:
#           print(f"Done in {counter} attempts!")
#           break
#       elif condition_a:
#           print("hint a")
#       elif condition_b:
#           print("hint b")
#
# This pattern appears in:
#   - Guessing games
#   - Login attempt systems
#   - Retry mechanisms
#   - Any "keep trying until success" scenario
# ----------------------------------------------------------------------------------------------------


# Q4.  Write a loop-based function that finds the GCD (greatest common
#      divisor) of two numbers using the Euclidean algorithm.

def GCD(a,b):
    while b!= 0:
        a,b = b, a%b
    return a

result = GCD(48,18)
print(result)

# Q5.  Given a 2D list (matrix), use nested loops to compute the sum of
#      each row and each column separately. Return as two lists.

'''
Understanding
2d list = [
[2,4,5],
[5,1,5],
[5,6,7]
]


requriement -
new list containing sum of each row - [sum of 2+4+5,sum of 5+1+5, sum of 5+6+7]
new list containing sum if each column - [sum of 2+5+5, sum of 4+1+6, sum of 5+5+7]

nested loop will be used to access the elements in list of list
first loop will access the list in the list 

create 2 empty list 
row_sum =[]
column_sum []

next loop for element in list of list(): where addition will happen between the sum and appened in the particular empty list
this is easyly done for rows

let me think of columns
'''

list_2d = [
[2,4,5],
[5,1,5],
[5,6,7]
]
row_sum = []
column_sum = []
for lst in list_2d:
    row_total = 0
    for row in lst:
        row_total = row_total+row

    row_sum.append(row_total)  

for col in range(len(list_2d[0])):
    col_total = 0
    for row in range(len(list_2d)):
        col_total = col_total + list_2d[row][col]
    column_sum.append(col_total) 
print(row_sum)
print(column_sum)

# -------------------------------------------------------
# Q13. Write a function using nested loops that prints a diamond pattern
#      of stars for a given odd number n.
#      Example n=5:
#        *
#       ***
#      *****
#       ***
#        *

def pattern(n):
    '''
    # For n=5:
        #   *       ← 2 spaces, 1 star
        #  ***      ← 1 space,  3 stars
        # *****     ← 0 spaces, 5 stars  ← CENTER (widest row!)
        #  ***      ← 1 space,  3 stars
        #   *       ← 2 spaces, 1 star
    
    Dry run

    n =5
    n//2 = 2.5 -> 2

    Top half range(0,3) = 0,1,2
    i=0 → spaces = 2-0 = 2 → stars = 2*0+1 = 1 → "  *"
    i=1 → spaces = 2-1 = 1 → stars = 2*1+1 = 3 → " ***"
    i=2 → spaces = 2-2 = 0 → stars = 2*2+1 = 5 → "*****"

    BOTTOM HALF — range(1, -1, -1) → i = 1, 0

    i=1 → spaces = 2-1 = 1 → stars = 2*1+1 = 3 → " ***"
    i=0 → spaces = 2-0 = 2 → stars = 2*0+1 = 1 → "  *"

    '''
    # top half including middle
    for i in range(n//2 + 1):
        spaces = ' ' * (n//2 - i)
        stars  = '*' * (2*i + 1)
        print(spaces + stars)

    # bottom half (reverse of top, skip middle)
    for i in range(n//2 - 1, -1, -1):
        spaces = ' ' * (n//2 - i)
        stars  = '*' * (2*i + 1)
        print(spaces + stars)

pattern(5)
