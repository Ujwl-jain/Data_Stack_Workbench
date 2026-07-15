# ============================================================
#                    DECORATORS IN PYTHON
# ============================================================
# A decorator is a function that takes another function as
# an argument, adds some functionality around it, and returns
# a new enhanced version of that function.
#
# In simple terms: wrap extra behaviour around an existing
# function WITHOUT changing its original code.
#
# SYNTAX:
#   @decorator_name
#   def my_function():
#       ...
#
# The @ symbol is just shorthand. These two are identical:
#   @greet
#   def hello(): ...
#
#   hello = greet(hello)   <- same thing written manually
# ============================================================


# ============================================================
#              THE PROBLEM DECORATORS SOLVE
# ============================================================
# Suppose you want to print a message before and after
# every function in your program.
#
# Without decorators -- you repeat the same lines everywhere:

def hello():
    print("Good morning")       # repeated in every function
    print("hello world")
    print("Thanks for using")   # repeated in every function

def add(a, b):
    print("Good morning")       # repeated again
    print(a + b)
    print("Thanks for using")   # repeated again

# PROBLEM: if the message changes, you update every function.
# Breaks the DRY principle -- Don't Repeat Yourself.
#
# WITH decorators -- write the wrapper once, apply everywhere:


# ============================================================
#                  HOW A DECORATOR WORKS
# ============================================================

def greet(fx):          # fx = the function being decorated
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)     # calls the original function
        print("Thanks for using the function")
    return mfx          # returns the enhanced version

# *args, **kwargs are needed inside mfx because the decorated
# function might have its own arguments (like add(a, b)).
# Without *args/**kwargs, passing arguments to add() would crash.

'''
Workflow:

Once we add @greet before a function and call it, Python
takes that function as an argument inside greet(), wraps it
with the extra behaviour inside mfx(), and returns mfx as
the new version of that function.

hello() is passed as argument to greet -- no arguments of its own.

add() is passed as argument to greet -- but add() has its own
arguments (a, b), so *args and **kwargs inside mfx capture
and forward those arguments to fx() when it is called.
'''

@greet
def hello():
    print("hello world")

@greet
def add(a, b):
    print(a + b)

hello()
# Output:
# Good morning
# hello world
# Thanks for using the function

add(1, 2)
# Output:
# Good morning
# 3
# Thanks for using the function


# ============================================================
#          @ SYMBOL vs MANUAL CALL -- SAME THING
# ============================================================
# These two are identical:

# using @ symbol:
@greet
def hello():
    print("hello world")

hello()

# doing it manually without @:
def hello():
    print("hello world")

hello = greet(hello)    # greet takes hello, wraps it, returns mfx
hello()                 # now hello points to mfx, not the original

# @ is just cleaner shorthand for: function = decorator(function)


# ============================================================
#                PRACTICAL EXAMPLE -- TIMER
# ============================================================
# A real and common use of decorators -- measure how long
# a function takes to run without touching the function itself.

import time

def timer(fx):
    def mfx(*args, **kwargs):
        start = time.time()             # record start time
        fx(*args, **kwargs)             # run the actual function
        end = time.time()               # record end time
        print(f"Time taken: {end - start:.4f} seconds")
    return mfx

@timer
def process_data():
    total = 0
    for i in range(1000000):
        total += i
    print(f"Total: {total}")

process_data()
# Output:
# Total: 499999500000
# Time taken: 0.0623 seconds

# Without decorator you would add time.time() calls inside
# every single function you want to measure.
# With decorator -- one wrapper, apply anywhere with @timer.


# ============================================================
#              REAL LIFE USE CASES OF DECORATORS
# ============================================================
# Decorators are used heavily in real projects and frameworks.
# You will see them constantly when working with Flask, Django,
# FastAPI -- all of which you are learning.
#
# 1. LOGIN REQUIRED -- protect a route, only logged in users can access:
#
#    @login_required         <- Flask/Django decorator
#    def dashboard():
#        return "Welcome to dashboard"
#
#    If user is not logged in, decorator redirects to login page.
#    The dashboard function itself has no auth logic -- decorator handles it.
#
# 2. ROUTE DEFINITION IN FASTAPI/FLASK -- every API endpoint uses @:
#
#    @app.get("/users")      <- FastAPI decorator
#    def get_users():
#        return all_users
#
#    The @app.get decorator registers this function as the handler
#    for GET requests to /users. The function just returns data.
#
# 3. LOGGING -- record every time a function is called:
#
#    @log_calls
#    def create_user(name):
#        ...
#
#    Decorator logs: "create_user called at 10:45 AM" automatically.
#
# 4. RETRY -- retry a function if it fails (e.g. API call fails):
#
#    @retry(times=3)
#    def fetch_data():
#        ...
#
#    If fetch_data() throws an error, decorator retries it 3 times
#    before giving up. The function itself has no retry logic.


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Term              Meaning
#  ──────────────────────────────────────────────────────────────
#  Decorator         Function that wraps another function
#  @decorator        Shorthand for func = decorator(func)
#  fx                The original function passed as argument
#  mfx               Inner wrapper function with added behaviour
#  *args, **kwargs   Needed to forward any arguments the original
#                    function might have -- always include them
#  return mfx        Returns the enhanced version of the function
#
#  Structure of every decorator:
#  ──────────────────────────────────────────────────────────────
#  def decorator(fx):
#      def wrapper(*args, **kwargs):
#          # code BEFORE the function
#          fx(*args, **kwargs)
#          # code AFTER the function
#      return wrapper
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Always use *args, **kwargs in wrapper -- even if you think
#     the function has no arguments, it is safer to always include
#  2. Always return the inner function -- return wrapper not wrapper()
#  3. @ is just cleaner shorthand -- both ways produce the same result
#  4. Original function code is never changed -- decorator wraps around it
#  5. Multiple decorators can be stacked on one function
#     @decorator1
#     @decorator2
#     def my_func(): ...   <- decorator2 applied first, then decorator1
#
# ============================================================