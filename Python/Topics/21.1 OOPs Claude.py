# ============================================================
#          OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
# ============================================================
# OOP is a way of writing code by mapping it to real world
# scenarios using objects and classes.
#
# TWO STYLES OF PROGRAMMING:
#
#   Procedural -- code runs top to bottom using functions and loops.
#                 Good for simple, linear tasks.
#                 Example: pandas operations, loops, functions.
#
#   OOP        -- code is organized around real world entities.
#                 Good for large programs that need to be maintained,
#                 extended, and understood by multiple people.
#                 Example: a Bank system, an E-commerce app.
#
# REAL WORLD ANALOGY:
#   Railway form  -> CLASS   (the blueprint -- same form for everyone)
#   Harry's form  -> OBJECT  (one filled instance of the form)
#   Tom's form    -> OBJECT  (another filled instance of the same form)
#
# The form (class) is created once.
# Each person (object) fills it with their own data.
#
# 4 MAIN FEATURES OF OOP (covered separately in detail):
#   1. Encapsulation
#   2. Access Modifiers
#   3. Polymorphism
#   4. Inheritance
# ============================================================


# ============================================================
#         PROCEDURAL vs OOP -- THE PROBLEM OOP SOLVES
# ============================================================

# Procedural way -- separate variables for each person:
# rajeev_sales  = 6000
# rajeev_profit = 3000
# rajeev_ad     = 1000
#
# raj_sales  = 6000
# raj_profit = 2000
# raj_ad     = 500
#
# PROBLEM: as the number of people grows, variables multiply.
# Hard to manage, easy to confuse rajeev_profit with raj_profit.
# No structure -- just a pile of loose variables.
#
# OOP way -- one class, many objects, each carries its own data.
# Clean, organized, and scalable.


# ============================================================
#                     CLASS AND OBJECT
# ============================================================
# CLASS  -- the blueprint. Defines what properties and methods
#           an entity will have. Written once.
#
# OBJECT -- a specific instance created FROM the class.
#           Each object has its own copy of the properties.
#           You can create as many objects as you need from one class.
#
# SYNTAX:
#   class ClassName:
#       property = default_value
#
#   object_name = ClassName()   <- creating an object (instance)
# ============================================================

class Person:
    name       = "Harry"    # default value
    occupation = "SD"       # default value
    worth      = 10         # default value

a = Person()
print(a.name)               # Harry  <- uses default from class

a.name       = 'Shubh'
a.occupation = 'Manager'
print(a.name, a.occupation) # Shubh Manager

# NOTE: changing a.name only affects object 'a'
# the class default "Harry" is still there for any new object
b = Person()
print(b.name)               # Harry  <- b still uses class default

'''
If you specifically mention the name that is not in the class it will print it
else it will print which is mentioned in the class.
You can try it by commenting the above 2 lines.
That is the simple analogy of how class works.
'''


# ============================================================
#                   METHODS INSIDE A CLASS
# ============================================================
# A method is a function defined inside a class.
# It defines the BEHAVIOUR of the class -- what it can do.
# Methods always take 'self' as the first parameter.

'''
Workflow of how class works:

we create a class, inside it we create multiple methods or functions.

then we can use an object of any name and store that class inside it,
and call its method to perform certain functions.
its like creating a copy of the class blueprint and storing it in a variable, so that variable can use everything the class has.

Below, person gets stored into b and with b we perform the function which is in class.
'''

class Person:
    name       = "Harry"
    occupation = "SD"
    worth      = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

b = Person()
b.name       = 'Shubh'
b.occupation = 'Manager'
b.info()                    # Shubh is a Manager


# ============================================================
#                      self KEYWORD
# ============================================================
# 'self' is a reference to the current instance of the class,
# used to access variables that belong to the class.

'''
From the example: the object for which a particular method is being called.

here if b object calls the method info(), it will print Shubh and Manager.
vice versa for c object it will print XYZ and ABC.

values inside classes are default values,
in case the object does not provide any input.
'''

class Person:
    name       = "Harry"    # class-level default
    occupation = "SD"
    worth      = 10

    def info(self):
        # self.name refers to THIS object's name, not the class default
        print(f"{self.name} is a {self.occupation}")

b = Person()
b.name       = 'Shubh'
b.occupation = 'Manager'

c = Person()
c.name       = 'XYZ'
c.occupation = 'ABC'

b.info()    # Shubh is a Manager  <- self = b here
c.info()    # XYZ is a ABC        <- self = c here

# same method, different output -- because self points to different objects

'''
In the end, class is like a common code with multiple functionality
that works for multiple instances or objects.

Railway form is the example we can understand it by.
Form is one but the filler is uncertain.

here form  = class
     filler = objects that will use the class
'''


# ============================================================
#              HOW A CLASS WORKS -- FULL PICTURE
# ============================================================
#
# STEP 1: Define the class (the blueprint)
#         class Person: ...
#
# STEP 2: Create objects from the class
#         b = Person()   c = Person()
#
# STEP 3: Each object gets its own copy of the class properties
#         b.name = 'Shubh'   c.name = 'XYZ'
#
# STEP 4: Call methods on objects -- self handles the right data
#         b.info() -> uses b's name and occupation
#         c.info() -> uses c's name and occupation
#
# Think of it as:
#   Class  = the form (template, same for everyone)
#   Object = a filled form (unique per person)
#   Method = what you can DO with that form
#   self   = "my own data" when the method runs


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Term        Meaning
#  ──────────────────────────────────────────────────────────────
#  Class       Blueprint -- defines properties and methods
#  Object      Instance of a class -- has its own data
#  Property    Variable inside a class (name, age, etc.)
#  Method      Function inside a class (what the object can do)
#  self        Reference to the current object calling the method
#  Instance    Another word for object
#
#  Syntax:
#  ──────────────────────────────────────────────────────────────
#  class MyClass:          define a class
#  obj = MyClass()         create an object (instantiate)
#  obj.property            access a property
#  obj.method()            call a method
#  def method(self):       define a method inside class
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Class name convention is PascalCase -- Person not person
#  2. Every method inside a class must have self as first parameter
#  3. Changing obj.property only affects that object -- class default unchanged
#  4. Multiple objects can be created from one class -- each independent
#  5. self is convention not a keyword -- but always use self
#
# ============================================================