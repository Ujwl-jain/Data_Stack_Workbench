# ---------------------------- Notes by claude -----------------------
# ============================================================
#                   EXCEPTION HANDLING IN PYTHON
# ============================================================
# Exception handling is the process of responding to unexpected
# or unwanted events (errors) that occur during program execution.
#
# WHY USE IT?
# - Prevents the program from crashing on unexpected input
# - Allows the program to continue running after an error
# - Helps in debugging by showing what went wrong
# - Lets you handle different errors in different ways
#
# WHAT IS AN EXCEPTION?
# When Python encounters an error, it RAISES an exception.
# If the exception is not handled, the interpreter stops the
# current process and the program crashes.
#
# Common built-in exceptions:
#   ValueError     -- wrong value type (e.g. int("abc"))
#   IndexError     -- index out of range (e.g. list[99])
#   KeyError       -- key not found in dictionary
#   TypeError      -- wrong data type used in operation
#   ZeroDivisionError -- dividing a number by zero
#   FileNotFoundError -- file does not exist
#   NameError      -- using a variable that was never defined
# ============================================================


# ============================================================
#                     TRY AND EXCEPT
# ============================================================
# try   -- wrap the code that MIGHT cause an error here
# except -- what to do IF that error occurs
#
# SYNTAX:
#   try:
#       # risky code
#   except ExceptionType:
#       # what to do if that error occurs
#
# The program does NOT crash -- execution continues after the block.
# ============================================================


# ------------------------------------------------------------
# Problem WITHOUT exception handling
# ------------------------------------------------------------
# If the user types a word instead of a number, this crashes.

# a = input("enter a number:")
# for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")   # crashes if a = "hello"


# ------------------------------------------------------------
# Solution WITH try-except
# ------------------------------------------------------------

a = input("enter a number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
    else:
        print("end of loop")

except Exception as e:
    # Exception is the BASE class -- catches ANY type of exception
    # 'as e' stores the error message in variable e so you can print it
    print(f"Invalid Input: {e}")

print("end of code")   # this still runs even if exception occurred


# without 'as e' -- just print your own message, no error details:
# except:
#     print("Invalid Input")


# ------------------------------------------------------------
# Catching specific exceptions
# ------------------------------------------------------------
# You can have multiple except blocks for different error types.
# Python checks them TOP to BOTTOM and runs the FIRST match.
# Always put specific exceptions BEFORE the general Exception.

try:
    num = int(input("enter a number: "))    # ValueError if not an int
    b = [5, 6, 7]
    print(b[num])                           # IndexError if num > 2

except ValueError:
    print("invalid input -- please enter an integer")

except IndexError:
    print("index out of range -- list only has indices 0, 1, 2")

except Exception as e:
    # catches anything else that was not covered above
    print(f"unexpected error: {e}")


# ------------------------------------------------------------
# try-except with else
# ------------------------------------------------------------
# The else block runs ONLY if no exception was raised in try.
# Useful to separate the success logic from the error logic.

try:
    num = int(input("enter a number: "))
    result = 100 / num

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("please enter a valid integer")

else:
    # runs only if try succeeded with no errors
    print(f"result is {result}")


# ============================================================
#                     FINALLY KEYWORD
# ============================================================
# The finally block ALWAYS executes -- whether an error occurred or not.
# Used for cleanup tasks: closing files, closing DB connections, etc.
#
# SYNTAX:
#   try:
#       ...
#   except:
#       ...
#   finally:
#       # always runs
# ============================================================

try:
    lst = [1, 2, 3]
    i = int(input("enter an index: "))
    print(lst[i])

except:
    print("an error occurred")

finally:
    print("finally block -- always runs no matter what")


# ------------------------------------------------------------
# Why not just write code after try-except instead of finally?
# ------------------------------------------------------------
# For simple scripts, printing after the block works the same.
# But inside a FUNCTION, return exits immediately.
# Code after try-except inside a function never runs after return.
# finally is the ONLY way to guarantee execution inside a function.

# Without finally -- the last print never runs because return exits first:
def without_finally():
    try:
        lst = [1, 2, 3]
        i = int(input("enter an index: "))
        print(lst[i])
        return True
    except:
        print("an error occurred")
        return False

    print("this will NEVER run -- return already exited the function")


# With finally -- guaranteed to run even after return:
def with_finally():
    try:
        lst = [1, 2, 3]
        i = int(input("enter an index: "))
        print(lst[i])
        return True
    except:
        print("an error occurred")
        return False
    finally:
        # runs EVEN AFTER return -- this is finally's biggest advantage
        print("cleanup done -- always runs regardless of return or error")

x = with_finally()
print(x)


# ============================================================
#                     RAISE KEYWORD
# ============================================================
# Used to MANUALLY raise an exception yourself.
# Useful when you want to enforce rules or constraints.
# Works as a notification during debugging or production.
#
# SYNTAX:
#   raise ExceptionType("your custom message")
# ============================================================

a = int(input("enter a value between 5-9: "))

if a < 5 or a > 9:
    raise ValueError("value must be between 5 and 9")

# if the condition is met, Python raises a ValueError with your message
# and stops execution just like a normal exception would


# raise inside a try-except -- so you can handle your own raised error:
try:
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age cannot be negative")
    print(f"your age is {age}")

except ValueError as e:
    print(f"invalid age: {e}")


# ============================================================
#                    QUICK REFERENCE SUMMARY
# ============================================================
#
#  Keyword        Purpose
#  ──────────────────────────────────────────────────────────────────
#  try            Wrap code that might raise an exception
#  except         Handle the exception if it occurs
#  else           Runs only if NO exception occurred in try
#  finally        ALWAYS runs -- error or not, return or not
#  raise          Manually trigger an exception yourself
#
#  Common Built-in Exceptions:
#  ──────────────────────────────────────────────────────────────────
#  ValueError          Wrong value type (int("abc"))
#  IndexError          Index out of range (list[99])
#  KeyError            Key missing in dictionary
#  TypeError           Wrong type in operation ("2" + 2)
#  ZeroDivisionError   Dividing by zero (10 / 0)
#  FileNotFoundError   File does not exist
#  NameError           Variable used before being defined
#  Exception           Base class -- catches ALL exceptions
#
#  Rules and Tips:
#  ──────────────────────────────────────────────────────────────────
#  1. Always put specific exceptions BEFORE the general Exception
#  2. Use 'except Exception as e' to print the actual error message
#  3. Use finally for cleanup -- closing files, DB connections etc
#  4. finally is essential inside functions -- runs even after return
#  5. Use raise to enforce your own rules and constraints
#  6. Never use a bare except: without any type -- hides all errors
#  7. Custom exceptions using classes -- covered when studying OOP
#
# ============================================================