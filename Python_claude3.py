'''
PYTHON CODING DRILL — BATCH 3 (126 QUESTIONS)
==============================================
14 Topics · 3 Easy + 3 Medium + 3 Hard each
Mixed concepts: local/global vars, lambda,
                importing modules, if __name__
==============================================


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1. IF-ELSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]- Done
Q1.  Write a function that takes a username (string) and password
     (string). If username is "admin" and password is "1234", return
     "Access granted", else return "Access denied".

Q2.  Write a function that takes a number and returns "fizz" if
     divisible by 3, "buzz" if by 5, "fizzbuzz" if by both, else
     returns the number itself. Use a lambda to call it on a list.

Q3.  Import the `math` module. Write a function that takes a number
     and returns "perfect square" if its square root is a whole number,
     else "not a perfect square". Use math.sqrt() inside.

[Medium]
Q4.  Write a function `bmi_category(weight_kg, height_m)` that
     calculates BMI and returns the category:
     Underweight (< 18.5), Normal (18.5–24.9),
     Overweight (25–29.9), Obese (30+).
     Use a local variable to store the computed BMI.

Q5.  Write a function that takes three numbers and returns them sorted
     as a tuple (min, mid, max) using only if-elif-else — no sort().

Q6.  Write a program with if __name__ == "__main__" that:
     - defines a function `classify_temp(t)` returning
       "cold" (<15), "warm" (15–30), "hot" (>30)
     - calls it with 3 different values and prints results
       only when run directly.

[Hard]
Q7.  Write a function `validate_password(pwd)` that returns a list of
     failed rules. Rules: min 8 chars, at least one uppercase, one
     lowercase, one digit, one special character (!@#$%^&*).
     Return empty list if all rules pass.

Q8.  Write a function that takes a Roman numeral string (up to 'M',
     'D', 'C', 'L', 'X', 'V', 'I') and converts it to an integer.
     Use if-else logic for subtractive notation (IV=4, IX=9 etc).

Q9.  Write a function `tax_calculator(income)` that applies
     progressive tax brackets:
     0–250000: 0%, 250001–500000: 5%, 500001–1000000: 20%,
     above 1000000: 30%.
     Use local variables for each bracket's tax amount.
     Return the total tax and effective tax rate as a tuple.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 2. LOOPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q10. Use a for loop with enumerate() to print each item in a list with
     its index starting from 1 (not 0).
     Example: 1. apple  2. banana  3. cherry

Q11. Write a loop that reads a list of numbers and uses a lambda with
     filter() to keep only numbers greater than the list's average.
     Print the filtered list.

Q12. Use a while loop to build a simple ATM simulation:
     Start with balance = 5000. Keep asking (simulate with a list of
     withdrawal amounts) until balance < 500 or list is exhausted.
     Print balance after each withdrawal.

[Medium]
Q13. Write a function using nested loops that prints a diamond pattern
     of stars for a given odd number n.
     Example n=5:
       *
      ***
     *****
      ***
       *

Q14. Use a for loop with zip() to iterate two lists simultaneously —
     one of student names and one of scores — and print:
     "PASS" if score >= 40, "FAIL" otherwise.
     Use a lambda inside to determine pass/fail.

Q15. Write a loop-based function that finds all pairs of numbers in a
     list whose product equals a given target. Use a global variable
     to count how many such pairs were found. Return the pairs.

[Hard]
Q16. Write a function that uses loops to implement the Sieve of
     Eratosthenes to find all primes up to n.
     Return the list of primes.

Q17. Write a function using loops that takes a 2D matrix and performs
     clockwise 90-degree rotation. Return the rotated matrix.
     Do not use zip or any shortcuts — use pure loop logic.

Q18. Write a number-to-words converter using loops and a dictionary
     mapping. Convert numbers from 0 to 99 into their English word
     form. Example: 42 → "forty two", 15 → "fifteen".


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 3. STRINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy] - Done
Q19. Write a function that takes a sentence and uses a lambda to
     capitalize the first letter of every word that has more than
     3 characters. Leave shorter words unchanged.

Q20. Import the `string` module. Write a function that removes all
     punctuation from a given string using string.punctuation.

Q21. Write a function `mask_email(email)` that returns the email
     with all characters before '@' replaced by '*' except the
     first and last character.
     Example: "ujjwal@gmail.com" → "u*****l@gmail.com"

[Medium]
Q22. Write a function that finds the longest common prefix among a
     list of strings. If no common prefix exists, return "".
     Example: ["flower","flow","flight"] → "fl"

Q23. Write a function `title_case_smart(sentence)` that converts a
     sentence to title case but keeps small words (a, an, the, in,
     on, of, and, or, but) lowercase unless they are the first word.
     Example: "the lord of the rings" → "The Lord of the Rings"

Q24. Write a function that checks if a string is a valid Python
     identifier (without using str.isidentifier()). Rules: starts with
     letter or underscore, rest are letters/digits/underscores, not
     a Python keyword. Import `keyword` module to check keywords.

[Hard]
Q25. Write a function `text_statistics(text)` that returns a dict with:
     word_count, unique_words, avg_word_length, most_common_word,
     longest_word, sentence_count (split by . ? !).
     Use local variables for intermediate calculations.

Q26. Write a function that takes a string and finds all words that
     appear more than once. Return them sorted by frequency (highest
     first), then alphabetically for ties. Case-insensitive.

Q27. Write a Morse code encoder: given a sentence, convert it to
     Morse code using a dictionary mapping. Separate letters with
     single space and words with ' / '.
     Example: "SOS" → "... --- ..."


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 4. LISTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q28. Write a function that takes a list and uses a lambda with sorted()
     to sort it by absolute value.
     Example: [-5, 2, -1, 4] → [-1, 2, 4, -5]

Q29. Use list comprehension with a local variable `threshold = 50` to
     filter a list of scores — keep scores above threshold and double
     them.

Q30. Write a function using map() and a lambda that takes a list of
     temperatures in Celsius and returns them converted to Fahrenheit.

[Medium]
Q31. Write a function `chunk_list(lst, size)` that splits a list into
     chunks of given size. Return a list of lists.
     Example: ([1,2,3,4,5,6,7], 3) → [[1,2,3],[4,5,6],[7]]

Q32. Write a function that rotates a matrix (list of lists) 90 degrees
     counterclockwise using list comprehension and zip.

Q33. Write a function that takes a list of dictionaries (each with
     'name', 'age', 'city') and uses a lambda to sort them first by
     city alphabetically, then by age descending within the same city.

[Hard]
Q34. Write a function `sliding_window_max(lst, k)` that returns a list
     of the maximum value in each sliding window of size k.
     Example: ([1,3,-1,-3,5,3,6,7], 3) → [3,3,5,5,6,7]

Q35. Write a function that merges two sorted lists into one sorted list
     without using sort() or sorted(). Use a two-pointer approach with
     a while loop.

Q36. Write a function that finds the longest increasing subsequence
     (LIS) length in a list of integers.
     Example: [10,9,2,5,3,7,101,18] → 4 (the LIS is [2,3,7,101])


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 5. TUPLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q37. Write a function that takes a list of (name, age) tuples and uses
     a lambda with sorted() to return them sorted by age ascending.

Q38. Write a function that zips two lists into a list of tuples, then
     uses a dict comprehension to convert it into a dictionary.
     Demonstrate with names and phone numbers.

Q39. Write a function that takes a tuple of numbers and returns a new
     tuple with only the even numbers, using a generator expression
     inside tuple().

[Medium]
Q40. Write a function `unzip(list_of_tuples)` that separates a list of
     tuples into individual lists — one per position.
     Example: [(1,'a',True),(2,'b',False)] → ([1,2],['a','b'],[True,False])

Q41. Write a function that uses enumerate() on a list and stores each
     (index, value) pair as a tuple in a new list. Then filter the
     list to only keep tuples where value > 10.

Q42. Given a list of (product, category, price) tuples, use a lambda
     and sorted() to sort by category first, then by price descending
     within the same category. Return the sorted list.

[Hard]
Q43. Write a function that takes a list of (x, y) coordinate tuples
     and returns the pair of points that are closest to each other.
     Use the Euclidean distance formula. Import math for sqrt.

Q44. Write a function that groups a flat list of values into n-tuples.
     If the list length isn't divisible by n, discard the leftover.
     Example: ([1,2,3,4,5,6,7], 3) → [(1,2,3),(4,5,6)]

Q45. Using namedtuples, model an Employee with fields:
     name, department, salary. Write a function that takes a list of
     Employees and returns a dict grouping employees by department,
     with average salary per department.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 6. SETS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q46. Write a function using sets that takes a string and returns True
     if all characters in it are unique (no repeats).

Q47. Given a list of integers, use a set to find and return all numbers
     that appear more than once (duplicates only). Return sorted list.

Q48. Write a function that takes two sets of tags (like blog post tags)
     and returns: common tags, tags only in first set, tags only in
     second set — as three separate sets.

[Medium]
Q49. Write a function that takes a list of strings and returns all
     strings that are subsets of characters of the longest string.
     Use set comparison (issubset) for checking.

Q50. Write a function `disjoint_groups(list_of_sets)` that returns
     True if all sets in the list are mutually disjoint (no element
     appears in more than one set).

Q51. Given a long string of text, use sets to find all letters of the
     alphabet that are NOT present in the text.
     Import string and use string.ascii_lowercase.
     Return the missing letters as a sorted list.

[Hard]
Q52. Write a function that takes a list of integers and finds the
     smallest positive integer NOT present in the list using set logic.
     Example: [3,4,-1,1] → 2,  [1,2,3] → 4

Q53. Write a function `set_cover(universe, subsets)` that implements
     a greedy set cover algorithm: given a universe of elements and a
     list of subsets, return the minimum number of subsets needed to
     cover all elements in the universe.

Q54. Given two sentences, use sets to compute their Jaccard similarity:
     |intersection| / |union| of their word sets.
     Return the score rounded to 2 decimal places.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 7. DICTIONARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q55. Write a function using a dictionary and a lambda with sorted() to
     return the top N keys by their value.
     Example: top 3 scoring students from a scores dict.

Q56. Write a function that takes a sentence and returns a dict of each
     word mapped to its reversed form.
     Example: "hello world" → {'hello':'olleh','world':'dlrow'}

Q57. Write a function `count_types(lst)` that takes a mixed list and
     returns a dict counting how many ints, floats, strings, bools,
     and NoneTypes are in it.

[Medium]
Q58. Write a function that takes a dictionary of student scores and
     returns a new dict with grades assigned (use a lambda to map
     score → grade: A/B/C/D/F).

Q59. Write a function that deep-copies a nested dictionary without
     using the copy module. Use recursion.

Q60. Write a function `dict_diff(d1, d2)` that returns a dict showing
     the differences between two dicts:
     'added': keys in d2 not in d1,
     'removed': keys in d1 not in d2,
     'changed': keys in both but with different values.

[Hard]
Q61. Write a function that inverts a dictionary where values are lists.
     Each element of the list becomes a key pointing to the original
     key.
     Example: {'a':[1,2],'b':[2,3]} → {1:'a',2:'b',3:'b'}
     (If a value appears in multiple lists, last one wins.)

Q62. Write a function `lru_cache_manual(capacity)` that returns an
     object (use a dict + list) simulating an LRU (Least Recently Used)
     cache with a given capacity. Implement get(key) and put(key,value).

Q63. Write a function that takes a list of log entries as dicts:
     {'user': 'alice', 'action': 'login', 'time': 900}
     Return a dict grouping actions per user, and for each user, the
     total number of actions and the first and last action times.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 8. SLICING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q64. Write a function that takes a string and uses slicing to return
     the first half and second half separately as a tuple.
     For odd length, the middle character goes to the first half.

Q65. Given a list, use slicing to remove the first 2 and last 2
     elements. Return the remaining middle portion.

Q66. Write a function that uses slicing to check if a list is a
     palindrome (reads the same forwards and backwards).

[Medium]
Q67. Write a function `interleave(lst1, lst2)` that merges two lists
     by alternating elements using slicing assignment.
     Example: [1,2,3],[a,b,c] → [1,a,2,b,3,c]

Q68. Write a function that takes a string and uses slicing to return
     all substrings of length k.
     Example: "abcde", k=3 → ["abc","bcd","cde"]

Q69. Given a 2D matrix, use slicing to extract:
     (a) first two rows, (b) last two columns of every row,
     (c) every alternate row.
     Return all three as a tuple.

[Hard]
Q70. Write a function that uses slicing to implement a simple circular
     buffer: given a list and a starting index, return the list rotated
     so the element at that index comes first, wrapping around.
     Example: [1,2,3,4,5], start=2 → [3,4,5,1,2]

Q71. Write a function that takes a list of integers and uses slicing to
     find the sublist with the maximum sum (contiguous subarray).
     Use brute force with slicing — check all [i:j] combinations.

Q72. Write a function that takes a string and uses step-slicing to
     encode it: take every 3rd character starting from 0, then 1,
     then 2. Concatenate all three groups as the encoded output.
     Decoding must reverse this. Implement both encode and decode.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 9. TYPE CASTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q73. Write a function that takes a list of mixed values and separates
     them into two lists: one where casting to int succeeded, and one
     where it failed. Use try-except inside.

Q74. Write a function using a lambda and map() that takes a list of
     float strings like ['1.5','2.7','3.9'] and returns a list of
     integers by casting float first, then int.
     Example: '1.5' → float('1.5') → int(1.5) → 1

Q75. Write a function that takes a boolean list like
     [True, False, True, True] and returns its integer sum,
     its string representation, and a float version of the sum.
     Return as a tuple.

[Medium]
Q76. Write a function `smart_cast(value)` that tries to cast a single
     string value to the most appropriate type in this priority order:
     int → float → bool → None → str. Return the typed value.
     Use a global dict to track how many times each type was returned.

Q77. Write a function that reads a list of strings representing time
     in "HH:MM:SS" format, converts each part to int, and returns
     total seconds for each. Use type casting and string splitting.
     Example: "01:30:45" → 5445

Q78. Write a function that takes a list of values and returns a
     summary dict:
     'can_be_int': count, 'can_be_float': count,
     'true_bools': count, 'none_count': count,
     'strings_only': count.
     Values should not be double-counted (use priority: bool first).

[Hard]
Q79. Write a function `matrix_from_string(s)` that parses a string
     representation of a matrix like "1 2 3; 4 5 6; 7 8 9" and
     returns it as a 2D list of integers. Handle type casting and
     strip whitespace carefully.

Q80. Write a function that takes a CSV-like string with a header row:
     "name,age,score\nAlice,25,88.5\nBob,30,91.0"
     Return a list of dicts with values properly cast:
     name stays str, age becomes int, score becomes float.

Q81. Write a type-safe vector addition function: given two lists of
     mixed types (strings of numbers, ints, floats), cast all to float,
     add element-wise, and return results rounded to 2 decimal places.
     Raise a TypeError with a clear message if any element can't be cast.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 10. RECURSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q82. Write a recursive function `multiply(a, b)` that multiplies two
     positive integers using only addition (no * operator).
     multiply(3,4) → 3+3+3+3 → 12

Q83. Write a recursive function that counts how many times a digit d
     appears in a number n.
     Example: count_digit(12321, 1) → 2

Q84. Write a recursive function that converts a decimal number to
     binary (as a string) without using bin() or any built-in.

[Medium]
Q85. Write a recursive function `power_set(lst)` that returns all
     possible subsets of a list (the power set).
     Example: [1,2,3] → [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

Q86. Write a recursive function that finds the minimum element in a
     list without using min() or any sorting.

Q87. Write a recursive function `is_sorted(lst)` that returns True if
     the list is sorted in ascending order, False otherwise.
     Base case: list of 0 or 1 elements is always sorted.

[Hard]
Q88. Write a recursive function `merge_sort(lst)` that implements
     merge sort and returns the sorted list.

Q89. Write a recursive function that generates all valid combinations
     of n pairs of parentheses.
     Example: n=2 → ["(())", "()()"]
     Example: n=3 → ["((()))","(()())","(())()","()(())","()()()"]

Q90. Write a recursive function `evaluate_expression(expr)` that
     evaluates a simple arithmetic expression string with only +, -
     and single-digit integers (no spaces, no * or /).
     Example: "1+2+3-1" → 5
     Hint: find the last + or - and split there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 11. FUNCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q91. Write a function `describe_list(lst)` with a full docstring that
     returns a dict with: length, first element, last element, and
     whether it contains any duplicates.

Q92. Write a function that uses *args to accept any number of strings
     and returns them joined by a custom separator passed as a keyword
     argument sep=" ". Default sep is a single space.

Q93. Use a lambda and the `map()` function to write a one-liner that
     takes a list of names and returns each name in the format
     "Hello, {name}!".

[Medium]
Q94. Write a closure `make_counter(start=0, step=1)` that returns a
     function. Each call to the returned function increments the
     counter by step and returns the new value.

Q95. Write a function `retry(func, times)` that calls func up to
     `times` attempts. If func raises an exception, retry. If all
     attempts fail, raise the last exception. If it succeeds, return
     the result.

Q96. Write a function using **kwargs that builds and returns an HTML
     tag string. Function signature: `make_tag(tag, content, **attrs)`.
     Example: make_tag("a", "Click", href="https://x.com", class_="btn")
     → '<a href="https://x.com" class="btn">Click</a>'

[Hard]
Q97. Write a `memoize` decorator that caches results of any function
     based on its arguments. Use a dict as the cache. Apply it to a
     recursive Fibonacci function and compare speed with/without it.

Q98. Write a function `pipeline(*funcs)` that takes a list of functions
     and returns a new function that passes its input through each
     function in order (left to right).
     Example: pipeline(strip, lower, split)("  Hello World  ")
              → ['hello', 'world']

Q99. Write a function that accepts a function and returns a new
     function that enforces type checking on arguments based on
     annotations. If a wrong type is passed, raise TypeError.
     Example: if func expects int and gets str, raise TypeError.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 12. F-STRINGS & DOCSTRINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q100. Write a function with a full Google-style docstring that takes
      a list of (item, price, qty) tuples and prints a formatted
      invoice using f-strings. Include subtotal, tax (18%), and total.

Q101. Use f-string debugging syntax (f"{variable=}") to write a
      function that traces through computing the area and perimeter
      of a rectangle, printing each intermediate value using f"{var=}".

Q102. Write a function that formats a large number with commas and
      currency symbol using f-strings.
      Example: 1234567.89 → "₹1,234,567.89"

[Medium]
Q103. Write a class `Circle` with a docstring, and methods area() and
      perimeter() each with their own docstring. Use f-strings inside
      a __str__ method to return a readable description.
      Import math for pi. Access all docstrings and print them.

Q104. Write a function that takes a dict of student names and scores
      and prints a leaderboard using f-strings with:
      rank (right-aligned 3), name (left-aligned 20),
      score (right-aligned 6), grade bar (e.g. ████░░ out of 10 blocks).

Q105. Write a function that takes start_date and n_days (both as
      strings/ints) and prints n daily log entries using f-strings:
      "Day 1 | Date: 01-Jan | Status: Pending"
      Use a list of status values that cycle (import itertools.cycle).

[Hard]
Q106. Write a module-level docstring, then a class with a class-level
      docstring, then methods with method-level docstrings. Write a
      separate function `print_all_docs(obj)` that uses __doc__ to
      print all available docstrings of the object and its methods
      automatically using dir().

Q107. Write a function that generates a formatted Markdown-style
      report string using f-strings and a template approach. It should
      take a dict of report data and produce a multi-section Markdown
      string with headers (##), bullet points (-), and a summary table.

Q108. Write a function that uses f-strings with format spec variables
      (not hardcoded widths) to dynamically align a table based on the
      longest entry in each column.
      Example: width = max(len(r[col]) for r in rows) then f"{val:{width}}".


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 13. EXCEPTION HANDLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q109. Write a function `safe_divide(a, b)` that catches ZeroDivisionError
      and returns None. Also catch TypeError if non-numbers are passed
      and return the string "invalid input".

Q110. Write a function that opens a file by name and reads its content.
      Handle FileNotFoundError and PermissionError separately with
      meaningful messages. Use a finally block to print "Done attempting".

Q111. Write a function that takes a list of values and tries to convert
      each to int. Collect all failed values into a separate list.
      Use try-except inside a loop. Return (successes, failures).

[Medium]
Q112. Write a custom exception class `InsufficientFundsError` that
      accepts a message and the amount short. Use it in a BankAccount
      class withdraw() method that raises this error when balance is
      insufficient.

Q113. Write a function `parse_config(config_dict, required_keys)` that
      raises a custom `MissingKeyError` if any required key is absent,
      a `TypeError` if a value is the wrong type, and returns the
      validated config dict on success.

Q114. Write a decorator `handle_exceptions(*exception_types)` that
      wraps any function and catches the specified exception types,
      printing a formatted error message and returning None.
      Demonstrate with at least 3 different exception types.

[Hard]
Q115. Write a function that reads a "database" (a list of dicts) and
      performs CRUD operations. Each operation should raise a specific
      custom exception: RecordNotFoundError, DuplicateRecordError,
      ValidationError. Define all three exception classes.

Q116. Write a context manager class `ManagedTransaction` using
      __enter__ and __exit__ that simulates a database transaction:
      on success it "commits" (prints confirmation), on any exception
      it "rolls back" (prints rollback message) and suppresses the error.
      Use it with the `with` statement.

Q117. Write a function `retry_with_backoff(func, max_retries, delay)`
      that retries a failing function with exponential backoff
      (delay doubles each retry). Import `time` module for sleep.
      Raise a custom `MaxRetriesExceededError` if all retries fail.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 14. ENUMERATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Easy]
Q118. Use enumerate() to rewrite a classic for-loop-with-index pattern.
      Given a list of tasks, print each as:
      "Task 1: Buy groceries", "Task 2: Read book", etc.

Q119. Use enumerate(start=1) with a list of exam scores to print a
      ranked leaderboard. If the score is the highest so far, also
      print "(new high!)" next to it.

Q120. Write a function that uses enumerate() to find and return the
      index of the first element in a list that satisfies a condition
      passed as a lambda.
      Example: first_match([4,7,2,9,1], lambda x: x > 6) → 1

[Medium]
Q121. Write a function that uses enumerate() to compare two lists
      element by element and return a list of (index, val1, val2)
      tuples for positions where the values differ.

Q122. Use enumerate() to implement a function `rotate_with_enum(lst, k)`
      that returns a new list where each element is shifted to the
      position (i + k) % len(lst). Build the result list using
      enumerate on the original.

Q123. Write a function that takes a 2D list (matrix) and uses nested
      enumerate() calls to find and return all positions (row, col)
      where the value equals a given target.
      Return as a list of (row, col) tuples.

[Hard]
Q124. Write a function `diff_lists(old_list, new_list)` that uses
      enumerate() to produce a line-by-line diff output (like git diff):
      lines only in old → "- line"
      lines only in new → "+ line"
      lines in both same position → "  line"

Q125. Write a function using enumerate() and a dictionary to detect
      duplicate elements in a list and return a dict:
      {value: [list of indices where it appears]}
      Only include values that appear more than once.

Q126. Write a function `csv_to_dicts(csv_string)` that uses enumerate()
      to parse a CSV string: line 0 is the header, lines 1+ are data.
      Use enumerate to assign header fields to each value by index.
      Return a list of dicts. Handle missing values with None.


==============================================
 SUMMARY — BATCH 3
==============================================
Total Questions  : 126
Easy per topic   : 3   (42 total)
Medium per topic : 3   (42 total)
Hard per topic   : 3   (42 total)

Topics           : if-else, loops, strings, lists,
                   tuples, sets, dictionaries, slicing,
                   type casting, recursion, functions,
                   f-strings & docstrings,
                   exception handling, enumerate

Mixed into Qs    : local/global variables, lambda,
                   importing modules, if __name__
==============================================
'''
