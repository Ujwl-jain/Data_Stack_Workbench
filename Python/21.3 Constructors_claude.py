# ============================================================
#                    CONSTRUCTORS IN PYTHON
# ============================================================
# A constructor is a special method used to create and
# initialize an object of a class.
#
# Python automatically calls the constructor every time
# an object is created -- we never call it manually.
#
# TYPES:
#   1. Default Constructor     -- no arguments
#   2. Parameterized Constructor -- accepts arguments
#
# Constructor method name is always: __init__()
# The double underscores mean it is a special Python method.
# ============================================================


# ============================================================
#           THE PROBLEM CONSTRUCTORS SOLVE
# ============================================================
# Without a constructor, values are assigned manually
# after every object creation.
# For 100 objects that means 200+ extra lines of code.

class Person:
    name       = "Harry"
    occupation = "Software Developer"

    def info(self):
        print(f"{self.name} is a {self.occupation}")

b = Person()
b.name       = "Shubh"       # manual assignment every time
b.occupation = "Manager"     # manual assignment every time
b.info()

# Constructors solve this -- values are passed at the time
# of object creation itself, no manual assignment needed.


# ============================================================
#              TYPE 1 -- PARAMETERIZED CONSTRUCTOR
# ============================================================
# Accepts arguments at the time of object creation.
# Values are initialized inside __init__() automatically.
# Preferred in real programs -- clean and scalable.

class Person:

    def __init__(self, n, o):
        print("Hi, I am a person.")  # runs automatically on object creation
        self.name       = n
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}")

b = Person("Harry", "Developer")
b.info()                    # Harry is a Developer

'''
Constructor workflow -- how it works internally:

When we write:
    b = Person("Harry", "Developer")

Python automatically calls:
    Person.__init__(b, "Harry", "Developer")

So internally:
    self = b          <- Python passes the object itself as self
    n    = "Harry"
    o    = "Developer"

We never pass self manually -- Python handles it.

Inside __init__():
    self.name       = n   means   b.name       = "Harry"
    self.occupation = o   means   b.occupation = "Developer"

Values are now stored inside object b.

It works like a function in that it accepts parameters,
but unlike a function, we never call it -- Python calls it
automatically the moment an object is created.
'''


# ============================================================
#              TYPE 2 -- DEFAULT CONSTRUCTOR
# ============================================================
# Takes no arguments.
# Runs automatically on object creation but does not
# initialize any values -- those are still assigned manually.
# Useful when you want to perform a task on every object
# creation without needing any input.

class Person:

    def __init__(self):
        print("Hi, I am a person.")  # runs automatically, no arguments needed

    def info(self):
        print(f"{self.name} is a {self.occupation}")

b = Person()
b.name       = "Shubh"     # still assigned manually after creation
b.occupation = "Manager"
b.info()                    # Shubh is a Manager

# WARNING: if b.info() is called without setting b.name and
# b.occupation first, Python raises AttributeError because
# __init__() never initialized them.
# This is why parameterized constructor is preferred --
# values are guaranteed to exist the moment the object is created.


# ============================================================
#          DEFAULT vs PARAMETERIZED -- SIDE BY SIDE
# ============================================================
#
#                    Default           Parameterized
#  ──────────────────────────────────────────────────────────────
#  Arguments         None              Takes values at creation
#  Values set        Manually after    Inside __init__ automatically
#  Risk              AttributeError    Values always guaranteed
#  100 objects       200 manual lines  100 clean one-liners
#  Use when          No input needed   Values differ per object


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Term              Meaning
#  ──────────────────────────────────────────────────────────────
#  __init__()        Constructor -- special method, auto-called on creation
#  self              Reference to the object being created
#  self.name = n     Stores value n inside the object as property 'name'
#
#  Internally what Python does:
#  ──────────────────────────────────────────────────────────────
#  b = Person("Harry", "Dev")
#  -> Person.__init__(b, "Harry", "Dev")
#  -> self = b, values stored inside b
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Constructor is always named __init__() -- cannot change this
#  2. self is always the first parameter -- Python passes it automatically
#  3. Constructor is called automatically -- never call __init__() manually
#  4. Parameterized constructor preferred -- values guaranteed at creation
#  5. Default constructor + no manual assignment = AttributeError risk
#
# ============================================================