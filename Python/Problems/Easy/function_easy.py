# Q1.  Write a function `greet(name, greeting="Hello")` that uses a default
#      argument and returns a greeting string like "Hello, Alice!".


def greet(name, greeting = 'Hello'):
    return f"{greeting}, {name}"

result = greet(name = 'Alice')
print(result)

# --------------------------------------------------------------------------------------------------
# Q2.  Write a function `calculator(a, b, op)` that takes two numbers and
#      an operator string ("+", "-", "*", "/") and returns the result.

def calculator(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    else:
        return "Invalid operator!"
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter a operator: ")

result1 = calculator(a,b,op)
print(result1)

# --------------------------------------------------------------------------------------------------
# Q3.  Write a function `is_divisible(n, divisor=2)` that returns True if
#      n is divisible by the divisor, False otherwise. Use a default param.

def is_divisible(n, divisor = 2):
    if n % divisor == 0:
        return True
    else:
        return False

result2 = is_divisible(25)
print(result2)

# --------------------------------------------------------------------------------------------------
# Q4.  Write a function that accepts *args and returns the sum of all
#      passed numbers. It should work with any number of arguments.

def multi_arg(*number):
    sum = 0
    print(type(number))
    for i in number:
        sum = sum + i
    
    return sum

result4 = multi_arg(4,2,15,67,13)
print(result4)