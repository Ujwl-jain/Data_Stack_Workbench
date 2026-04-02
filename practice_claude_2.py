'''
PYTHON CODING DRILL — BATCH 2 (60 QUESTIONS)
=============================================
Topics: if-else, slicing, list & comprehension, strings,
        type casting, tuples, dictionaries, loops,
        f-string & docstring, string & list methods,
        FUNCTIONS, SETS, RECURSION
=============================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1. FUNCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q1.  Write a function `greet(name, greeting="Hello")` that uses a default
     argument and returns a greeting string like "Hello, Alice!".

     DONE

Q2.  Write a function `calculator(a, b, op)` that takes two numbers and
     an operator string ("+", "-", "*", "/") and returns the result.

     DONE

Q3.  Write a function `is_divisible(n, divisor=2)` that returns True if
     n is divisible by the divisor, False otherwise. Use a default param.

     DONE

Q4.  Write a function that accepts *args and returns the sum of all
     passed numbers. It should work with any number of arguments.

     DONE

[Medium]
Q5.  Write a function `apply_twice(func, value)` that takes another
     function and a value, applies the function to the value twice,
     and returns the result. (Higher-order function)

Q6.  Write a function `power_factory(exp)` that returns a new function
     which raises any number to the power `exp`. Use closures.
     Example: square = power_factory(2); square(5) → 25

Q7.  Write a function that accepts **kwargs and prints each key-value
     pair in the format "key: value". Then call it with at least 4
     different keyword arguments.

     DONE

Q8.  Write a function `safe_divide(a, b)` that returns the result of
     a / b, but returns None and prints a warning if b is 0.
     Demonstrate calling it with both valid and zero divisor.

     DONE
     
Q9.  Write a lambda function that takes a list of tuples (name, score)
     and returns the list sorted by score in descending order.

[Hard]
Q10. Write a decorator `timer` that measures and prints how long a
     function takes to execute. Apply it to a function that runs a
     loop 1 million times.

Q11. Write a decorator `repeat(n)` that runs the decorated function
     n times. It should accept n as an argument to the decorator itself.

Q12. Write a function `compose(*funcs)` that takes multiple functions
     and returns a new function that applies them all from right to left.
     Example: compose(double, add_one)(3) → double(add_one(3)) → 8


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 2. SETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q13. Given two lists, find the common elements between them using sets.
     Return the result as a sorted list.

Q14. Given a list with duplicates, use a set to return only the unique
     elements as a sorted list.

Q15. Given two sets A and B, return four things: union, intersection,
     difference (A - B), and symmetric difference.

Q16. Write a function that checks if one set is a subset of another.
     Test with at least 3 different pairs of sets.

[Medium]
Q17. Given a sentence, find all unique words using a set (case-
     insensitive). Return them as a sorted list.

Q18. Given two lists of student names (class A and class B), find:
     (a) students in both classes, (b) students only in class A,
     (c) students in either class but not both.

Q19. Write a function that takes a list of lists and returns a set of
     elements that appear in ALL of the sublists.

Q20. Given a list of integers, use sets to find all pairs (a, b) where
     a + b = target. Return unique pairs only (no duplicates like (1,3)
     and (3,1)).

[Hard]
Q21. Given a list of words, group them into sets of anagrams.
     Return a list of sets where each set contains anagram words.
     Example: ['eat','tea','tan','ate','nat','bat'] →
              [{'eat','tea','ate'}, {'tan','nat'}, {'bat'}]

Q22. Implement a simple spell checker using sets. Given a dictionary
     set of valid words and a sentence, return a list of words that
     are NOT in the dictionary (misspelled words).


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 3. RECURSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q23. Write a recursive function to compute the factorial of n.
     factorial(0) = 1, factorial(n) = n * factorial(n-1).

Q24. Write a recursive function to compute the nth Fibonacci number.
     fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2).

Q25. Write a recursive function that computes the sum of all elements
     in a list without using any built-in sum() function.

Q26. Write a recursive function `count_down(n)` that prints numbers
     from n down to 0, then prints "Go!".

[Medium]
Q27. Write a recursive function to reverse a string.
     Do NOT use slicing or any built-in reverse method.

Q28. Write a recursive function to check if a string is a palindrome.
     Return True or False. Do not use slicing.

Q29. Write a recursive function `flatten(lst)` that flattens a deeply
     nested list of lists into a single flat list.
     Example: [1, [2, [3, [4]]]] → [1, 2, 3, 4]

Q30. Write a recursive function to compute x raised to the power n
     (x^n). Implement it efficiently using the rule:
     if n is even: x^n = (x^(n/2))^2
     if n is odd:  x^n = x * x^(n-1)

Q31. Write a recursive function `digit_sum(n)` that returns the sum of
     all digits of a number. Example: digit_sum(1234) → 10.

[Hard]
Q32. Write a recursive function to solve the Tower of Hanoi problem.
     Print each move as "Move disk X from A to C".
     Solve for n disks.

Q33. Write a recursive function `permutations(s)` that returns all
     permutations of a string as a list.
     Example: permutations("abc") → ["abc","acb","bac","bca","cab","cba"]

Q34. Write a recursive function `binary_search(arr, target, low, high)`
     that implements binary search recursively. Return index or -1.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 4. IF-ELSE  (new problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q35. Write a function that takes a character and returns whether it is
     a 'vowel', 'consonant', or 'not a letter'.

     DONE

[Medium]
Q36. Given a list of numbers, classify each as 'small' (< 10),
     'medium' (10–99), or 'large' (100+). Return a list of labels.

     DONE

Q37. Write a function that takes age and returns the life stage:
     'baby' (0-2), 'child' (3-12), 'teen' (13-17),
     'adult' (18-64), 'senior' (65+). Done

     def age_checker(age):
    if age >= 3 and age <= 12:
        return f'You are still a child as your age is {age}'
    elif age >=13 and age<=17:
        return f"You are a teen as your age is {age}"
    elif age>=18 and age<=64:
        return f"Your are an adult, as your age is {age}"
    elif age>=65:
        return f"You are a senior citizen, as your age is {age}"
    else:
        return f"Awwwww!! How cute, you just born 'baby' "

age = float(input("Enter the age: "))
age_result = age_checker(age)
print(age_result)

# enhanced version:

def age_checker(age):
    if age < 0:
        return "Invalid age!"
    elif age <= 2:
        return f"Awww!! How cute, you're just a baby at {age}!"
    elif age <= 12:
        return f"You are still a child, age {age}"
    elif age <= 17:
        return f"You are a teen, age {age}"
    elif age <= 64:
        return f"You are an adult, age {age}"
    else:
        return f"You are a senior citizen, age {age}"

age = float(input("Enter the age: "))
print(age_checker(age))

[Hard]
Q38. Write a function that takes a string representing a date in
     "DD/MM/YYYY" format and validates it: check valid day, month,
     year ranges and whether the day is valid for that specific month
     (account for leap years too). DONE

     def year_check(year):

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def date_checker(dmy):
    list_date = dmy.split('/')
    # since this is confirmed according to the format we can just store the date inside a variable:
    day = int(list_date[0])
    month = int(list_date[1])
    year = int(list_date[2])
    day_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month not in range(1,13):
        return 'Invalid Month'
    else:
        print('Valid Month - continue')
        if year < 1:
            return 'Invalid Year'
        elif year_check(year) is False:
            print('Valid Year - checking leap or not')
            if day < 1 or day > day_list[month]: 
                return 'Invalid Date'
            else:
                print('valid date')
                return 'Valid Date'
        elif year_check(year) is True:
            if year_check(year) and month == 2:
                max_days = 29
            else:
                max_days = day_list[month]
            if day <1 or day > max_days:
                return 'Invalid date'
            else:
                return 'Valid Date'

dmy = input("Enter a year in format DD/MM/YYYY: ")
if len(dmy.split('/')) != 3:
    print(dmy)
    print('invalid date')
else:
    result_date = date_checker(dmy)
    print(result_date)



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 5. STRINGS  (new problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q39. Write a function that takes a sentence and returns the number of
     words, characters (no spaces), and sentences (count periods).

[Medium]
Q40. Write a function that converts a snake_case string to camelCase.
     Example: "hello_world_python" → "helloWorldPython"

Q41. Write a function that takes a string and returns True if all
     brackets are balanced: (), [], {}.
     Example: "{[()]}" → True,  "{[(])}" → False

[Hard]
Q42. Write a function that compresses a string using run-length
     encoding. "aaabbbccddddee" → "a3b3c2d4e2".
     If a character appears once, just write the character: "abc" → "abc"


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 6. LISTS & COMPREHENSION  (new problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q43. Given a list of integers, return two lists: one with positive
     numbers and one with negative numbers, using list comprehension.

[Medium]
Q44. Given a list of sentences, return a list of lists where each inner
     list contains the individual words of that sentence.
     Use list comprehension.

Q45. Given a list of numbers, return a new list replacing every number
     less than 0 with 0 and every number greater than 100 with 100
     (clamping). Use list comprehension.

[Hard]
Q46. Write a function that takes a list of dictionaries (each with keys
     'name' and 'score') and returns a sorted list of names of students
     who scored above the average score.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 7. DICTIONARIES  (new problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q47. Write a function that takes a list of words and returns a
     dictionary of word lengths: {'word': length}.

[Medium]
Q48. Given a list of transactions as dicts with 'name' and 'amount',
     calculate the total amount spent per person.
     Return as a dictionary {name: total}.

Q49. Write a function that takes two dicts and returns a dict of keys
     that are common to both, with a tuple of their values.
     Example: {'a':1,'b':2}, {'b':3,'c':4} → {'b': (2, 3)}

[Hard]
Q50. Write a function that converts a flat dictionary with dot-notation
     keys back into a nested dictionary.
     Example: {'a.b.c': 1, 'a.b.d': 2} → {'a': {'b': {'c':1,'d':2}}}


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 8. LOOPS  (new problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q51. Print the following pattern using loops:
     1
     1 2
     1 2 3
     1 2 3 4
     1 2 3 4 5

[Medium]
Q52. Write a loop-based function that finds the GCD (greatest common
     divisor) of two numbers using the Euclidean algorithm.

Q53. Given a 2D list (matrix), use nested loops to compute the sum of
     each row and each column separately. Return as two lists.

[Hard]
Q54. Write a function using loops that generates Pascal's Triangle up
     to n rows. Return it as a list of lists.
     Row 0: [1]
     Row 1: [1, 1]
     Row 2: [1, 2, 1]


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 9. TUPLES  (new problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q55. Write a function that takes a list of numbers and returns a tuple
     of (min, max, sum, average) of the list.

[Medium]
Q56. Given a list of (student, subject, score) tuples, return a
     dictionary grouping scores by student:
     {'Alice': [85, 90], 'Bob': [78]}

[Hard]
Q57. Write a function that takes a list of coordinate tuples (x, y)
     and returns them sorted first by x, then by y, then returns only
     the unique coordinates (no duplicates).


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 10. TYPE CASTING  (new problems)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q58. Take a list of boolean values and convert them to integers (0 or 1).
     Then compute and return the sum.

[Medium]
Q59. Write a function that reads a string like "10 20 30 40 50",
     splits it by spaces, converts each to int, and returns the
     min, max, and average as a tuple of floats.

[Hard]
Q60. Write a function that takes a mixed list like:
     [1, '2', 3.5, True, '4.2', False, 'seven', None]
     and returns a dict:
     {
       'integers':   [list of ints, excluding bools],
       'floats':     [list of floats],
       'booleans':   [list of bools],
       'strings':    [list of valid numeric strings converted to float],
       'unparseable':[items that couldn't be converted to any number]
     }


=============================================
 SUMMARY — BATCH 2
=============================================
Total     : 60 questions
Easy      : 20
Medium    : 25
Hard      : 15

New Topics: Functions (12Q), Sets (10Q), Recursion (12Q)
Revisited : if-else, strings, lists, dicts,
            loops, tuples, type casting
============================================='''
