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

# --------------------------------------------------------------------------------------------------------------------
# Q3. Write a function that takes a character and returns whether it is a 'vowel', 'consonant', or 'not a letter'.

def str_checker(chr):
    list_vowels = ['a','e','i','o','u']
    if chr.isalpha() and chr in list_vowels:
        return 'Vowel'
    elif chr.isalpha():
        return 'Consonant'
    else:
        return 'Not a letter'


chr = input("enter a character to check: ")
result = str_checker(chr)
print(result)