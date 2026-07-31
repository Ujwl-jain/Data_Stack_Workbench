# ============================================================
#          INSTANCE VARIABLES vs CLASS VARIABLES
# ============================================================
#
# INSTANCE VARIABLE:
#   - Defined inside __init__ using self
#   - Belongs to a specific object (instance)
#   - Each object has its OWN copy -- changing one does not affect others
#
# CLASS VARIABLE:
#   - Defined directly inside the class, outside __init__
#   - Belongs to the CLASS itself -- shared across ALL instances
#   - Acts as a default -- used by all objects unless they
#     override it with their own instance variable
#
# LOOKUP ORDER (how Python finds a variable):
#   Python checks the INSTANCE first.
#   If not found on the instance, checks the CLASS.
#   This is why class variable acts as a default.
# ============================================================


class MyClass:
    companyname = 'Apple'       # CLASS variable -- shared by all instances

    def __init__(self, name):
        self.name         = name    # INSTANCE variable -- unique per object
        self.raise_amount = 0.02    # INSTANCE variable -- unique per object

    def showdetails(self):
        print(f"Name: {self.name} | Raise: {self.raise_amount} | Company: {self.companyname}")


emp1 = MyClass('Harry')
emp2 = MyClass('Rohan')

# before any changes:
emp1.showdetails()  # Name: Harry | Raise: 0.02  | Company: Apple
emp2.showdetails()  # Name: Rohan | Raise: 0.02  | Company: Apple


# ============================================================
#                  CHANGING INSTANCE VARIABLE
# ============================================================
# Changing on emp1 only affects emp1 -- emp2 is untouched.

emp1.raise_amount = 0.3         # creates instance variable on emp1 only
emp1.showdetails()  # Name: Harry | Raise: 0.3   | Company: Apple
emp2.showdetails()  # Name: Rohan | Raise: 0.02  | Company: Apple  <- unchanged


# ============================================================
#         OVERRIDING CLASS VARIABLE ON ONE INSTANCE
# ============================================================
# When you do emp1.companyname = 'Apple India', Python creates
# a NEW instance variable on emp1 that shadows the class variable.
# The class variable itself is untouched -- emp2 still sees 'Apple'.

emp1.companyname = 'Apple India'    # instance variable created on emp1 only
emp1.showdetails()  # Name: Harry | Raise: 0.3   | Company: Apple India
emp2.showdetails()  # Name: Rohan | Raise: 0.02  | Company: Apple  <- still class default

# LOOKUP happening here:
# emp1.companyname -> found on emp1 instance -> 'Apple India'
# emp2.companyname -> NOT on emp2 instance -> goes to class -> 'Apple'


# ============================================================
#            CHANGING CLASS VARIABLE FOR ALL INSTANCES
# ============================================================
# Change on the CLASS itself -- affects ALL instances that have
# not overridden it with their own instance variable.

MyClass.companyname = 'Google'
emp1.showdetails()  # Name: Harry | Raise: 0.3   | Company: Apple India
                    # emp1 has its OWN companyname -- class change ignored
emp2.showdetails()  # Name: Rohan | Raise: 0.02  | Company: Google
                    # emp2 has no own companyname -- sees class change


# ============================================================
#              HOW self WORKS -- TWO IDENTICAL CALLS
# ============================================================
# These two lines do the exact same thing:

emp1.showdetails()              # Python automatically passes emp1 as self
MyClass.showdetails(emp1)       # manually passing emp1 as self

# When you call emp1.showdetails(), Python converts it internally to
# MyClass.showdetails(emp1) -- self is always the object being used.
# You never pass self manually -- Python handles it automatically.


# ============================================================
#                   QUICK REFERENCE SUMMARY
# ============================================================
#
#                    Instance Variable      Class Variable
#  ──────────────────────────────────────────────────────────────
#  Defined in        __init__ with self     directly in class body
#  Belongs to        specific object        the class itself
#  Shared?           No -- unique per obj   Yes -- all instances share it
#  Change affects    only that object       all instances (unless overridden)
#  Acts as           object's own data      shared default for all
#
#  Lookup order:
#  ──────────────────────────────────────────────────────────────
#  Python checks INSTANCE first -> then CLASS
#  If found on instance -> uses that
#  If not found on instance -> falls back to class variable
#
#  Rules:
#  ──────────────────────────────────────────────────────────────
#  1. obj.var = x on an instance creates an instance variable
#     that SHADOWS the class variable -- class variable unchanged
#  2. ClassName.var = x changes the class variable for ALL
#     instances that have not overridden it
#  3. emp1.showdetails() and MyClass.showdetails(emp1) are identical
#     Python always passes the object as self automatically
#  4. Use class variables for data shared across all objects
#     Use instance variables for data unique to each object
#
# ============================================================
