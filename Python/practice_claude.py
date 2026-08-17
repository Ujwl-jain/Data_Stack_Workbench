'''
PYTHON CODING DRILL — 60 QUESTIONS
====================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1. IF-ELSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1  [Easy]   Write a function that takes an integer and returns 'positive', 'negative', or 'zero'. 

Q2  [Easy]   Check if a number is even or odd using a single-line if-else expression.

Q3  [Medium] Given three sides of a triangle, determine if it's equilateral, isosceles, or scalene.

Q4  [Medium] Write a grading system: A (90+), B (80-89), C (70-79), D (60-69), F (below 60).

Q5  [Hard]   FizzBuzz: Print numbers 1–100, but 'Fizz' for multiples of 3, 'Buzz' for 5, 'FizzBuzz' for both.

Q6  [Hard]   Given a year, determine if it's a leap year using proper Gregorian rules.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 2. SLICING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q7  [Easy]   Reverse a string using slicing only (no built-in reverse).

Q8  [Easy]   Extract every other character from a string starting from index 0.

Q9  [Medium] Given a list, return the middle third of it using slicing.

Q10 [Medium] Check if a string is a palindrome using slicing (no loops).

Q11 [Medium] Rotate a list to the right by k positions using slicing.

Q12 [Hard]   Given a 2D matrix (list of lists), extract the diagonal elements using slicing concepts.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 3. LIST & LIST COMPREHENSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q13 [Easy]   Create a list of squares of numbers from 1 to 10 using list comprehension.

Q14 [Easy]   Flatten a list of lists into a single list using list comprehension.

Q15 [Easy]   Filter all even numbers from a list using list comprehension.

Q16 [Medium] Given a list of words, return a list of words longer than 5 characters, uppercased.

Q17 [Medium] Remove duplicates from a list while preserving order (no set shortcuts).

Q18 [Medium] Transpose a matrix (list of lists) using list comprehension.

Q19 [Hard]   Generate a multiplication table (1–10) as a 2D list using nested list comprehension.

Q20 [Hard]   Find all prime numbers up to N using list comprehension and a helper function.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 4. STRINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q21 [Easy]   Count vowels in a string without using any built-in count method.

Q22 [Easy]   Reverse words in a sentence (not characters).

Q23 [Medium] Check if two strings are anagrams of each other.

Q24 [Medium] Find the longest word in a sentence using string methods only.

Q25 [Medium] Count frequency of each character in a string and return as a dictionary.

Q26 [Hard]   Implement a Caesar cipher: shift each letter by k positions, preserve case and non-letters.

Q27 [Hard]   Find all substrings of a string that are palindromes and return them sorted by length.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 5. TYPE CASTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q28 [Easy]   Write a safe int converter that returns None instead of raising ValueError.

Q29 [Easy]   Convert a list of string numbers ['1','2','3'] to actual integers using map and int.

Q30 [Medium] Given mixed input (int, float, str), convert all to float and sum them. Handle errors gracefully.

Q31 [Medium] Convert a decimal number to binary, octal, and hexadecimal without using bin/oct/hex.

Q32 [Hard]   Parse a CSV string '1,2.5,hello,True,None' into Python-typed values automatically.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 6. TUPLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q33 [Easy]   Unpack a tuple of (name, age, city) and print each using f-strings.

Q34 [Easy]   Swap two variables using tuple packing/unpacking in a single line.

Q35 [Medium] Sort a list of tuples by the second element, then by first element as tiebreaker.

list_tup = [(1, 3), (2, 1), (4, 1), (3, 2)]

final_list = sorted(list_tup, key=lambda x: (x[1], x[0]))
print(final_list)

Q36 [Medium] Create a named tuple for a 'Student' with fields name, grade, score. Demonstrate usage.
from collections import namedtuple

Student  = namedtuple('Student', ['name','grade','score'])
s1 = Student('Ujjwal', 'A', 95)

print(s1.name) 
print(s1.score) 
print(type(s1))
print(s1[0])  

Q37 [Hard]   Given a list of (item, price) tuples, find the most expensive item without using max().

list_items = [('apple', 30), ('laptop', 80000), ('pen', 10), ('phone', 50000)]

final_list = sorted(list_items, key = lambda x:x[1], reverse = True)
item, price = final_list[0]
print(item,price)

# using for loop
new_item = ''
max_price = 0
for item, price in final_list:
    if price>max_price:
        max_price = price
        new_item = item
    else:
        pass
print(new_item, max_price)
    
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 7. DICTIONARIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q38 [Easy]   Invert a dictionary (swap keys and values). Assume all values are unique.

Q39 [Easy]   Merge two dictionaries. If keys conflict, keep the value from the second dict.

Q40 [Medium] Count word frequency in a sentence and return the top 3 most common words.

Q41 [Medium] Group a list of words by their first letter using a dictionary.

Q42 [Medium] Implement a simple phone book: add, remove, lookup, and list all contacts.

Q43 [Hard]   Flatten a nested dictionary: {'a': {'b': {'c': 1}}} → {'a.b.c': 1}.

Q44 [Hard]   Implement a cache (memoization) using a dictionary to speed up Fibonacci.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 8. LOOPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q45 [Easy]   Print a pattern: right-angled triangle of stars with n rows using nested loops.

Q46 [Easy]   Find the sum of all digits of a number using a while loop.

Q47 [Medium] Implement binary search on a sorted list using a while loop.

Q48 [Medium] Use enumerate and zip together to pair elements from two lists with their index.

Q49 [Medium] Write a number guessing game loop: keep guessing until correct, count attempts.

Q50 [Hard]   Implement bubble sort using nested loops and count the number of swaps made.

Q51 [Hard]   Find all Armstrong numbers between 1 and 1000 using loops (e.g. 153 = 1³+5³+3³).


━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 9. F-STRING & DOCSTRING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q52 [Easy]   Format a person's info with f-string: name, age, and salary rounded to 2 decimal places.
age = 24
Salary = 4500.45146

print(f"My name is {name}, My age is {age}, and my salary is {Salary:.2f}")

Q53 [Easy]   Write a function with a proper docstring that converts Celsius to Fahrenheit.

def doc_string(c):
    '''
    Here the goal is to convert the celsius to Fahrenheit
    basically we can convert it using below formula
    this function will return the F to the caller
    '''
    F = (c * 9/5) + 32
    return F
f = doc_string(14)
print(f)

# enhanced -
def celsius_to_fahrenheit(c):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        c (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (c * 9/5) + 32
    return fahrenheit


f = celsius_to_fahrenheit(14)
print(f)

Q54 [Medium] Print a formatted table of products (name, qty, price) using f-strings with alignment.

products = [
    ('Apple',  10000, 'Rs 10/piece'),
    ('Laptop', 5,     'Rs 80000'),
    ('Pen',    500,   'Rs 10/piece'),
]

print(f"{'Name':<12} {'Qty':<10} {'Price':<12}")
print("-" * 45)
for name, qty, price in products:    # tuple unpacking!
    print(f"{name:<12} {qty:<10} {price:<12}")


Q55 [Medium] Use f-string to display a progress bar: '████░░░░ 50%' dynamically based on a value.

Q56 [Hard]   Write a class with a proper __doc__ and every method having docstrings. Access them via __doc__.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 10. STRING & LIST METHODS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q57 [Easy]   Use strip, lstrip, rstrip, upper, lower, title, capitalize on the same string and print results.

Q58 [Easy]   Use split, join, replace, find, count, startswith, endswith on a paragraph string.

Q59 [Medium] Use list methods: append, extend, insert, remove, pop, sort, reverse, index, count.

Q60 [Hard]   Implement your own version of str.split() and str.join() without using the built-in methods.


====================================
 SUMMARY
====================================
Total Questions : 60
Easy            : 22
Medium          : 26
Hard            : 12

Topics Covered  : if-else, slicing, list & comprehension,
                  strings, type casting, tuples, dictionaries,
                  loops, f-string & docstring, string & list methods
====================================
'''
