# Functions

# it is a block of code that performs a specific task whenever it is called.
# it is adiveced to use function in large amount of code this makes the program flow 
# orgranised and neat

a = 8
b = 7
if a>b:
  print("first is greater")
else:
  print("second")
gmean = (a*b)/(a+b)
print(gmean)

c = 8
d = 9
if c>d:
  print("first is greater")
else:
  print("second")
gmean2 = (c*d)/(c+d)
print(gmean2)

# instead create a function
def g_mean(a,b):
    if a>b:
        print("first is greater")
    else:
        print("second")
    mean = (a*b)/(a+b)
    print(mean)

# calling a function using the parameters in the paranthesis
g_mean(a,b)
g_mean(c,d)

def is_greater(e,f):
    if e>f:
        print("first is greater")
    else:
        print("second is greater")

# calling a function using the function namr and giving parameters in the paranthesis
is_greater(a,b)
is_greater(c,d)

def is_lesser(a,b): #means if a programmer wants to build a logic after some time he can just create a function and code later by doing 'pass' other wise it will show an error
   pass
    


# ------------------------------------------- Built in function ---------------------------------------
# these are defined and pre coded in python
# we do not have to use def with these functions
# examples - min(), max() sum (), type(), range(), dict(), list(), tuple(), set(), print(), etc
# for more example: list of all built in function - google it

# ------------------------------------------- User define function ---------------------------------------
# function created by user are user define function just like above exampe
# used to create to perform specific task based on users needs
# have to use def with these function



# --------------------- Arguments and return in function ------------------------

# certain ways of passing an argument ->
# 1. normally passing it
def average(a,b): #<-parameters
   print("average is", (a+b)/2)

average(6,8)  # <- arguments 

# 2. default argument
# it will just take the default values provided in the function paranthesis if no value is providedd at the time of calling a function
def average(a = 9,b = 10):
   print("average is", (a+b)/2)

average()

# in this case it will ignore the default arguments and took the actual arguments
def average(a = 9,b = 10):
   print("average is", (a+b)/2)

average(10,2) # it will take these arguments, ignoring the default arguments
average(b =2) # it will take these arguments, ignoring the default arguments of b and take the default value of a 
average(10) # it will take these arguments, ignoring the default arguments of a and take the default value of b

def name(fname, mname = "james", lname = "watson"):
   print("the name is: ", fname, mname, lname)

name('amy', "agarawal")

# 3. keywords arguments 
# the order in which the arguments are passed does not matter
# as it recognised the arguments by the parameter name
def name(fname, mname = "james", lname = "watson"):
   print("the name is: ", fname, mname, lname)

# for example it here i use the lname first then fname, but it will still work fine as i want.
name(lname = 'agarawal', fname = "Ujjwal") 

# 4. Required argument 
#  it is necessary to pas the arguments in the correct order and the number of arguments passed should match with actual function definition
# for example:
# in the below code default value are given for mname and lname means these are optional to provide in the arguments at the time of calling
# but fname does not have a default value means it is required argument which is needed at the time of calling the function
def name(fname, mname = "james", lname = "watson"):
   print("the name is: ", fname, mname, lname)

name(fname = 'amy')
# name('amy'), both are same.

# 5. variable lenth argument 

'''
sometimes we may need to passs more arguments than those defined in the actual function, this can
can be done using variable lenght arguments

for example: learn the example using 2 methods of this arguments
'''
# -> arbitary arguments:
'''
while creating a function, pass a * befor the parameter name while defining the function 
function access the arguments by processing them in the form of tuples
'''
def average_and(*number):
    print(type(number))
    sum = 0
    for i in number:
      sum = sum +i
    print("average is", sum/ len(number))

# here more than 1 arguments are passing and only 1 paramter is in the function, these arguments 
# will be converted into a series of tuple and then process through a loop to get an average
average_and(10,11,12,13)


# To make it work with a list, use * when calling:
# python my_list = [10,11,12,13]
# result4 = average_and(*my_list)  # * unpacks list into separate arguments!
# # same as writing average_And(10,11,12,13) 

# -> keyword arbitary arguments

'''
while creating a function, pass a ** befor the parameter name while defining the function 
function access the arguments by processing them in the form of dictionary
'''
def name_and(**name):
    print(type(name))
    print("the name is", name["fname"],name["mname"], name["lname"])

'''
here more than 1 arguments are passing and only 1 paramter is in the function, these arguments 
will be converted into a series of dictonary and then process through a loop to get a name
below arguments will be converted into key-value paired in the parameters which looks like this
**name  = {(mname: "bol", fname : "amit", lname : "bachan"}
'''
name_and(mname = "bol", fname = "amit", lname = "bachan")


# ------------------------- Return statement --------------------------
# Used to retunr the value of the expression back to the caliing function

def average_and(*number):
    print(type(number))
    sum = 0
    for i in number:
      sum = sum +i
    # print("average is", sum/ len(number))

    'if there are 2 returns first to be written will be returned, here i write return 0 but '
    'commented but if it is commented out it will return the 0 ignoring the next return'
    'if return nothing, it will return none by default to the calling function'
    # return 0
    return sum / len(number)

'''
c wil store the value of average after getting the return from the function 
as stated in the above script, here return of sum/len(number) will be returned to 
the calling function - average_and and stored it inside c
''' 
c = average_and(10,11,12,13)
print(c)




# ------------------------ NOTES BY Claude -------------------------

# ============================================================
#                     FUNCTIONS IN PYTHON
# ============================================================
# A function is a block of code that performs a specific task
# whenever it is called.
#
# WHY USE FUNCTIONS?
# - Avoid repeating the same code (DRY - Don't Repeat Yourself)
# - Makes code organized, readable, and easy to debug
# - A function is written once but can be called many times
# - Breaks large programs into smaller, manageable pieces
#
# SYNTAX:
#   def function_name(parameters):
#       # code block
#       return value    # optional
# ============================================================


# ------------------------------------------------------------
# Problem WITHOUT functions -- repeated code
# ------------------------------------------------------------
# Notice how the same logic is copy-pasted for different values.
# If you need to fix a bug, you have to fix it in EVERY copy.

a = 8
b = 7
if a > b:
    print("first is greater")
else:
    print("second")
gmean = (a * b) / (a + b)
print(gmean)

c = 8
d = 9
if c > d:
    print("first is greater")
else:
    print("second")
gmean2 = (c * d) / (c + d)
print(gmean2)


# ------------------------------------------------------------
# Solution WITH functions -- write once, call many times
# ------------------------------------------------------------
# Now if the logic changes, you only update ONE place.

def g_mean(a, b):
    if a > b:
        print("first is greater")
    else:
        print("second")
    mean = (a * b) / (a + b)
    print(mean)

# calling the function -- same logic, different values, no repetition
g_mean(8, 7)
g_mean(8, 9)


# ------------------------------------------------------------
# pass keyword -- empty function placeholder
# ------------------------------------------------------------
# If you want to define a function but write the logic later,
# use 'pass' to avoid a syntax error on an empty body.

def is_lesser(a, b):
    pass        # placeholder -- no error, no logic yet

# This is useful when planning out your program structure first.


# ============================================================
#                  TYPES OF FUNCTIONS
# ============================================================


# ------------------------------------------------------------
# 1. Built-in Functions
# ------------------------------------------------------------
# Pre-coded in Python -- no 'def' needed.
# Available directly without importing anything.
# Examples:

print(min(3, 7, 1))         # 1
print(max(3, 7, 1))         # 7
print(sum([1, 2, 3, 4]))    # 10
print(type("hello"))        # <class 'str'>
print(len([1, 2, 3]))       # 3
print(abs(-42))             # 42
print(round(3.7))           # 4

# Full list: https://docs.python.org/3/library/functions.html


# ------------------------------------------------------------
# 2. User-Defined Functions
# ------------------------------------------------------------
# Functions created by the programmer to perform specific tasks.
# Must use 'def' keyword.

def is_greater(a, b):
    if a > b:
        print("first is greater")
    else:
        print("second is greater")

is_greater(8, 7)    # first is greater
is_greater(8, 9)    # second is greater


# ============================================================
#              ARGUMENTS AND PARAMETERS
# ============================================================
# Parameters - variables listed in the function DEFINITION
# Arguments  - actual values passed when CALLING the function
#
# def average(a, b):   <- a and b are PARAMETERS
#     ...
# average(6, 8)        <- 6 and 8 are ARGUMENTS
# ============================================================


# ------------------------------------------------------------
# Type 1 - Normal (Positional) Arguments
# ------------------------------------------------------------
# Arguments are passed in the same ORDER as the parameters.
# Position matters -- first arg maps to first param, and so on.

def average(a, b):
    print("average is", (a + b) / 2)

average(6, 8)       # a=6, b=8 -> average is 7.0


# ------------------------------------------------------------
# Type 2 - Default Arguments
# ------------------------------------------------------------
# A default value is assigned to a parameter in the definition.
# If no argument is passed for that parameter, default is used.
# If an argument IS passed, it overrides the default.
# NOTE: Parameters with defaults must come AFTER required ones.

def average(a=9, b=10):
    print("average is", (a + b) / 2)

average()           # uses defaults -> a=9, b=10 -> 9.5
average(10, 2)      # overrides both defaults -> 6.0
average(10)         # a=10, b uses default 10 -> 10.0
average(b=2)        # b=2, a uses default 9 -> 5.5

def name(fname, mname="james", lname="watson"):
    print("the name is:", fname, mname, lname)

name("amy", "agarawal")    # fname=amy, mname=agarawal, lname=watson (default)


# ------------------------------------------------------------
# Type 3 - Keyword Arguments
# ------------------------------------------------------------
# Arguments are passed using the parameter NAME explicitly.
# Order does NOT matter when using keyword arguments.
# Makes function calls more readable and flexible.

def name(fname, mname="james", lname="watson"):
    print("the name is:", fname, mname, lname)

name(lname="agarawal", fname="Ujjwal")
# even though lname is passed first, Python maps it correctly
# Output: the name is: Ujjwal james agarawal


# ------------------------------------------------------------
# Type 4 - Required Arguments
# ------------------------------------------------------------
# Parameters WITHOUT a default value are REQUIRED.
# You MUST pass them when calling the function.
# If skipped, Python raises a TypeError.

def name(fname, mname="james", lname="watson"):
    print("the name is:", fname, mname, lname)

# fname has no default -> it is REQUIRED
name(fname="amy")           # works fine -> amy james watson
name("amy")                 # same as above, positional

# name()                    # TypeError: missing required argument 'fname'


# ------------------------------------------------------------
# Type 5 - Variable Length Arguments (*args)
# ------------------------------------------------------------
# Used when you don't know how many arguments will be passed.
# Use * before the parameter name in the function definition.
# All passed arguments are collected into a TUPLE inside the function.
# Useful when the number of inputs can vary each time.

def average_all(*numbers):
    print(type(numbers))        # <class 'tuple'>
    total = 0
    for i in numbers:
        total += i
    print("average is", total / len(numbers))

average_all(10, 11, 12, 13)         # 4 arguments
average_all(1, 2)                   # 2 arguments -- same function, different count
average_all(5, 10, 15, 20, 25)      # 5 arguments

# Internally: numbers = (10, 11, 12, 13) -- a tuple


# ------------------------------------------------------------
# Type 6 - Keyword Variable Length Arguments (**kwargs)
# ------------------------------------------------------------
# Use ** before the parameter name in the function definition.
# All passed keyword arguments are collected into a DICTIONARY.
# Keys = argument names, Values = argument values.
# Useful when you want named inputs of unknown count.

def name_all(**name):
    print(type(name))           # <class 'dict'>
    print("the name is", name["fname"], name["mname"], name["lname"])

name_all(mname="bol", fname="amit", lname="bachan")
# Internally: name = {"mname": "bol", "fname": "amit", "lname": "bachan"}

# You can also loop over **kwargs like a dictionary:
def show_details(**info):
    for key, value in info.items():
        print(key, ":", value)

show_details(city="pune", age=21, language="python")
# Output:
# city : pune
# age : 21
# language : python


# ============================================================
#                     RETURN STATEMENT
# ============================================================
# Used to send a value BACK to the place where the function was called.
# Once return is hit, the function STOPS executing immediately.
# A function can only return ONE value (but it can be a list/tuple).
# If no return is written, the function returns None by default.
# ============================================================

def average_all(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)     # sends result back to caller

# The returned value can be stored in a variable
result = average_all(10, 11, 12, 13)
print(result)           # 11.5

# Or used directly in an expression
print(average_all(1, 2, 3) * 2)     # 4.0


# return stops execution -- anything after it is ignored:
def demo():
    return 10           # function exits here
    print("this never runs")    # unreachable code

print(demo())           # 10


# returning multiple values -- Python packs them into a TUPLE:
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)        # 1 9


# no return -> returns None:
def greet(name):
    print("hello", name)

result = greet("ujjwal")
print(result)           # None


# ============================================================
#                    QUICK REFERENCE SUMMARY
# ============================================================
#
#  Concept                  Description
#  ──────────────────────────────────────────────────────────────────
#  def                      Keyword to define a function
#  Parameters               Variables in the function definition
#  Arguments                Values passed when calling the function
#  pass                     Placeholder for empty function body
#  return                   Sends a value back to the caller
#  return (nothing)         Returns None by default
#
#  Argument Types:
#  ──────────────────────────────────────────────────────────────────
#  Positional               Passed in order -- position matters
#  Default                  Has a fallback value if not passed
#  Keyword                  Passed by name -- order does not matter
#  Required                 No default -- must always be provided
#  *args                    Collects extra positional args as TUPLE
#  **kwargs                 Collects extra keyword args as DICTIONARY
#
#  Common Rules:
#  ──────────────────────────────────────────────────────────────────
#  1. Required parameters must come BEFORE default parameters
#  2. *args must come BEFORE **kwargs in the definition
#  3. return immediately exits the function
#  4. A function can only return one object (use tuple/list for many)
#  5. Forgetting () when calling a function does nothing (no error)
#
# ============================================================