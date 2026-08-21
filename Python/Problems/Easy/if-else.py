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

# ------------------------------------------------------------------------------------------------------------------
# Q4.  Write a function that takes a username (string) and password
#      (string). If username is "admin" and password is "1234", return
#      "Access granted", else return "Access denied".

def login_access(u,p):
    if u == 'admin' and password == '1234':
        return 'Access granted'
    else:
        return 'Access denied - Invalid username or password'

user = input('Enter the Username:')
password = input('Enter the Password')

result = login_access(user, password)
print(f'{result}')

#  ------------------------------------------------------------------------------------------------------------------
# Q5.  Write a function that takes a number and returns "fizz" if
#      divisible by 3, "buzz" if by 5, "fizzbuzz" if by both, else
#      returns the number itself. Use a lambda to call it on a list.

# lets do both the approach


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'Fizzbuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n
    
num = int(input('Enter the number: '))
result = fizzbuzz(num)
print(f'The {num} is {result}')

# # using lambda:
list_num = [1,2,3,4,5,6,7,8,9,10,15]
result = list(map(fizzbuzz,list_num))
print(result)


# Q6.  Import the `math` module. Write a function that takes a number
#      and returns "perfect square" if its square root is a whole number,
#      else "not a perfect square". Use math.sqrt() inside.

from math import sqrt

def calculations(n):
    sq_rt = sqrt(n)
    if sq_rt % 1 == 0:
        return 'Perfect Square'
    else:
        return 'Not a perfect square' 

num = int(input('Enter the number: '))
result = calculations(num)
print(f'The {num} is {result}')


# 
# Q7.  Write a function that takes a username (string) and password
#      (string). If username is "admin" and password is "1234", return
#      "Access granted", else return "Access denied".

class LoginPage():
    def __init__(self, user, ps):
        self.user = user
        self.ps = ps

    def logincred(self):
        if self.user == 'admin' and self.ps == '1234':
              return 'Access granted'
        else:
             return 'Access denied'

rohan = LoginPage('admin', '1234')
ujjwal = LoginPage('admin', '1243')

print(rohan.logincred())
print(ujjwal.logincred())
