# ============================================================
#                  ACCESS MODIFIERS IN PYTHON
# ============================================================
# Access modifiers control WHO can access a class variable
# or method -- inside the class, subclass, or from outside.
#
# OTHER LANGUAGES (Java, C++) enforce these strictly.
# PYTHON does NOT enforce them -- they are just conventions.
# Nothing physically stops you from accessing anything.
# The underscore is just a signal to other programmers:
# "you are not supposed to touch this directly."
#
# THREE TYPES:
#   Public    -- accessible everywhere (default)
#   Protected -- accessible inside class and subclass only (_name)
#   Private   -- accessible inside class only (__name)
# ============================================================


# ============================================================
#                      PUBLIC
# ============================================================
# Default for all variables and methods in Python.
# No underscore -- accessible from anywhere.
# Inside class, outside class, in subclass -- no restrictions.

class Employee:
    def __init__(self):
        self.name = 'Harry'     # public -- no underscore

a = Employee()
print(a.name)                   # Harry  <- accessible from outside, no issue


# ============================================================
#                      PROTECTED
# ============================================================
# Single underscore prefix: _name
# Convention means: "accessible inside class and subclass only."
# Python does NOT enforce this -- you CAN still access it from
# outside, but the underscore signals you should not.
#
# No name mangling needed -- can be accessed directly.
# Commonly used in inheritance to share between parent and child.

class Student:
    def __init__(self):
        self._name = 'Harry'        # protected attribute

    def _funName(self):             # protected method
        return 'Code with Harry'

class Subject(Student):             # child class
    pass

obj  = Student()
obj1 = Subject()

# accessible from student object:
print(obj._name)        # Harry
print(obj._funName())   # Code with Harry

# accessible from subject object (inherited):
print(obj1._name)       # Harry  <- inherited from Student
print(obj1._funName())  # Code with Harry  <- inherited from Student

# technically accessible from outside too -- Python won't stop you:
# print(obj._name)      # works, but convention says don't do this


# ============================================================
#                       PRIVATE
# ============================================================
# Double underscore prefix: __name
# Convention means: "accessible inside this class only."
# Python partially enforces this using NAME MANGLING --
# it internally renames __name to _ClassName__name.
# This makes direct access harder but not impossible.

class Employee:
    def __init__(self):
        self.__name = 'Harry'   # private -- double underscore

a = Employee()

# print(a.__name)               # AttributeError -- cannot access directly
print(a._Employee__name)        # Harry  <- name mangling workaround

# NAME MANGLING explained:
# Python renames self.__name to self._Employee__name internally.
# So __name appears to not exist when accessed from outside.
# But using _ClassName__variable you can still reach it.
# This is why protected (_name) is generally preferred over
# private (__name) -- no mangling needed, cleaner to work with.


# ============================================================
#         ACCESSING PRIVATE INSIDE THE CLASS -- CORRECT WAY
# ============================================================
# Private variables SHOULD be accessed from outside using
# a public method inside the class -- not name mangling.
# This is the proper OOP approach.

class Employee:
    def __init__(self):
        self.__name = 'Harry'

    def get_name(self):         # public method to expose private value
        return self.__name      # inside class -- can access __name directly

a = Employee()
print(a.get_name())             # Harry  <- clean, no mangling needed


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#  Type       Syntax     Accessible From              Enforced?
#  ──────────────────────────────────────────────────────────────
#  Public     name       Everywhere                   N/A
#  Protected  _name      Class + Subclass (convention) No
#  Private    __name     Class only (convention)       Partially
#
#  Access from different locations:
#  ──────────────────────────────────────────────────────────────
#                    Public    Protected    Private
#  Inside class       YES        YES          YES
#  Subclass           YES        YES          NO
#  Outside class      YES        NO*          NO*
#                              (*convention, not enforced)
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. Python does NOT enforce access modifiers -- all are conventions
#  2. Single underscore  _name  = "don't touch from outside" signal
#  3. Double underscore __name  = name mangling kicks in
#     renamed to _ClassName__name internally
#  4. Protected is preferred over private in Python --
#     cleaner, no mangling, works well with inheritance
#  5. Correct way to expose private = public method inside class
#     not name mangling from outside
#
# ============================================================
