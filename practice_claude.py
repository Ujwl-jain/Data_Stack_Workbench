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

Q36 [Medium] Create a named tuple for a 'Student' with fields name, grade, score. Demonstrate usage.

Q37 [Hard]   Given a list of (item, price) tuples, find the most expensive item without using max().


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

Q53 [Easy]   Write a function with a proper docstring that converts Celsius to Fahrenheit.

Q54 [Medium] Print a formatted table of products (name, qty, price) using f-strings with alignment.

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


# ---------------------------------------------------------------------------------------------------
# Q1 Write a function that takes an integer and returns 'positive', 'negative', or 'zero'.

def int_checker(n):
    if n == 0:
        print("it is zero")
    elif n > 0:
        print("it is positive number")
    else:
        print("the number is negative")

n = int(input("Enter the number to check: "))
int_checker(n)

# ---------------------------------------------------------------------------------------------------
# Q2.  Check if a number is even or odd using a single-line if-else expression.

# Normal
ev_od = int(input("Enter the number to check: "))
if ev_od % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

# single line
print('even' if ev_od % 2 == 0 else 'odd')

# ---------------------------------------------------------------------------------------------------
# # Q3  [Medium] Given three sides of a triangle, determine if it's equilateral, isosceles, or scalene.

ang1  = int(input("enter the side of a triangle: "))
ang2  = int(input("enter the side of a triangle: "))
ang3  = int(input("enter the side of a triangle: "))

if ang1 == ang2 == ang3:
    print("it is a equilateral triangle")
elif ang1 == ang2 or ang1 == ang3 or ang2== ang3:
    print("it is isosceles")
else:
    print("it is scalene")

# ---------------------------------------------------------------------------------------------------    
# # Q4  [Medium] Write a grading system: A (90+), B (80-89), C (70-79), D (60-69), F (below 60).

T_grade = int(input("enter the total number of percentage of your grade: "))

if T_grade < 0 or T_grade > 100:
    print("Invalid grade! Please enter between 0 and 100")
elif T_grade >= 90:
    print("Congrats!! you got an A")
elif T_grade >= 80:
    print("Yoho!! You got B")
elif T_grade >= 70:
    print("Nice!! You got C")
elif T_grade >= 60:
    print("HMMM! You got a D")
else:
    print("Better luck next time, Its F")
 
# --------------------------------------------------------------------------------------------------- 
# Q5  [Hard]   FizzBuzz: Print numbers 1–100, but 'Fizz' for multiples of 3, 'Buzz' for 5, 'FizzBuzz' for both.

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        n = "FizzBuzz"
    elif n % 3 == 0:
        n = "Fizz"
    elif n % 5 == 0:
        n = 'Buzz'
    print(n)

# different approach same thing:
for n in range(1, 101):  
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
     
# --------------------------------------------------------------------------------------------------- 
# Q6  [Hard]   Given a year, determine if it's a leap year using proper Gregorian rules.
year = int(input("enter a year to check the leap year: "))

if year % 400 == 0:
    print("it is leap year")
elif year % 100 == 0:
    print("it is not a leap year")
elif year % 4 == 0:
    print("it is a leap year")
else:
    print("it is not a leap year")

# ---------------------------------------------------------------------------------------------------
# Q7  [Easy]   Reverse a string using slicing only (no built-in reverse).

str_reverse = 'I am Ujjwal jain'
print(str_reverse[::-1])

# Q8  [Easy]   Extract every other character from a string starting from index 0.
str_cha= 'i am ujjwal jain i am 24 year old'
print(str_cha[::2])

# Q9  [Medium] Given a list, return the middle third of it using slicing.

list_slice = [1,2,3,4,5,6,7,8,9]

list_len = len(list_slice)
one_third = list_len // 3
start_third = one_third
mid_third = one_third * 2
end_third = one_third * 3

print(list_slice[one_third:mid_third])


# ---------------------------------------------------------------------------------------------------
# Q10 [Medium] Check if a string is a palindrome using slicing (no loops).

str1 = 'racecar'
if str1 == str1[::-1]:
    print("it is palindrome")
else:
    print("it is not palindome")

# Q11 [Medium] Rotate a list to the right by k positions using slicing.

# Q12 [Hard]   Given a 2D matrix (list of lists), extract the diagonal elements using slicing concepts.


# ---------------------------------------------------------------------------------------------------
# Q13   Create a list of squares of numbers from 1 to 10 using list comprehension.

# Normal way
square_list = []
for i in range(1,11):
    square_list.append(i**2)

print(square_list)

# list comprehension
squares = [i**2 for i in range(1,11)]
print(squares)


# ---------------------------------------------------------------------------------------------------
# Q14   Flatten a list of lists into a single list using list comprehension.

list_list = [['my','name'],[1,2],[True, False]]
final_result = [items for lists in list_list for items in lists]
print(final_result)


# ---------------------------------------------------------------------------------------------------
# Q15   Filter all even numbers from a list using list comprehension.

list_num = [2,1,4,1,5,6,2,8,10,54,99,104,32,14]
list_even = []
# normal way
for item in list_num:
    if item % 2 == 0:
        list_even.append(item)
    else:
        pass
print(list_even)

# list comprehension
list_even2 = [items for items in list_num if items % 2 == 0]
print(list_even2)


# ---------------------------------------------------------------------------------------------------
# Q16 [Medium] Given a list of words, return a list of words longer than 5 characters, uppercased.

list_word = ["mango", "tomato", "potato", "ice", "water", "colddrinks", "Lemon"]
list_long =[]

for words in list_word:
    if len(words) > 5:
        list_long.append(words.upper())

print(f"List of words longer than 5 characters in uppercase are: {list_long}")

# using list comprehension ->
list_long = [words.upper() for words in list_word if len(words) > 5]

# Read it like plain English:
# ```
# give me words.upper()
# for every words in list_word
# if len(words) > 5


# ---------------------------------------------------------------------------------------------------
# Q17 [Medium] Remove duplicates from a list while preserving order (no set shortcuts).5

list_rem = ["mango", "mango", "potato", "ice", "water", "colddrinks", "ice"]
list_original =[]

for words in list_rem:
    if words not in list_original:
        list_original.append(words)
        
list_rem = list_original
print(list_rem)



# ---------------------------------------------------------------------------------------------------
# Q18 [Medium] Transpose a matrix (list of lists) using list comprehension.

matrix = [[1,2],[5,6],[8,9],[0,4]]
transpose = []
for lst in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[lst])
    transpose.append(new_row)

print(transpose)    

# using list comprehension - need to learn this code
transpose_comp = [                              # outer list
            [row[lst] for row in matrix]        # inner list — same as new_row
            for lst in range(len(matrix[0]))    # outer loop
            ]


# -----------------------------------------------------------------------------------------------------------
# Q19 [Hard]   Generate a multiplication table (1–10) as a 2D list using nested list comprehension.

table_list = []
 
for row in range(1, 11):
    list_cal = []                        # reset inner list for each row
    for column in range(1, 11):
        mat = row * column               # calculate product
        list_cal.append(mat)             # add to current row
    table_list.append(list_cal)          # add completed row to final list
 
print(table_list)
 
# -----------------------------------------------------------------------------
# METHOD 2 — Nested List Comprehension (Same result, 1 line!)
# -----------------------------------------------------------------------------
 
list_Comp = [[row * column for column in range(1, 11)] 
             for row in range(1, 11)]
 
print(list_Comp)
 


# -------------------------------------------------------------------------------------------------------
# Q20 [Hard]   Find all prime numbers up to N using list comprehension and a helper function.

n = 10
list_prime = []

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    # is this return true outside cause it will automatically says true as call condition fails for actual prime numnber?? 
    return True
    
for i in range(n):
    if is_prime(i) == True:
        list_prime.append(i)

print(list_prime)

# using list comprehenion
prime_list = [i for i in range(10) if is_prime(i) == True ]
print(prime_list)



# ---------------------------------------------------------------------------------------------------
# Q21   Count vowels in a string without using any built-in count method.
string_line = 'i am ujjwal jain and i am 24 years old'

# set lookup is faster than list lookup here so instead of list we can create a set as well
# set_vowels ={'a','e','i','o','u'}
list_vowels = ['a','e','i','o','u']
count_v = 0
count_c = 0

for char in string_line.lower():
    if char in list_vowels:
        count_v += 1
    elif char.isalpha():
        count_c += 1
    else:
        pass
print(f"the number of vowels in the string is {count_v} and the number of consonant is {count_c}" )

# built in method approach - need to dry run this again
string_line = 'i am ujjwal jain and i am 24 years old'
vowels = 'aeiou'
count_v = sum(string_line.lower().count(v) for v in vowels)
print("Vowels:", count_v)

# using built in method and list comprehension - dry run this
string_line = 'i am ujjwal jain and i am 24 years old'
vowels = 'aeiou'

# meaning of the below line os  - For every character that satisfies the condition → add 1
# We use 1 because each valid character contributes 1 to the total count
count_v = sum(1 for char in string_line.lower() if char in vowels)
count_c = sum(1 for char in string_line.lower() if char.isalpha() and char not in vowels)

print("Vowels:", count_v)
print("Consonants:", count_c)


# ---------------------------------------------------------------------------------------------------
# Q22   Reverse words in a sentence (not characters).

string_rev = 'i am ujjwal jain and i am 24 years old'
list_rev = string_rev.split()[::-1]

rev_string = ' '.join(list_rev)
print(rev_string)


# ---------------------------------------------------------------------------------------------------
# Q23  Check if two strings are anagrams of each other.



# ---------------------------------------------------------------------------------------------------
# Q24  Find the longest word in a sentence using string methods only.

str1 = input("enter the first string: ")
str2 = input("enter the 2nd string: ")

if sorted(str1.lower()) == sorted(str2.lower()):
    print("yes this is anagram")

else:
    print("it is not anagram")

# ---------------------------------------------------------------------------------------------------------
# Q26 [Hard]   Implement a Caesar cipher: shift each letter by k positions, preserve case and non-letters. - explanation in hard_prob.py

str_CC = 'Hello! World$!'
k = 3
str_c = ''
for char in str_CC:
    if char.isdigit():
        pass
    elif char.isalpha() and char.islower():
        char =  chr(((ord(char) - ord('a')) + k) % 26 + ord('a'))
    elif char.isalpha and char.isupper():
        char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    else:
        char = char

    str_c = str_c + char

print(str_c)


# or - isalpha() is removed cause islower and isupper is indicating that the char is character not digit

str_CC = 'Hello! World$!'
k = 3
str_c = ''

for char in str_CC:
    if char.islower():
        char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
    elif char.isupper():
        char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
    str_c = str_c + char

print(str_c)


# -----------------------------------------------------------------------------------------------------------
# Q27 [Hard]   Find all substrings of a string that are palindromes and return them sorted by length.


str_sub = 'Hello'

list_sub = []
for start in range(len(str_sub)):
    for end in range(start+1, len(str_sub) + 1):
        sub = str_sub[start:end]
        if sub == sub[::-1]:
            list_sub.append(sub)
        else:
            pass

sort_sub = sorted(list_sub, key = len, reverse= True)
print(sort_sub)

# ---------------------------------------------------------------------------------------------------
# Q28 [Easy]   Write a safe int converter that returns None instead of raising ValueError.

a = 'Ujjwal'

try:
    print(int(a))

except:
    print(None)

# improved version -
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

# testing it
print(safe_int('Ujjwal'))  # None ✅
print(safe_int('123'))     # 123 ✅
print(safe_int('24.5'))    # None ✅ (float string also fails int conversion)


# ---------------------------------------------------------------------------------------------------
# Q29 [Easy]   Convert a list of string numbers ['1','2','3'] to actual integers using map and int.

list_s = ['1' , '2' , '3']
list_n = []
try:
    for n in list_s:
        list_n.append(int(n))
except ValueError:
    print("Invalid list") 

print(list_n)

# using map() - need to learn this

list_s = ['1', '2', '3']

list_n = list(map(int, list_s))

print(list_n)  # [1, 2, 3] 

# Q30 [Medium] Given mixed input (int, float, str), convert all to float and sum them. Handle errors gracefully.

# Q31 [Medium] Convert a decimal number to binary, octal, and hexadecimal without using bin/oct/hex.

# Q32 [Hard]   Parse a CSV string '1,2.5,hello,True,None' into Python-typed values automatically.



# ---------------------------------------------------------------------------------------------------
# Q33    Unpack a tuple of (name, age, city) and print each using f-strings.

tuple_unpack = ('Ujjwal', '24', 'Pune')
name, age, city = tuple_unpack

print(f"I am {name}, i am {age} year old and i am currently living in {city}")


# ---------------------------------------------------------------------------------------------------
# Q34    Swap two variables using tuple packing/unpacking in a single line.

x = 100
y = 10

x,y = (y,x)

print(y,x)


# ---------------------------------------------------------------------------------------------------
# Q38    Invert a dictionary (swap keys and values). Assume all values are unique.
dict_invert = {'number' : (1,2,3), 'string' : ('a-z','A-Z'), 'bool' : (True, False)}

dict_swap = {}
 
for key,value in dict_invert.items():
    dict_swap[value] = key

print(dict_swap)


# ---------------------------------------------------------------------------------------------------
# Q39    Merge two dictionaries. If keys conflict, keep the value from the second dict.

buy_dict = {'fruits' : 'mangos', 'veggies' : 'potato', 'spices' : 'clove'}
stock_dict = {'fruits' : 3, 'goods': 5, 'spices' : 10}

final_dict = {}

for key,value in buy_dict.items():
    final_dict[key] = value

for key, value in stock_dict.items():
    final_dict[key] = value

print(final_dict)

# using update - learn this
final_dict = buy_dict.copy()
final_dict.update(stock_dict)

print(final_dict)

# using dict unpacking - learn this
final_dict = {**buy_dict, **stock_dict}

print(final_dict)

# Q40 [Medium] Count word frequency in a sentence and return the top 3 most common words.
str_count = 'I am ujjwal jain, and I am 24 years old, i am in love with love python, studies, and games'

dict_freq = {}
count_k = 0

for word in str_count.lower().split():
    if word not in dict_freq:
        dict_freq[word] = 1
    else:
        dict_freq[word] += 1
dict_sort = sorted(dict_freq.items(), key = lambda x:x[1], reverse = True)

print(dict_sort[0:3])

# Q41 [Medium] Group a list of words by their first letter using a dictionary.

str_word = 'Data Scine, data analyst, data validation is the course of my direction value of this certification are vaybig'

dict_group = {}
for words in str_word.lower().split():
    if words[0] not in dict_group:
        dict_group[words[0]] = [words]
    else:
        dict_group[words[0]].append(words)

print(dict_group)

'''
first step is to excess the string convert it into list of words using split doing lower as well
second step is to excess that list and put the words in a list of words in that dictonary as value and its first char as key
for exmple if the word is data {'d' : [data]},
now how to append into the same list into dictonary, if the first word is same using if else
if word.split()[0] not in dict_group, then add it with the list of its value
else:
append in the value of list if it exist 
'''
# Q46 [Easy]   Find the sum of all digits of a number using a while loop.

# using for loop - wrong code according to the question, correct working
list1 = [5,1,40,20,199,4,19,77]
sum = 0
sum1 = 0
for n in list1:
    sum = sum + n

print(f'the sum of all the numbers in list is: {sum}')

# using while loop actual code of that question
num = int(input("enter a more than 3 digit number: "))
total = 0
while num>0:
    digit = num%10
    total = total + digit
    num = num // 10

print(total)


# Q50 [Hard]   Implement bubble sort using nested loops and count the number of swaps made.

unsorted_lst = [3,2,1,4]
swap_count = 0  

for element in range(len(unsorted_lst)-1):
    for ele in range(len(unsorted_lst) - 1 - element):
        if unsorted_lst[ele] > unsorted_lst[ele+1]:
            swap_count += 1
            unsorted_lst[ele], unsorted_lst[ele+1] = unsorted_lst[ele+1],  unsorted_lst[ele]
        
print(unsorted_lst, 'and', swap_count)

# Q51 [Hard]   Find all Armstrong numbers between 1 and 1000 using loops (e.g. 153 = 1³+5³+3³).

list_armstrong= []
for i in range (1,1001):
    digit = str(i)
    container = 0
    power = len(digit)
    for char in digit:
        container = container + (int(char)**power)
    
    if container == i:
        list_armstrong.append(i)
        
print(list_armstrong)

# Q59 [Medium] Use list methods: append, extend, insert, remove, pop, sort, reverse, index, count.

list_methods = ['Ujjwal', 'jain', 59, True, False, 'I am ujjwal Jain']
list_methods.append('Mango is a fruit')
list_methods.extend([1,5,2])
list_methods.insert(3, 'Yeahhhh')
list_methods.remove(59)
list_methods.pop(1)
# since sort can not be done cause list contains different data types
# list_methods.sort()
list_methods.reverse()
print(list_methods.index('Yeahhhh'))
print(list_methods.count('Ujjwal'))
print(list_methods)

# Q60 [Hard]   Implement your own version of str.split() and str.join() without using the built-in methods.
