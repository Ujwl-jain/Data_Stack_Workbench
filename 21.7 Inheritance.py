# ============================================================
#                   INHERITANCE IN PYTHON
# ============================================================
# Inheritance allows a class to acquire all properties and
# methods of another class.
#
# TWO TERMS:
#   Parent class (Base class)  -- the class being inherited FROM
#   Child class (Sub class)    -- the class that inherits
#
# WHY USE IT:
#   Avoid rewriting the same code in multiple classes.
#   Child gets everything parent has, plus its own extras.
#
# SYNTAX:
#   class Child(Parent):
#       ...
#
# REAL WORLD ANALOGY:
#   Employee is the parent -- has general properties (name, id)
#   Programmer is a child -- is an employee BUT also has extra
#   properties specific to programmers (language, etc.)
# ============================================================


# ============================================================
#                  PARENT CLASS
# ============================================================

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id   = id

    def showdetails(self):
        print(f"Name: {self.name}, ID: {self.id}")


e1 = Employee('Rohan', 240)
e1.showdetails()            # Name: Rohan, ID: 240

e2 = Employee('Ron', 10)
e2.showdetails()            # Name: Ron, ID: 10


# ============================================================
#                  CHILD CLASS
# ============================================================
# Programmer inherits from Employee.
# Gets showdetails() automatically -- no need to rewrite it.
# Also has its own method showlanguage() on top.

class Programmer(Employee):
    def showlanguage(self):
        print("The default language is Python")


# child can use parent methods:
e3 = Programmer('Han', 40)
e3.showdetails()            # Name: Han, ID: 40   <- inherited from Employee
e3.showlanguage()           # The default language is Python <- own method

# parent CANNOT use child methods:
e4 = Employee('Ron', 10)
# e4.showlanguage()         # AttributeError -- Employee has no showlanguage()

'''
All functions in the parent class are accessible in the child class.
But functions of the child class are NOT accessible from the parent class.

Employee cannot use showlanguage()
Programmer can use showdetails() AND showlanguage()
'''


# ============================================================
#            WHAT CHILD GETS FROM PARENT -- SUMMARY
# ============================================================
#
#              showdetails()    showlanguage()
#  ──────────────────────────────────────────
#  Employee         YES              NO
#  Programmer       YES (inherited)  YES (own)
#
# Think of it as:
#   Every Programmer IS an Employee -- so they get everything.
#   But not every Employee IS a Programmer -- so they get nothing extra.


# ============================================================
#                  TYPES OF INHERITANCE
# ============================================================
# (To be completed once learned)
#
# 1. Single      -- one child, one parent (shown above)
# 2. Multiple    -- one child, multiple parents
# 3. Multilevel  -- child of a child (grandparent -> parent -> child)
# 4. Hierarchical-- multiple children from one parent
# 5. Hybrid      -- combination of above types
# ============================================================
